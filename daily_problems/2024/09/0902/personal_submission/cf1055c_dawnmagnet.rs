fn gcd(a: i32, b: i32) -> i32 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}
fn main() {
    input! {mut la: i32, mut ra: i32, ta: i32}
    input! {mut lb: i32, mut rb: i32, tb: i32}

    let g = gcd(ta, tb);
    if ra - la > rb - lb {
        //swap a & b
        swap(&mut la, &mut lb);
        swap(&mut ra, &mut rb);
    }
    // make lb >= la and minimize lb
    let diff = lb - la;
    let part = diff / g;
    let lb = lb - part * g;
    let rb = rb - part * g;
    // calculate the intersection of [la, ra] and [lb, rb]
    let mut cal = |a: i32, b: i32, c: i32, d: i32| {
        let l = a.max(c);
        let r = b.min(d);
        0.max(r - l + 1)
    };
    let r1 = cal(la, ra, lb, rb);
    let r2 = cal(la, ra, lb - g, rb - g);
    println!("{}", r1.max(r2));
}