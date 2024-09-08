fn merge(v: &mut [usize], k: &mut usize) {
    if *k >= 2 && v.len() >= 2 {
        *k -= 2;
        let mid = v.len() / 2;
        // println!("{:?}", v);
        v.rotate_right(mid);
        // println!("{:?} {:?} {:?}", v, &v[..mid], &v[mid..]);

        merge(&mut v[..mid], k);
        merge(&mut v[mid..], k);
    }
}
fn main() {
    input! { n: usize, mut k: usize }
    let mut v = (1..=n).collect::<Vec<_>>();
    if k % 2 == 0 {
        println!("-1");
        return;
    }
    k -= 1;
    merge(&mut v, &mut k);
    if k == 0 {
        println!(
            "{}",
            v.iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        );
    } else {
        println!("-1");
    }
}