# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 201. [Hybrid Quantum Reinforcement Learning with QAOA for Improved Vehicle Routing Optimization](https://arxiv.org/abs/2605.01574)

**<font color=#1a73e8>作者：</font>** T. Satyanarayana Murthy, B. Swathi Sowmya, Santhosh Voruganti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vehicle Routing Problem (VRP) is one of the most complex NP-hard combinatorial optimization problem in transportation and logistics that requires a dynamic solution approach. In this paper we present a new hybrid approach that combines the Quantum Approximate Optimization Algorithm (QAOA) into the QRL policy network, instead of the usual variational layers, QAOA mixing and cost Hamiltonian layers. This enhancement enables the agent to exploit problem specific particular quantum correlations when learning policies, and so richer exploration of the routing solution space. The QAOA-augmented QRL framework shows quicker convergence in training and can tackle larger VRP instances that are beyond the reach of Grover's Adaptive Search (GAS) and Quantum Reinforcement Learning (QRL) approaches. Experiments on standard VRP instances demonstrate better solutions, fewer episodes to converge and good memory usage on near term quantum hardware simulators. These findings demonstrate QAOA- integrated QRL as a viable approach to scalable, high quality quantum-assisted combinatorial optimization.

---


### 202. [Model Merging: Foundations and Algorithms](https://arxiv.org/abs/2605.01580)

**<font color=#1a73e8>作者：</font>** Donato Crisostomi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning usually treats models as separate artifacts: trained independently, specialized for particular purposes, and replaced when improved versions appear. This thesis studies model merging as an alternative paradigm: combining independently trained neural networks directly in weight space, with little or no optimization and without requiring access to the original training data.
The thesis considers two main regimes. In the single-task setting, where models share an objective but differ in initialization, we introduce C$^2$M$^3$, a cycle-consistent merging algorithm based on Frank-Wolfe optimization. C$^2$M$^3$ aligns multiple networks into a shared, reference-free parameter space, making weight averaging meaningful without privileging any individual model.
In the multi-task setting, where models are fine-tuned for different downstream tasks from a common pretrained initialization, we first develop a theoretical account of task vectors as approximate gradients. This explains both the effectiveness and the limitations of task arithmetic. Building on this view, we show that task vectors inherit the low-rank structure of gradients and introduce Task Singular Vectors (TSV), a decomposition that enables compression and interference reduction through TSV-Merge. We then present MASS, an input-adaptive routing method that uses TSV geometry to select task-relevant subspaces at inference time. Finally, we introduce MERGE$^3$, an evolutionary merging framework that uses Item Response Theory to reduce evaluation costs by up to 50$\times$ while preserving solution quality.
Together, these contributions provide theoretical and algorithmic foundations for model merging, supporting a paradigm in which learned capabilities can be composed, reused, and extended across models.

---


### 203. [Concepts Whisper While Syntax Shouts: Spectral Anti-Concentration and the Dual Geometry of Transformer Representations](https://arxiv.org/abs/2605.01609)

**<font color=#1a73e8>作者：</font>** Pratyush Acharya, Nuraj Rimal, Habish Dhakal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We test whether the causal inner product of \citet{park2024linear} -- defined by the unembedding covariance $\Sigma$ -- enables cross-lingual concept transport. Across 17 models and 4 language pairs, a matched-spectrum randomization test finds that Whitened Causal Alignment is indistinguishable from spectral regularization alone ($p = 0.95$). However, this failure reveals a broader phenomenon: anti-concentration is observed in residual-stream difference-of-means vectors across five architecture families ($p < 10^{-33}$) and supported by SAE features (e.g., $p = 4.5 \times 10^{-19}$) and linear probes on Gemma and Llama. We discover a \emph{dual geometry}: activation-space concept directions anti-concentrate in the spectral tail, while static unembedding-row contrasts \emph{concentrate} in high-variance directions ($p < 10^{-4}$). Split-injection causal interventions support the functional basis on Gemma and Llama (Cohen's $d$ up to $1.80$), and POS-tag probing across 8 models shows syntax preferentially encodes in the high-variance subspace in 6 of 8 architectures ($p < 0.013$), with the Qwen~2.5 family showing a significant reversal consistent with architecture-specific spectral structure. These results suggest transformers may rotate semantic content into spectrally quiet regions during contextualized processing, encoding concepts where they can be manipulated with reduced grammatical disruption.

---


### 204. [From Packets to Patterns: Interpreting Encrypted Network Traffic as Longitudinal Behavioral Signals](https://arxiv.org/abs/2605.01616)

**<font color=#1a73e8>作者：</font>** Rameen Mahmood, Omar El Shahawy, Souptik Barua 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human behavior is difficult to observe continuously at scale, yet it leaves measurable traces in everyday device use. We test whether encrypted smartphone network traffic -- a ubiquitous, always-on, passive sensing modality -- can passively capture behavioral patterns related to sleep, stress, and loneliness. We model shared behavioral structure using a transformer backbone with per-user adapters, allowing the model to represent both typical individual behavior and deviations from it. To make these representations interpretable, we apply a sparse autoencoder to extract behavioral features corresponding to distinct patterns of activity. We relate these features to sleep disturbance, stress, and loneliness using generalized estimating equations with Mundlak decomposition, separating between-person differences from within-person changes over time. We find that the three outcomes reflect distinct temporal structures: stress is primarily associated with stable between-person differences, loneliness with within-person variation, and sleep disturbance with a combination of both. Notably, these within-person dynamics are not captured by predefined network-traffic features, demonstrating the value of learned representations for longitudinal behavioral sensing. These results establish encrypted network traffic as a viable passive sensing modality, revealing interpretable behavioral dynamics -- particularly deviations from an individual's baseline -- that are not visible in raw traffic features.

---


### 205. [PRIME: Protein Representation via Physics-Informed Multiscale Equivariant Hierarchies](https://arxiv.org/abs/2605.01625)

**<font color=#1a73e8>作者：</font>** Viet Thanh Duy Nguyen, John K. Johnstone, Truong-Son Hy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proteins are inherently multiscale physical systems whose functional properties emerge from coordinated structural organization across multiple spatial resolutions, ranging from atomic interactions to global fold topology. However, existing protein representation learning methods typically operate at a single structural level or treat different sources of structural information as parallel modalities, without explicitly modeling their hierarchical relationships. We introduce PRIME (Protein Representation via Physics-Informed Multiscale Equivariant Hierarchies), a unified framework that models proteins as a nested family of five physically grounded structural graphs spanning surface, atomic, residue, secondary-structure, and protein levels. Adjacent levels are connected through deterministic, physics-informed assignment operators, enabling bidirectional information exchange via bottom-up aggregation and top-down contextual refinement. Experiments on standard protein representation learning benchmarks demonstrate strong and competitive performance across diverse tasks, with particularly notable gains on the Fold Classification benchmark, where PRIME outperforms the strongest geometric GNN baseline by margins of 13.80 and 18.30 points on the harder Superfamily and Fold splits, and achieves a state-of-the-art accuracy of 84.10% on Reaction Class prediction, surpassing all baseline methods, including ESM. Ablation studies confirm that each structural level contributes complementary and non-redundant information, and adaptive cross-attention analysis reveals that PRIME autonomously identifies the most task-relevant structural resolutions at prediction time. Our source code is publicly available at this https URL

---


### 206. [Perturb and Correct: Post-Hoc Ensembles using Affine Redundancy](https://arxiv.org/abs/2605.01632)

**<font color=#1a73e8>作者：</font>** Eleanor Quint  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models that are indistinguishable on in-distribution data can behave very differently under distribution shift. We introduce Perturb-and-Correct (P&C), a post-hoc method for constructing epistemically diverse predictors from a single pretrained network. P&C applies random hidden layer perturbations with a least-squares correction in the subsequent affine layer, producing predictors that agree on calibration data while remaining free to disagree away from it. We analyze this mechanism through the post-correction residual and its first-order sensitivity: the residual is controlled near the calibration distribution by a leverage term, while corrected sensitivity grows as inputs deviate from the calibration geometry. Empirically, P&C achieves a strong ID/OOD tradeoff across MuJoCo dynamics prediction and CIFAR-10 OOD detection, matching or outperforming standard post-hoc baselines while requiring only a single pretrained model. Our findings highlight the potential in further exploiting overparameterization as a strength of deep learning models.

---


### 207. [Chebyshev-Augmented One-Shot Transfer Learning for PINNs on Nonlinear Differential Equations](https://arxiv.org/abs/2605.01634)

**<font color=#1a73e8>作者：</font>** Yiqi Rao, Pavlos Protopapas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) offer a flexible paradigm for solving differential equations by embedding governing laws into the training objective. A persistent limitation is instance specificity: standard PINNs typically require retraining for each new forcing term, boundary/initial condition, or parameter setting. One-shot transfer learning (OTL) addresses this bottleneck for linear operators by freezing a pretrained latent representation and computing optimal output weights in closed form, but for nonlinear problems closed-form adaptation is generally unavailable because the loss is nonconvex in the output layer.
In this paper we substantially broaden the class of nonlinearities amenable to one-shot PINN transfer by combining OTL with Chebyshev polynomial surrogates. We approximate general smooth weakly nonlinear terms by truncated Chebyshev expansions over a prescribed solution range, yielding a polynomial nonlinearity that can be handled by a perturbative decomposition into linear subproblems. A multi-head PINN learns a reusable latent space associated with the dominant linear operator; at test time, solutions to new instances are obtained via a sequence of closed-form linear solves in the output layer, without retraining the network body.
We provide a unified derivation of the framework for ODEs and PDEs and demonstrate accuracy and fast online adaptation on nonlinear benchmarks, including non-polynomial and singular ODE nonlinearities as well as a reaction-diffusion PDE with saturating kinetics, demonstrating the method's utility in many-query regimes.

---


### 208. [The Banach-Butterfly Invariant: Influence-Adaptive Walsh Geometry for Ternary Polynomial Threshold Functions](https://arxiv.org/abs/2605.01637)

**<font color=#1a73e8>作者：</font>** Gorgi Pavlov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Banach-Butterfly Invariant (BBT), an influence-adaptive Banach geometry on the Walsh-Hadamard butterfly factorization. For a Boolean function $f:\{-1,+1\}^n\to\{-1,+1\}$ with coordinate influences $\mathrm{Inf}_\ell(f)$, BBT assigns exponent $p_\ell = 1+\mathrm{Inf}_\ell(f)$ to butterfly layer $\ell$, yielding the contraction invariant $\mu(f)=\prod_\ell 2^{-\mathrm{Inf}_\ell/(1+\mathrm{Inf}_\ell)}$. We prove a Jensen lower bound $\log_2\mu(f) \ge -I(f)/(1+I(f)/n)$ and that $\mu$ is strictly Schur-convex in the influence vector (modulo permutation), giving scaling classes $\mu\sim 2^{-n/2}$ (parity), $2^{-\Theta(\sqrt{n})}$ (majority), $2^{-1/2}$ (dictators). $\log_2\mu$ is rational but not polynomial in the Fourier coefficients while $\mu$ is algebraic, and $\mu$ separates functions with identical total influence (122 pairs at $n=3$).
Using the certified $n \le 4$ ternary Walsh-threshold universe from a companion synthesis manuscript as a finite testbed, we compute exact MILP minimum-support certificates for all 65,536 Boolean functions at $n=4$ (mean 6.42, max 9, all-odd by a parity argument) and on 10,000 of the 616,126 NPN-canonical representatives we enumerate at $n=5$ (matching OEIS A000370). Conditional Spearman $\rho(\mu,|\mathrm{supp}|)$ at fixed total influence is $+0.571$ in the largest stratum at $n=4$ but reverses to $-0.38$ at $n=5$ under both function-uniform and NPN-canonical sampling: $\mu$ is a valid Schur-convex concentration invariant, not a universal monotone predictor of minimum support across $n$.
A companion application paper validates a real-valued WHT activation-energy proxy inspired by this theory on five pretrained LLMs at W2A16, cutting wikitext-2 perplexity by 15-58% versus vanilla auto-round; the transfer from Boolean theory to the real-valued proxy is qualitative, not formal.

---


### 209. [Prescriptive Scaling Laws for Data Constrained Training](https://arxiv.org/abs/2605.01640)

**<font color=#1a73e8>作者：</font>** Justin Lovelace, Christian Belardi, Srivatsa Kundurthy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training compute is increasingly outpacing the availability of high-quality data. This shifts the central challenge from optimal compute allocation to extracting maximum value from limited data. The widely adopted Chinchilla scaling law assumes every training token is unique. This limits its ability to guide pretraining decisions in data-constrained regimes. We model the excess loss under repetition with a simple additive overfitting penalty and find that it accurately describes model behavior. Our scaling law yields qualitatively new compute-optimal allocation advice. Beyond a point, further repetition is counterproductive and compute is better spent on model capacity. We show that following our law's recommended configuration improves performance in data-constrained regimes. Finally, because our one-parameter form isolates overfitting in a single coefficient, it enables direct comparison across training configurations. As a case study, we show that strong weight decay ($\lambda=1.0$) reduces this coefficient by approximately 70%, providing a scaling-law explanation for recent findings that optimal weight decay in data-constrained regimes is an order of magnitude larger than standard practice.

---


### 210. [Toward a Principled Framework for Agent Safety Measurement](https://arxiv.org/abs/2605.01644)

**<font color=#1a73e8>作者：</font>** Shuyi Lin, Anshuman Suri, Alina Oprea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents emit actions, not just text, and once taken, those actions often cannot be undone. Yet today's agent-safety evaluations run greedy or a few sampled rollouts and report a single safe/unsafe rate -- blind to the long-tail trajectories where unsafe behavior may arise from low-probability but non-negligible actions.
We argue agent safety should be measured by search, not sampling. We apply BOA, a framework that, given a deployment configuration (model, decoder, prompt, environment, judger, likelihood budget), searches the in-budget trajectory space and reports a safety score: the probability the agent stays safe under the configuration. BOA searches both within a single LLM round and across the agent-environment interaction tree under a given likelihood budget, and makes search practical via batched decoding/judging, prefix caching, and chunked tree expansion. On agent-safety workloads, BOA discovers unsafe trajectories that greedy and sampled evaluations miss. BOA can additionally be used for ranking models, defenses, and attacks, all on the same scale, with manageable GPU costs.

---


### 211. [Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection](https://arxiv.org/abs/2605.01647)

**<font color=#1a73e8>作者：</font>** Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training-free AI text detection methods primarily rely on model log-probabilities, achieving strong performance through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions. We introduce an alternative detection signal based on character distribution signatures. We provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence. To enable systematic evaluation, we construct the Models-Domains-Temperatures-Adversarials (MDTA) benchmark comprising 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies, substantially expanding the HC3 dataset with modern model responses, temperature variation, and adversarial augmentation. We introduce the Letter Distribution Score (LD-Score), demonstrating low correlation (r = 0.08-0.13) with perplexity methods. When integrated with DNA-DetectLLM, Binoculars and FastDetectGPT via a non-linear classifier, LD-Score yields consistent improvements in AUROC and F1, with particularly pronounced gains in specialized domains where vocabulary constraints amplify the detection signal. The MDTA dataset can be accessed at: this https URL.

---


### 212. [Geospatial foundation-model embeddings improve population estimation unevenly across space and scale](https://arxiv.org/abs/2605.01650)

**<font color=#1a73e8>作者：</font>** Wenbin Zhang, Eimear Cleary, Francisco Rowe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable subnational population estimates are essential for applications, yet remain difficult where censuses are sparse, outdated or spatially coarse. Existing population-mapping workflows rely on hand-built geospatial covariates, such as settlement extent, night-time lights, and environmental conditions, which must be assembled and harmonised across scales and geographies. Geospatial foundation models offer an alternative by learning reusable representations of place from more multifaceted and heterogeneous data sources. Here, we benchmark Population Dynamics Foundation Model (PDFM) embeddings against the harmonised geospatial covariates for subnational population estimation in Brazil, Nigeria and the United States. Under geographically structured validation, PDFM increased predictive fit by a median of 20.1% (IQR: 10.0-33.2%, across country-model comparisons) reduction in unexplained variance, and reduced Kullback-Leibler divergence by 23.2% (9.2-26.2%). However, these gains were uneven. PDFM was most advantageous where the geospatial covariates weakly characterised settlement context, such as larger and less-developed subnational areas. Moreover, PDFM performance was scale-coupled with embeddings providing less flexible transfer across spatial aggregations than geospatial covariates. These findings showed that geospatial foundation-model representations of place can improve population estimation in data poor settings, but their benefits break down predictably under spatial scale mismatch, revealing a fundamental limitation of current geospatial AI.

---


### 213. [SteeringDiffusion: A Bottlenecked Activation Control Interface for Diffusion Models](https://arxiv.org/abs/2605.01653)

**<font color=#1a73e8>作者：</font>** Fangzheng Wu, Brian Summa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SteeringDiffusion, a bottlenecked activation-level control interface for diffusion models that exposes a smooth, monotonic, and runtime-adjustable control surface over the content--style trade-off. Our method keeps the U-Net backbone frozen and learns a small, prompt-conditioned latent code projected to FiLM/AdaGN-style modulation parameters. A zero-initialized design guarantees exact equivalence to the base model at zero scale, while timestep-aware gating restricts modulation to later denoising stages. A single scalar at inference continuously traverses the control surface without retraining. Across experiments on Stable Diffusion~1.5 and SDXL covering multiple artistic styles, we show that SteeringDiffusion produces smooth and monotonic content--style trade-offs. Under matched parameter budgets, it outperforms LoRA in controllability and stability, while ControlNet and rank-1 adapters do not expose a comparable control surface. We further introduce an inversion-stability diagnostic based on DDIM inversion, used as a post-hoc trajectory probe, which reveals strong correlations with intervention magnitude. These results position \emph{Steering Bottlenecked Explicit Control (S-BEC)} as a practical, general-purpose control interface for frozen diffusion backbones.

---


### 214. [Limit Properties at Critical Indices of Linear Canonical Riesz Potentials and Their Applications to Security of Multi-Image Encryption](https://arxiv.org/abs/2605.01654)

**<font color=#1a73e8>作者：</font>** Zunwei Fu, Dachun Yang, Shuhui Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this article we introduce the linear canonical Riesz potential (for short, LCRP) and give its symbol in terms of linear canonical transforms. Driven by image processing, we establish the convergence/divergence of these LCRPs for different kinds of functions. Concretely, for grating functions, we prove that their classical Riesz potentials diverge, whereas their LCRP converge due to the key role of chirp functions. For the characteristic function ${\mathbf 1}_P$ of a convex polygon $P$, we show that the limit of its Riesz potential at any non-boundary point $\boldsymbol{x}$ equals ${\mathbf 1}_P(\boldsymbol{x})$, but its limit at the boundaries differ from ${\mathbf 1}_P$, while it is known that, for any Schwartz function $f$, the limit of its Riesz potential at any point $\boldsymbol{x}$ always equals $f(\boldsymbol{x})$. Based on these and the inverse operator of the LCRP (namely the linear canonical Laplacian operator), we propose an asymmetric cascaded LCRP method for the multi-image encryption and create an efficient and secure cryptosystem. Systematic security evaluations, including sensitivity, statistical, noise attack, and occlusion attack analyses, demonstrate its robustness and its security. Even for a single image, the proposed method is more efficient than the known encryption approach based on the fractional Riesz potential. The novelty of these results lies in that the convergence and the divergence of LCRTs at the critical indices, respectively, for ``good" Schwartz functions and for ``bad" discrete image functions essentially affect the security of image encryption and decryption.

---


### 215. [TRIMMER: A New Paradigm for Video Summarization through Self-Supervised Reinforcement Learning](https://arxiv.org/abs/2605.01659)

**<font color=#1a73e8>作者：</font>** Pritam Mishra, Coloma Ballester, Dimosthenis Karatzas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of video content across domains such as surveillance, education, and social media has made efficient content understanding increasingly critical. Video summarization addresses this challenge by generating concise yet semantically meaningful representations, but existing approaches often rely on expensive manual annotations, struggle to generalize across domains, and incur significant computational costs due to complex architectures. Moreover, unsupervised and weakly supervised methods typically underperform compared to supervised counterparts in capturing long-range temporal dependencies and semantic structure. In this work, we propose TRIMMER (Temporal Relative Information Maximization for Multi-objective Efficient Reinforcement), a novel self-supervised reinforcement learning framework for video summarization. TRIMMER operates in two stages: it first learns robust representations via self-supervised learning and then performs spatio-temporal decision making through reinforcement learning guided by information-theoretic reward functions. Unlike prior approaches that rely on similarity-based objectives, our method introduces entropy-based metrics to capture higher-order temporal dynamics and semantic diversity, while computing rewards directly over selected frame indices to improve computational efficiency. Extensive experiments on standard benchmarks demonstrate that TRIMMER achieves state-of-the-art performance among unsupervised and self-supervised methods, while remaining competitive with leading supervised approaches, highlighting its effectiveness for scalable and generalizable video summarization.

---


### 216. [Towards Efficient and Expressive Offline RL via Flow-Anchored Noise-conditioned Q-Learning](https://arxiv.org/abs/2605.01663)

**<font color=#1a73e8>作者：</font>** Sungyoung Lee, Dohyeong Kim, Eshan Balachandar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Flow-Anchored Noise-conditioned Q-Learning (FAN), a highly efficient and high-performing offline reinforcement learning (RL) algorithm. Recent work has shown that expressive flow policies and distributional critics improve offline RL performance, but at a high computational cost. Specifically, flow policies require iterative sampling to produce a single action, and distributional critics require computation over multiple samples (e.g., quantiles) to estimate value. To address these inefficiencies while maintaining high performance, we introduce FAN. Our method employs a behavior regularization technique that utilizes only a single flow policy iteration and requires only a single Gaussian noise sample for distributional critics. Our theoretical analysis of convergence and performance bounds demonstrates that these simplifications not only improve efficiency but also lead to superior task performance. Experiments on robotic manipulation and locomotion tasks demonstrate that FAN achieves state-of-the-art performance while significantly reducing both training and inference runtimes. We release our code at this https URL.

---


### 217. [IMPACT-HOI: Supervisory Control for Onset-Anchored Partial HOI Event Construction](https://arxiv.org/abs/2605.01666)

**<font color=#1a73e8>作者：</font>** Haoshen Zhang, Di Wen, Kunyu Peng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present IMPACT-HOI, a mixed-initiative framework for annotating egocentric procedural video by constructing structured event graphs for Human-Object Interactions (HOI), motivated by the need for high-quality structured supervision for learning robot manipulation from human demonstration. IMPACT-HOI frames this task as the incremental resolution of a partially specified, onset-anchored event state. A trust-calibrated controller selects among direct queries, human-confirmed suggestions, and conservative completions based on empirical annotator behavior and evidence quality. A risk-bounded execution protocol, utilizing atomic rollback, ensures that human-confirmed decisions are preserved against conflicting automated updates. A user study with 9 participants shows a 13.5% reduction in manual annotation actions, a 46.67% event match rate, and zero confirmed-field violations under the studied protocol. The code will be made publicly available at this https URL.

---


### 218. [Deep neural networks with Fisher vector encoding for medical image classification](https://arxiv.org/abs/2605.01667)

**<font color=#1a73e8>作者：</font>** Lucas O. Lyra, Antonio E. Fabris, Joao B. Florindo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Orderless encoding methods have shown to improve Convolutional Neural Networks (CNNs) for image classification in the context of limited availability of data. Additionally, hybrid CNN + Vision Transformers (ViT) models have been recently proposed to address CNN locality bias issues. These models outperformed CNN-only approaches. Despite that, the integration of such hybrid models with more elaborated feature representation can be highly beneficial and remains large unexplored in the literature. In this context, we propose the introduction of an orderless encoding method, Fisher Vectors, to hybrid CNN + ViT architectures, aiming at achieving a model suitable for both small and large datasets. Such enconding method relies on estimating a Gaussian Mixture Model (GMM) on image features. In large datasets, computational costs of the GMM estimation is a limiting factor for the application of Fisher Vectors. Thus, we propose a method to limit the growth of GMM estimation costs as we increase the size of the dataset. We explore the feasibility of our method in the context of medical image classification by appling it to MedMNIST (v2), Clean-CC-CCII and ISIC2018. This collection of datasets contains a wide variety of data scales and modalities. We outperform benchmark results in all MedMNIST (v2) datasets and obtain literature-competitive results in Clean-CC-CCII and ISIC2018.

---


### 219. [IMPACT-Scribe: Interactive Temporal Action Segmentation with Boundary Scribbles and Query Planning](https://arxiv.org/abs/2605.01668)

**<font color=#1a73e8>作者：</font>** Qian Yin, Di Wen, Kunyu Peng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense temporal annotation of procedural activity videos is vital for action understanding and embodied intelligence but remains labor-intensive due to reactive tools. Each correction is treated as an isolated edit, limiting reuse of information on annotator uncertainty and model reliability. We introduce IMPACT-Scribe, a correction-driven framework for dense labeling that uses each correction to improve future human-machine collaboration. IMPACT-Scribe combines uncertainty-aware boundary scribble supervision, local proposal modeling, cost-aware query planning, structured propagation, and correction-driven adaptation. Experiments and a human study show that this closed-loop design improves labeling quality per effort, enhances boundary accuracy, and fosters better human-machine interaction over time. The code will be made publicly available at this https URL.

---


### 220. [CP-SynC: Multi-Agent Zero-Shot Constraint Modeling in MiniZinc with Synthesized Checkers](https://arxiv.org/abs/2605.01675)

**<font color=#1a73e8>作者：</font>** Yuliang Song, Eldan Cohen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint Programming (CP) is a powerful paradigm for solving combinatorial problems, yet translating natural language problem descriptions into executable models remains a significant bottleneck. While Large Language Models (LLMs) show promise in automating this translation, they often struggle with subtle semantic errors in the absence of oracle validation at test time. To address this, we introduce CP-SynC (Constraint Programming modeling with Synthesized Checkers), a multi-agent workflow for zero-shot constraint modeling in MiniZinc. CP-SynC coordinates modeling agents that generate and refine candidate models and validation agents that synthesize semantic checkers to provide feedback on semantic correctness. To mitigate noise inherent in individual LLM outputs, CP-SynC explores multiple modeling trajectories in parallel and employs selection agents to select the final model via multi-agent evidence aggregation. Extensive experiments on a benchmark of 100 CP problems show that CP-SynC substantially outperforms existing baselines in MiniZinc modeling.

---


### 221. [Class-Aware Adaptive Differential Privacy in Deep Learning for Sensor-Based Fall Detection](https://arxiv.org/abs/2605.01679)

**<font color=#1a73e8>作者：</font>** Joydeb Kumar Sana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fall detection is a critical task in healthcare, particularly for elderly people. Timely fall detection and treatment can prevent severe injuries. Sensor-based activity data can be used to detect fall. However, this data are highly sensitive and raises significant privacy concerns. Existing privacy approaches apply uniform noise across all training samples, which affects the prediction performance. To address this limitation, we propose a Class-Aware Adaptive Differential Privacy (CA-ADP) framework integrated with a hybrid 3D Convolutional Neural Network and Bidirectional Long Short-Term Memory (3D CNN-BiLSTM) architecture. The CA-ADP mechanism dynamically adjusts the magnitude of noise added to gradients based on the class composition of each mini-batch. This process ensures privacy while mitigates performance degradation. We formally analyze the $(\epsilon,\delta)$-Differential Privacy guarantee and provide a privacy-utility trade-off analysis. The proposed method is evaluated on three public benchmark datasets, namely SisFall, UP-Fall, and MobiAct. The experimental results show that the proposed privacy model achieves improvements of 3.3\%, 8.5\%, and 7.5\% over the conventional privacy-based model in terms of F-score for the SisFall, UP-Fall, and MobiAct datasets, respectively. Comparisons with prior studies show that the CA-AD based framework achieves competitive performance and provides formal privacy guarantees, which are largely overlooked in existing studies. Wilcoxon signed-rank tests confirm that the proposed mechanism consistently outperforms conventional differential privacy. Those results establish the proposed CA-ADP framework as an effective approach to privacy-preserving fall detection in real-world healthcare settings.

---


### 222. [Benchmarking Single-Pose Docking, Consensus Rescoring, and Supervised ML on the LIT-PCBA Library: A Critical Evaluation of DiffDock, AutoDock-GPU, GNINA, and DiffDock-NMDN](https://arxiv.org/abs/2605.01681)

**<font color=#1a73e8>作者：</font>** Youssef Abo-Dahab, Xiaoiang Xiang, Xiaoiang Xiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual screening performance depends heavily on the chosen docking and scoring methods. Recent AI-based tools such as DiffDock and NMDN have reported strong benchmark results, but their practical utility on realistic, experimentally-derived datasets remains unclear. Here we perform a large-scale evaluation on the LIT-PCBA library (15 targets, 578,295 ligand-target pairs with experimentally confirmed actives and inactives). We compare AutoDock-GPU and DiffDock for pose generation, followed by rescoring with GNINA and NMDN. We further evaluate rank-based consensus strategies and supervised machine learning models trained on docking features.
GNINA rescoring of AutoDock-GPU poses (AutoDock-GNINA) emerged as the strongest single method with a median EF1% of 2.14. DiffDock-based approaches underperformed relative to AutoDock-GNINA, particularly on challenging targets such as OPRK1. Carefully designed consensus ranking improved robustness but did not surpass the best single scorer. Supervised ML re-ranking delivered the largest gains, achieving a median EF1% of 4.49 (+110% over AutoDock-GNINA).
Our results highlight that even the best classical+ML hybrid workflows provide only modest early enrichment on realistic benchmarks. We conclude that no single docking method dominates across targets and that rigorously validated, cost-effective combinations with supervised re-ranking currently offer the most practical value for virtual screening.

---


### 223. [GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory](https://arxiv.org/abs/2605.01688)

**<font color=#1a73e8>作者：</font>** Yushi Sun, Bowen Cao, Dong Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms. However, retrieved fragments are typically fed to the language model as unstructured text, lacking the relational, temporal, and thematic structures essential for complex reasoning. To bridge this reasoning gap, we introduce GRAVITY (\textbf{G}eneration-time \textbf{R}elational \textbf{A}nchoring \textbf{V}ia \textbf{I}njected \textbf{T}opological Memor\textbf{Y}), a plug-and-play structured memory module. GRAVITY extracts three complementary knowledge representations from raw conversational utterances: entity profiles grounded in relational graphs, temporal event tuples linked into causal traces, and cross-session topic summaries. At generation time, it injects these representations into the host system's prompt as structured anchoring contexts. This approach effectively synthesizes scattered evidence into a coherent, query-relevant context without requiring any architectural modifications to the host model. Extensive evaluations across five diverse memory systems on the LongMemEval and LoCoMo benchmarks demonstrate the efficacy of our approach. On average, GRAVITY improves LLM-judge accuracy by 7.5--10.1%. Gains are inversely correlated with baseline strength: the weakest host improves by 12.2% while the strongest still gains 3.8--5.7%. These findings establish structured context anchoring as a broadly effective, architecture-agnostic augmentation paradigm for long-horizon conversational memory.

---


### 224. [Complex Diffusion Maps with $ω$-Parameterized Kernels Revealing Inherent Harmonic Representations](https://arxiv.org/abs/2605.01691)

**<font color=#1a73e8>作者：</font>** Tongzhen Dang, Weiyang Ding, Michael K. Ng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose Complex Diffusion Maps (CDM), a novel diffusion mapping framework that aims to reveal the dominant complex harmonics of high-dimensional data. Inspired by the local Gaussian kernel relevant to the heat equation and the nonlocal Schrödinger kernel relevant to the Schrödinger equation, we propose a unified family of $\omega$-parameterized complex-valued kernels for the trade-off between local and nonlocal connections. We establish the theoretical foundation based on the operator spectrum theory, where the corresponding diffusion operator, diffusion distance, and complex harmonic maps are well-defined. An optimization-based interpretation of the maps is also developed, aiming to preserve angular structure in the complex diffusion space rather than relying solely on real-valued magnitude. We extensively evaluate CDM on both synthetic and real-world datasets. The complex-valued kernel amplifies differences among easily confusable samples, improving discriminative power over both linear and nonlinear methods based on real-valued kernels. CDM remains robust in high-noise settings, yielding a clearer eigengap that enhances spectral separation. For resting-state fMRI data, CDM captures more strongly correlated and nonlocal spatiotemporal dynamics. Without task-specific tuning, CDM achieves competitive performance on a public EEG sleep dataset, while maintaining high computational efficiency compared with both traditional machine learning and deep neural network approaches, highlighting its generality and practical value.

---


### 225. [Stability and Generalization for Decentralized Markov SGD](https://arxiv.org/abs/2605.01701)

**<font color=#1a73e8>作者：</font>** Jiahuan Wang, Ziqing Wen, Ping Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient methods are central to large-scale learning, yet their generalization theory typically relies on independent sampling assumptions. In many practical applications, data are generated by Markov chains and learning is performed in a decentralized manner, which introduces significant analytical challenges. In this work, we investigate the stability and generalization of decentralized stochastic gradient descent (SGD) and stochastic gradient descent ascent (SGDA) under Markov chain sampling. Leveraging a stability-based framework, we characterize how Markovian dependence and decentralized communication jointly influence generalization behavior. Our analysis captures the effects of network topology, Markov chain mixing properties, and primal-dual dynamics. We establish non-asymptotic generalization bounds for both algorithms, extending existing results on Markov stochastic gradient methods to decentralized and minimax settings.

---


### 226. [Floating-Point Networks with Automatic Differentiation Can Represent Almost All Floating-Point Functions and Their Gradients](https://arxiv.org/abs/2605.01702)

**<font color=#1a73e8>作者：</font>** Sejun Park, Yeachan Park, Geonho Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Theoretical studies show that for any differentiable function on a compact domain, there exists a neural network that approximates both the function values and gradients. However, such a result cannot be used in practice since it assumes real parameters and exact internal operations. In contrast, real implementations only use a finite subset of reals and machine operations with round-off errors. In this work, we investigate whether a similar result holds for neural networks under floating-point arithmetic, when the gradient with respect to the input is computed by the automatic differentiation algorithm $D^\mathtt{AD}$. We first show that given a floating-point function $\phi$ (e.g., a loss function), arbitrary function values and gradients can be represented by a floating-point network $f$ and $D^\mathtt{AD}(\phi\circ f)$, respectively. We further extend this result: given $\phi_1,\dots,\phi_n$, $D^\mathtt{AD}(\phi_i\circ f)$ can simultaneously represent arbitrary gradients while $f$ represents the target values, under mild conditions. Our results hold for practical activation functions, e.g., $\mathrm{ReLU}$, $\mathrm{ELU}$, $\mathrm{GeLU}$, $\mathrm{Swish}$, $\mathrm{Sigmoid}$, and $\mathrm{tanh}$.

---


### 227. [Exploring Entropy-based Active Learning for Fair Brain Segmentation](https://arxiv.org/abs/2605.01706)

**<font color=#1a73e8>作者：</font>** Ghazal Danaee, Mélanie Gaillochet, Christian Desrosiers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active learning (AL) has emerged as a crucial strategy for reducing the prohibitive costs associated with medical image segmentation. However, standard uncertainty-based AL methods typically focus on maximizing performance metrics, ignoring performance disparities or fairness across groups with sensitive attributes. While fair active learning has been explored in classification tasks, its intersection with medical image segmentation remains unaddressed. In this work, we introduced a fairness-aware active learning framework with a Weighted Entropy selection strategy that modulates uncertainty based on current group-specific performance estimates on the labeled set. To decouple true epistemic uncertainty from anatomical volume variances, we further utilized a masked, scaled entropy restricted to the region of interest. The framework was evaluated on synthetic T1-weighted brain MRIs with controlled left caudate bias in both strong and weak bias settings. A 3D U-Net was trained to segment the left caudate under several AL strategies, starting from both demographically balanced and strongly imbalanced initial labeled sets. Experiments demonstrated that our method markedly reduces performance disparities between groups compared to random sampling and standard uncertainty sampling. By prioritizing poorly segmented subgroups during the AL cycles, our method consistently achieved the highest equity-scaled performance and reduced the disparity metric by 75% (strong bias) and 86% (weak bias) relative to standard entropy at the final budget. Overall, this work is among the first studies on fair AL for medical image segmentation, offering an efficient strategy to train more equitable models in resource-constrained environments.

---


### 228. [Model Routing as a Trust Problem: Route Receipts for Adaptive AI Systems](https://arxiv.org/abs/2605.01710)

**<font color=#1a73e8>作者：</font>** Vincent Schmalbach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI products often route requests through version aliases, service tiers, tool choices, regional endpoints, fallback rules, or safety handling before responding. These routing steps are documented product surfaces in several widely used AI platforms and serving stacks.
Routing helps AI services stay affordable, fast, and available at scale, and it shapes trust. Trust can break when routing changes the cost, quality, or accountability of a response without the user being able to tell what happened. "Which model answered?" is only part of the audit question. The runtime path matters.
Adaptive AI systems should produce a runtime transparency artifact called the route receipt. A route receipt is a compact record of the route that served a request. It should capture enough material facts for people relying on the output to reconstruct important routing decisions without exposing proprietary internals or hidden reasoning.
Route transparency should be part of model documentation. Model cards describe trained model artifacts, while route receipts describe the runtime conditions under which a particular answer was produced. The paper introduces the route-receipt concept, a minimal schema and redaction model, and a documentation-based survey of selected platforms showing that receipt fragments already exist without a portable per-answer record.

---


### 229. [Linear-Time Global Visual Modeling without Explicit Attention](https://arxiv.org/abs/2605.01711)

**<font color=#1a73e8>作者：</font>** Ruize He, Dongchen Han, Gao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing research largely attributes the global sequence modeling capability of Transformers to the explicit computation of attention weights, a process that inherently incurs quadratic computational complexity. In this work, we offer a novel perspective: we demonstrate that attention can be mathematically reframed as a Multi-Layer Perceptron (MLP) equipped with dynamically predicted parameters. Through this lens, we explain attention's global modeling power not as explicit token-wise aggregation, but as an implicit process where dynamically generated parameters act as a compressed representation of the global context. Inspired by this insight, we investigate a fundamental question: can we achieve Transformer-level sequence global modeling entirely through dynamic parameterization while maintaining linear complexity, effectively replacing explicit attention? To explore this, we design various dynamic parameter prediction strategies and integrate them into standard network layers. Extensive empirical studies on vision models demonstrate that dynamic parameterization can indeed serve as a highly effective, linear-complexity alternative to explicit attention, opening new pathways for efficient sequence modeling. Code is available at this https URL.

---


### 230. [CoAction: Cross-task Correlation-aware Pareto Set Learning](https://arxiv.org/abs/2605.01712)

**<font color=#1a73e8>作者：</font>** Xinyue Chen, Yingxuan Liang, Yiqin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pareto set learning (PSL) is an emerging paradigm in multi-objective optimization that trains neural networks to map preference vectors to Pareto optimal solutions. However, existing PSL methods primarily focus on solving a single multi-objective optimization problem at a time. This limitation not only increases computational costs in multi-objective multitask optimization scenarios by requiring a separate model for each task, but also fails to exploit the inter-task correlations across tasks. To address this, we propose a Cross-tAsk correlation-aware Pareto Set Learning (CoAction) framework, which leverages task-aware transformer to handle multiple tasks simultaneously. Specifically, by assigning task-specific embedding vectors to individual tasks, the model effectively distinguishes between tasks while facilitating knowledge sharing among them. We utilize a Transformer encoder as the backbone architecture to leverage its self-attention mechanism for capturing complex task dependencies. The proposed approach is evaluated on comprehensive multitask test suites covering both benchmark problems and real-world applications, demonstrating effectiveness and competitive performance in Hypervolume, Range, and Sparsity.

---


### 231. [TCDA: Thread-Constrained Discourse-Aware Modeling for Conversational Sentiment Quadruple Analysis](https://arxiv.org/abs/2605.01717)

**<font color=#1a73e8>作者：</font>** Xinran Li, Xinze Che, Yifan Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational Aspect-based Sentiment Quadruple Analysis (DiaASQ) needs to capture the complex interrelationships in multiple rounds of dialogues. Existing methods usually employ simple Graph Convolutional Networks (GCN), which introduce structural noise and fail to consider the temporal sequence of the dialogues, or use standard RoPE, which implicitly captures relative distances in a flat sequence but cannot clearly separate the token-level syntactic order from the utterance-level progression, and may suffer from the Distance Dilution problem. To address these issues, we propose a new framework that combines Thread-Constrained Directed Acyclic Graph (TC-DAG) and Discourse-Aware Rotary Position Embedding (D-RoPE). Specifically, TC-DAG filters out cross-thread noise based on thread constraints, maintains global connectivity through root anchoring, and incorporates the temporal sequence of the dialogues. D-RoPE aligns multi-layer semantics using dual-stream projection and multi-scale frequency signals, captures thread dependencies using tree-like distances, and alleviates the token-level Distance Dilution problem by incorporating utterance-level progressions. Experimental results on two benchmark datasets demonstrate that our framework achieves state-of-the-art performance.

---


### 232. [Dual-branch Robust Unlearnable Examples](https://arxiv.org/abs/2605.01718)

**<font color=#1a73e8>作者：</font>** Xianlong Wang, Hangtao Zhang, Wenbo Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlearnable examples (UEs) aim to compromise model training by injecting imperceptible perturbations to clean samples. However, existing UE schemes exhibit limited robustness against advanced defenses due to their heuristic design or narrowly scoped domain perturbations. To address this, we propose \texttt{DUNE}, a \underline{\textbf{D}}ual-branch \underline{\textbf{UN}}learnable \underline{\textbf{E}}nsemble perturbation optimization approach. Specifically, \texttt{DUNE} separately optimizes perturbations in the spatial and color domains to establish the mapping between perturbations and shift-induced labels. This design extends the perturbation domain to increase noise intensity for improving robustness and drives the models to learn perturbation-oriented features with degraded generalization, thereby achieving unlearnability. To strengthen \texttt{DUNE}'s performance, we further propose an unlearnability-enhancing ensemble strategy that aggregates diverse pre-trained models during the dual-branch optimization. Extensive experiments on benchmark datasets CIFAR-10 and ImageNet verify that \texttt{DUNE}'s robustness outperforms 12 SOTA UE schemes under 7 mainstream defenses, yielding a lower average test accuracy of 14.95\% to 50.82\%.

---


### 233. [SignVerse-2M: A Two-Million-Clip Pose-Native Universe of 25+ Sign Languages](https://arxiv.org/abs/2605.01720)

**<font color=#1a73e8>作者：</font>** Sen Fang, Hongbin Zhong, Yanxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing large-scale sign language resources typically provide supervision only at the level of raw video-text alignment and are often produced in laboratory settings. While such resources are important for semantic understanding, they do not directly provide a unified interface for open-world recognition and translation, or for modern pose-driven sign language video generation frameworks: 1. RGB-based pretrained recognition models depend heavily on fixed backgrounds or clothing conditions during recording, and are less robust in open-world settings than style-agnostic pose-processing models. 2. Recent pose-guided image/video generation models mostly use a unified keypoint representation such as DWPose as their control interface. At present, the sign language field still lacks a data resource that can directly interface with this modern pose-native paradigm while also targeting real-world open scenarios. We present SignVerse-2M, a large-scale multilingual pose-native dataset for sign language pose modeling and evaluation. Built from publicly available multilingual sign language video resources, it applies DWPose in a unified preprocessing pipeline to convert raw videos into 2D pose sequences that can be used directly for modeling, resulting in a consolidated corpus of about two million clips covering more than 25 sign languages. Unlike many laboratory datasets, this resource preserves the recording conditions and speaker diversity of real-world videos while reducing appearance variation through a unified pose representation. Toward this goal, we further provide the data construction pipeline, task definitions, and a simple SignDW Transformer baseline, demonstrating the feasibility of this resource for multilingual pose-space modeling and its compatibility with modern pose-driven pipelines, while discussing the evaluation claims it can support as well as its current limitations.

---


### 234. [Automated Channel Fault Analysis with Tofu](https://arxiv.org/abs/2605.01721)

**<font color=#1a73e8>作者：</font>** Jacob Ginesin, Max von Hippel, Cristina Nita-Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed protocols are the linchpin of the modern internet, underpinning every internet service. This has in turn motivated a massive body of research ensuring the security, reliability, and performance of distributed protocols. In these works, a wide-ranging assumption is that distributed protocols operate over faulty or attacker-controlled channels, where messages can be arbitrarily inserted, dropped, replayed, or reordered. Formal verification work targeting distributed protocols typically defines its own notion of faulty or malicious channels, then constructively proves their protocol is correct with respect to it. In this work we take a fundamentally different approach: we develop a rigorous methodology for automatically conducting channel fault analysis on distributed protocols, and we introduce Tofu, a generalizable tool that implements our methodology. Tofu provides sound, complete analysis, synthesizing channel fault-based attack traces on arbitrary linear temporal logic (LTL) protocol specifications or proving the absence of such through an exhaustive state-space search. We demonstrate the applicability of Tofu by employing it to study TCP.

---


### 235. [Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2605.01725)

**<font color=#1a73e8>作者：</font>** Jing Xu, Yuexiao Ma, Songwei Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation paradigms offer theoretical promise for long video synthesis, yet their practical deployment is hindered by the computational burden of sequential iterative denoising. While cache reuse strategies can accelerate generation by skipping redundant denoising steps, existing methods rely on coarse-grained chunk-level skipping that fails to capture fine-grained pixel dynamics. This oversight is critical: pixels with high motion require more denoising steps to prevent error accumulation, while static pixels tolerate aggressive skipping. We formalize this insight theoretically by linking cache errors to residual instability, and propose MotionCache, a motion-aware cache framework that exploits inter-frame differences as a lightweight proxy for pixel-level motion characteristics. MotionCache employs a coarse-to-fine strategy: an initial warm-up phase establishes semantic coherence, followed by motion-weighted cache reuse that dynamically adjusts update frequencies per token. Extensive experiments on state-of-the-art models like SkyReels-V2 and MAGI-1 demonstrate that MotionCache achieves significant speedups of $\textbf{6.28}\times$ and $\textbf{1.64}\times$ respectively, while effectively preserving generation quality (VBench: $1\%\downarrow$ and $0.01\%\downarrow$ respectively). The code is available at this https URL.

---


### 236. [Stable GFlowNets with Probabilistic Guarantees](https://arxiv.org/abs/2605.01729)

**<font color=#1a73e8>作者：</font>** Zengxiang Lei, Ananth Shreekumar, Jonathan Rosenthal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) learn to sample states proportional to an unnormalized reward. Despite their theoretical promise, practical training is often unstable, exhibiting severe loss spikes and mode collapse. To tackle this, we first assess the sensitivity of GFlowNet objectives, demonstrating that a small Total Variation (TV) distance between the learned and target distributions does not preclude unbounded training loss. Motivated by this mismatch, we establish converse guarantees by deriving loss-to-TV bounds that certify global fidelity from bounded trajectory balance losses. Lastly, we propose Stable GFlowNets, an algorithm that leverages our theoretical results to stabilize training, and empirically demonstrate improved training behavior and superior distributional fidelity.

---


### 237. [Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736)

**<font color=#1a73e8>作者：</font>** Sixian Zhang, Yiyao Wang, Xinhang Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the geometric and semantic structure of environments is essential for embodied navigation and reasoning. Existing semantic mapping methods trade off between explicit geometry and multi-scale semantics, and lack a native interface for large models, thus requiring additional training of feature projection for semantic alignment. To this end, we propose the multi-scale Gaussian-Language Map (GLMap), which introduces three key designs: (1) explicit geometry, (2) multi-scale semantics covering both instance and region concepts, and (3) a dual-modality interface where each semantic unit jointly stores a natural language description and a 3D Gaussian representation. The 3D Gaussians enable compact storage and fast rendering of task-relevant images via Gaussian splatting. To enable efficient incremental construction, we further propose a Gaussian Estimator that analytically derives Gaussian parameters from dense point clouds without gradient-based optimization. Experiments on ObjectNav, InstNav, and SQA tasks show that GLMap effectively enhances target navigation and contextual reasoning, while remaining compatible with large-model-based methods in a zero-shot manner. The code is available at this https URL.

---


### 238. [Adaptive Texture-aware Masking for Self-Supervised Learning in 3D Dental CBCT Analysis](https://arxiv.org/abs/2605.01741)

**<font color=#1a73e8>作者：</font>** Xinquan Yang, Jianfeng Ren, Xuguang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone Beam Computed Tomography (CBCT) is pivotal for 3D diagnostic imaging in dentistry. However, the development of robust AI models for volumetric analysis is often constrained by the scarcity of large, annotated datasets. Self-supervised learning (SSL), particularly Masked Image Modeling (MIM), offers a promising pathway to leverage unlabeled data. A limitation of standard MIM is its reliance on random masking, which fails to prioritize diagnostically critical regions in dental CBCT volumes, such as subtle pathological changes and intricate anatomical boundaries. To address this, we propose ATMask, a novel adaptive masking strategy. Instead of applying random masks or employing computationally intensive attention modules, ATMask computes an inter-slice texture variation map to identify regions with high structural or textural complexity. These high-variation areas are then selectively masked during pre-training, compelling the model to learn richer contextual representations essential for inferring complex 3D morphological transitions. Furthermore, we contribute the first large-scale CBCT dataset, curated from both public and private sources, comprising 6,314 scans, for the dental AI model pretraining. Extensive experiments on three downstream dental CBCT tasks demonstrate that our ATMask enables more data-efficient and powerful representation learning than standard random masking and other advanced SSL baselines. The dataset and code will be released.

---


### 239. [Joint Architecture-Token-Bitwidth Multi-Axis Optimization of Vision Transformers for Semiconductor IC Packaging](https://arxiv.org/abs/2605.01742)

**<font color=#1a73e8>作者：</font>** Phat Nguyen, Xue Geng, Kaixin Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have achieved strong performance in visual recognition, yet their deployment in resource-constrained industrial environments remains limited. Some main challenges are their high computational cost, memory requirement, and energy consumption. While individual efficiency techniques such as neural architecture search (NAS), token compression, and low-precision inference have been extensively studied, most prior work targets only a single optimization axis, limiting overall deployment gains while preserving accuracy. In this paper, we present one of the first holistic frameworks that jointly optimizes three complementary axes: architecture, token, and bit-width. Specifically, the framework identifies compact backbones via Neural Architecture Search (AutoFormer), reduces information processing via token merging (ToMe), and accelerates per-operation execution via fp16 mixed-precision inference. Starting from a DeiT-B/16 baseline, we first analyze accuracy-efficiency trade-offs on ImageNet-1K under aggressive compression. Then, we apply the selected configurations to a real-world in-house 3D X-ray semiconductor defect classification dataset for IC chip packaging inspection. Results show that the proposed multi-axis framework achieves more than 10 times improvement in throughput along with over 10 times reductions in parameter count, FLOPs, and energy consumption, while maintaining the required accuracy on the downstream industrial task. To the best of our knowledge, this is among the earliest works to jointly optimize architecture, token, and bit-width dimensions in ViTs and the first such resource-efficient, deployment-focused study tailored to semiconductor manufacturing.

---


### 240. [MOC-3D: Manifold-Order Consistency for Text-to-3D Generation](https://arxiv.org/abs/2605.01743)

**<font color=#1a73e8>作者：</font>** Chenyang Fan, Junshi Cheng, Wen Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the burgeoning development of fields such as the Metaverse, Virtual Reality (VR), and Digital Twins, text-to-3D generation has emerged as a research hotspot in both academia and industry. Currently, optimization methods based on Score Distillation Sampling (SDS) utilizing 2D diffusion priors have become the mainstream technological paradigm in this field. However, due to the view bias of 2D priors and the mode-seeking ambiguity combined with gradient noise induced by high Classifier-Free Guidance (CFG), these methods still suffer from macro-topological inconsistency (e.g., the Janus problem) and micro-geometric discontinuity.
To address these challenges, we propose MOC-3D, a text-to-3D generation method based on geometric manifold and semantic view-order consistency. Built upon the ScaleDreamer framework, our method incorporates a Semantic View-Order Constraint Module and a Manifold-based Feature Continuity Module. The former aims to rectify macro-topological inconsistency, while the latter focuses on eliminating micro-geometric discontinuity. Specifically, the Semantic View-Order Constraint Module leverages the prior knowledge of CLIP to impose a Monotonicity Rank Constraint on semantic score representations across different views, thereby providing effective guidance for the global topological structure of 3D objects. Meanwhile, the Manifold-based Feature Continuity Module employs the Riemannian Metric on the Symmetric Positive Definite (SPD) manifold. By measuring the distance of feature statistical distributions in the Riemannian space, it promotes the smooth evolution and continuity of micro-textures across multi-views in a statistical sense. Under the macro-micro synergistic optimization of these two modules, our model can simultaneously improve macro-structural consistency and micro-detail continuity.

---


### 241. [NH-CROP: Robust Pricing for Governed Language Data Assets under Cost Uncertainty](https://arxiv.org/abs/2605.01745)

**<font color=#1a73e8>作者：</font>** Xu Zheng, Feiyu Wu, Zhuocheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language data are increasingly acquired and governed as assets, yet platforms often price candidate resources before knowing their true privacy or access costs. We study online pricing for governed language data assets under cost uncertainty. At each round, a platform observes an NLP task, a candidate asset, and a coarse cost estimate, may pay for a refined cost signal, posts a price, and receives safe net revenue.
We introduce \textsc{NH-CROP}, a clipped robust pricing framework with a no-harm information-acquisition gate. The method compares direct pricing, risk-aware pricing, and verify-then-price, and acquires information only when its estimated decision value exceeds the best no-verification alternative. Across synthetic, real-proxy, and downstream-utility-grounded benchmarks, clipped \textsc{NH-CROP} variants improve or remain competitive with price-only and risk-aware baselines. Causal ablations show that paid verification is not the main source of gains in real-proxy and utility-grounded settings: the strongest learned policies often choose not to verify. Oracle and high-decision-value diagnostics show that refined cost information can still have substantial local value. Overall, governed language-data platforms should calibrate pricing under uncertain access costs first and verify only when information is cheap and decision-actionable.

---


### 242. [Profile-Specific 3DMM Regression from a Single Lateral Face Image](https://arxiv.org/abs/2605.01746)

**<font color=#1a73e8>作者：</font>** Taiki Kanaya, Hideo Saito  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D face reconstruction is a core problem in computer vision, with important clinical applications such as cephalometric landmark analysis in orthodontics. Traditionally, this analysis relies on lateral X-ray imaging; however, frequent X-ray exposure is impractical due to radiation concerns. While recent research has explored detecting landmarks from lateral RGB images as an alternative, existing methods typically rely on 2D features such as the eyes, mouth, ears, and boundary silhouettes, failing to fully exploit the underlying 3D facial geometry spanning the facial profile and jawline, which is essential for accurate diagnosis. Meanwhile, although 3D face reconstruction from frontal views has seen significant progress, most learning-based 3D morphable model (3DMM) regressors are developed and benchmarked on near-frontal images, where appearance cues are abundant. In extreme profile views (yaw $\approx 90^\circ$), much of the face is occluded, and the available signal is dominated by boundary cues, making accurate 3D reconstruction challenging. In this paper, we bridge this gap with geometry-conditioned synthetic data and a simple profile-specific FLAME regression baseline for single lateral images. We introduce ProfileSynth, a dataset created by sampling FLAME shape and pose parameters in extreme yaw ranges and generating photorealistic profile images using a diffusion model conditioned on depth and normal maps. We further study a profile-specific baseline with visibility-aware jawline regularization. Our framework provides a practical baseline for "profile $\times$ 3DMM" reconstruction and a promising foundation for more accurate, non-invasive cephalometric analysis from lateral RGB images.

---


### 243. [Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality](https://arxiv.org/abs/2605.01749)

**<font color=#1a73e8>作者：</font>** Wen Luo, Guangyue Peng, Liang Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models achieve strong performance on complex tasks but remain prone to hallucinations, particularly in long-form generation where errors compound across reasoning steps. Existing approaches to improving factuality, including abstention and factuality-driven optimization, follow a \emph{coupled exploration-commitment} paradigm, in which intermediate reasoning is unconditionally propagated to the final output, limiting fine-grained control over information selection and integration. In this paper, we propose an \textbf{Exploration-Commitment Decoupling} paradigm that disentangles knowledge exploration from final commitment, enabling models to explore with awareness while answering cautiously. We instantiate the paradigm with \textbf{Calibration-Aware Generation (CAG)}, a framework that equips models with end-to-end, calibration-aware generation capabilities, by augmenting intermediate reasoning with calibrated reliability estimates and prioritizing reliable content in final outputs. Across five long-form factuality benchmarks and multiple model families, CAG improves factuality by up to 13%, while reducing decoding time by up to 37%. Overall, our work highlights decoupling as a principled approach for more reliable long-form generation, offering directions for trustworthy and self-aware generative systems.

---


### 244. [Talk is Cheap, Communication is Hard: Dynamic Grounding Failures and Repair in Multi-Agent Negotiation](https://arxiv.org/abs/2605.01750)

**<font color=#1a73e8>作者：</font>** Yiheng Yao, Chelsea Zou, Robert D. Hawkins  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Grounding is the collaborative process of establishing mutual belief sufficient for the current communicative purpose. While static grounding maps language to a shared, externally observable context, dynamic grounding is a joint activity where meaning is negotiated through interaction. Current multi-agent Large Language Model (LLM) benchmarks focus on static, one-shot tasks, overlooking the ability to repair grounding breakdowns across turns. We introduce an iterated, multi-turn negotiation game in which two agents allocate shared resources toward private projects with verifiable jointly optimal outcomes. While individual agents can identify Pareto-optimal allocations in isolation, agent dyads consistently fail to reach them across open- and closed-source models. Our investigation reveals four failure modes: (1) coordination degrades when shared interaction history is absent; (2) yet accumulated context can itself become a liability through stubborn anchoring, where initial proposals are treated as axiomatic rather than negotiable; (3) a reliance on perfunctory fairness (equal resource splits) over reward-maximizing coordination; and (4) failures in referential binding, where agents lose track of commitments across turns. These results highlight dynamic grounding as a critical and understudied axis of multi-agent coordination. Our framework decomposes the coordination gap into measurable components: the oracle baseline establishes that the gap is not attributable to individual reasoning limitations; the no-talk baseline establishes that communication is necessary; and a full-transparency intervention establishes that information exchange alone is insufficient: the bottleneck lies in the interactive processes of joint plan formation, commitment, and execution that constitute dynamic grounding.

---


### 245. [Robust Linear Dueling Bandits with Post-serving Context under Unknown Delays and Adversarial Corruptions](https://arxiv.org/abs/2605.01752)

**<font color=#1a73e8>作者：</font>** Youngmin Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study linear dueling bandits in volatile environments characterized by the simultaneous presence of post-serving contexts, delayed feedback, and adversarial corruption. Feedback is subject to unknown stochastic or adversarial delays and a cumulative corruption budget $\mathcal{C}$. To address these challenges, we propose \term, which integrates a learned approximator that predicts post-serving contexts from pre-serving information. It further employs an adaptive weighting strategy that clips feature vectors to mitigate the impact of corrupted and delayed observations simultaneously. Under standard regularity conditions and a parametric post-serving mapping, we rigorously establish that our algorithm is delay-regime-agnostic, achieving a regret upper bound of $\widetilde{\mathcal{O}}(d(\sqrt{T} + \mathcal{C} + \mathcal{D}))$, where $d$ is the total feature dimension and $\mathcal{D}$ encapsulates the delay complexity. Crucially, our analysis reveals an additive cost structure between corruption and delay, avoiding the multiplicative degradation typical of prior works. We further establish lower bounds that nearly match our upper bounds up to a $\sqrt{d}$ factor for adversarial delays in the absence of post-serving contexts.

---


### 246. [Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems](https://arxiv.org/abs/2605.01758)

**<font color=#1a73e8>作者：</font>** Yue Ma, Ziyuan Yang, Yi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large multimodal model-based Multi-Agent Systems (MASs) enable collaborative complex problem solving through specialized agents. However, MASs are vulnerable to infectious jailbreak, where compromising a single agent can spread to others, leading to widespread compromise. Existing defenses counter this by training a more contagious cure factor, biasing agents to retrieve it over virus adversarial examples (VirAEs). However, this homogenizes agent responses, providing only superficial suppression rather than true recovery. We revisit these defenses, which operate globally via a shared cure factor, while infectious jailbreak arise from localized interaction behaviors. This mismatch limits their effectiveness. To address this, we propose a training-free Foresight-Guided Local Purification (FLP) framework, where each agent reasons over future interactions to track behavioral evolution and eliminate infections. Specifically, each agent simulates future behavioral trajectories over subsequent chat rounds. To reflect diversity in MASs, we introduce a multi-persona simulation strategy for robust prediction across interaction contexts. We then use response diversity as a diagnostic signal to detect infection by analyzing inconsistencies across persona-based predictions at both retrieval-result and semantic levels. For infected agents, we apply localized purification: recent infections are mitigated via immediate album rollback, while long-term infections are handled using Recursive Binary Diagnosis (RBD), which recursively partitions the image album and applies the same diagnosis strategy to localize and eliminate VirAEs. Experiments show that FLP reduces the maximum cumulative infection rate from over 95% to below 5.47%. Moreover, retrieval and semantic metrics closely match benign baselines, indicating effective preservation of interaction diversity.

---


### 247. [PointCSP: Cross-Sample Semantic Propagation and Stability Preservation in Self-Supervised Point Cloud Learning](https://arxiv.org/abs/2605.01759)

**<font color=#1a73e8>作者：</font>** Xinxing Yu, Ajian Liu, Sunyuan Qiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene-level point cloud self-supervised learning (PC-SSL) has demonstrated potential in enhancing the generalization capability of 3D vision models. Despite the advances in the field through existing methods, the sample-independent modeling paradigm still poses significant limitations in terms of maintaining consistent semantic representations across scenes. This challenge hinders the construction of a unified and transferable semantic space. To address this issue, we propose a PC-SSL framework based on cross-sample semantic propagation (CSP), in which samples within a batch are serialized into continuous input and processed by a state-space model to enable semantic state propagation. This mechanism explicitly models the dynamic dependencies across samples in the state space, allowing the network to establish cross-sample semantic consistency in the latent space and achieve global semantic alignment. Since serialization-based pretraining requires batch-level input organization, we further introduce an asymmetric semantic preservation distillation (SPD) during finetuning to achieve structural alignment of semantic transfer and eliminate inconsistencies caused by batch dependency. The proposed SPD ensures stable transfer of pretrained semantics through a heterogeneous input mechanism and a semantic feature alignment constraint. This enables the model to maintain structured semantic consistency and robustness under single-scene testing conditions. Extensive experiments on multiple benchmark datasets demonstrate that our method consistently outperforms state-of-the-art methods in both performance and semantic consistency.

---


### 248. [TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/abs/2605.01761)

**<font color=#1a73e8>作者：</font>** Quanchen Zou, Nizhang Li, Wenxin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Video (T2V) models have demonstrated remarkable capability in generating temporally coherent videos from natural language prompts, yet they also risk producing unsafe content such as violence or explicit material. Existing prompt-level defenses are largely inherited from text-to-image safety and operate on the lexical surface of the input, making them vulnerable to jailbreak attacks that disguise harmful intent through rephrasing or adversarial prompting. Moreover, T2V generation introduces a distinctive challenge overlooked by prior work: temporally emergent risk, where a seemingly benign prompt leads to unsafe content through the generator's temporal extrapolation toward narrative coherence. We propose \method{}, a training-free, inference-time defense framework that reformulates T2V safety as a causal intervention in a temporally structured semantic space. TrajShield handles explicit unsafe prompts, jailbreak attacks, and temporally emergent risks in a unified manner by simulating the implied trajectory of a prompt, localizing the causal origin of potential risk, and applying a minimally invasive rewrite that neutralizes the risk while preserving safety-irrelevant semantics. Experiments on T2VSafetyBench across 14 safety categories and multiple T2V backends demonstrate that TrajShield achieves state-of-the-art defenseive performance while maintaining high semantic fidelity, substantially outperforming existing defenses, with an average ASR reduction of 52.44\%.

---


### 249. [VulKey: Automated Vulnerability Repair Guided by Domain-Specific Repair Patterns](https://arxiv.org/abs/2605.01769)

**<font color=#1a73e8>作者：</font>** Jia Li, Zhuangbin Chen, Yuxin Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing prevalence of software vulnerabilities highlights the need for effective Automatic Vulnerability Repair (AVR) tools. While LLM-based approaches are promising, they struggle to incorporate structured security knowledge from sources like CWE and NVD. Current methods either use this information superficially by concatenating the CWE-ID into the input prompt, yielding negligible benefits, or rely on few-shot learning with rigid, non-generalizable examples, which limits their effectiveness in real-world scenarios.
To address this gap, we propose VulKey, an LLM-based AVR framework that leverages a hierarchical abstraction of expert knowledge to guide patch generation. Our novel three-level abstraction formulates repair strategies in terms of CWE type, syntactic actions, and semantic key elements. This approach captures the essence of a security fix with greater generality than concrete examples and more semantic richness than traditional syntax-based templates, overcoming the coverage limitations of prior methods.
VulKey is implemented as a two-stage pipeline: first, expert knowledge matching predicts an appropriate repair pattern for the vulnerability; second, repair code generation uses a pattern-guided, fine-tuned LLM to produce secure patches.
On the real-world C/C++ dataset PrimeVul, VulKey achieves 31.5% repair accuracy, surpassing the best baseline by 7.6% and outperforming leading tools such as VulMaster and GPT-5. Moreover, VulKey demonstrates cross-language and cross-model generalizability, with state-of-the-art performance on the Java benchmark Vul4J. These results underscore the importance of structured expert knowledge in advancing AVR effectiveness.
Our work demonstrates that explicitly modeling and integrating expert security knowledge through hierarchical patterns is a crucial step toward building more effective and reliable AVR tools.

---


### 250. [The Compliance Gap: Why AI Systems Promise to Follow Process Instructions but Don't](https://arxiv.org/abs/2605.01771)

**<font color=#1a73e8>作者：</font>** Kwan Soo Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An auditor instructs an AI assistant: "open each file individually using the Read tool -- no scripts, no agents." The AI replies "Yes" -- then issues a single batched call summarizing all fifty files at once. We call this the Compliance Gap: a third, orthogonal axis of AI honesty distinct from factual truthfulness and rhetorical substance. Three questions: does this verbal-behavioral disconnect exist (existence); can any text-only observer recover it (detectability); what infrastructure does AI deployment need (remedy)? Some 75 benchmarks (IFEval, SWE-bench, BFCL, COMPASS, SpecEval) measure outcome fidelity; none measures process fidelity. Theorem 1 shows the gap is structurally inevitable under RL that rewards text without observing behavior. Theorem 2, via the Data Processing Inequality, shows it is undetectable from text alone -- by any human or LLM observer, present or future. Thirteen experiments and 2,031 sessions on six frontier models confirm both predictions. Under default framing, all six exhibit instruction compliance rates of 0% -- Claude Sonnet 4 verbally agrees ten out of ten times then bypasses in all ten. The gap is selective: 97% compliance where rationale is rewarded (audit trails), 0-4% where it is not (file reading, privacy masking); removing delegation tools raises compliance to 75% (Cohen's d = 2.47), confirming environmental affordance rather than weight-encoded failure. Nine blinded human raters achieve Fleiss' kappa = 0.130 and correctly identify zero of fifteen compliant sessions, exactly as Theorem 2 predicts. Where humans show 47% intention-behavior gaps in psychology and 96.5pp gaps in surgical audits, RLHF-trained models approach 100% under default conditions -- a regime warranting its own measurement infrastructure. We release BS-Bench: the first open benchmark for process compliance, with seven tool-call-log audit metrics and a public leaderboard.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
