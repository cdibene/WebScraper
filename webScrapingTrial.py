from bs4 import BeautifulSoup

html_doc ="""
<!DOCTYPE html>
<html lang="en">
    <head>
        <metacharset="UTF-8"/>
        <meta name="viewport" content="width=device-width,intial-scale=1.0"/>
        <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
        <title>My Webpage</title>
    </head>
    <body>
        <div id="section-1">
            <h3 data-hello="hi">Hello</h3>
            <img src="https://source.unspalsh.com/200x200/?nature,water"/>
            <p>
            Lorem ipsum dolor sit amet, est rebum exerci cu, ea rationibus adversarium 
            vituperatoribus sit. Dicunt vivendo nominavi at vix, harum lobortis honestatis 
            mei ex. Eu his dicta commune, per ut omnesque vivendum pertinax. Idque elitr 
            voluptatibus ad mei, quidam facilis antiopam vis id. Solet graece integre ea 
            mei, nec legendos comprehensam ad.
            </p>
        </div>
        <div id="section-2">
            <ul class="items">
                <li class="item"><a href="#">Item 1</a></li>
                <li class="item"><a href="#">Item 2</a></li>
                <li class="item"><a href="#">Item 3</a></li>
                <li class="item"><a href="#">Item 4</a></li>
                <li class="item"><a href="#">Item 5</a></li>
            </ul>
        </div>    
    </body>
</html>
"""

soup = BeautifulSoup(html_doc,'html.parser')

#Direct Find
#Unconevential method, usually using find() but this will directly find and print what is attached
#to the soup method

#print(soup.body) prints the body of the website html
#print(soup.head) prints the head of the website html and so on and so forth

#find() find the first match for a pattern. findall() finds *all* the matches
#setting a variable to print the first div
#el = soup.find('div')
#printing using the proper method stored in el
#if we want to find the secon div, utilize el = soup.findAll('div')[1]

#find_all() or findAll() for all divs
#el = soup.findAll('div')

#returns the id of the first section
#el = soup.find(id='section-1')

#finding classes will normally give you a syntax error bc it is a reserved word
#el = soup.find(class='items')
#to fix this, add an underscore
#el = soup.find(class_='items')

#will return the json object
#el = soup.find(attrs={"data-hello": "hi"})

#select 
#this will us to select by css 
#el = soup.select('#section-1') #will return the id of section1
#el = soup.select('.item')[0] #returns first item

#get_text() is what you actually want
#will grab the text values of what you are looking for 
#item grabs 1, items grabs them all
#el = soup.find(class_="item").get_text() #grabs the text of the first item

#loop to print all text values in items
#for item in soup.select('.item'):
    #print(item.get_text())

#Navigation
#returns a list including new lines looked at as items so [0] will give you nothing 
#because it is viewed as a new line
#el = soup.body.contents[0]
#el = soup.body.contents[1] will actually give you the first contents of the body section 1
#el = soup.body.contents[1].contents[1] #gives you the h3 
#el = soup.body.contents[1].contents[1].find_next_sibling() #gives you the sibling after h3 
#el = soup.find(id='section-2').find_previous_sibling() #gives you section-1
#el = soup.find(class_='item').find_parent() #gives you the parent of the class
#can also pass in parameters for next sibling function
el = soup.find('h3').find_next_sibling('p') #returns the paragraph

print(el)