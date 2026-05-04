# 📦 其他研究 | 2026年05月05日

> 本类共 **180** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-180**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-180**

---

### 151. [Budget Constraints as Riemannian Manifolds](https://arxiv.org/abs/2605.00649)

**<font color=#1a73e8>作者：</font>** Michael Helcig, Dan Alistarh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assigning one of K options to each of N groups under a total cost budget is a recurring problem in machine learning, appearing in mixed-precision quantization, non-uniform pruning, and expert selection. The objective (model loss) depends jointly on all assignments and does not decompose across groups, which prevents combinatorial solvers from optimizing the true objective directly and limits them to proxy objectives. Evolutionary search evaluates the actual loss but lacks gradient information, while penalty-based methods provide gradients but enforce the budget only approximately and require sensitive hyperparameter tuning. We observe that under softmax relaxation, the budget constraint defines a smooth Riemannian manifold in logit space with particularly simple geometry: the normal vector is available in closed form, shifting logits along the cost vector changes expected cost monotonically, allowing binary-search retraction, and vector transport reduces to a single inner product. Building on this structure, we propose Riemannian Constrained Optimization (RCO), which augments a standard Adam update with tangent projection, binary-search retraction, and momentum transport. Combined with Gumbel straight-through estimation and budget-constrained dynamic programming for discrete feasibility, RCO enables first-order optimization of the true objective under exact budget enforcement, without introducing constraint hyperparameters. On synthetic knapsack problems with known optima, the manifold-based constraint handling recovers optimal solutions, whereas penalty methods plateau at 83% of optimal. On LLM compression tasks, including mixed-precision quantization and MoE expert pruning, RCO matches or exceeds evolutionary search methods while requiring 3x to 16x lower wall-clock cost on the evaluated configurations.

---


### 152. [Reinforcement Learning with Markov Risk Measures and Multipattern Risk Approximation](https://arxiv.org/abs/2605.00654)

**<font color=#1a73e8>作者：</font>** Andrzej Ruszczynski, Tiangang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For a risk-averse finite-horizon Markov Decision Problem, we introduce a special class of Markov coherent risk measures, called mini-batch measures. We also define the class of multipattern risk-averse problems that generalizes the class of linear systems. We use both concepts in a feature-based $Q$-learning method with multipattern $Q$-factor approximation and we prove a high-probability regret bound of $\mathcal{O}\big(H^2 N^H \sqrt{ K}\big)$, where $H$ is the horizon, $N$ is the mini-batch size, and $K$ is the number of episodes. We also propose an economical version of the $Q$-learning method that streamlines the policy evaluation (backward) step. The theoretical results are illustrated on a stochastic assignment problem and a short-horizon multi-armed bandit problem.

---


### 153. [InpaintSLat: Inpainting Structured 3D Latents via Initial Noise Optimization](https://arxiv.org/abs/2605.00664)

**<font color=#1a73e8>作者：</font>** Jaeyoung Chung, Suyoung Lee, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a training-free approach for controllable 3D inpainting based on initial noise optimization. In the structured 3D latent diffusion framework, we observe that the underlying geometric structure is established during the early stages of the diffusion process and exhibits high sensitivity to the initial noise. Such characteristics compromise stability in tasks like inpainting and editing, where the model must ensure strict alignment with the existing context while synthesizing a new structure. In this paper, we introduce a strategy to optimize the initial noise within the structured 3D latent diffusion framework, ensuring high-fidelity 3D inpainting. Specifically, we update the initial noise by leveraging a backpropagation approximation grounded in the rectified flow model, with the spectral parameterization specially designed for robust and efficient structured 3D latent optimization. Experiments demonstrate consistent improvements in contextual consistency and prompt alignment over representative training-free inpainting baselines, establishing initial noise control as an independent dimension for 3D inpainting, orthogonal to conventional sampling trajectory manipulation.

---


### 154. [Prediction of Alzheimer's Disease Risk Factors from Retinal Images via Deep Learning: Development and Validation of Biologically Relevant Morphological Associations in the UK Biobank](https://arxiv.org/abs/2605.00665)

**<font color=#1a73e8>作者：</font>** Seowung Leem, Yunchao Yang, Adam J. Woods 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The systemic, metabolic, lifestyle factors have established associations with Alzheimer's Disease (AD) through epidemiologic and AD-specific biomarker studies. Whether colored fundus photography (CFP) contains retinal structural signatures corresponding to these AD-related risk domains remains unclear. To determine whether deep learning (DL) models can predict 12 AD-related risk factors from CFP and to characterize the retinal structures underlying these predictions, thereby assessing whether CFP reflects pathways to AD vulnerability. Using UK Biobank CFPs, DL models were trained using 62,876 images from 44,501 unique participants to predict 12 factors linked to AD incidence: 6 categorical (sex, smoking, sleeplessness, economic status, alcohol use, depression) and 6 continuous (age, age at completing education, BMI, systolic, diastolic blood pressure, HbA1c). Model performance, model saliency, and saliency-derived scores (CAM-Score) were evaluated and compared to retinal morphometry. The scores were also compared between incident-AD cases (average 8.55 years before onset) and matched controls. Performance of DL ranged from AUROC= 0.5654-0.9480 for categorical and R2=-0.0291-0.7620 for continuous factors, outperforming most of the morphometry-machine learning models. Saliency-based score consistently highlighted biologically meaningful regions, particularly the optic nerve head and retinal vasculature. It also aligned with present morphometric variations. Several saliency-based scores differed significantly between incident AD and matched controls, suggesting potential overlap between retinal correlates of risk factors and preclinical AD-associated changes. CFP encodes retinal signatures linked to AD risk factors. Although not diagnostic, DL-derived retinal representations may uncover biologically meaningful risk-related structural changes mirroring the potential AD vulnerability.

---


### 155. [Augmented Lagrangian Multiplier Network for State-wise Safety in Reinforcement Learning](https://arxiv.org/abs/2605.00667)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Yujie Yang, Yao Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety is a primary challenge in real-world reinforcement learning (RL). Formulating safety requirements as state-wise constraints has become a prominent paradigm. Handling state-wise constraints with the Lagrangian method requires a distinct multiplier for every state, necessitating neural networks to approximate them as a multiplier network. However, applying standard dual gradient ascent to multiplier networks induces severe training oscillations. This is because the inherent instability of dual ascent is exacerbated by network generalization -- local overshoots and delayed updates propagate to adjacent states, further amplifying policy fluctuations. Existing stabilization techniques are designed for scalar multipliers, which are inadequate for state-dependent multiplier networks. To address this challenge, we propose an augmented Lagrangian multiplier network (ALaM) framework for stable learning of state-wise multipliers. ALaM consists of two key components. First, a quadratic penalty is introduced into the augmented Lagrangian to compensate for delayed multiplier updates and establish the local convexity near the optimum, thereby mitigating policy oscillations. Second, the multiplier network is trained via supervised regression toward a dual target, which stabilizes training and promotes convergence. Theoretically, we show that ALaM guarantees multiplier convergence and thus recovers the optimal policy of the constrained problem. Building on this framework, we integrate soft actor-critic (SAC) with ALaM to develop the SAC-ALaM algorithm. Experiments demonstrate that SAC-ALaM outperforms state-of-the-art safe RL baselines in both safety and return, while also stabilizing training dynamics and learning well-calibrated multipliers for risk identification.

---


### 156. [DMDSC: A Dynamic-Margin Deep Simplex Classifier for Open-Set Recognition on Medical Image Datasets](https://arxiv.org/abs/2605.00675)

**<font color=#1a73e8>作者：</font>** Vishal, Arnav Aditya, Nitin Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging datasets are often characterized by extreme class imbalances, where rare pathologies are significantly underrepresented compared to common conditions. This imbalance poses a dual challenge for Open-Set Recognition (OSR): models must maintain high classification accuracy on known classes while reliably rejecting unknown samples unseen during training in the clinical settings. While recently proposed Deep Simplex Classifier (DSC)~\cite{cevikalp2024reaching} and UnCertainty-aware Deep Simplex Classifier (UCDSC)~\cite{Aditya_2026_WACV} successfully leverage Neural Collapse to ensure maximal inter-class separation, they rely on a uniform margin that does not account for the varying densities of medical classes.
In this paper, we propose DMDSC an enhanced framework featuring a dynamic margin approach. Our approach automatically adapts class-specific margins based on label frequency, enforcing a higher penalty and tighter feature clustering for rare pathologies to counteract the effects of data imbalance. Extensive experiments conducted on diverse medical benchmarks on BloodMNIST\cite{medmnistv2}, OCTMNIST\cite{medmnistv2}, DermaMNIST\cite{medmnistv2}, and BreaKHis~\cite{spanhol2015dataset} datasets, demonstrate that our framework outperforms state-of-the-art methods.

---


### 157. [Foundation AI Models for Aerosol Optical Depth Estimation from PACE Satellite Data](https://arxiv.org/abs/2605.00678)

**<font color=#1a73e8>作者：</font>** Zahid Hassan Tushar, Sanjay Purushotham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerosol Optical Depth (AOD) retrieval is essential for Earth observation, supporting applications from air quality monitoring to climate studies. Conventional physics-based AOD retrieval methods formulate the problem as a pixel-wise inversion, relying on radiative transfer modeling, memory-intensive look-up tables, and auxiliary meteorological data. While recent data-driven approaches have shown promise, many fail to exploit the spatial-spectral coherence of hyperspectral imagery, leading to spatially inconsistent and noise-sensitive retrievals. We present the first study exploring Foundation AI models for AOD retrieval and propose ViTCG, a Vision Transformer with Channel-wise Grouping-based spatial regression framework that reduces retrieval bias and error. ViTCG uses hyperspectral top-of-atmosphere radiance as input and jointly models spatial context and spectral information. Validation with PACE radiance observations demonstrates a 62% reduction in mean squared error compared to state-of-the-art foundation models, including Prithvi, and produces spatially coherent AOD fields.

---


### 158. [Learning to Act and Cooperate for Distributed Black-Box Consensus Optimization](https://arxiv.org/abs/2605.00691)

**<font color=#1a73e8>作者：</font>** Zi-Bo Qin, Feng-Feng Wei, Tai-You Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Distributed blackbox consensus optimization is a fundamental problem in multi-agent systems, where agents must improve a global objective using only local objective queries and limited neighbor communication. Existing methods largely rely on handcrafted update rules and static cooperation patterns, which often struggle to balance local adaptation, global coordination, and communication efficiency in heterogeneous nonconvex environments. In this paper, we take an initial step toward trajectory-driven self-design for distributed black-box consensus optimization. We first redesign the agent-level swarm dynamics with an adaptive internal mechanism tailored to decentralized consensus settings, improving the balance between exploration, convergence, and local escape. Built on top of this adaptive execution layer, we propose Learning to Act and Cooperate (LACMAS), a trajectorydriven framework in which large language models provide sparse highlevel guidance for shaping both agentinternal action behaviors and agentexternal cooperation patterns from historical optimization trajectories. We further introduce a phased cognitive scheduling strategy to activate different forms of adaptation in a resource-aware manner. Experiments on standard distributed black-box benchmarks and real-world distributed tasks show that LAC-MAS consistently improves solution quality, convergence efficiency, and communication efficiency over strong baselines, suggesting a practical route from handcrafted distributed coordination toward self-designing multi-agent optimization systems.

---


### 159. [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](https://arxiv.org/abs/2605.00702)

**<font color=#1a73e8>作者：</font>** Derong Xu, Shuochen Liu, Pengfei Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents require long-term user memory for consistent personalization, but limited context windows hinder tracking evolving preferences over long interactions. Existing memory systems mainly rely on static, hand-crafted update rules; although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable long-horizon optimization. Drawing on memory schema theory and the functional division between prefrontal regions and hippocampus regions, we introduce MemCoE, a cognition-inspired two-stage optimization framework that learns how memory should be organized and what information to update. In the first stage, we propose Memory Guideline Induction to optimize a global guideline via contrastive feedback interpreted as textual gradients; in the second stage, Guideline-Aligned Memory Policy Optimization uses the induced guideline to define structured process rewards and performs multi-turn RL to learn a guideline-following memory evolution policy. We evaluate on three personalization memory benchmarks, covering explicit/implicit preference and different sizes and noise, and observe consistent improvements over strong baselines with favorable robustness, transferability, and efficiency.

---


### 160. [PhysEdit: Physically-Consistent Region-Aware Image Editing via Adaptive Spatio-Temporal Reasoning](https://arxiv.org/abs/2605.00707)

**<font color=#1a73e8>作者：</font>** Guandong Li, Mengxia Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image editing instructions are heterogeneous: a color swap, an object insertion, and a physical-action edit all demand different spatial coverage and different reasoning depth, yet existing reasoning-based editors apply a single fixed inference recipe to every instruction. We argue that adaptivity along both the spatial and temporal axes is the missing degree of freedom, and we present PhysEdit, an editing framework built around this principle. PhysEdit introduces two inference-time modules that compose without retraining the backbone. At its core, (1) Complexity-Adaptive Reasoning Depth (CARD) predicts edit complexity directly from the instruction and reference image and allocates the reasoning step count N_r and reasoning-token length r per sample -- turning a previously fixed inference schedule into a conditional-computation problem. CARD is supported by (2) a Spatial Reasoning Mask (SRM) that extracts an instruction-conditioned spatial prior from cross-attention to confine reasoning to regions that semantically require it. On the full 737-case ImgEdit Basic-Edit Suite, PhysEdit delivers a 1.18x wall-clock speedup (64.3s vs. 76.1s per sample) over a strong reasoning baseline while slightly improving instruction adherence (CLIP-T 0.2283 vs. 0.2266, +0.7%) and matching identity preservation within noise (CLIP-I 0.8246 vs. 0.8280). The speedup is category-dependent and reaches 1.52x on appearance-level edits, validating CARD's adaptive allocation as the principal source of efficiency gain. A 30-sample pilot with full ablations isolates the contribution of each module.

---


### 161. [Deep Kernel Learning for Stratifying Glaucoma Trajectories](https://arxiv.org/abs/2605.00708)

**<font color=#1a73e8>作者：</font>** Bruce Rushing, Angela Danquah, Alireza Namazi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effectively stratifying patient risk in chronic diseases like glaucoma is a major clinical challenge. Clinicians need tools to identify patients at high risk of progression from sparse and irregularly-sampled electronic health records (EHRs). We propose a novel deep kernel learning (DKL) architecture that leverages a Gaussian Process (GP) backend. The GP's kernel is defined by a transformer-based feature extractor applied to clinical-BERT embeddings to model glaucoma patient trajectories from multimodal EHR data. Our method successfully identifies three clinically distinct patient subgroups. Crucially, the model learns to decouple disease progression from current severity, identifying a high-risk group with a worsening trajectory despite having better average visual acuity than a second, stably poor group. This reveals that the model learns to identify progression risk rather than just the current disease state. This ability to stratify patients based on their risk trajectory progression offers a powerful tool for clinical decision support, enabling targeted interventions for high-risk individuals and improving the management of glaucoma care.

---


### 162. [Aitchison Embeddings for Learning Compositional Graph Representations](https://arxiv.org/abs/2605.00716)

**<font color=#1a73e8>作者：</font>** Nikolaos Nakis, Chrysoula Kosma, Panagiotis Promponas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning is central to graph machine learning, powering tasks such as link prediction and node classification. However, most graph embeddings are hard to interpret, offering limited insight into how learned features relate to graph structure. Many networks naturally admit a role-mixture view, where nodes are best described as mixtures over latent archetypal factors. Motivated by this structure, we propose a compositional graph embedding framework grounded in Aitchison geometry, the canonical geometry for comparing mixtures. Nodes are represented as simplex-valued compositions and embedded via isometric log-ratio (ILR) coordinates, which preserve Aitchison distances while enabling unconstrained optimization in Euclidean space. This yields intrinsically interpretable embeddings whose geometry reflects relative trade-offs among archetypes and supports coherent behavior under component restriction; we consider both fixed and learnable ILR bases. Across node classification and link prediction, our method achieves competitive performance with strong baselines while providing explainability by construction rather than post-hoc. Finally, subcompositional coherence enables principled component restriction: removing and renormalizing subsets preserves a well-defined geometry, which we exploit via subcompositional dimensionality removal to probe how archetype groups influence representations and predictions.

---


### 163. [Learning Coarse-to-Fine Osteoarthritis Representations under Noisy Hierarchical Labels](https://arxiv.org/abs/2605.00718)

**<font color=#1a73e8>作者：</font>** Tongxu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knee osteoarthritis (OA) assessment involves a natural but often underused label hierarchy: a coarse binary OA decision and a fine-grained Kellgren--Lawrence (KL) severity grade. Existing deep learning studies commonly treat these targets as separate classification problems, either reducing OA assessment to disease presence or directly optimizing noisy ordinal KL labels. In this work, we ask whether this clinical hierarchy can serve as a representation-level supervisory prior. Rather than introducing a complex architecture, we use a deliberately simple dual-head model with a shared encoder and two task-specific heads as a probe of hierarchical supervision. We compare single-OA, single-KL, and dual-head training across multiple 3D backbones under the same test protocol. Beyond standard classification metrics, we perform paired statistical comparisons, analyze latent severity-axis geometry, and examine saliency overlap with cartilage regions. The results show that dual-head supervision produces backbone-dependent gains, with clear improvements in KL-related metrics for selected backbones. More importantly, the gains are accompanied by a more ordered coarse-to-fine latent organization and, for responsive backbones, stronger anatomical alignment of saliency with cartilage. These findings suggest that even simple hierarchical dual-head supervision can reshape disease representations under noisy coarse/fine labels, providing a useful inductive bias for OA diagnosis and severity grading.

---


### 164. [Unpaired Image Deraining Using Reward-Guided Self-Reinforcement Strategy](https://arxiv.org/abs/2605.00719)

**<font color=#1a73e8>作者：</font>** Yinghao Chen, Yeying Jin, Xiang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised deraining has attracted attention for its ability to learn the real-world distribution of rain without paired supervision. However, the lack of strong constraints makes it difficult for the network to converge, especially with the complex diversity of rain degradation. A key motivation is that high-quality deraining results occasionally emerge during training, which can be leveraged to guide the optimization process. To overcome these challenges, we introduce RGSUD (Reward-Guided Self-Reinforcement Unsupervised Image Deraining), comprising two key stages: reward recycling and self-reinforcement (SR) training. For the former stage, we propose an Image Quality Assessment (IQA)-based dynamic reward recycling mechanism that selects optimal derained outputs during training and continuously collects high-quality deraining images. In latter stage, we incorporate these rewards into the model's optimization process, constraining the optimization space and improving alignment between derained outputs and clean images. By leveraging IQA-based self-reinforced loss and dynamically updated rewards, we enhance the quality of synthesized pseudo-paired data and stabilize the optimization. Extensive experiments demonstrate that our method achieves SOTA performance across multiple datasets, including paired synthetic, paired real, and unpaired real images, outperforming existing unsupervised deraining approaches in both subjective and objective IQA metrics. Additionally, we show that the self-reinforcement strategy is adaptable to other unsupervised deraining methods and our deraining framework demonstrates strong generalization across existing supervised deraining networks.

---


### 165. [Exploring the Limits of End-to-End Feature-Affinity Propagation for Single-Point Supervised Infrared Small Target Detection](https://arxiv.org/abs/2605.00722)

**<font color=#1a73e8>作者：</font>** Qiancheng Zhou, Wenhua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-point supervised infrared small target detection (IRSTD) drastically reduces dense annotation costs. Current state-of-the-art (SOTA) methods achieve high precision by recovering mask supervision through explicit, offline pseudo-label construction, such as multi-stage active learning and physics-driven mask generation. In this paper, we study a minimalist alternative: generating point-to-mask supervision online through in-batch, point-anchored feature-affinity propagation. We instantiate this paradigm as GSACP, an end-to-end testbed that directly supervises the detector using hard-margin feature affinity gated by local image priors, entirely eliminating external label-evolution loops.
This compact design, however, exposes an optimization bottleneck. Because the affinity target is generated from the same feature representation being optimized, training forms a self-referential loop. We theoretically formalize this as \emph{Self-Referential Propagation Drift}, a representation-supervision entanglement that can sharpen true boundaries or distort the feature space to satisfy its own targets. To systematically isolate these failure modes, we apply a protocolized single-variable ablation procedure spanning local EMA teacher decoupling, hard-background contrastive separation, and adaptive support geometry.
On the SIRST3 dataset, GSACP-Final establishes a new ultra-low false-alarm operating regime, achieving a highly competitive $0.6674$ mIoU while demonstrating a $38\% relative reduction in false-positive artifacts ($\mathrm{Fa}$) compared with PAL. By systematically deconstructing the end-to-end paradigm, we map its performance boundaries and show that in-batch feature propagation provides a compact alternative for deployment scenarios where false-alarm suppression is paramount.

---


### 166. [Weisfeiler Lehman Test on Combinatorial Complexes: Generalized Expressive Power of Topological Neural Networks](https://arxiv.org/abs/2605.00725)

**<font color=#1a73e8>作者：</font>** Jiawen Chen, Qi Shao, Duxin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combinatorial complexes have unified set-based (e.g., graphs, hypergraphs) and part-whole (e.g., simplicial, cellular complexes) structures into a common topological framework. Existing topological neural networks and Weisfeiler-Lehman variants remain fragmented, lacking a unified theoretical foundation for topological deep learning. In this work, we introduce the Combinatorial Complex Weisfeiler-Lehman (CCWL) test, an axiomatic-style extension of the WL test to combinatorial complexes. CCWL formalizes topological message passing through four types of neighborhood relation and provides a unified perspective on the expressive power of higher-order variants. We further prove that upper and lower neighborhoods are sufficient among the four adjacent WL tests to reach the expressivity of the full CCWL framework across topological structures of combinatorial complexes. Building on this framework, we also propose the Combinatorial Complex Isomorphism Network (CCIN) and evaluate it on synthetic and real-world benchmarks. Experimental results indicate CCIN outperforms baseline methods and offers a generalized expressive framework for topological deep learning.

---


### 167. [Temporal Data Requirement for Predicting Unplanned Hospital Readmissions](https://arxiv.org/abs/2605.00738)

**<font color=#1a73e8>作者：</font>** Ramin Mohammadi, Vahab vahdat, Sarthak Jain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the proliferation of Electronic Health Records (EHRs), a critical challenge in building predictive models is determining the optimal historical data time window to maximize accuracy. This study investigates the impact of various observation windows ranging from the day of surgery to three years prior on predicting 30-day readmission following hip and knee arthroplasties. The dataset encompasses both structured encounter records (over 4 million) and unstructured clinical notes (80,000) from 7,174 patients. To extract meaning from the clinical notes, we employed a suite of non neural (BOW, count BOW, TF IDF, LDA) and neural encoders (BERT, 1D CNN, BiLSTM, Average). We subsequently evaluated models utilizing clinical notes alone, structured data alone, and a combination of both modalities. Our results demonstrate that the optimal time window for unstructured clinical notes is significantly shorter than for structured data, maximum predictive performance was achieved using notes from just three to six months prior to surgery. In contrast, performance using structured data improved as the time window lengthened, but strictly plateaued after twelve months. These modality-specific temporal patterns remained consistent regardless of model complexity or encoder type. Ultimately, these findings challenge the general assumption that more historical data inherently yields better machine learning predictions, establishing targeted time-window guidelines for optimizing readmission prediction models.

---


### 168. [Quantum Gradient-Based Approach for Edge and Corner Detection Using Sobel Kernels](https://arxiv.org/abs/2605.00744)

**<font color=#1a73e8>作者：</font>** Mohammad Aamir Sohail, Gabriela Pinheiro, Yasemin Poyraz Kocak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge detection refers to identifying points in a digital image where intensity changes sharply, indicating object boundaries or structural features. Corners are locations where gray-level intensity changes abruptly in multiple directions and are widely used in feature extraction, object tracking, and 3D modeling. In this study, we present a quantum implementation of Sobel-based edge detection and Harris-style corner detection. Two quantum image encoding methods - Flexible Representation of Quantum Images (FRQI) and Quantum Probability Image Encoding (QPIE) - are used to encode the input data and are comparatively analyzed. The proposed approach introduces a quantum gradient computation scheme based on lag-2 differences, enabling the evaluation of gradient-like features in superposition. To improve detection quality and reduce false positives, a classical post-processing step is applied to candidate corner points identified by the quantum circuit. Results show that the proposed quantum circuits produce outputs consistent with classical Sobel and Harris operators. Furthermore, the QPIE-based configuration yields more stable and coherent results than FRQI, especially under limited measurement shots. While gradient computation can be performed efficiently at the circuit level, the overall cost remains dominated by state preparation, measurement, and classical post-processing. All experiments are conducted under noiseless simulation, and performance on NISQ hardware may be affected by noise and measurement limitations. Therefore, this work demonstrates a functional and scalable quantum realization of classical edge and corner detection methods rather than an end-to-end speedup.

---


### 169. [NonZero: Interaction-Guided Exploration for Multi-Agent Monte Carlo Tree Search](https://arxiv.org/abs/2605.00751)

**<font color=#1a73e8>作者：</font>** Sizhe Tang, Zuyuan Zhang, Mahdi Imani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte Carlo Tree Search (MCTS) scales poorly in cooperative multi-agent domains because expansion must consider an exponentially large set of joint actions, severely limiting exploration under realistic search budgets. We propose NonZero, which keeps multi-agent MCTS tractable by running surrogate-guided selection over a low-dimensional nonlinear representation using an interaction-guided proposal rule, instead of directly exploring the full joint-action space. Our exploration uses an interaction score: single-agent deviations are ranked by predicted gain, while two-agent deviations are scored by a mixed-difference measure that reveals coordination benefits even when no single agent can improve alone. We formalize candidate proposal as a bandit problem over local deviations and derive a proposal rule, NonZero, with a sublinear local-regret guarantee for reaching approximate graph-local optima without enumerating the joint-action space. Empirically, NonZero improves sample efficiency and final performance on MatGame, SMAC, and SMACv2 relative to strong model-based and model-free baselines under matched search budgets.

---


### 170. [Learning the Helmholtz equation operator with DeepONet for non-parametric 2D geometries](https://arxiv.org/abs/2605.00760)

**<font color=#1a73e8>作者：</font>** Rodolphe Barlogis, Ferhat Tamssaouet, Quentin Falcoz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper deals with solving the 2D Helmholtz equation on non-parametric domains, leveraging a physics-informed neural operator network based on the DeepONet framework. We consider a 2D square domain with an inclusion of arbitrary boundary geometry at its center. This inclusion acts as a scatterer for an incoming harmonic wave. The aim is to learn the operator linking the geometry of the scatterer to the resulting scattered field. A signed distance function to the boundary of the inner inclusion, evaluated at several points in the domain, is used to encode its geometry. It serves as input for the branch part of the DeepONet architecture, while local information is used as input for the trunk part. This approach enables the encoding of arbitrary geometries, whether they are parameterized or not. The evaluation of the model on unseen geometries is compared with its finite element method (FEM) equivalent to test its generalization capabilities. The trained network weights implicitly embed the local physics and their interaction with the domain geometry. If the training space sufficiently covers the target evaluation space, the model can generalize accordingly. Furthermore, it can be refined to extend to another region of interest without retraining from scratch. This framework also avoids the need to remesh the domain for each geometry. The proposed approach delivers a computationally lighter surrogate model than FEM alternatives and avoids relying on FEM-generated training data.

---


### 171. [Meritocratic Fairness in Budgeted Combinatorial Multi-armed Bandits via Shapley Values](https://arxiv.org/abs/2605.00762)

**<font color=#1a73e8>作者：</font>** Shradha Sharma, Swapnil Dhamal, Shweta Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new framework for meritocratic fairness in budgeted combinatorial multi-armed bandits with full-bandit feedback (BCMAB-FBF). Unlike semi-bandit feedback, the contribution of individual arms is not received in full-bandit feedback, making the setting significantly more challenging. To compute arm contributions in BCMAB-FBF, we first extend the Shapley value, a classical solution concept from cooperative game theory, to the $K$-Shapley value, which captures the marginal contribution of an agent restricted to a set of size at most $K$. We show that $K$-Shapley value is a unique solution concept that satisfies Symmetry, Linearity, Null player, and efficiency properties. We next propose K-SVFair-FBF, a fairness-aware bandit algorithm that adaptively estimates $K$-Shapley value with unknown valuation function. Unlike standard bandit literature on full bandit feedback, K-SVFair-FBF not only learns the valuation function under full feedback setting but also mitigates the noise arising from Monte Carlo approximations. Theoretically, we prove that K-SVFair-FBF achieves $O(T^{3/4})$ regret bound on fairness regret. Through experiments on federated learning and social influence maximization datasets, we demonstrate that our approach achieves fairness and performs more effectively than existing baselines.

---


### 172. [Modeling Subjective Urban Perception with Human Gaze](https://arxiv.org/abs/2605.00764)

**<font color=#1a73e8>作者：</font>** Lin Che, Xi Wang, Marc Pollefeys 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban perception describes how people subjectively evaluate urban environments, shaping how cities are experienced and understood. Existing computational approaches primarily model urban perception directly from street view images, but largely ignore the human perceptual process through which such judgments are formed. In this paper, we introduce Place Pulse-Gaze, an urban perception dataset that augments street view images with synchronized eye-tracking recordings and individual perception labels. Based on this dataset, we propose a Gaze-Guided Urban Perception Framework to study how gaze behavior contributes to the modeling of subjective urban perception. The framework systematically investigates three complementary settings: gaze-only modeling, gaze fusion with explicit semantic scene representations, and gaze fusion with implicit richer visual representations. Experiments show that gaze alone already carries useful predictive signals for subjective urban perception, and that integrating gaze with scene representations further improves prediction under both semantic and richer visual representations. Overall, our findings highlight the importance of incorporating human perceptual processes into urban scene understanding and open a direction for gaze-guided multimodal urban computing.

---


### 173. [Characterizing the Expressivity of Local Attention in Transformers](https://arxiv.org/abs/2605.00768)

**<font color=#1a73e8>作者：</font>** Jiaoda Li, Ryan Cotterell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The transformer is the most popular neural architecture for language modeling. The cornerstone of the transformer is its global attention mechanism, which lets the model aggregate information from all preceding tokens before generating the next token. One common variant of attention is called local attention, which restricts each token to aggregating information from a bounded window of predecessors, reducing the quadratic cost of global attention to linear. Although this restriction is usually motivated by efficiency, it has also been found to improve model quality, a phenomenon that has so far lacked a satisfactory explanation. We provide a formal account of this phenomenon in terms of recognizer expressivity. It has been shown that fixed-precision transformers with global attention correspond to a fragment of linear temporal logic containing a single past operator. We additionally prove that adding local attention introduces a second temporal operator, strictly enlarging the class of recognizable regular languages. Moreover, global and local attention are expressively complementary: neither subsumes the other, and combining them yields the richest fragment. Experiments on formal language recognition and natural language modeling corroborate the theory, showing that hybrid global--local transformers outperform their global-only counterparts.

---


### 174. [Directed Social Regard: Surfacing Targeted Advocacy, Opposition, Aid, Harms, and Victimization in Online Media](https://arxiv.org/abs/2605.00776)

**<font color=#1a73e8>作者：</font>** Scott Friedman, Ruta Wheelock, Sonja Schmer-Galunder 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The language in online platforms, influence operations, and political rhetoric frequently directs a mix of pro-social sentiment (e.g., advocacy, helpfulness, compassion) and anti-social sentiment (e.g., threats, opposition, blame) at different topics, all in the same message. While many natural language processing (NLP) tools classify or score a text's overall sentiment as positive, neutral, or negative, these tools cannot report that positive and negative sentiments coexist, and they cannot report the target of those sentiments. This paper presents the Directed Social Regard (DSR) approach to multi-dimensional, multi-valence sentiment analysis, comprised of a pair of transformer-based models that (1) detects span-level targets of sentiment in a message and then (2) scores all spans within the message context along three (-1, 1) axes of regard that are motivated by social science theories of moral disengagement and moral framing. We present a data collection and annotation strategy for DSR dataset construction, a transformer-based architecture for span-level scoring, and a validation study with promising results. We apply the validated DSR model on six third-party datasets of online media and report meaningful correlations between DSR outputs and the labels and topics in these pre-existing social science datasets.

---


### 175. [Observable Performance Does Not Fully Reflect System Organization: A Multi-Level Analysis of Gait Dynamics Under Occlusal Constraint](https://arxiv.org/abs/2605.00778)

**<font color=#1a73e8>作者：</font>** Jacques Raynal, Pierre Slangen, Jacques Margerit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In biomechanical systems, observable performance is often used as a proxy for underlying system organization. However, this assumption implicitly presumes a correspondence between output metrics and internal system states that may not hold in adaptive systems. In this study, the vertical dimension of occlusion (VDO) is considered as a constraint applied to an adaptive neuromechanical system, enabling the exploration of system-level responses under controlled variations. A single-case design in a patient with Parkinson's disease allows an intra-individual analysis across repeated this http URL analysis is structured across three complementary levels: (i) aggregated linear metrics describing observable performance, (ii) a dynamical systems framework describing temporal organization in state space, and (iii) a latent space representation obtained through unsupervised embedding. The results show that conditions with comparable observable performance may correspond to different organizations in both state space and latent space representations. This dissociation highlights a limitation of aggregated metrics and suggests that similar outputs may arise from non-equivalent system states. A fourth level is proposed as a purely conceptual extension describing potential relationships between system states. This level is not implemented and is not derived from experimental data. These observations are strictly exploratory and non-causal. The proposed framework does not establish mechanistic, predictive, or directional relationships, but provides a structured approach for analyzing constraint-driven systems across multiple levels of representation.

---


### 176. [Map2World: Segment Map Conditioned Text to 3D World Generation](https://arxiv.org/abs/2605.00781)

**<font color=#1a73e8>作者：</font>** Jaeyoung Chung, Suyoung Lee, Jianfeng Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D world generation is essential for applications such as immersive content creation or autonomous driving simulation. Recent advances in 3D world generation have shown promising results; however, these methods are constrained by grid layouts and suffer from inconsistencies in object scale throughout the entire world. In this work, we introduce a novel framework, Map2World, that first enables 3D world generation conditioned on user-defined segment maps of arbitrary shapes and scales, ensuring global-scale consistency and flexibility across expansive environments. To further enhance the quality, we propose a detail enhancer network that generates fine details of the world. The detail enhancer enables the addition of fine-grained details without compromising overall scene coherence by incorporating global structure information. We design the entire pipeline to leverage strong priors from asset generators, achieving robust generalization across diverse domains, even under limited training data for scene generation. Extensive experiments demonstrate that our method significantly outperforms existing approaches in user-controllability, scale consistency, and content coherence, enabling users to generate 3D worlds under more complex conditions.

---


### 177. [SAVGO: Learning State-Action Value Geometry with Cosine Similarity for Continuous Control](https://arxiv.org/abs/2605.00787)

**<font color=#1a73e8>作者：</font>** Stavros Orfanoudakis, Pedro P. Vergara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While representation and similarity learning have improved the sample efficiency of Reinforcement Learning (RL), they are rarely used to shape policy updates directly in the action space. To bridge this gap, a geometry-aware RL algorithm that explicitly incorporates value-based similarity into the policy update, State-Action Value Geometry Optimization (SAVGO), is proposed. In detail, SAVGO learns a joint state-action embedding space in which pairs with similar action-value estimates exhibit high cosine similarity, while dissimilar pairs are mapped to distinct directions. This learned geometry enables the generation of a similarity kernel over candidate actions sampled at each update, allowing policy improvement to be guided directly toward higher-value regions beyond local gradient-based updates. As a result, representation learning, value estimation, and policy optimization are unified within a single geometry-consistent objective, while preserving the scalability of off-policy actor-critic training. The proposed method is evaluated on standard MuJoCo continuous-control benchmarks, demonstrating improvements over strong baselines on challenging high-dimensional tasks. Ablation studies are done to analyze the contributions of value-geometry learning and similarity-based policy updates.

---


### 178. [Repurposing Image Diffusion Models for Adversarial Synthetic Structured Data: A Case Study of Ground Truth Drift](https://arxiv.org/abs/2605.00788)

**<font color=#1a73e8>作者：</font>** Adam Arthur, Christopher Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public image diffusion models are now powerful enough that an attacker without the resources to train a tabular-specific generator may repurpose one off the shelf. This study tests that possibility directly. An unmodified Stable Diffusion U-Net is applied to the UCI Adult Income dataset by reshaping each row into a small single-channel pseudo-image. The architecture's inductive bias toward spatial locality makes feature placement a design variable, and several layouts are tested. However, this is only the beginning of the story, as this paper also draws two philosophical distinctions. One separates statistical from perceptual realism: whether synthetic content holds up to a machine's correlation audits or a human's sensory inspection. The other introduces synthetic evidence as a category alongside synthetic media: AI-generated material whose consumer is a machine in a closed evidentiary pipeline rather than a person in an open information system. An attacker succeeds with synthetic evidence by thinking like the machine that will receive it. And the more the attacker succeeds, the more they can induce ground truth drift: the silent reclassification of AI-generated outputs as authentic when reused in pipelines that do not interrogate their provenance.

---


### 179. [Prop-Chromeleon: Adaptive Haptic Props in Mixed Reality through Generative Artificial Intelligence](https://arxiv.org/abs/2605.00804)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Fengyuan Zhu, Bingjian Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed Reality (MR) aims to blend digital and physical worlds, but the absence of haptic feedback often breaks visual-tactile consistency. We introduce Prop-Chromeleon, a MR system based on generative artificial intelligence (AI) that dynamically transforms everyday objects into adaptive passive haptic props through user-provided text prompts. Our AI pipeline performs generation and anchoring of virtual assets that align with the shape of physical props, allowing us to study how virtual content generation behaves under geometric and prompt-based constraints. We evaluate Prop-Chromeleon's effectiveness through a generation study using varied object shapes and user prompts, combining quantitative shape similarity metrics with qualitative prompt fidelity analysis. Our user study further showcases Prop-Chromeleon's improvements in perceived realism, immersion, and enjoyment compared to static baselines. These results show that shape-aware generation can support both believable haptic interaction and creative engagement in MR.

---


### 180. [Posterior Augmented Flow Matching](https://arxiv.org/abs/2605.00825)

**<font color=#1a73e8>作者：</font>** George Stoica, Sayak Paul, Matthew Wallingford 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching (FM) trains a time-dependent vector field that transports samples from a simple prior to a complex data distribution. However, for high-dimensional images, each training sample supervises only a single trajectory and intermediate point, yielding an extremely sparse and high-variance training signal. This under-constrained supervision can cause flow collapse, where the learned dynamics memorize specific source-target pairings, mapping diverse inputs to overly similar outputs, failing to generalize. We introduce Posterior-Augmented Flow Matching (PAFM), a theoretically grounded generalization of FM that replaces single-target supervision with an expectation over an approximate posterior of valid target completions for a given intermediate state and condition. PAFM factorizes this intractable posterior into (i) the likelihood of the intermediate under a hypothesized endpoint and (ii) the prior probability of that endpoint under the condition, and uses an importance sampling scheme to construct a mixture over multiple candidate targets. We prove that PAFM yields an unbiased estimator of the original FM objective while substantially reducing gradient variance during training by aggregating information from many plausible continuation trajectories per intermediate. Finally, we show that PAFM improves over FM by up to 3.4 FID50K across different model scales (SiT-B/2 and SiT-XL/2), different architectures (SiT and MMDiT), and in both class and text conditioned benchmarks (ImageNet and CC12M), with a negligible increase in the compute overhead. Code: this https URL.

---


> [!TIP]
> 当前位于：**151-180**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-180**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
