fn fik(n: u16) -> u16 { // varian tipe data // nama func gk ngaruh
    if n <= 2 {
        return 1;
    } else {
        return fik(n - 1) + fik(n - 2);
    }
}

fn main() {
    let n = 19;
    println!("fik({n}) = {}", fik(n));
    //the result is  fik(19) = 4181
}