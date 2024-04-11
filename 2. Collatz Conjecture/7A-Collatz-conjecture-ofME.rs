fn collatz(n: u32) -> u32 { // function for loop, every condition must have a return
    if n == 1 {
        return 1;
    } else if n%2 == 0 { // even (genap) formula
        if  n/2 != 1 { print!( "{} ", n/2 ); } // tolak print double 1
        return collatz( n/2 ); // kembali ke function
    } else { // odd (ganjil)
        print!( "{} ", (3*n)+1 );
        return collatz( (3*n)+1 ); // kembali ke function
    }
}

fn main() {
    let n = 8;
    print!( "{} ", n);
    println!("{}", collatz(n));
}