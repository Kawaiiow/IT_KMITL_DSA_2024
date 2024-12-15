"""Swap"""

def convert_string_to_tuples(text_in):
  """tuple"""
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

def main() -> None :
    """void"""
    laongdao_data = convert_string_to_tuples(input())
    print(f"{laongdao_data[1], laongdao_data[0]}")
    # print("(", end="")
    # if laongdao_data[1].is_integer:
    #     print(f"{laongdao_data[1]:.1f}", end="")
    # else:
    #     print(laongdao_data[1], end="")
    # print(", ", end="")
    # if laongdao_data[0].is_integer:
    #     print(f"{laongdao_data[0]:.1f}", end="")
    # else:
    #     print(laongdao_data[0], end="")
    # print(")", end="")
main()
