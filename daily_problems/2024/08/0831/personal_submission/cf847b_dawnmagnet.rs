fn main() {
    input! { n: usize, a: [usize; n] };

    let mut res = vec![vec![a[0]]];
    for i in 1..n {
        let mut l = 0;
        let mut r = res.len() - 1;
        while l < r {
            let mid = (l + r) / 2;
            if res[mid].last().unwrap() < &a[i] {
                r = mid;
            } else {
                l = mid + 1
            }
        }
        if res[l].last().unwrap() < &a[i] {
            res[l].push(a[i]);
        } else {
            res.push(vec![a[i]]);
        }
        // eprintln!("{:?}", res);
    }
    for t in res {
        for it in t {
            print!("{} ", it);
        }
        println!();
    }
}