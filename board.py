import pygame

class Board:
   def __init__(self, N) -> None:
      self.WIDTH=400
      self.HEIGHT=400
      self.N = N
      self.matrix=[[0] * self.N for i in range(self.N)]
      self.block_size=self.WIDTH/self.N

   def draw_board(self, screen, queen_image):
      QUEEN = pygame.transform.scale(queen_image,(int(self.block_size-10),int(self.block_size-10)))
      self.draw_grid(screen, QUEEN)

   def draw_grid(self, screen, queen):
      for j in range(self.N):
         for i in range(self.N):
            rect = pygame.Rect(200+(i*(self.block_size+1)), 100+(j*(self.block_size+1)), self.block_size, self.block_size)
            if (i+j)%2==0:
               pygame.draw.rect(screen, ('#FDEFBC'), rect)
            else:
               pygame.draw.rect(screen, ('#B09865'), rect)

            if self.matrix[i][j]==1:
               screen.blit(queen, (205+(i*(self.block_size+1)), 105+(j*(self.block_size+1))))
   
   def reset_board(self, n):
      self.N+=n
      self.matrix=[[0] * self.N for i in range(self.N)]
      self.block_size=self.WIDTH/self.N

   def solve(self, row):
      #Base case
      if row>=self.N:
         return True
      #Recurtion form
      for i in range(self.N):
         if self.bounding_func(row, i):
            self.matrix[row][i]=1
            if self.solve(row+1):
               return True
            self.matrix[row][i]=0
      return False

   def bounding_func(self, row, col):
      num=1
      for i in range(self.N):
         if self.matrix[row][i]==1 or self.matrix[i][col]==1:
            num+=1
         if num>1:
            return False

      for i in range(self.N):
         try:
            j = self.matrix[i].index(1)
            if row-col==i-j or row+col==i+j:
               return False
         except:
            pass      

      return True