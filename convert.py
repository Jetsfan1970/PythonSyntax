def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
  
    if unit_in != "f" and unit_in != "c":
        return f"Invalid unit {unit_in}"

    if unit_out != "f" and unit_out != "c":
        return f"Invalid unit {unit_out}"
      
    if unit_in == "f" and unit_out == "c":
      print((temp - 32) / 1.8)
    
    elif unit_in == "c" and unit_out == "f":
      print((temp * 1.8) + 32)
      
    return temp
      

