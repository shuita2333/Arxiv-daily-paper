# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-264](./part-06.md)

---

### 151. [Beyond DFT electronic band structures via dual-space orbital learning](https://arxiv.org/abs/2610.19919)

**<font color=#1a73e8>作者：</font>** Minhyuk Kang, Beom Seok Kang, Nikolai Argatoff 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate electronic band structures are essential for predicting material properties, but high-fidelity calculations are computationally demanding. We introduce O-kRystal, a dual-space orbital-learning framework that uses a lower-cost Perdew-Burke-Ernzerhof (PBE) calculation as both an energy baseline and a source of structured orbital information. Combining PBE band energies with real- and reciprocal-space orbital matrices, O-kRystal predicts higher-level corrections for individual electronic states as a function of crystal momentum and spin. For states within 5 eV of the band-edge midpoint, it predicts Heyd-Scuseria-Ernzerhof (HSE06) band energies with a mean absolute error of $0.171 \pm 0.009$ eV across nearly 6,000 three-dimensional materials spanning insulating, metallic, magnetic, and nonmagnetic systems. On a separate benchmark of six strongly correlated materials, it reduces the corresponding PBE band-energy MAE by 68.7% and resolves orbital-dependent changes in the relative placement of transition-metal d and ligand p states. Despite training only at high-symmetry points, it maintains comparable accuracy at unseen points along band paths and reconstructs HSE06 densities of states from dense Brillouin-zone predictions. Finally, training O-kRystal on $G_0W_0$ quasiparticle energies for two-dimensional materials demonstrates its applicability across levels of theory and the potential of orbital learning for higher-fidelity, momentum-resolved electronic-structure prediction beyond density functional theory.

---


### 152. [SAM3RL: Memory Control via Reinforcement Learning for Visual Object Tracking](https://arxiv.org/abs/2610.19931)

**<font color=#1a73e8>作者：</font>** Tomáš Čížek, Matej Straka, Illia Volkov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Model 3 (SAM 3) is a foundation model for image and video segmentation that sets the state of the art in visual object tracking. Its tracker, inherited from SAM 2, stores information from past frames in a memory bank, managed by a simple First-In-First-Out rule, allowing temporal consistency in complex videos. Several recent methods improve SAM 2 with hand-crafted memory update rules, each targeting a specific failure mode, such as distractors, occlusions, or object motion. However, their gains transfer only partially to the stronger SAM 3 backbone. We instead present a more general, data-driven approach that frames memory control as a sequential decision-making task. SAM3RL is an extension of the SAM 3 tracker with a lightweight memory controller, trained by reinforcement learning, that decides which frames enter the memory bank in order to maximize tracking performance. SAM3RL sets a new state of the art on 10 of 12 tracking and video object segmentation benchmarks, outperforming all hand-crafted rules without any runtime overhead. The same approach applied to SAM 2 gives SAM2RL, which outperforms hand-crafted rules on 9 of the 12 benchmarks, showing the generality of our method across model generations.

---


### 153. [MorphingNet: Symbolic Regression Where the Network Is the Formula](https://arxiv.org/abs/2610.19942)

**<font color=#1a73e8>作者：</font>** Jincheng Gao, Jiahe Yi, Shuo Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MorphingNet, a network for symbolic regression (SR) whose units change their function continuously. Instead of searching over expressions built from a fixed operator library, MorphingNet trains the form of each function as a parameter, so SR becomes one continuous optimization problem. Its units are either pole-free rational functions or complex exponential--logarithm functions, which move between exponentials, sinusoids, damped oscillations, power laws and logarithms as their parameters change. The network is a readable formula at every step of training, and no operator library is needed to train it; a structure-recovery step afterwards rewrites the trained formula into short elementary expressions. Training is dense linear algebra, so it is GPU-friendly and scales to large data. MorphingNet achieves state-of-the-art accuracy on SRBench, recovers most generating formulas on synthetic benchmarks, and on large data is up to two orders of magnitude faster than the strongest search method. By turning the search for a formula into the training of a network, MorphingNet offers a new paradigm for SR and for scientific discovery from data.

---


### 154. [Does Machine Translation Retain Media Bias?](https://arxiv.org/abs/2610.19945)

**<font color=#1a73e8>作者：</font>** Silvia V. Gargova, Tim Menzner, Jochen L. Leidner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Within the most recent two decades, machine translation (MT) has been advanced from a research area to a mature, deployed technology for prose text and most language pairs. However, language has different dimensions of meaning, and the alluded progress has primarily been demonstrated for propositional meaning.
In this small exploratory study, we investigate whether one type of affective meaning, namely different types of linguistically expressed media bias, are retained under automatic translation for two language pairs, English and German as the source languages, and Bulgarian as the target language. We evaluate four state-of-the-art translation methods to answer the question whether and to what degree a loss of non-neutral language (specifically, 27 types of media bias) can occur as a result of applying MT.
Our empirical findings are consistent with the claim that MT does not fully retain existing news bias of its input source text, but also may add extra bias of its own. To the best of our knowledge, this is the first experimental study of MT media bias retention.

---


### 155. [Learning Graph Energies for Finite-Time Generation](https://arxiv.org/abs/2610.19946)

**<font color=#1a73e8>作者：</font>** Amartya Banerjee, Xingyu Xu, Caroline Moosmüller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy-based models can represent distributions over discrete structures such as molecular graphs, but an energy that is accurate at equilibrium need not yield accurate samples when the sampler stops after a fixed number of steps. We introduce finite-horizon energy learning, which adapts the acceptance energy of a Metropolis--Hastings sampler to the distribution it returns after a prescribed number of steps, with initialization, proposals, and annealing schedule held fixed. For graph generation, a frozen pretrained model supplies initialization and proposals, and a learned energy governs acceptance. A training-only discriminator scores completed samples, and coupled continuations of the accepted and rejected branches of a proposal give an acceptance-gradient estimator that is unbiased for a fixed discriminator under stated conditions, without equilibrated negative samples or differentiation through discrete states. Generation uses the learned energy in the original single-trajectory sampler, without discriminator evaluations or reranking. On twelve pairwise binary targets with exactly evaluated terminal laws, learned energies have lower median terminal total variation than the equilibrium-correct energy in every tested short-horizon setting, and than its numerically tuned scalar multiple in most settings. On MOSES, a learned two-coefficient combination of pretrained Graph Energy Matching (GEM) potentials lowers FCD by 3.7--10.5\% relative to scale-calibrated GEM at matched sampling steps, with validity gains at the shortest budget and a sub-point validity trade-off at higher budgets.

---


### 156. [Quiet Triggers, Loud Footprints: A Tri-Space Measurement Study of Backdoor Stealthiness](https://arxiv.org/abs/2610.19947)

**<font color=#1a73e8>作者：</font>** Behrad Tajalli, Henk Berendsen, Xiaoyun Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks on deep neural networks are commonly evaluated by attack success rate and benign accuracy, yet their stealthiness remains inconsistently defined and measured. Existing work often studies only one observable aspect of stealthiness, such as trigger imperceptibility, feature-space separability, parameter-space concentration, or evasion of particular defenses. This creates a fragmented picture: an attack may appear stealthy under one metric while leaving conspicuous footprints elsewhere. This paper presents a tri-space measurement study of backdoor stealthiness in image classification. We distinguish latent stealthiness---the ideal but unobservable difficulty of distinguishing a backdoored system from a benign one---from measurable footprints in three spaces: input, feature, and parameter space. Under this framework, we evaluate representative backdoor attacks across four datasets and three model architectures using a broad suite of footprint metrics.
Our results show that stealthiness is not monolithic: attacks that are quiet in one space are often loud in another, and existing attacks rarely achieve consistently small footprints across all three spaces. We further analyze agreement and disagreement among stealthiness metrics and study how footprint measurements interact with attack success rate. Based on observed blind spots in existing measurements, we introduce two diagnostic metrics: Class-Specific Davies--Bouldin Index (CDBI), which captures class-conditional feature overlap, and TAC--UCLC Product (TUP), which identifies channels that are both trigger-responsive and downstream influential. These metrics are intended to augment, not replace, the broader measurement suite. Finally, we provide practical guidance for future stealthiness evaluations.

---


### 157. [Neurosymbolic Learning of Interpretable World Models](https://arxiv.org/abs/2610.19955)

**<font color=#1a73e8>作者：</font>** Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about the world. We introduce Concept-Grounded World Models (CGWMs), a neurosymbolic world model design that instead learns interpretable concept representations. We learn these concepts from observations using explicit and complete knowledge, expressed in temporal logic, that specifies the valid world states and the temporal relations governing their dynamics. Furthermore, we directly use this knowledge by formulating planning as differentiable reasoning, optimising the agent's actions by gradient ascent to satisfy a goal. We experimentally compare CGWM with a purely neural baseline and a neurosymbolic baseline on two game environments. We find that CGWMs ground concepts much more accurately, even over long horizons, resulting in significantly more robust planning both in and out of distribution.

---


### 158. [Choosing the Number of Attention Heads from Intrinsic Dimension: A Small-Scale Study](https://arxiv.org/abs/2610.19966)

**<font color=#1a73e8>作者：</font>** Arjun Boya, Charan Sai Bandaru, Masthanaiah Pillimetla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The number of attention heads in a transformer is usually set by convention or grid search. We test a simple heuristic for setting it in advance: estimate the intrinsic dimension of token representations without labels, and use roughly that many heads. We estimate intrinsic dimension with a nested-dropout VAE trained on DistilBERT embeddings of WikiText-2, choosing the KL weight at the knee of the VAE's rate-distortion curve rather than by hand. This gives $k^*=9.2$ (95% CI [8.6, 9.8]). In a small 4-layer transformer trained from scratch, 10 heads and 32 heads are statistically equivalent on SST-2 and on MRPC (paired TOST over 10 seeds, $\pm1$ point margin), with 69% fewer attention parameters for the 10-head model. Training 10 heads from the start also slightly outperforms training 32 heads and pruning to 10 (0.6 points, $p=0.008$). The evidence is narrow: two classification tasks, one small architecture, no pretrained models, and no formal link between intrinsic dimension and head count. We present the result as a practical heuristic worth testing at larger scale, not as a general principle.

---


### 159. [AdaptaFace: Adversarial Assistance for Inclusive Facial Gesture Interaction](https://arxiv.org/abs/2610.19977)

**<font color=#1a73e8>作者：</font>** Siyu Zhang, Yelu Gu, Xiaoyun Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Facial gestures can enable access for people with motor impairments (PwM), yet recognizers may not reliably interpret individual facial movement patterns. Existing approaches either constrain agency by requiring predefined templates or impose repeated calibration, data collection, and computation through user-specific retraining. We present AdaptaFace, an input-level compatibility layer using bounded, proxy-dependent adversarial perturbations to translate user-compatible gestures into inputs for an unchanged facial action unit (AU)-based recognizer. Designed around six personalization principles informed by interviews with 12 PwM, AdaptaFace supports both recognition enhancement and gesture vocabulary extension. In a within-subject study with 16 participants, AdaptaFace increased task completion from 59.7% to 90.5% and reduced workload from 5.61 to 4.21. Offline validation showed strong steering with aligned perturbation generation and evaluation but weaker cross-recognizer transfer, defining the approach's boundary. These findings frame adversarial assistance as input-side accessibility mediation for personalized facial-gesture interaction.

---


### 160. [Think Once, Reflect Twice: How Feedback Shapes Human-AI Collaboration](https://arxiv.org/abs/2610.19991)

**<font color=#1a73e8>作者：</font>** Joshua Holstein, Philipp Spitzer, Sebastian Schäfer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) increasingly supports human decision-making in high-stakes domains, designing effective human-AI collaboration becomes critical. Successful collaboration requires humans to reflect on decision-making processes and adjust their strategies accordingly. Current research typically investigates interventions, such as explainable AI, that target reflection during the decision-making process (reflection-in-action). Less attention has been given to retrospective examination of decisions (reflection-on-action). This work explores reflection-on-action by studying the impact of feedback on reliance behavior and human-AI team performance. Specifically, we investigate feedback interventions targeting overrides of AI advice through a behavioral study (N=244). We find that such feedback influences reflection-on-action, while unidirectional feedback risks reducing subsequent reflection-in-action. Furthermore, we identify opposing shifts in reliance behavior that leave overall human-AI team performance unchanged but show context-dependent effects. Balanced feedback did not show these risks, preserving both concurrent and retrospective reflection, offering insights for designing for appropriate reliance on AI.

---


### 161. [Why 3D Reconstruction Breaks Down on Under-Ice AUV Video, and How to Predict It](https://arxiv.org/abs/2610.19993)

**<font color=#1a73e8>作者：</font>** Ana-Ştefania Kogălniceanu, Klára Orbán, Ashwin Nedungadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction of 3D structures using under-ice AUV video footage has been inaccurate, although it is not certain whether this is due to shortcomings in the methods or an inherent deficiency of the capture system. We test four different models for reconstruction on the same Antarctic under-ice AUV video (Icefin, Kamb Ice Stream): classical feature matching SfM, differentiable photometric splatting, volumetric depth fusion, and a pose-free feed-forward foundation model. All four fail, each in a distinct way: near-total registration yielding almost no structure, geometrically broken output despite healthy photometric metrics, a persistent coverage artifact, and unstable cross-chunk scale. We show that all four are consistent with the same capture regime, a small camera-baseline-to-scene-depth ratio. Following our analysis, we propose a detection system that flags this type of failure in minutes, rather than hours of wasted compute.

---


### 162. [Empirical Boundaries of Reservoir Computing for Few-Shot Sequence Pattern Tasks](https://arxiv.org/abs/2610.19997)

**<font color=#1a73e8>作者：</font>** Mario Mallea, Angela Nebot, Franscisco Mugica  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient sequence modeling remains a fundamental challenge in machine learning. Despite the success of Transformers, recurrent neural networks (RNNs) have recently re-emerged as efficient alternatives. Particularly, Echo State Networks (ESNs) offer a compelling framework of randomized RNNs that have been extensively studied for time-series forecasting and dynamical systems. This paper presents an empirical analysis of distributional, architectural, and optimization variants of ESNs evaluated on few-shot sequence-to-sequence (seq2seq) pattern tasks. These synthetic tasks utilize discrete symbol sequences, characterized by delays, inactive phases, and triggered markers to isolate and evaluate memory and pattern recognition capabilities. The minimality of these tasks is crucial to understand the strengths and limitations of machine learning models. Furthermore, when the input signal utilizes a one-hot encoding, ESN dynamics are governed strictly by their weight distributions, offering an ideal lens through which to study reservoir computing.
Our findings map the performance boundaries of ESNs relative to state-of-the-art (SOTA) models. We show that preserving a linear state regime is vital for memory tasks, such as pattern completion or simple copy. We propose a data-dependent modulation mechanism for nonlinear input injection into the reservoir (G-ESN). G-ESN functions as a statistical filter capable of solving tasks that conventional ESNs cannot (the adding problem and bracket matching). Finally, for Deep ESNs, we evaluate a shared readout mechanism across layers that outperforms conventional concatenated readouts on structural tasks, including selective copy, sorting problem, and bracket matching.

---


### 163. [Provable Transformer Context Compression for In-Context Reinforcement Learning](https://arxiv.org/abs/2610.20004)

**<font color=#1a73e8>作者：</font>** Yajie Zhao, Yingjun Mo, Zhiyong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers can perform in-context reinforcement learning without parameter updates. However, existing theoretical constructions often require context sizes that grow with the number of sampled transitions, leading to increasing memory costs in large-scale problems. This raises a fundamental scalability question: how much context is intrinsically necessary to carry out such learning? We answer this question for fixed-policy TD evaluation. We show that, with a shared linear decoder, the minimum context dimension required to exactly reproduce the first $L$ TD iterates is the Krylov dimension induced by the sampled transitions. When the available context dimension $m$ falls below this threshold, exact reproduction is no longer possible. In this regime, we characterize the optimal approximation error and show that it decays as $\Theta(\gamma^m\max\{1,1/(m(1-\gamma))\})$ where $\gamma$ is the discounting factor. Moving from representation complexity to actual memory cost, we characterize the optimal retained memory for exact continuous representations as $\Theta(nk_L)$ and show experimentally that on a sampled task whose exact rank is full but whose numerical rank is small, a context accurate to $10^{-2}$ is $88.7\%$ smaller than the sparse sufficient statistics of TD. Finally, we establish the learnability of the shared executor through pretraining by proving global convergence of an auxiliary objective over effective attention parameters under suitable task diversity. Experiments across diverse TD evaluation problems validate parameter recovery and the predicted context--accuracy tradeoff.

---


### 164. [Outperforming 1000 Euclidean Layers With Hyperbolic Goal-Conditioned RL](https://arxiv.org/abs/2610.20009)

**<font color=#1a73e8>作者：</font>** Timo Klein, Thomas Lang, Andrii Shkabrii 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling self-supervised contrastive reinforcement learning (CRL) to 1000-layer Euclidean neural networks has enabled state-of-the-art goal-reaching performance, yet wall-clock time scales linearly with depth. We find that changing the geometry achieves stronger performance with far shallower networks. This matters in complex navigation environments, where walls can make route distance deviate substantially from Euclidean distance. In a U-shaped maze, we show that the longer the route, the more it deviates from Euclidean distance. Hyperbolic CRL addresses this mismatch by replacing Euclidean distances in CRL's contrastive objective with geodesic distances in hyperbolic space. On hard navigation tasks, inductive bias beats scale: depth 64 hyperbolic agents outperform 1024-layer-deep Euclidean networks while training more than $12 \times$ faster and using about $13 \times$ fewer parameters. We observe that hyperbolic agents behave qualitatively better in hard humanoid mazes, where they follow corridors to reach goals, whereas Euclidean agents try straight-line shortcuts over walls. Our results show that matching the representation geometry to the task can substitute for substantial network depth. Code is at this https URL .

---


### 165. [On the Convergence of Semi-Gradient TD: A Mean Field Perspective](https://arxiv.org/abs/2610.20014)

**<font color=#1a73e8>作者：</font>** Haruki Settai, Tadashi Kozuno, Shinji Ito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-gradient temporal-difference learning is a core algorithmic component of reinforcement learning, but bootstrapping with function approximation generally induces a non-conservative vector field and can lead to instability. We analyze this effect for two-layer neural networks in the mean-field regime and identify a simple stability mechanism in which entropy-induced relaxation dominates the sensitivity of the moving bootstrap target. Under this condition, we prove exponential convergence to a unique fixed point and quantify its bias relative to the unregularized Bellman solution. We also show that the same mechanism extends to entropy-regularized off-policy control through soft Q-learning.

---


### 166. [Sequential Learning-Based Physics-Informed Neural Network Modeling for Parameter Estimation on a Power Converter](https://arxiv.org/abs/2610.20041)

**<font color=#1a73e8>作者：</font>** Samuela Rokocakau, Panagiotis Kakosimos, Giulia Tresca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A staged physics-informed neural network (PINN) is proposed for identifying the inductance, capacitance and parasitic resistances of a DC buck converter from time-domain data. Gradients are released in the order of L to C to rL to rC, a sequence derived from sensitivity analysis. The five-stage schedule recovers L and C to within 5% and the series ESR to 10%, while a three-stage variant attains the same accuracy 11% faster. An 84 factorial sweep confirms that the trained PINN remains accurate for simultaneous 8% perturbations of all four components, achieving a waveform RMSE of 2.6 x 10-2 over 5 ms-an order-of-magnitude better than a simultaneous-training baseline.

---


### 167. [ESAU: Expeditious Swarm Remote Attestation for Pub-Sub IoT Networks with Untrusted Cloud-based Proxy Verifier](https://arxiv.org/abs/2610.20047)

**<font color=#1a73e8>作者：</font>** Ruei-Hau Hsu, Yu-Hsiang Hu, Rafael Kaliski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Internet of Things (IoT) devices collect and process data, security is essential. IoT devices often combine with other emerging technologies, such as artificial intelligence (AI) and fifth-generation (5G) communications, to support applications such as smart grids and internet-of-vehicles (IoV). Because IoT devices are deployed remotely, remote attestation (RA) effectively verifies each device's state. However, the scale of IoT deployments makes device management challenging for owners. Therefore, cloud-assisted IoT management services often provide RA solutions. Although cloud-based IoT services can securely manage IoT devices, passive malicious administrators or hacked IoT device owners' accounts can control IoT devices without cloud IoT service authorization. Therefore, this work proposes a cloud-assisted RA system that addresses three main challenges of IoT device RA: 1) lightweight RA design for resource-limited IoT devices, 2) unauthorized access to IoT devices by passive malicious administrators or compromised owner accounts on the cloud IoT management platform, and 3) RA may not extend to an authenticated key exchange protocol. In addition to proposing a swarm RA scheme that addresses these three challenges, this work analyzes the system's security properties and evaluates its feasibility through implementation and simulation.

---


### 168. [CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection](https://arxiv.org/abs/2610.20049)

**<font color=#1a73e8>作者：</font>** Qichen Zhao, Shengfang Zhai, Qingni Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent difficult to identify through individual-package auditing. We introduce CoRedSkill, a compositional red-teaming method that forms stealthy attacks through cooperating skills while preserving their original utility. CoRedSkill decomposes an existing workflow into interdependent skills and embeds attack operations in task functions through abstract syntax tree (AST) rewriting, with skill instructions guiding the agent to autonomously select and invoke the relevant skills, and workflow dependencies and intermediate artifacts connecting the injected operations during task execution. We construct a benchmark of 150 cases covering 50 tasks and three attack objectives to evaluate attack success, task completion, and audit detection. In the main evaluation, CoRedSkill achieves 98.0% attack success and 95.3% task success with a 3.3% detection rate, and a joint success rate of 90.7% (attack success, task completion, and audit evasion in the same case) compared with 6.7--42.7% for the four baselines. Skill compositions can therefore complete legitimate tasks while carrying out unauthorized operations that evade auditing.

---


### 169. [GBTSVR: Twin Support Vector Regression via Granular Ball Computing](https://arxiv.org/abs/2610.20053)

**<font color=#1a73e8>作者：</font>** A. Quadir, M. Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regression models used in real-world applications are often challenged by noise, outliers, data heterogeneity, and asymmetric error characteristics, which severely limit the effectiveness of conventional point-wise learning models. While twin support vector regression (TSVR) partially addresses these issues through the use of nonparallel regression bounds, it still relies on individual samples as basic learning units. As a result, TSVR remains highly sensitive to noisy and contaminated observations and fails to leverage the underlying structural and regional information inherent in complex datasets, leading to suboptimal robustness and generalization performance. To address these limitations, we introduce granular ball twin support vector regression (GBTSVR) and its quantile extension, granular ball twin support vector quantile regression (GB-TSVQR). The proposed models integrate granular ball computing with TSVR, replacing individual data points with compact, structure-preserving granular balls as fundamental learning units. This region-level representation effectively suppresses noise and outliers while preserving intrinsic data geometry, thereby enhancing robustness, stability, and generalization. GBTSVR constructs nonparallel lower- and upper-bound regression functions over granular balls, significantly reducing sensitivity to sample-level perturbations. Building upon this framework, GB-TSVQR further incorporates quantile regression principles to simultaneously capture heterogeneous trends and asymmetric error distributions across different quantile levels. Extensive experiments on synthetic datasets, time-series benchmarks, and outlier-contaminated data demonstrate that the proposed GBTSVR and GB-TSVQR consistently outperform state-of-the-art regression models.

---


### 170. [Trainable at Depth, Solvable at Small Size: What the Loss Surface of a Polynomial Activation Dictates for Designing, Initializing and Training Networks](https://arxiv.org/abs/2610.20069)

**<font color=#1a73e8>作者：</font>** Xiuyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What makes a deep network train, and what shape is its loss surface? We answer both with one construction at two scales: a polynomial activation f (z) = z + {\lambda}z 3 , clamped and projected onto the unit sphere, plus an unnormalized identity path. As a deep stack it trains to one hundred layers on MNIST with no normalization machinery; as a small model its square loss is a polynomial system we solve exactly. The small scale explains the large one: it prescribes how to design, initialize and train the stack.

---


### 171. [Rethinking Prediction Horizons: Decoupling Model Queries from State Updates in Few-Step MeanFlow](https://arxiv.org/abs/2610.20071)

**<font color=#1a73e8>作者：</font>** Tinglan Wang, Haixu Liu, Shaobo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MeanFlow predicts interval-average velocities, but conventional few-step sampling ties the interval queried from the model to the duration of the state update. We separate these two quantities at inference, fixing the model, update grid, and number of queries while varying the prediction horizon. Our central finding is that the horizon response depends on both query position and the states entering that query. Across seven independently trained CIFAR-10 checkpoints at classifier-free guidance (CFG) scale 2, a longer horizon worsens FID at early steps but improves it at the midpoint. To probe whether query time alone determines this response, we fix the midpoint query and current/subsequent guidance while changing only earlier CFG. In held-out factorial outcomes on five previously studied checkpoints, the mean midpoint horizon benefit increases from 0.109 to 1.308 FID, indicating sensitivity to the incoming-state distribution. A frozen four-query rule reduces mean CIFAR-10 FID by 2.023 without retraining or extra queries, including gains on five checkpoints trained after rule selection. A milder rule also improves mean FID by 1.041 on a stronger frozen grid, with fixed-rule FID gains on the evaluated public ImageNet-256 and AFHQ checkpoints. However, matched-budget calibration favors query-start shifting in historical CIFAR tests, and the tested Horizon allocation adds no FID benefit beyond Grid+Start on two public ImageNet models. Thus, prediction horizon is a distinct, position- and state-sensitive inference control, but not a universally preferred one.

---


### 172. [GDBA-Net: A Gated Dual-Branch Adaptation of SAM2 for Robust Cross-Domain Nuclei Segmentation](https://arxiv.org/abs/2610.20073)

**<font color=#1a73e8>作者：</font>** Biplab Poudel, Betserai Albert Magarire, Anish Kumar Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate nuclei segmentation underpins quantitative computational pathology, yet remains challenging due to morphological variability, weak boundaries, nuclear crowding, and pronounced domain shifts arising from differences in tissue preparation, staining, and acquisition. While deep learning and recent foundation models have improved segmentation performance under matched distributions with the original training data, their generalization across heterogeneous histopathology domains remains limited. We introduce GDBA-Net, a parameter-efficient nuclei segmentation framework built around the proposed Gated Dual-Branch Adapter (GDBA). GDBA-Net adapts a frozen SAM2 encoder by integrating pretrained semantic representations with explicit frequency-derived structural priors. The complementary representations are independently transformed through Grid MLP branches and dynamically integrated using sample-adaptive channel-wise gating, selectively emphasizing structural cues relevant to nuclear delineation. Despite using only 4.3 million trainable parameters, GDBA-Net achieves state-of-the-art in-dataset performance and consistently superior cross-dataset generalization across six diverse nuclei segmentation benchmarks under fully supervised, cross-dataset, and five-shot adaptation protocols, outperforming competing CNN-, transformer-, and foundation model based methods. Comprehensive ablations confirm that these gains arise from the coordinated design of semantic-frequency complementarity and adaptive gating rather than increased model capacity. By uniting transferable semantic representations with explicit structural priors, GDBA-Net provides a robust, annotation-efficient solution to domain variability in nuclei segmentation. this https URL

---


### 173. [Feasibility of a Patient-Specific Digital Twin for Ventriculoperitoneal Shunt Trajectory Planning](https://arxiv.org/abs/2610.20074)

**<font color=#1a73e8>作者：</font>** Kritsanavis Chongsrid, Vich Yindeedej, Supaporn Konmun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Catheter obstruction is the commonest cause of shunt failure; freehand insertion at Keen's point leaves the tip free in cerebrospinal fluid in only one case in ten. We built a digital twin that reconstructs skull, scalp, ear and ventricles from preoperative CT by deterministic geometry, searches every entry around Keen's point for the perpendicular trajectory with the longest intraventricular length under safety constraints, and returns the plan as two ruler measurements from the ear and two depths. Executed freehand in 11 consecutive adults (IDEAL Stage 2a), it achieved Hayhurst Grade 1 placement in 10 of 11 against 22 of 213 historically (p = 9 x 10^-9), median entry and angular deviations 2.5 mm and 5.9 degrees, 1.4 cm more intraventricular catheter than Keen's point, and no intraoperative complication. The technique was unchanged; the gain came from choosing entry and depth per patient. Whether it lowers revision is the next stage's hypothesis.

---


### 174. [A Large-Dimensional Analysis of Least-Squares Federated Learning via Generalized Total Variation Minimization](https://arxiv.org/abs/2610.20075)

**<font color=#1a73e8>作者：</font>** Ekkehard Schnoor, Malik Tiomoko, Alexander Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning over decentralized networks inherently trades off the suppression of local finite-sample noise through collaboration against the bias that collaboration introduces between heterogeneous nodes. We study this tension by performing a large-dimensional analysis of Generalized Total Variation Minimization with least-squares models. Using tools from random matrix theory, we show that Lipschitz observations of the global GTVMin solution concentrate in large dimensions, universally for any underlying network structure. We provide exact analytic expressions for the asymptotically precise performance under both i.i.d. and non-i.i.d. Gaussian mixture distributions on a fixed network. For the latter, these expressions quantify how regularization balances local adaptation against collaboration. Our theoretical results are confirmed by experiments on synthetic and real-world data.

---


### 175. [RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation](https://arxiv.org/abs/2610.20091)

**<font color=#1a73e8>作者：</font>** Jaeyeon Heo, Geuntaek Lim, Yukyung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video scene graph generation (VidSGG) aims to capture objects and their evolving relationships in videos. This requires accounting for both the persistence of object identities and abrupt changes in relationships. Existing methods aggregate information across frames to exploit temporal context, but an emphasis on consistency can obscure these changes. As a result, a model may retain its previous prediction even after the underlying relation has changed. We refer to this failure mode as relational semantic inertia. To address this issue, we propose Relation-Transition-Aware Transformer (RTAformer), a one-stage framework that separately models entity persistence and relation changes. It injects calibrated differences between adjacent-frame relation queries to guide predicate updates, while cross-frame instance alignment during training helps reduce cross-frame representational drift. Experiments on Action Genome show improvements in recall and mean recall over existing methods, with ablation studies supporting the contributions of the proposed components and comparisons using matched backbones showing larger gains on relation-transition frames than on non-transition frames.

---


### 176. [Task-State Governance: A Virtual Machine for Verifiable and Recoverable GUI Agent Execution](https://arxiv.org/abs/2610.20100)

**<font color=#1a73e8>作者：</font>** Wenkui Yang, Yiming Hao, Kai Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents now execute workflows across real applications, but when execution drifts, users must determine what changed, what should have remained untouched, and what can still be recovered. Plan-centric interfaces leave users supervising procedure, but users live with changes to application state. We introduce task-state governance, an interaction paradigm that represents a task as an editable contract linking desired outcomes, facts that must be preserved, and observed application state. We instantiate this paradigm in TaskVM, which projects live state into editable task controls, executes user edits as genuine interface actions, verifies outcomes through independent observation, and marks each action as reversible, compensatable, or irreversible. Across an automated contract benchmark, a controlled user study, and an open live-model exploration, the paradigm strengthened contract compliance and users' recovery control and trust, while execution outcomes were held constant. Task contracts open a design space for governable agent interfaces.

---


### 177. [Language Exposure Matters: Distribution and Order in Multilingual BabyLM Pre-training](https://arxiv.org/abs/2610.20102)

**<font color=#1a73e8>作者：</font>** JiWoo Hwang, Lukas Edman, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate two aspects of multilingual pre-training with limited data, namely how language exposure is distributed across English, Dutch, and Chinese, and how that exposure is ordered during training. In particular, we compare balanced multilingual exposure to language-dominant exposure, where one language is exposed with more training data than the others. We also compare mixed training, where multilingual training data is used throughout training, with curriculum training, where monolingual exposure of the dominant language is followed by balanced multilingual exposure. Our results show that multilingual BabyLM performance varies with both the amount and order of language exposure. Mixed training outperforms curriculum learning across all 15 matched configurations, indicating that simultaneous multilingual exposure is more effective than staged exposure in our setting. Several language-dominant mixed training configurations achieve higher scores than the balanced configuration, suggesting that a balanced distribution is not necessarily the highest-performing configuration in our setting. Interestingly, the Dutch-primary configurations achieve the best overall performance.

---


### 178. [Exhaustive Canonical Skeletons Generation: A Formal Dataset for Decomposable Symbolic Regression](https://arxiv.org/abs/2610.20108)

**<font color=#1a73e8>作者：</font>** Giorgio Morales, Anikó Ekárt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural symbolic regression (SR) models require diverse datasets of mathematical expressions for robust training. However, existing datasets rely predominantly on stochastic sampling methods, which suffer from high structural redundancy and incomplete functional coverage. To address this, we introduce an exhaustive dataset of univariate canonical skeletons generated via a deterministic constrained context-free grammar. A canonical skeleton acts as a generic structural representation that subsumes more specific functional forms, eliminating redundant expressions and avoiding repeated computational efforts. Although our dataset consists of univariate skeletons, it is designed to support the decomposable SR paradigm to solve multivariate SR problems without assuming linear separability. Furthermore, we pair this dataset with a sampling strategy that generates clean numerical data without triggering numerical instabilities or relying on artificial protected operators. Canonicalizing two existing neural SR datasets reveals that our dataset is substantially more compact, eliminates structural repetitions, and achieves a uniform operator distribution free of simplicity bias. Finally, we establish a benchmark of 150 SR problems across three tiers, on which state-of-the-art SR methods are shown to struggle significantly.

---


### 179. [RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](https://arxiv.org/abs/2610.20111)

**<font color=#1a73e8>作者：</font>** Siming Fu, Zheming Fu, Lianrui Mu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling pretrained video diffusion models into few-step autoregressive (AR) generators typically combines student initialization with distribution matching distillation (DMD). An intermediate AR teacher can provide causally compatible targets for ODE initialization. However, causally compatible targets alone do not ensure high-quality generation under a short sampling schedule. We analyze the posterior-mean predictions favored by direct latent regression and empirically find that causal ODE initialization alleviates blur but still leaves fine detail unresolved. To address this limitation, we propose Representation Forcing, which learns few-step causal initialization through representation-space supervision rather than intermediate-teacher trajectory regression. The student is trained with teacher forcing by comparing clean predictions and training targets through normalized features of a frozen video diffusion transformer. This phase reuses the synthetic videos generated by a bidirectional model for AR teacher training and replaces both teacher training and causal ODE distillation, without generating additional causal ODE trajectories. The subsequent asymmetric DMD procedure remains unchanged. Empirical results show that, at four sampling steps, RepForcing better preserves generation quality than intermediate-teacher-based initialization before DMD. After DMD, our four-step chunk-wise model improves VBench Total from 84.04 to 84.66 (+0.62 points) and VisionReward from 6.326 to 10.074 (+59.25%) over the reported causal-ODE-based baseline.

---


### 180. [From Spectral to Frobenius: When Muon Loses Its Spectral Implicit Bias](https://arxiv.org/abs/2610.20112)

**<font color=#1a73e8>作者：</font>** Yongtao Wu, Mahdi Mansouri, Zhenyu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work on implicit bias shows that gradient descent selects the Frobenius max-margin direction on linearly separable problems, whereas Fan et al. (2025) established spectral max-margin behavior for spectral-norm steepest descent methods, including idealized Muon with exact orthogonalization. In practice, however, Muon approximates orthogonalization using finite Newton-Schulz iterations and a positive stabilization constant. We prove that these implementation choices cause Muon to select the Frobenius rather than the spectral max-margin direction in linear classification with separable data. We also establish this behavior for both exponential moving average and Nesterov-style momentum. The key technical ingredient is a summable perturbation argument showing that the resulting parameter trajectories remain at bounded distance from those of gradient descent. We then disentangle the roles of Newton-Schulz iteration count, the stabilization constant, and the Newton-Schulz polynomial, revealing distinct asymptotic behaviors, including directions that achieve neither Frobenius nor spectral max-margin. Finally, we show that Muon can recover its spectral max-margin bias with Newton-Schulz iterations growing logarithmically over training.

---


### 181. [KANLab: TensorFlow Playground for Kolmogorov-Arnold Networks](https://arxiv.org/abs/2610.20117)

**<font color=#1a73e8>作者：</font>** Lukas Niehaus, Robin Rawiel, Ulf Krumnack  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KANLab is a browser-based visualization tool designed to interactively teach the core concepts of Kolmogorov-Arnold Networks (KAN), forked from the widely successful TensorFlow Playground. To maximize educational clarity, KANLab omits residual connections and learnable scaling parameters found in modern KAN implementations, ensuring that displayed B-spline activation curves directly correspond to their underlying trainable control points. Users can inspect and modify activation functions, initialization schemes and observe gradient descent correcting manual disruptions. Furthermore, user can explore phenomena such as activation variance, interactive pruning, and re\-/training within a compact 2D machine learning setting. KANLab is open-source and available at this https URL

---


### 182. [A Bregman Proximal Viewpoint on Neural Operators](https://arxiv.org/abs/2610.20120)

**<font color=#1a73e8>作者：</font>** Abdel-Rahim Mezidi, Jordan Patracone, Saverio Salzo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present several advances on neural operators by viewing the action of operator layers as the minimizers of Bregman regularized optimization problems over Banach function spaces. The proposed framework allows interpreting the activation operators as Bregman proximity operators from dual to primal space. This novel viewpoint is general enough to recover classical neural operators as well as a new variant, coined Bregman neural operators, which includes the inverse activation operator and features the same expressivity of standard neural operators. Numerical experiments support the added benefits of the Bregman variant of Fourier neural operators for training deeper and more accurate models.

---


### 183. [DreamHMR: From Video Generation to Human Motion Modeling via Structural Focusing](https://arxiv.org/abs/2610.20124)

**<font color=#1a73e8>作者：</font>** Zhengjie Xu, Ruihao Gong, Xianglong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human mesh recovery (HMR) provides a geometric foundation for understanding human motion, but accurately reconstructing both body motion and fine hand articulation from videos remains challenging, especially in real-world scenes where occlusion and partial visibility are common. Video generation pretraining offers rich spatial and temporal priors for this task, but its focus on visual synthesis leaves a gap between these representations and explicit human geometry. We present DreamHMR, a general framework that adapts video generation priors for complete body-and-hand reconstruction. It follows a global-to-local strategy, first grounding video representations in human geometry and then refining body and hand detail with reliable local evidence. Global Body Representation Transfer trains the video backbone to predict complete human renderings, turning its native prediction task into a means of learning surface correspondence and posed geometry. Local Joint Feature Enhancement combines contextual estimates with reliable local evidence to recover fine body and hand detail, while limiting interference from occluders and background. Experiments on five datasets with four video backbones demonstrate strong reconstruction performance across backbone families. Under a unified evaluation protocol, our best model outperforms the best existing methods on all reported metrics of 3DPW, EMDB-1, and RICH, reducing body MPJPE by 4.2%, 4.7%, and 6.1%, respectively. In more challenging occlusion settings on held-out BEDLAM and EgoBody sequences, DreamHMR reduces overall body and hand MPJPE by 7.0% and 10.0%, respectively. Our code will be made publicly available.

---


### 184. [In-Context Batch Black-box Optimization via Flow Matching](https://arxiv.org/abs/2610.20138)

**<font color=#1a73e8>作者：</font>** Quoc-Anh Hoang Nguyen, Xinyu Zhang, Daolang Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batch black-box optimization is important for expensive systems where many candidates can be evaluated in parallel, yet only a few rounds of evaluation are affordable. In this regime, effective batch construction must identify multiple promising regions while avoiding redundant evaluations, and conventional Bayesian optimization can require increasingly difficult batch-selection procedures as the batch size grows. We introduce Flow Matching for Thompson-Sampling Refinement (FMTR), an amortized approach that learns offline a continuous, history-conditioned proposal distribution from which variable-size batches can be sampled. FMTR is trained offline by conditional flow matching on Thompson-sampling argmaxes refined toward high-value regions via a horizon-dependent Langevin pushforward map, adapting the exploration-exploitation tradeoff over the optimization horizon. At test time, the model parameters remain fixed and batch generation requires neither task-specific surrogate refitting nor numerical acquisition optimization. FMTR achieves strong performance against batch BO and in-context baselines on synthetic and real-world benchmarks, while substantially reducing the computational cost of batch selection.

---


### 185. [Attention-Based Spatio-Temporal Approach for Fire and Smoke Detection](https://arxiv.org/abs/2610.20141)

**<font color=#1a73e8>作者：</font>** Alireza Mirrashid, Mohammad Khoshbin, Ali Atghaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In various industries, smoke and fire are two of the most important threats in the workplace. One of the common methods for detecting smoke and fire is the use of infrared thermal and smoke sensors, which cannot be used in outdoor applications. Therefore, the use of vision-based methods seems necessary. The problem of smoke and fire detection is spatiotemporal and requires spatiotemporal solutions. This paper presents a method that uses spatial features along with temporal-based features to detect smoke and fire in the scene. It consists of three main parts; the task of each part is to reduce the error of the previous part so that the final model has a robust performance. This method also uses transformer modules to increase the accuracy of the model. The results of our model show the proper performance of the proposed approach in solving the problem of smoke and fire detection and can be used to increase workplace safety.

---


### 186. [Dataset-Level Regularization for Joint-Embedding Self-Supervised Learning](https://arxiv.org/abs/2610.20158)

**<font color=#1a73e8>作者：</font>** Konstantinos Almpanakis, Anna Kreshuk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised joint embedding learning aligns representations of augmented views while regularizing their distribution to prevent collapse. Regularization aims to shape the overall representation distribution, but most joint embedding methods restrict its computation to the active minibatch. We propose out-of-batch regularization, which maintains a dataset-level state in CPU memory and uses globally constructed per-instance targets during minibatch training. Evaluated on natural images and biomedical datasets, these anchors approximate the full-dataset regularization gradient more faithfully than conventional minibatch estimation at small batch sizes. Applications to contrastive (SimCLR) and non-contrastive (SIGReg) approaches show consistent improvement over the corresponding in-batch objectives for image classification, minority-class performance under controlled imbalance, instance retrieval, and continued self-supervised pretraining, with the largest gains at small batch sizes. These results suggest that dataset-level regularization can be decoupled from minibatch optimization, making batch size an optimization choice that does not affect the geometry of the regularizer.

---


### 187. [OneLA: Learning Many Worlds from Latent Actions](https://arxiv.org/abs/2610.20160)

**<font color=#1a73e8>作者：</font>** Ziyu Zhu, Zhaoxu Sun, Fan Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning world models across diverse domains calls for a unified control space, yet ac- tion interfaces vary across domains and action annotations are often scarce. Latent ac- tions learned directly from videos offer a promising way to establish such a space without explicit action supervision. However, learning shared latent actions across domains re- mains challenging, as variations in appearance, embodiment, and dynamics can entangle domain-specific visual cues with transferable transition structure. To this end, we intro- duce OneLA, a simple framework that learns continuous latent actions through a shared orthogonal dictionary and a common predictive objective, without task-specific designs or cross-domain alignment losses during latent action pretraining. These latent actions pro- vide a shared conditioning interface for world models, with lightweight adapters mapping native control commands into the same space. Conditioned on latent actions and the cur- rent visual state, the world model predicts context-dependent transitions for controllable rollout. OneLA improves action readout across domains and reduces action cycle-transfer rotation error by 24.8% over the strongest evaluated baseline. A joint-training comparison further shows a 20.5% improvement in Human Preference Score v3 (HPSv3) for real- scene generation. These results suggest a path toward general-purpose world models that learn from diverse videos and support flexible control through latent action space.

---


### 188. [The Body-Algorithm-Emotion Loop: Making Emotion AI Misrecognition Visible through Artistic Practice](https://arxiv.org/abs/2610.20161)

**<font color=#1a73e8>作者：</font>** Chunyi Shen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This pictorial presents The Body in Algorithmic Colonialism, a screen-based interactive installation that critically examines Emotion-AI through artistic practice. The work uses facial tracking to simulate how commercial Emotion-AI systems translate facial movement into emotional categories and verdicts of compliance or non-compliance. Rather than treating explainability as technical transparency alone, the installation approaches XAI as an embodied encounter with misrecognition: viewers experience how the body is measured, classified, and returned to itself through algorithmic thresholds. Drawing on critical AI studies, affect theory, and practice-as-research, the pictorial positions artistic practice as a method for making affective classification visible and contestable. It documents the conceptual framework, technical process, and critical context of a prototype developed in the first year of a practice-based PhD. No audience responses, interviews, or participant data are analysed in this submission.

---


### 189. [Optimizing Sparse Boolean Rule Networks using Mixed Integer Linear Programming](https://arxiv.org/abs/2610.20170)

**<font color=#1a73e8>作者：</font>** Thomas Pammer, Johannes Fürnkranz, Markus Sinnl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning accurate and cognitively simple binary classifiers that are directly interpretable as Boolean rules. We propose mixed integer linear programming (MILP) formulations for training sparse disjunctive normal form (DNF) networks, viewed as small networks with a conjunctive hidden layer and a disjunctive output layer. Contrary to previous work that uses MILP for inductive rule learning, we start with a fixed network structure, for which we then find optimal weights. A regularized objective explicitly trades off misclassification costs against sparsity, yielding globally optimized rule sets. Our main technical contribution is an enhanced formulation that substantially reduces the number of integer decision variables and eliminates redundant constraints, while preserving exact Boolean semantics for all feasible solutions. Furthermore, we develop a combined approach based on initialization and dropout to break symmetries in the weights between rules, mitigating redundancy, and encouraging more diverse and stable rule representations. Experiments on synthetic benchmarks and UCI datasets show that the advanced formulation improves computational efficiency and achieves competitive or superior accuracy compared to established interpretable baselines, including SAT-based DNF learning and well-known rule- and tree-based learners. Overall, our approach provides a principled optimization framework for learning compact Boolean rule sets with explicit control over accuracy and sparsity trade-offs.

---


### 190. [FreeSBee: A Constant-Time Compilation Pipeline](https://arxiv.org/abs/2610.20171)

**<font color=#1a73e8>作者：</font>** Julian Ganz, David Knothe, David Oswald 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Constant-time execution is an important security property, especially for IoT devices, that prevents the leakage of sensitive information over timing side-channels. However, achieving constant-time execution is very hard when going down to the cycle level, at least on realistic devices. A lot of research is concerned with producing tools that either determine whether code is constant-time or that ensure it is compiled into a constant-time binary, with various degrees of accuracy. In this work, we present and evaluate a full workflow for hardening against timing side-channels during compilation. It starts with taint analysis to determine the code locations that depend on sensitive information. These are then the object of automated control-flow transformations inside the compiler to seal possible timing side-channels. We evaluate our workflow in detail on a realistic application running on a RISC-V core using both static timing analysis and statistical methods. Even though we do not reach cycle-accurate constant-time execution, our statistical results suggest that our hardened binary is safe against timing attacks.

---


### 191. [Secret Sharing from Non-Extractable Randomness](https://arxiv.org/abs/2610.20173)

**<font color=#1a73e8>作者：</font>** Divesh Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bosley and Dodis (TCC 2007) proved that a class of imperfect randomness sources that suffices for information-theoretic encryption of messages longer than the logarithm of the key length must admit deterministic extraction of nearly uniform bits, and asked whether the same is true of two-out-of-two secret sharing. Aggarwal, Chung, Obremski, and Ribeiro (TCC 2022) gave a positive answer for schemes that are in addition leakage-resilient or non-malleable; the original question remained open.
We answer it in the negative. For every $b\ge2$ we construct a class of flat sources on $\{0,1\}^{b+2}$, each of min-entropy at least $b$, together with a perfectly correct and perfectly private two-out-of-two scheme that shares a $b$-bit secret into two $(b+1)$-bit shares using any source in the class, and we show that every deterministic map from $\{0,1\}^{b+2}$ to $\{0,1\}$ is at statistical distance at least $1/6$ from uniform on some source in the class. This implies that sharing a long enough secret does not require extractable randomness. The proof is a short parity argument. The idea of the construction extends to other thresholds: for two-out-of-$n$ and $r$-out-of-$r$ sharing we give perfect schemes with $(b+1)$-bit shares, private for classes of flat sources from which no single bit can be extracted with error below $1/(4n-2)$ and $1/(2(2^r-1))$, respectively.

---


### 192. [When Occupation-derived Skills Don't Help: On the Limits of Skill-Augmented Career Path Prediction](https://arxiv.org/abs/2610.20186)

**<font color=#1a73e8>作者：</font>** Ege Süalp, Elena Senger, Toine Bogers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills are widely assumed to play a central role in career transitions, motivating their use in career path prediction (CPP) systems. In this work, we critically examine whether explicit skill representations provide complementary signal beyond text-based job representations. We evaluate multiple strategies for incorporating skills into CPP models, including score fusion and neural architectures, under two conditions: predicted skills and ground-truth ESCO annotations. Surprisingly, across two benchmark datasets, none of these settings yield substantial improvements over strong text-only baselines. Even when using ground-truth skills, gains remain marginal and inconsistent. Through detailed analysis, we identify key factors underlying this result: high redundancy between textual and skill representations, limited discriminative power of ESCO's taxonomy, and representational collapse in skill embeddings. Furthermore, we find that skill prediction difficulty correlates with overall sample difficulty, limiting the potential for complementary signals. Our findings challenge the common assumption that explicit skill modeling inherently benefits career prediction and suggest that dense text representations already capture most skill-relevant information.

---


### 193. [Dimension-Optimal Dynamic Regret in Exp-Concave Online Learning](https://arxiv.org/abs/2610.20187)

**<font color=#1a73e8>作者：</font>** Yanyi Li, Wendao Wu, Haihan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tracking changing comparators is a central problem in online learning. For exp-concave losses, previous work established the $T^{1/3}P_T^{2/3}$ dependence on the horizon $T$ and Euclidean path length $P_T$ for fixed dimension, while the optimal cost of dimension remained unresolved. We resolve this question by establishing a sharp $d^{1/3}$ curved dimension factor, improving the $d^{2/3}$ factor of recent switching and interval reductions [1, 2]. To achieve this improvement, we develop a proper, full-information learner on compact convex subsets of $\mathbb{R}^d$ that adapts to the unknown path length and, under fixed dimension-independent diameter, gradient, and curvature parameters, guarantees
$$\operatorname{Reg}_T(u_{1:T}) \le \widetilde{O}\left(d+\min\left\{d^{1/3}T^{1/3}P_T^{2/3},\sqrt{TP_T},T\right\}\right).$$
A matching lower bound on a diameter-one Euclidean ball establishes the minimax frontier up to logarithmic factors when $T\gtrsim d^2$, including the transition from the curved rate to larger path budgets. The lower bound already holds for losses that depend on only one coordinate per round, isolating an unavoidable cost of learning across directions. Our upper bound follows from square-root Gaussian KL control of comparator movement and a cancellation argument that pays for history restarts. The curved learner maintains $O(\log^2 T)$ Gaussian states, uses one gradient per round, and runs in time near-linear in $T$ under a Mahalanobis-projection oracle.

---


### 194. [Value-Guided Repulsion for Offline Reinforcement Learning](https://arxiv.org/abs/2610.20190)

**<font color=#1a73e8>作者：</font>** Yixue Hao, Jiahao Zhang, Jiesong Lian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drifting models have emerged as a highly efficient and stable paradigm for policy design in offline reinforcement learning (RL). However, standard drift policies determine repulsion solely from geometric relationships among generated actions and therefore cannot distinguish them by expected value. To address this limitation, we introduce Value-Guided Repulsion Q-Learning (VRQL) to integrate action value estimates into the particle interaction field. For each state, VRQL combines geometric kernel distance with a normalized Q value scaling. This mechanism assigns greater repulsive influence to particles with lower values while strictly retaining attraction toward behavior action. Consequently, this value-guided interaction field aligns behavior regularization with policy improvement without adding an auxiliary behavior model stage. On 50 OGBench task configurations and 6 D4RL AntMaze configurations, VRQL demonstrates highly competitive performance against established baselines, suggesting that value-guided particle interaction is an effective method for offline RL.

---


### 195. [What and Where in Identifying and Quantifying Conventions in Humans and AI Agents](https://arxiv.org/abs/2610.20205)

**<font color=#1a73e8>作者：</font>** Makoto Fukushima, Tim Puphal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cooperative success rests in part on implicit communication. Partners converge on conventions: regularities that give an action meaning beyond its direct effect. Yet conventions are usually observed only indirectly: a score drop when partners are swapped shows that a convention existed, but not what it was or where it was used. In the card game Hanabi, the exact probability that a play fails can be computed from the hints received and the cards in view. Players who use conventions succeed more often than this prediction allows; the resulting margin is the convention gap. Off-belief learning provides a hierarchy of agents (levels 1-5) whose first level uses no conventions by construction and whose later levels use progressively more. For humans and these agents on one scale, we ask what the conventions are and where they are used. On what: in two independently collected corpora of human games, humans show a larger gap than every agent level. On the conventions both populations use, however, humans do no better than level 2. The human advantage is concentrated in a situation that no agent level learns to use: hints that point to a card other than the ones they touch. On where: conventions depend on what the player already knows about the card, not on how recently it was hinted, and they are used most in the mid-game; humans use them earlier and later in the game than the agents. In interventions on the agents, blocking a single high-gap situation costs little, because meaning reroutes to other situations, but blocking several together costs far more than the sum of the single costs. Thus, the convention gap turns conventions from an inferred cause of score loss into a measurable, comparable, and causally testable object.

---


### 196. [HGRP: Heterogeneous Graph Neural Network for Routability Prediction](https://arxiv.org/abs/2610.20209)

**<font color=#1a73e8>作者：</font>** Yule Sheng, Yue Yuan, Shan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routability prediction enables rapid evaluation of placement quality without routing, providing effective feedback for routability-driven placement optimization. Recent machine learning methods have achieved efficient routability prediction through data-driven approach. However, their prediction performance highly depends on the capability of input representations to capture essential circuit information. To address the limitations of existing circuit representations in simultaneously preserving logical topology, physical layout and routing resource information, this paper proposes HGRP, a heterogeneous graph neural network for routability prediction. HGRP models the cells, nets, and routing grids as distinct types of nodes and explicitly represents topological connectivity, spatial mapping, and grid adjacency, thereby constructing a heterogeneous graph representation that preserves multi-level circuit semantics. Based on the representation, a heterogeneous message passing mechanism is developed to enable information interaction and feature fusion among distinct types of nodes, effectively learning the complex correlations between circuit structures and routing behaviors. Experimental results on the CircuitNet dataset show that HGRP improves F1-score by 18.69\% relative improvements compared with the state-of-the-art in the congestion prediction task. The source code is publicly available at this https URL.

---


### 197. [Robust Counterfactuals for Markov Decision Processes under Statistical and Causal Uncertainties](https://arxiv.org/abs/2610.20210)

**<font color=#1a73e8>作者：</font>** Jessica Lally, Milad Kazemi, Nicola Paoletti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Counterfactual reasoning (asking what would have happened, had a decision been different) is a powerful tool for identifying causes of failure and explaining the behaviour of AI systems in sequential decision-making tasks. In Markov Decision Processes (MDPs), two sources of uncertainty complicate counterfactual inference: statistical uncertainty in the MDP transitions when the MDP is estimated from trajectory data, and uncertainty about the unknown causal model, as there are multiple structural causal models (SCMs) compatible with each MDP. Existing work addresses these two challenges in isolation. We address both simultaneously by introducing a framework for partial counterfactual inference in MDPs that is robust to both statistical and causal uncertainty. Our approach provides: 1) closed-form analytical bounds for the counterfactual probabilities that are valid across all SCMs entailed by a given interval MDP (IMDP); 2) a method to compute minimal robust interventions to achieve a desired counterfactual outcome via pessimistic value iteration on the induced counterfactual IMDP. Since the latter is constructed using our analytical bounds, our approach remains efficient and scalable to realistic MDP environments. Experiments across multiple case studies demonstrate our method's robustness and practical utility for identifying minimal sets of actions that, if changed, would have led to improved outcomes.

---


### 198. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220)

**<font color=#1a73e8>作者：</font>** Zhuobai Dong, Junchao Yi, Hu Jian Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show it can be made dramatically more efficient. Pushing this efficiency to its extreme, we reduce trajectory supervision to a single sample, the strictest setting possible, and find that it causes severe quality collapse. We trace this to the teacher's trajectory geometry: the high-noise regime, governing semantic layout and motion, and the low-noise regime, governing fine texture exhibit fundamentally different curvature and optimization behavior, so a single monolithic student cannot jointly fit both, causing severe representation interference. Motivated by this, we propose Glance Forcing, a lightweight distillation framework that decouples the denoising trajectory into two complementary slow and fast experts, each guided by a tailored, stage-specific objective, while keeping the pretrained teacher entirely frozen. This decoupling further reveals a general mechanism underlying few-step distillation: PF-ODE distillation mainly straightens the few-step trajectory geometry, while the subsequent distribution-matching stage independently governs distributional quality. Using only one PF-ODE trajectory, Glance Forcing already surpasses the fully-trained state-of-the-art baseline, raising the VBench Total score from 84.04 to 84.22 while cutting trajectory-collection cost from thousands of GPU-hours to about one A100-GPU-hour, with markedly larger gains in dynamic degree, VisionReward, and instruction-following, and consistent preference from human raters over strong baselines.

---


### 199. [Design Space Exploration of Reinforcement Learning Configurations for Post-Legalization Placement](https://arxiv.org/abs/2610.20224)

**<font color=#1a73e8>作者：</font>** Foteini Oikonomou, Maria Pantazi-Kypraiou, George Goudroumanis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) and Reinforcement Learning (RL) have recently been explored for VLSI placement optimization, but their effectiveness for post-legalization placement refinement remains unclear. This paper presents a systematic design space exploration of a GNN-Proximal Policy Optimization (GNN-PPO) framework across three ISPD2015 benchmarks. We evaluate 18 configurations covering reward functions, GNN architectures, action spaces, candidate-set sizes, and training strategies. We analyse the results we obtain to identify pitfalls and to assess the prospects and opportunities of the RL methods for post-legalization placement. On top of that we propose a design classification approach to guide the design decisions of RL models.

---


### 200. [PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents](https://arxiv.org/abs/2610.20240)

**<font color=#1a73e8>作者：</font>** Siqi Yang, Yimu Wang, Ziqi Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view. A point-of-view (POV) video captures such changes only after they enter its field of view, whereas panoramic video records the surroundings in every viewing direction and has served as an intermediate representation of the world state in recent world models. Learning this task therefore requires synchronized POV and panoramic videos of interacting players together with their actions, yet no existing dataset provides this combination in Minecraft, an established testbed in which players act independently in a shared, modifiable 3D world. We present PAWA, a dataset and framework for action-conditioned panoramic multiplayer world modeling. The dataset pairs each player's POV video with world-stabilized panoramic video and aligned actions. Its distributed pipeline decouples CPU gameplay capture from GPU rendering, scales beyond 64 simultaneous players, and re-renders each recorded session under new observation configurations without replaying the gameplay. On this dataset, we develop a dual-tower model that jointly predicts POV and panoramic video and couples the two streams through cross-attention that aligns tokens observing the same direction in a shared world frame. We further introduce a quadratic-phase player encoding that provides many more player codes than existing rotary codes at the same embedding dimension. Experiments show that PAWA outperforms state-of-the-art multiplayer world models in POV prediction quality while also producing high-fidelity panoramic predictions. The dataset and collection pipeline are open source to support further research on multiplayer world models.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-264](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
