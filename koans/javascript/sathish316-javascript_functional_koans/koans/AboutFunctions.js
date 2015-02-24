  describe("Functions", function(){

    describe("As First class objects", function(){

      it("can be assigned to var", function(){
        function add(a, b){
          return a + b;
        }
        expect(add(2, 3)).toEqual(5);

        // Int and Strings are first class objects in a language and can
        // be assigned to var. Similary functions can be assigned to vars
        var multiply = function(a, b){
          return a * b;
        }
        expect(multiply(2,3)).toEqual(FILL_ME_IN);
      });

      it("can be passed as argument to another function", function(){
        function calculate(operation, a, b){
          return operation(a, b);
        }
        var add = function(a, b){ return a + b}
        var multiply = function(a, b) { return a * b}

        expect(calculate(add, 5, 10)).toEqual(FILL_ME_IN);
        expect(calculate(multiply, 5, 10)).toEqual(FILL_ME_IN);
      });

      it("can be returned from other functions", function(){
        function greeter(){
          return function(name){
            return "Hello " + name;
          }
        }
        var hello = greeter();

        expect(hello("Jack")).toEqual(FILL_ME_IN);
      });


    });
  });
