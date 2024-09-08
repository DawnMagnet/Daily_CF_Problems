fn main() {
    input! {a: usize, b: usize, k: usize}
    let j = 1_000_000_000 % k;

    if b >= k {
        println!("2");
        return;
    }
    let mut ct = vec![false; k];
    for i in 0..=a {
        let m = (i * j) % k;
        // println!("{}", m);

        if ct[m] {
            println!("2");
            return;
        }
        ct[m] = true;

        if m == 0 {
            continue;
        }
        let p = k - m;
        if p > b {
            // format into 000001(9digits)
            println!("1 {:09}", i);
            exit(0);
        }
    }
    println!("2");
}