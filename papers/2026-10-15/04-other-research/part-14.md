# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**651-700**（第 14/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-700** | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 651. [BRIDGE: Selective Boundary Repair with Dependency Graph Evidence in Multi-Agent Systems](https://arxiv.org/abs/2610.17805)

**<font color=#1a73e8>作者：</font>** Encheng Su, Pengze Li, Ziheng Hua 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent collaboration has emerged as a critical paradigm for tackling complex, long-horizon tasks; however, while coordination protocols continue to advance, systemic failures at the inter-agent collaboration interface remain a pervasive bottleneck. In collaborative workflows, systems frequently suffer from \emph{broken handoffs}---where critical task context is omitted, misrouted, or ignored despite each agent emitting locally plausible responses. To address this challenge, we present \method, a verifiable runtime control framework that treats handoff repair as selective intervention over explicit dependency graphs. Central to \method is an integrated fault-attribution and calibration pipeline, \dataset, which decouples execution dependencies and injects counterfactual handoff perturbations to provide empirical supervision for runtime intervention. Leveraging this diagnostic foundation, \method dynamically compiles observable interaction traces into a provenance graph to pinpoint unresolved dependencies, without accessing private agent states. It then evaluates candidate repairs through an empirical gate that weighs expected gains against disruption risks, and executes repairs only when formal local postconditions hold. Extensive evaluations across demanding benchmarks demonstrate that \method boosts task success by up to 12.3 absolute percentage points on SILO-BENCH and 11.1 on TeamBench. Across both backbones, \method maintains strict cost-effectiveness, adding as little as 2.0\% marginal token overhead. Furthermore, on 562 handoff-relevant traces from the MAST benchmark, \method achieves 69.8\% F1 in a single pass, establishing a reliable operational boundary for verifiable coordination repair.

---


### 652. [SPARCL: Spatially Adaptive Regional Coverage for Active Learning in Chest X-ray Analysis](https://arxiv.org/abs/2610.17808)

**<font color=#1a73e8>作者：</font>** Juho Jung, Seongjae Kang, Mijoo Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-level annotation for chest X-ray (CXR) lesion segmentation is expensive, making active learning (AL) essential. However, existing AL strategies fail to account for the spatial distribution of selected samples, resulting in inconsistent performance across focal (e.g., aortic calcification) and diffuse (e.g., nodules) pathologies. In this paper, we propose SPARCL (Spatially Adaptive Regional Coverage for Active Learning) to dynamically balance predictive uncertainty with cumulative spatial coverage. By employing a concave coverage function, SPARCL imposes diminishing returns on previously annotated regions, naturally directing the annotation budget toward under-labeled areas. Furthermore, an entropy gate reverts the algorithm to standard uncertainty sampling when spatial variation is absent. This coverage objective is monotone submodular, guaranteeing near-optimal greedy batch selection. To address how aggregate metrics like Dice obscure regional failures, we further introduce two metrics---Spatial Inconsistency (SI) and Performance Coverage (PC)---to quantify anatomical fairness across AL rounds. Evaluated on an in-house calcification cohort and public CXR benchmarks, SPARCL reaches 95% of fully supervised performance using only 24% of the data, compared to 29% for the best baseline. Ultimately, SPARCL ensures robust spatial reliability, surfacing regional gains that aggregate metrics miss.

---


### 653. [Follow the Perturbed Leader for Linear Bandits: $\sqrt{T}$ Regret over General Convex Sets](https://arxiv.org/abs/2610.17818)

**<font color=#1a73e8>作者：</font>** Chen-Yu Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give the first adversarial linear bandit algorithm based on Follow-the-Perturbed-Leader (FTPL) that achieves $\sqrt{T}$ regret over general convex action sets. Our algorithm attains $\widetilde{\mathcal{O}}(d^{5/4}\sqrt{T})$ regret using only linear optimization oracles, and the near-optimal $\widetilde{\mathcal{O}}(d\sqrt{T})$ regret when an optimal-design exploration distribution is further available. This improves on the $T^{2/3}$ regret of the FTPL algorithm of Dani and Hayes (2006) for general convex sets, and generalizes the $\sqrt{T}$ regret of Lévy et al. (2026) over two special action sets (hypercube and Euclidean ball). Compared to previous oracle-efficient linear bandit algorithms based on continuous exponential weights, the FTPL approach generally has better computational efficiency, and is much simpler to implement.
The key algorithmic element is a perturbation distribution that adapts to the estimated rewards. Its simplest form, an adaptive Gaussian perturbation, is straightforward to implement and already attains the regret bound above. We further extend it to two general constructions, random-weighting and elliptical perturbations, each covering distributions from light tails (Gaussian) to heavy tails (Student-$t_2$). On the technical side, we develop a systematic way to analyze the stability term in the FTPL regret through the Fisher information of the perturbation distribution. This builds a general framework for FTPL beyond existing ones such as the hazard rate and the FTRL-FTPL duality.

---


### 654. [Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents](https://arxiv.org/abs/2610.17827)

**<font color=#1a73e8>作者：</font>** Haochen Zhao, Minsheng Hao, Zheng Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing approaches to training and evaluating search agents focus heavily on final-answer quality, largely neglecting how generated answers map back to retrieved evidence. Recent methods track citations to enforce grounding, but citation support alone does not establish source independence or whether an answer appropriately handles conflicting evidence. We argue that credibility in open-web retrieval depends on principled cross-source evidence grounding that accounts for source independence and systematically attributes and adjudicates conflicting evidence, while hierarchical judgments of these grounding decisions provide a unified signal for training and evaluation. To this end, we propose an evaluation framework, Cross-Source Evidence Grounding (CSEG), that employs a fine-grained, six-layer decision tree over the complete search trajectory. We introduce CSEG-Bench and trainable reward models to provide targeted supervision following this framework. Our approach helps eliminating the severe data skew of natural trajectories by providing targeted coverage over complex, deep-layer decision paths, such as cross-source conflict resolution and nuanced attribution, that standard rollouts fail to capture. Specifically, (1) we define the hierarchy at label, node, and path levels; (2) we construct 1,160 verified trajectories over nine canonical paths by rewriting answers on real retrieved document pools, with independent frontier judges reproducing the entire gold path and human experts deciding inclusion; (3) we train CSEG-RM, which reaches 83.9% exact accuracy on our benchmark while lying on the performance-token efficiency Pareto frontier. Experiments that use this reward alone to supervise a frozen-retrieval answer policy raise the independently judged mean label from 2.83 to 4.19, and show that learning the hierarchy generalizes across layers at a fraction of frontier-judge cost.

---


### 655. [QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](https://arxiv.org/abs/2610.17829)

**<font color=#1a73e8>作者：</font>** Tiancheng Shen, Zilong Huang, Xiangtai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Diffusion Transformers (MM-DiTs) have recently emerged as a powerful framework for unified text-vision synthesis, surpassing traditional U-Net architectures in generative tasks. One key innovation lies in its Multimodal Self-Attention (MM-SA) interaction, where image and text tokens are concatenated and processed via self-attention. However, this mechanism poses significant challenges for editing, rendering conventional U-Net-based attention manipulation methods ineffective. To address this limitation, we propose QK-Edit, a training-free framework that exploits the unique attention dynamics of MM-DiTs for precise text-guided image and video editing. By introducing a novel query-key manipulation strategy, our method isolates and adjusts critical attention components to achieve an optimal balance between prompt fidelity and structural consistency. This enables seamless edits across various tasks, including object addition, object removal, object replacement, changing background, changing material, changing color, and style transformation. Notably, it can be easily implemented with feature replacement in inference. QK-Edit demonstrates superior editing performance on state-of-the-art models, such as FLUX and HunyuanVideo, effectively bridging the gap between generative power and editable flexibility in MM-DiTs, and paving the way for scalable multimodal content creation.

---


### 656. [GeoNIRS: Geometry-Aware Pretraining for Heterogeneous fNIRS Representation Learning](https://arxiv.org/abs/2610.17845)

**<font color=#1a73e8>作者：</font>** Zongsheng Li, Shengyuan Zhu, Zimo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional near-infrared spectroscopy (fNIRS) provides portable and spatially localized measurements of cortical hemodynamics, but differences in channel count, probe layout, signal distribution, and task type hinder joint pretraining across datasets. We introduce GeoNIRS, a geometry-aware framework that uses source-detector locations as a shared spatial reference across heterogeneous probe layouts. GeoNIRS compresses variable-size channel sets into a fixed-size latent representation and employs bidirectional HbO/HbR cross-reconstruction with contiguous temporal masking. GeoNIRS-base is pretrained on eight heterogeneous datasets, while GeoNIRS-large scales to 22 datasets. Neither downstream data nor labels are used during pretraining, enabling evaluation under a strict cross-task setting. To our knowledge, GeoNIRS is the first fNIRS framework to explicitly model physical channel geometry during joint pretraining across heterogeneous channel configurations, and the first to provide complete source code and downloadable pretrained checkpoints. We evaluate GeoNIRS on eight held-out tasks spanning clinical and auditory assessment, pain and affective processing, semantic decoding, and motor function. GeoNIRS achieves the highest task-averaged balanced accuracy among the evaluated conventional machine-learning, fNIRS-specific, general time-series, and fNIRS pretraining baselines. Compared with random initialization, pretraining improves average balanced accuracy by 4.12 percentage points under linear probing and 3.30 points under full fine-tuning, with larger benefits when labels are scarce. GeoNIRS also remains robust to missing input channels. Geometry perturbations and pretraining ablations further show that both channel geometry and cross-chromophore reconstruction contribute to the learned representations.

---


### 657. [Persistence Positional Encoding: A Minimal Transformer Recipe for Persistence Diagrams](https://arxiv.org/abs/2610.17848)

**<font color=#1a73e8>作者：</font>** Eunwoo Heo, Ganghyun Kim, Jaejun Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistence diagrams (PDs) represent multiscale topological information as multisets of birth-death pairs $(b,d)$. How best to use them with Transformers, however, remains unclear. Connecting PDs to Transformers requires choosing how topological information is tokenized and exposed to self-attention. Prior methods use specialized designs for tokenization, aggregation, Transformer blocks, or attention, but are hard to compare since reported results rarely share PD inputs, splits, or model-selection rules. We instead confine the diagram-specific design to point representation, mapping each birth-death pair through fixed random Fourier features while leaving the Transformer backbone unchanged, and call this recipe Persistence Positional Encoding (PPE). In matched controls on eight TU graph benchmarks (TU8), changing only point representation shifts macro accuracy by 5.49 to 6.47 percentage points (pp), against 0.47 to 1.45 pp from changing the downstream module, identifying point representation as the dominant design variable tested. We further reevaluate vectorizations, kernels, learned representations, and Transformer-based models under one protocol with shared PD inputs, outer folds, and validation-only selection. Among all evaluated PD methods and downstream configurations, PPE achieves the highest mean on most benchmarks, including TU8, ORBIT5K, and MCB-C. Finally, we prove that grid averaging leaves a reconstruction error at any resolution, whereas a Transformer with fixed random Fourier frequencies is almost surely universal. PPE thus offers a minimal, Transformer-native baseline for persistence diagrams, and a common protocol for future comparison.

---


### 658. [Frequency Routing and Identity Conditioning for Thermal-to-Visible Face Translation](https://arxiv.org/abs/2610.17859)

**<font color=#1a73e8>作者：</font>** Haojie Li, Xinlong Sun, Xiaohaoyang Lei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal-to-visible (T2V) face translation has important applications in nighttime biometric recognition, low-light surveillance, and human interpretation of thermal observations. The task remains challenging because thermal images do not directly record visible appearance, while the cross-spectral cues useful for reconstruction vary across frequency components and semantic roles. Existing spatially conditioned models tend to process these cues through a homogeneous adaptation path and do not explicitly separate local structure from global identity. We propose FreqID-Control, a parameter-efficient framework that organizes thermal guidance according to spectral reliability and semantic role while preserving the pretrained generative prior. It combines frequency-routed low-rank adaptation, which allocates separate transformation subspaces to low-frequency structure and high-frequency detail, with shared cross-spectral identity conditioning, which supplies compact global identity tokens independently of spatial thermal tokens. A controlled analysis on MCXFace and SpeakingFaces provides the empirical basis for this design, revealing stable low-frequency correspondence and edge-localized detail correspondence. Experiments on both datasets demonstrate strong image fidelity and biometric identity preservation, while controlled ablations on MCXFace confirm the complementary contributions of frequency routing and shared identity conditioning.

---


### 659. [TStruct: Learning Shared Temporal Structures for Long-Term Time-Series Forecasting](https://arxiv.org/abs/2610.17864)

**<font color=#1a73e8>作者：</font>** Yangze Li, Zhengyang Zhou, Qihe Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting requires temporal dependency modeling that remains stable and generalizable under temporal distribution shifts. However, real-world time series are often noisy and non-stationary, making deep learning models prone to fitting incidental temporal interactions in the training data. A key question is whether there exist temporal relationship structures that recur across different temporal positions and variables. We analyze temporal relationship matrices on commonly used time series datasets and find that samples from different temporal positions and different variables exhibit shared dominant temporal relationship structures. This indicates that temporal relationship structures contain patterns that recur stably across samples and variables. To learn such shared structures, we propose \textbf{T}emporal \textbf{Struct}ure Network (\textbf{TStruct}), a simple yet effective network for directly learning shared and generalizable temporal dependencies. Specifically, TStruct directly parameterizes a set of shared temporal dependency matrices and generates normalized combination weights using dynamic sample information and static variable priors. These weights represent a soft allocation of each sample-variable pair over shared temporal dependency structures, enabling the model to generate adaptive temporal dependency matrices under shared structural constraints, rather than fitting incidental interactions in a fully unconstrained manner. Notably, this simple structure-aware design consistently outperforms several strong baselines across all datasets, achieving superior accuracy while maintaining high computational efficiency.

---


### 660. [Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration](https://arxiv.org/abs/2610.17874)

**<font color=#1a73e8>作者：</font>** Sanchit Kabra, Nurendra Choudhary, Jiangshu Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering what drives an outcome from data is central to science and often requires deciding what is worth investigating before a specific hypothesis is known. Yet most existing hypothesis generation settings substantially narrow this search by providing a research question, target relationship, or curated context. We introduce open-ended multiple hypothesis discovery, where a system receives only a large tabular dataset and an outcome and must discover multiple data-supported hypotheses without knowing in advance the relevant variables, functional forms, conditions, or number of underlying mechanisms. To study this problem, we introduce a benchmark built from structural causal models grounded in real-world data schemas, containing 351 planted hypotheses across 15 tasks and five domains, with 53--65 variables and 1M--10M rows per task. The causal model is hidden from the discovery method and retained only by the evaluator, allowing proposed hypotheses to be tested through interventions and separating observational discovery from causal validation. We further propose HypAgent, which treats the dataset as an interactive environment and performs iterative search by proposing candidate directions, triaging and refining promising hypotheses, and removing explained signal so that each accepted discovery redirects subsequent search. HypAgent achieves 0.47 precision, 0.51 recall, and 0.49 F1, compared with 0.35 F1 for the strongest baseline. Our analysis shows that many failures occur after a relevant variable has already been surfaced, suggesting that correctly characterizing a mechanism's functional form and conditions, rather than merely identifying relevant variables, remains a key challenge in open-ended discovery.

---


### 661. [LoopREG: Representation Supervision Enables Test-Time Recurrent Depth in Diffusion Transformers](https://arxiv.org/abs/2610.17877)

**<font color=#1a73e8>作者：</font>** Zipeng Wang, Anping Xiong, Jing Zhang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reusing Transformer blocks offers a way to increase diffusion-model computation at test time, but naive recurrence can degrade generation beyond its training depth. We introduce LoopREG, a representation-supervised recurrent diffusion Transformer that repeatedly applies a shared block at the state supervised by a pretrained visual encoder. Alignment is applied after the final recurrent visit during training; inference extends the same learned operator to additional visits. On ImageNet 256 x 256, LoopREG reduces SiT-B/2 FID from the local REG baseline's 15.08 to 4.91 at 400K training steps, a 67.41% reduction. Within a checkpoint trained with two visits, one extra inference visit improves FID from 14.71 to 5.34 with unchanged weights. The benefit persists on SiT-L/2 and SiT-XL/2. Controlled interventions show that useful recurrence follows the location of representation supervision, while REPA alignment produces a smaller extrapolation benefit. These results make representation-supervised recurrence a practical route to improving diffusion generation through additional inference depth.

---


### 662. [Deep Mesoscopic Dynamics](https://arxiv.org/abs/2610.17885)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Shiqi Wu, Yihang Ouyang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Microscopic simulations resolve spatial patterns but are feasible only over small domains and short timescales, whereas bulk descriptions erase those patterns through spatial averaging. Mesoscopic fields preserve this spatial organisation, but their effective equations are known only for selected microscopic systems and scaling limits. We introduce Deep Mesoscopic Dynamics (DeepMesoD), which uses neural networks to learn an effective mesoscopic field equation from microscopic trajectories at a prescribed coarse-graining scale. For the nonconserved dissipative dynamics studied here, DeepMesoD learns the free-energy functional with a spatial interaction kernel and a state-dependent dissipation operator constrained by the fluctuation-dissipation relation. We first validate the construction in the Ising-Kac model, where the learned mesoscopic equation recovers the known hydrodynamic limit and rollouts remain stable far beyond the training horizon. We then treat two systems without closed-form mesoscopic descriptions. For a two-dimensional Heisenberg ferromagnet governed by atomistic spin dynamics, DeepMesoD learns a mesoscopic model whose predictions match atomistic references up to 1 ns, and a rollout with an unseen initial condition remains bounded up to 25 ns. For layered CrBr$_3$, the learned kernel captures the suppression and sign reversal of interlayer coupling at a stacking fault whose location and strength are not supplied as inputs. Controlled changes to the learned interaction show how fault number and placement shape multistep magnetic responses, complementing our magneto-photoluminescence measurements. Across the two atomistic systems, DeepMesoD achieves a three-to-four-order-of-magnitude reduction in wall-clock time compared with atomistic spin dynamics.

---


### 663. [Stable-Plastic Subspace Construction for Differentially Private Continual LoRA](https://arxiv.org/abs/2610.17904)

**<font color=#1a73e8>作者：</font>** Jin Liu, Ning Xi, Yinbin Miao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) adapts pretrained models to a sequence of tasks while retaining knowledge acquired from earlier tasks. When task data are sensitive, differential privacy (DP) provides record-level protection, but maintaining both adaptation and retention under privacy constraints remains challenging. We study this problem in continual low-rank adaptation (LoRA) and observe that: 1) private training increases forgetting primarily during subsequent adaptation rather than initial task acquisition; 2) jointly perturbing both LoRA factors introduces a non-negligible bilinear noise interaction; and 3) DP aggravates the stability-plasticity dilemma, hindering both knowledge retention and adaptation to new tasks. Based on these observations, we propose DP-SPA, which constructs a stable subspace from previously privatized updates and a plastic subspace from pretrained weights within its orthogonal complement. The method fixes these bases and privately optimizes only the LoRA factor, eliminating the bilinear noise interaction within each step. Before merging each task update, it rescales stable-direction coefficients using historical and current update energies. We establish a privacy guarantee and show that recalibration does not increase historical overlap and tightens a conditional upper bound on old-task loss increase. Experiments across five datasets, eight settings, and multiple privacy budgets show that DP-SPA improves average accuracy and reduces forgetting compared with the evaluated baselines.

---


### 664. [NBCLT: Parameter-Agnostic Norm-Ball Clipped Local Training](https://arxiv.org/abs/2610.17913)

**<font color=#1a73e8>作者：</font>** Linxuan Pan, Shucheng Yang, Junchi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed learning with multiple local steps reduces communication but aggravates drift, and its practical performance often depends on carefully tuned hyperparameters under heterogeneous data and communication constraints. At the same time, recent Muon-type optimizers suggest that constraining updates within suitable norm balls provides a simple way to encode geometric priors into optimization. In this work, we propose NBCLT (Norm-Ball Clipped Local Training), a unified local-training framework for both federated learning (FL) and decentralized learning (DL). NBCLT combines a predict-and-correct local update rule with Euclidean projections onto flexible norm balls, thereby performing norm-ball clipping under flexible update geometries while retaining a simple implementation. In FL, its problem-parameter-free regime achieves $\mathcal{O}(\epsilon^{-2})$ communication complexity and $\mathcal{O}(\epsilon^{-4})$ total stochastic-gradient complexity without assuming bounded heterogeneity, when the per-round local-computation budget is scaled appropriately with the horizon. In DL, NBCLT is compatible with both static and time-varying mixing and preserves these accuracy exponents under the analogous computation scaling, up to fixed network constants and an additive initialization cost.

---


### 665. [Stein Variational Distributional Reinforcement Learning: Score-Guided Particles for Multivariate Return Distributions](https://arxiv.org/abs/2610.17925)

**<font color=#1a73e8>作者：</font>** Manuel Haußmann, Melih Kandemir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decisions that weigh several reward signals against each other require the joint distribution of the return vector. Categorical critics scale exponentially in the reward dimension, and quantiles have no canonical multivariate analogue. Multivariate distributional critics therefore represent each return distribution by M equal-weight particles trained with a discrepancy loss. Beyond their atoms, the particles provide no sampler and cannot resolve events rarer than 1/M. We propose Stein variational distributional RL (SVDRL). Its critic outputs Stein particles, which Stein variational gradient descent transports along a learned score field of the distributional Bellman target. We learn this field by bootstrapped denoising score matching across noise levels and tie it across the Bellman recursion by a consistency loss, which we prove is a non-expansive temporal-difference scheme in score space. The same field certifies the particles. Its reverse-diffusion sampler satisfies a supremal Wasserstein policy-evaluation bound that holds for bounded, possibly multimodal returns. The Stein particles inherit this bound up to a gap that we measure without ground truth, and the sampler answers tail-risk queries below the particle resolution at any sample size. Empirically, SVDRL is more accurate on rare events than particle critics with the same number of particles, and on par on MuJoCo continuous control.

---


### 666. [PUGS: Physics-Guided Uncertainty Modeling for Underwater Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2610.17936)

**<font color=#1a73e8>作者：</font>** Tingjun Li, Yuxi Wang, Guoqiang Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D Gaussian Splatting (3DGS) provides an efficient framework for dynamic scene reconstruction. Most existing approaches model scene dynamics with deterministic deformation fields, assuming each Gaussian follows a distinct geometric trajectory over time. This assumption breaks down underwater, where light scattering, refraction, marine snow and low visibility create substantial physical ambiguity in captured images. We present PUGS, a physics-guided uncertainty model for underwater dynamic 3DGS. PUGS learns inherent uncertainty induced by underwater image formation and leverages it as a physical signal for dynamic scene modeling. Rather than estimating a single deterministic displacement, it parameterizes each Gaussian's motion as a probability distribution with expected deformation and physical uncertainty. We adopt stochastic deformation optimization to sample Gaussian trajectories via local reparameterization, exploring multiple physically plausible solutions during training. We further propose uncertainty stochastic annealing and a dual-path self-consistency distillation objective, converting stochastic exploration to deterministic reconstruction while preserving temporal coherence. Extensive experiments on underwater dynamic datasets and physics-aware benchmarks demonstrate superior rendering quality, temporal consistency and reconstruction robustness. Our method achieves 1.16 dB PSNR gain over the strongest baseline on UVEB and 3.99 dB on DRUVA.

---


### 667. [Sea-Net: A Small and Inherently Interpretable Neural Network for Time Series Classification](https://arxiv.org/abs/2610.17939)

**<font color=#1a73e8>作者：</font>** Ubaid Ur Rehman, Tanmoy Mondal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional time-series classification methods often operate as black boxes, providing a class prediction without indicating which time point or time interval within the series led to that prediction. To improve temporal interpretability, MILLET (Multiple Instance Learning with Temporal Explanation), which combines an InceptionTime encoder with Conjunctive Pooling, provides both classification and temporal explanations. However, MILLET contains approximately 424 K parameters, making it unsuitable for deployment on resource-constrained micro-controllers, and it achieves an overall time-series accuracy of 0.888 and an explanation score of 0.681 NDCG@n. We therefore propose SEA-Net, a lightweight architecture using small multi-scale depthwise-separable convolutional TSC encoders and improved Multiple Instance Learning (MIL) pooling heads. Our SEA-Net bottleneck encoder with Top-k pooling achieves 0.931 accuracy and 0.765 NDCG@n with only 41 K parameters. Another variant, using a gated encoder with Top-k pooling, achieves 0.955 accuracy and 0.750 NDCG@n with 62 K parameters. These results demonstrate that lightweight architectures can maintain strong classification performance and temporal explanations while substantially reducing model size. The proposed variants address specific limitations of the pooling strategy used by MILLET, providing a practical direction for interpretable time-series classification on resource-constrained edge devices.

---


### 668. [AI-Enhanced Hyperspectral Imaging for Intraoperative Detection of Low-Grade Glioma: A Clinical Study](https://arxiv.org/abs/2610.17944)

**<font color=#1a73e8>作者：</font>** Siri Willems, Ishika Jain, Jens De Winne 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current image-guided neuronavigation techniques, such as intraoperative MRI and ultrasound, are limited by high costs, limited sensitivity and operational complexity. There is a clear need for more efficient systems to enhance intra-operative tumor detection and improve patient outcomes for intrinsic brain tumor resection. Whereas previous intraoperative brain HSI studies have predominantly investigated high-grade gliomas, glioblastomas, or mixed-grade cohorts, this clinical study focuses specifically on low-grade gliomas (LGGs). LGGs strongly resemble normal brain under white light conditions on the operative microscope. This study characterizes spectral differences between healthy and tumor tissue and provides a paired comparison of HSI- and RGB-based classification at matched tissue locations and under identical patient-level data splits. Tumor regions showed consistently lower reflectance, which may be associated with differences in hemoglobin concentration and oxygenation. A range of classification models was evaluated. The 3D CNN, which integrates spectral and spatial features, achieved the highest median ROC-AUC of 74.5%, compared with 67.9% for the spectral-only XGBoost model and 64.0% for the RGB-based model. These results support further investigation of HSI for low-grade glioma classification and quantify its performance relative to conventional RGB imaging in this cohort.

---


### 669. [FETALFusion: Resolution-Aware State-Space Modeling for Multi-Domain Fetal Head Segmentation](https://arxiv.org/abs/2610.17951)

**<font color=#1a73e8>作者：</font>** Ammar Bhilwarawala, Mainak Bandyopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head circumference (HC) measured from 2D ultrasound is a routine marker of fetal growth, and automating it needs segmentations whose boundaries hold up on individual scans, not only on average. We present FETALFusion, a dual-path CNN-Mamba encoder-decoder for fetal head segmentation across acquisition types. It applies four-directional state-space scans only at the two highest-resolution stages, routes bottleneck features through domain-specific channel gates that are averaged at test time, and adds a weak landmark shape prior. We train jointly on transabdominal (HC-18) and transperineal (PSFHS) images and compare ten methods on a held-out test set of 471 images, each trained under one schedule and scored by surface distances at native resolution. FETALFusion reaches a Dice score of 0.963 and an HD95 of 2.10 mm without test-time augmentation or a domain label. It improves on U-Mamba on all five reported metrics (HD95 reduced by 0.31 mm; Holm-corrected ($p < 10^{-4}$), a lead that holds under test-time augmentation and across two independent training runs, and in the mean on U-Net, Attention U-Net and TransUNet. Residual encoders close the gap: a ResNet-34 UNet++ exceeds FETALFusion, and an ImageNet initialised ResNet-34 U-Net is best overall (HD95 1.75 mm). The ablation agrees. Calibrated against run-to-run variation, it attributes FETALFusion's measurable gains to the landmark shape prior and, on transperineal images, to the domain gates, while removing the state-space branch does not measurably change accuracy. HC from the predicted masks agrees with the clinical reference at an intraclass correlation of 0.9986.

---


### 670. [Standing, Not Truth: Who May Say What About Whom in Agentic Selection](https://arxiv.org/abs/2610.17952)

**<font color=#1a73e8>作者：</font>** Yedidel Louck, Amit Dvir, Ariel Stulman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software agents increasingly choose on a user's behalf among competing offerings described by the parties who benefit. A lawful participant, publishing under its own identity, compromising no channel and issuing no instruction, can move that choice with a single false factual claim about a competing offering.
Across twelve published defenses spanning the three placements a check can occupy, none separates it from marketing. Each accepts it for a reason correct on its own: its origin is a lawful channel, its influence is evidence meant to decide, its action serves the user's goal. None establishes that the publisher was entitled to speak about a competitor, each exclusion stated by the defenses' own authors. Disclosure does not replace enforcement: re-rendering every description as attributed speech leaves the attack at 72/72, the agent repeating the attribution and reasoning from it.
The missing relation is standing: whether a claimant's bound identity entitles it to assert about a claim's subject. A publisher may say what its own package does. It has no standing to say a competitor's package is frozen, and the difference is decidable without settling whether either is true. Deciding it needs the one fact prose extraction does not recover, who spoke, which a catalogue binds to every entry and then drops.
The check is quiet on honest traffic, flagging 0.9% of natural pairs in two corpora. Used as a gate it stops 130 of 131 landed attacks and disturbs none of 348 honest selections. Applied everywhere it changes 0.9% and 2.6%, where deleting the whole description changes 12.7% and 21.0%. On thirteen further agents the attack succeeds on 50.7% of decisions and sentence removal leaves 10.3% standing. Two published attacks stay outside: self-directed claims, which standing admits, and injected criteria, with no subject in the set.

---


### 671. [Better Capturing Interactions Between Products in~Retail: Revisited Negative Sampling for~Basket Choice Modeling](https://arxiv.org/abs/2610.17963)

**<font color=#1a73e8>作者：</font>** Jules Désir, Vincent Auriau, Martin Možina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brick-and-mortar retailers face many different challenges that involve understanding thoroughly its products catalog and customer preferences. In particular, assortment optimization - proposing the ideal mix of products - and promotion planning hold a pivotal role in their strategy. By leveraging sales data, retailers can make informed decisions on which products to sell and how to manage inventory, based on customer preferences as well as regional and seasonal trends. It is especially crucial to capture interactions between products, in order to minimize the number of items that cannibalize each other's sales and to ensure that complementary products, which are often purchased together, are conjointly available and sold across all stores. In this paper, we propose a model of shopping basket that learns embeddings to represent interactions between products, prices and stores. Our model is built to uncover sales patterns from very large transaction datasets. In particular, the optimization loss is computed with random negative samples in order to overcome the computational bottlenecks that arise with large number of items. Our experiments on synthetic data show the efficiency of drawing such negative samples based on the actual assortment of available products, with better results than approaches from the literature. We also validate our approach by training and evaluating our model on a dataset composed of millions of transactions from Fortenova Group, one of the leading retail company in Southeast Europe. Our model showcases promising applications in the sector of retail, with enriched interfaces to efficiently support category managers.

---


### 672. [Web Scale on a Budget: Tail-Aware Retrieval Evaluation](https://arxiv.org/abs/2610.17986)

**<font color=#1a73e8>作者：</font>** Boaz Meivar, Shai Avidan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A common practice in instance retrieval is to grow the gallery size to improve a benchmark's discrimination capability. One prominent example is ILIAS, which adds up to 100 million distractor images. The prevailing assumption is that faithful evaluation demands web scale, and that indexing all 100M images through the backbone is the unavoidable price of a comparable number. That price is steep: hundreds of GPU-hours and ~200 GB of descriptors per model, paid again for every method or ablation. We show the web-scale indexing price is largely avoidable: evaluation itself obeys a scaling law. The number of distractors that outrank a positive is Binomial in the gallery size. We define the per-query retrieval hardness, a gallery-scale agnostic quantity that yields a retrieval metric at any scale, and demonstrate it can be derived from a small random sample. The underlying sampled-rank machinery is long established in recommender-system and biometric evaluation, but to our knowledge has never been adapted to visual retrieval. We make the law per-query and estimable, and validate it at true 100M scale on ILIAS and INSTRE, and on the full 759k-distractor Google Landmarks v2 pool. Concretely, within a 5% sample (a flat 20x less indexing), every backbone's tail-aware (EVT) estimate has converged onto the large-scale mAP, to within ~0.01 (mean absolute error 0.005), across five backbones, three benchmarks, and two distractor pools (mAP@1000 at 100M on ILIAS/INSTRE; the official mAP@100 at the full 759k pool on GLDv2); the recommender-systems count baseline over-predicts everywhere (+0.037 to +0.068). This is an order of magnitude better than naively reporting the metric on the same subset (+0.08 to +0.13). We release code and the per-query hardness to facilitate faster, cheaper, and greener retrieval evaluation.

---


### 673. [PolUR: Polarization Aware Multimodal Degradation Perception for Underwater Image Restoration](https://arxiv.org/abs/2610.17991)

**<font color=#1a73e8>作者：</font>** Wenshuo Zhang, Xiangyue Zhang, Junlin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering high-quality images from degraded underwater observations is crucial for underwater exploration. Polarization observations show promise as an effective source of complementary physical cues for recovering target radiance under clear-water conditions. However, existing methods have yet to jointly model raw intensity information and polarization cues to enable image restoration driven by an understanding of mixed degradations (color casts, haze, and low light). To overcome these limitations, we propose PolUR, a unified multimodal language-driven framework that jointly uses polarization and RGB information to identify degradation types and severity levels through structured semantic instructions and enhances joint restoration representations under the guidance of degradation-aware semantic features to improve restoration robustness under mixed degradations. We further construct a new benchmark named MixPolar, which contains underwater images exhibiting real-world degradations and their corresponding degradation descriptions. MixPolar supports systematic evaluation of degradation perception, image restoration, and performance on downstream tasks. Extensive experiments demonstrate that PolUR effectively integrates polarization and RGB information, achieving competitive performance in degradation perception and image restoration, while also demonstrating generalization capability and utility for downstream tasks.

---


### 674. [Counterfactual Certification for Sequential Unlearning with Long-Run Performance Guarantees](https://arxiv.org/abs/2610.17993)

**<font color=#1a73e8>作者：</font>** Hanna Benarroch, Jamal Atif, Olivier Cappé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified machine unlearning ensures the proximity between the unlearned model and a model retrained without the data to be forgotten. Extending this framework to sequential deletion requests, typically arriving as groups of variable size (e.g., all records of one user or of coordinated users), is challenging. For unlearning methods based on fine-tuning on the retain sets, this leads to either degrading performance or increasing computation as the number of unlearning requests grows. For independent successive requests, we instead certify each model release against a counterfactual unlearning trajectory in which the group being deleted never took part. With a fixed fine-tuning budget per deletion, we show that, for smooth strongly convex objectives, this approach keeps the performance loss bounded, uniformly in the number of requests. Experiments with multiclass logistic regression on FEMNIST show that the resulting algorithm needs fewer corrective steps than existing sequential methods and outperforms training-time differential privacy, particularly when group sizes are heterogeneous.

---


### 675. [Improving Neural Symbolic Regression with a Diverse Prior and Post-training Alignment](https://arxiv.org/abs/2610.17994)

**<font color=#1a73e8>作者：</font>** David Otte, Jörg K.H. Franke, Frank Hutter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression is the problem of finding an expression that fits a dataset. Solving it requires searching a combinatorial space of candidate expressions. Neural symbolic regression can amortize that search by training a model once on synthetic data and then predicting expressions for a new dataset. But existing models still underperform genetic programming on real, noisy data. We argue that the deficit lies in the training rather than in the paradigm, and present RASR (Reinforced Amortized Symbolic Regression), a method with two key changes to the training recipe. First, we design a synthetic prior that narrows the gap with real-world data: inputs come from the prior of a tabular foundation model; constants are sampled bottom-up, conditioned on the data; targets carry heteroscedastic and structured noise; and everything is standardized. Second, we split training into two stages. Supervised pre-training maximizes the token-level likelihood of a reference expression. This is followed by reinforcement-learning post-training that aligns the model with its inference-time use by rewarding held-out fit and penalizing expression size. On the black-box track of SRBench 2.0, RASR achieves the best mean test $R^2$ rank of all evaluated methods. Three RASR variants, trained with different size penalties, make up most of the accuracy-complexity Pareto front. On Strogatz, our method recovers more ground-truth expressions than any baseline, and on Feynman it is competitive with the best-performing methods.

---


### 676. [Uncertainty-Aware Semi-Supervised Framework with Supervised Contrastive Learning for Sugarcane Leaf Disease Detection](https://arxiv.org/abs/2610.17996)

**<font color=#1a73e8>作者：</font>** Shalini Dangi, Divya Teja, Omkar Kabde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sugarcane leaf diseases severely impact crop yield and quality, making accurate and timely detection critical for sustainable agriculture. Conventional deep learning models for plant disease detection depend on large annotated datasets, which are expensive to obtain and challenging to prepare due to challenges commonly observed across crop disease detection tasks, including (i) high intra-class variation caused by diverse symptom expressions across growth stages, (ii) subtle inter-class similarities between diseased and healthy tissues, and (iii) the risk of noisy labels degrading model reliability. To handle these challenges, we presented an Uncertainty-aware Mean-Teacher based Semi-Supervised Learning Disease Detection Network (U-SSDNet) that leverages unlabeled data while maintaining robustness. First, discrete wavelet transform preprocessing is applied to enhance lesion visibility and reduce intra- class variation. Subsequently, the KL divergence is employed to refine the pseudo-labels and reduce the impact of confirmation bias. At the same time, supervised contrastive learning is applied to make the features more distin- guishable and improve the separation among different classes. Experimental evaluations on sugarcane leaf disease datasets, considered a representative case study, demonstrate that the proposed approach achieves performance close to that of fully supervised models while requiring far fewer annotated samples and consistently outperforms state-of-the-art supervised and semi-supervised approaches.

---


### 677. [Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks](https://arxiv.org/abs/2610.17998)

**<font color=#1a73e8>作者：</font>** Francesco Panetta, Federico Di Valerio, Michela Proietti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only explanations based on spike activity. These explanations are temporally aggregated into spatial attention maps and used to select the most informative image patches for replay, instead of storing full images. Experiments on Split CIFAR10 and Split CIFAR100 show that SAM-guided EPR improves the accuracy-memory trade-off under tight memory budgets, and remains competitive while requiring substantially less storage.

---


### 678. [Surface Reconstruction from Range Scans Under Visibility Constraints](https://arxiv.org/abs/2610.18005)

**<font color=#1a73e8>作者：</font>** Gabriel Lenain, Edmond Boyer, Jean Ponce  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface reconstruction from range scans is challenging in the presence of noise and outliers, as fidelity to observations must be balanced against sensitivity to measurement errors. Yet, most neural approaches discard the sensor positions and corresponding visibility information, compensating for this loss with geometric priors or regularization terms. We instead formulate surface reconstruction as robust regression of the predicted first surface intersection along each acquisition ray against its measured depth, which penalizes predicted surface intersections within the segment between the sensor and the observed point. We represent the surface as the zero set of a 1-Lipschitz multi-layer perceptron, allowing the use of linearly convergent sphere tracing to compute the first hit, and use a robust Huber loss for regression. Our formulation requires neither oriented normals, sampled off-surface points, nor an eikonal loss. Comparisons with the state of the art on synthetic and real data with varying levels of noise and outlier contamination demonstrate competitive performance on clean data and much improved fidelity and robustness under even moderate corruption. Our analysis further confirms a trade-off between fidelity and robustness: greater fitting capacity improves data fidelity in the clean case but increases sensitivity to the measurement errors inherent in real acquisitions, with a sweet spot typically emerging at intermediate capacity.

---


### 679. [Dynamic Interpolation for Training-Time Prediction Reshaping in Low-Light Image Enhancement](https://arxiv.org/abs/2610.18018)

**<font color=#1a73e8>作者：</font>** Peirui Zhu, Shijie Hao, Jingxi Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) is an important image/video processing problem for reliable visual systems under poor illumination, yet it remains challenging due to the strong coupling among insufficient illumination, noise amplification, and structural degradation. Existing methods typically rely on sophisticated network architectures or engineered objective functions. While effective, the former increases model complexity and deployment burden, whereas the latter relies on empirically tuned loss weights. We revisit supervised LLIE from a training-dynamics perspective and observe that brightness-related errors tend to converge early, while residual noise and structural artifacts often remain insufficiently optimized in later stages. To address this issue, we propose a Dynamic Interpolation Training-only Module (DITM), which introduces no additional learnable parameters and adaptively reshapes the model prediction for supervised feed-forward LLIE training. Specifically, DITM employs brightness-aware interpolation, in which the model prediction is combined with a mean brightness-aligned image constructed by rescaling the model prediction according to the mean brightness of the ground-truth image. By reducing the relative dominance of global brightness discrepancy, DITM makes residual local errors more influential during backpropagation after global luminance has largely stabilized, thereby facilitating artifact suppression and fine-detail restoration in later training stages. DITM is used only during training and is fully removed at inference, introducing no additional inference cost. Extensive experiments on multiple benchmark datasets and CNN-, Transformer-, and Mamba-based LLIE backbones show that DITM consistently improves fidelity and perceptual quality while preserving the inference-time architecture and introducing no additional inference-time computation.

---


### 680. [FlowSim: Rendering-Free Closed-Loop Simulation for Evaluating End-to-End Driving Systems](https://arxiv.org/abs/2610.18030)

**<font color=#1a73e8>作者：</font>** Hanfeng Wu, Alvaro Marcos-Ramiro, Michael Schmidt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Closed-loop evaluation of end-to-end (E2E) driving systems typically relies on generating sensor observations and re-processing them through the perception encoder, introducing substantial computational cost and a sim2real gap between simulated and real sensor observations. In this paper, we ask a more fundamental question: is image-space simulation necessary for closed-loop evaluation of E2E driving systems? We propose FlowSim, a rendering-free simulation paradigm that predicts the internal latent representation directly from a previous latent and target-frame symbolic scene conditions. The predicted latent is then processed by the original frozen downstream modules, eliminating image rendering and perception re-encoding. Explicit cross-frame agent association improves latent transition prediction and rollout stability, while variable-horizon simulation enables long-horizon prediction from a common real anchor without accumulating intermediate rollout errors. Experiments on nuScenes and NavSim demonstrate that FlowSim preserves downstream behavior competitively with, and often exceeds image-space simulation in source-to-reference agreement across variable simulation horizons and both dense and sparse latent representations. By predicting the latent directly, both instantiations of FlowSim simulate each step in 0.04--0.06s, substantially faster than the image-space simulation methods they are compared against. These results establish FlowSim as an efficient and practical alternative to conventional image-space simulation methods.

---


### 681. [COMPASS: Contextual Moment Prior Alignment for Generalizable AIGI Detection](https://arxiv.org/abs/2610.18034)

**<font color=#1a73e8>作者：</font>** Zhan Yang, Tiancheng Shen, Weijie Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable AI-generated image (AIGI) and deepfake detection remain challenging due to the asymmetry phenomenon, where adaptation to limited training distributions can degrade the transferable representations of Vision Foundation Models (VFMs). Recent subspace adaptation methods mitigate this issue by freezing high-magnitude principal components while adapting the residual subspace. However, such magnitude-based decomposition is data-agnostic and does not explicitly account for target-relevant semantics, potentially leading to semantic misalignment. We propose COMPASS (COntextual Moment Prior Alignment for Subspace Separation), a data-aware subspace adaptation framework that uses a small unlabeled Semantic Proxy Set to estimate target activation statistics. COMPASS incorporates activation covariance into the decomposition of pre-trained weights, preserving target-relevant representations as a stable semantic reference while the residual adapter learns forgery-related variations. The proxy calibration requires no gradient-based optimization. Extensive experiments demonstrate strong generalization across cross-dataset, cross-method, joint cross-dataset-method, and open-world cross-generator evaluations, achieving state-of-the-art performance on both Deepfake and AIGI detection benchmarks.

---


### 682. [Scaling Vision Transformers Without Training: Prune-and-Merge Token Compression](https://arxiv.org/abs/2610.18039)

**<font color=#1a73e8>作者：</font>** Vatsal, Soumil Malhotra, Priyanshu Chahal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers achieve strong performance but incur high computational costs from quadratic token interactions. Training-free token reduction methods improve efficiency, but their robustness remains underexplored. We propose Prune-and Merge ViT, a training-free framework for off-the-shelf models. It combines class attention-based pruning with similarity-based merging to reduce redundancy while preserving semantic information. To evaluate robustness we introduce two metrics. Relative Accuracy Drop (RAD) measures relative accuracy degradation under transformations, and Prediction Flip Rate (PFR) quantifies prediction consistency. On pretrained ViT and DeiT, Prune-and-Merge reduces computation competitively while maintaining robustness and better accuracy than existing token reduction methods. Our analysis suggests that hybrid token reduction does not introduce hallucination-like behavior and preserves prediction stability for common image transformations.

---


### 683. [Beyond Black Boxes: Visual Grounding for Text Embeddings](https://arxiv.org/abs/2610.18047)

**<font color=#1a73e8>作者：</font>** Slimane Larabi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, our goal is to represent text embeddings as sketches for three main reasons. First, to visualize text representation and to explore their potential their potential for AI explainability. Second, to investigate the potential benefits of the sketch-based representation for information retrieval. Third, to explore their potential for reasoning, drawing inspiration from the concept of mental imagery. We propose a sketch-based visual grounding framework that transforms text representations into visual topographic sketches. Our approach aims to emphasis the semantics content encoded in the text embeddings through the corresponding sketch.
Evaluations are conducted on the MS-COCO dataset to examine the utility of these sketches for text retrieval. The comparative study of SBERT and Sketch-based method reveals that SBERT retains an advantage in strict top-1 retrieval accuracy while achieving comparable performance to the sketch-based method in top-5 retrieval. A cascaded approach combining SBERT and the sketch-based method outperforms SBERT alone, suggesting that the Sketch-based representation could offer significant potential for information retrieval if trained directly on text.

---


### 684. [Privacy-Preserving GNN Inference on Financial Transaction Graphs via Homomorphic Encryption](https://arxiv.org/abs/2610.18054)

**<font color=#1a73e8>作者：</font>** H. Çağrı Bilgi, Kemal Mutluergil, Ceren Yıldırım 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anti-money laundering (AML) in financial networks requires modeling transaction patterns that span multiple institutions. In practice, however, banks cannot share account and transaction features due to strict privacy regulations. We propose a privacy-preserving graph neural network (GNN) inference framework tailored to this multi-bank setting. A central server holds the graph connectivity and pretrained model weights in plaintext, while each bank keeps its transaction features encrypted. Inference is then carried out entirely on encrypted features under the CKKS homomorphic encryption scheme, so that no plaintext transaction features or predictions are exposed to the server. The key to making this practical is an edge-centric GNN architecture, wherein message passing is expressed through operations on node--edge incidence matrices. This formulation not only preserves the edge-attributed multigraph structure of transaction networks but also reduces every aggregation step to plaintext--ciphertext matrix products. Since CKKS can evaluate only polynomial circuits, we also approximate each nonlinearity with a composite polynomial of the sign function, which we calibrate per activation site. On the IBM AML benchmark, our model achieves performance competitive with plaintext baselines, and with a consumer-grade GPU, classifies each queried transaction end-to-end in as little as \textbf{5.31} seconds, while per-transaction latency can be amortized to \textbf{1.65} seconds when optimized for throughput.

---


### 685. [From Policy Evaluation to Off-Policy Control: Provable Emergence of In-Context Q-Learning](https://arxiv.org/abs/2610.18057)

**<font color=#1a73e8>作者：</font>** Yingjun Mo, Yajie Zhao, Fang Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers can implement reinforcement-learning algorithms in context, yet how off-policy control emerges within Transformers remains poorly understood. We study Q-learning, a foundational model-free control algorithm that combines off-policy bootstrapping with greedy policy improvement. We prove that a two-layer attention-only Transformer can implement a finite-temperature form of Q-learning, where the temperature $\tau>0$ controls the approximation to greedy action selection, recovering window Q-learning as $\tau\to0$. We train the structured Transformer on randomly generated MDP tasks using output-only supervision. Experiments show that the theoretically predicted parameter structure emerges during training, including the internal greedy action-selection mechanism, and that the trained Transformer achieves performance comparable to Q-learning on unseen tasks. Our theoretical analysis further shows that the equivalent realizations form a solution manifold and that, under suitable task-diversity conditions, the training iterates converge locally to this manifold at an exponential rate. For the random-task model analyzed here, the local worst-case number of gradient steps needed to reduce the distance to the manifold by a factor $\epsilon$ is $\Theta\left(\tau^{-5}\log(1/\varepsilon)\right)$, quantifying the increasing optimization cost as the learned update approaches window Q-learning.

---


### 686. [A Benchmark for Bangla Task-Oriented Dialogue Understanding](https://arxiv.org/abs/2610.18060)

**<font color=#1a73e8>作者：</font>** Afrina Alam Lamia, Sumiaya Sharif, Prottoy Modak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented dialogue understanding remains underexplored for Bangla, particularly in multilingual settings involving English and romanized Bangla (Banglish). We introduce BanglaTOD, a parallel tri-lingual benchmark comprising 209 multi-turn dialogues across nine Bangladesh-specific service domains and 64 intents. Each conversational turn is aligned across Bangla, English, and Banglish, yielding 4,689 language-specific turn records annotated with intents, token-level slots, state updates, and accumulated dialogue states. We establish context-aware baselines for joint intent classification and slot filling using mBERT, BERT-base-uncased, and BanglaBERT. Cross-language analysis reveals substantial performance differences across models and linguistic representations, while removing dialogue history reduces intent accuracy by 19.0--25.7 percentage points. BanglaTOD provides a foundation for multilingual dialogue understanding and future dialogue state tracking research in Bangladesh-specific conversational applications. The dataset is publicly available at \href{this https URL}{Hugging Face}.

---


### 687. [Uncertainty Evaluation: Bridging Machine Learning and Measurement Science](https://arxiv.org/abs/2610.18066)

**<font color=#1a73e8>作者：</font>** Dario Petri, Luca Mari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty evaluation is essential for assessing the trustworthiness of machine learning (ML) predictions, particularly in safety-critical applications. This paper explores conceptual analogies between uncertainty evaluation in ML and measurement science, drawing on the evolution of metrology from error-based approaches to the framework established by the Guide to the Expression of Uncertainty in Measurement (GUM). Particular attention is devoted to the distinction between process-level and result-level quality and to the limitations of the conventional classification of ML uncertainty into aleatoric and epistemic components. It is argued that this dichotomy, similarly to the traditional distinction between random and systematic measurement errors, is inherently model-dependent and provides an insufficient basis for a unified uncertainty evaluation framework. Further analogies between machine learning and measurement field of knowledge are identified concerning distribution shifts, anomalous operating conditions, and the validity of uncertainty evaluation. Building on the proposed considerations, the paper advocates a metrology-inspired approach based on the systematic identification, quantification, and propagation of uncertainty contributions. By extending the methodology already established in measurement science to ML, this approach could offer a potentially rigorous, consistent, and transferable framework for evaluating the trustworthiness of individual predictions.

---


### 688. [Causal Discovery Under Hard Selection Bias: A New Robust Score-Matching Approach](https://arxiv.org/abs/2610.18075)

**<font color=#1a73e8>作者：</font>** Yiwen Qiu, Francesco Montagna, Shimeng Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selection bias is a difficult yet widespread problem in causal discovery, occurring whenever non-random selection processes lead to data that is not representative of the underlying populations. Due to its practical importance, related works have been proposed to address the problem under local [Versteeg et al., 2022] or interventional settings [Dai et al., 2025a], but general algorithms for observational data remain elusive. In this paper, we focus on truncated data (hard selection), and provide a general result for Additive Noise Models (ANM). We show that score-based methods are a surprisingly suitable candidate due to a special property of the score function ($\nabla \log p(x)$): deterministic truncation preserves both the score of the joint distribution as well as the Jacobian of the score. While established score-matching algorithms still fail in most settings, we actively leverage this observation to propose a new method for causal discovery that is robust under truncated data with ANMs. Overall, our approach offers a general, robust solution that is agnostic to external information about the selection process and still achieves comparable performance to the state-of-the-art approaches when selection is not present.

---


### 689. [Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization](https://arxiv.org/abs/2610.18085)

**<font color=#1a73e8>作者：</font>** Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the mismatch between parameter and update scales. To make runs restarted from equivalent checkpoints follow the same trajectory, we balance matrix pairs and transform their moment estimates together, bringing distinct but equivalent training states to the same starting point. To correct scale imbalance between paired Transformer matrices without changing predictions, we propose Symmetry-Aware Gradient Geometry Stabilization (SAGGS), which periodically equalizes the Frobenius norms of exact symmetry pairs, and its damped variant, Soft SAGGS. SAGGS reduces perplexity (PPL) by $0.374\pm0.026$ at 101M parameters on WikiText-103, and Soft SAGGS reduces PPL by $0.780\pm0.040$ in a 31M modern-architecture replication, both under scale imbalance. In a 123.8M checkpoint-resume experiment, reciprocally rescaling matrix pairs barely changes validation loss at restart but increases final PPL by $3.78\pm0.42$; hard and soft rebalancing recover to within $0.02$ PPL of the control.

---


### 690. [One-Sided Verification Under Limited Expert Review](https://arxiv.org/abs/2610.18089)

**<font color=#1a73e8>作者：</font>** Fan Nie, Haotian Ye, Shurui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI has become increasingly helpful in scientific discovery, yet human expert review remains essential for those problems without reliable automated evaluation, posing a fundamental challenge as candidate generation scales beyond available review capacity. This paper studies verification under limited human effort, where rare valid solutions need to be prioritized while invalid candidates should be filtered out to reduce human workload. We adopt the one-sided verification objective that maximizes the rejection rate of invalid solutions (TNR) under a constraint on the false-rejection rate of valid ones (FNR), making human review cost an explicit term to minimize. Drawing on the intuition that verifying a specific error can be easier than discovering one, we introduce OSVerify, an algorithmic framework that decouples error proposal from error validation. The error proposer searches for errors in solutions across different granularities by hierarchical decomposition, while the validator distinguishes substantial errors from minor or hallucinated ones. Experiments on competition- and research-level benchmarks show that OSVerify reduces the number of human reviews of invalid solutions by 46% on average compared to voting baselines under the same empirical low FNR constraint. Our post-training of the validator further improves the reduction to 57%. As high-impact real-world use cases, we apply OSVerify to identify errors in published research papers that are subsequently confirmed by the original authors and help resolve three Langlands open conjectures that are confirmed by experts, demonstrating its utility to facilitate human-AI research collaboration.

---


### 691. [APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation](https://arxiv.org/abs/2610.18097)

**<font color=#1a73e8>作者：</font>** Sirui Zhang, Fangyun Wei, Dong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability profile. APT coordinates three agents to construct evaluation sets from user requirements, diagnose model-specific strengths and failure modes, and generate reinforcement learning data with an adaptive prompt distribution that emphasizes underperforming capabilities. By repeatedly evaluating, diagnosing, and updating the generator, APT lets the current model's behavior shape its next training tasks, forming a feedback loop inspired by recursive self-improvement. For general-purpose settings without user-specified evaluation scenarios, we further develop an evaluation harness that enables broad and diverse evaluation set generation. Experiments across multiple base models, benchmarks, and generation architectures demonstrate that APT is model-agnostic, benchmark-agnostic, architecture-agnostic, and fully automated.

---


### 692. [The Effect of Layer Ordering in Hybrid Architectures](https://arxiv.org/abs/2610.18104)

**<font color=#1a73e8>作者：</font>** John Cooper, Mingchen Ma, Jiaqi Mo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid attention is rapidly becoming the dominant architectural choice for frontier models. Despite their successes, such architectures complicate model design by introducing additional choices, including the types and locations of layers. This combinatorially large design space has been studied empirically, but given the vast expense of training and evaluating models with different configurations, a principled understanding of the effects of layer selection and ordering is needed. We provide the first such analysis, showing that the dominant hybrid architecture is highly task-specific. Concretely, for any layer configuration, we prove that there exists a task where we can construct a model with this configuration that provably outperforms any other model of any different configuration under fixed resource constraints. Empirically, we observe that for standard training, learned hybrid architectures exhibit separations between layer orderings that match our theoretical findings. For instance, under the same memory budget, the optimal architecture predicted by our theory for a segmented retrieval task consistently achieves perfect accuracy, whereas the next strongest plateaus below 0.5. These results extend to deeper models, where ``containing'' the dominant architecture for a task indicates whether the model attains high performance. In addition, we investigate the mechanisms learned by hybrids, observing that Transformer layers contribute the largest share of performance on associative recall across architectures. This work establishes insights into task-dependent hybrid architecture design relevant to the training and scaling of frontier-scale hybrids.

---


### 693. [SYNPRED: A Synergistic Approach to Multimodal Learning for Clinical Prediction](https://arxiv.org/abs/2610.18110)

**<font color=#1a73e8>作者：</font>** Ivana Janíčková, Yen Y. Tan, Thomas H. Helbich 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal medical data captures complementary aspects of disease. It provides a comprehensive basis for diagnosis and the identification of biological associations linked to progression or treatment response. Established contrastive learning approaches exploit shared information across modalities, but fall short in exploiting complementary, modality-specific signals relevant for a task. Here, we propose a synergistic multimodal variational autoencoder (VAE) framework that separates task-relevant unimodal and multimodal information from instance-specific variation task-irrelevant, allowing complementary signals across modalities to be leveraged for prediction. The method yields benefits even if modalities are missing at test time. We evaluate the method on a treatment response prediction task using medical imaging and RNA data. Empirical comparison with alignment-based and multimodal VAE state-of-the-art approaches demonstrates improved multimodal prediction performance, and consistent benefits for prediction from a single modality after multimodal training. The full code can be found here: this https URL.

---


### 694. [When Missingness Follows the Graph: Beyond Feature Propagation for Missing Features](https://arxiv.org/abs/2610.18113)

**<font color=#1a73e8>作者：</font>** Enrico Chialà, Francesco Ferrini, Antonio Longa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) commonly assume that node features are fully observed, despite missing features being pervasive in real-world applications. By leveraging the dependence between node features and graph structure, existing graph-specific methods handle missingness by propagating observed feature values along graph edges. However, these methods have mainly been evaluated in overly optimistic settings, where feature entries are removed independently and uniformly across the graph. This overlooks realistic scenarios in which missingness propagates among connected nodes, as can occur during localized sensing failures in sensor networks. We formalize this complementary notion as graph-structured mask dependence, where the joint distribution of missingness indicators is shaped by the graph, and introduce a controlled mechanism that instantiates this setting. We study propagation-based methods theoretically and empirically in this setting, showing that their effectiveness changes substantially compared with the uniformly random regime. Motivated by this limitation, we propose PEMix, designed to remain effective under challenging graph-structured missingness. Rather than propagating observed values, PEMix uses global structural representations to condition a probabilistic model of incomplete node features before message passing. Experiments under controlled graph-structured missingness and naturally occurring missingness show that PEMix remains robust across complex missingness regimes, with particularly strong performance as missingness becomes severe.

---


### 695. [Human-Inspired Asymmetric Collaboration for Dual-Student Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2610.18133)

**<font color=#1a73e8>作者：</font>** Huiyi Ren, Ziming Fang, Jiaming Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-student learning enriches predictive diversity in SSMIS by introducing a strongly augmented view alongside a weakly augmented view. Insufficient strong augmentation may homogenize the students, whereas excessive augmentation can corrupt anatomical evidence and destabilize collaboration. This challenge echoes feedback-regulated human instruction, where learners receive differentiated tasks and the task difficulty is continually adjusted according to their evolving responses. Inspired by these, we propose Human-Inspired Asymmetric Collaboration (HAC), a closed-loop dual-student framework that maintains weak--strong learning through adaptive difficulty calibration and geometry preservation. Specifically, Reinforcement-guided Difficulty Calibration (RDC) formulates strong-augmentation control as a window-level reinforcement learning process, using augmentation history, realized perturbations, and training responses to dynamically adjust the augmentation magnitude, operation number, and magnitude range. Meanwhile, the Gramian Geometry Preservation Constraint (G2PC) preserves the early-stage three-branch geometry through global volume and pairwise area constraints, preventing shared supervision from homogenizing the two students. Comprehensive evaluations across LA, Pancreas, and BraTS-2019 validate both the segmentation effectiveness and capability-aware difficulty calibration of HAC.

---


### 696. [FlowCred: Hierarchical Credit Assignment and Functional Coordination for Joint Text-to-Video Post-Training](https://arxiv.org/abs/2610.18142)

**<font color=#1a73e8>作者：</font>** Mingxuan Zhu, Yanwei Huang, Shiyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt optimization and generator post-training are two complementary ways to improve text-to-video (T2V) generation, and recent systems increasingly train both modules jointly. However, optimizing a prompt policy and a video generator from the same terminal reward creates two ambiguities: prompt quality is confounded with stochastic generation, and the two modules may realize overlapping local improvements. We introduce FlowCred, a two-level framework for joint T2V post-training. First, hierarchical credit assignment uses matched prompt-seed rollout grids to separate prompt-level credit from prompt-conditioned generator residuals under shared randomness. Second, functional coordination probes alternative current-policy prompts at states from actual generation trajectories, providing generator-aware evidence for prompt optimization while selectively attenuating generator updates already supported by conditioning changes. Across multiple T2V benchmarks, FlowCred consistently improves matched joint-training baselines. On LTX-2.5, FlowCred improves a strictly matched joint-training control from 61.47 to 64.46 on T2V-CompBench and from 55.58 to 58.08 on StoryEval, without increasing decoded-video or reward-model-call budgets. Factorial and realized-update analyses show complementary contributions from prompt shaping and generator routing, while human evaluation and transfer across backbones and updater families provide further supporting evidence.

---


### 697. [Attacking Only Half the Data: Two-Sided Evaluation of AI-Text Detector Robustness](https://arxiv.org/abs/2610.18151)

**<font color=#1a73e8>作者：</font>** Apu Chandraw Shill, Rabindra Nath Nandi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the robustness of widely used AI text detectors under attacks applied to both human and machine text. Prior evaluations typically attack only machine text, overlooking that human text is routinely modified through grammar correction, formatting, or invisible character insertion. We introduce a two-sided protocol that applies attacks to both classes. Across two corpora and nine detectors, reported AUROC gains vanish under two-sided evaluation, with attacked human text misclassified at rates up to 100%. While simple preprocessing reverses character-level attacks, word-level synonym substitution remains effective meaning-preserving, and irreversible.

---


### 698. [Learning a Group Element from Its Action: Galois Correspondences, Optimal ERM, and an Abel-Ruffini Threshold for the Natarajan Dimension](https://arxiv.org/abs/2610.18154)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning an unknown element $g$ of a group acting with finite orbits on a countable set, from examples $(x,gx)$. After a sample on $A$, the consistent hypotheses are the restrictions of a coset of the pointwise stabilizer of $A$, and the sample forces exactly the labels of points this stabilizer fixes; for a Galois group, they form the field generated by the data. Through this correspondence, multiclass dimensions become group invariants: the DS and graph dimensions equal the height, the Littlestone dimension the longest irredundant sequence length, and the teaching dimension the minimal base size. Among deterministic learners, symmetry makes empirical risk minimization optimal: on nondegenerate classes every consistent learner, whatever its tie-breaking, attains the optimal realizable sample complexity up to constant factors, and every consistent online learner the optimal mistake bound. Agnostically, every ERM's sample complexity exceeds the known lower bound by at most the DS-to-Natarajan ratio, up to constants. For finite Galois extensions of countable fields, the Natarajan dimension equals a group invariant, the coset-cube number, which is at least the number of complemented factors of any chief series of any subgroup. Hence the dimensions coincide for every solvable Galois group, while for the groups $A_5$ and $S_5$ of the quintic they are $2<3$ and $3<4$, and $A_5$ is the smallest group with a gap. For the Galois group $S_n$ of the general equation of degree $n$, they coincide exactly when $n\le 4$, i.e., in characteristic zero, exactly when the equation is solvable by radicals; the implication is one-way, as the simple group $\mathrm{PSL}(2,8)$ has no gap. For linear, orthogonal and unitary maps of $\mathbb R^d$ or $\mathbb C^d$ both dimensions equal $d$, and a two-fibered pseudo-cube is a disjoint union of Natarajan cubes exactly when its monodromy group is abelian.

---


### 699. [When Do Learned Blocks Preserve Causal Meaning? Block Identifiability and Constructive Causal Abstractions](https://arxiv.org/abs/2610.18155)

**<font color=#1a73e8>作者：</font>** Karim Zaghw, Wieland Brendel, Patrik Reizinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard identifiability theory assumes one-dimensional latent factors, but learned representations can encode latent information across multidimensional blocks whose internal coordinates are not uniquely determined. When such blocks are used to represent and intervene on higher-level concepts, it is unclear whether their causal meaning survives the transformations left unresolved by block-identifiability. We connect block-identifiability to constructive causal abstraction. We show that block-diagonal invertible transformations followed by compatible coordinate permutations form the maximal class that preserves every constructive causal abstraction built on those blocks. This guarantee assumes that the correspondence between blocks and concepts is updated with the representation. A small synthetic experiment with additive autoencoders shows that high-level interventions can be transferred between independently learned representations while approximately preserving their intended effects.

---


### 700. [When and How Order-Flow Interventions Work After Dealers Adapt](https://arxiv.org/abs/2610.18158)

**<font color=#1a73e8>作者：</font>** Guanghao Wu, Zhuo Cai, Zhidong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning dealer agents can settle on persistently wide quotes, raising what customers pay to trade. A venue can route more orders to tighter quotes, but a wide quote may reflect real risk, and once dealers adapt, an end-to-end comparison cannot show why a rule works: because it intervenes more, picks better moments, is announced in advance, or rewards the right quote. We propose SOFA (State-aligned Order-Flow Allocation), a public order-flow contract with three parts: a State Scorer ranks market states from lagged public data, a Commitment Scheduler announces a budgeted intervention strength before dealers quote, and a Quote-to-Flow Allocator shifts a bounded share of fixed customer demand toward tighter quotes. Our paired re-adaptation protocol gives competing rules the same intervention strengths, only re-timed, lets dealers re-adapt to each rule from a shared checkpoint, and breaks one link at a time. Across 20 independently trained dealer populations in an ABIDES market, concentrating the intervention in states that the score ranks as low-risk lowers low-risk execution cost relative to random timing in every population, by 0.040 tick on average, while a stale announcement or a broken quote-to-flow link raises this cost. In the primary setting the gain comes at the expense of high-risk trades, whose costs rise, so state alignment pays off only for a venue that weighs low-risk costs more than 1.38 times as heavily as high-risk costs. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**651-700**（第 14/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-700** | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
