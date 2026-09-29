# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 151. [Topology-Adaptive Hyperbolic Graph Attention Networks Guided by the Hyperbolic Sombor Index](https://arxiv.org/abs/2609.32275)

**<font color=#1a73e8>作者：</font>** Haifang Cao, Boan Tao, Xiyuan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic geometry has emerged as a principled space for representing hierarchical graphs. However, existing hyperbolic graph neural networks typically rely on shared curvature configurations and feature-driven attention, failing to explicitly exploit local hierarchical topological patterns. To bridge this gap, we introduce the Hyperbolic Sombor Index (HSO) as a lightweight structural prior for capturing hierarchy-indicative degree stratification. Building on this, we propose \textbf{HSO-GAT}, a topology-adaptive hyperbolic graph attention network that unifies geometric adaptation and message propagation. Specifically, it comprises two complementary modules: HSO-Guided Local Curvature Adaptation, which performs adaptive node-wise geometric scaling from aggregated node-level HSO signals, and HSO-Gated Hyperbolic Graph Attention, which enables structure-aware message passing through feature-conditioned gating. Theoretically, we establish the monotonic sensitivity of edge-level HSO to degree imbalance and analyze the validity and radial scaling properties of node-adaptive hyperbolic mappings. Extensive experiments on eight benchmark datasets demonstrate that HSO-GAT consistently achieves state-of-the-art performance in both node classification and link prediction tasks.

---


### 152. [HyperLabel: Multi-Label Classification via Hypergraph-Based Label Correlation Modeling](https://arxiv.org/abs/2609.32276)

**<font color=#1a73e8>作者：</font>** Peiyu Zhang, Heng Ping, Nikos Kanakaris 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label classification (MLC) requires predicting multiple relevant labels for each instance, where a central challenge is modeling complex label dependencies arising from co-occurrence patterns. Existing approaches are limited in capturing high-order label correlations, relying on implicit learning through contrastive objectives or pairwise attention mechanisms without structural guidance. We propose HyperLabel, an encoder-decoder framework that explicitly models label dependencies through hypergraph neural networks. Our contributions are twofold: (i) We construct a label hypergraph where sample-defined hyperedges naturally encode multi-way co-occurrence patterns, providing explicit structural prior knowledge that captures relationships beyond pairwise interactions. (ii) We propose a unified cross-modal learning approach where HGNN+ performs bidirectional message passing to integrate feature information with label structure, and a shared cross-attention decoder processes both modalities through complementary learning objectives. Extensive experiments on seven benchmark datasets demonstrate that HyperLabel achieves state-of-the-art performance, with particularly significant improvements on macro-F1 scores (+10.3% on Delicious, +8.2% on Bibtex), validating that explicit hypergraph structure effectively captures complex label relationships. The code is available at this https URL .

---


### 153. [SIMANF: Sample Free Learning of Unnormalized Distributions via Simulated Annealing in Normalizing Flows](https://arxiv.org/abs/2609.32279)

**<font color=#1a73e8>作者：</font>** Vikas Kanaujia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficiently learning and sampling from high dimensional, multimodal unnormalized distributions without target samples remains a challenging problem. Although normalizing flows can generate samples efficiently, training based on the reverse KL divergence using only the unnormalized target density may suffer from mode collapse. We introduce SIMANF, a sample free framework that integrates simulated annealing with normalizing flows. SIMANF progressively transforms the target distribution from a smooth initial form to the original target distribution and trains the flow sequentially across these stages. By transferring the learned representation between stages, the method promotes mode coverage while progressively capturing finer features of the target distribution. Following annealing, a final refinement stage combines the reverse KL divergence with an importance weighted forward KL objective using samples generated by the flow. SIMANF requires no target samples during training and uses only the unnormalized density. We demonstrate its effectiveness on Many-Well distributions and high dimensional Scalar Phi4 lattice field theory distribution.

---


### 154. [Supporting and Performing Culture from the Inside](https://arxiv.org/abs/2609.32281)

**<font color=#1a73e8>作者：</font>** Lea Frermann, Steven Bird  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Anthropology and related disciplines which study culture have often found it useful to consider their epistemological and methodological approaches in terms of emic versus etic. This is the distinction between the insider perspective, how the world is viewed by a member of the culture, versus the outsider perspective, the scientific cataloguing of cultural knowledge and practice. We adopt this framework to systematically analyse assumptions in recent research on culture in NLP along the full pipeline of task selection, data collection, system design and evaluation. We draw attention to the `culture of NLP' which shapes the research focus and approaches of our field, and suggest pathways towards a more culturally attuned AI.

---


### 155. [A Journey to the Edge of Stability](https://arxiv.org/abs/2609.32290)

**<font color=#1a73e8>作者：</font>** Jaerin Lee, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It has recently been found that deep learning often occurs at the "edge of stability (EoS)," where the maximum Hessian eigenvalue of the model is stabilized at a value reciprocal to the learning rate. However, what happens before we reach that regime? We fix a deep learning problem and vary first order optimization methods with dense learning rate sweeps. We then track the characterizing quantities of a learning trajectory: the loss, the sharpness, and the alignment between consecutive gradients. To our surprise, if we scale the learning rate by the dc gain of the optimizer, these traces from the sweeps from different optimizers almost perfectly overlap across a large range of learning rates. The dc-normalized optimizers have another role that only becomes apparent in high learning rates: they select when the sharpness value detaches from this universal curve and enters the edge of stability. Upon this discovery, we specify three distinct regimes with respect to the dc-adjusted learning rate: the low-LR regime where the trajectory is nearly insensitive to the optimizer, the high-LR regime, where the optimizer governs the sharpness according to the EoS reciprocal rule, and the in-between mid-LR regime where so-called progressive sharpening originates independently of the optimizer. This distinguishes the role of the optimizer, the learning rate, and the model in shaping the learning progress.

---


### 156. [FUND: Density Flow for Sampling Unnormalised Distributions](https://arxiv.org/abs/2609.32296)

**<font color=#1a73e8>作者：</font>** Vikas Kanaujia, Vipul Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient sampling from Boltzmann distributions is central to modelling complex physical systems. Markov Chain Monte Carlo (MCMC) methods suffer from critical slowing down, high autocorrelation, and poor mode-mixing, limiting their scalability. Recent advances, like Boltzmann Generators, offer a promising alternative but remain constrained by costly MCMC-based training, inefficient sampling, and poor ergodicity. We introduce an algorithm for learning Boltzmann distributions that does not require any true samples for training. Our approach draws inspiration from flow matching but departs fundamentally from sample-trajectory matching to distribution-trajectory matching. The algorithm iteratively reshapes the target distribution, using model generated samples to guide learning and ensure comprehensive mode coverage. We validate our method on standard benchmarks, including a 2D Gaussian mixture, Many-Well distributions, and high-dimensional scalar $\phi^4$ theory. The proposed approach not only improves sampling performance and accuracy over traditional MCMC and flow-based baselines but also establishes a new method for sample-free learning of complex physical distributions.

---


### 157. [Agentsensus: Consensus-Compressed Shared Memory for Multi-Agent Story Worlds](https://arxiv.org/abs/2609.32297)

**<font color=#1a73e8>作者：</font>** Yu Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A agentic story world is a dynamic system simulating who learned what, when, and from whom -- yet the standard design gives each character a private memory stream. A shared event is therefore stored once per witness, large duplication will be incurred in terms of storage. We present Agentsensus, a story-world simulation framework in which there is an unified long-term memory. Records of the same event merge into one owned by all its witnesses, and semantically relevant memory records are linked. We evaluate on four worlds -- two classical Chinese novels, Hamlet, and a real-world conflict timeline -- run for 40 to 80 rounds against three per-character memory designs under an equal-granularity protocol. Agentsensus writes 22-44% fewer entries than the closest baseline and is the only design whose memory becomes shared (14-28% of records held by more than one character, some by 10) and linked (94-99%), at judged simulation quality indistinguishable or even better than the baselines. An ablation attributes this to the merge itself: disabling it multiplies the store by 3.1x and takes sharing to exactly zero. Sharing also compounds with the horizon rather than saturating early, rising 6% to 9% to 14% as one world is re-run at 10, 20 and 40 rounds.

---


### 158. [Refresh or Realize? Compute Allocation in Drifting Models](https://arxiv.org/abs/2609.32298)

**<font color=#1a73e8>作者：</font>** Sipeng Chen, Xu Zheng, Shibo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting Models train a one-step generator by recomputing a finite-sample drift field at every iteration and taking an optimizer step toward the drifted target. The field says how generated samples should move, but the step is taken in parameters shared by all samples, so the motion the network actually makes need not match the motion it was given. This leaves a basic training question open: should extra compute go into fitting the current target more closely, or into recomputing the field? We study it on ImageNet 256x256. Holding the target fixed for k optimizer steps and measuring the realized displacement, we find that deeper fitting does bring the network closer to the frozen target, and that the number of steps needed before it makes any net progress drops from about sixteen early in training to one later on. When the extra steps come for free, k=2 also lowers FID. Once they are paid for, the result flips: at approximately matched measured wall-clock, spending the budget on fresh fields gives lower FID than deeper fitting, on both training seeds. The target itself shows why a fresh field is worth so much. Redrawing the finite support rotates its direction far more than a parameter update does (cosine ~0.3-0.6 against ~0.95), and a correction that is optimal in field space is not reliably better in FID than a parameter-free one. For Drifting, fitting each target well and spending compute well are different goals.

---


### 159. [When Does Synergy Help Active Feature Acquisition? A PID-Based Study](https://arxiv.org/abs/2609.32301)

**<font color=#1a73e8>作者：</font>** Jie Li, Maruf A. Dhali, Hjalmar R. Bouma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active feature acquisition (AFA) sequentially selects informative features under budget constraints. However, existing policies rarely distinguish whether information contributed by interacting features is redundant, unique, or synergistic. We introduce SynAFA, a state-dependent AFA policy that combines pairwise joint information and conditional information, with Partial Information Decomposition (PID) characterizing its information structure. Across five tabular datasets and MNIST-loop, performance is heterogeneous. SynAFA shows its strongest gains at low budgets on PhysioNet, where synergistic and redundant feature pairs are supported by permutation tests, but its advantage diminishes as budgets increase and does not depend on pair proposals. SynAFA performs significantly worse than nearly all baselines on MiniBooNE, and than CAE on MNIST-loop. Controlled synthetic experiments further show that, within budget, SynAFA's advantage rises as joint information becomes more synergy-dominated, including when total joint information is held approximately constant. Further analyses show that the budget-dependent erosion is not resolved by non-greedy local search, which improves a diagnostic set-level objective but leaves predictive performance no better, often significantly worse, and that improvements in this objective are weakly aligned with the fixed classifier's predictive utility. These findings characterize when pairwise synergy can benefit AFA while exposing a persistent challenge in translating local information into effective acquisition objectives.

---


### 160. [PhiFold: Towards Dynamic Protein Design with Physics-Structured Covariance Modeling](https://arxiv.org/abs/2609.32309)

**<font color=#1a73e8>作者：</font>** Yutian Liu, Mujie Lin, LanqianZhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein design is moving beyond structural correctness toward function-aware design, yet existing generative models typically treat dynamics as a downstream property estimated through simulation or prediction after structure generation. Using MD trajectories as a generative target is also undesirable because stochastic, path-dependent trajectories over-specify the underlying equilibrium ensemble. We introduce PhiFold, a framework for jointly generating protein backbones and their second-order dynamics, represented by residue-displacement covariance. Rather than predicting the quadratically sized full covariance, PhiFold decomposes dynamics into three interpretable components: local flexibility, a low-rank collective-motion representation, and residue-wise collective participation. These components are assembled into a positive-definite covariance matrix with exact marginal consistency, yielding a compact and physically constrained representation of equilibrium dynamics. Across generated proteins, PhiFold improves recovery of local fluctuations and long-range residue coupling while remaining competitive on dominant collective-motion subspaces. It further enables bidirectional control of residue flexibility while preserving backbone designability. By unifying structure generation with an explicit representation of equilibrium dynamics, PhiFold lays a foundation for designing proteins not only by how they look, but also by how they move.

---


### 161. [One Perception, All Maneuvers: Directional Traffic Signal Understanding for Maneuver-Level Signal Intent Prediction](https://arxiv.org/abs/2609.32316)

**<font color=#1a73e8>作者：</font>** Ang Zou, Runzhe Zheng, Zhigang li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic lights are a key regulatory signal for autonomous driving at urban intersections, yet existing traffic signal perception is still predominantly formulated as instance-level detection or color recognition. Such formulations identify where traffic lights are and what colors they display, but leave a critical semantic gap before downstream planning: which ego maneuver is controlled by each visible signal and what dynamic permission the signal expresses for that maneuver.
In this paper, we formulate Directional Traffic Signal Understanding, a decision-oriented task that predicts structured signal states for straight, left-turn, right-turn, and U-turn maneuvers from a front-view image. Each state contains the associated signal color and signal-implied passability. Based on OpenLane-V2, we provide a direction-level benchmark with maneuver-level supervision and metrics for color recognition, passability, full-frame consistency, and safety-critical errors. A direction-aware baseline combines global context, localized traffic-light evidence, and maneuver-specific representations. Experiments show that direction-level modeling improves passability prediction over image-level classifiers and detection-oriented pipelines, particularly at complex multi-signal intersections. The resulting representation provides a direct and interpretable traffic-signal interface for downstream planning together with topology, route, and surrounding-agent information.

---


### 162. [Superposed Inference for Hyperdimensional Computing](https://arxiv.org/abs/2609.32320)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Nilesh Prasad Pandey, Ye Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional computing (HDC) is attractive for efficient and robust learning, but conventional inference still encodes every query independently, repeatedly paying the cost of high-dimensional projection. We introduce SupHDC, a new inference paradigm that processes multiple queries through a shared encoding computation. SupHDC assigns lightweight random slot keys, superposes the keyed queries before encoding, and uses slot-specific classifiers to recover their individual predictions. A random-feature kernel view explains why exact recovery of each hypervector is unnecessary: inference only needs to preserve the class evidence that determines the prediction. Across ten datasets, SupHDC achieves 1.39x analytical speedup with no average accuracy loss, and up to 2.08x speedup with only a 2.67 percentage-point mean accuracy loss. On a Raspberry Pi~5, it delivers 2.01x measured wall-clock speedup with a 2.26 percentage-point loss in mean prediction accuracy. SupHDC shows that high-dimensional redundancy can be used not only for robustness, but also as capacity for shared inference.

---


### 163. [Not All Errors Matter: Decision-Relevant Prediction Error Predicts Planning Quality](https://arxiv.org/abs/2609.32322)

**<font color=#1a73e8>作者：</font>** Linhao Wang, Yiyan Fan, Dongjin Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are typically trained and evaluated by prediction error, assuming that more accurate predictions lead to better decisions. We show that this assumption can fail because models with similar total error can differ substantially in planning performance when their errors occur on different state dimensions. We introduce Decision-Relevant Prediction Error (DRPE), which measures prediction error on the state dimensions that affect decisions. We also develop an iso-error evaluation protocol that varies error allocation while keeping total error fixed. In a factored gridworld with known state relevance and a standardized planner, we evaluate 55 controlled and learned models across different error levels and allocations. Total prediction error is weakly related to planning success (Spearman $\rho=-0.25$), whereas DRPE is strongly predictive ($\rho=-0.84$; $-0.98$ within the controlled family). Models with only a 1\% difference in total error can differ by 60 percentage points in planning success (97\% vs 37\%). The relevant error also depends on the task, with model rankings reversing across tasks at the same total error. Deeper imagination further amplifies decision-relevant errors, while learned models exhibit systematic bias on rare but decision-critical events. We formalize sufficient conditions under which DRPE correctly ranks models and total prediction error cannot.

---


### 164. [Active Feature Acquisition With Incomplete Training Data](https://arxiv.org/abs/2609.32325)

**<font color=#1a73e8>作者：</font>** Reza Rezvan, Valter Schütz, Han Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many prediction tasks, acquiring all features can be a prohibitively expensive or outright impossible task. Further, in many cases a static subset of features may not be enough to solve the problem sufficiently across various instances. Active Feature Acquisition (AFA) addresses these problems by formalizing the trade-off between feature cost and predictive performance during sequential feature selection. However, prior AFA work largely assumes access to complete training data, an assumption that is often violated in practice. Here we study AFA with Incomplete Training Data (AFA-ITD), showing that under missing completely at random (MCAR) data, one-step acquisition values remain unchanged, whereas multi-step values can decrease. We analyze three approaches to learning from incomplete data: aliasing, filtering, and generative restoration. We show that filtering can require a number of training instances scaling exponentially with the dimension, whereas generative restoration scales exponentially with the acquisition budget. We empirically test our theory on a controlled experiment and across common AFA datasets and find that missingness mainly damages methods that exploit multi-step acquisitions and that generative restoration is able to recover lost performance in many experiments. Code is available at this https URL.

---


### 165. [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326)

**<font color=#1a73e8>作者：</font>** Ziqiao Shang, Zian Xu, Ji-Chen Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal reasoning requires models to preserve visual evidence through long decision chains while selecting appropriate procedures across diverse scenarios and rules. When learning is guided only by terminal verifiers, reinforcement learning (RL) reveals whether a final answer is correct but not how it should be produced. The policy must therefore discover reusable reasoning procedures while learning to execute them, creating a program cold-start problem. Skills can externalize successful procedures, reduce repeated exploration, and provide inspectable guidance. However, a fixed Skill Bank assumes that this guidance remains compatible with an evolving policy, while updating Skills alone can leave their triggers, execution protocols, and demonstrations stale or mutually inconsistent. We introduce RLHARNESS, which organizes Skills, selection and execution protocols, few-shot demonstrations, and task contracts into a unified, versioned Harness and alternates Harness evolution with policy learning. An Exploration-Distillation Harness builds the initial Harness and version-aligned verified traces for SFT and DAPO I. After the first RL block, a Post-RL Reconstruction Harness rebuilds Skills, protocols, and demonstrations from fresh success-failure rollouts, and DAPO II adapts the policy to the reconstructed program. RLHARNESS improves Accuracy from 16.25%/27.50% to 62.00%/50.00% on MetroMap/TravelMap and raises F1 score from 37.13%/45.50% to 65.81%/65.51% on Fee-VL/Cancel-VL. All four tasks achieve their best results only after reconstruction and DAPO II, showing that an evolving Harness complements RL by continually updating the external program that the policy learns to execute.

---


### 166. [Continual Data Unlearning in Diffusion Models via Transition-based Regularization](https://arxiv.org/abs/2609.32328)

**<font color=#1a73e8>作者：</font>** Sunbeom Jeong, Sehwan Kim, Sangwoo Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data unlearning in diffusion models aims to remove the influence of specific training examples without suppressing the broader concepts they represent. However, when deletion requests arrive sequentially, updates for new requests can degrade generative utility and undermine earlier deletions. We propose a continual data unlearning framework that uses completed deletion transitions as directional references to regularize future updates. For each request, we record changes in denoiser responses on the same fixed noisy inputs before and after unlearning. Rather than matching full post-deletion responses, we apply a one-sided penalty that discourages reversal along the recorded directions relative to the post-deletion references, while leaving orthogonal response changes and progress beyond these references unpenalized. To keep storage independent of the number of requests, we maintain a fixed-capacity bank of representative transition records. Records are selected based on the local sensitivity of progress along their recorded directions to parameter updates, allowing them to be retained even when their penalties are inactive. Empirical evaluations show that the proposed framework achieves a better balance between deletion persistence and generative utility than existing unlearning baselines as requests accumulate, using only a small transition memory.

---


### 167. [When the Merge Coefficient Stops Mattering: Proximity Regularized Merging for Continual LoRA Adaptation](https://arxiv.org/abs/2609.32332)

**<font color=#1a73e8>作者：</font>** Yixuan Liu, Yuhao Sun, Sen Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rehearsal-free continual learning with parameter-efficient adapters can be cast as a sequence of task-vector write-in operations: for each new task, a low-rank adapter is learned and merged into a running model. We propose Proximity Regularized Merging (PRM), a minimal modification to sequential LoRA merging that adds a proximal penalty during task-vector training without changing the subsequent write-in rule. PRM acts as a robust task-vector regularizer: in the reported Base->+Prox diagnostics, it improves AAA across multiple write-in rules, backbones, and class-incremental settings, while its fixed-coefficient variant remains competitive with strong coefficient-based baselines. Mechanistically, matched-prefix norm controls and proximal-strength sweeps show that proximal training shrinks the task-vector radius, lowers Fisher-weighted interference, broadens the coefficient plateau, and exposes a stability-plasticity trade-off. Together, these results suggest that the effectiveness of sequential LoRA merging depends not only on how much of a task vector is written in, but also on whether the task vector itself has been trained to be mergeable.

---


### 168. [OpenMASC: An Open-Source Pipeline for Cross-Trajectory Metal-Aware Sampling and Correction in Accelerated MRI](https://arxiv.org/abs/2609.32343)

**<font color=#1a73e8>作者：</font>** Zhengyi Lu, Ming Lu, Chongyu Qu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal implants corrupt MRI measurements throughout $k$-space, yet existing accelerated MRI methods assume clean data and most metal artifact reduction approaches assume fully sampled acquisitions. No public dataset provides paired $k$-space and images with and without metal for the same anatomy, and no framework jointly addresses artifact-aware acquisition and reconstruction across sampling trajectories. We present OpenMASC, an open-source pipeline covering the full workflow from data generation to deployment. A physics-based data generation module converts public CT volumes into paired clean and metal-corrupted MRI data in both Cartesian and radial formats. MA-VarNet, an unrolled reconstruction network with a per-cascade DC Rectifier, corrects artifacts that data-consistency steps reintroduce from corrupted measurements. A reinforcement learning agent actively selects $k$-space readouts and co-trains with the reconstruction network through a decoupled three-stage procedure. The framework is trajectory-agnostic except for the data-consistency operator, supporting both Cartesian and radial acquisition without architectural changes. Experiments on two datasets at $4\times$ and $8\times$ acceleration demonstrate consistent improvements over conventional and learned baselines on both trajectories.

---


### 169. [Analog-Friendly Predictive Coding without Activation Derivatives](https://arxiv.org/abs/2609.32350)

**<font color=#1a73e8>作者：</font>** Francesco Innocenti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding (PC) is a local, energy-based alternative to backpropagation (BP) whose iterative inference dynamics make it attractive for implementation on analog hardware. However, standard nonlinear PC requires evaluating the derivative of the activation function during both inference and learning, which can be difficult to realise physically. Here, we introduce \textit{activation-matched Bregman PC}, replacing standard squared-error energies with Bregman divergences matched to the activation function. This formulation eliminates activation derivatives and, when combined with inference via mirror descent, yields local inference and learning rules requiring only weighted sums, local prediction errors, state integration, and the activation function. In digital experiments, Bregman PC performs comparably to standard PC and BP on classification and generative tasks, while preserving characteristic learning dynamics of PC and its convergence to BP under stable large-model parameterisations. These results provide a more analog-friendly formulation of nonlinear PC while retaining its key computational properties.

---


### 170. [Editable Map-Conditioned Trajectory Generation for Human Mobility Simulation](https://arxiv.org/abs/2609.32360)

**<font color=#1a73e8>作者：</font>** Takayuki Mizuno, Shouji Fujimoto, Mikito Hiruki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geospatial simulation of infrastructure interventions requires mobility generators that respond directly to edited maps, yet many data-driven generators do not expose the map as an editable condition. We formulate this task as map-conditioned autoregressive generation of human mobility: a road raster conditions a decoder that emits nominal 31.25 m mesh-cell tokens at one-minute intervals. The mesh-local vocabulary supports held-out and locally edited maps without retraining or vocabulary changes. We instantiate a ResNet-50 visual-prefix configuration and a Vision Transformer (ViT) cross-attention configuration, trained from scratch on 87,400 smartphone-derived trajectories from 874 meshes in Ishikawa Prefecture, Japan; 219 meshes are held out. We evaluate map sensitivity by comparing correct-map and within-split shuffled-map generations with held-out real trajectories. On the 110-mesh test split, for the ResNet-50 configuration, correct-map generations are closer than shuffled-map generations on 60% of meshes under Hausdorff-based energy distance (p = 0.021), while DTW is directional but inconclusive (57%, p = 0.074); correlation with real density is 0.38 with the correct map versus 0.01 with shuffled maps. The ViT configuration shows weaker trajectory-level sensitivity and smaller density gains. An illustrative bridge-removal edit changes generated continuations without retraining. Together, these results support the feasibility of editable-map human-mobility simulation.

---


### 171. [Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation](https://arxiv.org/abs/2609.32361)

**<font color=#1a73e8>作者：</font>** Derui Wang, Zewei Shi, Rayne Holland 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Debate distillation adapts weaker verifiers using multi-agent debate transcripts to improve their judgement in subsequent debates, but gains on monitored tasks do not establish reliability on related unmonitored tasks. We study epistemic reliability degradation, in which adaptation preserves monitored performance while reducing support for correct responses on hidden tasks. We consider an adversarial debater that manipulates debate arguments while defending the correct monitored response, and ask whether the resulting degradation merely reflects catastrophic forgetting and whether standard evaluation can detect it. To address these questions, we propose ER-Audit, a two-stage black-box auditing framework that compares frozen verifier checkpoints before and after adaptation, and introduce two evaluation benchmarks pairing monitored and hidden task prompts grounded in shared contexts. ER-Audit searches for counterexamples to non-degradation by evaluating semantically valid paraphrases and, if none is found, uses independent paraphrases for sequential hypothesis testing. We derive anytime-valid lower confidence bounds on the non-degradation probability, allowing data-dependent stopping within a finite budget. We further establish a common lower bound across fixed paraphrase distributions and extend it to distributions within a bounded total variation distance of their mixtures. Our experiments show that higher hidden-task accuracy can coexist with more counterexamples to non-degradation and lower non-degradation bounds. This divergence challenges explanations based solely on broad catastrophic forgetting and shows that auditing can uncover selective hidden-task degradation concealed by aggregate performance gains. Our code and benchmarks are available at this https URL.

---


### 172. [StegGNN: Learning Graphical Representation for Image Steganography](https://arxiv.org/abs/2609.32362)

**<font color=#1a73e8>作者：</font>** Abhinav Kumar, Shorya Singhal, Agam Pandey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image steganography refers to embedding secret messages within cover images while maintaining imperceptibility. Recent advances in deep learning - primarily driven by Convolutional Neural Networks (CNNs) and architectures such as inverse neural networks, autoencoders, and generative adversarial networks - have led to notable progress. However, these frameworks are primarily built on CNN architectures, which treat images as regular grids and are limited by their receptive field size and a bias toward spatial locality. In parallel, Graph Neural Networks (GNNs) have recently demonstrated strong adaptability in several computer vision tasks, achieving state-of-the-art performance with architectures such as Vision GNN (ViG). This work moves in that direction and introduces StegGNN - a novel autoencoder-based, cover-agnostic image steganography framework based on GNNs. By modeling images as graph structures, our approach leverages the representational flexibility of GNNs over the grid-based rigidity of conventional CNNs. We conduct extensive experiments on standard benchmark datasets to evaluate visual quality and imperceptibility. Our results show that our GNN-based method performs comparably to existing CNN benchmarks. These findings suggest that GNNs provide a promising alternative representation for steganographic embedding and open the field of deep learning-based steganography to further exploration of GNN-based architectures.

---


### 173. [DiffPTS: Rethinking Diffusion ELBO for Probabilistic Time Series Forecasting](https://arxiv.org/abs/2609.32363)

**<font color=#1a73e8>作者：</font>** Weiwei Ye, Dongyuan Li, Hangchen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic time series forecasting requires modeling and predicting complex and time-varying distributions. Recently, Denoising Diffusion Probabilistic Model (DDPM)-based approaches have shown promise by equipping the dif- fusion process with pretrained mean and variance estimators to accommodate distributional shift. However, these methods typically follow the standard DDPM framework and consider only partial components of the evidence lower bound (ELBO), treating the training of estimators as designed regression tasks separate from the variational inference framework. To address this, we rethink the ELBO under the Location-Scale Noise Model (LSNM) and find that it naturally induces a Gaussian negative log likelihood objective for the estimators and inherently defines a joint training objective that unifies recent diffusion paradigms for probabilistic forecasting. Building on this principled ELBO reformulation, we propose Diff- PTS, a general framework that enables end-to-end optimization of all components within the ELBO. Across multiple benchmarks, DiffPTS consistently outperforms recent models, achieving state-of-the-art performance with an average CRPS/MSE reduction of over 14.53%/16.55% compared to existing diffusion-based methods. The code is available at this https URL.

---


### 174. [STRIDE: State-Transition Representation via Increment Dynamics and Evolution](https://arxiv.org/abs/2609.32367)

**<font color=#1a73e8>作者：</font>** Yuchen Xiong, Siming Huang, Jianfeng Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce STRIDE (State-Transition Representation via Increment Dynamics and Evolution), which defines states through derivative fingerprints and learns local functions for state transitions (qpairs), recasting continuous forecasting as transition prediction. Trailing convolution windows estimate local joint-transition frequencies, whose lagged differences form a high-dimensional increment trajectory. Proper orthogonal decomposition (POD) gives coordinate paths, jointly forecast by sparse dynamics with memory. Recombining their forecasts and applying history-anchored inversion recovers future transition distributions; sampled state paths select local functions to generate continuous forecasts. Three-seed experiments compare STRIDE against fourteen baselines across nine benchmark families. Five independent Markov and hidden-state baselines cover all 230 evaluated tasks, with 220 complete whole-horizon pairs. Against these comparators, system-weighted late-Energy win fractions range from 73.6% to 78.5% on 190 multi-step pairs; against DLinear, the fraction is 77.3% on 72 paired multi-step tasks. Matched controls examine the intermediate representation. On 64 independently initialized Aizawa trajectories, late-Energy reductions against four matched controls range from approximately 24% to 56%, with all four prespecified contrasts passing Holm correction. These results connect transition-statistic prediction to continuous probabilistic forecasting, with substantial long-horizon gains in the matched Aizawa study.

---


### 175. [An End-to-End Latent-Rollout Approach for Pushing Few-Step ImageNet-$256$ Generation to FID $1.11$ without Fréchet Losses](https://arxiv.org/abs/2609.32376)

**<font color=#1a73e8>作者：</font>** Xiaoran Xu, Yujing Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative generation poses a joint optimization problem across steps, as intermediate predictions shape subsequent computations and ultimately determine the final output distribution. Few-step generators distilled from pretrained diffusion and flow-matching models make such optimization computationally practical end to end. We build on this opportunity with a distill-then-refine approach that uses teacher imitation to establish a strong initialization for a few-step rollout in latent space, then shifts to end-to-end refinement of the complete latent rollout against real data. We introduce FiST (Flow-in-Stage Transformer), an architecture that composes learned latent-state transitions in a few stages using a shared Transformer, with optional cross-stage hidden communication. Distillation applies teacher-forced regression to selected states along teacher trajectories; refinement replaces this supervision with adversarial and auxiliary classification objectives on the final latent output. A trainable discriminator module operates on semantically rich features extracted from clean real and generated latents by a frozen SiT backbone pretrained with REPA. All training takes place in latent space, without image decoding. During refinement, FiST consumes its own intermediate predictions, and endpoint gradients pass through every generation stage. For class-conditional generation on ImageNet at $256\times256$, our approach achieves FID 1.11 (IS 282) with three stages and FID 1.15 (IS 280) with two. These results demonstrate competitive few-step generation through learned distribution-level supervision, without explicit Fréchet-distance minimization. Ablations characterize how distillation, pretrained checkpoint choices, refinement supervision, and cross-stage hidden communication affect generation quality.

---


### 176. [TimeES: Probabilistic and Deterministic Time Series Forecasting via Evolutionary Spectra](https://arxiv.org/abs/2609.32384)

**<font color=#1a73e8>作者：</font>** Weiwei Ye, Renhe Jiang, Hangchen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series are inherently non-stationary, with trends, periodic patterns, and uncertainty evolving over time. While the Fourier domain offers a natural lens to model time series, current deep learning approaches do not explicitly model evolution and randomness in the Fourier spectra, which limits their ability to accurately predict both the expected trajectory and its uncertainty in non-stationary time series. Motivated by Evolutionary Spectra (ES) theory, we propose TimeES, a general framework that enables probabilistic and deterministic forecasting via the evolutionary spectra theory. Specifically, we derive a parameterizable evolutionary spectra formulation, recasting non-stationary random process modeling as learning an evolving representation modulated by random variables. Furthermore, we reduce the complexity of the estimated spectra from O(NM) to O(NK), where K << M/2, by exploiting Hermitian symmetry and spectral energy sparsity for frequency selection. Based on a simple linear backbone, our proposed TimeES achieves consistent state-of-the-art performance across both deterministic and probabilistic forecasting tasks, with high efficiency and interpretability. Code is available at: this https URL.

---


### 177. [DashAct: A Progressive Diagnostic Benchmark for GUI Agents in Interactive Dashboard Analysis](https://arxiv.org/abs/2609.32385)

**<font color=#1a73e8>作者：</font>** Chuhan Zhang, Qi Xie, Ziyue Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive dashboards require users to reveal and connect evidence across stateful interactions. Although graphical user interface (GUI) agents could automate this process, existing dashboard benchmarks primarily report final answers or task success. They provide limited insight into whether failures arise from maintaining the analytical process, selecting actions, or grounding visual targets. We introduce DashAct, to our knowledge the first benchmark to diagnose these failures at a fine-grained level within the same dashboard task. DashAct contains 357 human-verified interaction trajectories with milestone dependencies and hierarchical target annotations. Its progressive diagnostic cascade evaluates end-to-end execution, restores verified context for next-action prediction, and provides target semantics and a local view for visual grounding. By progressively restoring the conditions for success, DashAct measures the minimum support an agent needs to recover rather than scoring isolated skills. Experiments show that current models struggle even as support is added. The cascade outcomes reveal bottlenecks hidden by end-to-end scores and provide actionable guidance for improving GUI agents.

---


### 178. [Using Machine Learning to Investigate Predictors of Fasting Blood Glucose: Insights into Circadian Timing and Age Interactions](https://arxiv.org/abs/2609.32386)

**<font color=#1a73e8>作者：</font>** Viktoriya Bu-Dager, Silvia Cirstea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Impaired glucose regulation is a major contributor to metabolic dysfunction and type 2 diabetes. This study developed an interpretable machine-learning framework to predict log-transformed fasting blood glucose using metabolic, hormonal, lifestyle, demographic, nutritional, and circadian variables from the National Health and Nutrition Examination Survey 2017--2020 pre-pandemic dataset. After merging multiple NHANES sub-datasets, data processing used a leakage-resistant pipeline in which imputation, scaling, and one-hot encoding were performed only after dataset splitting and within training folds. Elastic Net, LASSO, and XGBoost models were evaluated using 94 candidate predictors and engineered circadian interaction terms. Performance was assessed using mean absolute error, root mean squared error, coefficient of determination, calibration, and Shapley Additive Explanations. The final interaction-augmented XGBoost model achieved strong performance on the independent test set, with a mean absolute error of 0.0804, a root mean squared error of 0.1148, and a coefficient of determination of 0.7761, using 10 predictors. Glycohemoglobin was the dominant predictor, followed by insulin, diabetes diagnosis, gamma-glutamyl transferase, age, race, and gender. Among the engineered interaction terms, sleep midpoint multiplied by age was consistently retained in repeated random-split analyses, although its contribution remained modest relative to dominant glycaemic predictors. These findings support further investigation of circadian-age interactions in metabolic health.

---


### 179. [Reward Hacking and Agent Containment Failure: A Monte Carlo Study Based on the 2026 Hugging Face Incident](https://arxiv.org/abs/2609.32390)

**<font color=#1a73e8>作者：</font>** Murat Ozer, Bulent Erenay, Ibrahim Berber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The July 2026 intrusion into Hugging Face production infrastructure showed how reward hacking can become an external cybersecurity incident when a capable agent encounters weak containment boundaries. This study develops a probabilistic risk model linking five stages: reward hacking, containment escape, usable access, persistence, and failure of detection. A Monte Carlo simulation evaluates 100,000 runs under each of four control configurations. Input distributions represent explicit uncertainty and are used for comparative analysis rather than real-world frequency prediction. Under the stated assumptions, layered controls reduce simulated external-incident probability substantially more than network isolation or monitoring used alone, an ordering that holds under independent plus/minus 25% perturbation of every coefficient in the model across 300 draws. Sensitivity analysis shows that agent capability and weaknesses in monitoring, authorization, and credential control exert the greatest influence on modeled risk. Human temporal discounting and metric gaming provide a behavioral analogy for short-horizon optimization, but the study does not infer that AI agents experience gratification or human motivation. The results support treating cyber-capable agent evaluations as hostile security zones in which indirect egress, shared infrastructure, credentials, and evaluation artifacts must remain outside the agent's effective authority.

---


### 180. [FA-Bench: A Benchmark for Word-Level and Phone-Level Forced-Alignment and ASR Timestamps Under Clean and Noisy Conditions](https://arxiv.org/abs/2609.32396)

**<font color=#1a73e8>作者：</font>** Wei Chu, Yuanzhe Dong, Ke Tan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forced alignment aligns speech audio with a text transcript to generate word and phone timestamps. Published comparisons normalize transcripts, split the data and match boundaries differently, so their numbers cannot be read together. We present FA-Bench, an open framework that fixes those choices once and releases the code, splits, phone mapping, text normalization and scoring script, with results published periodically. Track 1 gives every aligner the reference transcript and Track 2 gives it a recognizer's output, on the same audio, clean and degraded four ways, with 21 open models and 9 commercial APIs under a unified protocol. We score every boundary of an utterance and check the two labels beside it, so a word the recognizer missed or invented is charged. Using a tolerance-based F1 as our primary metric eliminates the 9% to 14% score inflation that standard MAE causes on recognition-dependent systems in conversational speech. We then group boundaries by their position and how many adjacent words were recognized correctly, which shows where a system lost the score. We discovered systematic bias in how current systems time words, with Whisper about 150 ms early and several commercial ASR APIs over 50 ms late. Code and results are at this https URL

---


### 181. [Endo-TSR: Temporal Spectral Modeling of Appearance and Motion for Endoscopic Reconstruction](https://arxiv.org/abs/2609.32399)

**<font color=#1a73e8>作者：</font>** Taoyu Wu, Yiyi Miao, Qi Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endoscopic scene reconstruction requires modeling tissue motion and temporal appearance while recovering fine surface detail. Deformable Gaussian models provide explicit trajectories, but their fixed colour coefficients lack a dedicated temporal representation for photometric changes. We propose Endo-TSR, which augments deformable Gaussian splatting with bounded Fourier colour residuals and independent translation residuals on shared temporal frequencies. The colour residuals capture local appearance changes, while a Matérn spectral prior regularises motion corrections. Multi-scale Laplacian supervision guides tissue-detail recovery during joint image fitting. Extensive experiments on the EndoNeRF and StereoMIS datasets demonstrate state-of-the-art rendering quality, with the highest PSNR across all evaluated sequences. Ablation studies show that temporal appearance yields the largest PSNR gain among the tested component additions, while appearance and detail supervision jointly improve rendering with fixed Gaussian counts.

---


### 182. [Toward On-Chip Training of Spiking Neural Networks for Dense Event-Based Vision](https://arxiv.org/abs/2609.32405)

**<font color=#1a73e8>作者：</font>** Maxime Vaillant, Axel Carlier, Lai Xing Ng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras provide low-latency, asynchronous visual sensing for resource-constrained robotics. Spiking neural networks (SNNs) process event streams naturally, but training deep SNNs with backpropagation through time (BPTT) requires substantial memory and remains difficult on neuromorphic hardware. Local learning avoids this by restricting error propagation to local blocks, but existing methods mainly target classification rather than dense prediction. We introduce DELL (Dense Event-driven Local Learning), a block wise scheme for dense event-based vision that replaces global gradient propagation with local dense supervision. Learnable, spatially structured local heads supervise each block at its appropriate resolution while preserving temporal dynamics within blocks. We evaluate DELL on optical-flow regression and semantic segmentation with a fully spiking U-shaped architecture. On DSEC optical flow, DELL reduces peak training memory by 39.6% relative to end-to-end BPTT while improving accuracy, reaching 1.670 px endpoint error on the official test benchmark versus 1.941 px for the same backbone trained end-to-end. Block detachment behaves more like a regularizer than a constraint. DECOLLE, the existing local-learning baseline, relies on fixed random local read-outs poorly suited to dense regression, resulting in a 3.9x higher endpoint error; learnable local heads recover this loss and outperform end-to-end training across all optical-flow metrics. On segmentation, they recover most of the performance gap, although DELL remains a few mIoU points behind end-to-end training. With 2.3M parameters, 24x fewer than the strongest SNN baseline, the backbone remains competitive with the SNN state of the art on DSEC. These results extend local learning to dense event-based prediction while substantially reducing training memory.

---


### 183. [Automatic Speech Recognition for the Basaà Language: A Low-Resource Approach](https://arxiv.org/abs/2609.32408)

**<font color=#1a73e8>作者：</font>** Sophie Gertrude Ngo Mock, Charles Moudina Varmantchaonala, Paul Dayang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Artificial Intelligence (AI) and Natural Language Processing (NLP) has revolutionized the way humans interact with machines. Among the most impactful developments is Automatic Speech Recognition (ASR), which enables computers to convert spoken language into text. Systems such as those built on deep neural networks, transformer architectures, and self-supervised learning have achieved near-human performance for well-resourced languages such as English and French. Yet, these advances have disproportionately benefited a small fraction of the world's languages.

---


### 184. [Recovery-Directed Symbolic Distillation of Neural Likelihoods](https://arxiv.org/abs/2609.32409)

**<font color=#1a73e8>作者：</font>** Kianté Fernandez, Xinwei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amortized neural likelihoods enable computationally expensive inference for models with analytically intractable or unspecified likelihoods, but their black-box nature limits interpretability. We introduce a symbolic distillation pipeline that converts trained neural likelihoods into explicit, interpretable expressions optimized for efficient parameter estimation. Our approach uses a recovery-directed objective to guide symbolic regression toward expressions that preserve parameter-recovery accuracy rather than merely approximating the likelihood function. Candidate expressions are evaluated on held-out datasets and selected using a criterion that jointly accounts for expression complexity, parameter-recovery performance, and distributional distance from the learned likelihood. We evaluate the pipeline on the diffusion decision model, a classical cognitive model, whose analytically tractable likelihood provides ground truth for controlled evaluation. The proposed recovery-directed objective improves parameter recovery over standard symbolic-regression objectives. The resulting symbolic likelihoods enable over 100 times faster parameter evaluation than both neural likelihoods and, when available, the exact likelihood, while maintaining a manageable loss in precision. We further demonstrate these computational benefits in Bayesian hierarchical inference on empirical data. Our pipeline provides a lightweight interface for integrating symbolic distillation with existing neural-likelihood estimation methods and can be adapted to a range of simulation-based inference settings.

---


### 185. [Carnator: Fast Text-to-Video Generation with Generation-Native Compatibility-Guided Cross-Request Reuse](https://arxiv.org/abs/2609.32420)

**<font color=#1a73e8>作者：</font>** Xingkun Yin, Xuebin Tang, Mingkun Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers produce high-quality videos, yet iterative denoising incurs substantial inference latency, limiting interactive and large-scale serving. Most existing acceleration methods focus on individual requests, thereby restricting efficiency gains to redundancy within a single generation trajectory. Recent cross-request reuse offers an additional source of savings, but existing approaches often infer reusability from coarse semantic similarity. This conflates semantic relatedness with generation-level computational compatibility, so aggressive reuse may accept incompatible historical computation while conservative reuse leaves substantial acceleration unrealized. We present \emph{Carnator}, a cross-request acceleration framework that addresses this challenge by extracting and using generation-native compatibility evidence directly from the model's evolving internal states. Specifically, \emph{Carnator} performs a lightweight early probe to construct an Early Signature from internal diffusion states, assessing reuse validity through risk-aware compatibility decisions. The same evidence characterizes reuse scope by localizing target-specific computation and guiding joint reuse of historical latent trajectories and sparse attention connectivity. Across three text-to-video backbones, Carnator consistently achieves higher cache-hit end-to-end acceleration than the evaluated cross-request baselines despite more selective cache acceptance, reaching up to 2.17$\times$ speedup while maintaining competitive generation quality.

---


### 186. [HoTS: Homophily-Aware Temperature Scaling for Graph Neural Network Calibration](https://arxiv.org/abs/2609.32426)

**<font color=#1a73e8>作者：</font>** Inwoo Tae, Yoontae Hwang, Yongjae Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For graph node classification, calibrated class probabilities are needed when confidence scores, usually the maximum predicted class probability, are used to rank predictions, defer uncertain nodes to human review, or control risk. Existing post-hoc calibrators either apply one global temperature or use graph-aware modules without a principled structural form. We study how local graph structure should enter node-level calibration. Our first results show that a logit-only temperature rule is insufficient when nodes with identical logits but different local homophily require different optimal temperatures. We then analyze a population-concentration contextual stochastic block model with Gaussian features and a one-layer linear GCN. Under equidistant class means, the Bayes posterior over class-template scores is a temperature-scaled softmax whose inverse-temperature is governed by a homophily-dependent signal strength. In the positive-signal homophilic regime, the resulting temperature decreases approximately inversely with normalized local homophily. This law motivates Homophily-aware Temperature Scaling (HoTS), a simple post-hoc calibrator that assigns each node a positive scalar temperature from entropy-based logit concentration and estimated local homophily. HoTS has three temperature parameters, preserves the predicted class, and learns the strength of the structural correction from calibration data. Across 18 node-classification benchmarks, two GNN backbones, and eight calibration baselines, HoTS achieves the best mean Expected Calibration Error (ECE) of 4.79%, the best average rank, and the most reliable confidence ranking in selective classification. Code is available at this https URL.

---


### 187. [Beyond the Manifold Hypothesis: Hybrid Spectral Parameterizations for Flow Matching](https://arxiv.org/abs/2609.32432)

**<font color=#1a73e8>作者：</font>** Ségolène Martin, Anne Gagneux, Quentin Bertrand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching and diffusion can be trained to predict different quantities, most commonly the data $x_1$, the source noise $x_0$, or the velocity~$v$. Although theoretically equivalent, these can lead to substantially different performances. We identify two main drivers for these differences: the source--data signal-to-noise ratio, and the information bottleneck induced by the neural architecture. We show that, beyond intrinsic data dimension, the factor affecting the optimal parametrization the most is a certain signal-to-noise ratio in each data covariance direction. From this analysis, we introduce new \emph{spectral hybrid} parameterizations that adapt across time and data covariance directions; we show that these are optimal for Gaussian data. We also show that architecture-induced compression changes which parameterization is easier to learn, with $v$-prediction being more sensitive to discarded directions than $x_1$-prediction. Experiments across architectures and source scales show that our spectral parameterizations are robust across regimes, can substantially accelerate optimization, while incurring essentially no additional training cost compared with standard parameterizations.

---


### 188. [Controllable GNN Explanations via Multi-Metric Preference Selection](https://arxiv.org/abs/2609.32436)

**<font color=#1a73e8>作者：</font>** Rachit Verma, Yashraj J. Deshmukh, Anirban Dasgupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanisms for generating GNN explanations are crucial for building trust and mitigating biases in Graph Neural Networks (GNNs), especially in high-stakes scenarios. Most current methods optimize only for fidelity under the sparsity constraint. However, this discounts the need for interpretable explanations (those that consist of familiar motif patterns) and stable explanations (those that remain unchanged under structural perturbations). We propose a novel approach that optimizes GNN explanations across these metrics, exposing their relative weighing as a control. Experiments on various real-world datasets, including MUTAG, BA-2Motif, BAMultiShapes, and PROTEINS, suggest that our method produces higher-fidelity explanations than a state-of-the-art baseline on MUTAG and PROTEINS across all evaluated budgets, and on BA-2Motif at larger budgets, while being faster in the regime of small explanation budgets. We also explore how, given an input motif library containing standard motifs for the corresponding domain, the method can be used to determine the relative importance of those motifs in generating the explanations, and how this information can be used to further improve the quality of the output explanations. We also examine the relationship between different metrics through their induced tradeoff surface, and explore its dependence on the nature of the motif library.

---


### 189. [Length-Independent State Tracking Under a Parallel Scan](https://arxiv.org/abs/2609.32447)

**<font color=#1a73e8>作者：</font>** Julien Brandoit, Arthur Fyon, Thomas Braipson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning robust and scalable finite-state tracking is fundamental to sequence processing. While linear recurrent neural networks (RNNs), linear attention, and state space models enable scalable parallel training through affine recurrences, their theoretical expressivity guarantees assume idealized arithmetic and do not extend to finite precision, where the parallel scan that makes them fast is itself a source of perturbation. We formalize finite-state tracking at finite precision and characterize length independence: tracking that stays correct at every sequence length, at a precision cost that does not grow with the length. We show that length-independent state tracking requires two competing dynamics within a single map: contraction to suppress numerical perturbations and separation to keep distinct states apart. We prove that affine recurrences, which offer a single rate at each step to serve both roles, realize at most definite automata at finite precision. Instead of treating scan compatibility as a restriction on the update map, we reinterpret it as a computational budget and introduce the Neural Finite-State Machine (NFSM): a nonaffine, scan-compatible RNN built for length-independent finite-state tracking. On synthetic benchmarks spanning abelian and nonabelian groups, noninvertible monoids, and textual state-tracking tasks, affine baselines fail on every nondefinite task, most of them within a few hundred steps. A single NFSM layer instead learns the exact transition tables of every algebraic task, which certifies correctness beyond the tested lengths, and a stack of NFSMs keeps perfect accuracy on the textual tasks at every tested length.

---


### 190. [De-biasing Skeleton-based Action Recognition with Convex Hull Adaptive Shift](https://arxiv.org/abs/2609.32454)

**<font color=#1a73e8>作者：</font>** Mengyuan Liu, Yuhang Wen, Yi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton sequences can represent both individual actions and multi-entity interactions, encompassing human bodies, hands, objects, and robots. Existing approaches to recognize skeleton-based actions and interactions usually adopt a late fusion strategy, which expects individuals are independent and identically distributed to train a robust weight-shared entity encoder. However, observed entity bias in various skeletal data violates this assumption, leading to suboptimal optimization of backbone models that might produce wrong recognition results. This bias arises from the world coordinate system's initial configuration, where the choice of origin often creates bias in representation. To this end, we propose a Convex Hull Adaptive Shift based normalization method to reduce Entity bias (CHASE), improving performance across a variety of skeleton-based action and interaction recognition tasks. To adaptively apply plausible shifts to the input skeletons, we formulate a plug-and-play parameterized network that ensures the relocated world origin lies within the skeleton convex hull, which avoids non-convergence by limiting the search space. To further minimize entity bias, we incorporate an auxiliary objective that leverages pair-wise distribution distances to guide network optimization. To support both single- and multi-entity actions, we propose a sub-entity strategy that offers a consistent formulation for both scenarios. Moreover, CHASE demonstrates compatibility with various intra-skeleton modalities, such as bones and velocities, highlighting its adaptability. Essentially, our method works as a normalization approach to reduce entity bias, enabling subsequent classifiers to achieve improved recognition performance across diverse settings. Extensive experiments on 7 datasets verify our approach by seamlessly integrating with various backbones and significantly boosting their performance.

---


### 191. [QuacamFM: Quaternion-Constrained Flow Matching for Camera Pose Estimation](https://arxiv.org/abs/2609.32455)

**<font color=#1a73e8>作者：</font>** Bao-Long Tran, Cuong Le, Tahereh Dehdarirad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera pose estimation from multi-view images remains a challenge in computer vision. Traditional methods often address this problem using Structure-from-Motion (SfM) with bundle adjustment. However, camera poses estimated from sparse views are inherently ambiguous due to insufficient geometric constraints. Recent work leverages probabilistic models, such as diffusion models, to generate multiple camera pose hypotheses and therefore capture this uncertainty better. Most of these methods represent camera rotations using unit quaternions, but treat them as unconstrained 4D vectors during the generative processes, thereby ignoring the unit-norm constraint of quaternions. Unconstrained quaternions create non-smooth and suboptimal generation trajectories. To this end, we propose *QuacamFM*, a quaternion-constrained flow matching framework for camera pose estimation that preserves unit quaternion representations throughout the entire flow trajectory. We design the optimal transport of the quaternion flows using smooth spherical linear interpolation. Experiments on CO3Dv2 demonstrate our method's advantage in camera pose accuracy over diffusion-based methods and classical SfM approaches. We further show that our quaternion-constrained formulation outperforms the naive application of standard flow matching to 4D quaternion vectors on sparse-view camera pose estimation. Finally, it is observed that QuacamFM generalizes well across datasets and in-the-wild examples.

---


### 192. [Seeing Parts, Reasoning about Worlds: Visual Inference under Partial Observation](https://arxiv.org/abs/2609.32456)

**<font color=#1a73e8>作者：</font>** Wei Wang, Wenqiao Zhang, Yutong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World modeling under partial observation requires reasoning about the complete worlds that remain compatible with limited visual evidence. Occluded objects and unseen regions can leave several world states possible; additional views can exclude alternatives and strengthen the conclusions supported by the observations. We introduce WorldScope to study this process through possible-world semantics, evidence-grounded data, and learned visual representations. WorldScope-1.2M provides 1.2 million English question-answer pairs spanning eight world properties, ten task interfaces, and three observation protocols. Its answers encode confirmed facts, supported bounds, and unresolved possibilities. Complementary supervision comprises 4,800 certified counterworld groups with equivalent base observations and different hidden object configurations and query answers. These groups provide physical witnesses of ambiguity and training-only labels for world compatibility and view-induced exclusions. We propose WorldFlow, which composes cross-view entity evidence and support-surface coverage into an image-subset evidence lattice. Counterworld compatibility and transition objectives train subset representations to reflect how new observations constrain possible worlds. A shared answer generator uses these representations to predict the strongest supported conclusion. WorldScope-Bench evaluates claim judgments and evidence-dependent conclusions as views are selected, combined, removed, or ordered. On its 5,000-question test set, WorldFlow reaches 64.34% exact accuracy, improving over the same backbone trained on QA alone by 24.88 percentage points. It retains 50.43% accuracy on the 3,000 questions from structure-disjoint scenes.

---


### 193. [REMEDY: How Far Is Video Generation from Medical Education World Models?](https://arxiv.org/abs/2609.32460)

**<font color=#1a73e8>作者：</font>** Lixing Tan, Yanghao Zhou, Qing Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generation models produce realistic videos and show potential as a foundation for world models. These advances create opportunities for generating medical teaching demonstrations, which requires both convincing visual quality and precise procedural actions. However, whether current generators can meet these requirements has not been measured. To address this problem, we introduce Readiness Evaluation of Medical Education Demonstration sYnthesis (REMEDY), to our knowledge, the first benchmark for AI-generated medical teaching demonstrations. REMEDY provides 900 first frames from real demonstration videos, covering 12 tasks across four scenarios: operating room, imaging, clinic and bedside, and resuscitation. Five contemporary open-source video generation models produce 4,500 videos from these frames. We combine task-specific clinical checklists with video and motion quality metrics. Evaluation covers four dimensions: clinical action following, clinical profiles, video quality, and motion quality. Our results show that realistic appearance and temporal consistency do not ensure correct clinical actions. Even the most advanced MiniMax-H3 achieves only 28.25% on strict clinical success rate, and fine-grained clinical actions remain challenging. These findings establish a foundation and roadmap for developing future medical education world models.

---


### 194. [Adapting Nonstationary Multi-output Gaussian Processes to Bayesian Optimization](https://arxiv.org/abs/2609.32464)

**<font color=#1a73e8>作者：</font>** Zikai Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimization (MOBO) commonly relies on independent Gaussian processes (GPs) with stationary kernels, limiting its ability to represent nonstationary structure and share information between objectives. However, expressive nonstationary GPs do not necessarily make reliable BO decisions. We study this mismatch for the multi-output low-rank nonstationary (MO-LRN) GP: strong training fit can coexist with large off-design errors and optimistic acquisition predictions. We introduce MOLRN-BO, which combines a regularized shared-spectral surrogate with objective-specific residuals, prequential mean correction and tempered covariance scaling, and Pareto-local qLogEHVI optimization with periodic global search. Experiments on 12 deterministic bi-objective benchmarks show that MOLRN-BO substantially improves upon the original MO-LRN and achieves the best average problem ranks for final normalized hypervolume and normalized inverted generational distance among nine evaluated algorithms. It also achieves the strongest adverse-tail performance while remaining competitive with the leading baselines in anytime optimization. Ablation studies further show that the shared spectral construction improves off-design prediction, the local--global decision policy improves optimization performance, and hierarchical calibration reduces systematic candidate bias. These results demonstrate that nonstationary multi-output surrogates can deliver strong and robust MOBO performance when their structure and use are explicitly adapted to the demands of sequential optimization.

---


### 195. [PolyStepOR: Learning to Decide Without Optimal Decisions](https://arxiv.org/abs/2609.32465)

**<font color=#1a73e8>作者：</font>** Viet The Nguyen, Gunther Gust, An Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning (DFL) trains predictors for downstream decision quality, but often relies on optimal reference decisions that are expensive to obtain. We present PolyStepOR, which trains directly from realized decision costs without pre-computed optima and extends to in-constraint predictions through repair or infeasibility penalties. To handle piecewise-constant losses, PolyStepOR perturbs predictor parameters, evaluates the resulting decisions, and uses optimal transport to favor lower-cost directions, requiring no derivatives. Without task-specific tuning, PolyStepOR performs strongly on classical optimization benchmarks and competitively on predicted-constraint and real-world problems. Theoretically, we characterize decision-preserving perturbations and boundary detection, bound sensitivity to cost errors, and establish stationarity guarantees for a smoothed objective. PolyStepOR thus replaces optimal reference decisions and derivatives with forward evaluations.

---


### 196. [Bison: Cross-Dataset Learning for Unseen-Compound Perturbation Prediction](https://arxiv.org/abs/2609.32467)

**<font color=#1a73e8>作者：</font>** Yunfan Liu, Kasra Ghorbani, Yufei Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting transcriptional responses to unseen compounds is limited by fragmented chemical coverage and heterogeneous experimental platforms and gene panels. To assess molecular generalization across these settings, we build on Chem-PerturBridge to benchmark eight datasets with 16,771 compounds, withholding test compounds from every training dataset. This comparison reveals that high overall response agreement can coexist with weak prediction of drug-specific differences, despite reproducible signals across repeated measurements. To exploit complementary chemical supervision while targeting these differences, we introduce Bison: a shared gene representation connects native panels, while two discrete diffusion models compose context-dependent responses with molecular deviations learned through matched drug-contrast supervision. A single Bison model jointly trained across all eight datasets achieves the highest mean overall-response and drug-contrast Pearson correlations on the full benchmark in comparison with 11 methods trained independently per dataset. Compared with dataset-specific training of the same architecture, joint training increases mean drug-contrast correlation by 27.4\%, with gains across all eight datasets and improvements in overall response prediction. These results demonstrate how matched drug contrasts turn complementary screens into shared molecular supervision for unseen-drug response prediction while preserving native gene measurements.

---


### 197. [Back-Tracking from Clarity: Self-Learning to See Text from Afar](https://arxiv.org/abs/2609.32477)

**<font color=#1a73e8>作者：</font>** Duc-Tri Tran, Phi Le Nguyen, Minh Hoai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a self-supervised framework designed to enhance the capability of scene text detectors in identifying and recognizing text in scenarios where instances are shown at significant distances, typically small, blurred, and frequently missed by conventional models. Our approach leverages the high-fidelity performance of existing text spotting models on large, clear text as a foundational supervisor. By temporally back-tracking these high-confidence detections through video sequences, we automatically synthesize pseudo-labels for preceding frames where the distant text is still visually degraded or undersized. These pseudo-labels enable training a student model specialized for early text detection, without requiring any manual annotation. The success of this approach depends on accurate pseudo-label generation, for which we develop a dedicated scene text tracker capable of maintaining consistent text identities across challenging video sequences. In addition, we propose SceneText50, a diverse multilingual outdoor dataset to facilitate training and evaluation. Experiments show that our framework significantly improves early detection accuracy and robustness across varied scenes and languages. Code and data are at \href{this https URL}{this https URL}.

---


### 198. [Fast and Precise Learned Charged-Particle Trajectory Regression at the Large Hadron Collider](https://arxiv.org/abs/2609.32479)

**<font color=#1a73e8>作者：</font>** Jonathan Renusch, Benjamin Huth, Daniel Murnane 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a training recipe that treats charged-particle trajectory parameter regression on high-energy physics detector data as a sequence-modeling task. Kalman filters and linearized least-squares fits have been the classical standard approach for this task: they are optimal estimators for sparsely sampled linear-Gaussian data and are commonly used for trajectory parameter regression (fitting). The classical fitting techniques implemented for this domain reach a final precision of one part in $10^5$ through detailed modeling of detector geometry, material, detection effects and precise numerical integration of the equations of motion through the detector's inhomogeneous magnetic field. With this study, we demonstrate that using a bidirectional gated linear recurrent encoder, one is able to reproduce the full precision of classical track fitting techniques. Using a custom kernel, we also achieve significantly higher throughput during GPU inference, compared to classical fitting software running on similarly priced multi-core CPU servers representing typically employed hardware. Such a speedup would lead to considerable cost savings for the pattern recognition at the Large Hadron Collider. To our knowledge, this is the first end-to-end learned track fit to reach the full precision and, at the same time, offer the opportunity to reduce the computing costs.

---


### 199. [JEPA Learns What the Mask Leaves Unrecoverable](https://arxiv.org/abs/2609.32481)

**<font color=#1a73e8>作者：</font>** Peng Xie, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures are unusually sensitive to how the input is masked: block masks work, scattered masks do not, and the explanations are empirical. We give a measurement account. A mask is a linear measurement, and in a compactly supported wavelet basis every atom whose support lies inside the hidden region falls in the measurement's null space and leaves no trace in the data. The JEPA loss asks only that the encoded context suffice for the target, so a target that a low-level prior can recover admits a shortcut, one the moving-average target encoder can make self-consistent. What removes the shortcut is the coarse-scale content the mask leaves unrecoverable, provided enough context stays within reach of each target. We score that content before training and test the account's distinctive predictions in 151 pre-training runs. On ImageNet-100, strip masks match blocks in area and contiguity yet are recoverable, and they land at 40.3% linear top-1, beside random masks at 40.8%, against 64.3% for blocks; within one geometry family, the placements that leave the least unrecoverable content lose 6.5 points to those that leave the most, over five seed pairs; pixel targets span 7 points where latent targets span 25; and against a frozen target the gap between random and block masks, 19 points on the same kind of GPU, closes to 1.5, so the geometry acts through the target the encoder produces for itself. On UCF101 the masking ratio decides which condition, content or reach, binds; removing whole frames, unrecoverable in space but recoverable from neighbouring frames, is worst at both ratios; and on V-JEPA's own masks, batching them intact instead of truncated changes little (36.0% against 35.1%), whereas making 100 target tokens inside the blocks visible lifts them to 48.7% and hiding 100 context tokens outside the blocks does not (33.7%).

---


### 200. [Separating Diagnosis from Disease Representation: Dual-View EEG Learning with Neural-Dynamics-Guided Deformation](https://arxiv.org/abs/2609.32483)

**<font color=#1a73e8>作者：</font>** Jiaying Wang, Shouqian Shi, Yutong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based closed-loop neuromodulation calls for a subject-specific structured state, as opposed to a single disease probability, specifying which brain regions are deviant, at which frequencies, and at which lags. Sensor-space models keep the strongest diagnostic evidence without anatomy, source-space models give anatomy at a loss of predictive signal, and post-hoc attributions stay outside the prediction. We separate the two instead of forcing them into one representation, and propose DMD-EEG (Dual-view Multiscale Deformation for EEG), which keeps a fixed scalp spectral expert for diagnosis and models the source-space disease-related representation as a low-rank, sparse, iterative deformation of a healthy neural-dynamics prior in a $46$-region-of-interest (ROI) $\times$ $5$-frequency $\times$ $4$-lag (autocorrelation-timescale) space. The two experts meet only at a fixed decision level, so the source state is architecturally separate from the scalp expert. Across major depressive disorder (MDD), first-episode psychosis (FEP), and Parkinson's disease (PD), decision-level fusion matches the strongest single expert on MDD and FEP and exceeds the source branch on PD. On FEP the source expert is the strongest branch, the task where the deformation contributes most. The source state is an explicit ROI-frequency-lag attribution defined in a shared source coordinate system across montages, which we treat as an anatomically-coordinated predictive representation whose coordinates are directly readable and hypothesis-generating. The highest-saliency coordinates align with established disease circuitry (fronto-limbic-temporal regions in MDD, motor-cortex beta in PD), and the MDD state transfers by rank to an unseen cohort recorded with a different montage.

---


> [!TIP]
> 当前位于：**151-200**（第 4/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
