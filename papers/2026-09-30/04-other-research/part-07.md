# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 301. [Adaptive Latent Capacity for World Models](https://arxiv.org/abs/2609.32921)

**<font color=#1a73e8>作者：</font>** Idan Achituve, Lior Dikstein, Idit Diamant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Adaptive LeWorldModel (ALeWM), a world model based on a joint-embedding predictive architecture (JEPA) that learns to concentrate predictive information in compact prefixes of a wide latent representation. To encourage this ordering, ALeWM learns a sequence-conditioned distribution over prefix lengths and trains the predictor to estimate the full next embedding from a sampled input prefix. As standard anti-collapse objectives encourage variation across latent coordinates and do not organize them by predictive importance, we also introduce MixSIGReg. MixSIGReg regularizes the masked embeddings against a prior-weighted mixture with Gaussian active prefixes and zeros in the remaining coordinates. As a result, the ALeWM objective encourages early coordinates to retain information useful for prediction and recursive planning. Our analysis shows that the mixture distribution used by MixSIGReg assigns higher variance to earlier coordinate blocks and lower variance to later ones. In addition, we show that, under specified assumptions, prediction error is minimized by placing the information most useful for prediction in earlier blocks. Empirically, we study the behavior of ALeWM in a controlled dynamical system with known state variables and in goal-conditioned visual control. We show that ALeWM consistently achieves higher mean success rates than tuned fixed-width LeWM, with lower planning capacity on average.

---


### 302. [Precision As You Need: Stochastic Computing Is a Dense Adaptive Quantizer](https://arxiv.org/abs/2609.32922)

**<font color=#1a73e8>作者：</font>** Haoran Jin, Kangqi Zhang, Jirong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Matrix multiplications dominate the inference cost of modern transformer-based vision models, yet existing efficiency techniques such as post-training quantization and mixed-precision inference are largely limited to the small set of fixed-width formats (INT4, INT8, BF16, and FP16) supported by conventional accelerators. We revisit stochastic computing (SC) as a way to lift this constraint: viewed as a dense adaptive quantizer, SC controls precision by bit-stream length L rather than a fixed datapath, while each multiplication reduces to a single AND/XNOR gate. We build a GPU library that emulates SC matrix multiplication at scale, exposes stream lengths as first-class kernel arguments, and evaluates SC end-to-end on image classification, object detection and instance segmentation, class-conditional image generation, and visual world-model planning. On top of this substrate, we develop a dynamic per-row mixed-precision policy that assigns stream length per token or group at matched average budget, requires no retraining, and uses the same SC hardware across schedules. Across tasks, SC remains competitive with fixed-format INT quantization at matched bit budgets, while per-row mixed precision helps maintain accuracy at lower average stream lengths. These results provide software-level feasibility evidence that SC can serve as a dense-precision substrate for fine-grained mixed-precision inference on modern vision transformers.

---


### 303. [TRACE: Learning to Self-Calibrate Wireless Digital Twins from ISAC Measurements](https://arxiv.org/abs/2609.32923)

**<font color=#1a73e8>作者：</font>** Saad Masrur, Saeed R. Khosravirad, Ismail Guvenc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wireless digital twins (DTs) rely on 3D environment models to predict radio propagation and support wireless-network decisions, yet these models are often initialized from imperfect 3D maps. Errors in building position, height, footprint, and orientation can therefore cause a high-fidelity propagation engine to simulate the wrong physical environment. In this paper, we study how a deployed wireless network can repair an existing DT using its own radio frequency (RF) measurements. In particular, we introduce Twin Residual Alignment and Calibration Engine (TRACE), a physics-grounded learning-based self-calibration framework that treats twin maintenance as residual alignment between the physical world and the current DT. Using the same sensing configuration as the physical measurements, TRACE ray-traces the current DT, coherently backprojects the measured and simulated RF onto a common world grid, and extracts the same local region around each building's current DT position. A multi-view corrector then fuses evidence across sensing nodes and neighboring buildings to predict a gated six-parameter correction per building, without relying on absolute layout or sensor ordering, and supports iterative correction through re-rendering. On 5,400 held-out samples from unseen simulated scenes at 28 GHz, TRACE reduces 3D position RMSE from 2.202 m to 0.302 m and yaw RMSE from 4.978° to 0.894°, outperforming ViT and U-Net baselines under changes in layout, building count, sensing-node count, and SNR. On measured 28 GHz RF data from the NIST outdoor courtyard, a model trained only on synthetic RF reduces mean planar wall-position error from 1.00 m to 7.8 cm, without measured-data fine-tuning or geometric labels. These results show that the discrepancy between measured and twin-rendered RF can serve as a learning signal for repairing a wireless DT.

---


### 304. [Phenomenon-Graph JEPA: Label-Efficient Representation Learning for Contactless Cardiorespiratory Sensing](https://arxiv.org/abs/2609.32928)

**<font color=#1a73e8>作者：</font>** Constantino Álvarez Casado, Nhi Nguyen, Mohammad Rakibur Rahman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar and RGB-D cameras can record cardiac and respiratory waveforms continuously and without contact, but labeled recordings remain scarce because every label requires a supervised acquisition session. Self-supervised pretraining can exploit the unlabeled signals, yet contrastive methods depend on signal transformations and negative pairs whose validity is uncertain for cardiorespiratory data, where time warping changes breathing rate and distant windows can share the same physiological state. We present Phenomenon-Graph JEPA, a joint-embedding predictive architecture that learns from four processed one-dimensional streams without negative pairs or synthetic augmentation in its base configuration. Each stream is encoded by a temporal convolutional branch and a band-limited spectral branch. During pretraining, the model predicts stopped target embeddings along typed edges, which connect streams assigned to the same physiological phenomenon, and forward in time within a state episode. We treat this physiological typing as a testable hypothesis and compare it with wrong-edge and all-pairs prediction graphs. In the OMuSense-23 dataset, pretraining improves label-efficiency area over matched supervised training by 3.91 percentage points (95% interval 2.08 to 5.80, Holm-adjusted p = 0.006), and by 3.74 points under a second configuration evaluated on the same test participants. However, the wrong-edge and all-pairs controls do not establish a benefit from physiological typing. Optional Takens-inspired delay coordinates improve a validation comparison with learned history, whereas two wrist-only WESAD protocols do not establish a pretraining advantage. The study therefore separates the measured benefit of predictive representations from the physiological prior used to organize their training.

---


### 305. [Efficient Dynamic Algorithms for Graph Neural Networks with Non-Linear Propagation](https://arxiv.org/abs/2609.32929)

**<font color=#1a73e8>作者：</font>** Kiarash Banihashem, MohammadTaghi Hajiaghayi, Mahdi JafariRaviz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are widely used for representation learning on graphs, but most methods assume static topologies, making them inefficient on evolving networks where edges change over time. Existing dynamic approaches either model graph evolution through temporal GNN architectures without focusing on efficient dynamic maintenance, or are restricted to linear propagation models based on Personalized PageRank.
In this work, we study how to efficiently maintain node representations for non-linear GNN propagation under edge insertions and deletions. The propagation has no learned parameters, and only a classifier applied afterward is trained. For a broad class of standard activation functions, we develop a residual-based dynamic algorithm that selectively propagates local errors via push operations, maintaining an approximation to the evolving fixed point without full recomputation. We prove that our method achieves amortized $O(1/\epsilon)$ update time per graph change under a degree-normalized error guarantee. Our approach uses a potential-based analysis in a degree-scaled norm and, in contrast to prior work on the linear case, requires no randomness assumptions on either the update sequence or the input vector. For the linear special case, we additionally provide an exact dynamic algorithm via low-rank matrix inverse updates. Experiments on benchmark datasets show that incorporating non-linearity improves accuracy while preserving efficient update performance, yielding a scalable and theoretically grounded method for maintaining this propagation on dynamic graphs.

---


### 306. [Last-Iterate Guarantees for Online Reinforcement Learning in Structured Constrained MDPs](https://arxiv.org/abs/2609.32933)

**<font color=#1a73e8>作者：</font>** Nam Phuong Tran, Trinh Ha Mai Huynh, Tuyen Pham Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In safety-critical applications, deployment uses a single policy, whose performance and constraint satisfaction should hold directly rather than only for an average or mixture of training policies. This motivates last-iterate guarantees in constrained reinforcement learning. Recent progress has established such guarantees in exact-gradient or tabular online settings, yet scalable results for structured large-state problems remain open. We develop a general, statistically efficient framework for last-iterate convergence in structured Constrained MDPs (CMDPs). Our analysis separates contraction of the regularised primal-dual dynamics from actor approximation and statistical errors in policy evaluation under online exploration. This enables model-free on- and off-policy learning with structured function approximation: optimistic policy evaluation avoids explicit transition-model construction, while a compact parametric actor avoids maintaining mixtures or histories of past policies. We instantiate the framework for linear CMDPs and general function approximation, obtaining representation-dependent complexity and improved target-accuracy dependence over prior optimistic regularised primal-dual analyses. We further validate the stabilising effect predicted by our theory on a synthetic linear CMDP: the regularised method exhibits stable last-iterate behaviour, whereas its unregularised counterpart shows larger oscillations.

---


### 307. [The Impact of Stochasticity on the Rashomon Effect in Machine Learning](https://arxiv.org/abs/2609.32934)

**<font color=#1a73e8>作者：</font>** Andrea Apicella, Francesco Isgrò, Andrea Pollastro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network training is inherently stochastic, with factors such as weight initialization leading to distinct models despite comparable predictive performance. This phenomenon is commonly associated with the Rashomon effect, which describes the existence of multiple near-optimal models for the same task. Although the Rashomon effect has received increasing attention, it remains unclear whether different sources of training stochasticity contribute similarly or differently to its manifestations. In this work, we present an empirical study of the Rashomon phenomenon along three complementary dimensions: solution-space multiplicity, predictive multiplicity, and decision-basis multiplicity. These dimensions are quantified through the size of the empirical Rashomon set, predictive ambiguity, and agreement between XAI attribution maps, respectively. By independently controlling three standard sources of stochasticity, namely weight initialization, mini-batch data ordering, and dropout, we isolate their respective contributions to each dimension of the Rashomon phenomenon. Experiments on tabular and image classification benchmarks reveal that these sources affect the three dimensions in different ways. In particular, larger empirical Rashomon sets do not necessarily correspond to greater predictive disagreement or lower explanation agreement, indicating that solution-space, predictive, and decision-basis multiplicity capture complementary rather than interchangeable aspects of the Rashomon effect. Overall, our results show that training stochasticity influences not only predictive performance but also the stability of predictions and explanations, highlighting the importance of identifying the specific sources of stochasticity responsible for different manifestations of the Rashomon phenomenon when assessing the reliability, reproducibility, and interpretability of neural network models.

---


### 308. [TwinS-GCN: Spectral conjugate for Spectral Graph Convolutional Networks](https://arxiv.org/abs/2609.32940)

**<font color=#1a73e8>作者：</font>** Chun Hei Michael Chan, Flavia Petruso, Dimitri Van De Ville  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph convolutional networks propagate information by repeated local aggregation through a graph shift operator; i.e., a $K$-layer network reaches $K$ hops neighborhood. On the one hand, such spreading can lead to oversmoothing. On the other hand, long-range dependencies demand the depth. Transporting information on long distances and without attenuation requires the shift to distinguish a direction of flow, which a symmetric operator cannot perform but a directed one can fulfill. A natural way to extract pure-directionality is to take the skew-symmetric part of the shift operator through the Cartesian split, which, however, generally does not commute with the shift itself, meaning that the filters built on it are not shift-invariant. We instead use the spectral conjugate; i.e., the image of the operator under $\tau:z\mapsto \bar{z}$, which commutes with the shift and splits it into a dissipative and a non-dissipative part. Two filter families follow: a sum filter, whose non-dissipative component transports signal without energy loss, and a ratio filter, ratio in the pair of components rather than polynomial in the shift. Both arise from non-holomorphic kernels, placing them outside the holomorphic class underlying classical spectral convolution. On the directed cycle, the ratio filter becomes an IIR filter with global impulse response, for which we prove a long-range reach gap against every degree-$K$ polynomial filter. Chebyshev reparameterization gives stable vertex-domain layers with real coefficients, yielding TwinS-GCN, which solves graph transfer tasks at reduced depth and is competitive with state-of-the-art graph convolutional networks on node classification benchmarks.

---


### 309. [Generative Priors Conditioned on Natural Language for Bayesian Inversion in PDEs](https://arxiv.org/abs/2609.32941)

**<font color=#1a73e8>作者：</font>** Pengyu Zhang, Mark Girolami, Arnaud Vadeboncoeur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring quantities of interest (QoI) from data is a central task in Science and Engineering. In such contexts, we often have access to both quantitative data and qualitative data. Quantitative data may be represented by noisy sensor measurements, simulation data, re-analysis data; qualitative data may be in the form of text descriptions of experimental setups, expected experiment outcomes, and human-perceived system behaviours. The task we address in this paper is the following. Given a training set of paired qualitative text and quantitative QoI data, we learn to exploit the inherent correlation between the two modalities to learn a highly informative data-driven natural-language-conditional Bayesian prior, such that when presented with a new physical system, we can coherently combine (i) the training dataset, (ii) qualitative text describing the new system, and (iii) a small number of noisy sensor readings from that new system, to perform inference and uncertainty quantification (UQ) over the QoI. To achieve this task, we develop two parallel approaches, one uses conditional diffusion and the other conditional autoencoders, and compare both against classical Bayesian methodology, unconditional generative models and deterministic supervised methods. Each approach has specific strengths and tradeoffs; conditional autoencoder offers theoretical tractability, allows for fast posterior sampling, and provides better-calibrated UQ, whereas conditional diffusion is explored for greater expressiveness and capturing complex posteriors with irregular QoI fields. The approach is tested on the steady-state heat equation, damped Helmholtz equation, and UK weather reanalysis data.

---


### 310. [Synthetic Thermal Image Generation for Real-Time Animal Detection Under Low-Visibility Conditions](https://arxiv.org/abs/2609.32944)

**<font color=#1a73e8>作者：</font>** James Momoh, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildlife-vehicle collisions remain a significant road safety concern, particularly during nighttime and low-visibility conditions when RGB-based perception systems are often unreliable. Thermal imaging offers a promising alternative for detecting animals under poor illumination. However, the limited availability of annotated infrared animal datasets restricts the development of robust deep learning-based detection models. This paper investigates synthetic thermal image generation as a scalable approach for real-time animal detection under low-visibility conditions. A subset of 514 annotated visible-spectrum animal images from the NTLNP dataset is translated into synthetic thermal representations using CycleGAN-Turbo, while a limited real thermal dataset of 60 images is expanded through thermal-focused augmentation. Multiple object detection architectures, including YOLOv8, YOLOv9, YOLOv10, and RT-DETR, are trained independently on synthetic and real thermal datasets and evaluated using precision, recall, mAP@0.5, mAP@0.5:0.95, model size, and inference latency. Experimental results show that synthetic thermal images provide competitive detection performance, with RT-DETR achieving the highest synthetic-data mAP@0.5 of 0.9613. Models trained on augmented real thermal data achieve the strongest overall performance, with YOLOv10s obtaining 0.9879 mAP@0.5 and 0.9571 mAP@0.5:0.95. Computational analysis further indicates that lightweight YOLO variants provide favorable inference latency, supporting their potential for real-time deployment. These findings demonstrate that synthetic thermal imagery can reduce dependence on scarce infrared datasets and support the development of efficient animal detection systems for future vehicle-mounted wildlife collision mitigation applications.

---


### 311. [Optimal Nonparametric Dynamic Pricing with Censored Demand and Adversarial Inventory](https://arxiv.org/abs/2609.32949)

**<font color=#1a73e8>作者：</font>** Mengxiao Zhang, Yingfei Wang, Haipeng Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online dynamic pricing with censored demand, where an arbitrary inventory level is revealed before pricing and may adapt to past observations, while demand follows an unknown, price-dependent distribution that is stationary over time. For a horizon of $T$ rounds, Xu et al. [2026] achieved $\widetilde{\mathcal{O}}(\sqrt{T})$ regret under restrictive structural assumptions including linear demand, price-independent additive noise, and conditions relating inventory levels to the noise support. Our first contribution is to extend this framework to a substantially more general and statistically harder nonparametric setting, requiring only the natural assumption that expected sales are nonincreasing in price and allowing nonlinear demand curves and price-dependent noise. For this model, we first propose a simple baseline, Double-Grid-UCB, which discretizes both price and inventory and achieves $\widetilde{\mathcal{O}}(T^{3/4})$ expected regret using separate revenue estimates for each price-inventory grid pair. Then, we develop Threshold-UCB, which improves the expected regret to $\widetilde{\mathcal{O}}(T^{2/3})$. Unlike Double-Grid-UCB, Threshold-UCB reuses sales observations across inventory levels through shared estimates of demand-tail probabilities, allowing the same data to support revenue upper bounds for multiple inventories rather than a single inventory bin. We also complement this upper bound with an $\Omega(T^{2/3})$ lower bound via a reduction from stochastic posted pricing, establishing its minimax optimality. Finally, extensive experiments across inventory processes, demand functions, and noise models demonstrate consistently superior performance of Threshold-UCB over benchmark algorithms.

---


### 312. [Constrained Flow Policy Updates: A Generalized Schrödinger Bridge View](https://arxiv.org/abs/2609.32952)

**<font color=#1a73e8>作者：</font>** Boyang Li, Matthew Kim, Sylvia Herbert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online safe reinforcement learning (RL) seeks policies that maximize reward while satisfying safety constraints. Reward and safety can induce multimodal action distributions, challenging the prevailing primal-dual methods: Gaussian actors may collapse onto a single suboptimal mode, and optimization over the nonconvex Lagrangian landscape can be unstable. Diffusion and flow policies can represent such distributions, but recent work with a diffusion actor relies on estimating and matching the score of an augmented-Lagrangian target policy. Instead, we differentiate the augmented objective directly through the generation path of a flow policy, so no score needs to be estimated. Because a flow policy lacks a readily available action log-density for entropy regularization, we build on the density-free kinetic-energy regularizer of FLAC, a recent reward-only method, and propose Reparameterized Augmented-Lagrangian Flow Actor with Least Energy (RAFALE), an off-policy actor-critic method for safe RL. We formulate its update as a constrained one-ended generalized Schrödinger bridge and show that, for each source draw, this path-space problem is exactly an entropy-regularized problem in action space. At positive noise, its solution reweights the reward-only action distribution only where the estimated cost exceeds a threshold set by the Lagrange multiplier. As the noise vanishes, the optimal value converges to that of a least-energy map objective that the flow policy optimizes directly. Across seven Safety-Gymnasium tasks, RAFALE achieves competitive reward with mean final cost within budget on every task, whereas strong baselines trade one for the other; ablations support the necessity of both its augmented objective and its flow actor.

---


### 313. [Efficient Message Passing for Partial Differential Equation Priors](https://arxiv.org/abs/2609.32956)

**<font color=#1a73e8>作者：</font>** Anna Kazachkova, Leonhard Hennicke, Rainer Schlosser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior information for real-world physical quantities is most elegantly expressed via partial differential equations (PDEs). In this paper, we propose a novel way to solve PDEs using probabilistic inference on a factor graph. In general, factor graphs provide a natural way to encode prior knowledge into a model as explicit factors; here, this knowledge is provided by a governing PDE, which narrows the solution space, while observed data further shape the posterior over the parameters. The approximate parameter posterior is inferred using message passing based on moment matching, without posterior sampling or global gradient-based optimization. We demonstrate our approach on the first-order advection and the second-order semi-linear Fisher-KPP equations, where it achieves predictive accuracy comparable to a standard baseline while providing structured predictive uncertainty. Moreover, the inferred posterior marginal means and uncertainty structure match more closely those obtained using Hamiltonian Monte Carlo than the evaluated mean-field variational inference baseline, while requiring up to 10x less training time in our experiments, with inference speed comparable to variational inference.

---


### 314. [Clipped or Unclipped? Finite-Sample Trade-offs for Averaged SGD under Heavy-Tailed Noise](https://arxiv.org/abs/2609.32962)

**<font color=#1a73e8>作者：</font>** Alexandra Suvorikova, Egor Gladin, Darina Dvinskikh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient clipping is widely used to stabilize training, but it need not improve the statistical accuracy of averaged SGD, even under heavy-tailed noise. We derive a finite-sample comparison of clipped and unclipped Polyak-Ruppert averaged SGD under finite conditional $p$-th moments, $p\ge2$. Our main result gives explicit accuracy and confidence conditions under which, for $p>2$, the Gaussian term dominates the unclipped deviation bound, so clipping need not improve its leading order. By balancing clipping bias and concentration, we obtain a bound in which the heavy-tail correction depends logarithmically rather than polynomially on the inverse failure probability. At $p=2$, this improves the confidence dependence of the leading bound. We establish sharpness of the unclipped heavy-tail term through an exact one-dimensional quadratic recursion and extend the comparison to projected convex SGD. We also prove concrete costs of clipping: every fixed finite threshold increases asymptotic variance on a scalar Gaussian quadratic, while whole-gradient clipping can shift the limiting point under asymmetric noise.

---


### 315. [Self-Confirming Superposition Traps in Reinforcement Learning](https://arxiv.org/abs/2609.32966)

**<font color=#1a73e8>作者：</font>** Dai Shi, Andi Han, Feng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) trains representations on data selected by the agent's policy, which then uses the resulting returns to guide its next choices. We show that this loop can sustain a lower-return policy even when representation fitting is globally optimal on those data. In a self-confirming superposition trap, every optimal code assigns overlapping directions to features that rarely occur together under the current policy. An alternative action brings them together, causing interference that lowers its return and reinforces avoidance, although refitting to that action would yield more return at the same capacity. We characterize the dimensions admitting a trap in a tied two-step model and show separately that equal feature frequencies, continued visitation, and independent controller learning need not prevent it. Because fitting weights errors by visitation, an avoided action can lose its return advantage at little cost to the objective. In a finite-action model, we bound this distortion and derive a replay condition: sufficient training weight on the best separately adapted action preserves its ranking despite residual error. Neural PPO experiments show how the feedback develops during learning: agents initialized toward different actions develop different interference patterns, opposite mean return rankings, and different final policies at the same capacity. We therefore test whether retaining access to neglected states can improve control. Keeping these states in training reduces measured interference and improves sequential return, with gains even when the encoder is frozen. Related interventions on state access, replay weights, and feature overlap improve control on MiniGrid and DMControl. For agents that learn through a world model, protected fitting improves DreamerV3--Crafter's cumulative training scores at unchanged capacity.

---


### 316. [Distributed Hydrological Modeling in the Feature Space](https://arxiv.org/abs/2609.32971)

**<font color=#1a73e8>作者：</font>** Mohamad Hakam Shams Eddin, Maria Luisa Taccari, Yikui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of river discharge and floods is very challenging. River dynamics are affected by storage, meteorological forcing, and flow propagation at different spatial and temporal scales. Forecasting thus requires a framework that considers the upstream-to-downstream flow through river networks across grid cells and catchments. This modeling is known in hydrology as distributed modeling and routing. Existing deep learning approaches either ignore this topology, operate on lumped catchments, or route predicted physical quantities through a separate graph or physical routing model. We instead introduce feature-space routing: a topology-aware state-space operator embedded directly in the forecasting dynamics. At every forecast step, the operator gathers latent states from upstream grid cells and causally updates the downstream state according to the known river network. This preserves the physical connectivity of the river system while allowing the propagated state itself to be learned end-to-end and allows the model to predict river discharge considering both local dynamics and neighboring upstream contributions. To address uncertainty and provide probabilistic forecasts, we minimize the fair continuous ranked probability score (fCRPS) as a training objective. Our experiments on the European Flood Awareness System (EFAS) and observational data for river discharge forecasting demonstrate that encoding the physical structure of river networks explicitly in the feature space substantially improves the forecasting skill, particularly in an ungauged setting. Our approach achieves state-of-the-art results on both reanalysis and observational data and is able to forecast maps of river discharge at 1 arcminute and 6-hourly resolution up to 10 days lead time.

---


### 317. [Exploring the Effects of Olfactory Cues and Ventilation on Teleportation-based Navigation in VR](https://arxiv.org/abs/2609.32975)

**<font color=#1a73e8>作者：</font>** Dongyun Han, Heecheol Kim, Siyeon Bak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatial cognition supports how people interpret spatial relationships and navigate their surroundings. Although vision plays a dominant role, other sensory modalities, including olfaction, may also contribute under limited visual conditions. This paper investigates the role of olfactory cues in location recognition during virtual reality (VR) navigation. We conducted two formal studies using a wearable olfactory prototype. Study 1 examined whether olfactory cues and ventilation influenced users' recognition of encountered locations during \HDY{teleportation-} and dash-based navigation. Study 2 extended this investigation to repeated navigation and examined whether ventilation duration influenced recognition performance and user experience across successive movements. Results show that olfactory cues can support recognition of encountered locations during navigation, while ventilation was associated with reduced residual interference and improved usability. However, longer ventilation did not clearly improve recognition accuracy in repeated navigation. These findings suggest the potential of olfactory cues as contextual signals during VR navigation, while also highlighting the importance of scent management for maintaining perceptual clarity and user comfort.

---


### 318. [Adaptive Ensemble Selection for Noisy Labels on Tabular Data](https://arxiv.org/abs/2609.32976)

**<font color=#1a73e8>作者：</font>** Faizaan Ali, Inwon Kang, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Incorrect or corrupted labels in tabular datasets can significantly degrade supervised learning performance, particularly when mislabeling is subtle and not easily detectable from feature space alone. In the context of automated or AI-augmented data science workflows, robust detection of such label noise is critical for building reliable models. We propose a data-centric reasoning module for AI data science systems that automatically diagnoses dataset quality and selects appropriate cleaning strategies. Given a dataset, a meta-model predicts weights over a diverse set of detectors, including confidence-based, neighborhood-based, and distributional methods. Across benchmark datasets with controlled noise, our approach achieves performance comparable to a Confident Learning baseline on average, with dataset-dependent gains and losses, particularly in heterogeneous regimes. We further show that detector effectiveness is systematically linked to dataset properties. These results demonstrate the value of descriptor-driven, data-centric ensembling as a component of AI-assisted data-science pipelines for robust dataset assessment and model reliability.

---


### 319. [Feasible Flow Matching for Graph Reconstruction via Within-Sampling Primal-Dual Guidance](https://arxiv.org/abs/2609.32980)

**<font color=#1a73e8>作者：</font>** Haoming Chen, Nicolas Zilberstein, Santiago Paternain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph reconstruction from partial observations often comes with structural side information, such as degree bounds, triangle counts, or an edge-density band. Prior-Informed Flow Matching (PIFM) reconstructs graphs by transporting a local prior toward the graph distribution, but it provides no mechanism to incorporate this side information. We put forth Constrained Primal-Dual PIFM (CPD-PIFM), which augments the sampler with Lagrange multipliers that evolve along each trajectory. The multipliers respond to constraint violations at a predicted endpoint and guide subsequent sampling steps without retraining. We prove that the sampler inherits PIFM's permutation equivariance and bound its expected terminal slack by a term that decays as the inverse square root of the number of steps, plus two approximation terms. On three link-prediction benchmarks and nine combinations of datasets and constraints, CPD-PIFM raises feasibility by 11-26 percentage points and remains competitive with fixed guidance without selecting a separate multiplier for each constraint.

---


### 320. [VocalEyes: Speaker-Aware Augmented Reality Captioning through In-Conversation Registration](https://arxiv.org/abs/2609.32983)

**<font color=#1a73e8>作者：</font>** Yuxiao Wang, Xulong Tang, Chen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Co-located augmented reality (AR) captions make speech readable, but they can separate an utterance from the person who produced it. In unfamiliar groups, losing that source complicates immediate responses and later review: users must recover not only what was said, but also who said it. Conventional diarization returns anonymous clusters, while speaker recognition typically assumes pre-meeting enrollment. We built VocalEyes, a speaker-aware AR captioning system that creates named voice profiles from natural self-introductions. The interface coordinates speaker-attributed captions, a fixed profile card, and a visual cue that marks the articulating face. In a controlled within-subjects study with 20 participants who reported typical hearing, VocalEyes identified speakers with 88.0% accuracy and increased participant speaker-tracking accuracy from 47.2% with caption-only AR to 87.3% with the complete interface. Participants also reported lower workload with the complete interface. These findings show how in-conversation registration can preserve speaker attribution across live captions and meeting records in scripted small-group meetings.

---


### 321. [Coordinated Electromagnetic Side-Channel Attacks for Voter--Ballot Linking: A Case Study of the Brazilian E-Polling System](https://arxiv.org/abs/2609.32988)

**<font color=#1a73e8>作者：</font>** Leandro Hyeda, Kleber V. Cardoso, Antonio Oliveira-Jr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this work, we show how two adversaries (Eve and Mallory) can coordinate an electromagnetic side-channel attack to recon- struct the vote displayed on an e-voting machine (EVM) and link it to a specific voter (Alice). Assuming that Eve has access to a place adjacent to the e-polling room (e.g., restroom, unsupervised room), she performs vote reconstruction by intercepting un- intended electromagnetic emanations associated with the video signal. Meanwhile, Mallory observes when Alice is voting and reports this information to Eve over the Internet. To validate the most critical stage of the attack, we conduct a software-defined radio experiment using the official Brazilian e-voting interface and demonstrate through-wall vote reconstruction. Although conventional monitors are employed rather than official EVMs, our findings provide insights into information forensics and support security recommendations for government authorities responsible for e-voting systems.

---


### 322. [Smelling the Way: Olfactory Modulation of Spatial Estimation and Path Integration in Virtual Reality](https://arxiv.org/abs/2609.32992)

**<font color=#1a73e8>作者：</font>** Siyeon Bak, Junho Kim, Dongyun Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatial cognition enables individuals to perceive and interpret spatial relationships, estimate locations, and navigate within their surroundings. While vision plays a dominant role, other sensory modalities, particularly olfaction, can support spatial processing when visual cues are limited. This paper explores the effects of scent-delivery within virtual reality (VR) environments by using fan-mediated olfactory devices. We conducted two formal studies to evaluate the effects on spatial information acquisition. Study 1 (N=24) examined the participants' ability to localize a scent source while walking a linear path using two different olfactory devices. Study 2 (N=19) employed a triangle completion task, in which participants attempted to return to their starting point under varying rotation angles and olfactory conditions. Results indicate that scent-delivery feedback influenced spatial behavior in distinct ways across the two studies. In Study 1, visual-olfactory misalignment produced systematic directional biases without improving absolute localization accuracy. In Study 2, distance-modulated scent-delivery feedback reduced terminal homing error but also increased traveled distance and completion time, suggesting a more deliberate goal-confirmation strategy.

---


### 323. [On the Usage of Verifiable Credentials in Privacy-Preserving Federated Analytics](https://arxiv.org/abs/2609.33004)

**<font color=#1a73e8>作者：</font>** Andreea-Elena Drăgnoiu, Ruxandra F. Olimid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-Preserving Federated Analytics enables multiple nodes to collaboratively derive statistical insights without exchanging raw data. However, ensuring node authenticity and data validation (avoiding concerns such as identity tracking, data linkage, or data leakage) remain fundamental challenges. This paper offers some insights into the feasibility of defining an authenticated, integrity-preserving data model by coupling FPPA with Verifiable Credentials defined within the Self-Sovereign Identity framework.

---


### 324. [Safety-Constrained Cascade Inference for Robust Malaria Cell Classification Under Field Corruptions](https://arxiv.org/abs/2609.33005)

**<font color=#1a73e8>作者：</font>** J. T. Hagbe, Michel Emel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated malaria diagnosis from thin blood-smear microscopy could meaningfully reduce the burden on under-resourced laboratories, but a model that maximises accuracy on clean laboratory images fails badly the moment an inexpensive smartphone camera introduces sensor noise. This paper introduces MalariaCascade, a two-stage inference system in which a lightweight MobileNetV2 sentinel (2,225,153 parameters) makes confident classifications at low compute cost and escalates uncertain cases to an EfficientNet-B3 expert (10,697,769 parameters) that sees only clean, standardised images regardless of how corrupted the incoming frame is. Structural isolation of the expert stage, not learned robustness, is the mechanism. The sentinel is trained under a safety-score objective that places an explicit floor on Recall(Parasitised) (>=0.95) and Recall(Uninfected) (>=0.40) before precision is optimised, ensuring the checkpoint satisfies clinical safety constraints by construction. On the NIH Malaria Cell Images Dataset (27,558 cells), the cascade reaches Accuracy=0.9736, Recall(Parasitised)=0.9570, Precision(Parasitised)=0.9912, F1=0.9738, and AUROC=0.9955 on the clean test set. Under Gaussian sensor noise at full severity, cascade Recall(Parasitised) degrades by only 2.4 pp (0.9570 to 0.9329), while the flat single-model baseline collapses by 63.0 pp (0.9584 to 0.3281). McNemar's test confirms the cascade improvement is statistically significant (chi^2=11.14, p=0.00085). An ablation isolating the structural property shows that routing clean images to the expert is responsible for a 16.8 pp Recall(Parasitised) advantage under sensor noise relative to a cascade where the expert also sees corrupted inputs.

---


### 325. [Saturation-Insensitive Dueling Bandits with General Function Approximation](https://arxiv.org/abs/2609.33011)

**<font color=#1a73e8>作者：</font>** Chenggong Zhang, Xuheng Li, Qiwei Di 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study contextual dueling bandits with general function approximation under the Bradley-Terry-Luce (BTL) preference model. A key challenge in this setting is the saturation of the preference model: when the current reward model can already distinguish two actions with high confidence, the resulting preference feedback becomes weakly informative, making it difficult to further improve reward estimation. Consequently, existing sample-complexity analyses often depend on the inverse-derivative factor $1 / \sigma'[\Delta_{r^\ast}]$ which can be prohibitively large when the link function $\sigma$ saturates for large reward gaps $\Delta_{r^\ast}$. To address this issue, we introduce `SI-CDB`, an algorithm that selects opponent arms using a carefully designed heuristic for arm selection. This design enables saturation-insensitive reward learning and recovers the near-optimal dependence for linear reward classes, eliminating the unfavorable $1/\sigma'(\cdot)$ factor. The core of our analysis is a localized Eluder dimension framework tailored to dueling bandits with general function approximation. Our theoretical results also explain why two-arm regret analysis is crucial for improving single-arm performance in dueling bandits.

---


### 326. [When Pair Count Is Not the Sample Size: What All-Pairs Agent Comparisons Estimate](https://arxiv.org/abs/2609.33012)

**<font color=#1a73e8>作者：</font>** Wei-Jung Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an agent benchmark compares every pair of leaderboard entries, the number of comparisons can look much larger than the independent evidence behind them: A versus B and A versus C both reuse A. Whether this reuse affects inference depends on what the analysis is meant to describe. If the board and its outcomes are fixed, the all-pairs mean is an exact summary of those entries, and any interval must come from another declared source of randomness. If the entries are instead treated as iid draws from a population of future configurations and the pair rule is regular and nondegenerate, the same mean is an order-two U-statistic whose first-order uncertainty depends on the number of configurations, not the number of pairs. We use near ties as the running example, but the distinction extends to other symmetric pair summaries when their regularity conditions hold. We examine both interpretations using a fixed SWE-bench Verified snapshot and an exact binary model with known truth. On SWE-bench, intervals that accounted for shared configurations were more than twice as wide as a pair-iid reference that treated the pairs as independent. In the exact model, pair-iid coverage fell far below the nominal level when edges shared endpoints but remained near nominal for matched independent edges. Results on two other fixed leaderboards show that exact summaries also depend on which pairs are included and how they are weighted. An all-pairs analysis must therefore state what is fixed, what is sampled, and how it handles shared entries and pair aggregation.

---


### 327. [Trust and Task Completion in the World of Consumer AI Agents](https://arxiv.org/abs/2609.33017)

**<font color=#1a73e8>作者：</font>** Jeroen Olieslagers, Eduardo Pujol, Gal Zahavi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Action agents do things for people. They send email, spend money, and call businesses while the user is busy with something else, so a mistake can turn into an action before anyone notices. They fail their users in two ways. They break trust when they do something the user never agreed to, or hold back after the user clearly said go. And they fall short on completion when they give up on errands that turn out to be hard. Both depend heavily on the harness around the model, meaning its instructions, tools, context, and guardrails. We built an evaluation that scores trust and completion on the same runs, in a simulated world of businesses with their own websites, inboxes, and phone lines, and of people who write back. A simulated user answers the assistant's questions. Trust means that nothing happens the user did not agree to. No email goes to someone they never approved, no private detail ends up on a group thread, no money is spent past their limit, no stranger's instructions are followed, and nothing is claimed without a source. Every trap has a matched control in which acting is the right call. We use the evaluation to measure Fo, Wajo's personal assistant, against a base model with basic instructions on three foundation models, and against the Fo harness with its guardrails switched off. Fo completes 71% of the errands and keeps the user's trust on 94% of the trap runs. The base models complete 50% to 64% and keep trust on 59% to 75%. On the matched controls, Fo goes ahead slightly less often. OpenClaw, a popular open-source assistant given the same access, completes 42% of the errands it shares with Fo, against 71%, and keeps the user's trust on 74% of the shared trap runs, against 94%. Measuring trust and completion together, on the whole system rather than the model alone, is how we think action agents become safe to hand real work to.

---


### 328. [Residual Diffusion Implicit Models](https://arxiv.org/abs/2609.33020)

**<font color=#1a73e8>作者：</font>** João Guerreiro, Pedro Tomás, Helena Aidos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve state-of-the-art results across multiple tasks. However, in inverse problems, standard initialization from pure Gaussian noise misaligns the generative process with real-world degradations. More recent methods such as diffusion bridges impose strict endpoint constraints and often require long reverse processes that are prone to hallucinations. Alternative consistency models provide noise-invariant, one-step mappings but lack inherent variance modeling and can degrade under severe corruption. Hence, residual diffusion implicit models (RDIMs) are proposed, constituting a generalized framework that explicitly models the residuals between high-quality (HQ) and low-quality (LQ) images, aligning the forward process with the actual degradation. A non-Markovian implicit reverse sampler is derived, which can skip intermediate timesteps, enabling accurate few-step or even single-step reconstruction, while mitigating the hallucinations inherent to long diffusion chains. RDIM also introduces a controllable variance mechanism that interpolates between deterministic and stochastic sampling, balancing fidelity and diversity. Furthermore, it enables the straightforward use of perceptual losses, when needed. Experiments on denoising and super-resolution benchmarks demonstrate that RDIMs consistently outperforms the state of the art, including bridge and consistency models, in terms of PSNR, SSIM, and LPIPS, reducing hallucinations while requiring only a few sampling steps (often just one). The results position RDIMs as an efficient solution for a broad range of image restoration tasks.

---


### 329. [SRE-Marathon: A Continuous, Change-Driven Benchmark for Autonomous Site Reliability Agents](https://arxiv.org/abs/2609.33023)

**<font color=#1a73e8>作者：</font>** Yifang Tian, Yingjian Bai, Yifeng He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks for site reliability engineering (SRE) agents are typically episodic: one fault is injected, the agent receives an incident task, and its response is scored. Production operation is not. Incidents surface through noisy alerts, overlap in time, and often originate from code or configuration changes. We present SRE-Marathon, a benchmark for long-horizon, continuous SRE operation. An agent is invoked at a fixed cadence with cumulative alert history and a persistent workspace while operating a live two-zone Kubernetes deployment as a fault orchestrator injects overlapping faults according to a seeded, production-calibrated schedule. Curated code and configuration changes deployed through the same build pipeline available for repair. Each run is recorded into a sealed bundle and scored offline: Marathon-Score credits each injected fault for ordered progress through correlation, localization, and repair, with all metrics computed deterministically from recorded system evidence. Across three applications and about sixty faults per run, the best of 10 methods reaches only 41.3 out of 100. Agents often correlate and localize faults, but almost never complete repairs while the faults remain active.

---


### 330. [Low-Rank Single-Index Bandits with Unknown Links: From Matrices to Tensors](https://arxiv.org/abs/2609.33025)

**<font color=#1a73e8>作者：</font>** Zhongxuan Liu, Yue Kang, Thomas C. M. Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank matrix and tensor bandits exploit structured interactions but typically assume a known reward link. Recent single-index bandit methods accommodate unknown links without directly exploiting matrix or tensor rank. We address this gap by studying stochastic matrix and tensor bandits with an unknown shared Lipschitz link and a low-rank index parameter under known regular candidate distributions and finite-variance noise. For monotone links, T-ESTOR combines robust, rank-adaptive Stein estimation with epoch-based greedy selection. Under exact selected-score access and a uniformly positive selected-design Stein signal, it achieves square-root regret with dimension dependence determined by the low-rank structure. For every admissible design, the monotone lower bound matches the rank, dimension, and horizon dependence up to logarithmic factors at large horizons, for fixed menu size and model/design constants. For nonmonotone links under a nonzero base-law Stein signal, T-BSTOR combines structured estimation with robust bin-based learning and attains the optimal $\widetilde{O}(T^{2/3})$ horizon rate for fixed dimensions, menu size, and model/design constants. Synthetic and CCLE-based experiments illustrate the benefits of structured estimation relative to vectorized and competing single-index baseline methods.

---


### 331. [Łukasiewicz Neural Networks Extended: Residual Architectures and Crystallization Strategies for Interpretable Rule Extraction](https://arxiv.org/abs/2609.33028)

**<font color=#1a73e8>作者：</font>** Carlos Leandro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A feed-forward neural network whose weights are integers and whose activation is the truncated identity implements, neuron by neuron, the connectives of Łukasiewicz many-valued logic. This exact correspondence --- established theoretically by Castro and Trillas and developed into a training algorithm by Leandro --- enables \emph{symbolic knowledge extraction}: training produces not a black-box model but a logical formula. Two obstacles have limited the approach to shallow architectures and small datasets: crystallization (forcing weights to integers) succeeds only probabilistically under the original Levenberg--Marquardt training scheme, and the theoretical guarantees break down as networks grow deeper.
This paper addresses both obstacles. First, we prove that \emph{residual connections} (skip connections of the kind used in ResNets) extend Łukasiewicz neural networks to arbitrary depth while preserving the symbolic correspondence \emph{at merge neurons} by construction: merge neurons in a Łukasiewicz residual block automatically satisfy the neuron-classification proposition, regardless of the inner layer weights; inner-layer neurons are trained toward representability by the crystallization strategy. Second, we analyse three crystallization strategies --- Levenberg--Marquardt (corrected), straight-through estimation (STE), and proximal regularization --- characterizing their theoretical guarantees, failure modes, and interpretability trade-offs.

---


### 332. [What Must a World Model Distinguish for Planning?](https://arxiv.org/abs/2609.33030)

**<font color=#1a73e8>作者：</font>** Rongzhe Wei, Hans Hao-Hsun Hsu, Peizhi Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models simulate the consequences of action candidates, but good planning need not preserve every physical distinction required for accurate prediction. We formalize this gap through a hierarchy of mechanism, response, and decision sufficiency. Given a candidate set, the planning query determines which physical variations matter and how precisely they must be preserved: coarse decisions can discard much of the information needed for prediction, whereas fine decisions may require nearly the same resolution. In practice, planners often adaptively search to construct candidates, and information unnecessary for final selection may still be needed to discover good candidates. What a world model must preserve therefore depends on the query, the candidate set, and the planner. We study these effects in a collision system, nonlinear dynamics, and robotic planning. These varying requirements raise a design question: where should query information enter the planning system? A model that jointly generates actions and outcomes conditioned on the query achieves lower regret than an action-conditioned world model on seen objectives, but this advantage largely disappears when generalizing to unseen objectives. Motivated by this, we propose a modular design in which the query determines where to look and an action-conditioned model predicts what will happen, allowing the same predictions to be reused across objectives.

---


### 333. [DevelopmentODE: Structured Neural ODEs for Early Brain Development Dynamics Across a Decade](https://arxiv.org/abs/2609.33048)

**<font color=#1a73e8>作者：</font>** Kaiqiao Han, Haitao Chen, Bryan Quah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how individual brain development unfolds over childhood requires modeling developmental trajectories from sparse longitudinal observations. Long-term neurodevelopmental forecasting is challenging because each child is typically observed at only a few irregularly spaced visits, while developmental dynamics vary across individuals and age. Generic continuous-time models accommodate irregular timing but often absorb these factors into a single flexible transition function, providing little structure for how population progression, individual variability, and developmental age shape the dynamics. We propose DevelopmentODE, a structured continuous-time framework that organizes population- and subject-specific variation within a shared developmental geometry while allowing the governing dynamics to evolve with age. The model builds this geometry around a developmental canal representing the population trajectory, whose local direction provides a reference for organizing subject-specific variation. Subject deviation velocities are constrained relative to this direction, while a shared nonlinear deviation field captures individual developmental motion without disrupting population-level progression. DevelopmentODE further models developmental non-stationarity through ordered age-dependent deformations of the shared vector field, progressively adapting a common dynamical structure as age changes, while elapsed time determines the integration horizon. This formulation uses population-level developmental structure to guide learning from sparse individual trajectories while allowing dynamics to evolve smoothly with age. We evaluate DevelopmentODE on longitudinal fMRI by predicting future functional connectivity of the same child from earlier observations. DevelopmentODE consistently outperforms competing baselines across short- and long-horizon predictions.

---


### 334. [BudgetVerify: Budget-Tiered Verification for Financial QA](https://arxiv.org/abs/2609.33052)

**<font color=#1a73e8>作者：</font>** Janet Jenq, Hongda Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial question answering often requires precise numerical extraction, unit handling, and arithmetic over tables and text, but applying expensive verification uniformly wastes test-time compute. We propose BudgetVerify, a budget-tiered generator-verifier framework that routes each generated answer to one of three verification tiers: no verification, lightweight check-and-revise, or higher-cost solve-first-then-compare verification. The router is trained from offline correctness and token-cost outcomes and, at test time, selects a verification tier using information available before verification, including the question, context statistics, the generated answer, and associated generator metadata. The selected tier either returns the generated answer directly or invokes the corresponding verifier. Across six commercial and open-weight base models, BudgetVerify consistently produces more efficient accuracy-cost Pareto frontiers than fixed verification policies by selectively allocating stronger verification only when it is useful. Although absolute performance varies across models, these efficiency gains and the resulting qualitative frontier shape are consistent across generator models.

---


### 335. [Deep Learning Techniques for Phoneme Recognition in Italian Children' s Speech](https://arxiv.org/abs/2609.33060)

**<font color=#1a73e8>作者：</font>** Nicola Barbaro, Cristina Gena, Francesco Petriglia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech therapists often face difficulties diagnosing impairments due to the lack of efficient tools for transcribing speech into the International Phonetic Alphabet (IPA). This work addresses this challenge with Broca, a Conformer-based deep learning system pretrained on 8 days of adult speech and fine-tuned on a 165-minute dataset of Italian child speech collected through a range of standardized diagnostic tests for children aged 3.5-6.5. Broca was optimized to handle phonetic variability in children's speech, including tone, accent, and speech errors, and achieved a state-of-the-art weighted Phoneme Error Rate of 13.36% on Italian speech. Remarkably, this performance was obtained using less than three hours of child-specific data, underscoring the model's efficiency and robustness in low-resource clinical settings. This work demonstrates that accurate, vocabulary-independent speech-to-IPA transcription can be achieved with minimal data, paving the way for more accessible, data-efficient tools to support speech assessment and diagnosis.

---


### 336. [Zero-Storage Procedural Neural Synthesis via Boundary Dynamics: Formal Verification in Lean 4 and Bare-Metal Gauntlet Validation](https://arxiv.org/abs/2609.33066)

**<font color=#1a73e8>作者：</font>** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contemporary neural inference architectures rely on dense floating-point weight matrices stored in high-bandwidth memory (VRAM), incurring severe memory-wall bottlenecks and preventing native execution inside deterministic virtual machines like the Ethereum Virtual Machine (EVM). Verifying termination and arithmetic invariants for recursive dynamical systems over continuous domains is generally undecidable in the Blum-Shub-Smale model. Here, we present the formal verification and bare-metal empirical validation of WERR (Waves & Errors) and Phase III Orbital Error Dynamics (OED), a non-tensor decision paradigm that procedurally synthesizes non-linear decision boundaries on demand from a 24-byte coordinate seed $\Theta = (c_x, c_y, \text{zoom})$ along the boundary of the Mandelbrot set ($\partial\mathcal{M}$). By projecting the recurrence $z_{n+1} = z_n^2 + c$ onto the modular residue ring $\mathbb{Z}/9\mathbb{Z}$ and the fixed-point domain $\mathbb{Q}_{16.16}$, we establish ten machine-verified theorems in Lean 4 (v4.34.1) with Mathlib4 and zero unproven conjectures (sorry): proving $\mathcal{I}_3 = \{0,3,6\} \subset \mathbb{Z}/9\mathbb{Z}$ ideal closure, universal fuel-bounded halting ($\le 9$ and $\le 12$ steps), absence of $\mathbb{Q}_{16.16}$ square overflow below $2^{63}-1$, non-constant boundary escape sensitivity, and a parametric EVM gas bound ($\le 22,557 \le 24,000$ gas). Evaluated on a 40-core Dual Intel Xeon server, the vectorized 36-iteration CPU kernel processes 100,000 decisions in 6.49 s (15,397 decisions/s, 0 Bytes VRAM, 15.15x speedup), while a sigmoidal outlier gate suppresses 100.00% of adversarial spikes while preserving 89.60% of clean baseline signals.

---


### 337. [Algorithmic Harms Associated with Generative Model-Augmented Recommendation Systems](https://arxiv.org/abs/2609.33073)

**<font color=#1a73e8>作者：</font>** Christine Herlihy, Xumei Xi, Shloka Desai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we consider algorithmic harms that may arise as generative models are incorporated into machine learning platforms. We argue that existing harm taxonomies and threat models require extension to (1) address novel causal drivers of well-studied representational and quality-of-service harms; and (2) anticipate and mitigate endogenous harms, such as sanitization, which may arise when system inputs are misaligned with the system designer's objectives, or the generative model's inductive priors. To this end, we introduce an expanded taxonomy of algorithmic harms associated with the use of generative models in non-conversational recommendation systems. In addition, we offer a causal analysis of how problematic subsets of the (input, output) joint distribution can arise, in an effort to inform harms detection and mitigation efforts.

---


### 338. [QureRadEmbed: Structuring Radiological Similarity through Attribute and Reasoning Supervision](https://arxiv.org/abs/2609.33075)

**<font color=#1a73e8>作者：</font>** Janhavi Prabhu, Sahil, Shivam Ashok Shukla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radiological similarity depends on disease relationships and on fine details such as laterality, lobe, severity, size, and certainty. Broad biomedical similarity can overlook these qualifiers, particularly when several attributes vary together. We introduce QureRadEmbed, a 4B radiology-aware encoder trained with two complementary signals: RadSim supplies deterministic, attribute-decomposed ranking targets, while RadThought aligns reports with hierarchical evidence and reasoning descriptions. A three-stage curriculum combines these signals with report triplets, finding perturbations, and single- and cross-attribute contrasts. The final model achieves 0.996 mean ordering accuracy across ten controlled synthetic attributes and raises Spearman correlation with the designed joint-attribute targets from 0.501 to 0.976. On external findings-to-impression retrieval, Recall@1 reaches 10.5% on Open-I, 12.4% on testing XR, and 42.9% on testing CT, compared with 6.6%, 5.7%, and 31.4% for its backbone. Frozen embeddings support finding extraction with only 100 labeled testing-XR reports (macro-F1 0.481 versus 0.412 for the backbone). Whole-report comparison costs 8.8 seconds per 1,000 pairs in our benchmark, versus 2,755.1 seconds for the generative evaluator GREEN. Sentence-level comparison improves sensitivity to local discrepancies, although generative evaluation remains stronger on several expert-rated and subtle-error tasks. The results support reusable radiology-aware representations for search, structured report indexing, and efficient report comparison.

---


### 339. [NutriVision: Ingredient-Conditioned Fusion and Prediction for Single-Image Food Nutrition Estimation](https://arxiv.org/abs/2609.33076)

**<font color=#1a73e8>作者：</font>** Aman Kumar, Avinash Anand, Chaitanya Lakhchaura 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nutrition estimation is a fundamental task in consumer diet tracking, clinical dietetics, chronic disease management, sports and hospital nutrition, and broader food computing systems. The existing approaches have progressed along two largely separate axes, vision models that rely on calibrated RGB-depth captures and ingredient-aware methods that use textual cues but use limited multimodal fusion. We introduce NutriVision, an end-to-end framework that leverages visual geometry and ingredient semantics to estimate calories, mass, fat content, carbohydrates, and protein from a single RGB image and an optional ingredient list. It obtains the unavailable depth modality using DepthAnything-V3 and encodes ingredient descriptions using CLIP. It integrates three complementary mechanisms: (1) an \emph{Ingredient-Conditioned Frequency-Aligned Fusion Module (IC-FAFM)}, which uses textual guidance to reweight and align RGB-depth frequency components; (2) an \emph{Ingredient-Aware Mask-based Prediction Head (IA-MPH)}, whose gating and channel masks are conditioned on food identity; and (3) modality-specific \emph{Internal Semantic Modeling (ISM)} blocks. On the Nutrition5k dataset, NutriVision achieves a mean PMAE of $\mathbf{13.60\pm0.10\%}$, outperforming our IGSMNet implementation by $0.89$ percentage points and OmniFood8k by $2.90$ percentage points (both $p<0.001$). The module-level ablations identify the ingredient-aware prediction head as the primary architectural contributor, improving mean PMAE by $1.50\pm0.17$ percentage points ($p<0.001$). These results demonstrate that ingredient-conditioned prediction and frequency-aware RGB-depth fusion provide measurable gains for single-image nutrient estimation. More broadly, NutriVision offers a practical route toward nutrition-assessment systems that exploit geometric and semantic cues without requiring specialized depth-sensing hardware

---


### 340. [Parameter-Efficient 3D Segmentation of Liver and Liver tumors: Depthwise factorization Scales Better Than Dense Convolution with Spatial Dimensionality](https://arxiv.org/abs/2609.33077)

**<font color=#1a73e8>作者：</font>** Adham M. Alkhadrawi, Mohammed A.B. Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional dense convolutional networks are the strongest performers on volumetric medical image segmentation, but their parameter counts scale poorly: moving a dense k x k convolution to k x k x k multiplies its weights by k. We observe that depthwise separable factorization does not share this penalty. Because the cubic kernel term applies only to the depthwise stage while the pointwise projection, which dominates the parameter count, is unchanged, the same architecture grows by 5 % from 2D to 3D where a dense convolutional U-Net grows by 200 %. We exploit this asymmetry to build a 3D U-Net with 536,990 parameters, 24x fewer than an identical dense 3D U-Net. On MSD Task03 Liver (the Medical Segmentation Decathlon liver task, derived from LiTS), evaluated per case under five-fold cross-validation over all 131 public volumes, the model reaches a tumor Dice of 0.577 (95% CI [0.518, 0.633]) and a liver Dice of 0.947 (95% CI [0.941, 0.952]). Its liver Dice exceeds previously reported performance. Its tumor Dice exceeds their low-resolution configuration (0.4701) by 0.107 and their 2D configuration (0.5394), at approximately one twenty-fourth of the parameters and roughly half the in-plane resolution. Trained under identical conditions on a common held-out split, it exceeds a dense 3D U-Net on liver by +0.031 Dice (paired p = 0.006) and on tumor by +0.041 (95 % CI [+0.005, +0.081], paired p = 0.056), suggesting the factorization also acts as a regularizer in the small-data regime characteristic of medical imaging. We further show, on both LiTS and a 2D endoscopy benchmark, that a large fraction of the network's learnable spatial filters can be replaced by fixed shifts at no cost in accuracy, but that replacing all of them is measurably worse, the placement of spatial capacity matters more than its total amount.

---


### 341. [The limits of exactness: On the failure of automatic differentiation in physics-informed machine learning](https://arxiv.org/abs/2609.33078)

**<font color=#1a73e8>作者：</font>** Ameya D. Jagtap  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic differentiation (AD) lets neural networks compute derivatives of governing equations to machine precision, and this precision has made it the computational backbone of physics-informed machine learning. Yet exactness in the mathematical sense is not the same as fidelity to the physics. Here I argue that a derivative can be numerically perfect and still be the wrong derivative for the problem at hand, because AD, by construction, has no notion of the physical structure a solution must obey. Convection and its associated directionality, diffusion, and dispersion are only the most visible instances of a much longer list that spans all branches of computational science and engineering, including conservation, thermodynamic consistency, symmetry, symplectic structure, positivity, monotonicity, and boundedness. Recognizing this broader gap reframes how the field should build the next generation of PDE-driven neural surrogates.

---


### 342. [Structure-Mapping-Guided Self-Explanation for Learning Mathematical Procedures](https://arxiv.org/abs/2609.33079)

**<font color=#1a73e8>作者：</font>** Shinhaeng Lee, Christopher J. MacLellan, Daniel Weitekamp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Worked examples are a powerful form of instruction, but learners must infer how the demonstrated steps were produced. A naive simulation of this self-explanation process can generate thousands of numerical explanations that reproduce one observed change without capturing its underlying procedure. We propose structure-mapping-guided self-explanation as a computational account of the cognitive biases that reduce search effort and make this inference tractable. The model represents mathematical expressions as typed relational structures and uses structure mapping to identify corresponding source and target regions. For each changed target value, the corresponding source region serves as an anchor: it guides abductive search toward structurally relevant values and operations before broader alternatives, yielding ordered, executable candidate procedures with inspectable source evidence. Across 70 mathematical transformations containing 120 changed numeric components, the model recovered every intended procedure. It returned the intended procedure before any other computation producing the same target value in 104 subproblems (86.7%), compared with a median of 32 (26.7%) across 100 unguided runs that tested candidate calculations in random order. Our proposed model also tested 93.8% fewer combinations of values and operations than unguided search before reaching the intended procedures. These results provide an efficient, interpretable account of how relational structure can guide procedural learning and a testable hypothesis about human self-explanation from worked examples.

---


### 343. [QSCP: Beyond Class-Name Prompts for Query-Guided Semantic Change Parsing](https://arxiv.org/abs/2609.33088)

**<font color=#1a73e8>作者：</font>** Yuan Qian, Jie Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional change detection (CD) identifies changes between bi-temporal remote sensing images, while semantic change detection (SCD) assigns predefined land-cover classes. However, mapping all changes may not meet a user's specific needs. Referring change detection (RCD) enables selective retrieval through category prompts. However, existing category-prompted RCD uses the queried category to specify the destination of a change and returns only a binary mask of the corresponding regions. Users may instead request a particular transition and paired semantic maps to understand what changed into what. Such requests require explicit source and target reasoning beyond target-class localization. To address these needs, we propose query-guided semantic change parsing (QSCP), which supports category names, synonyms, and intent-bearing sentences and returns a query-specific mask with paired temporal semantic maps. QSCP parses requests into intents and semantic slots, composes bidirectional visual evidence, and predicts both temporal states with a query-conditioned decoder. On SECOND, QSCP outperforms RCDNet on synonym, sentence, and transition queries and improves end-to-end semantic prediction over evaluated semantic baselines. WHU-CDC experiments further assess cross-dataset transfer and consistency across equivalent expressions without target-domain training. Code is available at this https URL

---


### 344. [Geometry-Aware Operator Families for Structured Representation Learning](https://arxiv.org/abs/2609.33089)

**<font color=#1a73e8>作者：</font>** Zuyuan Zhang, Fei Xu Yu, Tian Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The geometry of latent representations governs which components should interact and how information should propagate, making geometry-aware operator design a fundamental ingredient of structured deep representation learning. However, existing neural architectures typically rely on generic operator templates or geometry-specific constructions, creating a need for a unified framework that can derive admissible operators directly from fixed structural information while remaining adaptive to changing contexts. We introduce \emph{Geometry-Induced Operator Families} (GIOF), a general framework that converts fixed geometry into a structured family of propagation operators and dynamically selects an appropriate member of this family according to the current context. GIOF first transforms geometry-derived interaction channels into reusable generator bases, then combines them through a context-dependent selector and adaptive propagation scale, and finally realizes the selected operator through stable continuous-time propagation and a bottleneck residual layer. We establish theoretical guarantees covering parameter compression, identifiability, stability, locality, compositional structure, and oversmoothing behavior, while controlled experiments validate these mechanisms and experiments on PEMS-BAY and METR-LA achieve the lowest mean MAE across all reported regional-outage settings, improving over the strongest retained baseline by 2.4\%--8.8\% at 30\% missing sensors.

---


### 345. [How Linear Attention Remembers](https://arxiv.org/abs/2609.33093)

**<font color=#1a73e8>作者：</font>** Kichang Lee, JaeYeon Park, Songkuk Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention replaces the growing key--value (KV) cache of standard attention with a fixed-size recurrent state, substantially reducing memory growth with context length. This efficiency, however, changes how past information is stored: many tokens must share and repeatedly update the same memory. We study how this recurrent state functions as a memory system. Using an analytical decomposition together with controlled causal interventions in pretrained GLA and GDN models, we trace how recalled information is written, retained, and later accessed. We find that fact-specific information enters recurrent memory through concentrated, content-dependent writes and is later accessed through concentrated query-time read pathways. Multiple facts can remain selectively accessible within the same state, yet their internal representations exhibit cross-fact causal coupling rather than independent KV-like storage. As memory load increases, both recall and targeted editability degrade, whereas elapsed context alone has a substantially smaller effect within the tested regime. Causal interventions on subsequent writes further show that interference is shaped by their overlap with existing memory. Finally, in hybrid architectures that combine recurrent layers with full attention, the runtime memory directly supporting recall shifts predominantly to the full-attention KV state. Together, these results reveal how fixed-size recurrent memory supports selective recall despite shared storage, while exposing the interference and capacity limits that distinguish it from token-addressable KV memory.

---


### 346. [Query, Align, and Distill: Navigation-Aware Cross-Modal Interaction for Efficient Vision-and-Language Navigation](https://arxiv.org/abs/2609.33097)

**<font color=#1a73e8>作者：</font>** Zhihao Chen, Yiyuan Ge, Ziyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large-scale Vision-and-Language Navigation (VLN) models deliver strong accuracy but remain costly to deploy due to their large parameter counts and computational requirements. We tackle efficient VLN in two steps. First, we build a high-performing teacher that makes navigation evidence selection explicit and compressible. The teacher introduces a small set of learnable query slots to extract global and local action-sufficient navigable evidence from panoramic observations via a Navigable Query Generator, then progressively grounds these evidence tokens to the instruction with an Instruction-Query Aligner for policy prediction. Second, using this explicit query bottleneck as a distillation interface, we train a compact student by transferring both where to attend and what to do. We distill the teacher's global and local navigable queries with a navigation-aware token-adaptive objective, then further match action distributions during fine-tuning. Experiments on standard VLN benchmarks demonstrate that our student nearly matches the teacher's navigation performance while reducing the number of parameters by 93.65% compared to the teacher.

---


### 347. [Never Emitted: Reporter Attribution in GitHub's Machine-Readable Vulnerability Records](https://arxiv.org/abs/2609.33099)

**<font color=#1a73e8>作者：</font>** Anas Mohiuddin Syed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The CVE record format defines a credits container that names who found or reported a vulnerability, with a typed role per entry. The OSV schema defines an equivalent field. GitHub, which assigns CVE identifiers for advisories in its ecosystems, collects this information from reporters, requires them to accept it, displays it on the advisory page, and serves it through its own REST API. It emits it into neither standardized format. Across 238 GitHub-assigned CVE records whose linked advisory publicly credits at least one party, zero carry a credits container, while all 238 carry metrics and problemTypes, two fields the CVE schema leaves optional exactly as it leaves credits. Across 302 advisories in the same pool we retrieved GitHub's own OSV export file, and zero carry a credits field. The omission is not a property of either format: the Erlang Ecosystem Foundation populates the CVE field on 18 of 18 records in the same pool using a freely available client for CVE Services. In a census of all 4,889 published CVE records in a two-week window, 46.9% carry credits, GitHub's rate is 0 of 570 without any advisory filter, and assigner behaviour is concentrated at the extremes without being exhausted by them: 16 assigners emit the field on no record and 13 on essentially every record, while 8 assigners covering 23% of the records sit in between. A request to close the gap has been open since January 2023; GitHub's stated reason for deferring it is quoted verbatim. We further show that the NVD API schema defines no credits field, so attribution that CNAs do emit does not reach the database most tooling consumes: of 43 credit-bearing records traced from advisory to CVE record to NVD, none retained it. We release the collection scripts and a frozen snapshot of every API response.

---


### 348. [Octree-based Video Representation](https://arxiv.org/abs/2609.33100)

**<font color=#1a73e8>作者：</font>** Rungui Zhou, Chuanzhi Zhou, Yuk-Kit Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models commonly use uniform grids even though visual complexity varies substantially across space and time. We introduce OctVideo, which approximates a video clip with an octree. This hierarchy recursively partitions a spatio-temporal volume into eight subvolumes, so that smooth regions remain coarse while detailed regions receive finer cells. Each leaf stores local RGB values and spatio-temporal gradients, supplemented by a lightweight learned residual. For reconstruction, a Conv1D VAE maps the serialized cells to a regular latent grid and selectively refines details during decoding. Our VAE achieves 36.12 dB PSNR with 38.2M parameters and 189.4 GFLOPs per clip on Kinetics-400 (K400). It also generalizes zero-shot to the high-resolution Densely Annotated VIdeo Segmentation (DAVIS) 2016 dataset with reconstruction quality comparable to the best evaluated models. On both datasets, it requires the fewest model FLOPs and achieves the fastest encoding and decoding among the evaluated models. OctVideo also supports video understanding, achieving competitive recognition performance with few input tokens when trained from scratch. By exploiting the redundancy already present in video signals and efficiently processing sparse structures, OctVideo provides an efficient representation for video.

---


### 349. [CARVE: Breaking Data Barriers in Chip Placement by Harnessing Reusable Expertise](https://arxiv.org/abs/2609.33106)

**<font color=#1a73e8>作者：</font>** Jiefu Zhang, Haixiang Sun, Yang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained macro-placement policies can reduce repeated optimization across circuits, but deployment often exposes them to unfamiliar designs when the original training data are unavailable. Repeatedly fine-tuning a single serving model can overwrite earlier improvements, while simply saving checkpoints does not determine where they can be reliably reused. We introduce Continual Adaptation through the Reuse of Validated Expertise (CARVE), a framework that represents accumulated expertise as a frozen base policy, immutable specialists, and task-specific credentials obtained through local validation. For a new task, CARVE first checks existing specialists and trains a new specialist from the frozen base only when none qualifies. Under fixed task distributions and validation rules that control cumulative error, we establish expected-performance guarantees for repeated reuse. For bounded losses, we also derive matching worst-case bounds on the local samples needed for reliable reuse. In macro placement, a reuse-first follow-up reduces recorded training time by 58.5% (9.66 to 4.01 hours), while mean HPWL gain changes only from 8.41% to 7.86%. In a simulated receiving deployment, imported specialists are reused on six of seven new IBM circuits with no receiver-side training, achieving a 5.76% mean HPWL gain. Navigation studies provide complementary evidence on repair retention and repeated adaptation.

---


### 350. [D-JEPA: Design-Recoverable JEPA Representation with Swappable Physics Decoders](https://arxiv.org/abs/2609.33110)

**<font color=#1a73e8>作者：</font>** Nitin Nagesh Kulkarni, Aashwin Anand Mishra, Yin Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) provide a framework for learning compact representations without directly reconstructing high-dimensional observations. However, in parameterized physical systems, learned representations can entangle geometry with operating conditions and task-specific physical responses, limiting their reuse across prediction tasks. We introduce D-JEPA (Design-recoverable JEPA), a geometry-centric JEPA that computes a compact representation from geometry alone and reuses it across operating conditions and physical response spaces through lightweight physics-specific decoders. An explicit design-recoverability objective encourages the geometry latent to preserve information about the underlying design variables, enabling the representation to support design analysis and optimization. We further identify a case-level collapse failure mode in which target representations become nearly invariant across distinct geometries despite low reconstruction error, and mitigate it using case-level variation constraints and auxiliary target reconstruction. Across four 3D aerodynamic, hydrodynamic, and structural benchmarks, D-JEPA maintains or improves full-field prediction accuracy while achieving near-perfect linear recoverability of design parameters. The frozen geometry representation can be reused at held-out operating conditions and transferred to a structural response task with fewer trainable parameters. Finally, the representation supports differentiable design optimization, with designs validated using high-fidelity CFD, preserving the predicted ranking of candidate designs. These results demonstrate that separating a reusable geometry representation from physics-specific prediction provides a practical representation for scientific surrogate modeling and design.

---


> [!TIP]
> 当前位于：**301-350**（第 7/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
