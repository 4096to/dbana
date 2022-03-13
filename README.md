# Summary

Simple python script that permit a simple analysis of a database (most used emails, most used passwords, etc).

## Requierements

Python 3.0 or + with time, sys and os modules.\
Grep

## Installation

If you don't have it install [ripgrep](https://github.com/BurntSushi/ripgrep) \
Use the package manager [pip](https://pip.pypa.io/en/stable/).
```bash
pip install time
pip install sys
pip install os
```

## CLI usage

```python
# With filename the database file name and extension
python dbana.py filename
```

## Sample output

Using Black-Gen_data_users.sql leaked database as an example.
```python
python dbana.py Black-Gen_data_users.sql
```
```python
---------------------------------------------------------------
>====>     >=>>=>          >>       >==>    >=>       >>       
>=>   >=>  >>   >=>       >>=>      >> >=>  >=>      >>=>      
>=>    >=> >>    >=>     >> >=>     >=> >=> >=>     >> >=>     
>=>    >=> >==>>=>      >=>  >=>    >=>  >=>>=>    >=>  >=>    
>=>    >=> >>    >=>   >=====>>=>   >=>   > >=>   >=====>>=>   
>=>   >=>  >>     >>  >=>      >=>  >=>    >>=>  >=>      >=>  
>====>     >===>>=>  >=>        >=> >=>     >=> >=>        >=> 
Analysis of : Black-Gen_data_users.sql launched...
---------------------------------------------------------------
Number of lines :
13940
---------------------------------------------------------------
Number of generated passwords :
0
0
Passwords are likelly hashed, cant proceed this analysis.
---------------------------------------------------------------
Most used emails count :
Gmail :
9976
Hotmail :
390
Yahoo :
114
Protonmail :
47
Riseup :
1
---------------------------------------------------------------
Admins account informations :
(2001, 'admin', 'bc25ca38f20515fda071104b7bef3d7eac2bb201', 'hinoxim@poly-swarm.com', 0, 0, 0, 0, '0', 0, 0, 0, 0, ''),
(8673, 'BlackGenAdmin', 'e4aa41b1118ffe1402949d02913fce8d4dbf3929', 'BlackGenAdmin@yopmail.com', 0, 0, 0, 0, '0', 0, 0, 0, 0, '0'),
(11393, 'adminx', 'ad3ef606e31a088e75332f6d44b8ac37a894c1a0', 'admin@gmail.com', 0, 0, 0, 0, '0', 0, 0, 0, 0, '0'),
---------------------------------------------------------------
The execution took :
0.06 sec
```
## Roadmap
Use ripgrep\
Add more analysis\
Compare to another database

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html) \
Built for educational purposes only.
