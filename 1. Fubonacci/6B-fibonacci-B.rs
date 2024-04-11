fn fik(n: u16) -> u16 { // varian tipe data // nama func gk ngaruh
    if n <= 2 {
        return 3;
    } else {
        return 10;
    }
}

fn main() {
    let n = 19;
    println!("fik({n}) = {}", fik(n));
    // the result is  10
}