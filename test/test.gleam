import gleam/io
import gleam/string

pub fn main() {
  let _name: String = "Gleam"

  let _is_cool: Bool = True

  let _version: Int = 1 * 10
  let counts = 10

  io.debug(string.drop_left(string.drop_right("Hello, Joe!", 1), 7))

  // With the pipe operator
  "Hello, Mike!"
  |> string.drop_right(1)
  |> string.drop_left(7)
  |> io.debug

  // Changing order with function capturing
  "1"
  |> string.append("2")
  |> string.append("3", _)
  |> io.debug
}
