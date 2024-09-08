fn inter() -> usize {
    flush! {};
    input! { x: usize }
    x
}
fn main() {
    input! {n: usize, k: usize}
    let mut real = vec![vec![0; n]; n];

    let mut reflect = vec![0];
    for i in 0..5 {
        let ri = i * 2;
        let rk = 1 << ri;
        for item in reflect.clone().into_iter().rev() {
            reflect.push(rk + item);
        }
    }
    for i in 0..n {
        for j in 0..n {
            // gray code
            real[i][j] = (reflect[i] * 2) ^ (reflect[j]);
        }
    }
    for i in 0..n {
        for j in 0..n - 1 {
            print!("{} ", real[i][j] ^ real[i][j + 1]);
        }
        println!();
    }
    for i in 0..n - 1 {
        for j in 0..n {
            print!("{} ", real[i][j] ^ real[i + 1][j]);
        }
        println!();
    }
    let mut pos = HashMap::new();
    for i in 0..n {
        for j in 0..n {
            pos.insert(real[i][j], (i, j));
        }
    }
    let mut cur = 0;
    for i in 0..k {
        cur ^= inter();
        let (x, y) = pos[&cur];
        print!("{} {}\n", x + 1, y + 1);
    }
}