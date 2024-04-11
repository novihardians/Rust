static mut DET_COLLATZ: Vec<u32> = vec![]; // global variabel for ARRAY

fn collatz_seq(n: u32) -> u32 {

    if n == 1 {
        // unsafe means getting mutable static
        unsafe {
            println!("{:?}", DET_COLLATZ);
        }
        return 1; // syarat (n: u32)
    } else if n % 2 == 0 { 

        // iseng cetak array
        let _a =  n / 2; // a = (if this is intentional, prefix it with an underscore: `_a`)
        unsafe {
            DET_COLLATZ.push(_a);
            // println!("{:?}", DET_COLLATZ);
        }

        return collatz_seq( n/2 );  // karena rumus ini jadi sulit eksekusinya
    } else { 

        // iseng cetak array
        let _a =  3 * n + 1;
        unsafe {
            DET_COLLATZ.push(_a);
            // println!("{:?}", DET_COLLATZ);
        }

        return collatz_seq( (3*n)+1 );
    }   
}

fn main() {
    println!("{:?}", collatz_seq(15));
}