/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x){

if (x < 0) return false
if (x % 10 === 0 && x !== 0 ) return false


let reverse = 0
let n = x

console.log(`starting reversal for x = ${x}`)

// step 1 create the reverse of x 
while (n >= 1 ) {

    let remainder = n % 10
    n = Math.floor(n/10)
    reverse = reverse * 10 + remainder

    console.log(remainder)
    console.log(`new n: ${n}`)
    console.log(`reverse: ${reverse}`)
}

// step 2 compare reverse to x
    
    return reverse === x
}

console.log(isPalindrome(121))