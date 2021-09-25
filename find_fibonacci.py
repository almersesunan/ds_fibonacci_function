def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    a = 1
    b = 1
    while True: #Looping sampai ketemu return
      if x == 0:
        return True
      elif b <= x:
        if b == x:
          return True
        else:
          temp = b
          b = b + a
          a = temp
      else:
        return False

if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
