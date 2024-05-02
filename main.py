from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Girl dancing in the forest", negative_prompt="spoon", model_type="art")
print(result.description) # Description about the generated images # >>> Shrek devouring planet Earth with a sinister grin
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path