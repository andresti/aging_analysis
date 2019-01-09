import sys
sys.path.append('../DTCurrent/')

import struct
import DTCurrentPlot
import DTCurrentData
import numpy as np
import matplotlib.pyplot as plt
#from ROOT import *
import ROOT
from rootpy.io import root_open, DoesNotExist
from rootpy.plotting import Hist, Canvas
import datetime

def plot_current_vs_time():
  data = DTCurrentData.DTCurrentData('../fills/4522/')
  data2 = DTCurrentData.DTCurrentData('../fills/4525/')

  xs, ys = data.current_vs_timestamp(wheel=-1, station=4, sector=4,  superlayer=1)
  plt.plot(xs, ys, '.',c="r",label='SL1 YB-1 S4 MB4 4485')

  xs, ys = data2.current_vs_timestamp(wheel=-1, station=4, sector=4, superlayer=1 )
  plt.plot(xs, ys, ',',c="r",label='SL1 YB-1 S4 MB4 4440')

  xs, ys = data.current_vs_timestamp(wheel=-1, station=4, sector=4,  superlayer=2)
  plt.plot(xs, ys, '.',c="b",label='SL2 YB-1 S4 MB4 4485')

  xs, ys = data2.current_vs_timestamp(wheel=-1, station=4, sector=4, superlayer=2 )
  plt.plot(xs, ys, ',',c="b",label='SL2 YB-1 S4 MB4 4440')

  #xs, ys = data2.current_vs_PMIL5515(wheel=-1, station=4, sector=4,  )
  #plt.plot(xs, ys, '.',c="r",label='Lumi 4485')
  title = "Comparison Runs"
  #plt.title(r'$\alpha > \beta$')
  #plt.ylabel(r'$\mu$ A / ')
  plt.xlabel(r'Current over time')
  #plt.ylabel(r'Ramses Measurement PMIL5514 $\mu$ S/h')
  #plt.ylabel(r'Mean Current for wire channel $\mu$A')
  #plt.xlabel('Luminosity')
  plt.title(title)
  #plt.plot(xs, ys, '.', c=colors[0], label='current')
  plt.legend(loc='upper left', ncol=1, frameon=False, numpoints=1)
  plt.grid()
  plt.show()
  #plt.savefig(self.path + filename, bbox_inches='tight')


def stuff():
  ROOT.TH1.AddDirectory(ROOT.kFALSE)
  #TH1.SetDirectory(0)
  #f = root_open("/eos/cms/store/group/dpg_dt/comm_dt/dtRootple2015/DTTree_Run259685.root", "r")
  f = root_open("/eos/cms/store/group/dpg_dt/comm_dt/dtRootple2017/Express/DTTree_Run306092.root", "r")
  
  f2 = root_open("tmp.root", "RECREATE")
  for path, dirs, objects in f.walk():
    print(objects)
  tree = f.DTTree

  vec_wheel = ROOT.vector('short')()
  vec_station = ROOT.vector('short')()
  tree.SetBranchAddress("digi_wheel", vec_wheel)
  tree.SetBranchAddress("digi_station", vec_station)

  for event in tree:
    n_digis = event.Ndigis
    #print n_digis
    #print "TS", event.timestamp, type(event.timestamp)
    #date = tree.timestamp # & 0xffffffff)
    #print type(tree.timestamp), tree.timestamp, tree.timestamp & 0xffffffff, date.GetYear(), date.GetMonth(), date.GetDay(), date.GetHour(), date.GetMinute(), date.GetSecond()
    for i_digi in range(n_digis):
      #print vec_wheel[0], vec_station[0]
      #print event.digi_wheel[0], event.digi_wheel[1], event.digi_wheel[2]
      if not event.digi_wheel[i_digi]==-1: continue
      if not event.digi_station[i_digi]==4: continue
      if not event.digi_sector[i_digi]==4: continue
      if not event.digi_sl[i_digi]==1:continue
      if not event.digi_layer[i_digi]==1:continue
      if not (event.digi_time[i_digi] < 300 or event.digi_time[i_digi] > 700): continue
      #" & digi_wire=='wire0'"
      #print event.timestamp/1000000000#, totimestamp(datetime.datetime.utcnow()), totimestamp(datetime.datetime.utcnow()) - event.timestamp/1000
      print n_digis, i_digi, datetime.datetime.fromtimestamp(event.timestamp) #, "%d-%m-%Y %H:%M:%S"

def stuff2():
  ROOT.TH1.AddDirectory(ROOT.kFALSE)
  #TH1.SetDirectory(0)
  #f = ROOT.TFile("/eos/cms/store/group/dpg_dt/comm_dt/dtRootple2016/Express/DTTree_Run279931.root")
  f = root_open("/eos/cms/store/group/dpg_dt/comm_dt/dtRootple2017/Express/DTTree_Run306092.root", "r")
  tree = f.Get("DTTree")
  entries = tree.GetEntriesFast()

  for jentry in xrange(entries):
    if tree.LoadTree(jentry) < 0: break
    if tree.GetEntry(jentry) <= 0: continue
    ui = (i & 0xffffffffffffffff)
    #date = ROOT.TDatime(tree.timestamp & 0xffffffffffffffff)
    date = ROOT.TDatime(tree.timestamp)
    print type(tree.timestamp), uint, date.GetYear(), date.GetMonth(), date.GetDay(), date.GetHour(), date.GetMinute(), date.GetSecond()

  """for event in tree:
    n_digis = event.Ndigis
    #print n_digis
    for i_digi in range(n_digis):
      #print vec_wheel[0], vec_station[0]
      #print event.digi_wheel[0], event.digi_wheel[1], event.digi_wheel[2]
      if not event.digi_wheel[i_digi]==-1: continue
      if not event.digi_station[i_digi]==4: continue
      if not event.digi_sector[i_digi]==4: continue
      if not event.digi_sl[i_digi]==1:continue
      if not event.digi_layer[i_digi]==1:continue
      if not (event.digi_time[i_digi] < 300 or event.digi_time[i_digi] > 700): continue
      #" & digi_wire=='wire0'"
      print event.timestamp/1000000000, (long long) event.timestamp#,  totimestamp(datetime.datetime.utcnow()), totimestamp(datetime.datetime.utcnow()) - event.timestamp/1000
      print n_digis, i_digi, datetime.datetime.fromtimestamp(event.timestamp/1000000000.) #, "%d-%m-%Y %H:%M:%S"
  """


"""def stuff3():
  from DataFormats.FWLite import Handle, Events
  events = Events("root://eoscms//eos/cms/store/group/dpg_dt/comm_dt/dtRootple2015/DTTree_Run259685.root")
  hndl_ts = Handle('edm::Timestamp')
  #hist_muon_pt = ROOT.TH1D('muon_pt', ';leading muon: P_{T};events', 50, 0., 500.)
  for evt in events:
    evt.getByLabel('slimmedMuons', hndl_muons)
    muons = hndl_muons.product()
    if muons.size():
    hist_muon_pt.Fill(muons[0].pt())
    hist_muon_pt.SaveAs('leading_muon_pt.root')

  
  vec_wheel = ROOT.vector('short')()
  vec_station = ROOT.vector('short')()
  tree.SetBranchAddress("digi_wheel", vec_wheel)
  tree.SetBranchAddress("digi_station", vec_station)

  for event in tree:
    n_digis = event.Ndigis
    #print n_digis
    for i_digi in range(n_digis):
      #print vec_wheel[0], vec_station[0]
      #print event.digi_wheel[0], event.digi_wheel[1], event.digi_wheel[2]
      if not event.digi_wheel[i_digi]==-1: continue
      if not event.digi_station[i_digi]==4: continue
      if not event.digi_sector[i_digi]==4: continue
      if not event.digi_sl[i_digi]==1:continue
      if not event.digi_layer[i_digi]==1:continue
      if not (event.digi_time[i_digi] < 300 or event.digi_time[i_digi] > 700): continue
      #" & digi_wire=='wire0'"
      print event.timestamp/1000000000#, totimestamp(datetime.datetime.utcnow()), totimestamp(datetime.datetime.utcnow()) - event.timestamp/1000
      print n_digis, i_digi, datetime.datetime.fromtimestamp(event.timestamp/1000000000.) #, "%d-%m-%Y %H:%M:%S"
"""

def draw_stuff():
  ROOT.TH1.AddDirectory(ROOT.kFALSE)
  #TH1.SetDirectory(0)
  f = root_open("/eos/cms/store/group/dpg_dt/comm_dt/dtRootple2015/DTTree_Run259685.root", "r")
  f2 = root_open("tmp.root", "RECREATE")
  for path, dirs, objects in f.walk():
    print(objects)
  tree = f.DTTree  
  #for branch in f.DTTree.branchnames:
  #  print branch
  canvas = Canvas()
  hist = Hist(100, 0.0, 1E3, name='h' + '_' + '_IPchi2', type='D')
  
  #tree.Draw('Ndigis', '', '', hist)
  selection = "digi_wheel==-1 & digi_station==4 & digi_sector==4 & digi_sl==1 & digi_layer==1 & (digi_time < 300 | digi_time > 700)"# & digi_wire=='wire0'"
  h = tree.Draw('timestamp', selection = selection, create_hist = True)
  #h.SetDirectory(0)  
  canvas.SaveAs("test.png")

if __name__ == "__main__":
  #plot_current_vs_time()
  stuff()
