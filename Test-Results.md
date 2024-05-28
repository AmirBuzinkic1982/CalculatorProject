Test-Results
# Test Results

## Black Box Testing

### Test Cases

1. **Input**: `4+5`
   - **Expected Output**: `9.0`
   - **Actual Output**: `9.0`
   - **Result**: Pass

2. **Input**: `10+5*4+3`
   - **Expected Output**: `33.0`
   - **Actual Output**: `33.0`
   - **Result**: Pass

3. **Input**: `-3+2*5`
   - **Expected Output**: `7.0`
   - **Actual Output**: `7.0`
   - **Result**: Pass

4. **Input**: `5/0`
   - **Expected Output**: `ERROR` (or handle division by zero)
   - **Actual Output**: `ERROR`
   - **Result**: Pass

### Observations and Issues

- Observed an issue when input contains invalid characters: the program returns `ERROR`.
- Division by zero is correctly handled and returns `ERROR`.
- ...

## Unit Testing

### Method: `Calculate`

- **Test Case**: `Calculate([3, 2], ['*'])`
  - **Expected Output**: `6.0`
  - **Actual Output**: `6.0`
  - **Result**: Pass

- **Test Case**: `Calculate([10, 5, 4, 3], ['+', '*', '+'])`
  - **Expected Output**: `33.0`
  - **Actual Output**: `33.0`
  - **Result**: Pass

- **Test Case**: `Calculate([7, 0], ['/'])`
  - **Expected Output**: `ERROR` (handle division by zero)
  - **Actual Output**: `ERROR`
  - **Result**: Pass
