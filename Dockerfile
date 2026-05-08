FROM python                                 
WORKDIR /mypython                            
COPY requirements.txt .                       
RUN pip install -r req.txt                    
COPY . .                                      
CMD ["python","app.py"]                        
