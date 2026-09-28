# 📦 其他研究 | 2026年09月29日

> 本类共 **225** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-225**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-225**

---

### 201. [AxonSynth: Domain-Randomized Synthetic Data for Zero-Shot 3D Axon Segmentation in Light-Sheet Microscopy](https://arxiv.org/abs/2609.31431)

**<font color=#1a73e8>作者：</font>** Edward Gaibor, Kyriaki-Margarita Bintsi, Carmen Luz Leiva Ureta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of axons in 3D microscopy data is important for analyzing white-matter organization, but dense ground truth labels are expensive to obtain. Existing supervised axon segmentation methods rely on target-domain annotations and can be brittle when tissue type, species, modality, or acquisition conditions change. We present AxonSynth, a domain-randomized synthetic-data framework for training 3D axon segmentation models without manually annotated real training volumes. AxonSynth generates dense synthetic axon labels with orientation priors that reflect realistic fiber configurations and renders them with randomized density, contrast, bias fields, blur, and noise. A three-class 3D U-Net is trained to predict background, axon sheath and intra-axonal space. We evaluate zero-shot transfer on 10 held-out light-sheet microscopy (LSM) patches from macaque and human brain samples labeled with one of three axonal markers, comparing against calibrated thresholding and Frangi filtering using overlap, corrected detection, false-positive, and topology metrics. On macaque samples, AxonSynth achieved the best corrected Dice and corrected precision (0.826 and 0.851), compared with 0.765 and 0.754 for thresholding and 0.685 and 0.762 for Frangi. On human samples, corrected Dice was comparable to thresholding (0.857 vs. 0.868), while component-count error decreased from 22,504 to 3,377. Across all held-out patches, AxonSynth reduced component-count error in 10/10 patches and Euler-characteristic error in 8/10. These results show that synthetic-label domain randomization can reduce dependence on manual axon annotation while supporting synthetic-to-real 3D segmentation.

---


### 202. [Implicit Neural Representation for Hyperspectral Video Compression](https://arxiv.org/abs/2609.31435)

**<font color=#1a73e8>作者：</font>** Alfredo Scalera, Paul Murray, Jaime Zabalza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advent of snapshot cameras, hyperspectral video is becoming more readily available. In recent years, new applications have emerged which have led to increasingly larger datasets. However, hyperspectral video compression remains in the early stages. In this study, we explore the use of implicit neural representation as a candidate solution. We propose a novel extension of an existing RGB video compression model, achieving Bjøntegaard Delta PSNR gains of +4.99 dB and Bjøntegaard Delta rate of -88.88% compared to traditional hyperspectral image compression methods applied frame-by-frame. In addition to reconstruction quality, the effects on downstream task performance are measured in the form of object tracking success. Compared to video compressed with methods based on principal component analysis and JPEG2000 in low data regimes, our proposed method improves tracking area under the curve by up to 23.42% and distance precision by up to 35.56% on examples from the HOT2026 dataset.

---


### 203. [Different Corruptions, Different Signals: Uncertainty and Loss in Federated Data Quality](https://arxiv.org/abs/2609.31454)

**<font color=#1a73e8>作者：</font>** Bradley Scott, Zeqi Luo, Edmond S. L. Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) data corruption can affect either inputs or labels, but it remains unclear whether input-conditional uncertainty and prediction-label loss expose these corruption modes equally. This paper compares two corruption-detection signals in FL: input-conditional uncertainty and prediction-label loss. The uncertainty signal is characterised using a learned aleatoric variance estimate together with Monte Carlo (MC) dropout variance and entropy measures, while the loss is computed against the supplied label. We test these signals against additive image noise and persistent random label flips. On ResNet-20 with CIFAR-10 and SVHN under Dirichlet partitions with data that are not independent and identically distributed (non-IID), the two corruption types behave differently. For persistent random label flips, the within-client per-sample area under the receiver operating characteristic curve (AUC) is 0.85 on CIFAR-10 and 0.95 on SVHN for prediction-label loss, while every uncertainty estimator stays at chance (0.49--0.50). This pattern is consistent with the model remaining confident in the underlying image despite the supplied label being wrong. For image noise, expected-entropy uncertainty rises above chance (0.67 on CIFAR-10 and 0.66 on SVHN), while loss responds comparably (0.64 on both). Each signal is therefore the stronger detector for a different corruption: the prediction-label loss for persistent label flips, and expected-entropy uncertainty for image noise, with its advantage becoming apparent as federation-wide corruption prevalence increases. Robust FL data-quality assessment should match the signal to the corruption rather than rely on uncertainty alone across corruption types.

---


### 204. [Uncertainty-Aware Federated Learning for Infant Movement Analysis](https://arxiv.org/abs/2609.31463)

**<font color=#1a73e8>作者：</font>** Edmond S. L. Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Infant movement analysis provides valuable biomarkers for the early identification of neurodevelopmental disorders. Recent advances in deep learning have enabled automated analysis of infant movements from video-derived skeletal representations, achieving performance comparable to expert assessment for tasks such as General Movement Assessment (GMA). However, most existing approaches rely on centralized training, requiring data from multiple institutions to be collected and stored at a single site. Such assumptions are often impractical in clinical settings due to privacy, governance, and data-sharing constraints. To address these challenges, we present, to the best of our knowledge, the first federated learning framework for automated infant movement analysis and General Movement Assessment using skeletal motion data. As a clinically relevant use case, the proposed framework is evaluated on fidgety movement classification. To quantify model confidence, Monte Carlo (MC) Dropout is employed to estimate predictive uncertainty during inference. Building upon this, we propose an Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy that incorporates predictive entropy derived from MC-Dropout into the federated aggregation process, enabling client contributions to be adjusted according to their predictive uncertainty. Experiments were conducted using a cross-subject evaluation protocol under a three-client federated learning setting. Results demonstrate that federated learning substantially improves classification performance compared with independently trained local models while achieving performance approaching that of centralized training. Furthermore, UA-FedAvg and its variant incorporating validation loss generally outperform conventional FedAvg across the evaluated data-split configurations.

---


### 205. [Scaffold: Support Graph Theory Based Sparsification for Graph Neural Networks](https://arxiv.org/abs/2609.31466)

**<font color=#1a73e8>作者：</font>** Siddhartha Shankar Das, Sai Karthik Navuluru, S M Ferdous 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) rely on message passing over graph edges, making their computational and memory costs strongly dependent on graph density. Graph sparsification offers a natural way to reduce these costs, but removing edges indiscriminately can distort important communication structure and degrade predictive performance. We introduce Scaffold, a topology-based, unsupervised graph sparsification framework derived from support graph theory preconditioners. Scaffold explicitly controls two complementary structural quantities: dilation, which measures the length of rerouting paths induced by removed edges, and congestion, which measures how strongly these rerouted paths concentrate on the retained support. By jointly controlling dilation and congestion, Scaffold preserves short communication paths while avoiding structural bottlenecks. To our knowledge, Scaffold is the first scalable GNN sparsification framework to use a joint supporting-path dilation-congestion criterion. Across 19 homophilic and heterophilic benchmarks spanning small to large graphs, Scaffold achieves the best aggregate rank among the evaluated sparsification and related methods. Using only 10%-50% of the original edges per sparse support, Scaffold recovers or closely approaches full-graph GNN performance while using less than half the memory of full-graph training and reducing end-to-end training time, including sparsification overhead. We provide an open-source software package at this https URL.

---


### 206. [Verifiable Randomness for Blockchain-Based Lottery Systems](https://arxiv.org/abs/2609.31485)

**<font color=#1a73e8>作者：</font>** Gonçalo Ferreira, André Zúquete, Paulo Bartolomeu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As lotteries and other high-stakes decentralized applications increasingly depend on unpredictable randomness for their operations, the lack of a secure and transparent on-chain random number generator that is verifiable by all participants remains a critical open problem. Various approaches to blockchain-based random number generation have emerged over the years, each with their own strengths and limitations, and have consistently been superseded as blockchain technology evolved. This paper surveys existing approaches to on-chain randomness and proposes a new platform that builds upon the well-known commit-and-reveal scheme while directly addressing its principal vulnerability, the last revealer attack, in which the final participant can withhold their reveal in order to bias or abort the output upon seeing an unfavorable result. We further compare this solution with prior approaches and evaluate its entropy properties. The proposed architecture combines a web-based front-end with a Solidity smart contract deployed on the Polygon 2.0 blockchain. Implemented and tested on the Amoy testnet, the prototype is low-cost and simple to deploy, providing a practical, accessible proof-of-concept for verifiable on-chain randomness.

---


### 207. [UQ-LOB: Uncertainty-Aware Limit Order Book Mid-Price Forecasting](https://arxiv.org/abs/2609.31491)

**<font color=#1a73e8>作者：</font>** Derrick Gilchrist Edward Manoharan, Eljas Linna, Kestutis Baltakys 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting short-horizon mid-price movements from limit order book (LOB) data is central to algorithmic trading, yet most deep LOB forecasters are point predictors: they output a direction or a displacement, but never indicate which of their forecasts can be trusted. We introduce UQ-LOB, a lightweight, encoder-agnostic uncertainty quantification module that attaches to any pretrained LOB encoder and, in the spirit of attentive neural processes, conditions each forecast on a context set of recently completed windows whose outcomes are already realised. The UQ-regression variant outputs a calibrated Gaussian over the future tick displacement, while the UQ-classification variant outputs a categorical distribution over down/up/stationary. Both expose a scalar confidence (predicted signal-to-noise ratio or class probability) that supports selective prediction. On 5.2 billion LOB events across seven cryptocurrency assets and horizons of 5, 10 and 15 seconds, UQ-regression attains near-nominal 68% interval coverage, and restricting to the most confident 10% of predictions raises directional macro F1 by 0.11-0.15 for UQ-regression and 0.05-0.11 for UQ-classification, at every horizon. On large, economically meaningful moves, the tightest confidence tier reaches a directional F1 of 0.88 (down) and 0.83 (up) at the 5-second horizon.

---


### 208. [Toward verifiably private learning from federated data](https://arxiv.org/abs/2609.31494)

**<font color=#1a73e8>作者：</font>** Katharine Daly, Yu Xiao, Zachary Garrett 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) allows devices with private data to collaborate in training a shared model. We present a next-generation FL system based on Trusted Execution Environments (TEEs) that addresses operational challenges associated with earlier systems and provides externally verifiable central Differential Privacy (DP) guarantees for the first time while offering a better privacy-utility tradeoff. In our system, devices upload data encrypted with keys managed by a TEE-hosted Key Management Service (KMS). The uploaded data is cryptographically tied to a policy limiting the set of Python programs that may later process the data in server-side TEEs. External parties may inspect public transparency logs to observe the set of workloads allowed by these policies. Our experimental results show that the new system improves device coverage and favorably shifts privacy-utility curves by enabling collected data to be integrated into the server-side workload at a schedule that optimizes DP guarantees and is unaffected by device availability. Our new system has been productionized, enabling models for the Android Keyboard (Gboard) to be trained faster and achieve better accuracy under smaller, now externally verifiable privacy budgets in comparison to models trained using the prior system.

---


### 209. [ClearGS: Reliability-Aware Gaussian Splatting from Handheld Videos](https://arxiv.org/abs/2609.31509)

**<font color=#1a73e8>作者：</font>** Xuanzhi Liu, Xinyi Wu, Hang Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ClearGS for 3D Gaussian Splatting (3DGS) from handheld videos with uneven viewpoint coverage and mixed frame quality. Rather than selecting frames with binary decisions, ClearGS uses Reliability-aware View Allocation (RVA) to assign graded raw-supervision weights based on appearance reliability, degradation risk, and geometric utility, while weakly reactivating useful suppressed frames to maintain trajectory coverage. Since weighting cannot restore details lost to blur or distortion, ClearGS further introduces Render-Guided In-Video Restoration (RIVR). The current 3DGS render provides a pose-aligned structural candidate, a frozen no-reference restoration expert restores the corresponding raw video observation without any clean reference image, and no-reference perceptual scores select among the render, restored observation, and high-frequency fused candidate. ClearGS then applies Full-Trajectory Repair Consolidation to revisit accepted repairs and preserve details introduced early. On GS2E and GSOTM, ClearGS achieves state-of-the-art overall performance, with consistent CLIP-IQA and MUSIQ gains and LPIPS reductions in most degradation settings, without paired sharp supervision or matched clean references.

---


### 210. [Fast and Secure Simultaneous Authentication of Equals for WPA3](https://arxiv.org/abs/2609.31519)

**<font color=#1a73e8>作者：</font>** João Ferreira, André Zúquete, Hélder Gomes  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Simultaneous Authentication of Equals (SAE) protocol, introduced in WPA3, provides robust protection against offline dictionary attacks against a network Pre-Shared Key (PSK) and also protection of session keys from other people knowing that PSK. However, its high computational cost for the Password Element (PE) derivation makes Access Points (APs) vulnerable to CPU exhaustion Denial-of-Service (DoS) attacks. This paper proposes a resilient architectural modification to SAE. First, we introduce an asymmetric resource cost model that offloads the iterative discovery of cryptographic elements to the client, allowing the AP to maintain a fixed computational load during the handshake. To further mitigate brute-force attempts, we implement a mechanism based on a slow-path key derivation (with variable cost key derivation functions, such as PBKDF2 or Argon2), incorporating a deliberate processing delay on the supplicant. Finally, we introduce a ticket-based mechanism to facilitate efficient re-authentication for known devices, bypassing expensive exchanges while preserving system availability under adversarial conditions. Experimental results demonstrate that this architecture significantly mitigates DoS risks without compromising legitimate network access.

---


### 211. [HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.31531)

**<font color=#1a73e8>作者：</font>** Xinglong Luo, Yuding Zhang, Yuheng Kuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning under partial observability and shared rewards requires assigning team outcomes to individual agents and high-order coalitions. A MAPPO-style critic compresses joint behavior into one global value, while critics that dynamically reconstruct the grouping topology change the mapping from agents and coalitions to value components as interactions or active agents evolve. We refer to this inconsistency as structural target drift. We introduce HySTAR, a MAPPO-based framework that separates adaptive representation learning from a temporally consistent high-order value-decomposition basis. HySTAR anchors an overlapping sparse hypergraph as a uniformly covered decomposition scaffold, uses a spatiotemporal encoder to represent physical and task-dependent interactions, and combines temporal and structural relevance to construct agent-specific advantages. Experiments on SMAC, GRF, Traffic Junction, and MPE demonstrate consistent improvements over MAPPO-style, value-factorization, and dynamic-grouping baselines. On the hardest SMAC settings, HySTAR achieves relative gains of 16.7\% over MAPPO and 15.6\% over HYGMA, ranks first on all six GRF scenarios, reduces Traffic Junction convergence epochs by up to 40.2\% relative to MAGIC, and obtains the highest MPE episode rewards. Controlled topology, agent-death, neighborhood, and parameter analyses support the benefit of anchoring the decomposition scaffold while adapting the propagated representations.

---


### 212. [NEXT: Physics-Informed Neuro-Spectral Exponential Time Differencing Architectures](https://arxiv.org/abs/2609.31539)

**<font color=#1a73e8>作者：</font>** Márcio Marques, Leonardo Mendonça, Leonardo M. Moreira 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) build neural representations of time-dependent PDE solutions, naturally incorporating physics knowledge and observational data, which makes them well suited to both forward and inverse PDE problems. PINNs, however, are known to suffer from spectral bias and lack of causality. Neuro-Spectral Architectures (NeuSA), a recently proposed alternative to PINNs, mitigate both issues, but their numerical integration becomes unstable for stiff differential equations arising in many relevant physical problems. This study proposes Neuro-Spectral Exponential Time Differencing Architectures (NEXT), which combines the spectral representation of the PDE solution in NeuSA with high-order exponential integrators. Within this approach, the linear stiff part of the vector field induced by the PDE is integrated exactly through matrix exponentials, while the possibly nonlinear remainder is modeled by a neural network. The effectiveness of NEXT is verified through benchmark experiments on a set of stiff PDEs, in which NEXT is stable and accurate while NeuSA diverges numerically. It is also shown that NEXT can be applied to inverse problems, where the model has to learn unknown parameters or boundary conditions from sparse data. All code used in this work is publicly available at: this https URL .

---


### 213. [A Flow Matching Framework for Neural Representational Dissimilarity](https://arxiv.org/abs/2609.31544)

**<font color=#1a73e8>作者：</font>** Zeyuan Ye, Xue-Xin Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural representational dissimilarity quantifies differences between neural response distributions, and is essential for comparing neural codes across stimuli, brain areas, tasks, and models. Commonly used distance metrics involve different assumptions and are estimated with separate methods. Here, we show that a variety of distance metrics can be unified under a flow matching framework developed in deep generative models. That is, these distances arise as Jeffreys divergences under different velocity constraints. We find that flow matching has advantages for estimating distances involving complicated distributions and continuous variables. Furthermore, this framework enables the design of new distance metrics in a principled way. Together, flow matching provides a unified approach for understanding, estimating, and designing neural representational dissimilarity metrics.

---


### 214. [BeatGraph: Self-Supervised Heartbeat Graphs for Infant ECG Representations from the Home Environment](https://arxiv.org/abs/2609.31546)

**<font color=#1a73e8>作者：</font>** Mohammad Nur Hossain Khan, M. S. Krafczyk, Beverly G. Bolster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) foundation models typically tokenize the signal into fixed-length patches that ignore cardiac structure, so a patch may split a heartbeat and the number of beats in each patch shifts with heart rate. This matters most for infants, whose heart rates are higher and whose ECG differs from the adult, clinic-recorded 12-lead data these models are built on. A model for infant ECG should therefore reason about heartbeats directly rather than recover them from arbitrary patches. We propose BeatGraph, which makes the heartbeat its unit of representation, modeling each 30-second window as a graph of beats. A shared beat encoder embeds each heartbeat from its waveform and inter-beat intervals, a Transformer with positional encoding orders the beats in time, and residual graph attention layers relate every beat to every other before attention pooling yields a window embedding. We pretrain BeatGraph on our new corpus of unlabeled infant recordings by predicting masked-beat embeddings, then fine-tune it for each task. One backbone supports sleep-wake detection, infant-state classification, activity-source identification (infant- or caregiver-initiated movement), and affect recognition, improving macro-F1 over the strongest baseline on each task by 0.076 to 0.158. It also transfers across age groups, reaching 0.892 AUROC on the ZZU-pECG pediatric benchmark (ages 0 to 14), within 0.001 of the best published self-supervised ECG model, and matching that model under linear evaluation on the adult PTB-XL benchmark despite infant-only pretraining. Finally, to our knowledge, we release the first public infant ECG corpus collected in homes, classrooms, and laboratory settings with state and affect labels. It contains 3,408 hours of single-channel ECG from 143 infants aged 3 to 11 months, with unlabeled pretraining data, benchmark tasks, and subject-level splits.

---


### 215. [MexHat: A Dataset for Hate Speech Detection in Mexican Spanish Videos](https://arxiv.org/abs/2609.31553)

**<font color=#1a73e8>作者：</font>** Itzel Tlelo-Coyotecatl, Hugo Jair Escalante  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring online safety through content monitoring had raised Hate Speech Detection as a crucial task to be addressed. By essence the task demands the capture of contextual cues, which are essential for a precise understanding of the content's intent. Although automated detection approaches for the task have advanced significantly, the scarcity of non-English resources persists, limiting the ability of models to adapt to the subtle, context-dependent, and culturally related nature of multimodal content. In this paper, we introduce MexHat, a video dataset designed to capture the linguistic and cultural cues for the hate-speech detection task in a Mexican Spanish context. Our dataset comprises around 1k video clips annotated across two tasks: a three-way class evaluation (no negative content, offensive content and hate-speech content), and a fine-grained class evaluation including three hate-speech sub-categories. The dataset statistics and the baseline results highlight the inherent challenges associated with the task. Disclaimer: This paper contains sensitive content that may be disturbing to some readers.

---


### 216. [Region-Level Black-Box Defense Against Stealthy Embedding-Space Backdoors in CLIP](https://arxiv.org/abs/2609.31558)

**<font color=#1a73e8>作者：</font>** Ahmed Abdelnaby, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language--Image Pretraining (CLIP) has emerged as a dominant vision backbone due to its strong transferability and zero-shot capabilities. However, recent studies reveal a critical vulnerability: embedding-space backdoor attacks. By poisoning only a tiny fraction of image--text pairs, adversaries can implant stealthy triggers that induce targeted shifts in CLIP's joint embedding space. Unlike conventional backdoors that manipulate classifier logits, these attacks corrupt representations directly, making them highly effective under extremely low poisoning ratios and difficult to detect. Existing defenses require access to model parameters, gradients, logits, or clean validation data---assumptions that rarely hold in realistic black-box deployments. Moreover, current black-box methods struggle to accurately localize small or out-of-distribution triggers. We propose CLIPGuard, a lightweight and fully black-box defense specifically designed to mitigate embedding-space backdoors in CLIP encoders. CLIPGuard identifies malicious regions by measuring segment-wise embedding perturbations and selectively purifies only suspicious segments via semantic inpainting, preserving benign visual content and alignment quality. Extensive experiments on STL-10, ImageNet, and diverse trigger families---including BadCLIP, BadNets, blended, patch-based, and typographic attacks---demonstrate that CLIPGuard reduces attack success rates to as low as 1.05% while maintaining clean accuracy up to 86.34%, consistently outperforming existing black-box defenses, including CleanCLIP and CleanerCLIP. Our code is available this https URL

---


### 217. [Online Learning via Learned Latent Bayesian Tracking](https://arxiv.org/abs/2609.31559)

**<font color=#1a73e8>作者：</font>** Guy Gerson, Tomer Raviv, Nir Shlezinger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online learning in non-stationary environments requires models to adapt rapidly from streaming data under strict computational constraints. A principled approach casts online learning as Bayesian state tracking, where model parameters are updated sequentially via Bayesian filtering. However, applying Bayesian filters directly to modern deep models is computationally prohibitive due to the high dimensionality of parameter space, forcing existing methods to rely on restrictive approximations or manually designed low-dimensional subspaces. In this work, we identify the absence of a suitable low-dimensional dynamical representation as the core bottleneck in Bayesian filtering-based online learning. Accordingly, we propose Adaptive Update through Representation Adaptation (AURA), a meta-learning framework that learns offline a low-dimensional latent state-space model governing the evolution of optimal model parameters under distribution shift. Online adaptation is then performed via extended Kalman filtering in this learned latent space followed by reconstruction of the full model parameters through a learned lifting map, enabling efficient single-step online adaptation while preserving model expressiveness. Evaluated on online adaptation of neural wireless receivers under time-varying channels and on non-stationary image classification, AURA shows substantial improvements in adaptation speed, accuracy, and computational efficiency over existing online learning and Bayesian filtering baselines, demonstrating that an adaptation-aware latent geometry is beneficial for effective Bayesian online learning in high-dimensional models.

---


### 218. [Generalization behavior of OPTQ and the role of regularization](https://arxiv.org/abs/2609.31560)

**<font color=#1a73e8>作者：</font>** Erin George, Rayan Saab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large neural networks can be compressed by rounding or "quantizing" their weights to numbers that admit representations with fewer bits. One algorithm for quantization, OPTQ, progressively quantizes the weights of a neural network so that the squared quantization error on a specified calibration dataset is as small as possible. We study the performance of OPTQ and a variant algorithm, stochastic OPTQ, in a generalization setting and derive bounds for the expected squared error accrued by the algorithm when a test point is drawn from a fixed distribution. We prove two results. One result relates the generalization error to the error on a calibration dataset comprising independent samples from the same distribution as the test distribution. The other result bounds the generalization error of stochastic OPTQ for all sufficiently nice distributions, regardless of the calibration dataset. In both of these results, the regularization term $\lambda$ plays an important role. We use insights from these results to make a new recommendation for the choice of $\lambda$ and see that this choice of $\lambda$ preforms favorably in experiments when compared to prior recommendations in the literature.

---


### 219. [Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights](https://arxiv.org/abs/2609.31564)

**<font color=#1a73e8>作者：</font>** Irene Tallini, Daniele Solombrino, Alberto Cazzaniga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that neural network weights can be explicilty fintuned to admit a smaller grammar. Weight Pair Encoding (WeightPE) does so by placing a lossy Re-Pair compressor inside a straight-through estimator. The int8 weights of the network are flattened into one string, and near-matching Re-Pair patterns are made exactly equal within a global L2 budget. The network computes with the rewritten weights and trains through them with a straight-through estimator. Unlike a flat codebook of fixed-size entries, a grammar offers variable-length patterns and reuses them hierarchically inside larger ones. On the MLP weights of ViT-B/16 and ViT-L/16 finetuned on CIFAR-10, WeightPE produces a Re-Pair grammar 0.43x and 0.38x the size of the one produced by an equivalent int8 QAT run, at a cost of 1.9 and 1.1 accuracy points. The trend extends to different grammar compressors (LZ78, SEQUITUR), over which the networks has not be finetuned against. To our knowledge, this is the first time grammar size has been used as an explicit training objective for network weights.

---


### 220. [Adapting for AI: How elementary teachers adjust their practices for an AI-integrated curriculum](https://arxiv.org/abs/2609.31569)

**<font color=#1a73e8>作者：</font>** Fasika Melese, Ruiyang Wu, Xinyue Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI tools are entering children's everyday experiences, and schools are interested in adopting them. However, successful classroom integration depends not only on the technology but also on the work teachers do to make it usable and appropriate for their students and classroom context. There is little known about how elementary teachers work as they implement conversational AI tools in real classrooms. In this study, we examine three teachers' experiences implementing an AI literacy and English Language Arts (ELA) curriculum built around ToyTalk, a conversational AI toy development platform, over 13 instructional days, a three-week summer camp. Drawing on daily individual reflections, group reflections, and post-camp interviews, we find that teachers' adaptive practices of repair, differentiation, translation, and balancing sit at the intersection of three tensions (technology, learner, and instruction). Teachers' understanding of AI and their role evolved over the camp experiences. From these findings, we contribute design implications and considerations for deploying conversational AI within elementary classrooms.

---


### 221. [OC-GS: Gaussian Splatting for Irregular Turntable Capture](https://arxiv.org/abs/2609.31572)

**<font color=#1a73e8>作者：</font>** Jae Joong Lee, Bedrich Benes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uneven rotation and dropped frames make equal-angle assumptions unreliable for turntable reconstruction. We present OC-GS, an object-centric Gaussian splatting that refines each image's angle while maintaining a shared camera, rotation axis, and pivot. This orbit-consistent refinement jointly optimizes image-derived geometry and angles to reconstruct objects from sparse, irregular captures. On rendered objects with 12, 8, and 6 irregularly spaced views, OC-GS achieves mean foreground PSNR scores of 21.26, 19.36, and 15.83dB, respectively, exceeding all four evaluated pose-free Gaussian splatting baselines in each condition. Under a shared trainer, refining image-estimated angles improves mean foreground PSNR by 7.88dB over keeping those estimates fixed. An ablation study shows that both image-derived angle initialization and the shared motion model contribute to the improvement. On real captures, OC-GS's refinement increases mean foreground PSNR by 0.70dB. Results show that refining uncertain angles within a shared motion model improves reconstruction from sparse, irregular turntable captures.

---


### 222. [How Far Can INRs Go? Cross-Domain Parameter-efficient INR-Based Semantic Segmentation for Brain MRI](https://arxiv.org/abs/2609.31573)

**<font color=#1a73e8>作者：</font>** Ziyao Shang, Pouya Sadeghi, Letian Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biomedical image segmentation is central to medical image analysis, but practical deployment often faces limited annotations, memory constraints, and cross-site distribution shifts. Implicit Neural Representations (INRs) have recently emerged as a lightweight alternative for semantic segmentation, achieving competitive performance with substantially fewer parameters than conventional architectures. However, the mechanisms, scaling behavior, and domain generalization abilities of INR-based segmentation remain insufficiently understood. In this work, we study these questions in the context of cross-domain brain MRI segmentation. We analyze INR-based segmentation across low-parameter regimes, comparing it with conventional pipelines in both in-domain and out-of-domain settings. Surprisingly, we find that INR-based models do not simply improve with increasing parameter budget. Their advantage is most pronounced under low-parameter and limited-augmentation settings, while U-Net-based models benefit more from larger capacity and standard augmentation. We also investigate how INRs encode semantic information in their hidden features and show that complementary segmentation-relevant structure is distributed across multiple INR layers. Building on this insight, we introduce HierINRSeg, a hierarchical INR-based architecture that aggregates multi-layer representations for improved robustness and generalization. Extensive experiments show that HierINRSeg consistently outperforms MetaSeg, a strong recent INR-based segmentation baseline, with an average improvement of 5.6 percentage points in Dice for the in-domain test set and 8.2 percentage points out-of-domain. Overall, our analysis identifies the conditions under which INR-based segmentation is most effective, providing concrete guidance for model selection and future research.

---


### 223. [Trust Guided Decision Transformer](https://arxiv.org/abs/2609.31586)

**<font color=#1a73e8>作者：</font>** Chainesh Gautam, Raghuram Bharadwaj Diddigi, Chandramouli Kamanchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision Transformer performance degrades on long rollouts because the conditioning context drifts out of the training distribution. We show that this drift is visible through the model's own next state prediction error, which rises during rollout and stays elevated, giving a direct signal of when context has become unreliable. We introduce Trust Guided Decision Transformer (TGDT), which selects context before applying value guidance. At each step, TGDT evaluates several recent context suffixes using rolling next state prediction error, calibrated against held out offline data via split conformal prediction. It keeps only suffixes whose error stays within the calibrated threshold, then uses a frozen critic to choose the highest value action among the trusted suffixes. This reverses the order used by value only elastic selection, where the critic may choose an action generated from a context the model itself has flagged as unreliable. Experiments on D4RL navigation and locomotion tasks show that state prediction, critic guidance, and hard context reset each solve only part of the problem. TGDT reduces persistent high error runs and improves return over vanilla Decision Transformer, reset based context control, and value only context selection.

---


### 224. [Common-Mode Collapse and Recovery in Direct Feedback Alignment](https://arxiv.org/abs/2609.31589)

**<font color=#1a73e8>作者：</font>** Varun Reddy, Bernardo L. Sabatini, Houman Safaai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct feedback alignment (DFA) trains hidden layers through fixed random projections of output error. With tanh hidden units and independent sigmoid outputs, plain stochastic gradient descent can stall near the loss of a constant predictor of class frequencies. We trace this stall to the error's common mode, the component shared across inputs. An exact mean-covariance decomposition separates a rank-one update formed by the mean teaching signal and mean presynaptic activity. Its leading component drives tanh units toward saturation. At initialization, random feedback provides no systematic correction of the shared error on average; readout learning limits its duration. A reduced model initialized from the network, without fitted parameters, predicts the concentration of activation sensitivity across 48 settings. On MNIST, class decodability largely survives collapse, but readout learning remains slow at a fixed learning rate. Adam learns faster despite deeper collapse. Calibrating the baseline readout to the class prior suppresses collapse and speeds learning; weaker feedback trades less collapse for slower learning. Replacing errors by their signs sustains collapse; subtracting the signal's batch mean prevents sustained collapse and improves learning in the tested setting. Related effects occur in deeper and convolutional networks and on CIFAR-10, with severity and cost depending on the readout, optimizer and input statistics.

---


### 225. [FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620)

**<font color=#1a73e8>作者：</font>** Hongyang Du, Yunfei Xie, Junjie Ye 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation autoencoders (RAEs) reuse features from a pretrained visual encoder as reconstruction and diffusion latents, integrating strong visual representations into image generation. However, RAEs still need to decide which encoder layers form the shared latent space for the generator and pixel decoder. This choice involves a trade-off. Shallower layers tend to preserve fine pixel details better, while deeper layers tend to yield better generation metrics. A fixed heuristic layer fusion therefore couples two stages that benefit from different information. We introduce FuseReg, which replaces heuristic feature selection with training over random subsets of encoder layers. We theoretically analyze the underlying mechanism: subset sampling explicitly penalizes sensitivity to cross-layer disagreement. On ImageNet-256 with DINOv3-L, a single FuseReg decoder reconstructs from full, sparse, and single-layer fusions without retraining, achieving higher PSNR than decoders specialized to fixed fusions. This flexibility also benefits generation: decoder replacement alone reduces unguided gFID by 27% with an unchanged RAEv2 DiT-XL generator. The same regularization principle extends to diffusion training, with joint regularization of both stages reducing unguided gFID by 29% on DiT-Base. These results show that training downstream models for layer-fusion robustness narrows the reconstruction-generation gap without modifying the pretrained encoder.

---


> [!TIP]
> 当前位于：**201-225**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-225**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
