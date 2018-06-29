import matplotlib.pyplot as plt
import seaborn as sns
import pickle

sns.set_style("dark")
with open('Adam0629/result.pkl', 'rb') as f:
    data = pickle.load(f)

# plt.plot(range(1, 25), data['train_loss'], 'b-.', label='train_loss')
# plt.plot(range(1, 25), data['train_loss'], '-', label='train_loss')
# plt.plot(range(1, 25), data['val_loss'], 'g-.', label='val_loss')
# plt.plot(range(1, 25), data['val_loss'], '--', label='val_loss')
plt.plot(range(1, 25), data['train_acc'], 'y-.', label='train_acc')
# plt.plot(range(1, 25), data['train_acc'], '-.', label='train_acc')
plt.plot(range(1, 25), data['val_acc'], 'm-.', label='val_acc')
# plt.plot(range(1, 25), data['val_acc'], ':', label='val_acc')
plt.xlim([1,25])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
