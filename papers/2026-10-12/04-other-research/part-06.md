# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-329](./part-07.md)

---

### 251. [Moving Target Defense in SDN-enabled EV Charging Network](https://arxiv.org/abs/2610.11996)

**<font color=#1a73e8>作者：</font>** Roland Plaka, Mikael Asplund, Simin Nadjm-Tehran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-Defined Networking (SDN) is emerging as a promis- ing technology for EV Charging infrastructure (EVCI) since it enables flexible, programmable control of EVCI networks, yet its security gain to EVCI remains underexplored. SDN-enabled EVCI faces an increas- ing number of cyber threats arising from the convergence of IT and OT components; in particular, low-rate Denial-of-Service (DoS) attacks. Ear- lier works identify a trend toward low-rate attacks in OT networks that may exhaust SDN switch flow tables and which can result in disabling the entire charging sites without triggering volume-based defenses. In this paper, we propose CS-SHIELD, a Moving Target Defense mecha- nism for SDN-enabled EVCI communication. We showcase the imple- mentation of the proposed mechanism that detects malicious flow table rules via cross-layer identity verification and responds by reassigning virtual IP addresses to all active chargers. Experiments on an emulated SDN testbed with a real charging protocol implementation demonstrate that CS-SHIELD maintains full site availability under attack, responds quickly, adds only a negligible delay under normal conditions. The reas- signing (shuffle) approach at each reaction makes the earlier reconnais- sance knowledge by the attacker rendered worthless.

---


### 252. [An Interpretable Approach to PDE Solution Discovery via Structural Experience Distillation](https://arxiv.org/abs/2610.12003)

**<font color=#1a73e8>作者：</font>** Yunpeng Gong, Huolong Wu, Can Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> PDE solution discovery aims to identify explicit symbolic expressions for unknown physical fields from observations under known physical constraints. Existing methods, however, collapse data fidelity and physical consistency into a single terminal score used as the sole feedback signal, providing little information about which subexpressions are responsible for a candidate's final performance. This opaque terminal feedback severely limits the interpretability of the search process itself, offering no insight into why a candidate succeeds or fails. Consequently, reusable structures in otherwise suboptimal candidates are often discarded, whereas incidental syntax along successful search trajectories may be repeatedly reinforced. We propose SED-MCTS, a Monte Carlo tree search approach that distills structural experience from evaluated expressions and reuses it to guide subsequent symbolic solution search. Through counterfactual subtree interventions, SED-MCTS estimates local structural contributions, routes reliable evidence to the responsible construction edges, and preserves useful components in a refined structural archive. The approach naturally extends to coupled multiphysics systems. Across a diverse suite of PDE benchmarks, SED-MCTS achieves strong performance under a fixed evaluation budget and improves search efficiency and robustness under noisy or scarce observations.

---


### 253. [The Polytopal Neural Network](https://arxiv.org/abs/2610.12004)

**<font color=#1a73e8>作者：</font>** A. Emilie J. Wedenborg, Anders V. Nørskov, Teresa Dorszewski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how deep neural networks process information remains a central challenge. Existing interpretability methods often compromise structural fidelity, rely on prespecified corpora, or explain models post-hoc. We propose Polytopal Neural Networks (PNNs), a framework that extracts distinct layer-wise aspects by enforcing a polytope-based structure that is used directly in subsequent information processing. We scale our approach using learned corpus representations and an amortized simplex inference procedure and highlight how the framework also gives a direct route to vector quantized (VQ) training. In PNNs, observations are explicitly described by their alignment with layer-specific aspects. Empirical results show that imposing polytopal constraints on neural network representations preserves meaningful structures in the latent space with minimal degradation in performance, favorable compressed representations when compared to VQ representations in unsupervised learning, while also providing a performant new approach to VQ deep learning training. Our findings suggest that deep networks can enforce interpretable polytope-based representations, offering a principled path toward more transparent AI systems with minimal performance compromise.

---


### 254. [Complexity of Grounded Semantics and Preferred Semantics in Finitary Argumentation Frameworks](https://arxiv.org/abs/2610.12008)

**<font color=#1a73e8>作者：</font>** Jinfan Xu, Jieting Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abstract argumentation frameworks (AFs) introduced by Dung provide a formal foundation for non-monotonic reasoning in artificial intelligence. While decision problems for general infinite AFs typically reside at high levels of the analytical hierarchy ($\Sigma_1^1$ or $\Pi_1^1$), restricting the framework to be computably finitary reduces some of the complexity to the arithmetical hierarchy. In this paper, we present a complexity mapping of grounded and preferred semantics in computably finitary AFs across standard decision problems: credulous acceptance ($\Cred$), skeptical acceptance ($\Skep$), extension existence ($\Ex$), uniqueness ($\Uni$), and non-empty existence ($\NE$). For grounded semantics, credulous and skeptical acceptance are already known to be $\Sigma_1^0$-complete. We show that non-empty existence is also $\Sigma_1^0$-complete, whereas existence and uniqueness are trivial. These classifications are understood within the domain of valid computably finitary representations. For preferred semantics, using a computably finitely branching computation tree, $\Cred_{\pref}$ is shown to be in $\Pi_1^0$-c and $\NE_{\pref}$ is $\Sigma_2^0$-c. However, it is insufficient to reduce universal quantification and global uniqueness, leaving $\Skep_{\pref}$ in $\Pi_1^1$ and $\UniPref$ in $\Sigma_2^1$-c. Our results show the precise boundary where finitarity succeeds to bring reasoning down to the arithmetical hierarchy and where second-order quantification forces problems back into the analytical hierarchy.

---


### 255. [PulseBound: Future-Beat State Forecasting Under an Explicit Information Boundary](https://arxiv.org/abs/2610.12010)

**<font color=#1a73e8>作者：</font>** Chenyang Xu, Donglin Xie, Xi Xiang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive representation learning from photoplethysmography (PPG) can violate causal information access even with causal attention, as normalization, nonlocal transforms, or companion views may depend on withheld samples. We introduce PulseBound, a PPG representation learner combining physiologically structured future-beat prediction with an explicit stored-window information boundary. A content-independent cutoff separates the visible prefix from the prediction target. Prefix-only normalization, suffix replacement before derived-view construction, and aligned masking ensure that encoder inputs depend only on the visible prefix and cutoff. This yields stored-suffix invariance: with fixed model state, randomness, prefix, and cutoff, changing the stored suffix cannot change the forecast context. A shared horizon-conditioned head predicts nine rhythm and morphology descriptors for up to four extractor-valid future beats, using elementwise validity masks; optional ECG-derived pulse-arrival-time supervision is restricted to training. On MIMIC and VitalDB groups held out from PulseBound backbone pretraining, PulseBound reduces nine-state transformed-space MAE relative to last-visible-beat persistence by 28.06% and 22.22%, respectively, with gains in MAE, MAE-Skill, and Spearman correlation across all 40 source-cutoff-horizon cells. In a separate comparison of seven models on 13 downstream tasks, PulseBound achieves the best mean on nine frozen linear-probe and seven full-fine-tuning tasks. Stored-suffix interventions cause zero recorded changes in forecast contexts or predictions, with zero suffix-input gradients at audited precision under the stored-window interface. These findings separate three testable aspects of predictive physiological representation learning: information access, supervised future structure, and transfer.

---


### 256. [CausalDreamer: Learning Predictive World Models with Latent Disentanglement](https://arxiv.org/abs/2610.12016)

**<font color=#1a73e8>作者：</font>** Prince Jha, Nils Lukas, Kun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward. Generative world models such as Dreamer 4 consist of a video tokenizer, which encodes each frame into a latent, and a dynamics model, which is pretrained to predict future latents from past latents and actions. Yet the tokenizer is trained with a reconstruction objective, without action or reward supervision, so its latent provides no explicit mechanism to separate controllable, uncontrollable, reward-relevant, and reward-irrelevant information. We propose \textit{CausalDreamer}, which keeps the tokenizer frozen and re-encodes its latent into a factored representation of four groups along two axes: controllability, where only the two controllable groups receive the action, and reward relevance, learned by predicting the reward from the two reward-relevant groups. The pretrained dynamics model is then fine-tuned to predict the factored representation. We evaluate \textit{CausalDreamer} and the pretrained world model it starts from with model-predictive planning on 20 MMBench2 tasks: 10 clean tasks seen during training and 10 unseen tasks, of which 6 are manipulated variants of clean tasks with a changed background, object, or maze layout, and 4 are new environments. We normalize returns so that a policy taking uniformly random actions scores 0 and an expert scores 1. \textit{CausalDreamer} achieves a 14\% higher normalized score than the pretrained world model on the clean tasks (0.199 vs.\ 0.175) and a 25\% higher score on the manipulated variants (0.307 vs.\ 0.246), while neither model scores meaningfully above the random policy in the new environments. Additionally, our analysis shows that the factored representation separates reward-irrelevant changes, such as a changed background, from its reward-relevant groups.

---


### 257. [InterviewPlayground: A Simulation Environment for Evaluating AI Interviewers](https://arxiv.org/abs/2610.12023)

**<font color=#1a73e8>作者：</font>** Jonathan Ivey, Aimee Liang, Arthur Y.S. Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Increasingly, AI interviewers are being developed to elicit open-ended responses in applications like market research, public polling, preference elicitation, and social science research. However, evaluating AI interviewers is challenging because they function in extended, multi-turn interactions where they must adapt to participant behaviors. To address this need, we develop InterviewPlayground, a simulation environment for evaluating AI interviewers using simulated study participants whose behaviors are grounded in social theory. Simulated studies in InterviewPlayground produce an InterviewReportCard, which assesses the performance of AI interviewers using a suite of validated measures. To test whether our simulation-based evaluations predict performance with human participants, we conduct 15 real qualitative studies with five AI interviewers, three interview topics, and 450 human participants and compare them to simulated studies in InterviewPlayground. We find that AI interviewer performance in InterviewPlayground predicts performance in human studies with an average Pearson correlation of 0.86 across 12 measures, and the simulated interactions from InterviewPlayground reproduce key findings from behavioral analysis of AI interviewers in the human studies. Together, these findings support the validity of InterviewPlayground in assessing AI interviewer performance and examining potential failure modes. Our work contributes a simulation environment for AI interviewers supported with empirical validation, and more broadly, a roadmap for future work to develop validated, simulation-based evaluations of conversational AI systems.

---


### 258. [HPQ-AKE: A Provably Secure Sign-Less Hybrid Authenticated Key Exchange Protocol for Bandwidth-Constrained IoT and Edge Networks](https://arxiv.org/abs/2610.12024)

**<font color=#1a73e8>作者：</font>** Khiem Pham-Tuan, Minh Quang Le, Khuong Nguyen-An  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Securing bandwidth-constrained Internet of Things (IoT) and edge networks during post-quantum migration creates an authentication trade-off: ML-KEM provides post-quantum key establishment, whereas post-quantum signatures increase certificate-chain size, verification cost, and handshake latency. We present HPQ-AKE, a sign-less hybrid authenticated key exchange for RSA-enabled IoT gateways and edge/cloud services that replaces transcript signatures with dual KEMs. HPQ-AKE combines ML-KEM-768 for post-quantum session secrecy and forward secrecy with RSA-OAEP for implicit mutual authentication, preserving existing RSA-enabled infrastructure during migration. We analyze HPQ-AKE in an extended Bellare-Rogaway model, separating classical authentication in the Random Oracle Model from session-key secrecy in the Quantum Random Oracle Model. Under the Module-LWE and RSA assumptions, it establishes AKE security, forward secrecy, and conditional KCI resistance under the long-term-key-only exposure assumptions. Evaluation combines x86 micro-benchmarking, analytical latency modeling, and 10,000-iteration Monte Carlo simulation. HPQ-AKE reduces modeled handshake transmission from 13,009 to 5,668 Bytes, a 56.4% reduction relative to a Hybrid TLS 1.3 Full handshake, while requiring 7.11 ms of total local computation on the measured x86 testbed. Under a simulated 50 kbps satellite-like link with 600 ms RTT and stochastic jitter, median latency is 1,914 ms, 31.4% below the 2,791 ms baseline. At 20 ms RTT, modeled break-even thresholds are 0.31 Mbps against the pre-cached baseline and 4.08 Mbps against the full baseline; both decrease as RTT increases. These x86-based results motivate evaluation on gateway-class IoT and edge platforms; performance on ARM gateways and unaccelerated microcontrollers remains unvalidated.

---


### 259. [MPGE: A Multi-Perspective Graph Explainer for Molecular Classification Explanation](https://arxiv.org/abs/2610.12039)

**<font color=#1a73e8>作者：</font>** Mahtab Sarvmaili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) predict molecular properties from chemical graph data, but predictive accuracy does not explain how graph information supports an individual decision. A compact prediction-preserving rationale does not necessarily reveal which changes reverse the decision or which modifications the model tolerates. We propose the Multi-Perspective Graph Explainer (MPGE), unifying factual support, counterfactual sensitivity, and exemplar tolerance for a frozen classifier. The factual view, originally termed prototype (PT), seeks a compact retained edge set with the same label and required confidence. Counterfactual (CF) explanations seek bounded prediction-changing deletions; exemplar (EXE) explanations seek non-trivial bounded deletions that preserve the label and confidence. A shared constrained formulation connects prediction behavior, compactness, and edit cost, while separate objectives generate the three views. Our graph-classification extension of CF-GNNExplainer learns symmetric edge rankings and verifies discrete candidates, recording unsuccessful searches. A separate BBBP fragment backend returns RDKit-sanitized molecules. We evaluate the primary GCN implementation on MUTAG, Mutagenicity, AIDS, COX2_MD, and BBBP using semantic coverage, conditional quality, stability, and runtime. Successful factual masks retained 8.6%--15.5% of input edges on average across datasets; bounded counterfactual coverage was 4.8%--67.6%, and exemplar preservation coverage was 98.9%--100.0%. Exploratory controls reveal the influence of hard projection and retained node information. Quantitative comparisons and molecular visualizations characterize model support, sensitivity, and tolerance without treating them as validated chemical mechanisms.

---


### 260. [Protecting CPU AI On Edge TEEs: WebAssembly's Promise and Practical Challenges](https://arxiv.org/abs/2610.12050)

**<font color=#1a73e8>作者：</font>** Friedrich Vandenberghe, Lachlan Gunn, Bruno Volckaert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI models on edge hardware contain important intellectual property (IP), but an adversary can steal it when they achieve root access. Trusted Execution Environments (TEE) like Arm TrustZone protect against these Operating System (OS) level attacks. However, they are challenging to use. More precisely, it is difficult to run unaltered applications inside a TEE. This work presents a solution that allows the execution of unaltered AI models, compiled to WebAssembly, on the WebAssembly Micro Runtime (WAMR) in OP-TEE for Arm TrustZone. Additionally, this work provides an AI model distributor that encrypts the WebAssembly binary and places the encryption key in one of the device's fuses. This way, only the WAMR Trusted Application (TA) in OP-TEE can decrypt and execute the AI model. A thorough evaluation of our solution shows that it incurs an additional overhead of 22% in comparison to an application manually ported to OP-TEE, while also facilitating the execution of unaltered AI models with an additional inference latency of 6% without significant porting effort. Overall, there is a pressing need to safeguard the IP of AI models and this work shows that there is a real promise in WebAssembly, but there remain some practical challenges.

---


### 261. [LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes](https://arxiv.org/abs/2610.12069)

**<font color=#1a73e8>作者：</font>** Peijun Xu, Chuansen Nie, Yiyang He 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic household simulation must capture not only diverse environments but also the lived-in object arrangements and spatial constraints that shape robot motion and interaction. Existing resources often trade off scale, real-world correspondence, and interaction readiness, leaving a gap in faithful, interactive replicas of how real homes are actually arranged. To this end, we introduce LIVIN, a benchmark for spatial and embodied intelligence built on digital twins of 30 diverse lived-in homes. These replicas preserve observed room layouts, furniture configurations, and everyday belongings. To construct them, we design a human-in-the-loop workflow comprising instance recognition, architectural reconstruction, and object generation and placement, with intermediate results reviewed and corrected by humans against the source observations at each stage. We evaluate four tasks in LIVIN: 3D detection, 3D reconstruction, navigation, and loco-manipulation. Our evaluations show that current methods remain challenged by the dense object arrangements, occlusions, limited free space, and constrained interaction regions found in realistic lived-in homes. We hope LIVIN will help advance embodied AI in real-world homes, from spatial understanding to robotic interaction, and ultimately bring embodied intelligence into everyday home environments.

---


### 262. [Exploiting Gradients in Bayesian Inference of Expensive Simulators](https://arxiv.org/abs/2610.12076)

**<font color=#1a73e8>作者：</font>** Šimon Soldát, Václav Šmídl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulators based on differential equations are ubiquitous in science and engineering. They are often used in simulation-based inference to evaluate the posterior distribution of the input parameters based on real-world observations of the simulator outputs. However, inference becomes challenging when individual simulator evaluations are computationally expensive. In such cases, a Bayesian optimization-based active learning approach with Gaussian process surrogate models has been used to maximize the information obtained from a limited simulation budget. Recently, gradients of simulator outputs with respect to input parameters have become increasingly available, yet they are rarely exploited for inference. Even though we only need to learn the simulator input-output relationship, gradient information can provide an additional valuable signal to guide the active learning procedure. This is of particular interest in the case of expensive simulators, when sample efficiency is crucial.
In this paper, we demonstrate how incorporating gradient information into the Gaussian process surrogate accelerates Bayesian optimization-based inference under a limited simulation budget. Our results show significant improvement in convergence speed from using gradient information. For reverse-mode differentiation, the inference efficiency gains are maintained when accounting for the additional computational cost. In contrast, for forward-mode differentiation, the inference speed-up does not outweigh the computational costs. These results indicate that gradient-enhanced surrogates are beneficial primarily in problems where the number of parameters exceeds the output dimensionality, where reverse-mode differentiation is efficient.

---


### 263. [Perception Test 2026: Challenge Summary and Extension to City-scale Audio-Visual Reasoning](https://arxiv.org/abs/2610.12081)

**<font color=#1a73e8>作者：</font>** Fedor Kitashov, João Carreira, Shiry Ginosar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuing the Perception Test challenge series, we organised the fourth edition as a workshop at the European Conference on Computer Vision (ECCV) 2026 in Malmö, Sweden. This edition focused on spatial intelligence and featured four different tracks: unified multiple-choice videoQA and grounded videoQA from the original Perception Test benchmark, alongside two new tracks based on city-scale walking-tour videos (KilometerAudio and KilometerVision). In this report, we describe the new benchmarks used for the city-scale tracks and summarise the winning solutions across all tracks, including a generalist model that competed across all tracks with satisfactory performance. The winning solutions in the newly added city-scale tracks demonstrated that complex spatial and multimodal reasoning can be solved by expensive agentic pipelines, but remains difficult for multimodal models used standalone.

---


### 264. [DVLA-RL++: Dual-Level Vision-Language Alignment with Reinforcement Learning Gating for Few-Shot Learning](https://arxiv.org/abs/2610.12095)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Xianjing Meng, Qiangchang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot learning aims to recognize novel categories from limited labeled examples. Recent studies incorporate textual semantics to compensate for limited visual observations and improve class representations. However, high image-text agreement may reflect both intrinsic object properties and incidental context, making support prototypes susceptible to contextual contamination. To address this problem, we propose DVLA-RL++, which extends DVLA-RL with complementary semantic purification (CSP) and counterfactual reinforcement-learning gating (CRG). Specifically, CSP generates intrinsic and nuisance descriptions from labeled supports and compares their agreement with each support token. An ambiguity-dependent rejection margin guides sparse evidence allocation, while an intrinsic semantic anchor fills the unassigned mass to provide a fallback when visual evidence is unreliable. CRG learns layer-wise semantic fusion strengths using a reward that balances recognition performance and nuisance exposure. An independently executed reference trajectory on the same episode provides a paired learning signal. Theoretical analysis relates retained evidence and anchor quality to prototype stability and establishes conditions for unbiased on-policy gradient estimation. Experiments on standard, fine-grained, and cross-domain benchmarks show state-of-the-art accuracy, with an average gain of 1.4% over DVLA-RL. The project page is available at this https URL.

---


### 265. [SCORE: Spectral Correlation Estimation for Multivariate Gaussians](https://arxiv.org/abs/2610.12096)

**<font color=#1a73e8>作者：</font>** Christopher Bülte, Emil Partow, Astha Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network-based predictive modeling with high-dimensional structured Gaussian targets requires an efficient and numerically stable, yet expressive approximation of the covariance matrix. We propose SCORE: a scalable framework, combining scoring rule training with an expressive covariance approximation learned in spectral space. For $d$-dimensional data, the learning task is decomposed into learning the marginal distributions and learning a structured correlation matrix, which enables dense dependencies with linear storage and $\mathcal{O}(d\log d)$ cost. We utilize the closed form Gaussian kernel score for training, which remains defined even for degenerate covariances and admits bounded gradients during optimization. We characterize kernel scores under invertible transforms and prove exact invariance under unitary transforms. At population level, our two-level objective recovers the true marginals and projects the target correlation onto the representable class; finite-sample PAC bounds show that the errors of the two stages enter additively. We evaluate our model on a variety of tasks with a commonly assumed Gaussian domain: Time-series forecasting, monocular depth estimation, and spatial weather prediction, showing improved performance at lower computational cost.

---


### 266. [Few-Step Generation via Data-Space Iteration](https://arxiv.org/abs/2610.12102)

**<font color=#1a73e8>作者：</font>** Shanchuan Lin, Yansong Peng, Fu-Yun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as a scalable paradigm for training high-quality generative models, but sampling from the learned probability flow requires many network evaluations. Distillation can reduce this cost to one or a few evaluations; however, one-step generation often sacrifices quality, making few-step generation the practical operating regime. Existing few-step methods perform their iterative computation along the probability flow and therefore require a fixed, manually chosen timestep discretization. This discretization is often chosen heuristically and is expensive to tune; it may also be restrictive when refinement difficulty differs across samples or spatial locations. We introduce data-space iteration, a few-step generation framework that removes flow discretization altogether. Starting from noise, a shared generator directly refines its prediction in data space, with every iteration trained to produce the best sample permitted by its capacity. Our formulation integrates with distribution matching distillation (DMD) with minimal changes, enabling a controlled comparison between iteration methods under matched training settings. On class-conditional ImageNet 256x256, data-space iteration outperforms standard discretization baselines and matches or improves upon variants selected through schedule search, without requiring schedule-specific training. These results show that data-space iteration provides a simple and effective alternative to discretized flow-space iteration for fast generation.

---


### 267. [A Geometric Approach to Soft Actor-Critic with Zonotopes for Locomotion Learning](https://arxiv.org/abs/2610.12113)

**<font color=#1a73e8>作者：</font>** Panagiotis Roditis, Panagiotis P. Filntisis, Petros Maragos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy actor--critic methods control overestimation bias by taking the minimum of two critics. This uses the same aggregation rule everywhere, regardless of how the critics disagree. We propose \textbf{GeZo-SAC}, which uses auxiliary geometric representations to adapt critic pessimism to the state and action. Alongside its scalar value, each critic predicts a set of generators defining a zonotope. Probing this zonotope along sampled directions provides a geometric width, "subtracted from each critic value as a pessimistic offset, and a measure of disagreement between the two critics, aggregated with log-sum-exp. This disagreement controls how the critics are combined, moving from a width-weighted average toward the usual minimum as disagreement increases. At inference, the deployed policy is an unmodified SAC actor, since the generators are used only on the critic side during this http URL four MuJoCo-v5 locomotion benchmarks and six off-policy baselines, GeZo-SAC achieves the highest mean return on Ant-v5 and Hopper-v5 and remains competitive with other methods on the remaining tasks. Our analysis further shows that GeZo-SAC achieves the lowest average actuator work and action effort per metre among the evaluated methods, while maintaining near-zero measured overestimation frequency across all four environments.

---


### 268. [Credal Machine Learning for Risk-Averse Decision Making](https://arxiv.org/abs/2610.12115)

**<font color=#1a73e8>作者：</font>** Timo Löhr, Paul Hofman, Maximilian Muschalik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many machine learning applications, it is necessary to guard against worst-case scenarios and predictions that could result in substantial losses. In principle, this can be achieved by training risk-averse predictive models that minimize loss functions such as conditional value-at-risk (CVaR), rather than relying on models that perform well on average. In practice, however, the effectiveness of this approach to risk aversion is undermined by the learner's uncertainty regarding the true loss distribution and, consequently, the true CVaR. To achieve reliable risk-aversion, we propose a method in which this (epistemic) uncertainty is represented in terms of credal sets, i.e., sets of probability distributions. More specifically, we develop an efficient yet reliable learner that produces predictions in the form of credal sets and combine it with a novel decision rule that maps each credal set to a single predictive distribution for CVaR minimization. Across classification, under distribution shift, and in reinforcement learning, our approach reliably avoids catastrophic decisions, while sacrificing little in expected performance.

---


### 269. [Using Weisfeiler-Leman Features for Algorithm Selection in Constraint Optimisation](https://arxiv.org/abs/2610.12119)

**<font color=#1a73e8>作者：</font>** Alessio Pellegrino, Jacopo Mauro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithm Selection is essential for efficient Constraint Programming. Over the years, many algorithm selectors based on machine learning methods have been successfully applied, yet traditional feature extraction methods often rely on manually decided instance-level statistics that fail to capture the underlying problem structure.
In this paper we aim to bridge this gap by introducing a novel, automated feature extraction methodology that integrates graph conversion and Weisfeiler-Lehman graph kernels to generate robust structural representations of problem instances. The 1-WL test bounds the graph-distinguishing power of standard message-passing Graph Neural Networks (GNNs), and suitable GNN architectures match this bound \citep{Xuetal2018}. WL-based features offer an alternative that does not require training a GNN. Our primary contribution is a cut-based representation (\texttt{WLc}) designed to model structural partitions and provide a more nuanced predictive signal. We evaluate our approach on instances from the 2023--2025 MiniZinc Challenges across two tasks: maximizing Borda count scores and maximizing predictive accuracy. Experimental results across Support Vector Machines, Random Forests, and Multi-Layer Perceptrons demonstrate that cut-based features outperform \texttt{fzn2feat} with SVMs, while results with RFs and MLPs are closer.

---


### 270. [LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127)

**<font color=#1a73e8>作者：</font>** Qizhou Huo, Xuan Sun, Yongfei Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive scene exploration requires frequent view updates, although small camera motions preserve much of the visible content. Conventional 3D Gaussian Splatting nevertheless renders each target view, leaving this image overlap unexploited. Reusing rendered images offers an alternative. Geometric warping alone cannot recover newly exposed content and remains sensitive to depth errors. We propose a per-scene framework that replaces repeated scene rendering for nearby views with relative-pose-guided RGB-D image reuse. Geometric warping uses depth and relative pose to transport source content, while a lightweight multiscale network predicts RGB residuals to correct artifacts and infer missing appearance. Cached source features further reduce repeated computation. On GS-render, residual refinement improves PSNR by 0.72~dB over pure warping; evaluations on captured and rendered scenes demonstrate low query latency. This separation of scene rendering from local view updates supports responsive scene exploration, with potential applications in augmented and virtual reality.

---


### 271. [An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling](https://arxiv.org/abs/2610.12129)

**<font color=#1a73e8>作者：</font>** Robert Graham, Yariv Barsheshat, Phil Blandfort 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A large body of research measures model coherence based on output variance without adequately considering competing causes. We identify two such causes, ambiguity and indifference, and we introduce a set of 175 questions where contradicting answers cannot easily be explained by either. We then measure incoherence in terms of contradictions when resampling answers to the same question. In contrast to other methods our metric has high specificity, and only ranks models as incoherent when the issues are glaring. Even so, we find narrow finetunes score poorly. Inspecting inconsistencies flagged by our method, we find that model organisms from the literature display severe issues such as identity conflation, introspection failures and rationalizations. These findings suggest that the pathologies induced by narrow finetuning may limit what these models can tell us about coherent misaligned behaviour.

---


### 272. [Rehearse Everything, Remember Nothing: Attic-KV Rehearses What Will Be Read](https://arxiv.org/abs/2610.12133)

**<font color=#1a73e8>作者：</font>** Zhiyun Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many key-value (KV) caches are compressed before anyone knows what will be asked of them: a document cached for retrieval, a prompt prefix shared across requests, the memory of a long conversation. The prevailing approach scores KV entries by rehearsal: the model rereads the context and keeps the entries it attends to, assuming that the more completely a cache rehearses its context, the better it remembers it. We show that under tight budgets this assumption backfires: rehearse everything, remember nothing. At a 3% keep ratio, rereading the whole context keeps 31.5 of 96.5 points on RULER, and on LongBench's natural-text tasks it falls below methods that rehearse nothing at all. The cause is that a cache keeps what it rehearses: rereading spreads the budget across the whole context, so the answer's own entries survive at little more than chance. Like a student before an exam, a cache remembers more by testing itself than by rereading. Two principles follow: rehearse what will be read, and rehearse as much as there is. We instantiate them as Attic-KV (Attic for short), a training-free rehearsal in which the model quizzes itself with question-answer pairs that quote the context, alongside anchor tokens in a content-adaptive amount. Changing only the rehearsal lifts three hosts that score it in three different ways: Attic alone is the best training-free method in all eight settings we test on RULER and LongBench's natural-text tasks, and plugged into the gradient-based KVgrad and the trained RestoreKV+, it raises them by up to 17.1 and 28.1 points. Its advantage grows as the budget shrinks, reaching 41.9 points over full rereading at a 3% keep ratio, and it compresses faster than rereading the whole context.

---


### 273. [OA-MAP: Evidence-Grounded Multi-Agent Multimodal Framework for Interpretable Knee Osteoarthritis Progression](https://arxiv.org/abs/2610.12134)

**<font color=#1a73e8>作者：</font>** Sixu Chen, Mingrui Yang, Qiang Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knee osteoarthritis (KOA) progression prediction can support patient monitoring, requiring the integration of multimodal data and multidomain expertise. Moreover, isolated risk estimates provide limited insight underlying a prediction. To automate the progression assessment workflow and reduce manual effort while providing interpretable findings and supporting evidence, we present OA-MAP, an autonomous multi-agent framework for evidence-grounded assessment of structural and pain progression in KOA. The system incorporates modality-specific agents including MRI, X-ray, and clinical agents, together with a coordinator agent. This framework can autonomously recruit specialist agents, select tools for prediction and analysis, and retrieve literature as external evidence based on user request and available patient information. An uncertainty-informed human-in-the-loop mechanism enables clinicians to review and correct intermediate findings, triggering recomputation of affected results. We evaluate the prediction models using 600 participants from the FNIH Osteoarthritis Biomarkers Consortium cohort. On the test set of 100 participants, the fusion models achieve AUROCs of 0.80 for structural progression and 0.68 for pain progression. A case study illustrates how OA-MAP combines risk estimates with intermediate findings, cross-modal conflicts, literature support, and uncertainty indicators to support interactive review.

---


### 274. [Q-Shaped Options for Hierarchical Reinforcement Learning](https://arxiv.org/abs/2610.12135)

**<font color=#1a73e8>作者：</font>** Clarisse Wibault, Antoine Gorceix, Antonio Léon Villares 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning to tackle long-horizon, goal-conditioned tasks requires an agent to reason over extended timescales and act across a broad range of states. In principle, Hierarchical Reinforcement Learning (HRL) addresses both challenges through the interaction between action (temporal) and state (spatial) abstraction. First, using an action abstraction to represent temporally extended behaviour as options reduces the effective decision horizon. Second, enabling different state abstractions at each level of the decision process permits greater data aggregation for learning. However, realising these two benefits of a hierarchical policy depends on learning an appropriate action abstraction. Current HRL algorithms fail in one of two ways. Some discard distinctions between options needed for optimal control, undermining hierarchy altogether. Others retain unnecessary distinctions, preserving horizon reduction, but forfeiting coarser state abstraction. In this work, we characterise three desiderata for an action abstraction. We introduce Q-Shaped Options (QSO) to address all three. QSO builds on an architecture with distinct state-value functions, Q functions and policies at each level of the hierarchy. It learns the action abstraction between consecutive levels as a shared encoder shaped by their respective Q functions. The low-level Q function uses the option as a goal, encouraging the abstraction to retain distinctions necessary for optimal control. The high-level Q function uses it as an action, encouraging unnecessary distinctions to be discarded. Across offline goal-conditioned locomotion and manipulation environments, QSO learns semantically meaningful option spaces and outperforms baselines, achieving non-zero performance in tasks where all other evaluated algorithms fail.

---


### 275. [Large-Scale Benchmarking of Quantum Neural Network Configurations for Financial Time Series Forecasting](https://arxiv.org/abs/2610.12148)

**<font color=#1a73e8>作者：</font>** Jack Waller, Xing Liang, Dimitrios Makris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum machine learning, and quantum neural networks (QNNs) in particular, are advancing fields with growing potential. Although systematic comparisons of QNN configurations have been explored primarily for classification tasks, comparatively little attention has been given to regression problems, particularly financial time series forecasting. This study presents a large-scale systematic comparative evaluation of QNN component configurations for financial time series forecasting, using the GBP/USD spot exchange rate as a case study. A grid search across encoding methods, ansatz designs, qubit counts, layer depths, and cost functions yields 1,368 distinct model configurations, each evaluated in terms of prediction accuracy, computational cost, and convergence behaviour. The results reveal unique insights into how the choice of methods influences performance, such as that gate selection and arrangement are more critical to model success than raw parameter count, and that entanglement is a system-level property of the full circuit rather than solely at the ansatz level. The best-performing QNN configuration achieves an $R^2$ score of 0.985, outperforming a classical BiLSTM baseline. Additionally, the impact of real quantum hardware noise is assessed through execution on the IQM Emerald device, revealing that gate errors and decoherence represent a significant barrier to practical deployment, with gate selection and circuit depth identified as key determinants of hardware noise resilience. Overall, the findings provide practical architectural guidance for QNN design and establish a baseline characterisation of QNN noise sensitivity on near-term quantum devices.

---


### 276. [Bayesian Optimisation under State-Preservation Constraints](https://arxiv.org/abs/2610.12150)

**<font color=#1a73e8>作者：</font>** Gabriel Diaz-Aylwin, Vignesh Gopakumar, Omkar Myatra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many engineering design problems, the objective and constraints depend on the state: the solution of a PDE determined by the design parameters. We consider improving a design while holding selected state observables near trusted values, which we call state preservation constraints. Constrained Bayesian optimisation handles these with a learnt feasibility model, but struggles with this problem's highly anisotropic feasible set. Our central idea is to pre-compute the set of controls whose linearised constraint response stays within tolerance, thereby pulling back the state-space constraint into design space. This linearisation defines an ellipsoid from which we can efficiently draw a large number of well-spread candidates. The underlying linear response map is refined online, and the ellipsoid is rebuilt accordingly. We demonstrate the method end-to-end on our key application - Tokamak divertor optimisation under plasma-boundary preservation.

---


### 277. [Toward Optimal Regret in Adversarial MDPs with Stochastic Hard Constraints](https://arxiv.org/abs/2610.12153)

**<font color=#1a73e8>作者：</font>** Qian Zuo, Francesco Emanuele Stradi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study episodic constrained Markov decision processes with adversarial losses under stochastic hard constraints. Specifically, starting from a known strictly feasible policy with margin $d$, we seek to obtain optimal regret while satisfying the expected cost constraints in every episode. In this setting, Stradi et al. (2025) show that a carefully designed mixing rule attains regret of order $\widetilde{\mathcal{O}}(\sqrt{T}/\min\{d,d^2\})$. Interestingly, they also provide a lower bound of order $\Omega(\sqrt{T}/\rho)$ for the same setting, where $\rho$ is the Slater margin of the offline problem and can be much larger than $d$. In this work, we build on their approach to obtain optimal regret dependence on these margins. Specifically, we propose MA-OPS, an algorithm that combines an optimistic search for the Slater margin with a pessimistic evaluation of the selected policies to safely learn a policy with a large feasibility margin. This policy is then used to minimize regret while satisfying the constraints at every episode. In particular, we show that MA-OPS attains regret $\widetilde{\mathcal{O}}(\sqrt{T}/\rho + 1/(d\rho))$. Finally, we provide a matching lower bound, showing that the dependence on $T$, $d$, $\rho$ in the regret bound is optimal up to logarithmic factors.

---


### 278. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](https://arxiv.org/abs/2610.12156)

**<font color=#1a73e8>作者：</font>** Dongbin Zhang, Chaoda Zheng, Kangjie Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To stream long videos while maintaining visual quality and temporal consistency, Self Forcing mitigates exposure bias through self-rollout training on self-generated histories with key-value (KV) caching. To keep memory manageable, it detaches historical caches, preserving forward dependencies between chunks but severing the backward gradient paths. We introduce Connected Self Forcing, a training framework that reconnects gradient paths across autoregressive chunks, allowing feedback from later predictions to guide how earlier context is generated. These connections go beyond historical KV-writing: gradients pass through generated latents into the computations that produced them, linking the generation of earlier context to its use in later predictions. To make this connected training memory-efficient, we develop shortcut gradient replay, which recovers cross-chunk gradients without retaining the full rollout computation graph. Integrated with distribution matching distillation, Connected Self Forcing trains historical chunks according to both their direct supervision and their contribution to subsequent generation. Experiments on autoregressive video generation show improvements in long-horizon visual quality and temporal consistency, without changing the inference procedure.

---


### 279. [When KL Regularization Misfires in Group Policy Optimization](https://arxiv.org/abs/2610.12161)

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why does removing reference-policy KL regularization sometimes improve group policy optimization? This motivates studying how reference-policy information should enter group-relative updates. We analyze seven potential failure modes in the interactions between KL and rewards: residual KL updates after reward clipping, after gradient cancellation, and in groups with identical rewards; KL growth with response length and an imbalance in its relative contribution; KL concentration on a small number of tokens; and sampling noise when k1 is incorporated into rewards. We propose Zero-Sum Calibrated Policy Optimization (ZCPO), which uses relative drift measured by conditional KL to calibrate within-group reward coefficients and integrates them into the base surrogate. Mathematical reasoning experiments and ablations support this design's effectiveness in our settings.

---


### 280. [Scalable Hierarchical Graph Generation via Soft Community Structure](https://arxiv.org/abs/2610.12163)

**<font color=#1a73e8>作者：</font>** Ahmet Tüzen, Helge Langseth, Kjetil Nørvåg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating large attributed graphs requires reproducing the topology, generating attributes jointly with the structure, and remaining scalable. Many real-world graphs exist as a single large graph, so a generative model has to generalize from the one graph it is fit on, without independent samples. We present Schema, which recursively decomposes a reference graph into a hierarchy of soft communities, assigning each node a membership distribution. Generation is then split into three stages, each trained independently: (1) synthesizing node attributes conditioned on soft memberships, (2) generating intra-community edges from local structural context, and (3) modeling inter-community connections over bridge nodes whose membership mass is distributed across several communities. No stage forms the full adjacency matrix, and each stage operates on a subgraph bounded by the community size. We also introduce an evaluation protocol that covers structural fidelity, memorization, downstream utility, and scalability. On four real-world attributed graphs, Schema recovers the balance between local and long-range structure more closely than any other model that generates attributes, while reproducing only a small fraction of the reference edges. It retains the downstream accuracy of the reference graph without raising it artificially above that level. Baselines that match its structural fidelity memorize the reference, while those with higher downstream accuracy either exceed the reference accuracy or fail to complete on the larger graphs. We measure scalability on six additional graphs with up to 10 million nodes.

---


### 281. [Is Real-World Training Data Necessary for Generalist Graph Anomaly Detection?](https://arxiv.org/abs/2610.12167)

**<font color=#1a73e8>作者：</font>** Yujing Liu, Yixin Liu, Yue Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalist graph anomaly detection (GAD) aims to build a foundation model that detects anomalies on arbitrary unseen graphs without retraining or fine-tuning. Sufficient data are essential for foundation model training, yet generalist GAD still faces a data shortage, as real-world anomalous graphs are scarce and costly to collect and annotate. To fill this gap, we propose AG-FORGE, an Anomalous Graph generation Forge for automatic synthesis of anomalous graphs, exploring the feasibility of synthetic data-driven training for generalist GAD. Empirically, we find that synthetic data can achieve performance comparable to real-world training, but fail to push the performance boundary further due to the limited capacity of existing methods. To further unlock model capacity as training data scale up, we develop TS-GGAD, a Topology-Semantic coordinated Generalist GAD that captures complementary topological and semantic anomaly evidence, together with a curriculum learning strategy tailored to large-scale synthetic training. Extensive experiments on 14 real-world datasets demonstrate that TS-GGAD, trained on data generated by AG-FORGE, significantly outperforms state-of-the-art methods.

---


### 282. [AI-Based On-Board Maritime Object Detection for Earth Observation Payload Data Reduction on Versal Embedded Hardware](https://arxiv.org/abs/2610.12182)

**<font color=#1a73e8>作者：</font>** Thomas Goudemant, Aurélien Bobey, Omar Hlimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Very-high-resolution Earth-observation satellites acquire more data than they can store and downlink, while in maritime surveillance the vessels cover a tiny fraction of each scene. We study onboard vessel detection as a way to select what is downlinked, which reduces the data according to its content rather than coding every pixel; it is complementary to conventional onboard compression. The work follows three axes. (i) Data and algorithm: a controlled dataset is generated from 68 annotated Maxar scenes with 43 vessel classes, and a YOLOX-S detector is trained on it. (ii) Embedded deployment: the detector is quantized and deployed on the DPU of a Versal VC1902, with a limited loss of detection quality and a processing time of a few seconds per scene. (iii) Data reduction: we propose several downlink modes, from metadata only (box, class and score of each detection) to image crops around vessels, tiles holding detections, or the whole scene with a degraded background, and estimate from the measured detection errors the trade-off each offers between the vessels kept and the volume downlinked. On our dense harbor and coastal scenes, tiles keep 98% of the vessels with 29% of the scene volume, and crops 83% with 3%.

---


### 283. [Just Weather Scoring: Efficient End-to-end Nowcasting with Distributional Diffusion](https://arxiv.org/abs/2610.12189)

**<font color=#1a73e8>作者：</font>** Jannik Wiese, Johannes Schusterbauer, Tommaso Martorella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative diffusion models are well-suited for probabilistic precipitation nowcasting, but existing approaches often rely on separately trained compression or deterministic forecasting components and remain costly at inference due to iterative denoising. We introduce Just Weather Scoring (JWS), a single-stage, end-to-end diffusion model which addresses both issues by forecasting directly in radar space and enabling few-step generation. Radar-space modeling greatly simplifies training and inference and eliminates uncertainty arising from lossy compression. JWS combines Masked Asynchronous Diffusion, a timestep-sampling scheme that preserves clean context while adapting diffusion training to high-dimensional spatio-temporal data, with a simple scoring-rule objective that aligns training with probabilistic forecasting and unlocks few-step generation. On the SEVIR and MeteoNet benchmarks, JWS achieves state-of-the-art probabilistic forecasting performance at reduced training and inference cost. Even our smallest model remains competitive using substantially fewer parameters and more than 17x faster inference.

---


### 284. [Verification with Transfer: Exact Information Frontiers and Their Price in Calls](https://arxiv.org/abs/2610.12211)

**<font color=#1a73e8>作者：</font>** Hazar Yueksel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A verifier that accepts or rejects whole answers reveals little: under a flat prior over $k$-bit answers, zero error needs $2^k-1$ verifications. The usual remedy is to solve related source tasks, either all first, as a curriculum does, or interleaved with verification. We price this remedy in information and in calls. With an exact verifier, the least causal information that any interleaving of source calls and $n$ verifications needs to succeed with probability $s$ is a list rate-distortion function, attained by one observation before any verification. It lower-bounds the expected number of binary source calls, which designed sources meet within $1+\log_25$ calls for unique answers and within a logarithmic term in general, where no additive constant suffices. With an exact verifier and fixed sources, moving every call before the first verification preserves all hard caps on calls, although interleaving can save unboundedly many expected calls; under a noisy verifier, source-first protocols can lose unbounded factors in information and in error. For linear banks over $\mathbb{F}_2$, optimal accuracy has a closed form, and after a polynomial-time reduction the budget profile is computable in time $2^{O(h^2)}\operatorname{poly}(J,k+h)$ for $J$ sources and nuisance dimension $h$. In these banks, for zero error under a hard cap, the calls beyond the rounded-up information price are exactly those spent on nuisance. Every numbered result apart from two clauses about the planner is machine-checked in Lean 4, assuming two published results. Used as a ruler, the frontier shows a small transformer using all delivered bits at latent dimension $5$ and none at $11$ within fixed training budgets; in a test with predictions recorded before training, low XOR degree of the target bits did not suffice for their use.

---


### 285. [When Has a Bayesian Neural Network Sampled Enough? Adaptive Inference Time with Statistical Guarantees](https://arxiv.org/abs/2610.12212)

**<font color=#1a73e8>作者：</font>** Fabian Denoodt, Sibylle Hess  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian neural network predictions are commonly approximated using a fixed number of Monte Carlo samples per input, without controlling the resulting error that comes from this finite sample. We propose the use of confidence sequences to dynamically determine how many samples are needed while maintaining statistical guarantees. We consider several ways in which predictive probabilities are used, including identifying the most likely class, approximating the full predictive distribution, and resolving probability-threshold decisions. Sampling stops once the corresponding decision can be made with the desired guarantee. Experiments show that the method allocates the computational budget efficiently, assigning more samples to ambiguous inputs than to easy inputs while preserving reliable decisions and reducing overall latency relative to a fixed Monte Carlo budget.

---


### 286. [Stride Independent Patching for Deep Learning](https://arxiv.org/abs/2610.12216)

**<font color=#1a73e8>作者：</font>** Olivier Rukundo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents semi-automatic stride-independent patching (SSP) as an alternative to automatic stride-dependent patching techniques. SSP uses user or expert input to position predefined patches over one or more objects of interest. To evaluate its effectiveness, three patch-based datasets were created using SSP, overlapping patching (Overlap), and non-overlapping patching (Noverlap). DeepLabV3+ models with ResNet50, ResNet18, and MobileNetV2 backbones were trained sepa-rately on each dataset. Quantitative evaluations were performed on the respective test splits and a common external test set. SSP generally achieved higher segmentation scores on the test splits and required the shortest model training time across all three backbones. On the external test set, SSP achieved the highest average precision and F1-score across backbones, whereas Noverlap achieved the highest average recall. These preliminary results demonstrate that the potentially greater spatial coverage of Noverlap and Overlap does not generally translate into better segmentation perfor-mance and that SSP offers a favorable balance between segmentation performance and model training time.

---


### 287. [One Node, Two Roles: Simultaneous Contests for Validation and Attention in Rollups](https://arxiv.org/abs/2610.12220)

**<font color=#1a73e8>作者：</font>** Pranay Anchuri, Ben Berger, Matteo Campanelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An optimistic rollup is safe as long as at least one honest validator executes its state transition function (STF) and disputes any assertion that is inconsistent with the result of the execution. Allowing anyone to participate, however, does not give incentive to do so: as long as every assertion is correct, verifying assertion correctness goes unpaid. Attention mechanisms address this by paying nodes to execute the rollup's STF, regardless of whether they participate in the validation process. Since a single node operator can back many registered identities with a single execution, paying per identity does not buy execution diversity, that is, the number of operators that independently execute. In this work we provide a new modeling framework for this problem. We formalize the underlying cryptographic primitive as a new notion, arguments with registered provers, whose properties include a form of non-amortizability that, to our knowledge, has not been studied for modern succinct cryptographic proofs before. We design validation and attention reward mechanisms and analyze them as two coupled Tullock-like contests, in which an operator pays once for the required execution and then chooses how many identities to deploy in each role. We quantify the attainable range of execution diversities in equilibrium as a function of the marginal cost of deploying an extra attention identity. We use our framework as a lens through which we compare two attention mechanisms, TRACE (MARBLE 2026) and Proof of Diligence (AFT 2024). In particular, we show that as opposed to Proof of Diligence, in TRACE the marginal cost mentioned above can be adjusted to support a higher execution diversity. As a case study, we apply our results to Arbitrum One, a widely deployed optimistic rollup.

---


### 288. [From Prompting to Composing: A Spatial Canvas Interface for Poster Generation](https://arxiv.org/abs/2610.12230)

**<font color=#1a73e8>作者：</font>** Yitong Wang, Fangyun Wei, Jinjing Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text prompting is an indirect interface for poster generation, requiring users to encode inherently two-dimensional composition intent into a one-dimensional sequence of words. We introduce a Spatial Canvas Interface that enables users to directly compose generation intent in space through four complementary binding types: semantic, identity, text, and pixel, together with Text Specifications for individual elements and global appearance. Based on this interface, we develop Compo, a poster generation model adapted from a pretrained image editing model to understand Spatial Canvas inputs and Text Specifications. Compo supports both direct inference, where users explicitly construct the canvas, and agentic mode, where a high-level request is automatically translated into a planned Spatial Canvas. To train Compo, we develop a scalable pipeline that automatically constructs supervision data for different binding types and their combinations, enabling efficient adaptation without training a specialized poster generator from scratch. We further introduce a benchmark that evaluates adherence to individual binding types and their joint composition. Experiments show that Compo achieves stronger compositional controllability than both general-purpose image generation models and dedicated poster generation systems while maintaining high visual quality. By decoupling intent specification from visual generation, our work shifts poster generation from prompting toward composing.

---


### 289. [Training on the Future: A Delay-Aware Audit of Test-Time Adaptation for Time-Series Forecasting](https://arxiv.org/abs/2610.12232)

**<font color=#1a73e8>作者：</font>** Mohamed Readh Fentazi, Mazene Ameur, Adlen Ksentini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) methods for time-series forecasting update a deployed model, or a small adapter around it, from incoming ground truth. But the label of an $H$-step forecast exists only $H$ steps later, and real data pipelines add further delay. We build a leakage-free harness in which the label of forecast origin $s$ is released for updates only at step $s+d$ with $d \ge H$, and enforce this rule inside the released code of four recent TTA methods (TAFAS, COSA, PETSA and DynaTTA), run on their own backbones and checkpoints across five benchmarks (ETTm1, ETTh2, Weather, Electricity and Traffic). As references we add two closed-form correctors: a bank of recursive least squares (RLS) filters combined by a per-coordinate median, with no tunable hyperparameters and 56 microseconds per step on the 7-channel streams, and an ELF-style linear corrector. Under causal delayed labels the picture is asymmetric. On ETTm1 every audited method genuinely adapts, yet the RLS bank still beats three of the four at a fraction of their cost; only DynaTTA beats the bank, only at the minimum causal delay, and at roughly 2,500 times the per-update cost; the ELF-style corrector beats all four. On the other four datasets, the largest statistically significant improvement any published method achieves over its own frozen checkpoint is half a percent, on all four at least one published method is significantly worse than the frozen model at the minimum causal delay, and on drift-heavy ETTh2 longer label delays make every adapter that separates from the frozen model, ours included, significantly harmful. Leaky next-step updates inflate the apparent gains of simple adapters by up to 110%, and the backbone training recipe moves frozen online error by up to a factor of 25, more than any adaptation effect we measure. We release the harness, integration patches and all cached runs.

---


### 290. [AdaCast: Conditional Parameter Generation for Adaptive Time Series Forecasting](https://arxiv.org/abs/2610.12240)

**<font color=#1a73e8>作者：</font>** Darahaas Nallagatla, Darryl Cherian Jacob, Pan He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) have achieved strong forecasting performance across domains. However, most adaptation methods remain static. Existing all-in-one methods learn a single set of dataset-level parameter updates and apply the same adapted model to every input. As a result, they cannot adapt the model parameters to the temporal patterns, seasonality and dynamics of each input time series. This limits their ability to produce forecasts that are tailored to heterogeneous inputs. To address this limitation, we propose AdaCast, a conditional parameter generation framework for time-series forecasting. AdaCast uses a generator to produce input-specific low-rank parameter updates for a frozen pretrained TSFM. These updates adapt the model to each input during both training and inference. Across six public benchmarks, AdaCast consistently outperforms static adaptation baseline in in-domain forecasting and improves zero-shot generalization to held-out datasets across domains. These results demonstrate that conditional parameter generation provides an effective approach for adaptive forecasting.

---


### 291. [RIFT: Relative Isolation From Trees For Anomaly Detection](https://arxiv.org/abs/2610.12244)

**<font color=#1a73e8>作者：</font>** Mark Daniel Szalai, Gabor Horvath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Isolation Forest (IF) is a widely used baseline for unsupervised anomaly detection. Recent studies provide a closed-form expression for the infinite-forest limit for one-dimensional data. Inspired by the geometric interpretation of this formula, we introduce RIFT (Relative Isolation From Trees), a deterministic anomaly detection method that generates the minimum spanning tree and scores each point by the sum of the apparent sizes of tree edges as viewed from that point. For one-dimensional data, the RIFT score recovers the closed-form IF limit exactly. In higher dimensions, it provides a parameter-free generalization that is deterministic, robust to varying density and clustered anomalies and avoids the axis-parallel artifacts of IF. We further propose an ensemble variant for large datasets. Experiments on synthetic data and the ADBench benchmark demonstrate that the accuracy is comparable to IF, while the ensemble variant exhibits significantly lower variance across random seeds.

---


### 292. [Batch Before You Lift: Scalable Topological Deep Learning on Large Graphs](https://arxiv.org/abs/2610.12247)

**<font color=#1a73e8>作者：</font>** David Leko, Luka Benić, Guillermo Bernárdez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes. These domains are typically constructed from patterns in an input graph through a process of graph lifting. Full-domain training constructs and stores the complete lifted representation before model execution. On large and dense datasets like Reddit (233k nodes and 57.3M edges), this global materialization becomes a severe computational bottleneck, often rendering training infeasible. To address this limitation, we introduce Cluster-TNN, a domain-agnostic framework that avoids this bottleneck by lifting locally instead. After partitioning the input graph during preprocessing, at runtime Cluster-TNN dynamically samples groups of node clusters, reconstructs their induced subgraphs to form mini-batches, and applies the chosen lifting within each mini-batch. Retaining all edges among sampled nodes preserves the connectivity needed to construct higher-order structures across clusters, producing topological mini-batches that existing Topological Neural Networks can process directly. Across 21 matched comparisons with full-graph execution, Cluster-TNN reduces peak GPU memory in every configuration, by 83.2% on average while maintaining competitive predictive performance. Notably, such a reduction enables, to our knowledge, the first training of multiple different higher-order Topological Neural Networks on large datasets such as Reddit and OGBN Products. These results establish Cluster-TNN as a general strategy for scaling Topological Deep Learning beyond the limitations of global domain construction.

---


### 293. [Syn-Omni: Structured Specialization and Progressive Collaboration for Omnimodal Embeddings](https://arxiv.org/abs/2610.12256)

**<font color=#1a73e8>作者：</font>** Youngtaek Oh, Qiyu Wu, Hiromi Wakaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal embeddings naturally involve both shared representations and modality-specific features across heterogeneous inputs. However, existing omnimodal embedding methods often rely on a single shared parameter space over mixed-modality data, limiting structural separation between universal and modality-specific representations. To address this, we propose Syn-Omni, a unified framework for structured omnimodal adaptation with modality specialization and controlled cross-modal collaboration. Specifically, we introduce Orthogonal Modality-Expert LoRA (OME-LoRA), which decomposes adaptation into a shared LoRA path for universal semantics and modality-expert LoRA paths for modality-aware specialization. Furthermore, Progressive Synergy Routing (PSR) enables experts to first establish modality-specific priors, then gradually interact with other modality-experts for cross-modal synergy. Evaluated across 81 diverse tasks spanning image, video, audio, and audiovisual modalities, Syn-Omni consistently outperforms omnimodal baselines, demonstrating the effectiveness of structured specialization and cross-modal progressive collaboration.

---


### 294. [AdaptLSTM: Efficient Adaptive Online Learning for Cloud Workload Forecasting under Distribution Drift](https://arxiv.org/abs/2610.12265)

**<font color=#1a73e8>作者：</font>** Xinhua Miao, Bowei Yang, Zhengong Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate workload forecasting is critical for elastic resource provisioning in web-scale cloud services, where distribution shifts driven by viral content, product launches, and user behavior degrade offline-trained models rapidly. Naive online learning recovers accuracy but incurs prohibitive per-step compute cost. We propose AdaptLSTM, an adaptive online framework that detects drift via validation-calibrated thresholds and applies selective, targeted updates. On the Alibaba Machine Trace, AdaptLSTM recovers 54\% of Naive Online's improvement at 20\% cost ($2.7\times$ efficiency, $p=0.002$ over 10 seeds). On the more volatile Container Trace, it achieves 96\% at 20\% cost ($4.8\times$ efficiency, $+75\%$ MAE reduction over Static). Unlike classical drift detectors (ADWIN, DDM, Page-Hinkley) which fail to trigger on regression-scale error streams, AdaptLSTM fires 42 times over 301 steps and outperforms matched-budget baselines. Wall-clock profiling shows $1.33\times$ throughput gain and 45\% update-time reduction. The framework is model-agnostic: identical Pareto patterns hold for LSTM, GRU, and Transformer backbones.

---


### 295. [Slot3R: Set-Associative Spatial Memory for Streaming 3D Reconstruction](https://arxiv.org/abs/2610.12282)

**<font color=#1a73e8>作者：</font>** Xiyuan Zhang, Yanming Yang, Kaiyuan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction must preserve evidence from each frame while processing an expanding scene online. Spatial memory is a natural fit because it organizes history by reconstructed 3D location. Yet Point3R uses spatial proximity both to associate a new observation with an existing memory entry and to decide whether to fuse it, conflating co-location with state identity. Because pointers summarize image patches, nearby pointers may encode distinct surfaces, viewpoints, or visibility conditions; averaging them can destroy complementary evidence before later frames disambiguate it. We argue that location should determine address, not whether observations must merge. Slot3R realizes this principle as a training-free, set-associative retrofit that lets multiple states coexist at a shared address while keeping the pretrained Point3R backbone frozen. A bounded sparse readout further decouples persistent storage from per-frame decoder access. At 300-500 sampled frames, Slot3R reduces Point3R's point-cloud accuracy error (Acc) by 57.1%-63.1% on 7Scenes and 64.0%-72.0% on NeuralRGBD, lowers Sim(3)-aligned absolute trajectory error (ATE) on all three pose benchmarks, and remains competitive on video-depth estimation. It completes all evaluated settings from 600 to 1000 sampled frames at about 19 FPS under the same protocol, whereas Point3R and InfiniteVGGT run out of memory at 800 frames and beyond.

---


### 296. [Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction](https://arxiv.org/abs/2610.12299)

**<font color=#1a73e8>作者：</font>** Dahyun Chung, Siyoon Jin, Hyunwook Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate multi-agent egocentric world modeling as synchronized ego-stream generation for multiple agents interacting through fine-grained actions in a shared world. This requires cross-view action consistency, shared-environment consistency, and consistent propagation of interaction-induced state updates. We propose Multi-agent Egocentric World Model (ME-World), which jointly denoises multiple ego streams in a shared token sequence, conditions each stream on all agents' target-view poses, and grounds generation with shared environment memory. We train and evaluate on real and synthetic multi-agent data and introduce shared-world consistency metrics for environment, update, and identity consistency. Experiments show ME-World improves shared-world consistency, action control, identity preservation, and video quality over existing methods.

---


### 297. [A Structural Theory of Cognitive Representation and Problem Solving,Contexts, Invariance, and the Knowledge Space](https://arxiv.org/abs/2610.12306)

**<font color=#1a73e8>作者：</font>** Antal Jakovác, András Telcs  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning and problem solving depend critically on the structure of internal representations. While many modern data-driven artificial systems achieve strong predictive performance, their learned representations often lack explicit structure for expressing abstraction, invariance, and task-relevant regularities. We propose a minimal structural framework in which representational operations relevant to problem solving, such as context formation, invariance recognition, representative selection, abstraction, and procedural reuse, are made explicit. The central notion is that of a \emph{context}, formalized as a partition of a subset of an underlying state space, which fixes the distinctions, granularity, and form in which a problem can be posed. Within this setting, invariance recognition and representative selection are treated as fundamental representational operations. The framework is realized as a Knowledge Space composed of two coupled graph structures: a Concept Graph that hosts constructed and refined concepts, and a Procedure Graph that encodes typed operations over representations. Together, these structures provide a minimal cognitive-representational algebra for operating on representations without assuming sophisticated inference, learning, control, perception, or motor mechanisms. Using simple illustrative examples and a finite weak-solver demonstration, we show that appropriate representational organization can simplify the form and scope of admissible regularities, even when problem solving is carried out by a fixed and limited solver. The contribution of the paper is structural rather than algorithmic: it identifies representational prerequisites for abstraction, invariance, and procedural reuse in problem solving, and states explicit success and failure conditions for the weak-solver setting.

---


### 298. [Controllable Exaggeration for Generative Motion Models via Training-Time Adaptation and Inference-Time Guidance](https://arxiv.org/abs/2610.12316)

**<font color=#1a73e8>作者：</font>** Amirhossein Zamani, Arianna Rampini, Bruno Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent motion generative models have demonstrated strong capabilities in synthesizing physically plausible character motion, but often overlook established animation principles used by professional animators to ground and design their animation work. Understanding and incorporating these principles into motion generative pipelines is essential for producing motions that serve not only physically grounded applications but also the needs of the character animation community. This enables the creation of characters that not only move in physically plausible ways but also feel alive, expressive, and engaging. To close this gap, we focus on the Exaggeration principle of animation and investigate how it can be incorporated into modern motion generative pipelines to produce more expressive character motions. To this end, we introduce a framework that operates at two stages of existing motion generative pipelines. The first stage introduces exaggeration during training, where we perform supervised fine-tuning of pre-trained text-to-motion models on our curated exaggeration dataset. The second stage operates at inference time, where we: (i) introduce a mathematical formulation of exaggeration based on dynamic movement primitives (DMPs); and (ii) leverage this formulation as an exaggeration guidance signal to guide existing diffusion and flow-matching text-to-motion generation models toward exaggerated motion without additional training. Through qualitative and quantitative evaluations against three strong motion generation models, we show that our methods generate more exaggerated and expressive motions while preserving neutral reference motion intent and physical plausibility.

---


### 299. [Spatial Pattern Formation from Multi-Agent Learning in Public Goods Dilemmas](https://arxiv.org/abs/2610.12321)

**<font color=#1a73e8>作者：</font>** Yefei Zhang, Yuxuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Spatial public goods models show that prescribed movement toward richer locations can generate spatial patterns. We ask how such patterns emerge when agents learn where to move and how learning rates shape their consequences for collective welfare. Fixed populations of cooperators and defectors independently learn movement policies using tabular Q-learning and local observations. Cooperator learning generates clusters around resource peaks, while co-adaptation changes their strength and motion. At a fixed training budget, the largest welfare losses occur when cooperators learn at high rates and defectors at low rates. In part of this regime, learned policies also generate traveling bands supported by a shared directional preference. The conditions supporting travel change with further training, so these patterns reflect training history rather than an established asymptotic outcome. Across the tested learning-rate conditions with cooperator learning, mean collective welfare falls below random movement because increased crowding outweighs gains in resource benefit. Charging agents for the crowding they impose on others during learning recovers much of the welfare loss in the tested conditions. These results connect learning rates to the emergence and welfare costs of spatial organization driven by individual rewards.

---


### 300. [Composite Online-to-Nonconvex Conversion with Optimal Oracle Complexity](https://arxiv.org/abs/2610.12328)

**<font color=#1a73e8>作者：</font>** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider stochastic nonsmooth nonconvex composite optimization, which includes several important problems such as constrained optimization and the regularized training of neural networks. The objective is the sum of a possibly nonsmooth nonconvex Lipschitz function and a convex regularizer, and the function is accessed through stochastic gradients or function values. The goal is to find a point that satisfies a Goldstein-type stationarity condition designed for composite objectives. To our knowledge, no oracle complexity bound for this setting is known under first-order access, and existing complexities under zeroth-order access are suboptimal. To handle this issue, we employ the framework of online-to-nonconvex conversion, which chooses update directions by an online learner and is known to achieve optimal rates for noncomposite problems. We extend the framework to our composite scenario by introducing new losses for the learner, which contain the regularizer itself rather than its linearization and for which a variant of online mirror descent achieves low regret. We show that the resulting algorithm finds such a point with $O(\delta^{-1}\varepsilon^{-3})$ stochastic gradient queries or $O(d\delta^{-1}\varepsilon^{-3})$ function-value queries, where $\delta$ is the Goldstein radius, $\varepsilon$ is the stationarity tolerance, and $d$ is the dimension. These rates match the optimal ones for noncomposite nonsmooth nonconvex optimization, demonstrating that the additional convex regularizer does not worsen the oracle complexity. We also give rates for the smooth case and present numerical experiments.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
