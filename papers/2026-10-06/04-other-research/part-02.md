# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

---

### 51. [Post-Training Quantization of Autoregressive Weather Models](https://arxiv.org/abs/2610.02511)

**<font color=#1a73e8>作者：</font>** Ananyo Bhattacharya, Swastik Bhattacharya, Christiane Jablonowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advancements in high-resolution numerical weather prediction (NWP) and data assimilation (DA) have shaped the developments in deep learning (DL) architectures emulating atmospheric dynamics. Emulators for weather forecasting exhibit forecast quality comparable to physics based models at forecast horizon scaling from few days to subseasonal time scales. The emulators are driven by hardware-accelerated matrix multiplication in autoregressive inferences, significantly reducing the computation time and resources required for NWP. Optimization of the matrix multiplication processes in GPU architectures provides opportunities to scale towards high-resolution domain, and offers implementation of out of the box solutions. Post-training quantization (PTQ) has been demonstrated across multiple DL architectures to accelerate and increase the number of computations in unit time while consuming less power, enabling applications on edge hardware. In this study, we investigate the effect of PTQ on pre-trained AI emulators for global-scale weather forecasting. We implement PTQ algorithms in Deep Learning Weather Prediction (DLWP) and FourCastNet (FCN) models as a proof of concept for geophysical fluid dynamics applications. We systematically investigate the effect of PTQ on emulator inferences over short-range forecast horizons. Evaluation of PTQ configurations using simulated quantization hints at qualitatively meaningful forecasts over short-time horizons. These results provide a first benchmark of PTQ for autoregressive weather emulators and a basis for quantization-based optimization of DL models for dynamical systems.

---


### 52. [Learning the Latent Structure: A Feature-Centric Approach to Graph Data Augmentation](https://arxiv.org/abs/2610.02517)

**<font color=#1a73e8>作者：</font>** Yu Song, Zhigang Hua, Yan Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-structured data plays a pivotal role in modeling complex relationships. However, real-world graphs are often incomplete due to data collection and observational constraints, severely limiting the effectiveness of modern graph learning pipelines. While existing Graph Data Augmentation (GDA) methods attempt to refine graph structures for improved downstream performance, they are typically label-dependent, computationally expensive, and inherently transductive, limiting their applicability in practical scenarios. In this work, we present a novel feature-centric graph data augmentation framework that bypasses explicit structure modeling by operating directly in the embedding space. Through a self-supervised inverse masking process, our method captures latent ties between observed and complete graphs, enabling recovery of unobserved structural signals through refined node representations. To enhance robustness under noisy and sparse supervision, we introduce a message regularizer and a bootstrap strategy for effective training and generalization. Evaluated on ten graph datasets spanning multiple domains, our approach, SelfAug, consistently outperforms state-of-the-art methods in both accuracy and efficiency across inductive and cold-start settings, highlighting its potential as a scalable and generalizable solution for real-world graph learning scenarios.

---


### 53. [Instance-Dependent Regret for CMDPs with Step-Wise Constraints](https://arxiv.org/abs/2610.02520)

**<font color=#1a73e8>作者：</font>** Qian Zuo, Francesco Emanuele Stradi, Leyang Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online learning in episodic tabular constrained Markov decision processes with step-wise safety constraints. In such a setting, the constraints induce a safe subgraph that shapes the variance of cumulative rewards under feasible policies and, consequently, the difficulty of learning. Exploiting this structure, however, requires learning which actions are safe while controlling constraint violations. We propose Safe Variance-Adaptive Exploration (SVAE), an efficient algorithm that learns candidate safe subgraphs and performs variance-adaptive optimistic planning within them. With high probability, SVAE achieves cumulative regret of order $\widetilde{\mathcal{O}}(\sqrt{SAH\min\{\mathbb{V}_\Sigma,K\mathrm{Var}^{\star}\}}+S\sqrt{AH^3\min\{K,\mathcal{C}\}}+S^2AH^2)$ over $K$ episodes, where $H$ is the horizon of a single episode, while $S$ and $A$ are the numbers of states and actions, respectively. Here, $\mathrm{Var}^{\star}$ is the maximum return variance among safe policies, $\mathbb{V}_\Sigma$ is the variance accumulated before the first unsafe action is encountered, and $\mathcal{C}$ captures the statistical complexity of eliminating actions incorrectly considered potentially safe. SVAE additionally attains $\widetilde{\mathcal{O}}(H\sqrt{SAK}+S^2AH^2)$ step-wise constraint violation and a gap-dependent violation bound that is polylogarithmic in $K$. Finally, we establish a lower bound showing that dependence on these instance-specific quantities is unavoidable.

---


### 54. [BaCP: Backbone Contrastive Pruning for Preserving Representations in Extremely Sparse Neural Networks](https://arxiv.org/abs/2610.02524)

**<font color=#1a73e8>作者：</font>** Mohammad Haroon Khawaja, Muhammad Haseeb, Mohammad Fatim Shoaib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unstructured pruning at extreme sparsity often suffers from representational collapse, causing sharp drops in accuracy. To address this, we study Backbone Contrastive Pruning (BaCP), which regularizes the sparse network's embedding space by aligning it with pretrained, fine-tuned, and historical snapshot models. Building on the contrastive decomposition of the CAP framework (Xu et al., 2022), we provide a rigorous matched-budget characterization of this approach across multiple pruning criteria. Evaluated across 90 settings, BaCP improves accuracy substantially in extreme sparsity regimes where standard pruning fails, and is close to baseline where representations remain intact.

---


### 55. [Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents](https://arxiv.org/abs/2610.02525)

**<font color=#1a73e8>作者：</font>** Ankur Samanta, Yonathan Efroni, Paul Sajda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon research agents must decide both how to investigate and what to investigate next as evidence accumulates. This is hard to learn because such decisions are sparse in long execution traces, and their consequences may emerge several investigations later. We introduce Meta-reasoning for Iterative Research Agents (MIRA), a hierarchical architecture separating research allocation from execution. An outer-loop meta-reasoner curates context from a persistent research record, then writes a work order for the next investigation or ends the episode. A fresh inner-loop executor carries out each work order, making execution part of the transition between meta-reasoning actions. Without policy training, MIRA improves long-horizon inference and allocates additional compute more effectively in theorem proving and open-ended neural-architecture research. Its decision boundaries also provide natural units for credit assignment. At each boundary, we train a generative critic to forecast expected remaining return from partial states, outperforming token-level alternatives. Cross-environment pretraining improves forecasting and adaptation, yielding a transferable prior for valuing partial progress. We use this prior to initialize MIRA-AC, a generative actor-critic jointly trained to forecast remaining return and choose the next investigation, without a separate critic model. MIRA-AC concentrates policy optimization on meta-reasoning decisions, enabling efficient long-horizon reinforcement learning without directly optimizing the longer execution traces they initiate. Training MIRA-AC on the model's own proxy hill-climbing signals improves gold performance across four autoresearch environments; the actor transfers with cross-environment value initialization. Together, these results show that meta-reasoning can be learned as an explicit policy for directing long-horizon autonomous research.

---


### 56. [Autoregressive Differentiable Method for Integer Programming](https://arxiv.org/abs/2610.02528)

**<font color=#1a73e8>作者：</font>** Ouns El Harzli, Yudong Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce an autoregressive differentiable method to solve 0-1 integer programs. We fix an arbitrary order of the binary variables and we train a transformer to predict the next bit while remaining in the feasible set. Our method is first trained on feasible incumbents provided by any solver, thus allowing us to initialize the transformer in the feasible set. Our procedure then implements a Lagrangian penalty to penalize infeasible solutions, and the transformer is further trained to explore the feasible set using Gumbel-softmax activations on the relaxed objective. We have tested our method on non-convex instances of quadratic knapsack problem and demonstrated consistent improvement upon state-of-the-art open-source solvers for dense problems up to 10,000 binary variables. In particular, we empirically demonstrate a phenomenon akin to a tunneling effect where the effective change of variables from binary variable to the continuous weights of the transformer that the method implements enables crossing barriers in the relaxed objective landscape.

---


### 57. [A generative-informed neuro-symbolic framework for syntactic ambiguity resolution: Evidence from Arabic DPs](https://arxiv.org/abs/2610.02529)

**<font color=#1a73e8>作者：</font>** Mohammed Damom, Muneef Y. Alshawsh, Ashraf A. Naji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Syntactic ambiguity poses a persistent challenge for Arabic NLP, particularly in morphologically rich nominal constructions where multiple structu6ral interpretations may be compatible with the same surface sequence. This study proposes a generatively informed neuro-symbolic framework for resolving structural ambiguity in Modern Standard Arabic (MSA) DPs. The framework integrates generative syntactic notions with AraBERT by representing ambiguity as a candidate-based decision task in which linguistically motivated alternatives are explicitly constructed and evaluated through candidate-conditioned input representations. Findings indicate that the model achieved 96.88% accuracy, 95.92% macro-F1, 96.83% weighted F1, and 93.94% binary F1 on the unseen evaluation set. Class-level analysis revealed asymmetric performance, with recall of 99.71% for High/VP Attachment (N1) and 89.26% for Low/NP/Embedded Attachment (N2), indicating greater difficulty in recovering the embedded interpretation. The study concludes that formal syntactic representations can be operationalized within Transformer-based NLP as an explicit interface between linguistic structure and contextual neural modeling, providing a controlled and interpretable approach to Arabic syntactic ambiguity resolution and beyond.

---


### 58. [Reward Inflation: A Healthy Stimulus for Reinforcement Learning](https://arxiv.org/abs/2610.02545)

**<font color=#1a73e8>作者：</font>** Ganghun Lee, Minji Kim, Minsu Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward serves as the primary learning signal in reinforcement learning (RL). However, while reward magnitudes are typically held fixed throughout training, their temporal modulation remains underexplored. In this paper, we propose reward inflation, a gradual scaling of rewards over the course of training, and show that it can act as a healthy stimulus for RL. Theoretically, reward inflation induces an implicit recency weighting that upweights recent transitions during policy updates, enabling faster adaptation. We further show that, by sustaining gradient signals as the policy saturates, reward inflation suppresses the emergence of dormant neurons and helps preserve plasticity. Empirical results on ALE games and MuJoCo tasks corroborate these findings, showing that an appropriate level of reward inflation benefits a broad range of tasks. Finally, we introduce Fed, an adaptive variant that adjusts the inflation level on the fly, and find that it often improves upon fixed inflation.

---


### 59. [Out of Sync, Out of Sight: Phantom State Attacks against IIoT Intrusion Detection](https://arxiv.org/abs/2610.02552)

**<font color=#1a73e8>作者：</font>** Sabrine Ennaji, Elhadj Benkhelifa, Nadia Kabachi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems (IDS) are critical for securing Industrial Internet of Things (IIoT) environments. Most adversarial research against them perturbs the feature vector or the traffic that produces it, and depends on gradient access, repeated model queries, or a learned model of benign traffic. A smaller line of work reshapes packet timing without querying the detector, but makes malicious traffic mimic a learned model of benign timing. Across these approaches, one assumption of industrial monitoring pipelines has received little attention: temporal synchronization. An IDS reconstructs operational state by aggregating telemetry into sliding or tumbling windows, so its view depends not only on what is observed but on when each observation falls relative to a window boundary.
We introduce the Phantom State Attack (PSA), which exploits that dependence under a passive, zero-query threat model. Rather than modifying packets, perturbing features, querying the classifier, or fitting any model of benign traffic, PSA injects bounded timing drift calibrated to the attack flow's own inter-arrival variability, moving observations across the nearest window boundary by the minimal shift needed. The IDS then reconstructs a phantom state that diverges from the true process state.
We evaluate PSA on ToN-IoT and CIC IIoT 2025 (DataSense), against Random Forest, MLP and XGBoost, measuring detection degradation, synchronization distortion, stealth, and attacker cost. PSA degrades detection on flows carrying enough packets for window-boundary redistribution, and leaves others almost unchanged, so its effect is conditional. A query-based baseline reaches higher raw success but needs many queries per window, while PSA needs none. The results identify temporal aggregation as an attack surface reachable under weaker assumptions than prior evasion techniques.

---


### 60. [How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate](https://arxiv.org/abs/2610.02557)

**<font color=#1a73e8>作者：</font>** Jiawei Li, Zhiyang Xun, Lijie Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As powerful AI systems reach and sometimes surpass the abilities of human experts across a range of cognitively demanding tasks, the problem of accurate oversight and supervision of these systems has become increasingly urgent. One promising approach is AI debate, which seeks to leverage a debate between two powerful AIs to break complex questions down into simpler claims that can be easily judged directly. Theoretical work on debate has formalized this intuition in the language of computational complexity theory, where the goal is to design protocols (i.e., rules of the debate game) that provide rigorous guarantees on correctness for judging solutions to complex problems with limited supervision. Specifically, the current best protocol has been shown to work for all problems that have sufficiently stable decompositions into subproblems. In this paper, we design a new protocol for this same class of problems that improves on the prior work in several ways. First, correctness holds in a worst-case rather than an average-case sense. Second, being honest and correct is a dominant-strategy equilibrium for both debaters, rather than a Stackelberg equilibrium. Finally, we prove black-box lower bounds, showing that our new protocol is instance-wise optimal. That is, no protocol for this class of problems can outperform ours while making only black-box queries to human judgments. We obtain these results by relating the notion of stable problem decompositions to the concept of fractional block sensitivity from query complexity.

---


### 61. [Neuron merging via inverse-activation regression for post-training compression of sigmoid neural networks](https://arxiv.org/abs/2610.02559)

**<font color=#1a73e8>作者：</font>** Ao Kuniya, Jun Ohkubo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As neural networks continue to grow in scale, model compression is becoming increasingly important for efficient inference under limited computational resources. Structured pruning methods remove neurons or channels that are estimated to be less important, but the removed units may still contain useful information. From the viewpoint of coarse-graining a trained network, it is valuable to ask which information should be retained when multiple neuronal degrees of freedom are consolidated. In this paper, we discuss cluster-based merging methods for compression of trained neural networks. In addition to a data-free contribution-weighted averaging method, we propose neuron-merging methods in which neuron responses are mapped back to the pre-activation space via the inverse activation function, and the weights and biases of each representative neuron are estimated using the least-squares method. We also examine both a data-assisted strategy with actual training inputs and a data-free strategy using randomly generated inputs. The comparisons provide empirical evidence, in the tested sigmoid networks, that weight information is particularly useful for clustering whereas activation information is useful for representative-neuron reconstruction in the merging process.

---


### 62. [Oracle headroom without signal: null-calibrated evaluation of candidate selection for thermal heart rate estimation](https://arxiv.org/abs/2610.02561)

**<font color=#1a73e8>作者：</font>** Mohammad Rakibur Rahman, Nhi Nguyen, Sasan Sharifipour 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based physiological monitoring can produce multiple estimates from several facial regions, extraction methods, and processing settings. Signal quality indices aim to select reliable estimates without a physiological reference, and their potential is often assessed with an oracle that selects the estimate closest to the reference in each window. This retrospective selection can reward chance agreement. We model the effect with order statistics. For K independent candidates unrelated to the reference, the expected oracle error decreases approximately as 1/K. We analyze thermal heart rate estimation on 96 iBVP recordings with 168 candidates per 10 s window. The oracle achieves a mean absolute error of 0.91 bpm, compared with 10.74 bpm for the best fixed configuration, 18.03 bpm for the best quality index, and 8.61 bpm for a constant predictor. With K = 24, a forehead signal from another recording matches the correct one, with 4.62 against 4.61 bpm. Oracle evaluations should report candidate count, valid coverage, and matched null controls.

---


### 63. [Santiago's A.T. Field: Visualizing Urban Accessibility through an Evangelion-Inspired Interface](https://arxiv.org/abs/2610.02562)

**<font color=#1a73e8>作者：</font>** Eduardo Graells-Garrido, Ignacio Pérez-Messina, Claudio Gaete  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Science-fiction interfaces are often reproduced for their appearance, and their diagnostic logic is rarely rebuilt around real data. Here we describe Santiago's A.T. Field, an interactive visualization of urban accessibility built from a diagnostic interface in Episode 13 of Neon Genesis Evangelion. We translated that interface in five stages: phenomenon, field, progression, interface, and response. A microscopic Angel became a relational urban problem, and a fictional scanning lattice became an accessibility field computed with the E2SFCA method. Every element of the fictional display is tied to a quantity of the model. Three tensions appeared when we made the fictional language operational: the saturated palette of the genre against color-vision deficiency, the motion of the genre against the reduced-motion preference, and the per-frame cost of the animation. The urgency of the fictional command center has its own cost, because emergency aesthetics can cast urban populations as threats. These three tensions are what the translation cost, and they are what transfers to other attempts of this kind.

---


### 64. [DAGS: Disentangled Appearance-and-Geometry Steering of a Frozen Image DiT for Temporally Stabilized Generative Rendering](https://arxiv.org/abs/2610.02567)

**<font color=#1a73e8>作者：</font>** Karthik Mohan Kumar, Damian Andrysiak, Pedro Antonio Pena 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) generate high-fidelity images from text and image conditions, but their outputs carry large variance and their faithfulness to a desired target depends heavily on how the condition is supplied. We present DAGS, a lightweight, attention-free, disentangled appearance and geometry conditioning scheme that steers a frozen image DiT to produce high-fidelity, highly faithful, and independently controllable renders. Two small convolutional encoders compute conditioning features once per frame and inject them as a learned, per-layer, element-wise residual into the image tokens, avoiding the quadratic cost of stacking conditions through attention. Because control and temporal handling live outside the frozen backbone, we retain its vast pretrained prior and eliminate backbone-overfitting risk. We further add a small recurrent lighting stabilizer and a training-free temporal guidance term that, coupled with our conditioning, elevate a per-frame image model into a streaming renderer. DAGS produces controllable, high-quality renders at a fraction of the compute of path tracing; it is not real-time, trading compute for controllability and quality. On a matched 1-spp + G-buffer input, per-frame DAGS reconstructs +8.6 dB / +10.1 dB PSNR over the real-time denoiser Intel OIDN and the diffusion renderer RGB<->X while being 2.5-8x more temporally stable perceptually (temporal-LPIPS flicker).

---


### 65. [Physical AI Smart Spaces: A Large-Scale Benchmark for Multi-Camera 3D Perception in Smart Spaces](https://arxiv.org/abs/2610.02580)

**<font color=#1a73e8>作者：</font>** Yuxing Wang, Yizhou Wang, Anqi Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical AI Smart Spaces is, to the best of our knowledge, the first benchmark to simultaneously provide large-scale, multi-class, and multi-camera 3D perception data for indoor smart spaces. It contains over 280 hours of synchronized 1080p footage captured by nearly 1,800 cameras in warehouses, hospitals, retail venues, and similar settings, together with automatic annotations for multi-camera identities, 2D bounding boxes, 3D bounding boxes, camera calibration, and depth where available. The benchmark spans Isaac Sim synthetic generation, Cosmos Transfer appearance augmentation, and real-world Sim2Real evaluation. For the real-world target, we include two warehouse deployments with time-synchronized streams, automatic VGGT-based calibration, and a 3D labeling interface that projects world-frame 3D boxes into each view for cross-camera verification. We describe the dataset scope, annotation and calibration schema, generation workflow, benchmark protocols, and official evaluation system, which standardizes submission format, and leaderboard reporting. A central contribution is a 3D instantiation of Higher Order Tracking Accuracy (HOTA), extending the usual 2D box-based tracking evaluation to 3D locations and 3D boxes. We further report empirical baselines from the AI City Challenge leaderboards, showing how methods evolve from person-only 3D location tracking to multi-class 3D box tracking under realistic smart-space constraints. The release is available at this https URL.

---


### 66. [Effects of a Behavioural Commitment Scheme on Study Regularity in a Self-Paced Learning Platform](https://arxiv.org/abs/2610.02595)

**<font color=#1a73e8>作者：</font>** Meenakshi V., Pavani Ayinampudi, Aditya B. M. V. 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online education has enabled learners worldwide to take up courses from reputed institutions. However, a self-paced online course cannot guarantee the motivation and engagement that a learner experiences in a real-time classroom. Self-paced access also makes platform load unpredictable, which drives up the compute cost. We propose a Commitment Scheme for course access that aligns learner commitment with platform capacity. Learners book their study slots in advance; the instructor sets the budget of learning hours available for the course; and learners who use a full window earn additional watch hours. A booked window records an intention to study at a stated time, and a learner who appears in that window implements it. The byproduct is a platform load that can be forecast and bounded. The study involved two courses taken in sequence by the same learners, with the slot booking system activated only in the second. In-window study was observed on 86.8% of booked windows, and the median committer placed 95.5% of all study time inside self-booked windows. Among learners who studied across the launch, study regularity improved from 1.01 to 1.33 active days per week, with a supporting difference of +1.37 days per week against the same learners' preceding course. Commitments made on the same day as the study slot were honoured more often than advance bookings (88.8% against 62.5% two days ahead), which is consistent with the classic intention-behaviour gap.

---


### 67. [TasteBench: Multimodal Benchmark for Sensory Prediction, from Molecules to Sustainable Foods](https://arxiv.org/abs/2610.02599)

**<font color=#1a73e8>作者：</font>** Anna T. Thomas, Sohum Patnaik, Caroline Cotto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustainable protein discovery lacks the fast computational proxies, analogous to molecular docking or density functional theory, that accelerate drug and materials discovery. Evaluating whether a novel food tastes like its animal-based target requires expensive human sensory panels, bottlenecking the design-build-test loop. We introduce TasteBench, a multimodal benchmark and privacy-preserving competition for sensory prediction, spanning two tasks: a food-level ranking task built on 21K+ human evaluations across 215 plant-based foods in 24 product categories, yielding 935 within-category ranking pairs, and a supporting molecular-level taste classification task over 15K flavor molecules. To enable rigorous interpretation of model performance, we characterize the ground truth: inter-rater agreement among panelists is low (Krippendorff's $\alpha = .077$), and the split-half reliability ceiling of panel-aggregated rankings is .825, establishing the range within which ML systems on this benchmark should be assessed. We evaluate baselines across four input modalities; on the same pairs panelists rated, the best model achieves .661 pairwise accuracy, competitive with the median individual panelist (.650), and .683 across all within-category pairs. TasteBench provides the evaluation infrastructure and baselines for measuring progress on computational screening for sustainable protein discovery.

---


### 68. [Time Series Forecasting Benchmarks Need Scenario-Grounded Stress Testing](https://arxiv.org/abs/2610.02608)

**<font color=#1a73e8>作者：</font>** Yuyang Zhao, Lian Xu, Hao Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting (TSF) increasingly drives decisions in transportation, energy, finance, healthcare, and infrastructure, yet current evaluation remains overly narrow: standard benchmarks reward low held-out error, while robustness studies typically reduce failure to Gaussian noise, random masking, or bounded adversarial perturbations. This obscures the real failure modes of deployed forecasting systems. Input-side anomalies are not merely noisier inputs: they often reflect structured events that alter temporal dynamics, break cross-variable dependencies, induce regime shifts, or propagate from faulty sensors to downstream decisions. These semantic, causal, and system-level failures cannot be faithfully captured by i.i.d. perturbations alone. The rise of TSF foundation models makes this evaluation gap more urgent, as unauditable pretraining corpora make held-out generalization increasingly unreliable. We therefore advocate scenario-grounded stress testing. Each test instance should include historical inputs and future targets, together with a semantic scenario, an explicit failure operator, and a measurable difficulty level. This shift makes evaluation interpretable, attributable, and deployment-relevant and friendly, enabling the community to ask not only which model is accurate, but under what conditions it fails and why.

---


### 69. [Seer: Maximum Likelihood Regression for Learning-Speed Curves](https://arxiv.org/abs/2610.02610)

**<font color=#1a73e8>作者：</font>** Carl Myers Kadie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The research presented here focuses on modeling machine-learning performance. The thesis introduces Seer, a system that generates empirical observations of classification-learning performance and then uses those observations to create statistical models. The models can be used to predict the number of training examples needed to achieve a desired level and the maximum accuracy possible given an unlimited number of training examples. Seer advances the state of the art with 1) models that embody the best constraints for classification learning and most useful parameters, 2) algorithms that efficiently find maximum-likelihood models, and 3) a demonstration on real-world data from three domains of a practicable application of such modeling.
The first part of the thesis gives an overview of the requirements for a good maximum-likelihood model of classification-learning performance. Next, reasonable design choices for such models are explored. Selection among such models is a task of nonlinear programming, but by exploiting appropriate problem constraints, the task is reduced to a nonlinear regression task that can be solved with an efficient iterative algorithm. The latter part of the thesis describes almost 100 experiments in the domains of soybean disease, heart disease, and audiological problems. The tests show that Seer is excellent at characterizing learning-performance and that it seems to be as good as possible at predicting learning performance. Finally, recommendations for choosing a regression model for a particular situation are made and directions for further research are identified.

---


### 70. [Scale-Recursive Rectified Flows for Few-Step Precipitation Ensembles](https://arxiv.org/abs/2610.02611)

**<font color=#1a73e8>作者：</font>** Shunya Nagashima, Takumi Bannai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-resolution precipitation estimates support flood risk assessment and water management, but coarse satellite products cannot resolve rainfall within each grid cell. Generative models address this ambiguity by producing ensembles of plausible high-resolution rainfall fields. Among these models, rectified flows generate samples by iteratively transforming random noise into rainfall fields. Reducing the number of sampling steps accelerates generation but can make ensemble members too similar, understating uncertainty. We propose a scale-recursive rectified flow that generates broad patterns before local details and guides sampling-step allocation by comparing ensemble variability with prediction error across spatial scales. Validation scores and rainfall power spectra constrain the allocation to avoid excessive amplification. In satellite-to-radar downscaling over the contiguous United States, our analysis identified broad rainfall patterns as the main source of insufficient ensemble variability under reduced sampling budgets. Allocating more steps to the coarse flow improved probabilistic accuracy and rain detection across training seeds at fixed architecture and computational cost. The proposed model also achieved better probabilistic accuracy with shorter sampling time than a nonrecursive flow using more steps.

---


### 71. [Quantifying the Value of Constructive Induction, Knowledge, and Noise Filtering on Inductive Learning](https://arxiv.org/abs/2610.02615)

**<font color=#1a73e8>作者：</font>** Carl M. Kadie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning research, as one of its central goals, tries to measure, model, and understand how learning-problem properties affect average-case learning performance. For example, we would like to quantify the value of constructive induction, noise filtering, and background knowledge. This paper describes the effective dimension, a new learning measure that helps link problem properties to learning performance. Like the Vapnik-Chervonenkis (VC) dimension, the effective dimension is often in a simple linear relation with problem properties. Unlike the VC dimension, the effective dimension can be estimated empirically and makes average-case predictions. It is therefore more widely applicable to machine and human learning research. The measure is demonstrated on several learning systems including Backpropagation. Finally, the measure is used to precisely predict the benefit of using FRINGE, a feature construction system. The benefit is found to decrease as the complexity of the target concept increases.

---


### 72. [Capturing Dynamics: The 4D Facial Expression Intensity Dataset](https://arxiv.org/abs/2610.02647)

**<font color=#1a73e8>作者：</font>** Zesheng Wang, Alexandre Bruckert, Pierre Lebreton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The estimation and analysis of facial expression intensity play a crucial role in affective communication and human-computer interaction. Previous research has primarily focused on detecting and estimating facial expression intensity from frame-level 2D representations. However, this limitation restricts a comprehensive understanding of real-world facial expressions, as they are inherently 3D and temporally continuous. This paper investigates the perception of facial expression intensity by introducing the 4D Facial Expression Intensity Dataset (4DFEID). We employ a parametric face model and compile a total of 2,869 mesh sequences with controlled geometric variations, generating 4D data instances with diverse peak intensities and identity attributes. Using a Likert scale, we collect more than 90,000 subjective intensity perception ratings via a crowdsourcing platform. We explore various architectures and aggregation methods to establish baselines for episode intensity estimation on the new dataset, revealing that spatial-temporal graph models consistently outperform traditional frame-aggregation methods. In contrast to existing datasets that rely on 2D static imagery, the proposed 4D-FEID dataset provides the community with a unique and vital resource for investigating the perception of facial expression intensity through the use of dynamic 3D stimuli. By offering high-fidelity, spatio-temporally coherent facial data, 4D-FEID establishes a new foundation for research into more nuanced and naturalistic expression analysis, thereby addressing a gap in the current landscape of affective computing and human-computer interaction studies. The dataset is available at link.

---


### 73. [Distributed Learning with Selective State Space Models: Architecture-Aware Convergence Analysis](https://arxiv.org/abs/2610.02659)

**<font color=#1a73e8>作者：</font>** Adam Piaseczny, Md Kamran Chowdhury Shisher, Shiqiang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern state space models (SSMs), such as Mamba2, provide a compelling alternative to transformers by combining linear-time sequence modeling with recurrent state-space dynamics. However, the behavior of SSMs in distributed learning settings remains poorly understood. In particular, the existing standard federated learning methods are largely architecture-agnostic, and do not account for the stability, selectivity, and state-space parameterization that characterize modern selective SSMs. To address this, we derive architecture-aware gradient and smoothness bounds for single- and multi-layer selective SSMs, and convergence bounds for FedAvg and FedProx, characterizing how recurrent stability, input-dependent discretization, and state projection norms affect federated optimization. We then numerically validate the single-layer bounds on sequences generated by a teacher SSM, using a learner that follows the analyzed recurrence. We use this analysis to formulate expectations about the effects of local training and client heterogeneity, and examine these expectations by comparing nine federated learning algorithms on Mamba2 language modeling across six text domains. These experiments illustrate how SSM-specific bounds can provide a basis for interpreting the behavior of practical federated learning algorithms.

---


### 74. [SpectralCache: Accelerating Diffusion-Based World Models via Spectral Feature Caching](https://arxiv.org/abs/2610.02660)

**<font color=#1a73e8>作者：</font>** Zhendong Mi, Pu Zhao, Ziyu Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based world models enable high-quality interactive environment generation but suffer from substantial inference overhead due to repeated Transformer evaluations during denoising. Existing caching methods mainly exploit temporal redundancy at the feature or token level, leaving the underlying mathematical structure of diffusion features largely unexplored. In this work, we reveal that world-model features exhibit highly stable singular subspaces across nearby denoising steps, while their singular values follow predictable evolution patterns. Building on this observation, we propose SpectralCache, a training-free spectral caching framework that reuses stable singular subspaces and estimates only low-dimensional singular values through linear extrapolation. We further exploit the spectral consistency between neighboring full-computation features to skip selected expensive backbone evaluations via singular value scaling. Extensive experiments on representative world models demonstrate that SpectralCache consistently improves inference efficiency while preserving generation quality. On HunyuanWorld-Voyager-13B, SpectralCache achieves 5.22x acceleration while maintaining a WorldScore of 65.90 for static scenes, substantially outperforming existing training-free caching methods in inference efficiency.

---


### 75. [AIGS: Adaptive Incremental Gating System for Online Representation Learning in Non-Stationary Data Streams](https://arxiv.org/abs/2610.02661)

**<font color=#1a73e8>作者：</font>** SiRui He, Kai Liang Lew, Chui Zi Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time data streams in Web of Things (WoT) and edge computing environments often evolve through latent regime changes. For online representation learning under strict computational constraints, the central problem is resolving the stability-plasticity dilemma: keeping useful historical knowledge while rapidly reacting to concept drift. Existing methods employ fixed update schedules or rolling windows. However, they suffer from parameter ossification during sudden shifts and waste computational resources when the stream remains stable. This paper proposes the Adaptive Incremental Gating System (AIGS), a lightweight closed-loop state-aware adaptation framework. AIGS introduces the Shock Ratio, an endogenous residual feedback mechanism that normalizes current reconstruction error against recent variation. This signal drives a Continuous Plasticity Controller that smoothly interpolates between learning plasticity and memory retention. By treating representation learning as a closed-loop control mechanism, AIGS avoids catastrophic forgetting and maintains a strictly linear $\mathcal{O}\left(k\cdot d\right)$ per-step complexity suitable for latency-sensitive edge devices. Experiments on real-world smart city dynamic streams-spanning traffic networks, meteorological systems, and industrial infrastructure-demonstrate distinct domain-dependent advantages. On Electricity Transformer Temperature datasets, AIGS achieves preventative early-warning lead times of 8.31 (ETTm1) and 9.88 (ETTm2) steps under gradual degradation. On Performance Measurement System traffic datasets, it shows significantly faster post-shift recovery after abrupt mutations. On the highly noisy Weather dataset, it improves anomaly recall while resisting stochastic noise overfitting. These findings establish AIGS as a practical, plug-and-play adapter for resource-constrained edge monitoring systems.

---


### 76. [Mind the Refinement Gap: When Safe High-Level Robot Plans Produce Unsafe Executions](https://arxiv.org/abs/2610.02662)

**<font color=#1a73e8>作者：</font>** Stabak Das, Priyesh Ranjan, Xiangfang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-enabled robot systems increasingly combine semantic-graph planning with temporal-logic safety monitors. We investigate a trace-completeness assumption in these systems: whether the high-level action sequence checked by a monitor represents the navigation and implicit action effects induced during execution. We audit this assumption in RoboGuard by comparing its verdict on a surface plan with its verdict on a graph-refined trace under the same Linear Temporal Logic (LTL) specification. Our evaluation comprises 28 controlled cases spanning five action-abstraction families and 14 end-to-end cases in which SPINE [1] generates plans from natural-language instructions while RoboGuard generates scene-grounded safety specifications. In the controlled evaluation, all 12 targeted abstraction cases exhibit the predicted surface-versus-refined discrepancy while all 16 controls behave as expected, motivating graph-based trace refinement as a lightweight mitigation and a diagnostic tool for physical-AI safety monitors.

---


### 77. [Label-Efficient Time Series Classification at Scale: A Dual-Stream OSSE-LSTM with Counterfactual Attribution](https://arxiv.org/abs/2610.02704)

**<font color=#1a73e8>作者：</font>** Nguyen Ho, Bach Tung Tran, Trung Ky Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series are produced continuously at enormous scale by industrial equipment, wearables, power grids, and clinical monitors, yet annotation remains manual, expensive, and expert-dependent. The binding constraint in large-scale time series analytics is therefore not data volume but label volume, and the question facing a practitioner is concrete: how many examples per class must be labeled before a classifier becomes usable? We study this question directly, in a regime where the label space is fixed and known in advance and the decision rule must be constructed from only K labeled examples per class. We propose Dual-Stream OSSE-LSTM, an episodic metric-learning framework that pairs an Omni-Scale CNN with Squeeze-and-Excitation recalibration, for multi-scale motif extraction without per-dataset kernel tuning, with a Bidirectional LSTM for global temporal context. The two streams are independently normalized and fused into a prototype-oriented embedding. Because decisions taken from a few labels must also be explainable, we introduce Counterfactual Integrated Gradients (C-IG), which attributes the prototype margin between target and opposing classes rather than an isolated classifier logit, and reuses the resulting maps as soft masks for test-time prototype refinement without updating the encoder. On 19 univariate UCR datasets, OSSE-LSTM attains the highest average accuracy and per-dataset win count at every support size, and its accuracy remains within a 0.36-point band (96.36-96.72%) across that range. Its weakest configuration still exceeding the best result any compared baseline achieves at any K (93.99%).

---


### 78. [Characterizing the Performance Gap in Human Activity Recognition for Older Adults](https://arxiv.org/abs/2610.02711)

**<font color=#1a73e8>作者：</font>** Hossein Khayami, Sungjin Hwang, Eshed Ohn-Bar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) from wrist-worn accelerometers is increasingly used for health and behavioral tracking. Yet, most wearable HAR models are developed and evaluated on datasets dominated by younger adults, leaving it unclear whether benchmark progress generalizes across age groups. In this work, we leverage MyMove, our carefully annotated, free-living older-adult HAR dataset (mean age 71), to evaluate deep-learning architectures and training regimes under both leave-one-subject-out and cross-dataset transfer. We find that improvements on younger-adult benchmarks fail to transfer equally to data collected from older adults, resulting in a persistent and often widening performance gap. However, richer representations, particularly frozen self-supervised features pretrained on the age-diverse UK Biobank dataset, substantially improve performance on data from older adults and consistently narrow the performance gap, at modest cost to younger-adult performance, though disparities remain. These findings suggest that benchmark gains and architectural scaling alone provide an incomplete picture of progress in wearable HAR, and broader advances may require representations that better capture population diversity, alongside personalized adaptation to individual movement patterns and routines.

---


### 79. [Differential Privacy of Gradient Descent on Perturbed Objectives](https://arxiv.org/abs/2610.02716)

**<font color=#1a73e8>作者：</font>** Austin Watkins, Raman Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective perturbation adds a random linear term to a regularized empirical risk and releases the exact perturbed minimizer. We study the finite computation obtained by releasing the $N$-th iterate of deterministic gradient descent on $w\mapsto F(w;S)+\langle z,w\rangle$, where $z\sim\mathcal N(0,\sigma^2I_d)$ is drawn once before optimization. For strongly convex and smooth objectives with Lipschitz Hessian, we prove an explicit condition under which the map $z\mapsto w_N$ is a $C^1$-diffeomorphism on the bounded domains used in the privacy argument, with a quantitative lower bound on the smallest singular value of its Jacobian. This permits a direct change-of-variables analysis of the finite iterate. For generalized linear models, the resulting privacy-profile bound has no explicit ambient-dimension factor once the iteration condition holds, and its finite-iteration correction decreases geometrically. By letting the free truncation parameter grow slowly with $N$, we recover the corresponding exact-minimizer certificate in the limit. We also bound the expected excess empirical risk by $d\sigma^2/(2\mu)$ plus a geometrically decreasing optimization term, and transfer the result to population risk without an additional multiplicative condition-number factor in the leading statistical terms.

---


### 80. [Structural-Functional Brain Connectivity Generation via Multimodal Hypergraph-based Flow Matching](https://arxiv.org/abs/2610.02722)

**<font color=#1a73e8>作者：</font>** Chyong Yi Poh, Hwa Hui Tew, Junn Yong Loo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural connectivity (SC) and functional connectivity (FC) provide complementary information on interactions between brain regions and are widely used in neuroimaging studies of neuropsychiatric disorders. Generative modelling can alleviate the scarcity of large-scale paired SC-FC data, but existing approaches typically use pairwise graphs that capture only dyadic interactions and often generate SC and FC independently, limiting preservation of higher-order structure-function relationships. We propose a Multimodal Hypergraph Flow Matching (MHG-FM) framework for joint SC-FC connectivity generation and cross-modal translation. MHG-FM constructs modality-specific hypergraphs, learns higher-order representations with Hypergraph Neural Network (HGNN) encoders, and performs bidirectional cross-modal fusion using Dual Cross-Attention (DCA). A variational autoencoder maps the fused representations to a compact latent space, where conditional flow matching enables connectivity synthesis and multimodal translation via latent transport. Experiments on the Human Connectome Project Young Adult (HCP-YA) dataset show that MHG-FM outperforms several state-of-the-art baselines in reconstruction quality, topology preservation, distributional similarity, and SC-FC coupling, while achieving approximately 8x faster sampling than a matched diffusion backbone.

---


### 81. [SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726)

**<font color=#1a73e8>作者：</font>** Xi Ye, Yuzhu Wang, Xiaoyang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-matching-based multi-view world models generate realistic videos, but are commonly restricted to fixed camera rigs. Extending them to continuously varying camera poses requires paired pose--video observations with dense pose coverage, which are costly to acquire. We introduce \emph{SymRegFlow}, a symmetry-regularized flow-matching framework for multi-view-consistent video generation across continuous viewpoints without ground-truth novel-view RGB supervision. For each target pose, SymRegFlow geometrically warps source views into noisy anchors and combines masked dual-anchor supervision with cross-anchor denoising-output consistency to mitigate anchor-specific errors. Under an affine Gaussian surrogate, we prove that suitable consistency regularization recovers the clean-reference optimum at fixed noise levels, strictly outperforming single- and merged-anchor baselines. Experiments on Cosmos-Drive-Dreams and nuScenes demonstrate high-quality, multi-view-consistent autonomous-driving video generation: on nuScenes, SymRegFlow achieves the lowest FVD and FVMD among the evaluated baselines, reducing FVD by over 31\% relative to the best baseline, and source-conditioned inference also attains the best FID and instance preservation.

---


### 82. [Bellman Error Minimization Via Linear Programming Normalization](https://arxiv.org/abs/2610.02730)

**<font color=#1a73e8>作者：</font>** Haining Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a new functional approximation approach to reduce Bellman error in high-dimensional dynamic programming and Reinforcement Learning problems. Using a classic dynamic programming problem (network capacity control in revenue management) as the motivational example, the paper illustrates that deep neural networks and linear programming approximation algorithms can be combined to derive approximate solutions to dynamic programming problems. Simulation results show the proposed approximation algorithms achieves competitive performance when compared with benchmark.

---


### 83. [Beyond Correctness: Resolving Underspecification in Agentic Text-to-SQL](https://arxiv.org/abs/2610.02739)

**<font color=#1a73e8>作者：</font>** Wen-Zhi Li, Yue Gong, Konstantinos Kanellis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic Text-to-SQL systems can interact with users to clarify underspecified queries before generating SQL. However, a correct execution result does not necessarily imply that the agent has adequately resolved the underlying underspecification: the agent may silently make unverified assumptions that happen to match the intended answer. We show that this behavior is driven in part by premature clarification termination. Although forcing an agent to ask more questions improves execution accuracy, ambiguities are concentrated in earlier interactions, making brute-force questioning inefficient. More importantly, even when explicitly prompted to plan its clarification process, the agent frequently abandons questions that it has already identified as relevant. To address this failure mode, we introduce PlanPool, which externalizes the clarification plan as a mutable question pool. Every planned question must be explicitly asked or dropped before submission, while newly discovered ambiguities can be added during interaction. Across three benchmarks derived from BIRD-Interact and Spider, PlanPool consistently improves ambiguity coverage and reduces silent failures over unconstrained and prompt-based alternatives, while maintaining competitive execution accuracy. Our results highlight an important distinction in agentic reasoning: identifying missing information is not sufficient, and the agent must also reliably maintain and resolve it before committing to an answer.

---


### 84. [Correcting Guided Diffusion Trajectories with Spectral Alignment](https://arxiv.org/abs/2610.02753)

**<font color=#1a73e8>作者：</font>** Gihoon Kim, Taesup Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The practical success of conditional image generation hinges on fine-grained differences in condition alignment and visual fidelity. Classifier-free guidance (CFG) is central to this success, but its lack of an explicit criterion makes it difficult to assess whether the guided trajectory is progressing as intended. To address this gap, we show that spectral alignment provides a principled criterion for understanding guidance behavior and improving guided diffusion sampling through adaptive correction. Our analysis identifies the spectra of intermediate states as an indicator of consistency with the expected spectral evolution of the forward process. Based on this observation, we introduce Spectral Correction Guidance, a method that corrects deviations from an analytic reference spectrum during sampling. The proposed method is training-free and applicable across diffusion backbones and conditional generation tasks without modifying the underlying model. Experiments demonstrate consistent gains in preference-based metrics over baseline guidance methods in text-to-image generation and improved generation quality over CFG on ImageNet. These improvements persist across a range of guidance scales and with fewer denoising steps. Our analyses and ablations provide insight into guidance behavior and how the proposed method affects generation quality.

---


### 85. [Jumping up and down: Denoiser diffusion models for discrete ordinal data](https://arxiv.org/abs/2610.02754)

**<font color=#1a73e8>作者：</font>** Yair Shenfeld, Ricardo Baptista, Stefano Peluchetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are highly developed in continuous spaces for image and video domains. Recently, major advances have been made for discrete diffusion models for categorical data, specifically in the language domain. In contrast, diffusion models for discrete integer-valued data are less developed, despite the prevalence of this modality, ranging from images and music to gene counts. We introduce Jumping Up and Down (JUD)---a new family of denoiser-based diffusion models for discrete ordinal data. This is the first family of diffusion models for ordinal data which centers around training denoisers, which at the same time allows for bi-directional (up and down) perturbations of the data. The simplicity of the training objective, combined with the flexibility of bi-directional perturbations, leads us to obtain competitive results across different data modalities.

---


### 86. [A Two-Stage Cascade for Near-Real-Time Forest Anomaly Detection from Sentinel-1 SAR Time Series](https://arxiv.org/abs/2610.02763)

**<font color=#1a73e8>作者：</font>** Pann Thinzar Seint, Subas Chhatkuli, Bryan Atwood  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tropical forest monitoring is essential for global climate stability and biodiversity preservation. To address the urgent need for rapid, reliable detection of forest loss which is essential for timely intervention against illegal logging, supply chain transparency, land-use governance and carbon market standards, we introduce a two-stage statistics-encoder cascade for near-real-time anomaly detection using Sentinel-1 time series. Our system is designed to overcome two fundamental challenges in remote sensing: the cloud-cover limitations that restrict optical monitoring and seasonal backscatter variation that causes SAR systems to mistake natural moisture changes for forest loss. The architecture integrates two distinct analytical engines to ensure high-fidelity detection: (1) an adaptive, robust-statistics z-score test on co-registered Sentinel-1 VH backscatter, same-season historical baseline and (2) a learned confirmation gate based on the latent-space structural similarity (SSIM) of a convolutional autoencoder trained on stable-forest patches. A candidate disturbance is confirmed as an alert only when both stages agree, and is assigned a confidence score and a Low/Medium/High risk tier from its repeat-occurrence history. The system produces per-alert auditable confidence scores and area-in-hectares estimates directly compatible with Monitoring, Reporting and Verification (MRV) workflows, sustainable forestry management, operational field checks and environmental risk assessments. Beyond its primary application, the model's flexibility allows for critical environmental applications ranging from selective logging to large-scale agricultural encroachment mapping, flood mapping and so on.

---


### 87. [No-Free-Graph: Learning When Multimodal Data Should Be Graphified](https://arxiv.org/abs/2610.02768)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Kai Hu, YuXin Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph learning has recently emerged as an effective paradigm for in corporating inter-entity relationships into multimodal representations. Existing studies have made substantial progress on how to construct and optimize graphs, but rarely consider a more fundamental question: whether additional relational structures should be introduced for a given dataset and task. Through empirical studies across diverse datasets, tasks, and graph constructors, we reveal that graphification is not consistently beneficial: introducing relational structures can provide substantial improvements in some cases, while offering limited or even negative gains. This observation motivates a new perspective that graph construction should be treated as a selective decision based on its expected utility rather than a default preprocessing step. To address this issue, we propose MAG-SCOUT, a pre-construction graph assessment framework that estimates whether introducing graph structures is beneficial before generating the complete topology. MAG-SCOUT collects limited relational evidence, analyzes its potential taskspecific contribution, and estimates the expected utility of graphification together with construction cost to make a build-or-skip decision. Extensive experiments across six multimodal datasets, three downstream tasks, and diverse graph constructors demonstrate that MAG-SCOUT effectively identifies when graph structures should be introduced, saving 33.1% of task-macro graph work while retaining 96.7% of held-out positive-gain mass under the pre-registered floor.

---


### 88. [Nearly Optimal Fixed-Confidence Best-Arm Identification with 1-Bit Feedback](https://arxiv.org/abs/2610.02771)

**<font color=#1a73e8>作者：</font>** Khang Luong, Dinh Thai Son, Hoang Ta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study fixed-confidence best-arm identification under strict 1-bit feedback constraints. At each round, the learner selects an arm and a query set, and receives only a single bit indicating whether the sampled reward belongs to that set. We consider a distribution-free finite-variance setting with arm-wise localization, where direct empirical mean estimation is no longer available and clipping becomes unavoidable. We first formulate a time-uniform 1-bit mean-estimation primitive based on randomized threshold queries and a clipped tail-integral identity. We then embed this primitive into candidate-challenger best-arm identification algorithms. A fixed-clipping algorithm gives a simple anytime $(\epsilon,\delta)$-PAC guarantee, while a phased adaptive-clipping algorithm matches the clipping level to the current resolution and yields a gap-adaptive sample complexity. We also prove a $K$-arm worst-case information-theoretic lower bound showing that the logarithmic penalty caused by finite-variance 1-bit feedback is intrinsic. This bound matches the leading dependence of the phased algorithm up to lower-order $\log\log$ factors.

---


### 89. [LatticeSMC: Where to Spend Inference-Time Compute in Chunked Sequence Generators](https://arxiv.org/abs/2610.02774)

**<font color=#1a73e8>作者：</font>** Xuanchen Wang, Heng Wang, Weidong Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-form generators for music, motion and video produce sequences chunk by chunk, with each chunk generated by iterative denoising while rewards are defined over the full sequence. Existing inference-time steering methods typically act on one axis at a time: best-of-N at the end, Feynman-Kac steering across denoising steps, or streaming pruning across chunks, and are often compared under unmatched compute or different return rules. We introduce budget-matched chunked steering and propose LatticeSMC, a sampler derived from a Feynman-Kac model on the two-dimensional lattice of chunk index and denoising step. Two telescoping results make its design exact: for chunk-additive rewards, the two axes induce identical weights, so resampling should occur where lookahead is cheapest; for terminal rewards, any prefix score defines an exact intermediate potential, making prefix-evaluable rewards twists with no estimation or extra denoiser calls. LatticeSMC resamples on these potentials at chunk boundaries and, when scoring is free, within chunks, returning either a weighted draw or the best particle. Under matched compute, on music-to-dance diffusion and 40-second text-to-music generation, it raises beat alignment from 0.234 to 0.441 (best-of-N: 0.354) and prompt adherence from 0.470 to 0.560 at 32 particles, while preserving held-out quality. It also retains its advantage on long-range rewards and is preferred by human raters in 60-77 percent of pairwise comparisons. Finally, we show that commitment strength should follow the information in the current potential, while the value of lookahead is predicted by the within-set predictability of future reward.

---


### 90. [TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.02779)

**<font color=#1a73e8>作者：</font>** Jiaxing Song, Weiqi Yan, You Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present trajectory-aware reuse and adaptive correction (TRAC), a training-free framework for efficient autoregressive (AR) video generation. Existing acceleration methods mainly target single-trajectory generation with bidirectional attention. AR video generation, by contrast, sequentially couples chunk-level denoising trajectories. Consequently, approximation errors accumulate and propagate through the generation process. TRAC addresses this challenge with three components, including robust cumulative scheduling (RCS), autoregressive trajectory-aware guidance scheduling (ATGS), and spectral structure correction (SSC). RCS selects cache reuse schedules by cumulative rollout error and cross-chunk/prompt variation. ATGS coordinates CFG refreshes along the global AR trajectory. SSC restores low-frequency structure of the first chunk to correct long-term structural loss. Experiments on SkyReels-V2 and FramePack-F1 show that, compared with existing methods, TRAC achieves both the highest inference efficiency and the best generation quality for AR video generation.

---


### 91. [Controlling Polar Exposure to Delay Memorization in Diffusion Models](https://arxiv.org/abs/2610.02780)

**<font color=#1a73e8>作者：</font>** Xuanchen Wang, Heng Wang, Weidong Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models can reach useful sample quality before copying training examples, but fast optimization can compress this generalization window by accelerating sample-specific fitting. We investigate this effect through update geometry and propose Quality-Gated De-whitening (QGD), a controller that retains a fast polar-update prefix and progressively restores fixed-gain momentum. Our random-feature analysis separates covariance-controlled, curvature-equalized and amplitude-controlled memorization clocks. Under aligned spectral assumptions, it establishes a finite-exposure condition under which a fixed-gain tail recovers a delay proportional to dataset size. QGD implements this principle with a confirmed quality gate, a bounded decay envelope and causal copy feedback. Immediate switching is the conservative limit; gradual control balances delayed copying against continued quality improvement. We pair QGD with Copy-Budgeted Selection (CBS), which applies simultaneous binomial calibration to a frozen checkpoint family, followed by a fresh evaluation of the released checkpoint. On 2,000-image CIFAR-10 subsets, QGD preserves the polar baseline's quality-arrival time while expanding its useful interval by 8.32x and reducing common-checkpoint copying by 75.9%. With identical calibration and independent quality evaluation, QGD achieves FID 75.56 versus 79.37 for SGD with the same selector. Exposure-matched controls, independent detector audits and transfer to flow matching and dance generation support adaptive exposure control as a practical way to improve the quality-copying tradeoff.

---


### 92. [Efficient Memory Crystallization for Graph Learning under Non-Stationary Distribution Shifts](https://arxiv.org/abs/2610.02795)

**<font color=#1a73e8>作者：</font>** Yue Hou, Ruomei Liu, Yingke Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep graph learning models deployed in real-world systems often need to cope with non-stationary environments, where the underlying graph distribution drifts continually over time. Prevailing solutions rely on training auxiliary generative modules to synthesize memory graphs for cross-domain adaptation, which incurs substantial computational overhead and scales poorly under prolonged distribution shifts. We argue that a more economical path exists: rather than generating memory, one can crystallize it. To this end, we propose Efficient Memory Crystallization (EMC), a training-free test-time framework that distills each incoming graph domain into a compact, semantically faithful memory through a closed-form solution to a memory-oriented distribution-matching objective, thereby eliminating redundant domain information under continual covariate shifts. To preserve both generalizability and adaptability as the model traverses a long sequence of target domains, EMC further models inter-domain dependencies through state-evolving memories and admits a theoretically grounded, tighter generalization error bound than direct adaptation. Extensive experiments demonstrate the superior performance of EMC over state-of-the-art baselines on graphs under non-stationary distribution shifts, while reducing average runtime by 87.4% and GPU memory consumption by 92.4% relative to the recent competitor, making continual graph adaptation practical at scale.

---


### 93. [Modeling Shared and Individual Structure for Cross-Subject Continuous Affect Regression from EEG-fNIRS](https://arxiv.org/abs/2610.02796)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Bing Wang, Shuai Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous, second-by-second valence-arousal estimation from physiological signals is typically studied in a subject-dependent setting, where the model sees labeled data from the same person it is later evaluated on. We study the harder zero-shot cross-subject variant on a synchronized EEG-fNIRS dataset: predict raw-scale ([1, 255]) valence and arousal trajectories for subjects whose labels the model never observes, given only their unlabeled EEG/fNIRS recordings while watching the same video stimuli as a disjoint set of training subjects. We decompose the affect trajectory into a structure shared across subjects who watch the same stimuli and an individual structure estimated for each test subject from a label-free EEG marker (alpha-band cross-channel synchrony), which rescales the shared trajectory around the scale midpoint. We validate the per-subject calibration mechanism on four independent axes: leave-one-subject-out correlation between the marker and each subject's true optimal gain, a functional-form comparison against non-linear alternatives, a repeated leave-4-out component ablation isolating each part of the pipeline's contribution, and a ceiling analysis bounding the remaining headroom for per-subject scaling. On held-out subjects, the model reaches an overall MAE of 25.96 / 22.80 across two evaluation batches (valence 21.94 / 19.6, arousal 29.98 / 26.0), well below EEGNet and ASAC-Net baselines reported for the same subject-independent split (raw scale score 60.6 and 55.0 respectively). We further report a systematic negative-result search across model architectures, feature representations, and prediction targets that found no signal able to improve on the single alpha-synchrony marker.

---


### 94. [Muon Learns Facts Better: Understanding the Role of Spectral Orthogonalization](https://arxiv.org/abs/2610.02798)

**<font color=#1a73e8>作者：</font>** Xuheng Li, Qiwei Di, Yuan Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer applies spectral orthogonalization to matrix-valued updates and has shown strong performance in large-scale neural network training, yet the mechanisms of this transformation in feature learning remain poorly understood. In this work, we investigate this question through a tractable factual-recall model, where a fact maps each subject-relation pair to an answer, and a linear transformer learns the subject- and relation-dependent information required to recover this mapping. The transformer is optimized with gradient flow (GF), spectral GF, or Sign GF, which are continuous-time limits of gradient descent, Muon, and Adam, respectively. Prior studies (Nichani et al., 2025) have shown that when the number of subjects exceeds the number of relations, GF learns relation-dependent information before subject-dependent information, producing a feature-separation phase during training. We characterize this separation with the learning times when the subject- and relation-dependent components of the prediction reach a target accuracy. With $S$ subjects and $R$ relations, GF has a learning-time ratio of $\widetilde{\Theta}(\sqrt{S/R})$, whereas Spectral GF reduces this ratio to $\widetilde{\Theta}(1)$. In addition, for fixed $S$ and $R$, the subject- and relation-dependent errors decay as $1/(T\log T)$ in training time $T$ under GF, but as $\exp(-\mathrm{poly}(T))$ under spectral GF. Finally, we show that GF and spectral GF are equivariant under orthogonal transformations of the token embeddings, whereas Sign GF is not: Different orthonormal embeddings can potentially produce no feature separation, a large feature-separation phase, or even a reversed learning order. These results provide a mechanistic view of how spectral orthogonalization can fundamentally reshape feature-learning dynamics.

---


### 95. [FUSEye: Training-Light Fisheye Detection with Overlapping Views and Zero-Initialized Adapters](https://arxiv.org/abs/2610.02799)

**<font color=#1a73e8>作者：</font>** Wenya Su, Kai Luo, Di Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fisheye cameras give mobile robots a single-sensor, low-cost view of their surroundings, yet the COCO-pretrained detectors that practitioners routinely reuse fail on them: strong radial distortion warps local image structure, while boundary compression shrinks objects to near-invisible sizes. Full fine-tuning closes much of the gap but requires abundant fisheye labels and compute. We present FUSEye, a training-light framework that turns a frozen-backbone COCO-pretrained extra-large YOLO26 detector (YOLO26-x) into a fisheye detector. FUSEye adds roughly 227k new parameters while updating the inserted modules and the pretrained detection head. It addresses the transfer gap at three causally linked levels. At the input level, overlapping grid view generation and box remapping (GridViews) enlarge compressed boundary regions. At the feature level, zero-initialized residual adapters (Z-Adapters) correct distortion-induced feature misalignment. At the decision level, learned cross-projection agreement fusion (AgreeFusion) promotes low-confidence detections only when they are supported by consistent evidence across multiple views. On the WoodScape surround-view fisheye benchmark, FUSEye raises YOLO26-x from 0.148 to 0.266 mAP50 and retains 84.3% fully fine-tuned accuracy. Moreover, randomly using only 25% of the labeled training images, FUSEye achieves 0.2597 mAP50, retaining 97.6% of its full-label performance. FUSEye also consistently improves YOLOv8-11 detectors, showing that the recipe is architecture-agnostic. Source code will be available at this https URL.

---


### 96. [VIGOR: Zero-Shot Visual Generalization via Latent-Space Consistency in Model-Based Reinforcement Learning](https://arxiv.org/abs/2610.02801)

**<font color=#1a73e8>作者：</font>** Mingyu Park, Samyeul Noh, Hyun Myung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) achieves strong sample efficiency by planning within learned latent dynamics, yet its performance degrades substantially under unseen visual distractions such as background variations, lighting changes, or camera shifts. Unlike model-free RL, where encoder perturbations affect only single-step predictions, MBRL suffers from a two-level vulnerability: visual distractions first push encoder outputs out of distribution, and these errors then compound through recursive latent rollouts over the planning horizon. We propose visual generalization via latent-space consistency in model-based RL (VIGOR), a framework that enables zero-shot generalization to unseen visual distractions while retaining the sample efficiency of its MBRL backbone. VIGOR integrates three interdependent components: (i) asymmetric weak-to-strong augmentation, which pairs weak-only and weak-to-strong latent views within a single batch; (ii) dynamics-level consistency, which enforces augmentation-invariant transition predictions through direct latent regression; and (iii) encoder-level stabilization, which prevents encoder drift under the cross-augmentation supervision imposed by dynamics-level consistency. Evaluations on the DeepMind Control Suite (DMC) and Robosuite show that VIGOR outperforms state-of-the-art model-free and model-based baselines, surpassing the second-best baseline by 3.4% on DMC and 43.6% on Robosuite. Ablations further show that VIGOR's robustness is augmentation-agnostic: replacing the default augmentation with alternatives from distinct perturbation families preserves strong generalization, confirming that latent-space consistency, not the augmentation choice, drives robustness.

---


### 97. [From TS-SUF-2 to TS-SUF-4: Practical Security Enhancements for FROST2 Threshold Signatures](https://arxiv.org/abs/2610.02805)

**<font color=#1a73e8>作者：</font>** Will Wang, Syh-Yuan Tan, Ryan Chow 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threshold signature schemes play a vital role in securing digital assets within blockchain and distributed systems. FROST2 stands out as a practical threshold Schnorr signature scheme, noted for its efficiency and compatibility with standard verification processes. However, under the one-more discrete logarithm assumption, with static corruption and centralized key generation settings, FROST2 has been shown by Bellare et al. (in CRYPTO 2022) to achieve only TS-SUF-2 security, which is a consequence of its vulnerability to TS-UF-3 attacks.
In this paper, we address this security limitation by presenting an enhanced variant of FROST2, namely, FROST2+ which achieves the TS-SUF-4 security level under the same computational assumptions as the original FROST2. FROST2+ strengthens FROST2 by integrating additional pre-processing token verifications that help mitigate TS-UF-3 and TS-UF-4 vulnerabilities while maintaining practical efficiency. We show that FROST2+ can achieve TS-SUF-4 security not only under the same conditions as the original FROST2 analysis, but also when initialized with a distributed key generation protocol such as PedPoP. Our benchmark using ZCash's FROST library shows that the performance of FROST2+ is comparable to FROST2 and about 64-79% faster than FROST when precomputation is enabled.

---


### 98. [ROUTEAUDIT: Interaction-Aware Identification for Budgeted Multi-Verifier Routing](https://arxiv.org/abs/2610.02808)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive multi-verifier systems are commonly compared through endpoint quality-cost gaps, even when the verifier catalog, availability, accounting, information filtration, or scorer changes with the policy. We formulate verifier routing as a contract-conditioned identification problem. The contract records request support, verifier catalog, realized availability, resource accounting, online filtration, and post-trace scoring; a matched route contrast changes only the policy coordinate. ROUTEAUDIT adds three measurable objects to this contract. A contract lattice averages coordinate increments over every admissible bridge order and reports the resulting attribution together with its path sensitivity. A policy-independent response tape identifies paired sequential contrasts when adaptive policies reveal different observations. For incomplete matching, request-level bounds use whichever potential outcome remains observed and give a sharp finite-population interval. The protocol commits paid observations and ledger events before the oracle join and returns an attribution certificate for each comparison. On two held-out raw-tail caches, matched static SF+SA equals the cascade, assigning the apparent gains of 0.1797 and 0.1250 over full static to the verifier-set edge. On 1,319 held-out task requests, the learned and RLVR studies report quality 0.9522 and 0.9553 versus 0.9484 for matched static; the RLVR-static paired difference is +0.0068 with a request-paired interval $[0.0015,0.0122]$ and a training-seed-by-request hierarchical interval $[0.0006,0.0131]$. Controlled attribution recovery yields route mean absolute error 0.0011 and endpoint reconstruction error 0.0004. Factorial, bridge-order, and stochastic-provider studies evaluate the certificate interface; RLVR supplies a learned-policy stress test under the same identification contract.

---


### 99. [Co-Designing AI For Mental Health Support With Young Adults of Color (YOC): Needs, Expectations, and Implications for AI Literacy](https://arxiv.org/abs/2610.02812)

**<font color=#1a73e8>作者：</font>** Elaine Dabin Jeon, John Bosco S. Bunyi, Hannah Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Young adults of color (YOC) face heightened mental health challenges and barriers to care while navigating developmental and life transitions. Situated between youth-oriented safeguards and adult-oriented AI systems, little is known about how they use AI chatbots for mental health and well-being support or how sociocultural contexts shape their expectations, concerns, and design preferences. We conducted a two-day co-design workshop with 13 Asian, Black, and Hispanic/Latino/a young adults aged 18--24. Participants found generic chatbot advice to flatten their lived experiences; rather than making incorrect assumptions, they wanted more opportunities for identity-informed disclosure. Preferences for YOC-centered personalization also revealed gaps in privacy and AI literacy. Participants negotiated different therapeutic roles for chatbots and sought greater AI accountability and user agency, highlighting blurred boundaries between clinical and non-clinical AI-mediated support. Findings suggest directions for integrating AI literacy with mental health literacy and centering YOC's experiences in the privacy calculus.

---


### 100. [Gated Slot Attention-2: Two-Sided Associative Memory Correction in Linear Attention](https://arxiv.org/abs/2610.02816)

**<font color=#1a73e8>作者：</font>** Ruijie Li, Shengnan Ding, Weimin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention models have emerged as efficient alternatives to standard attention, but effectively managing their fixed-size recurrent memory remains challenging. To improve memory, recent work has explored two distinct directions: delta-rule variants for precise correction of values associated with keys, and slot-based architectures such as Gated Slot Attention for modeling key and value memories in two stages. We observe that these directions are complementary--the delta rule provides effective memory correction, while the two-stage structure provides a natural way to operate on both sides of an association. Building on this insight, we introduce a new Gated Oja Rule for key-side correction and extend it with decoupled erase and write control to obtain Gated Oja Rule-2. We then introduce Gated Slot Attention-2 (GSA2), which combines Gated Oja Rule-2 for key-side correction with Gated Delta Rule-2 for value-side correction through shared latent slots. We further derive a hardware-efficient chunkwise algorithm for parallel training. Experiments demonstrate that GSA2 consistently improves over strong linear-attention baselines across benchmarks while retaining linear-time sequence modeling and constant-memory recurrent decoding.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
