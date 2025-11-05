from datetime import datetime, timedelta
from typing import Optional ,Union, Dict, List, Any
from pydantic import BaseModel
from sqlalchemy import Integer, Column, String, MetaData, create_engine, ForeignKey,JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session,declarative_base
import os
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage ,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage ,SystemMessage
from langchain_core.prompts import ChatPromptTemplate

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
