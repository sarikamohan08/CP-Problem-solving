CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select  distinct salary as getNthHighestSalary 
      from Employee as e1
      where N-1=(select count(distinct salary)
                 from Employee as e2
                 where e2.salary > e1.salary)
      
  );
END