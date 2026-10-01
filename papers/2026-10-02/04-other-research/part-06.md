# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-382](./part-08.md)

---

### 251. [Lens Flare Removal and Reconstruction](https://arxiv.org/abs/2609.39527)

**<font color=#1a73e8>作者：</font>** Tarun Yenamandra, Jonathon Luiten, Daniel Cremers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The presence of lens flares in images can significantly reduce the quality of downstream application results for tasks such as 3D scene reconstruction. This is because lens flares are a property of the camera imaging system, and not a part of the underlying scene being modeled. There are previous methods that tackle the removal of small flares focused around a light source. However, existing methods struggle with large flares, such as those that fill the entire image. In this work, we compile a novel dataset for large-flare removal, combining publicly available real-world data with a procedural generation pipeline. We fine-tune a diffusion-based model on our dataset to remove complex, large lens flares. On the other hand, lens flares remain effective artistic tools, widely used in the media. While there are ways to simulate 2D flares, representing and reconstructing lens flares consistently across multiple views has not yet been explored. To achieve this, we introduce a flare representation model that leverages the symmetry of lens flares about the camera's principal point. We propose a computational pipeline to jointly optimize this flare model and a Gaussian splatting model (3DGS). This enables the decomposition of a 3D scene into lens flares and the scene itself, using our flare-removal model. Because the reconstructed flare is explicit and re-renderable, it can be edited and transferred to novel images and new 3D scenes. We evaluate removal on an established benchmark and a new one for large reflective flares, quantify the flare/scene decomposition directly, and show that the pipeline is robust to errors in automatic light-source localization.

---


### 252. [Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean](https://arxiv.org/abs/2609.39544)

**<font color=#1a73e8>作者：</font>** Jules Viennot, Guillaume Baudart, Marc Lelarge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent achievements in AI-assisted mathematics require intensive interaction of agents with proof assistants to generate machine-checked proof certificates. Agents interact with proof assistants such as Rocq or Lean through an interface that controls what the agent receives from the prover and the cost of these interactions. Today, these interfaces are adapted from tools designed for humans and not optimized for agents. We propose an evolutionary method where a frontier model incrementally proposes new features and only keeps the ones that improve the overall performance of smaller models. We demonstrate the effectiveness of our method by growing, on a curated set of mathematical problems, \rme, a new MCP server for the Rocq prover. On the held-out \texttt{test} split of miniF2F-Rocq, an agent equipped with \rme outperforms both the baseline that only exposes the Rocq compiler and an established MCP server, across four models from two families, in success rate, cost per solve, and time per solve. Although evolved for Rocq, the resulting server transfers to Lean, improving cost and time per solve on a subset of PutnamBench. We release \rme and its port to Lean.

---


### 253. [Learning Normal Diffusion Dynamics for Backdoor Defense in Text-to-Image Models](https://arxiv.org/abs/2609.39548)

**<font color=#1a73e8>作者：</font>** Junjian Li, Xiaolong Liu, Peng Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a serious threat to the secure deployment of text-to-image (T2I) diffusion models. Existing defenses typically detect backdoors from specific abnormal patterns in internal representations, which may limit their generalizability with the emergence of increasingly diverse attack mechanisms. In this paper, we study backdoor defense of T2I diffusion models from a transition-dynamics perspective. We observe that benign diffusion trajectories exhibit structured and timestep-dependent transition patterns from cross-attention, latent and noise spaces, whereas backdoor attacks tend to induce deviations from such normal evolution. Motivated by these observations, we propose Normal Diffusion Dynamics Learning (NDDL), a novel backdoor defense framework that learns the normal transition dynamics of diffusion trajectories utilizing only benign samples. NDDL constructs compact multi-space trajectory representations and trains a timestep-conditioned dynamics model to predict the diffusion evolution. In the inference phase, deviations between the observed and predicted transitions are exploited to quantify dynamics inconsistency for backdoor detection. NDDL further enables trigger localization without any prior knowledge of the embedded backdoor by performing substitution with low-semantic words. Extensive experiments for diverse backdoor attacks demonstrate the effectiveness and generalizability of our proposed NDDL.

---


### 254. [Hyperbolic Prototype Routing for Rehearsal-Free Class-Incremental Learning](https://arxiv.org/abs/2609.39550)

**<font color=#1a73e8>作者：</font>** HongWei Zhao, Rui Liu, Yong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) aims to continually learn new classes while preserving prior knowledge. Parameter-efficient fine-tuning with pre-trained models enables CIL with minimal parameter updates, but existing approaches still suffer from catastrophic forgetting caused by cumulative interference and suboptimal module-sample matching at inference. We propose Hyperbolic Prototype Routing (HyPro), a rehearsal-free framework for continual learning. HyPro allocates a dedicated LoRA-Expert module to each incremental task for isolated representation learning, then projects routing features onto a Poincare ball and performs geodesic nearest-prototype matching for reliable task-level discrimination. Extensive experiments on standard CIL and Few-Shot CIL benchmarks show that HyPro consistently improves average and final-stage accuracy over strong baselines.

---


### 255. [EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553)

**<font color=#1a73e8>作者：</font>** Changbai Li, Shuo Yang, Yichen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis, but existing general-purpose acceleration methods suffer severe rendering quality degradation when extended to more complex, large-scale scenes. To address this issue, we propose EffGS, a more general acceleration framework that improves training and rendering efficiency while maintaining reconstruction quality comparable to or better than vanilla 3DGS across bounded and large-scale scenes. EffGS combines frequency-aware guidance, localized density control, and adaptive primitive scale modulation. First, an importance scoring mechanism combines pixel-wise reconstruction errors with a difference-of-Gaussians mask scheduled over training to provide stage-dependent spatial guidance. Second, localized densification and pruning restricts density modifications to Gaussians with valid projected footprints in the sampled views. Third, learnable per-Gaussian scale modulation adjusts effective primitive extent during optimization while retaining the Compact Box rasterization rule. Extensive experiments on bounded and large-scale scene datasets demonstrate a favorable balance between reconstruction quality, training time, and primitive count. Component ablations and matched-primitive-budget comparisons further support the effectiveness of the framework.

---


### 256. [Divide and Collapse: MAPF-Collapse via Exact Decomposition into Independent Sub-Instances](https://arxiv.org/abs/2609.39559)

**<font color=#1a73e8>作者：</font>** Oren Salzman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work we study the problem of MAPFC, a post-optimization step for Multi-Agent Path Finding (MAPF) plans where we are given a feasible plan produced by a modern MAPF solver and are tasked with removing avoidable moves while preserving feasibility. This NP-hard problem naturally arises when using learning-based state-of-the-art (SOTA) solvers which construct plans that contain redundant moves that can be removed. Recently, Tang et al. presented Judgelight, which uses Integer Linear Programming (ILP) to solve MAPFC. Importantly, the ILP is constructed over all agents jointly, so its cost is governed by the full instance rather than by the small coupled residue that actually requires joint reasoning. Our key insight, motivating this work, is that MAPFC instances naturally decompose into independent sub-problems, most of which involve a single agent and can be solved without any inter-agent reasoning. To this end, we first identify which agents need to coordinate their motion and partition the instance into sub-problems accordingly. For the cases where no coordination is required, we introduce an extremely lightweight solver that is $\approx\!1{,}900\times$ faster than Judgelight. For cases where coordination is required, Judgelight can be used but we introduce an alternative CBS-like solver which is more efficient on easier problems. The resulting framework is exact, uses no commercial ILP solver, and matches Judgelight's quality while running substantially faster on the coordination-light majority of instances; on the coordination-heavy instances we propose a regime-aware hybrid planner that falls back to Judgelight. Over all benchmarks tested, this planner achieves a median $10.5\times$ per-instance speedup over Judgelight.

---


### 257. [Candidate Retention for Abductive Learning](https://arxiv.org/abs/2609.39561)

**<font color=#1a73e8>作者：</font>** Hao-Yuan He, Yu Liu, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abductive learning combines neural perception with symbolic reasoning, using explanations generated by abduction to supervise the perception model. Multiple valid explanations of the same symbolic target can assign conflicting labels to the same inputs. Common policies select a single candidate as a pseudo-label, which may reinforce mistaken assignments, or weight all candidates, which may spread supervision across competing labels. These risks motivate selecting a retained subset to balance supervision sharpness and model-mass coverage. To guide this choice, we bound the coordinate-level supervision error using retained uncertainty, discarded model mass, and model mismatch. For a fixed model and training pair, only the first two terms depend on the retained set. We propose Abductive Candidate Retention (ACR), which uses these terms to guide greedy additions, accepting a candidate when its recovered mass exceeds the increase in retained uncertainty. Experiments show that ACR improves concept accuracy over single-candidate baselines and A3BL in most evaluated aggregated mod-addition settings. Objective ablations support the joint use of uncertainty and posterior mass.

---


### 258. [Invariant Shape Analysis of Surfaces with Spherical Topology](https://arxiv.org/abs/2609.39567)

**<font color=#1a73e8>作者：</font>** T. Shaska, M.-R. Siadat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spherical harmonic descriptors of closed 3D shapes depend on the parameterization, the pose and the scale of the surface, and the standard rotation-invariant reductions, the power spectrum and the bispectrum, discard the relative orientation of the harmonic bands and cannot distinguish a shape from its mirror image. We construct a descriptor that removes all three dependencies exactly and loses nothing else: a conformal parameterization normalized by its conformal barycenter, followed by polynomial invariants of the rotation group. Identifying each harmonic band with a binary form turns the rotation quotient into classical invariant theory and makes reflections visible as the sign of an invariant, so chirality is recorded. The descriptor is complete for the truncated expansion, stable in the orbit distance, and comes with numerical diagnostics. Benchmarks confirm the guarantees, and on bilateral anatomical structures the descriptor separates mirror-image pairs from asymmetric pairs, which parity-blind descriptors cannot.

---


### 259. [Steering Fields: Adaptive Vector Fields for Safe Image Generation and Beyond](https://arxiv.org/abs/2609.39573)

**<font color=#1a73e8>作者：</font>** Simone Facchiano, Jan Eric Lenssen, Bernt Schiele 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As state-of-the-art text-to-image flow models achieve near-photorealistic quality, controlling their outputs, e.g., suppressing harmful content while promoting benign alternatives, has become a central challenge. The current steering paradigm consists of adding a global steering vector to selected activations. While functional, a fixed and example-agnostic vector applied uniformly along the entire trajectory cannot adapt to the changing state of the generation and often causes unintended global changes. We introduce Steering Fields, a generalization of steering vectors that adaptively re-estimates the steering direction at each step of the generative process. Steering Fields operate on the noisy states of flow models, expose a continuous trade-off between steering strength and content preservation, and are compositional, enabling the simultaneous induction and inhibition of concepts, setting a new state of the art on safety steering benchmarks. Despite using no explicit spatial masks or object priors, the trajectory-adaptive estimation naturally preserves local structure, in a manner reminiscent of image editing. In fact, Steering Fields can serve as a structure-preserving image-editing technique that achieves state-of-the-art semantic fidelity (CLIP, VQAScore), while remaining model-agnostic and inversion-free.

---


### 260. [AVERT-VLN: Abstention-aware Visual Error Recovery and Training for Vision-and-Language Navigation](https://arxiv.org/abs/2609.39579)

**<font color=#1a73e8>作者：</font>** Minrui Liu, Jingke Wang, Yuehao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying vision-and-language navigation (VLN) agents in unseen environments remains challenging because unfamiliar layouts and visual conditions can cause execution to go off track. Rather than relying on continuous human supervision, a practical strategy is to selectively request corrective guidance, recover the ongoing task, and reuse corrective interactions to improve subsequent navigation. We propose Abstention-aware Visual Error Recovery and Training for Vision-and-Language Navigation (AVERT-VLN), a closed-loop framework that uses a plug-in vision-language Monitor for online human-assisted recovery and offline preference learning. The Monitor operates separately from navigation decision generation and assesses instruction-execution consistency from the instruction, visual history, and current observation. To train the Monitor for deviation recognition, we construct LOSTNAV DATASET with 20K counterfactual risk trajectories and rule-based deviation labels. The Monitor is first fine-tuned on 40K normal trajectories to assess instruction progress and then jointly fine-tuned on normal and risk trajectories to recognize semantic deviations. At runtime, Asynchronous Sidecar Monitoring evaluates execution alongside the navigation model. When the controller accepts a LOST verdict, it suspends autonomous execution and requests human guidance for recovery. For offline policy improvement, Trajectory-Anchored Preference Learning converts deviation-associated failures into decision-level preference pairs under shared decision contexts, restricting supervision to the decisions targeted for correction. Under human-assisted evaluation, the full AVERT-VLN system achieves success rates of 76.2% and 66.3% on the val-unseen splits of R2R-CE and RxR-CE, respectively. The same monitoring and human-assisted recovery interface also improves success rates across the three evaluated navigation architectures.

---


### 261. [Robust Transfer Learning for Paper ECG Recognition](https://arxiv.org/abs/2609.39581)

**<font color=#1a73e8>作者：</font>** Yinghao Xie, Zhenbang Dai, Haojun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Paper ECG recognition is challenging because real-world ECG images vary in layout, physical artifacts, and label availability. We introduce RobECG-CL, a rank-aware contrastive learning framework for robust paper ECG representation learning. Starting from standard 12-lead ECG recordings, we construct progressively degraded paper ECG views with heterogeneous layouts and train the model to balance same-recording invariance with degradation-aware ordering. Across synthetic stress tests on CODE-II and EchoNext, RobECG-CL improves robustness under severe degradation and few-shot transfer, outperforming contrastive learning baselines and surpassing the waveform-based foundation model, ECG-FM, in the 1% labeled setting. On 312 samples of hospital data with 37 labels, RobECG-CL achieves the best macro AUROC.

---


### 262. [Cybersecurity in Edge Computing: A Trust-Aware Federated Hybrid Intrusion Detection Framework](https://arxiv.org/abs/2609.39584)

**<font color=#1a73e8>作者：</font>** Zawad Yalmie Sazid, Robert Abbas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge computing has emerged as a critical computing paradigm in modern distributed systems by migrating data processing closer to end users and Internet of Things (IoT) devices. While this paradigm decentralizes processes, minimizes latency, and reduces backhaul bandwidth congestion, it exponentially enlarges the cyberattack surface. Heterogeneous, resource-constrained edge devices deployed across unmanaged administrative domains present highly vulnerable targets. To address these vulnerabilities without compromising global data privacy regulations, this paper proposes a novel Trust-Aware Federated Hybrid Intrusion Detection Framework (TA-FHIDF). The proposed framework integrates an Autoencoder, a 1D Convolutional Neural Network (1D-CNN), and a Bidirectional Long Short-Term Memory (BiLSTM) model into a unified, localized deep learning engine capable of autonomous spatial and temporal feature extraction. Model training is performed collaboratively via federated learning, ensuring raw network telemetry remains isolated at local gateways. Furthermore, to defend against adversarial model poisoning attacks, we introduce a robust server-side trust-aware aggregation mechanism that evaluates client reliability using a cosine similarity metric before global model integration. Empirical evaluations across multi-vector benchmark datasets (UNSW-NB15, CICIDS2017, and Edge-IIoTset) demonstrate the framework's superior detection accuracy, rapid convergence, and high Byzantine fault tolerance under adversarial attack scenarios.

---


### 263. [A Generalizable and Explainable Framework for Synthetic Video Detection Using First-Digit Gradient Statistics](https://arxiv.org/abs/2609.39585)

**<font color=#1a73e8>作者：</font>** Sidharth Shanu, Gautam Kumar, Tej Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI video generators have not only become harder to detect but are used to generate a diverse set of scenarios from landscapes to street views to animal videos. This creates a problem where CNN-based detectors are effective but offer no insight into their inner workings, while forensics-based detectors are often pretrained for a set scenario or become too complex to derive meaningful insights. We present a novel approach to AI video detection using Sobel gradient values analysed with the first-digit law. Using linear discriminant analysis, we visualise the discriminatory signal, while a multi-layer perceptron is used for classification. The detection method has no generator- or scenespecific features, and the model has no knowledge of container formats, codec, bitrate, or compression artefacts. The model is trained and tested on GenBuster-200K, GenBusterBench, GenVA, FaceForensics++ C23, and CelebDF. We also show how zero-shot detection fails even though the feature set carries a discriminatory signal.

---


### 264. [SPOON: Towards Coherent Compositional 3D Scene Generation from Uncalibrated Multi-view Images](https://arxiv.org/abs/2609.39590)

**<font color=#1a73e8>作者：</font>** Guibiao Liao, Mochu Xiang, Heng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional 3D scene generation aims to recover complete 3D object shapes and their spatial arrangement from visual observations. Recent image-conditioned 3D generators provide strong priors for producing high-quality object geometry, making the generation of complex scenes increasingly practical. A central challenge is therefore to spatially organize these generated assets into a globally coherent scene while remaining consistent with multi-view observations. Existing approaches either entangle scene layout with object generation or separately estimate spatial placement from view-specific observations, where pose hypotheses may remain ambiguous and inconsistent across views, often resulting in an incoherent object-camera soup. We introduce SPOON, a framework that reformulates multi-view compositional 3D generation as scene-level, geometry-grounded pose reasoning. Rather than treating view-specific object pose hypotheses independently, SPOON coordinates them using reconstruction-derived multi-view geometry through a Guide-Route-Reconcile paradigm. This progressively organizes object poses and camera configurations into a coherent scene-level spatial arrangement. Extensive experiments on ARSG-110K and MIDI-3D-Front demonstrate consistent improvements in object placement and scene composition across varying numbers of input views. On ARSG-110K, SPOON reduces scene-level and object-level Chamfer distances by 12.7% and 17.7%, respectively, compared with a strong baseline.

---


### 265. [Structural Limits of the Information-Theoretic Uncertainty Decomposition](https://arxiv.org/abs/2609.39591)

**<font color=#1a73e8>作者：</font>** Jakob Lønborg Christensen, Christian F. Baumgartner, Morten Rieger Hannemose 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation in machine learning typically decomposes uncertainty into aleatoric uncertainty (AU) and epistemic uncertainty (EU) using the standard information-theoretic framework. However, in practice, two critical issues arise: entanglement (AU and EU are highly correlated) and epistemic collapse (EU magnitude shrinks with increasing model capacity). We analyze this framework on a functional level and discover that significant portions of the assumed AU, EU range are infeasible in finite settings, and cannot be attained with any class probabilities. We characterize how this infeasible region scales with the number of classes and Monte Carlo samples $N$ (e.g., from ensembles with $N$ members), revealing it is bounded by $\text{AU} \leq \log(2)/N$. Crucially, the infeasible region's boundary helps explain epistemic collapse: when model confidence is high, $\text{AU} > \text{EU}$ is guaranteed by this fundamental structural limitation. Our findings show that increasing ensemble size mitigates epistemic collapse by reducing the infeasible area. Lastly, we caution against interpreting AU and EU as independent quantities in low AU regimes, since we show they are coupled when $\text{AU} \leq \log(2)/N$.

---


### 266. [Convergence of Practical Muon with Finite Newton-Schulz Iterations and Nesterov Momentum](https://arxiv.org/abs/2609.39595)

**<font color=#1a73e8>作者：</font>** Hanyng Peng, Hui Wang, Yue Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practical Muon maintains momentum and performs a small, fixed number of Newton--Schulz iterations separately for each parameter matrix, often with a Nesterov correction. We analyze these layer-wise finite-step updates jointly on a coupled nonconvex objective, rather than replacing them by exact polar factors or one global orthogonalization. Under gradient-dependent $(\mathcal L_0,\mathcal L_1,q)$-smoothness and conditionally unbiased stochastic gradients with bounded layer-wise variance, we establish an $\mathcal O(T^{-1/4})$ bound on the expected average Frobenius gradient norm. The analysis retains the Nesterov recursion and requires neither bounded stochastic gradients, symmetric noise, nor a uniform positive lower bound on the nonzero output singular values. Its constants contain no explicit matrix-dimension or rank factors when the number of blocks and problem constants are fixed. The proof follows a descent inequality and a decomposition of the momentum tracking error into initialization, noise, and drift. For the original five-step quintic, we verify the required scalar-map bounds analytically; the result also allows step-dependent coefficients satisfying the same bounds. A complementary nuclear-norm result quantifies rank dependence under a stronger spectral condition. The vanishing rate uses coupled learning-rate and momentum schedules, including the standard single-coefficient Nesterov rule.

---


### 267. [Why Do Conventional World Models Fail to Learn Cellular Automata?](https://arxiv.org/abs/2609.39604)

**<font color=#1a73e8>作者：</font>** Shaoyang Guo, Ziming Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although conventional world models - auto-regressive or diffusion models based on transformers or convolutional networks - may learn surface statistics of world dynamics, can they learn the exact world dynamics from its observed history? Leveraging cellular automata as a simple testbed, we find the answer to be no in many cases. Conventional architectures predict most pixels correctly yet rarely complete a rollout: a CNN predicts 96.3% of cells but completes 18.9% of rollouts; a joint diffusion model completes none. We trace the gap to three failure modes of these world models - namely, they fail to exactly capture spatial locality, temporal locality or temporal stability. Simple changes repair each: (1) for spatial locality, two-dimensional rotary positions lift a transformer from 39.1% to 100% on the Game of Life; (2) for temporal locality, handing each token its cell's previous-frame neighbourhood lifts the same transformer from 25.8% to 99.9% on unseen rules; (3) for temporal stability, causal freezing lifts the same diffusion weights from 42.2% to 99.9%. None of the three changes touches the architectural backbone; each only modifies the information flow within it. We also compare joint and ordered sampling on billiards and, in an exploratory study, on a simulated Burgers equation.

---


### 268. [FOMO: Forget the Concept, Don't Miss Out on the Scene in Selective Video Unlearning](https://arxiv.org/abs/2609.39605)

**<font color=#1a73e8>作者：</font>** Łukasz Rudnik, Agnieszka Polowczyk, Alicja Polowczyk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative video models has enabled the synthesis of increasingly realistic and temporally coherent videos, while also raising concerns about the generation of harmful content. The reliance on large-scale web datasets during training inevitably exposes these models to undesirable material, making concept unlearning an essential mitigation. Existing methods mainly target static visual concepts, such as objects, identities, or unsafe appearance, largely overlooking motion unlearning. Furthermore, these approaches often pay little attention to preserving the surrounding scene. As a result, successful concept removal may unintentionally alter the background, composition, or overall video dynamics. We argue that effective unlearning should ideally change only what is targeted, while minimizing unnecessary changes to the remaining scene. In this work, we introduce FOMO, to the best of our knowledge the first training-based selective video unlearning method that directly treats preservation of the original scene as a priority. We formulate unlearning around two complementary objectives: what to change and what to preserve. Our method localizes concept-related representations and modifies them, while the preservation mechanism maintains non-target scene information without requiring auxiliary data. Beyond simply erasing unwanted concepts, FOMO explicitly redirects the generation toward a specified safe alternative. We further extend this formulation to motion unlearning, where the concept is defined by temporal behavior rather than a fixed spatial region. Our solution achieves effective unlearning across unsafe content, object, and motion concepts, while achieving the best trade-off between concept removal and scene preservation.
Code: this https URL
Project Page this https URL

---


### 269. [Hybrid Methods for Robust Tabular Data Imputation](https://arxiv.org/abs/2609.39613)

**<font color=#1a73e8>作者：</font>** Jinwei Li, Michelle Bruch, Daniel Tenbrinck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing data are a fundamental challenge in statistical analysis and machine learning, as the choice of imputation method substantially impacts downstream inference. In this work, we propose two hybrid imputation methods called NuclearForest and SoftForest, which combine nuclear-norm-based low-rank initialization using Singular Value Thresholding (SVT) and SoftImpute, respectively, with a non-iterative Random Forest refinement. For the SVT-based component, we further introduce an adaptive step-size rule, prove adaptive step-size bounds, and establish convergence for the corresponding zero-initialized iteration. The low-rank initialization provides a structured warm start that captures the global covariance patterns in the data, while the subsequent Random Forest step recovers residual nonlinear signals encoding local dependencies. We conduct an extensive benchmark on diverse datasets from different application domains, comparing the proposed methods with seven established imputation methods under the Missing Completely at Random (MCAR), Missing at Random (MAR), and Missing Not at Random (MNAR) mechanisms across varying missingness rates. Our results demonstrate that NuclearForest and SoftForest match or exceed the imputation fidelity of state-of-the-art iterative methods such as MissForest, while significantly reducing computational cost. In particular, they achieve speedups of approximately 5.81 times and 9.52 times over MissForest by replacing iterative cycles with a single refinement step. Our approach effectively exploits the low-rank structure of real-world tabular data and accommodates mixed-type variables, providing an efficient and robust solution for data imputation in bioinformatics, economics, and beyond.

---


### 270. [Semantic Watermarking for Malicious Image Manipulation Detection](https://arxiv.org/abs/2609.39623)

**<font color=#1a73e8>作者：</font>** Yoonseo Kim, Seungwoo Baek, Junyoung Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of high-fidelity generative editing models has made it possible to inject violent or sexual content into otherwise ordinary images while preserving visual plausibility, with concrete consequences for public discourse and vulnerable populations. We propose a robust semantic watermarking framework that reframes the watermark as a recoverable semantic reference rather than an opaque identifier. Our framework combines a $\beta$-VAE-based binary watermark (CLIP-VAE) with explicit channel-aware training---random bit-flip noise is injected during training so that the decoder learns graceful degradation under the noisy watermarking channel. As a downstream application, a lightweight module SDA-Net uses the recovered semantic embedding to expose not only whether but in which semantic direction an image has been altered. In a 5-way comparison against representative binary hashing baselines (SimHash, ITQ, HashNet, and their robust-MLP variants), CLIP-VAE achieves the highest reconstruction cosine similarity to the original CLIP embedding under realistic InstructPix2Pix bit-error rates, and uniquely supports direction-of-drift detection---a forensic complement to existing content-moderation pipelines.

---


### 271. [ExpandDiff: Dynamic Range Expanding Diffusion for Single-Image HDR Reconstruction](https://arxiv.org/abs/2609.39624)

**<font color=#1a73e8>作者：</font>** Mehmet Emre andıran, Zhuoqian Yang, Liying Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image HDR reconstruction requires inferring missing detail while preserving the visible content of an LDR image. Differences in sensor dynamic range and exposure cause LDR images to lose varying amounts of information in shadows and highlights. We present ExpandDiff, a conditional diffusion pipeline that jointly reconstructs clipped shadows and highlights. To account for this variation, we introduce Dynamic Clipping Synthesis (DCS), which randomly samples shadow and highlight clipping percentiles when constructing training inputs from HDR targets. A pixel-space diffusion model guided by spatially-adaptive normalization then predicts perceptually encoded HDR through a bounded output head, reconstructing both clipping directions in one sampling trajectory. On the SI-HDR benchmark, ExpandDiff variants improve HDR reconstruction accuracy by 3.43 dB in PU21-PSNR over the strongest evaluated competing method, and by 7.34 dB under two-sided clipping. The code and supplementary material are available at this https URL.

---


### 272. [D-Scope: Decomposing and Steering Diffusion Transformers with Sparse Autoencoders](https://arxiv.org/abs/2609.39625)

**<font color=#1a73e8>作者：</font>** Xinyue Xu, Jiahao Zhang, Lijie Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) reveal visual structure in diffusion transformers (DiTs), but interpreting a feature does not establish whether it can be used to control generation. We introduce D-Scope (Diffusion Scope), a framework that connects feature interpretation to generation control through shared visual evidence. D-Scope aggregates SigLIP~2 embeddings of highly activating image patches into visual centroids. Matching target text descriptions against these visual centroids in the shared image-text embedding space then enables retrieval of individual features without per-feature text annotations. The underlying patches provide evidence for inspecting each selection, while spatially masked interventions test the corresponding decoder direction at varying strengths under fixed generation conditions. We characterize 150 SAEs across two model families and five layers, and introduce a benchmark of 100 target concepts with ten contexts each spanning under-specified and explicit-conflict conditions. Our empirical results show that high reconstruction fidelity can coexist with low dictionary utilization and limited visual-evidence coverage. Under per-case best-of-sweep strength selection, contrastive retrieval yields larger mean regional SigLIP~2 gains than direct retrieval across the tested steering configurations, without consistently improving outside-region preservation. D-Scope provides an inspectable framework for evaluating sparse DiT features through their visual evidence and the effects of their decoder directions on generation. The demo is available at this https URL.

---


### 273. [Parameterization method of reservoir properties for ensemble-based data assimilation using intermediate latent space of StyleGAN](https://arxiv.org/abs/2609.39626)

**<font color=#1a73e8>作者：</font>** Marcio A. Sampaio, Paulo H. Ranazzi, Martin J. Blunt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensemble smoothers are the most successful and efficient techniques currently available for history matching. However, because these methods rely on Gaussian assumptions, their performance is severely degraded when the prior geology is described in terms of complex facies distributions (non-Gaussian). In this way, for these methods, we need to apply efficient parameterization techniques. Currently, the most efficient methods for performing parameterization are deep learning models. However, given the variety of existing deep learning models, studies have not identified which is most suitable for use with ensemble-based methods, although some important models had already been evaluated. Based on a recent literature review, the most promising models selected were VAE-GAN, Latent Diffusion, and StyleGAN models. As a novel aspect of this work, data assimilation with the second generation of StyleGAN (StyleGAN2) model was performed using the latent z-space and intermediate w-space, separately. They were applied in two 2D case studies: one categorical (three facies) and the other continuous. The results demonstrated that all three models are highly efficient, with the StyleGAN2 model standing out for generating samples with geological realism and achieving excellent data matching in the cases studied. Our findings show that performing data assimilation with StyleGAN2 using the intermediate space (w-space) yielded better results than the traditional application in the latent space (z-space). This is due to the fact that ESMDA uses linear updates and the w-space is much more linear and disentangled than the highly entangled z-space, thereby ensuring that the updated vectors remain close to realistic geological patterns. These results were validated using main geostatistical and history matching metrics.

---


### 274. [Introduction to Computer Vision](https://arxiv.org/abs/2609.39627)

**<font color=#1a73e8>作者：</font>** Stan Birchfield  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This book presents a code-first introduction to computer vision, spanning classical 2D image processing, classical 3D vision, and deep learning. Organized as 44 short chapters across three parts, the book builds each topic from first principles: image arithmetic and morphology; convolution, pyramids, and frequency-domain filtering; feature detection, optical flow, and stereo; projective geometry, camera calibration, and structure from motion; and the full arc of modern deep learning, from a single neuron through convolutional networks, backpropagation, classic architectures, transfer learning, object detection, and semantic and instance segmentation, concluding with engineering considerations like mixed-precision and parallel training. Every technique is implemented directly in Python and NumPy or PyTorch and checked numerically against the corresponding OpenCV or PyTorch library function, so readers see not just the mathematics but its concrete behavior on real and synthetic data. The material was distilled with AI assistance from freely available online course notes, condensing extensive working code into concise mathematical exposition while preserving verified, reproducible results throughout. It is intended as a self-contained reference for students and practitioners who want to understand computer vision algorithms and their Python implementations.

---


### 275. [MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation](https://arxiv.org/abs/2609.39628)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Mohammad Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes MIND, a marginal-invariant neural dependency diffusion model for mixed-type tabular data. MIND does not directly learn the joint distribution in the original heterogeneous feature space. Instead, it first maps different variable types into a unified latent dependency space via column-wise marginal transport. A conditional diffusion model then learns cross-column relationships. Copula-tangent denoising separates known marginal components from learnable dependency residuals. Rank projection during the sampling phase further mitigates marginal shift in reverse diffusion. Experiments across nine diverse tabular benchmarks show that MIND consistently improves marginal fidelity and dependency preservation over existing unified approaches. By explicitly isolating marginal modelling from dependency learning, MIND achieves a strong and stable balance among marginal fidelity, joint dependency preservation, and downstream prediction utility. This work supports separating marginal and dependency modelling as a principled and highly effective paradigm for complex mixed-type tabular generation.

---


### 276. [Certification-Based Differentially Private Learning](https://arxiv.org/abs/2609.39629)

**<font color=#1a73e8>作者：</font>** Mihnea Ghitu, Matthew Wicker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) in machine learning is typically achieved by adding noise to model parameters (private learning) or to model outputs (private prediction). Recent work uses formal methods, namely abstract interpretation, to provide tighter privacy guarantees, but only for private prediction in classification settings. In this work, we investigate the use of formal methods as a general tool for tighter privacy analysis. First, we generalize the abstract gradient training (AGT) framework to private prediction in continuous, unbounded regression. Second, by reducing learning in parameterized models to a regression problem over the parameter space, we introduce Abstract Gradient Sampling (AGS), an algorithm that enables reachability-based analysis to provide guarantees for private learning. In both private prediction and private learning, we provide tightened privacy accounting for the AGT framework and a theoretical analysis demonstrating when our smooth sensitivity upper-bounds yield favourable privacy-utility trade-off. In practice, we validate that our regression bounds are tighter than global-sensitivity baselines on regression benchmarks, and, notably, yield the first finite privacy guarantees in settings where global prediction sensitivity is a priori unbounded. We also find that under matched conditions, our private learning algorithm can outperform standard private learners.

---


### 277. [PEG-Tab: Sampling-Time Record Repair and Release Control for Tabular Synthesis](https://arxiv.org/abs/2609.39630)

**<font color=#1a73e8>作者：</font>** Pengfei Li, QinYi Liu, Mohammad Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained tabular generators can reproduce training records even when aggregate utility remains high. When retraining is unavailable or too costly, sampling and release are the remaining intervention points. We present PEG-Tab (Post-Training Energy Guidance for Tabular Synthesis), a post-training repair and release-control framework for frozen tabular generators. For each generated row, a generator-native operator creates two alternatives. A shared calibrated score compares the three candidates, favours lower-risk records, and applies a final release check. We instantiate this interface for GReaT, CTGAN, TVAE, and TabDDPM without updating their parameters. Across five datasets and four generator families, PEG-Tab reduces mean Near Copy from $0.078$ to $0.027$ and lowers aggregate Exact Copy to zero. Relative to a $3\times$ post hoc filter, it retains higher utility in 12 of 16 transfer settings and Pareto-dominates the filter in eight. Gains are concentrated in copy and proximity-related risks.

---


### 278. [SAGE: Salient Factor Discovery and Generation with Visual Foundation Representations](https://arxiv.org/abs/2609.39635)

**<font color=#1a73e8>作者：</font>** Shuang Liang, Lejun Liao, Shiyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a target dataset, such as faces with eyeglasses, and a background dataset, such as faces without, contrastive analysis separates \textit{salient} factors specific to the target from \textit{common} content shared by both. We aim for salient representations that capture target-specific detail in each image, such as the shape, color, and position of the glasses, so that they reveal subtypes without subtype labels and guide the generation of new examples of a discovered subtype, even one with no name or text description. We introduce SAGE, which learns both factors directly in the high-dimensional spatial latent of a frozen representation autoencoder and conditions a diffusion transformer on the learned salient representation of a reference image. On Digits-ImageNet and FFHQ eyeglasses, SAGE combines high-fidelity \textit{reconstruction} (rFID below $2$) with unsupervised \textit{subtype discovery}, recovering the digits better than baselines (probe accuracy $0.950$ vs.\ at most $0.281$) and revealing eyewear types, finer sunglasses styles, and mislabeled images; salient-conditioned \textit{generation} raises Digits-ImageNet subtype accuracy over the unfactorized latent ($90.5\%$ vs.\ $27.7\%$) and diversity on both datasets. On retinal OCT, SAGE's salient space separates three diseases using only normal/disease labels.

---


### 279. [Zero-Compute Cross-Lingual Transferability Estimation Using Typological Feature Proxies](https://arxiv.org/abs/2609.39640)

**<font color=#1a73e8>作者：</font>** Dalton Raphael Harmsen, Swier Garst, Thomas van Osch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer describes how knowledge in a source language benefits a target language. Measuring it quantitatively requires broad multilingual pre-training, as prior work has done with cross-lingual transfer matrices. We ask whether transfer is predictable from freely available typological features, and whether the prominence of high-resource source languages reflects typology or data quality and quantity. We show that typological databases contain cheap and dense signals about cross-lingual transfer. Our typology-only random forest on a 24-language prior-work transfer matrix scores leave-one-language-out $\rho{=}0.705$ and $R^2{=}0.49$, beating a non-typological control at $\rho{=}0.62$, which verifies the ability of typology-only predictions to reconstruct costly measured cross-lingual transfer. The signal survives leave-one-script-out and leave-one-family-out protocols, so script and family confounding do not explain the effect. By decomposing the transfer into a typology term and a resource-and-script bias term, we find the best-source ranking sensitive to this bias. In contrast, typology is not affected by this bias, which makes it a zero-compute screening tool that replaces hundreds of training runs with a model fit. Our code is available \href{this https URL}{here}.

---


### 280. [RiboUnmix: Learning Shared Translational Dynamics from Biased and Noisy Ribo-seq Measurements](https://arxiv.org/abs/2609.39644)

**<font color=#1a73e8>作者：</font>** Gabriele Martino, Denis Skibinski, Ivo L. Hofacker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ribosome profiling (Ribo-seq) measures ribosome distributions along mRNAs, but observed occupancy profiles also contain experiment-specific distortions and stochastic variability. Consequently, models that accurately predict measured profiles may reproduce technical effects rather than recover the underlying biology. We ask whether jointly modeling datasets collected under different experimental conditions can reveal shared, sequence-dependent patterns of ribosome occupancy. We introduce RiboUnmix, a probabilistic multi-dataset framework in which each expected measured profile is represented as a shared sequence-dependent signal modulated by a dataset-specific multiplicative factor. A negative-binomial observation model captures variability across replicates. We evaluate RiboUnmix on a controlled synthetic benchmark combining programmed translation kinetics, ribosome traffic, stochastic count sampling, and sequence-dependent experimental distortions. Because the underlying kinetics and distortions are known, recovery of the shared profile and dataset-specific effects can be assessed separately. Both inferred components correlate strongly with their targets, demonstrating that RiboUnmix can disentangle shared kinetic patterns from experimental effects. Across four organism-specific real-data benchmarks, RiboUnmix outperforms sequence-to-profile baselines in predicting measured profiles. Models trained independently on subsets of 114 HEK-derived datasets recover concordant shared profiles for held-out transcripts, and experiments varying the number and composition of training datasets show that the learned representation remains stable. RiboUnmix thus converts variation across experiments into evidence for reproducible sequence-dependent patterns of ribosome occupancy, supporting biological hypothesis generation from diverse Ribo-seq datasets.

---


### 281. [Beyond Uniform Compression: Budgeted Transmission Allocation for Extreme Federated Learning](https://arxiv.org/abs/2609.39646)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Mohammad Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning faces severe communication bottlenecks when clients upload high-dimensional model updates. Existing methods often compress these updates uniformly across all layers. This uniform approach ignores the heterogeneous value of different parameter blocks and wastes limited bandwidth on insensitive layers. To address this issue, we propose Layer-wise Budgeted Adaptive Transmission (LBAT). LBAT reframes federated communication under extreme uplink budgets as a resource allocation problem. Our framework dynamically estimates the transmission value of different layers utilising local training signals. It then employs an exact byte dynamic programming allocator to determine optimal rank and bit configurations under strict budgets. We validate LBAT on highly heterogeneous federated tabular prediction and data generation tasks. Extensive experiments demonstrate that LBAT consistently outperforms uniform rank, uniform quantisation, and fixed compression baselines across various extreme budget regimes. Furthermore, it achieves significantly better communication and utility tradeoffs while preserving essential distributional fidelity.

---


### 282. [From Modes to Memories: Characterizing the Scale-Space Dynamics of Diffusion Models](https://arxiv.org/abs/2609.39648)

**<font color=#1a73e8>作者：</font>** Cristina López Amado, Marco Fumero, Francesco Locatello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are typically viewed as stochastic processes that transform noise into data. We take a complementary perspective: a diffusion model defines a family of deterministic dynamical systems indexed by noise scale. At each fixed scale $\sigma$, we treat the denoiser as a self-map and study its dynamics. For an exact denoiser, fixed points correspond to critical points of the smoothed data density, while attractors correspond to its modes; as $\sigma$ increases, sample-level modes merge into progressively coarser ones. This suggests a geometric view of memorization: examples that receive excess probability mass due to duplication or overfitting, as well as outliers, should remain distinguishable under stronger smoothing than ordinary examples. We quantify this persistence by the critical scale $\sigma_c$, the largest noise scale at which an example is retained by the fixed-scale dynamics. In conditional models, the same construction extends naturally to image--caption pairs. Experiments in controlled settings and on large-scale models show that $\sigma_c$ tracks memorization arising from duplication, overfitting, and outliers, and identifies both memorized and partially memorized examples in Stable Diffusion. Moreover, $\sigma_c$ yields interpretable measures of the image spatial distribution and caption dependence of memorization.

---


### 283. [FANVIDv2: Evaluating Video Super-Resolution by Face and Licence-Plate Recognition Under Compound Degradation](https://arxiv.org/abs/2609.39649)

**<font color=#1a73e8>作者：</font>** Kavitha Viswanathan, Vrinda Goel, Shlesh Gholap 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video super-resolution (VSR) is normally judged by PSNR and SSIM on clips that were downsampled bicubically, although in surveillance its purpose is to make faces and licence plates \emph{recognisable}. We present FANVIDv2, a benchmark that scores VSR by what a recognition pipeline can do with its output. FANVIDv2 provides $320\times180$ low-resolution (LR) clips with high-resolution (HR) references for 48 public figures (with one HR gallery image each) and 375 licence-plate clips covering 360 distinct plate strings. LR clips are generated with a randomised compound degradation (blur, resize jitter, sensor noise, JPEG compression, final downsampling) rather than bicubic downsampling alone. Two metrics score recognition \emph{inside} detections: FaceRecBox rewards a face only if it is localised and correctly identified, and TextRecBox scores plate transcriptions by normalised edit distance weighted by localisation quality. With a 2.3\,M-parameter VSR baseline (RCDM), FaceRecBox rises from 0.6864 to 0.7222, identity accuracy on matched faces from 84.35\% to 86.93\%, and TextRecBox from 0.3088 to 0.3667; a residual-map gated variant (RCDM-RMGF) reaches 0.3801 on plates. We describe the degradation model, the baseline architectures and the scorers in detail, and release annotations, metadata, download and degradation scripts and evaluation code.

---


### 284. [Diffusable Latents from Structure-Agnostic Distillation](https://arxiv.org/abs/2609.39657)

**<font color=#1a73e8>作者：</font>** Adrien Ramanana Rahary, Nicolas Dufour, Patrick Pérez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling pretrained foundation models into an autoencoder bottleneck improves latent diffusability, enabling diffusion models to converge faster and reach higher sample quality. Standard distillation aligns the latent at each position to a co-located teacher feature, tying the latent layout to the teacher's. We show this constraint is unnecessary: aligning a single pooled image-level descriptor to the teacher's performs as well as or slightly better than dense position-wise distillation. We compare first-order and relational pooled objectives across latent shapes and teacher modalities. First-order matching extends naturally to 1D token-sequence latents and across modalities, where distilling a text encoder into an image autoencoder still improves diffusability; a relational objective based only on each image's nearest neighbours improves it as well. Code and blog post are available at this https URL and this https URL.

---


### 285. [Graph Residual Conjugate Diffusion: SNR-Equalized Heat Flow for Graph Signals](https://arxiv.org/abs/2609.39658)

**<font color=#1a73e8>作者：</font>** Jinwei Li, Daniel Tenbrinck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate data by reversing a forward corruption process that typically approaches a simple Gaussian prior. Recent work has extended this framework to signals supported on fixed graphs, e.g., road-network traffic and sensor-network measurements. Many graph signals have nonuniform spectral energy, whereas isotropic corruption adds the same conditional noise variance to every graph-frequency mode. Driving all modes to near-zero terminal signal-to-noise ratio (SNR) requires strong corruption, which increases the noise range that must be covered under a fixed sampling budget. We introduce Graph Residual Conjugate Diffusion (GRCD), which replaces the shared clock of graph heat diffusion with a mode-dependent clock that gives every graph-Fourier mode the same conditional SNR. GRCD fits a zero-mean graph-spectral Gaussian reference on the training split and stops at a finite terminal SNR at which the propagated reference still carries the fitted spectral variances. The Gaussian component has an exact modewise propagator in the probability-flow ODE, so sampling advances it analytically and integrates only the learned residual score numerically. We evaluate GRCD on five settings (METR-LA traffic, Molene weather, and three stochastic block models) against seven comparators under a matched protocol: Graph-Aware Diffusion (GAD), EDM (graph backbone), two adaptations of Whitened Score Diffusion (WSD), and three preconditioning controls. At four function evaluations (NFEs), GRCD lowers averaged maximum mean discrepancy (aMMD) by 22 to 36 times over the best comparator on all five settings, reaching 0.054 on METR-LA, where it clears an aMMD 0.1 target with 87% less sampling wall-clock time than the cheapest comparator that reaches it. Fitting the terminal reference reduces aMMD by 2.7 to 7.3 times at finite terminal SNR, while the factors shrink to 1.00 to 1.01 near zero.

---


### 286. [MC-PanDA++: Simpler, Stronger, and More Robust Domain-Adaptive Panoptic Segmentation](https://arxiv.org/abs/2609.39681)

**<font color=#1a73e8>作者：</font>** Ivan Martinović, Josip Šarić, Yuki M. Asano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised domain adaptation (UDA) reduces the annotation burden in panoptic segmentation by leveraging a cost-effectively labeled source domain (e.g., synthetic) and an unlabeled target domain to bridge the distribution gap. Existing panoptic UDA methods rely on teacher-student consistency learning built upon suboptimal per-pixel segmentation architectures. In contrast, state-of-the-art mask transformers are rarely adopted due to their pronounced vulnerability to confirmation bias in consistency learning, where erroneous teacher predictions are reinforced during training. Our earlier approach, MC-PanDA, mitigates this issue through fine-grained confidence estimation, which suppresses gradients from unreliable masks while sampling informative yet reliable locations for loss computation. However, this method entails a complex multi-stage training and requires careful hyperparameter tuning. This work presents MC-PanDA++, which addresses these limitations by introducing: (i) self-supervised vision encoders that provide a stronger and more robust initialization, further reducing the reliance on human annotations, (ii) per-class, self-adapting mask-wide loss scaling that stabilizes training and enables the usage of a single set of hyperparameters across domains, and (iii) a single-stage training pipeline that decreases overall conceptual complexity. Together, these improvements result in a conceptually simpler, better-performing, and more robust method for domain-adaptive panoptics. Source code: this https URL

---


### 287. [Unapologetically Distributed: A Call for Decentralized Document Analysis](https://arxiv.org/abs/2609.39684)

**<font color=#1a73e8>作者：</font>** Adrià Molina, Oriol Ramos Terrades, Josep Lladós  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy has become an increasingly important concern in the Document Analysis community, to the extent that in many environments such as archives, governmental institutions, and local businesses, the adoption of automation is restricted by legal and policy constraints. While federated learning has often been regarded as a ``necessary evil'', implying an unavoidable performance trade-off in exchange for decentralization and privacy, many prior works overlook its potential to improve robustness to out-of-distribution data. In this paper, we present Unapologetically Distributed, the first comprehensive study evaluating distributed learning in Document Analysis along three key axes simultaneously: the tasks addressed, the architectures employed, and the fine-tuning strategies applied. Specifically, we demonstrate how various distributed training approaches enhance generalization capabilities across diverse tasks such as Table Recognition, handwriting recognition, and Word Spotting, particularly during transfer learning stages. Our results provide strong evidence that decentralization is not merely a constraint, but a valuable opportunity to improve model robustness and adaptability in real-world Document Analysis scenarios.

---


### 288. [When Masking Helps or Hurts Robustness in Compressed CLIP: A Pre-Deployment Diagnostic](https://arxiv.org/abs/2609.39704)

**<font color=#1a73e8>作者：</font>** Muhammad Zawish, Steven Davy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper demonstrate that whether masking-based token pruning helps or hurts worst-group robustness can be predicted before deployment, without labels or fine-tuning. A systematic study of semantic masking across 8 spurious-correlation benchmarks shows its effect on worst-group accuracy is highly unstable: it improves accuracy by up to 82.5\% relative on some datasets and degrades it by up to 100\% on others. We trace this instability to spurious inversion: background patches receive higher CLIP text-similarity than the true object when the spurious attribute is background-separable, inverting the assumption every text- and attention-guided pruning method relies on. We introduce the Spurious Inversion Metric (SIM), a label-free, pre-deployment diagnostic whose sign predicts this effect with statistical significance (binomial $p=0.035$) across all 8 datasets, and remains dependable across 6 CLIP architectures with a clean foreground/background split. Naive masking is itself a major source of risk: it causes the largest average-accuracy loss of any method we evaluate, and its own per-image segmentation step is a significant runtime bottleneck. To address this, we design a batched, synchronization-free GPU segmentation routine that cuts this overhead from 3.5$\times$ to 1.75$\times$ baseline. Gating deployment by SIM's sign recovers masking's benefits while avoiding its worst failures, matching or exceeding a strong pruning baseline on 7 of 8 datasets.

---


### 289. [BTC3D: Blended Tile Conditioning for Detail-Enhancing Image-to-3D Generation](https://arxiv.org/abs/2609.39709)

**<font color=#1a73e8>作者：</font>** Junyu Li, Qiuyu Chen, Pengcheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based pipelines have achieved promising progress in image-to-3D synthesis. However, generating high-fidelity details remains challenging, especially when the input image contains rich details. Existing approaches often rely on globally encoded conditioning features, which compress spatial information and limit the model to reproduce fine-grained details. This common design often leads to a phenomenon we term detail attenuation. Moreover, improving image-to-3D synthesis quality typically requires retraining or fine-tuning large diffusion models, which can be computationally expensive and impractical for complex 3D pipelines. In this work, we present Blended Tile Conditioning for image-to-3D generation (BTC3D), a training-free inference time framework that enhances fine-grained detail preservation in image-to-3D diffusion pipelines. To alleviate detail attenuation, we first examine the image feature additivity in image-to-3D models. Based on this property, we introduce a blended tile embedding that extracts local conditioning signals from split image regional patches, allowing the diffusion model to better preserve fine-grained visual details. To integrate the global and local conditioning guidance stably, we propose a dynamic conditioning schedule that gradually increases the influence of tile-level conditioning during later low-noise stages of diffusion. Our proposed method BTC3D operates entirely at inference time and can be seamlessly integrated into existing image-to-3D diffusion pipelines. Experimental results demonstrate that the proposed approach significantly improves texture quality and visual fidelity of the base model while maintaining global structural consistency in a training-free manner.

---


### 290. [Let the Carrier Carry the Attack: Preserving the Subject in Adversarial Image Generation](https://arxiv.org/abs/2609.39723)

**<font color=#1a73e8>作者：</font>** Linfeng Jiang, Steven McDonagh, Yuhang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strong unrestricted adversarial attacks can distort the primary object of an image, hereafter referred to as the subject. To preserve subject integrity without compromising attack magnitude, we introduce the carrier: a secondary visual element that provides an auxiliary region to facilitate the attack under global classifier guidance. We demonstrate three key findings: 1. A carrier mitigates subject distortion by absorbing a larger share of globally normalized attack updates. 2. A carrier improves cross-model transferability, governed by the strength of target-related features that balance semantic separation and transfer performance. 3. Successful targeted attacks retain the personalized subject as the primary content perceived by humans while successfully misleading the classifier. Our results demonstrate that a visually secondary carrier offers an auxiliary spatial pathway for adversarial changes, enabling strong and transferable attacks while improving subject preservation.

---


### 291. [A library for differentiable signal processing and machine learning on the sphere](https://arxiv.org/abs/2609.39737)

**<font color=#1a73e8>作者：</font>** Thorsten Kurth, Max Rietmann, Mauro Bisson 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The two-dimensional sphere embedded in three-dimensional Euclidean space S2, plays a central role in a variety of scientific and engineering domains, including geophysics, planetary science, geodesy, atmospheric physics, quantum chemistry, cosmology, and virtual reality, among many others. As machine learning increasingly permeates these fields, the demand grows for robust tools that process and model functions on the sphere, while respecting the inherent topological and symmetry properties of the domain. We present torch-harmonics, a comprehensive library that offers efficient, differentiable implementations of advanced signal processing and machine learning (ML) methods for spherical data. These include the spherical harmonic transform (SHT), the spherical analogue of the Fourier transform, vector spherical harmonics, discrete-continuous and spectral convolutions, as well as both global and neighborhood spherical attention mechanisms. Beyond traditional representations, torch-harmonics provides the building blocks for state-of-the-art spherical ML architectures such as spherical transformers in order to enable scalable, rotationally-aware learning and inference in modern scientific and engineering applications.

---


### 292. [CNCGEN: A Dataset and Framework for Machining Process Planning and Toolpath Generation from B-rep Models](https://arxiv.org/abs/2609.39738)

**<font color=#1a73e8>作者：</font>** Xiaolei Zhou, Boyi Lin, Yuchao Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning to generate machining process plans and toolpaths from B-rep CAD requires coupling discrete operation decisions with continuous tool motion as the workpiece evolves. Correctly predicting an operation sequence does not by itself ensure correct material removal, because each toolpath acts on the stock left by preceding cuts. We formulate this problem around persistent manufacturing objects: object identity determines the target of an operation, while the evolving stock state conditions the generation of its toolpath. Based on this formulation, we propose CNCGEN, a dataset and learning framework for three-axis machining. CNCGEN-Dataset contains approximately 50k geometrically verified synthetic machining flows and 800 held-out real CNC records. Each flow aligns B-rep geometry with object-referenced operations, parameterized toolpaths, intermediate stock states, and verification outcomes, enabling supervision of the correspondence between planning decisions and their geometric effects. CNCGEN generates operations and toolpaths for selected objects step by step, updating a compact machining state to guide subsequent predictions. During training, a learned surrogate verifier provides material-removal feedback that links local predictions to their geometric consequences. Experiments on synthetic and held-out real CNC records show that CNCGEN improves the resulting workpiece geometry and reduces residual material and overcut compared with adapted CNC generation baselines.

---


### 293. [Stable Transformers for Graph Generation](https://arxiv.org/abs/2609.39739)

**<font color=#1a73e8>作者：</font>** Luca Miglior, Alessio Gravina, Davide Bacciu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph generative models increasingly rely on Graph Transformers (GT) to capture complex dependencies among nodes and edges. While deeper architectures should provide greater expressive capacity and a broader receptive field, their effectiveness can decline with depth: repeated self-attention progressively contracts node representations, impeding information flow and gradient propagation. We analyse this phenomenon from a dynamical systems perspective, focusing on how the denoiser's spectral dynamics affect graph generation. We show that standard GT denoisers become increasingly dissipative as depth grows, leading to vanishing gradients and representation collapse. To isolate the effect of these dynamics, we construct a permutation-equivariant GT with inherently stable, non-dissipative transport. We also introduce a damping mechanism that continuously interpolates between non-dissipative and increasingly contractive regimes, enabling a direct assessment of how dissipation influences generation. Experiments on synthetic and molecular graph generation benchmarks show that the gap between these regimes widens with depth: non-dissipative dynamics preserve representation diversity and gradient flow, sustaining strong generative performance, whereas greater contraction progressively impairs it. These findings identify the denoiser's dynamical regime as a key design factor for deep graph generative models.

---


### 294. [LatentHarness: Learning Latent Actions for Memory and Reasoning via Counterfactual Policy Distillation](https://arxiv.org/abs/2609.39740)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Wang, Suyuchen Wang, Bang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning faces two complementary bottlenecks: retaining evidence across long inputs and sustaining computation across many reasoning steps. Existing approaches largely address them separately, with external memory extending access to distant evidence and latent reasoning compressing multi-step computation. We introduce LatentHarness, which unifies memory access and latent reasoning as sequential latent action selection. At each internal step, the model chooses THINK for further computation, RECALL from a fast-weight memory of input evidence and intermediate reasoning states, or EXIT to emit the next token. We train this policy with counterfactual policy distillation, which branches every action for one step and scores its effect on the emitted token. These gains teach the policy when memory is more useful than further reasoning, while gradients through counterfactual recall teach which intermediate states should be retained in memory for future use. Across six general and long-context reasoning benchmarks, LatentHarness at 1.4B improves on the strongest baselines by 2.8% and 10.0% relative, respectively, and runs 5.9x faster than the strongest long-context baseline.

---


### 295. [The Nixtlaverse: An Open-Source Ecosystem for Forecasting](https://arxiv.org/abs/2609.39741)

**<font color=#1a73e8>作者：</font>** Olivier Sprangers, Max Mergenthaler Canseco, Marco Peixeiro 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large forecasting applications often combine statistical, machine-learning, and neural models. These families solve the same problem but differ in fitted state, training procedures, and how they parallelize work. Forecasting software must therefore either hide these differences behind a single estimator interface, or keep the families in separate packages, forcing users to rewrite data preparation and evaluation for every package. We present the Nixtlaverse, an ecosystem of open-source Python libraries for time series forecasting, as a case study of a third design: all libraries share the same long-format panel data and keyed forecast outputs, while every model family keeps its own specialized implementation. We demonstrate this design through three use cases on the public M5 competition data. First, we evaluate statistical, machine-learning, and neural models, and an external engine from a separate ecosystem, in a single rolling-origin evaluation with per-series and hierarchy-weighted metrics. Second, we profile runtime and peak memory from 100 to 30,490 series and locate each family's bottleneck: statistical fitting scales approximately linearly in the number of series, feature construction dominates machine-learning memory, and neural training time is nearly independent of panel size under a fixed training budget. Third, we reconcile the forecasts of multiple engines, including the external one, over all 42,840 series of the M5 hierarchy, with sparse reconciliation where dense implementations exhausted memory. These use cases establish the costs, boundaries, and utility of shared data and output contracts. The Nixtlaverse has seen substantial public distribution, scholarly reuse, and adoption through other forecasting frameworks, and is released under permissive open-source licenses with public datasets, reproducible examples, and verifiable benchmark artifacts.

---


### 296. [FAST: Flow Any Scene Transformer](https://arxiv.org/abs/2609.39748)

**<font color=#1a73e8>作者：</font>** Yongjian Zhang, Longguang Wang, Zhuo Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling has become a primary driver of progress in language and vision foundation models, yet its role in precise correspondence matching remains underexplored. In this work, we present Flow Any Scene Transformer (FAST), a scalable correspondence model driven by two key insights. First, we reveal that the query-key projections inside single-view vision foundation models encode a coarse yet reusable prior for cross-view matching. Second, reusing these pretrained projections in cross-attention form yields a highly effective initialization for a ViT-based matcher built from a single-view encoder. Guided by these insights, we build FAST upon a vanilla single-view foundation model, utilizing a zero-parameter rewiring strategy to convert selected self-attention layers into cross-attention for cross-view interaction. This design allows ViT-based matchers to scale with advances in single-view foundation models, bypassing the need for a dedicated pair-centric pretraining stage. To fully unlock the scaling potential of this formulation, we assemble a 6-million-pair training corpus for general-purpose dense 2D displacement estimation across diverse co-visible image pairs. Extensive experiments demonstrate that FAST achieves state-of-the-art performance across a wide range of benchmarks, while scaling favorably with both backbone size and training data.

---


### 297. [Validity-Preserving Hierarchical RL for Joint Routing and Switch Placement in EDA](https://arxiv.org/abs/2609.39749)

**<font color=#1a73e8>作者：</font>** Dorian Gailhard, Ugo Lecerf, Enzo Tartaglione 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing and switch placement are fundamental combinatorial optimization problems in chip design, requiring the joint optimization of routing topology and physical placement under strict structural, geometric and logical constraints. Existing approaches typically rely on carefully engineered heuristics that incorporate strong problem-specific biases to navigate the enormous space of possible designs. In this work, we introduce a hierarchical reinforcement learning framework for joint routing and switch placement at the level of logical communication routes. Starting from a minimal routing graph, our method progressively constructs increasingly expressive solutions through three coupled operations: switch expansion, switch placement, and route refinement. These operations preserve routing validity by construction, restricting exploration to feasible configurations where every communicating initiator-target pair has one assigned loop-free route. We explore the induced solution space using Gumbel Monte Carlo Tree Search, showing that neural-guided search substantially improves solution quality over non-learning optimization methods. Furthermore, pretraining across floorplans provides a strong initialization for fine-tuning on unseen instances.

---


### 298. [Engagement-Led Segmentation of Gamified Participation Data in a Large-Scale Remote Internship: A Mixed-Methods Study](https://arxiv.org/abs/2609.39750)

**<font color=#1a73e8>作者：</font>** Sakshi Sharma, Pavani Ayinampudi, Aditya B.M.V. 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gamified points are widely used to represent learner participation, but cumulative point totals provide limited information about how participation changes over time. This limitation matters in continuously enrolling programmes, where learners have different opportunities to accumulate points. This study examines how gamified participation data can be interpreted as indicators of behavioural engagement in a large-scale, continuously enrolling remote internship. Using an anonymised operational dataset, 3,607 distinct started learners were first classified by participation status, separating dormant learners from those with observable participation. The 1,871 active learners were then grouped using K-means clustering on normalised longitudinal and opportunity-aware participation features. Four participation patterns emerged: Thriving Core, Tapering, Fast Starters, and Occasional Participants. Their trajectories differed in both level and direction. A perception survey of 597 respondents provided complementary learner-reported evidence, integrated with the behavioural strand through a joint display by segment. Perceptions differed across segments, while individual-level correlations between perceptions and behaviour were small, and learners with low recorded participation could report positive perceptions of the points system alongside external barriers. Segments assigned from the first four weeks were then checked against eleven weeks of later platform records: 94% of the Thriving Core attended at least ten further sessions and 22% completed the internship, against under 7% and under 1% in the low-engagement segments. The findings suggest that gamified participation data are more informative when interpreted as longitudinal, opportunity-aware behavioural indicators rather than cumulative scores alone.

---


### 299. [Determining Vertical Displacement of Agricultural Areas Using UAV-Photogrammetry and a Heteroscedastic Deep Learning Model](https://arxiv.org/abs/2609.39756)

**<font color=#1a73e8>作者：</font>** Wojciech Gruszczyński, Edyta Puniach, Paweł Ćwiąkała 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This article introduces an algorithm that uses a U-Net architecture to determine vertical ground surface displacements from unmanned aerial vehicle (UAV)-photogrammetry point clouds, offering an alternative to traditional ground filtering methods. Unlike con-ventional ground filters that rely on point cloud classification, the proposed approach em-ploys heteroscedastic regression. The U-Net model predicts the conditional expected val-ues of the elevation corrections, aiming to reduce the impact of vegetation on determined ground surface elevations. Concurrently, it estimates the logarithm of the elevation cor-rection variance, allowing for direct quantification of the uncertainty associated with each elevation correction value. The algorithm was evaluated using three metrics: the root mean square error (RMSE) of vertical displacements, the percentage of nodes with deter-mined displacement values, and the percentage of outliers among those values. Perfor-mance was assessed using the technique for order of preference by similarity to ideal so-lution (TOPSIS) method and compared against several ground-filter-based algorithms across four datasets, each including at least two time intervals. In most cases, the U-Net-based approach demonstrated a slight performance advantage over traditional ground filtering techniques. For example, for the U-Net-based algorithm, for one of the test da-tasets, the RMSE of the determined subsidences was 6.1 cm, the percentage of nodes with determined subsidences was 80.5%, and the percentage of outliers was 0.2%. For the same case, the algorithm based on the next best model (SMRF) allowed an RMSE of 7.7 cm to be obtained; for 77.3% of nodes, the subsidences were determined; and the percentage of outliers was 0.3%.

---


### 300. [Riemannian Flow Models with Reinforcement Learning for Molecular Crystal Structure Prediction](https://arxiv.org/abs/2609.39773)

**<font color=#1a73e8>作者：</font>** Thomas Egg, Harry Winston Sullivan, Maya M. Martirossyan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crystal structure governs material properties, making crystal structure prediction (CSP) a fundamental problem in materials science. Generative models are a promising approach for solving this problem, but the prevalence of polymorphism, coupled with large unit cells and complex packing geometry, makes the molecular CSP task challenging for existing models. To address this, we introduce Coarse-Grained Open Materials Generation (CG-OMatG), an equivariant Riemannian flow-based generative model. CG-OMatG predicts molecular crystal structures \textit{via} a coarse-grained, hierarchical representation. CG-OMatG treats molecules as rigid bodies---performing both inter- and intra-molecular message passing to construct a geometric representation for molecular packings---and learns to reconstruct molecule centroid positions, orientations, and lattice parameters, conditioned on chemical species and conformer geometry. We train the model on subsets of the Open Molecular Crystals (OMC25) and Cambridge Structural Database (CSD) datasets. Further, we fine-tune the model \textit{via} policy gradient reinforcement learning to steer the model towards generating low-energy candidate structures. We validate the generated structures on the CSP blind test benchmark, assessing agreement with experimentally determined crystals using COMPACK packing-similarity analysis. CG-OMatG exhibits strong performance for generative molecular crystal structure prediction, paving the way for accelerated polymorph screening and organic solid-state materials discovery.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-382](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
