# 📦 其他研究 | 2026年08月10日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-221](./part-05.md)

---

### 151. [SoK: Cryptographic Key Recovery for Cryptoasset Custody and Financial Technologies](https://arxiv.org/abs/2608.07104)

**<font color=#1a73e8>作者：</font>** Francisco Javier Becerra Sanchez, Antonio Ken Iannillo, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptoasset systems often bind cryptographic key control to financial control: losing a wallet seed, custody share, hardware device, or smart-account credential can remove spend authority, while compromised recovery can enable theft. Existing work treats recovery through separate vocabularies--key backup, secret sharing, account recovery, credential re-issuance, social recovery, and asset migration--making mechanisms and tradeoffs difficult to compare.
This paper presents a Systematization of Knowledge (SoK) on cryptographic key recovery for cryptoasset custody and financial technologies. Starting from a 118-paper systematic-review discovery corpus, we derive a 77-paper synthesis corpus and code each retained system in a master matrix covering recovered objects, recovery semantics, mechanisms, enrollment and storage, authorization, trust placement, failure events, post-recovery state, validation evidence, deployment status, privacy, usability, and limitations. The matrix supports an axis-first taxonomy that separates secret-restoring, hybrid, control-restoring, forensic/extractive, and framework-oriented recovery.
Our central observation is that recovery is not a single operation: systems may reconstruct an original secret, regenerate a seed, restore a share, reissue a credential, migrate signing authority, restore account control, move assets, or extract forensic artifacts. We derive a generalized construction model, check it against production-facing designs, and identify six findings: recovery semantics are heterogeneous; recovery shifts trust; liveness improvements create abuse paths; post-recovery lifecycle management is uneven; protocol evidence outpaces user evidence; and recovery metadata remains underprotected. These gaps motivate a research agenda for recovery-aware financial technologies.

---


### 152. [Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge](https://arxiv.org/abs/2608.07106)

**<font color=#1a73e8>作者：</font>** Niclas Meyer, Stefan Reitmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying three-dimensional deep learning frameworks to low-power embedded processors is bottlenecked by the unstructured nature of spatial data and the resource-intensive distance sorting algorithms often used before neural network inference. To address this gap, this paper presents a hardware-constrained workflow optimized for native execution on the Raspberry Pi 5. To account for the reality gap between noiseless, clean computer-aided design (CAD) datasets and real-world sensor data, we use physics-based simulation to construct a synthetic LiDAR dataset. Cross-dataset evaluations demonstrate a substantial drop in classification accuracy when networks trained on clean CAD data are evaluated on synthetic LiDAR sensor data, highlighting the critical need for sensor-aware training. To address the latency bottleneck of traditional geometric preprocessing on edge CPUs, we integrate an isolated, feature-driven Critical Points Layer (CPL) as a frontend filter. Our results show that the pretrained CPL deterministically compresses raw 1024-point clouds to a subset of 40 to 60 unique coordinates. When profiled on the ARM Cortex-A76 processor, the complete pipeline achieves an inference throughput of approximately 50 FPS while maintaining an instance classification accuracy of 88.36%, demonstrating the viability of deterministic real-time 3D perception at the edge.

---


### 153. [Modular TTT: Rethinking Test-Time Training as Composable Modules](https://arxiv.org/abs/2608.07110)

**<font color=#1a73e8>作者：</font>** Bohao Tang, Zhen Qin, Yuqi Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) views sequence modeling as an online learning problem in which fast weights are updated by an internal learning rule. Despite the growing number of TTT variants, existing approaches typically hard-code each variant separately, which makes it difficult to design new TTT methods and to isolate the role of each component. To address this, we propose Modular TTT, a framework that represents the inner learner as a directed acyclic graph and exposes the fast-weight network, loss function, learning rate, weight decay, and normalization as explicit design dimensions. Modular TTT automatically composes primitive-level train-view forward, train-view backward, and causal query-view rules into the full graph-level TTT computation, including the fast-weight state transition. Using Modular TTT, we systematically ablate the components of TTT and find that small learning-rate initialization, weight decay, and a single-layer nonlinearity improve performance, while MSE and inner-product losses perform similarly. Deeper fast-weight networks and normalization tend to hurt performance because they induce excessively large activations, while residual connections and gating provide little measurable benefit. Guided by these findings, we train the best resulting variant as 410M- and 1.45B-parameter models on 100B tokens, and observe training loss and benchmark performance comparable to Gated DeltaNet.

---


### 154. [Geometry-Aware Camera Localization for Bronchoscopy](https://arxiv.org/abs/2608.07116)

**<font color=#1a73e8>作者：</font>** Lumin Chen, Qingyao Tian, Jinpeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera localization in bronchoscopy remains a challenging problem due to stringent accuracy requirements, real-time constraints, and limited training data. Compared to natural scenes, the confined anatomical structures demand millimeter-level precision, while intraoperative guidance necessitates low-latency inference. However, existing methods often fail to effectively exploit preoperative geometric priors, limiting their robustness and accuracy. To address these limitations, we propose a unified geometry-aware bronchoscope localization framework (GABL) that effectively fuses preoperative structural priors with paired intraoperative video to estimate 6-DoF camera poses. Specifically, to address visual ambiguity in complex airways, we propose a graph-guided coarse-to-fine localization scheme that effectively leverages structural priors for precise pose estimation. Furthermore, to mitigate pose jitter and bridge the visual-structural gap, we integrate a Transformer-based tracking model with a novel RGB-depth matching objective, jointly enforcing spatio-temporal and geometric consistency. Extensive experiments demonstrate that our method yields remarkable reductions of 8.37% and 31.76% in translation and rotation errors over the prior state-of-the-art, alongside 4 times inference speedup (33.6 FPS) for robust real-time bronchoscope localization. Project website: this https URL.

---


### 155. [Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation](https://arxiv.org/abs/2608.07117)

**<font color=#1a73e8>作者：</font>** Bruno Palau, Franziska Vogt, Daria Laslo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reporting is time-consuming and subject to inter-rater variability, making automated report generation an attractive clinical application for Vision-Language Models (VLMs). We benchmark state-of-the-art VLMs on lumbar spine MRI with a focus on diagnostic accuracy and demonstrate that standard lexical and semantic metrics poorly reflect clinical correctness: fluent, well-structured reports can score highly while containing clinically meaningful diagnostic errors. To address this failure mode, we propose an architecture-agnostic framework that augments VLM inputs with spatially localized, disc-level anomaly heatmaps generated by a semi-supervised U-Net++ model. These heatmaps both improve anatomical sensitivity through explicit visual grounding and provide an independent interpretability output for clinical oversight, moving us closer to diagnostically reliable, visually grounded VLMs for lumbar spine MRI interpretation.

---


### 156. [How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2608.07118)

**<font color=#1a73e8>作者：</font>** Lichao Ma, Yang Sun, Shuaitao Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residuals to assign per-action credits that telescope to the trajectory advantage, and feedback-conditioned teacher-student likelihood gaps to allocate each credit across the realized action tokens. Per-action normalization preserves the action-average coefficient and prevents token-level sign flips. We pair this construction with an action-mean reduction, removing the implicit dependence of an action's scalar surrogate weight on its token length. At the behavior policy and before clipping, each action's inner action-mean surrogate equals its TD credit. FACTOR consistently improves over competitive baselines across ALFWorld, WebShop, and ScienceWorld, with every environment-seed comparison favoring FACTOR and the largest gains emerging on the longest-horizon environment. The same hyperparameters transfer without retuning to a larger backbone and to a different model family. Ablations identify TD action credit as the dominant driver of the improvement, with hindsight token allocation contributing complementary gains.

---


### 157. [Multiple Hypothesis Flow Estimation for Video Frame Interpolation under Matching Ambiguity](https://arxiv.org/abs/2608.07120)

**<font color=#1a73e8>作者：</font>** Zibo Su, Jing Kong, Ruixing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many flow-based video frame interpolation (VFI) methods synthesize an intermediate frame by estimating optical flow fields, warping the two input frames, and blending the warped observations. These latent flow fields are typically learned through image-level reconstruction supervision without direct flow annotations. In ambiguous regions containing repetitive or stochastic textures, rotating symmetric structures, or fast motion with blur, the matching evidence for a single query may contain multiple comparable and spatially separated peaks. Although the ground-truth intermediate frame provides indirect supervision, it may not uniquely identify the latent correspondence in ambiguous this http URL several locations provide multiple plausible matches, a single-flow estimator can retain only one displacement and discard the remaining candidates. If the selected match is incorrect or inconsistent with those of neighboring pixels, warping samples content from mismatched locations, producing ghosting, structural distortion, or this http URL address this limitation, we propose a multiple hypothesis flow estimation framework that preserves top-K candidate correspondences and selects one per location through a reliability-guided router. Each hypothesis is initialized from a coarse matching anchor and refined separately through anchor-centered local attention. Frame synthesis is thus conditioned on one selected flow-appearance hypothesis rather than a soft combination of candidate this http URL on the proposed MA-HD benchmark and public VFI benchmarks show that our method achieves the best LPIPS and DISTS among the compared methods.

---


### 158. [Thermodynamic Human-Computer Interaction](https://arxiv.org/abs/2608.07123)

**<font color=#1a73e8>作者：</font>** Uzafir Ahmad Rafaq, Muaz Hassan, Ali Muzaffar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional human-computer interaction models rely on domain-specific techniques to model target prediction; models designed for cursor interaction prediction fail to generalize to mobile interfaces and vice versa. We introduce a unifying framework grounded in thermodynamics, proposing that human interaction is composed of phases in thermodynamic equilibrium and non-equilibrium. To demonstrate this, we derive Fitts' law and the proposed target prediction model from equilibrium thermodynamics by assigning kinetic and potential energies to a moving agent and target. Subsequently, we analyze the shortcomings of the prediction model and Fitts' law in edge cases, such as predicting intent for large targets. This analysis demonstrates that large targets cannot be accurately modeled using equilibrium thermodynamics. The proposed model scales across interaction modalities without modification, requires zero training data, and evaluates in constant O(1) time. Furthermore, we show that design properties such as the color of a button act as independent parameters that influence the attractive force exerted on an agent. Applied to live web prefetching tasks, the framework achieved an efficient Fetch:Click ratio of 1.37 and predicted the user's target with an accuracy of 98.1%.

---


### 159. [PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery](https://arxiv.org/abs/2608.07126)

**<font color=#1a73e8>作者：</font>** Sumaiya Islam, Harsha Kumara Moraliyage  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which point recovery may no longer be possible. We propose PHOENIX (Predictive Health On-orbit Edge Neural Intelligence eXtension) to give the satellite its own fault reasoning capability. A fine-tuned Small Language Model (SLM) compact enough to run on embedded hardware is deployed onboard the CubeSat, running on the flight-proven Aethero NxN-ECM computer, monitoring all sensor readings continuously, and resolving recurring faults using a memory system that stores past repairs so the same inference does not need to run twice. Once per orbit it sends a short structured health report to the ground instead of a raw data dump; six specialized AI agents on the ground read that report and generate validated satellite commands within the 5-10 minute contact window. A generative diffusion model (DDPM) creates synthetic training data because real fault examples make up only 0.57-1.80% of the dataset. We report preliminary results on the ESA Anomaly Detection Benchmark (14 years, 76 channels, 118 labeled faults).

---


### 160. [Online Conformal Prediction Beyond Feedback](https://arxiv.org/abs/2608.07139)

**<font color=#1a73e8>作者：</font>** Joar Skalse, Edoardo Pona, Osvaldo Simeone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is essential when deploying machine learning models in safety-critical applications. Online conformal prediction (OCP) provides theoretically principled uncertainty quantification for arbitrary black-box classifiers and non-i.i.d. data streams by constructing prediction sets that are guaranteed to contain the true label at a user-specified frequency. OCP usually updates prediction sets using feedback from previously deployed predictions. We instead study an OCP setting beyond feedback: on each round, the learner can either output a prediction set or query the correct label, but not both. Thus, no deployed prediction is ever evaluated directly. We reduce this problem to a partial monitoring game in which prediction actions return no observation and a separate query action reveals the label. The reward function is constructed in a way that encourages the learner to output small prediction sets while ensuring that the correct label is covered with a sufficiently high probability. To solve this game, we develop OCP with queries (OCPQ) by adapting the label efficient forecaster of Cesa-Bianchi, Lugosi, and Stoltz (2004) to our setting. For any black box classifier and any (non-i.i.d.) oblivious data stream of length $T$, OCPQ has $O(T^{2/3})$ expected regret and expected coverage at least $\beta-O(T^{-1/3})$ for a user-defined $\beta$, while querying only an expected $T^{-1/3}$ fraction of rounds. This provides coverage comparable to bandit-based OCP methods while requiring no feedback from deployed prediction sets. Experiments on real-world datasets further demonstrate the effectiveness of our approach.

---


### 161. ["Operator, can you hear me?" A Faithful Line into the UNISOC Baseband](https://arxiv.org/abs/2608.07143)

**<font color=#1a73e8>作者：</font>** Eduard Vlad, Philipp Mao, Marcel Busch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Baseband processors are reachable over the radio at all times. Their most security-relevant logic runs deep inside protocol state machines: the control-plane handlers that gate registration, authentication, and session setup. Analyzing that logic systematically requires introspecting the firmware as it runs, which makes re-hosting the baseband necessary. Existing re-hosting work approximates the execution environment and under-approximates the SoC complexity of the baseband processor together with its surrounding components, bringing this state practically out of reach. We instead model each surrounding component, co-processors, SIM, application processor, from what a real device does, and step them in lockstep with the baseband on one shared clock. That makes faithfulness checkable at component interfaces, rather than assumed.
We call this method Unislop and demonstrate it on the UNISOC UDX710, a platform in an estimated 10-15% of cellular modems and in automotive systems, not systematically analyzed before. Starting from a Quectel RM500U-CNV module, we gain code execution, defeat its firmware-integrity check, instrument the baseband, and recover its peripheral environment from the running device. The resulting re-host reaches the same control-plane states as the real device, establishes a full PDU session, and carries real IP traffic on both ingress and egress. The recovered components are shared across UNISOC's baseband lineup, so with additional reverse-engineering effort the same design extends to further targets.

---


### 162. [InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144)

**<font color=#1a73e8>作者：</font>** Minchao Jiang, Xiaoxuan Ma, Shunyu Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables efficient and generalizable 3D reconstruction, but current feed-forward 3DGS methods for scene understanding remain largely category-oriented. In contrast, instance-aware 3DGS methods typically rely on per-scene optimization and often decouple reconstruction from instance and semantic learning, limiting reciprocal interactions among them. We present InstanceSplat, a unified feed-forward 3DGS framework for generalizable 3D reconstruction and instance-aware scene understanding from pose-free multi-view images. In a single forward pass, InstanceSplat constructs an instance-aware Gaussian representation that jointly encodes appearance, geometry, instance identity, and language-aligned semantics. Shared 3D Gaussians ground instance identities across views, producing renderable and cross-view-consistent instance features. To allow reconstruction and scene understanding to benefit from each other, we further design an instance-centric learning strategy that connects reconstruction, instance learning, and semantic learning through shared instance structure. Specifically, instance cues guide reconstruction, language-aligned semantics strengthen the discrimination of confusing same-category instances, and instance regions aggregate semantic evidence into coherent object-level predictions. Experiments on novel-view synthesis, instance segmentation, and open-vocabulary semantic understanding under varying input-view settings and on an unseen dataset demonstrate state-of-the-art performance, practical efficiency, and strong generalization.

---


### 163. [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](https://arxiv.org/abs/2608.07147)

**<font color=#1a73e8>作者：</font>** Xucong Wang, Zhe Zhao, Liheng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

---


### 164. [Interpretable reinforcement learning with decision-tree pruning](https://arxiv.org/abs/2608.07151)

**<font color=#1a73e8>作者：</font>** Mark Leon Ringer, Michel Tokic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning policies are difficult to inspect, but interpreting them is a prerequisite for trustworthiness. Converting a trained policy into explicit decision-tree rules improves transparency and the resulting artifacts often remain too complex for human understanding. We present a pruning process that simplifies such rule-based policies while preserving task performance and making edits to the policy auditable. The process defines a small set of structural and usage-aware operators and evaluates candidate edits by re-executing the policy to measure return and interpretability proxies. This exposes an transformation process from complex to compact policy structures. We investigate this approach on classic control and MuJoCo benchmarks, where pruning traces reveal consistent interpretability improvements while maintaining high performance.

---


### 165. [Machine Learning-Based Inter-Crystal Scatter Recovery for Ultra-High Resolution PET Imaging](https://arxiv.org/abs/2608.07155)

**<font color=#1a73e8>作者：</font>** Alexandre Bernier, Roger Lecomte, Jean-Baptiste Michaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inter-crystal scatter (ICS) events pose a significant challenge in ultrahigh- resolution positron emission tomography (UHR-PET), especially as detector crystals become smaller and their readouts increasingly segmented. Current approaches either reject these events, reducing sensitivity, or accept them with suboptimal positioning algorithms, degrading image resolution. We present a feed forward neural network to optimize ICS event recovery by inferring the line-of-response belonging to the first Compton interaction. Our approach was validated using both Monte Carlo simulations and experimental data from the fully pixelated LabPET-IIbased preclinical and brain UHR-PET this http URL demonstrate a 70% to 106% increase in sensitivity while preserving sub-millimeter spatial resolvability (down to 1.6 mm) compared to conventional methods. This ICS recovery approach is an effective solution that compensates for the lower detection efficiency of small, pixelated detectors in UHR-PET, enabling reduced scan times and lower radiation doses while largely preserving image quality.

---


### 166. [Edge Sparsification via Temporal Forman-Ricci Curvature for Dynamic Graph Learning](https://arxiv.org/abs/2608.07158)

**<font color=#1a73e8>作者：</font>** Poupak Azad, Cuneyt Gurcan Akcora, Kiarash Shamsi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph learning has become essential for analyzing real-world systems whose interactions continuously evolve over time, including financial transaction networks, communication systems, and online social platforms. However, learning from large-scale temporal graphs remains computationally challenging when networks are dense and rapidly changing. To address this limitation, we propose a network-curvature-inspired edge sparsification framework for dynamic graph learning. Our proposed method, TRicci, extends classical Forman-Ricci curvature to directed weighted temporal graphs by capturing structural support, temporal recency, and local interaction competition.
Experiments on 9 transaction networks and 3 temporal graph benchmark datasets demonstrate that the proposed framework preserves predictive performance across multiple graph-level prediction tasks. The results show that TRicci sparsifies temporal graphs by approximately 80% while reducing end-to-end downstream training and inference time by an average of 55.94%, without substantial degradation in predictive performance. Our findings suggest that temporal curvature can serve as a principled basis for scalable temporal graph learning by preserving predictive temporal-structural information under substantial sparsification.

---


### 167. [Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning](https://arxiv.org/abs/2608.07161)

**<font color=#1a73e8>作者：</font>** Shentong Mo, Guolin Ke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. We propose Fluid-DiT, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

---


### 168. [Momba: Network Modernization Improves Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2608.07180)

**<font color=#1a73e8>作者：</font>** Adam Štafa, Santeri Heiskanen, Petr Novotný 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep reinforcement learning (RL) have shown that improving neural network architectures can yield substantial gains in sample efficiency and asymptotic performance without altering the underlying algorithms. In contrast, work on multi-objective reinforcement learning (MORL), which aims to discover a set of policies that balance trade-offs among conflicting objectives, has predominantly focused on algorithmic innovations, leaving the area of architectures underexplored. While the optimal policies and value functions can differ significantly depending on the trade-offs, MORL algorithms commonly represent them with simple feedforward networks conditioned on the trade-off. This raises the question of whether the performance of the algorithms could be improved with more expressive function approximators. In this paper, we integrate recent advances in neural network design: (i) observation and feature normalization, (ii) weight normalization, and (iii) modeling of distributional returns with an entropy-regularized MORL algorithm. The empirical results across standard continuous control benchmarks demonstrate that these changes substantially improve the quality of the produced solution sets without requiring major changes to the underlying algorithm.

---


### 169. [Conformal Fusion Under Missing Modalities](https://arxiv.org/abs/2608.07183)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion architectures typically assume all modalities are available at inference, yet sensor failures, acquisition variability, and cost constraints routinely produce incomplete observations. Existing work treats modality absence as a prediction-accuracy problem, leaving a more basic question unanswered: whether a model's confidence estimates remain calibrated when an entire input stream is removed. We argue that missing-modality robustness and calibrated uncertainty are a single coupled property, and introduce Modality-Conditioned Conformal Fusion (MCCF), an architecture that addresses both at once. MCCF combines a multimodal bottleneck fusion backbone trained with modality dropout, per-modality evidential heads producing modality-decomposed Dirichlet distributions, and a Dempster-Shafer combination rule that fuses the per-modality evidence into a joint predictive distribution; an absent modality contributes vacuous evidence that is structurally ignored, so the fused uncertainty automatically reflects the reduced information without test-time imputation. A Mondrian conformal calibration module keyed on the modality-presence mask then provides finite-sample group-conditional coverage for every non-empty modality subset. MCCF is, to our knowledge, the first method with formal coverage guarantees under arbitrary modality availability through architectural integration rather than post-hoc recalibration, and the evidential decomposition yields per-modality vacuity scores that localise uncertainty to the absent modality responsible. Across a synthetic problem and three real multimodal benchmarks, MCCF holds its target coverage on every modality-presence subset, substantially narrows the coverage gap between full and partial modalities relative to a marginal split-conformal baseline, and imposes no measurable accuracy cost relative to temperature-scaled and evidential baselines.

---


### 170. [SetEasy: A Multi-Modal Classroom Engagement Assessment and Seating Optimization Framework](https://arxiv.org/abs/2608.07188)

**<font color=#1a73e8>作者：</font>** Zhihao Xie, Hongye Yang, Shien Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SetEasy optimizes classroom engagement in fixed seating grids. It fuses multimodal sensing (wristband physiology, 4K video, environmental data) and trains a v-Gage model grounded in a revised ISEQ. Each week, two-week engagement forecasts are mapped to a student-seat utility matrix, and CP-SAT generates seating plans under visual-access and social-dynamics constraints. In a four-week deployment (23 students, 331 classes), v-Gage converged across affective, behavioral, cognitive, and overall dimensions, cutting RMSE from 0.75 to 0.53. Optimization raised mean engagement from 0.30 to 0.70, with over two-thirds of seats reaching high engagement and back-row low-activity patterns markedly reduced. These results show that, without hardware changes, interpretable, data-driven seating strategies can substantially enhance engagement. The multimodal "assessment + optimization" paradigm offers a transferable, sustainable path to culturally responsive, differentiated spatial design amid global homogenization.

---


### 171. [MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor](https://arxiv.org/abs/2608.07192)

**<font color=#1a73e8>作者：</font>** Beatrice Alessandra Motetti, Tanguy Dugas du Villard, Matteo Risso 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-resolution infrared (IR) array sensors represent an interesting solution for privacy-preserving human sensing in embedded systems. In this letter, we describe a smart multi-pixel IR sensor integrating a 16$\times$16 thermal MOSFET (TMOS) array and a RISC-V microcontroller extended with low-precision SIMD instructions, capable of on-device learning and continual adaptation for pose and gesture recognition tasks under tight memory and power constraints ($<$32kB on-chip memory, $\approx$1.5mW). To avoid the memory overheads of backpropagation and replay buffers, we adopt a prototype-based Nearest Class Mean (NCM) classifier in which a simple Convolutional Neural Network (CNN) encoder is trained and quantized offline, while class prototypes are stored and updated on the device in streaming mode. With experiments on two datasets, we show that this approach yields accuracy on par with a conventional classifier, with negligible latency overheads in both the classification and the prototype update ($<$0.29% considering both phases), effectively enabling online adaptation of the perception framework.

---


### 172. [EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision](https://arxiv.org/abs/2608.07196)

**<font color=#1a73e8>作者：</font>** Chao Fei, Qingyi Si, Kaihua Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many methods for automated multi-agent system design optimize prompts and topologies during an initial design stage and then deploy the resulting system unchanged on subsequent samples. Experience from these samples is rarely consolidated into reusable system updates, while accuracy-oriented designs may incur high token costs. We introduce EMAS (Evolving Multi-Agent System), which uses this experience to revise MAS topology and prompts without updating LLM parameters, either to improve accuracy or to reduce cost. EMAS converts traces into structured diagnoses that specify a revision operation and target. It generates a candidate revision only when the same diagnosis recurs across samples and applies it only if paired validation against the current MAS meets the corresponding acceptance criterion. Across four benchmarks and two LLMs, EMAS attains the highest task-weighted overall accuracy for both backbones and is best or tied in six of eight model--benchmark settings. Within two evolution epochs, EMAS achieves relative gains of 6.30% and 20.10% in task-weighted accuracy on Kimi-K2-6 and Qwen3.6-27B, respectively. On MBPP with Qwen3.6-27B, EMAS raises accuracy from 55.09% to 89.12% while reducing token use per task by 62.2%. These results show that EMAS can turn experience from new samples into reusable updates to MAS topology and prompts.

---


### 173. [Flow-Corrected Shape Optimization: Taming Manifold Drift in High-Dimensional 3D Models](https://arxiv.org/abs/2608.07199)

**<font color=#1a73e8>作者：</font>** Emilien Seiler, Nicolas Talabot, Yingxuan You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optimizing 3D shapes within the latent spaces of deep generative models is fundamental to computer assisted engineering, yet remains prone to a critical failure mode we term manifold drift: the tendency of gradient-based optimization to move latent vectors away from the manifold of valid shapes. This problem is exacerbated in state-of-the-art 3D shape generative models that operate in increasingly high-dimensional latent spaces where valid shapes occupy a vanishingly small fraction of the full space. Existing mitigation strategies, including latent regularization and flow-matching approaches, either sacrifice expressiveness, demand a difficult trade-off between objective guidance and generative fidelity that remains prone to manifold drift, or are computationally infeasible to scale to modern, large-capacity 3D shape models. We introduce a novel optimizer-corrector framework that alternates between gradient steps for objective minimization and guided flow matching to drive the latent state back to the valid shape manifold. By decoupling objective minimization from flow-based correction, optimizing freely and correcting strictly, this alternating design avoids inherent trade-offs, preserving geometric validity without sacrificing expressiveness while remaining computationally feasible on modern 3D shape models. We demonstrate its effectiveness across generative priors of varying complexity, from simple vector latent spaces to large-scale architectures across a variety of downstream optimization tasks, including aerodynamic drag reduction and object compliance optimization.

---


### 174. [HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification](https://arxiv.org/abs/2608.07204)

**<font color=#1a73e8>作者：</font>** Zhenchao Wang, Xin Chen, Luoxi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific claim verification over a cited paper requires predicting the claim--paper relation and identifying the paragraphs that justify that prediction. This setting poses two linked challenges: within-paper distractors often resemble genuine evidence, while a classifier trained on gold evidence must operate on retrieved evidence at inference. We present HNR-DAC, a two-stage framework that trains each stage on the cases it will actually encounter. Hard-Negative Reranking (HNR) quantifies evidence confusability using a base reranker's scores on non-gold paragraphs and contrasts gold evidence against the most confusable candidates. Distribution-Aligned Classification (DAC) trains on the Top-1 paragraph produced by the same frozen HNR used to construct inference inputs, while HNR's Top-3 paragraph identifiers provide the evidence output. On the NLPCC 2026 Task 10 Track 2, the final configuration obtains 97.21% Hit@3, 95.79% Macro-F1, 94.47% Joint@3, and an average score of 95.13%. The corresponding submission ranks third on the official Track 2 leaderboard while achieving the highest overall Macro-F1 of 93.05%, alongside 70.16% Joint@3 and an average score of 81.61%.

---


### 175. [From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL](https://arxiv.org/abs/2608.07213)

**<font color=#1a73e8>作者：</font>** Jiaqian Wang, Yutao Qi, Wenjin Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling can correct difficult text-to-SQL queries, but the extra computation is normally discarded after each answer. Systems increasingly retain verified repair episodes, yet evaluations still report one end-to-end score. It cannot distinguish replay on recurring questions from help on unseen questions, or identify the responsible memory choice. We call measuring this future value the crystallization problem. Our controlled evaluation holds the single-shot solver fixed and varies one memory choice at a time. We separately measure replay, cross-question retention, and held-out same-database transfer. On BIRD, storing verified corrected queries improves held-out first-attempt accuracy by 4.34 percentage points. This gain captures 44.4% of the accuracy headroom provided by on-demand repair on the same questions. Controlled interventions identify database-specific content as the main operating ingredient. Reliable verification and broader retrieval coverage yield supported gains; richer formats and elaborate retrievers do not. Open-source code, evaluation artifacts, and reproduction instructions are available at this https URL.

---


### 176. [Beyond the Black Box: Interpretable Models of Human Randomisation Failures](https://arxiv.org/abs/2608.07220)

**<font color=#1a73e8>作者：</font>** Ngoc Linh Dao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed strategy equilibrium predicts i.i.d play: past actions should not help predict future decisions. Human players, however, systematically depart from this benchmark, and in O'Neill's zero sum card game, these departures can be predicted by black box sequence models such as LSTMs. This paper asks whether that predictive power can be achieved by transparent alternatives that also reveal the behavioural structure behind it. Using 84,060 decisions from 2,802 pairs, the analysis first benchmarks naive and behavioral models against interpretable machine learning and deep learning models, then evaluates the modified EWA specifications of prior work against these benchmarks and uses the LASSO diagnostics to motivate a further nested frequency tracking extension. The results show that repeat or avoid behavior, especially players' management of their own recent action histories, accounts for most of the interpretable and strategically exploitable signal, while frequency tracking adds little out of sample.

---


### 177. [Skaling: Chinchilla's Exponents Meet Kaplan's Coupling](https://arxiv.org/abs/2608.07222)

**<font color=#1a73e8>作者：</font>** Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute Percentage Error (MAPE) by 1.5-3x across both interpolation and extrapolation regimes. When paired with a sparse grid strategy restricted to low-compute regimes, the Skaling law achieves accurate full-grid extrapolation using approximately 10x less compute than uniform sweeps. By enabling reliable performance prediction from small-scale experiments, the Skaling law provides a more robust and resource-efficient framework for allocating compute budgets in next-generation model training.

---


### 178. [Stochastic Autoregressive Learning](https://arxiv.org/abs/2608.07224)

**<font color=#1a73e8>作者：</font>** Ilan Doron-Arad, Idan Mehalel, Elchanan Mossel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by LLMs, which generate outputs by iteratively sampling from next-token distributions, we introduce a PAC-learning model for binary stochastic autoregressive learning. This generalizes the deterministic autoregressive learning framework of Joshi et al., COLT 2025. In our model, one fixed generator assigns a Bernoulli next-token distribution to every prompt string. Starting from an input prompt, a token is sampled and appended to the prompt; the same generator is then applied again to this expanded prompt; this procedure is repeated for $M$ steps. Three forms of supervision are considered: base one-step samples, chain-of-thought (CoT) samples that reveal full random trajectories of length $M$, and end-to-end (e2e) samples that reveal only the final token of length $M$ trajectories. For a generator class, we study the minimum number of samples $m_{base}(\varepsilon),m_{CoT}(\varepsilon), m_{e2e}(\varepsilon)$, resp., required to learn the one-step probabilities in the base model, and the final-token probability in the CoT and e2e models, under squared loss error~$\varepsilon$.
We show that stochastic autoregressive learning fundamentally differs from the deterministic theory. At scale $\varepsilon$, there is no universal comparison between the three learning tasks: both $m_{CoT}/m_{base}$ and $m_{e2e}/m_{CoT}$ can be made simultaneously arbitrarily larger than $M/\varepsilon$, the natural analogue for the existing deterministic results. Nevertheless, after altering scales, for every class, CoT learning at scale $\varepsilon$ is upper-bounded by base learning at scale $\varepsilon/M^2$, whereas e2e learning at scale $\varepsilon$ is upper-bounded, up to logarithmic factors, by $(M/\varepsilon) m_{CoT}(\Theta(\varepsilon))$. These dependencies and scales are essentially tight. We complement these bounds by studying dimension $d$ logistic functions in our model.

---


### 179. [Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis](https://arxiv.org/abs/2608.07228)

**<font color=#1a73e8>作者：</font>** Idil Gözel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse.
We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why.
The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

---


### 180. [From probability to causality in probabilistic logic programming](https://arxiv.org/abs/2608.07230)

**<font color=#1a73e8>作者：</font>** Zora Wurm, Kilian Rückschloß, Felix Weitkämper  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic logic programming is a formalism of statistical relational artificial intelligence that supports causal queries, including interventions from outside the system. When the structure of a probabilistic logic program is learned from data, however, only probabilistic information is used, and a single probability distribution may be compatible with several causal orders. This leads to ambiguity in interventional reasoning, raising the question of when the causal order is uniquely determined by the distribution. Exploiting the relationship between acyclic probabilistic logic programs and Bayesian networks, we derive conditions under which the probabilistic information encoded in a program determines a unique causal order. We also incorporate constraints arising from relational structure by taking into account prescribed sets of causal symmetries induced by the underlying relational vocabulary. The result is a method for verifying when a learned probabilistic logic program supports well-defined intervention semantics.

---


### 181. [Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion](https://arxiv.org/abs/2608.07249)

**<font color=#1a73e8>作者：</font>** Eric Cullhed, Albin Thörn Cleland  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Stoicheia, a 405M-parameter character-level masked-diffusion encoder for Ancient Greek whose input factors into five aligned, independently maskable planes: letters, word and sentence boundaries, diacritics, capitalization, and punctuation. A single backbone can therefore restore lacunae, re-segment, accentuate, and punctuate unspaced text without task-specific retokenization. We pretrain it on an open, revision-pinned corpus of 380M words and release eleven checkpoints: ten rotated, decontaminated folds, guaranteeing that for any given literary passage at least one released model has never seen its text, and one with no exposure to documentary texts. Three experiments - reconstruction of damaged inscriptions and papyri, morphosyntactic tagging and dependency parsing, and macronization with metrical scansion - each carry a matched random-initialization control, isolating what character-level diffusion pretraining contributes: 5.6 CER points on inscription reconstruction, 12.9 LAS on parsing, and 6.0 points of balanced accuracy on macronization. On Ithaca's own test split, with identical frozen samples and strict scoring, Stoicheia reduces character error relative to both prior state-of-the-art systems, from 24.6 (Ithaca) and 23.5 (its 2025 Aeneas-framework successor) to 15.5, and raises top-1 accuracy from 63.0 and 64.0 to 74.5.

---


### 182. [CANIS: Generation-Assisted 3D Canonicalization via an Image-Semantic Bridge](https://arxiv.org/abs/2608.07256)

**<font color=#1a73e8>作者：</font>** Kendong Liu, Yuxin Yao, Junhui Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Canonicalizing 3D object orientation is fundamental to 3D understanding and analysis. Existing approaches often rely on geometric cues, although 3D canonicalization ultimately requires a semantically meaningful orientation. To address this gap, we propose CANIS, a category-agnostic, generation-assisted framework that introduces the semantic orientation prior of a frozen image-to-3D generative model into 3D canonicalization, without canonicalization-specific training or category-specific templates. Specifically, CANIS first renders the input object from candidate viewpoints, selects an informative view, and generates a proxy in a canonical orientation. During generation, a sparse structural latent encoded from the input guides the proxy to preserve the geometry of an object. CANIS then uses the selected image as a semantic bridge between the input and the proxy. Image patches identify semantic regions on the proxy, and depth back-projection locates the corresponding regions on the input. The resulting semantic anchors constrain geometric matching, from which we estimate the rigid transformation that canonicalizes the input. Experiments on synthetic benchmarks validate CANIS and its key components, while qualitative results on partial observations and OmniObject3D suggest its applicability to incomplete and real-world scans. CANIS also improves downstream 3D classification, part segmentation, and dense correspondence under arbitrary rotations. Project page: this https URL.

---


### 183. [WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN](https://arxiv.org/abs/2608.07267)

**<font color=#1a73e8>作者：</font>** Yuehao Huang, Yunzi Wu, Xiaotao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric training does not explicitly model how the agent's visual observations should evolve under its predicted motion. Generative world-action models (WAMs) jointly predict future observations and actions, yet existing WAMs for continuous VLN do not condition joint future-view and action generation on geometry-aware representations inferred from the observed history. We present WNM-3D, a generative World Navigation Model with 3D scene conditioning for continuous VLN. To consolidate past observations into persistent scene context, a frozen feed-forward geometry encoder extracts geometry-aware representations from the monocular egocentric RGB history, and a trainable 3D Scene-to-Token Adapter converts them into a fixed-length prefix in the token space of the world-action Diffusion Transformer. Through block-causal attention, this prefix conditions every future video-action block, providing a shared geometric context for both future-view and action generation. We train WNM-3D through supervised world-action fine-tuning on A*-generated demonstrations, DAgger-style adaptation on policy-visited states, and DanceGRPO-based closed-loop policy optimization. Experiments on GN-Bench show that WNM-3D outperforms strong VLM-based navigation policies and its 2D-conditioned counterpart in closed-loop navigation. On a fixed near-goal evaluation set, WNM-3D also achieves higher flow-action consistency and lower visual-motion error.

---


### 184. [Incidental Visualizations: Augmented Reality as a Medium for Contextual Information](https://arxiv.org/abs/2608.07271)

**<font color=#1a73e8>作者：</font>** Matilde Heitor, João Moreira, Daniel Gonçalves  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In today's fast-paced world, delivering information efficiently and unobtrusively is essential. While ambient and glanceable visualizations provide real-time data, they can increase cognitive load and disrupt primary tasks. We investigate incidental visualizations, a novel concept in information visualization designed to present contextually relevant information briefly and spontaneously, with minimal user interaction. Augmented Reality offers an ideal medium for this integration, embedding visualizations directly within the user's environment. Through controlled user studies on logic-based game tasks (Sudoku and Connect 4), this work compares ambient, periodic, and incidental visualization patterns in terms of comprehension accuracy, performance, and disruption. Results indicate that IVs deliver information as effectively as ambient displays while minimizing disruption, highlighting their potential for adaptive, context-aware information delivery in AR environments.

---


### 185. [TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split Federated Learning](https://arxiv.org/abs/2608.07274)

**<font color=#1a73e8>作者：</font>** Yuhan Xie, Jingrong Huang, Chen Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) facilitates privacy-preserving collaborative training with reduced client-side overhead. However, its split architecture introduces unique attack surfaces, rendering it vulnerable to diverse poisoning attacks. Most existing defenses fail to exploit the split paradigm, limiting their ability to detect and contain malicious behaviors at an early stage. To bridge this gap, we propose Target-Oriented Feature Decoupling (TOFD), a unified framework that jointly enables proactive detection and robust optimization against a wide range of poisoning attacks. TOFD operates in three stages: (1) Target Inference, which identifies potential attack targets by refining class-wise safe zones via class-specific Margin Perturbation (MP); (2) Sample Purification, which adaptively filters poisoned smashed data using thresholds calibrated through cross-class min-max normalization of MP; and (3) Decoupling Optimization, which leverages an adversarial guidance model to capture attack-induced patterns and decouple their influence during optimization, thereby suppressing residual adversarial effects. We provide theoretical guarantees for the convergence of TOFD. Extensive experiments on five datasets demonstrate that TOFD consistently outperforms state-of-the-art defenses under diverse attack scenarios, achieving superior robustness with low computational overhead suitable for practical deployment.

---


### 186. [Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction](https://arxiv.org/abs/2608.07280)

**<font color=#1a73e8>作者：</font>** Assaf Caftory, Almog Zemach, Moshe Butman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent simulations are widely used to study complex social and ecological systems, where rich and often unexpected emergent behaviors arise from local interactions. A large body of prior work has focused on analyzing such emergent dynamics across domains. In this paper, we move beyond analyzing emergent behavior and introduce a learning-based mechanism for actively shaping it via social reward modeling. We introduce Multi-Agent Reward Prediction (MARP), a simple framework that extends preference-based reward modeling to multi-agent reinforcement learning. While the framework is designed to be applicable across multi-agent settings, the present empirical validation is limited to a single environment, and we therefore present MARP as a proof of concept within the studied domain. Rather than relying on handcrafted rewards, MARP learns a shared reward model from episode-level evaluations of collective outcomes, enabling decentralized agents to align their behavior with global social objectives.
We study MARP in the Harvest Game, a canonical sequential social dilemma modeling common-pool resource management and related real-world challenges. Our results show that MARP can be tuned to produce behavior that is more closely aligned with target social metrics than standard reward-based baselines, while the learned reward model captures subtle environmental structure without explicit programming. Crucially, MARP supports multiple and composite social objectives within a single training regime. By modifying only the high-level evaluation metric, the same framework seamlessly aligns agent behavior with diverse goals, including sustainability, equality, and peace, as well as combinations of individual and group-level objectives. These findings demonstrate that emergent multi-agent behavior can be treated not only as a phenomenon to study, but as a target of principled, data-driven regulation.

---


### 187. [Gaze Behavior in Visual World Experiments Can be Modeled With Off-the-shelf Language-Vision Encoders](https://arxiv.org/abs/2608.07282)

**<font color=#1a73e8>作者：</font>** Rahul Murali Shankar, Titus von der Malsburg, Sebastian Padó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The recent advances in neural language models have also spurred much work in computational psycholinguistics, asking whether neural LMs are also promising models of human language processing. However, work has been overwhelmingly focused on the unimodal case of written or spoken language. In contrast, multimodal experimental paradigms, like visual world studies that present participants with both visual and linguistic input simultaneously, have been neglected. In this paper, we present a novel approach that predicts gaze behavior in visual world studies. It does so by combining a simple multi-modal bi-encoder model of the CLIP family with a bimodal attribution method. We demonstrate the ability of this approach to robustly replicate the results of a seminal English visual world study which shows hu- man predictive processing. Remarkably, it does so without a generative architecture and without the need for fine-tuning, despite not being trained for this task.

---


### 188. [A foundation-model approach to pediatric headache classification from rs-fMRI](https://arxiv.org/abs/2608.07287)

**<font color=#1a73e8>作者：</font>** Guilherme S. Imai Aldeia, Clara Moon, Julie Shulman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Headache is the most common neurological disorder in children and substantially affects quality of life. We investigated whether resting-state functional MRI (rs-fMRI) can support pediatric headache classification using machine learning. We encoded rs-fMRI data using NeuroSTORM, a recent foundation model, and fine-tuned it to distinguish healthy controls from children with headache and subsequently classify headache subtypes. We compared NeuroSTORM with a standard neuroscience approach using functional-connectivity (FC) matrices derived from brain activity as predictors. Using 189 rs-fMRI scans from 110 individuals collected across two visits (prevalence of any headache: 74%), NeuroSTORM achieved an area under the receiver operating characteristic curve (AUROC) of 0.82 (95% CI, 0.82-0.82) and an area under the precision-recall curve (AUPRC) of 0.93 (95% CI, 0.93-0.94) for discriminating headache from non-headache. In contrast, models trained on FC matrices showed lower performance (AUROC, 0.67 [95% CI, 0.67-0.67]; AUPRC, 0.85 [95% CI, 0.85-0.85]). In multiclass classification of healthy controls, chronic migraine, and non-chronic headaches (e.g., post-viral headache, new daily persistent headache, post-traumatic headache), NeuroSTORM achieved a macro-AUROC of 0.69 (95% CI, 0.68-0.69). Results suggest that the approach can distinguish chronic migraine but has difficulty differentiating other headache subtypes from chronic migraine. Overall, under limited-data conditions, NeuroSTORM appears to capture latent rs-fMRI representations that transfer to headache-related tasks without relying on FC features. These findings provide proof of concept for fMRI-based prediction of pediatric headache and highlight potential future utility for subtype identification and individualized treatment strategies.

---


### 189. [FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching](https://arxiv.org/abs/2608.07294)

**<font color=#1a73e8>作者：</font>** Suman Cha, Seongchan Lee, Dohyun Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating mixed-type tabular data requires jointly modeling diverse feature distributions and their complex cross-column dependencies. Variational flow matching handles distinct endpoints via factorized distributions, yet leaves feature-specific processing and cross-column interactions implicit within a shared backbone. We introduce Feature-wise Unified Specialization with cross-column Exchange (FUSE) to explicitly separate these roles. FUSE applies separate adaptive mixture modules to numerical and categorical features, allowing each feature to combine shared specialized subnetworks, while joint attention preserves information exchange across all columns. We also characterize the excess population risk from restricted conditioning contexts and bound the continuous Wasserstein generation error by endpoint-prediction risk. Comprehensive experiments on eight tabular datasets demonstrate that FUSE achieves strong and consistent performance across distributional fidelity and downstream utility metrics.

---


### 190. [Learning Long-Term Educational Investment Policies under Residential Sorting](https://arxiv.org/abs/2608.07295)

**<font color=#1a73e8>作者：</font>** Honglei Guo, Shuo Chen, Mingjie Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Allocating public-school investment effectively and fairly is difficult when school access depends on residence. School improvements can raise nearby housing demand and prices, reshape enrollment, and potentially limit access for lower-income households. These effects evolve as residential sorting changes school composition, quality, and future investment needs. Existing approaches often study school funding, household choice, and housing markets separately, while static models can miss their interconnected, long-term effects. We address this gap with a dynamic multi-agent framework that links government investment, household sorting, housing prices, population turnover, enrollment, and evolving school quality. A government planner uses reinforcement learning (RL) to identify multiyear allocation policies that account for household responses while balancing aggregate educational access and equity. In simulations, our RL-based policy attains the highest access level (0.4780) and second-lowest access Gini coefficient (0.0164) among representative baselines, demonstrating a favorable effectiveness-equity balance. The results also indicate reduced socioeconomic stratification in educational access. By making education-housing feedback explicit, our framework supports long-term analysis of how school investment shapes educational opportunity over time.

---


### 191. [EliSeg: Verified Target Construction for Report-Grounded Abnormality Segmentation](https://arxiv.org/abs/2608.07299)

**<font color=#1a73e8>作者：</font>** Chengyi Peng, Haoyu Yang, Meixing Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reports describe clinical observations but do not specify executable segmentation targets. They may contain present, negated, prior,uncertain, or irrelevant findings, while multiple valid abnormalities may coexist. Existing segmentation methods largely bypass this ambiguity by receiving a target identity or spatial prompt before inference, which acts as a hidden target oracle. We study report-grounded abnormality segmentation, where a model must determine target eligibility, cardinality, and finding-to-mask correspondence directly from an unfiltered report before delineating the corresponding regions. We propose \textbf{EliSeg}, an atcor--verify--revise framework that integrates target construction with mask generation. A grammar-constrained Actor proposes target slots and masks, an independent text-only Verifier reconstructs the eligible finding inventory, and Revision selectively re-executes the shared Actor when their target structures disagree. EliSeg requires no predefined target identity, finding prompt, point, or bounding box. Experiments on MIMIC-CXR-ILS show that EliSeg consistently outperforms direct segmentation methods and extract-then-segment cascades across findings, while effectively suppressing masks for ineligible report mentions. Ablation studies confirm the complementary roles of verification and revision, and evaluation on CheXlocalize demonstrates effective transfer of the EliSeg to an external this http URL is available at this https URL.

---


### 192. [Winning by Peeking: Unenforced Budgets and Test-Set Selection Inflate Short-Budget AutoML Comparisons](https://arxiv.org/abs/2608.07303)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparisons between AutoML systems at short time budgets -- tens of seconds rather than hours -- are common in tool READMEs and workshop papers, and they are easy to get wrong. We report a case study in which a simple AutoML engine, Orcetra, appeared to beat FLAML and AutoGluon on 513 OpenML datasets, winning 57.1% of them at a nominal 60-second budget and 78.4% of datasets against FLAML alone at 30 seconds. Both margins came from protocol defects that a results table cannot show. The search loop scored every candidate on the test split and reported the best, making the headline metric a maximum over dozens of noisy estimates while the baselines selected on training data and touched the test set once; and the budget was checked before launching a candidate but never enforced during one, so the system consumed a median of 120 s against a 60-second budget, 2.24x the wall-clock AutoGluon used. Re-running with selection moved to a validation split, the deadline enforced externally and every framework pinned to an equal share of the machine, Orcetra's win rate on the re-run subset falls from 59.4% to 34.3% and no pairwise difference against either competitor remains significant. Recording both estimands inside a single search lets us attribute the collapse: the selection rule accounts for 4.8 percentage points and unequal compute for most of the rest. The same traces give the selection bias as a function of budget, measured rather than assumed: it grows with $K$ but reaches only 0.27 accuracy points, about five times below the $\sigma\sqrt{2\ln K}$ bound a marginal-standard-error argument predicts, because candidates scored on shared test rows cancel most of the noise. We close with a checklist for short-budget comparisons. Code, per-dataset results and the scripts that regenerate every number and figure in the paper are released with it.

---


### 193. [Natural Language Processing Psychometrics](https://arxiv.org/abs/2608.07316)

**<font color=#1a73e8>作者：</font>** Edoardo Sebastiano De Duro, Emma Franchino, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) models predicting mental health outcomes rarely specify what they measure: contextual knowledge, emotional content, or syntactic structure. NLP Psychometrics treats psychological prediction from text as a psychometric problem, linking scores to interpretable linguistic evidence and testing beyond the training text format. Nine LLMs, conditioned on controlled personas (cognitive digital shadows), completed psychometric questionnaires with textual explanations per item. We extracted emotional profiles and syntactic-semantic structure via textual forma mentis networks, combined with personality and sociodemographic variables in ablated random forest (RF) regressors, using SHAP to identify which features drove performance and in which direction. Full RF models explained up to 70.8% of variance in life satisfaction (SWLS), 55.7% in depression (PHQ-9), and, for DASS-21, 68.5% depression, 76.0% anxiety, 72.4% stress. Sociodemographics alone explained no meaningful variance in depression, anxiety, or stress, but did so for life satisfaction, where emotion features and income were the strongest predictors; neuroticism and network topology instead dominated depression and anxiety, reversing direction between them. Without retraining, RF models separated diaries from low- and high-score personas ($r$ up to 0.91) and, using only network/emotion features, classified clinical from control participants in real transcripts with up to 68% accuracy. These results show the promise and limits of synthetic data: LLM personas can expose model biases, recover patterns consistent with clinical rumination, and support psychometric prediction from human text without a matched questionnaire, but cannot substitute for human validation. NLP Psychometrics makes these distinctions explicit, measurable, and testable through interpretable AI and network/emotional features.

---


### 194. [Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU](https://arxiv.org/abs/2608.07323)

**<font color=#1a73e8>作者：</font>** Yuting Ge, Pengju Yang, Mingkai Nie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We test whether decoder-only language-model FFNs require SwiGLU's open positive tail. We introduce MemGLU as a closed-tail comparator derived from a memristive branch geometry. Across paired 9M and 30M pretraining runs with three seeds, MemGLU remains within about 0.1% of SwiGLU in validation NLL. Trained SwiGLU checkpoints are sensitive to positive-tail suppression, while mechanism diagnostics show that the two models use their gates differently despite similar losses. These results suggest that models adapt to the gate geometry available during pretraining. At the tested scales, SwiGLU's open positive tail is not necessary for decoder-only language-model FFNs.

---


### 195. [When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series](https://arxiv.org/abs/2608.07333)

**<font color=#1a73e8>作者：</font>** Chen Shao, Yue Wang, Zhenyi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static graph topology and aggregating information from neighboring series. In this work, we investigate the representa- tional power of GNNs for forecasting under both static and dynamic settings (i.e., when pairwise correlations evolve drastically over time) and identify critical limitations in current architectures. To formalize this, we first propose Temporal Correlation Volatility (TCV), a model- agnostic metric designed to quantify the distributional evolution of these latent structures. We establish a clear connection between TCV and performance degradation, demonstrating that many popular models, including Transformers, generalize poorly in high-TCV settings and are often outperformed by simple structure-agnostic baselines. To address these limitations, we propose Graph Layer for Inference in Dynamic En- vironments (GLIDE), a novel GNN layer enhanced by two theoretically grounded design mechanisms: (D1) Path-based Message Passing, which captures path-based neighborhoods and (D2) Static and Dynamic Propagation Separation, which identifies optimal dynamics via local static approximation. These components significantly improve learning under dynamic topology while preserving robustness in static scenarios. Ex- tensive experiments on synthetic and real-world benchmarks show that GLIDE improves average performance by up to 45.6% across static and dynamic settings, with the largest gain reaching 85.7%. The source code is available at this https URL.

---


### 196. [Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks](https://arxiv.org/abs/2608.07335)

**<font color=#1a73e8>作者：</font>** Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in deep reinforcement learning have increasingly favored simplified, highly parallelized paradigms. Notably, the Parallelized Q-Network (PQN) algorithm achieves stable off-policy learning without relying on computationally expensive replay buffers or target networks. However, the representational capacity and parameter efficiency of visual encoders operating in these buffer-free settings remain underexplored. In this work, we systematically investigate the architectural design space of Convolutional Neural Networks for PQN. We design and rigorously evaluate eight distinct CNN topologies, optimizing for sample efficiency under strict parameter constraints. Furthermore, we study the impact of representation and value estimation enhancements by integrating the Hadamax encoding paradigm and advanced Q-learning extensions, including distributional, ensemble, and dueling heads. Extensive experiments on the Atari-57 benchmark demonstrate that our proposed composite architecture, Aftab, achieves an Interquartile Mean (IQM) Human-Normalized Score of 6.479, establishing a 0.86 Probability of Improvement over the standard PQN baseline. Additionally, structural resilience evaluations on the highly non-stationary Procgen Hard benchmark confirm out-of-distribution generalization, with Aftab yielding an IQM Procgen Normalized Score of 0.418 compared to the baseline's 0.382. Ultimately, this work establishes an efficient, probabilistically superior structural reference for model-free reinforcement learning, all while preserving the simplicity and memory efficiency of unbuffered, parallelized optimization.
The complete Aftab framework, including all model definitions, training configurations, and raw experimental logs, is open-sourced and available on our GitHub repository: this https URL

---


### 197. [H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation](https://arxiv.org/abs/2608.07340)

**<font color=#1a73e8>作者：</font>** Jia Wang, Jiaming Cai, Zunying Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registration-based Few-shot medical image segmentation (RFMIS) aims to generate pseudo-labels for unlabeled images by warping a labeled image through registration. However, existing methods primarily perform pixel-level optimization and inference in Euclidean space, treating anatomical structures as flat and disjoint. This neglect of inherent hierarchies degrades pseudo-label quality and weakens the discrimination of ambiguous regions, limiting the segmentation performance. To overcome this challenge, we propose a Hyperbolic Hierarchy-aware Aggregative Learning framework for RFMIS, termed H2AL, that enhances both deformation plausibility and anatomical discrimination for dual-task learning. Specifically, we introduce a Hyperbolic Hierarchy-aware Infusion (H2I) module, which leverages the hierarchical modeling capability of hyperbolic space to learn precise hierarchy-aware representations via transformation-guided supervised hyperbolic contrastive learning, and injects such hierarchical priors into Euclidean space through a gated infusion block while preserving semantic richness. Furthermore, we propose an end-to-end joint optimization algorithm by gradient aggregation, where the gradients from the registration and segmentation decoders, embedding semantic and hierarchical cues, are aggregated to update the shared encoder to promote collaborative learning across tasks. Extensive experiments on two anatomical regions, with five experimental settings, demonstrate the effectiveness and efficiency of our method in both registration and segmentation. The code is publicly available at this https URL.

---


### 198. [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](https://arxiv.org/abs/2608.07341)

**<font color=#1a73e8>作者：</font>** Ruijie Hou, Yueyang Jiao, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test data from public benchmarks inevitably leaks into pretraining corpora, inflating evaluation scores once memorized. \textbf{Contamination mitigation evaluation} intervenes in the decoding process to suppress memorization and restore a contaminated model's genuine capability, but its prevailing metric, the \textbf{G-AP} (\textbf{G}ap of \textbf{A}ggregate \textbf{P}erformance), is flawed. Discrete correct/incorrect readouts cannot characterize per-question performance, averaging before differencing lets over- and under-suppression cancel out, and uniform per-question weighting invites strategies to push solve probabilities onto the clean model's high-frequency values. We propose \textbf{SA-PPG} (\textbf{S}tratified \textbf{A}ggregate of \textbf{P}er-question \textbf{P}robability \textbf{G}aps): estimate each question's solve probability by sampling, difference it against the clean model per question, and aggregate within groups defined by the clean model's solve probability. Existing mitigation strategies first estimate where contamination lies and then operate on the estimate, so they are only as correct as the estimate. \textbf{RailCap} instead judges contamination during generation: whenever a sample falls back onto the greedy trajectory, the next trajectory token is capped to the runner-up, accumulating suppression until the response distribution becomes sufficiently dispersed. Across multiple contaminated models and benchmarks, SA-PPG reveals that prior strategies' restoration is substantially overestimated, while RailCap attains the lowest SA-PPG.

---


### 199. [Residual Algebra for Representation-Preserving Learning](https://arxiv.org/abs/2608.07349)

**<font color=#1a73e8>作者：</font>** Yao Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from heterogeneous representations is usually reduced to feature concatenation, which erases which representation produced an error. We instead algebraize the residual: a representation is a typed object that owns both a coordinate system and the residual it leaves unresolved, and learning is an ordered composition of operators that preserve or deliberately erase that type. Fold realizes the objects as point-in-time conditional-mean fields on 10x10 rank grids. FPRC-PQ realizes the algebra as relax-aggregate-close: each field is relaxed by a correction fitted to its own residual in its own coordinates; corrected fields meet at a fixed mean that is the sole identity-erasure boundary; and a shared learner closes only the aggregate's fresh residual. The composition telescopes exactly into representation, local residual estimate, and residual-of-residual estimate. Its aggregate is a learned control-variate interface with population variance reduction, while refitting the closer along perturbations of the backbone yields first-order coupled-path mean orthogonality. As an analytical extension, a reflective rumination operator reads the displacement of a global reconstruction from the aggregate anchor, reflects it, and fixes its gain by a unique orthogonal projection rather than return-tuned grid search. On 3.67M Chinese A-share stock-day observations (2023-2026) under a frozen point-in-time protocol, the evaluated base algebra raises net-of-cost return from 13.52% to 19.10% and Sharpe from 1.42 to 2.09. Matched-capacity, unified-residual, identity-free two-stage, and pairwise-only controls all trail it. The gain is therefore not explained by more features or more trees, but by making residual ownership and composition explicit while representation identity is still available.

---


### 200. [QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting](https://arxiv.org/abs/2608.07363)

**<font color=#1a73e8>作者：</font>** Junkai Lin, Siqi Hou, Raymond Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting non-stationary time series remains difficult due to long-range dependencies, local volatility bursts, structural shifts, and nonlinear oscillatory behaviors. Although Transformer-based forecasters are effective for modeling long-term temporal dependencies, their feed-forward blocks typically rely on smooth static activations that are insufficiently sensitive to abrupt regime changes. Motivated by quantitative Transformer designs and oscillator-based nonlinear activations, we propose QFCQT, short for Quantum-Fractal-inspired Chaotically Gated Quantformer, for robust forecasting under complex volatile dynamics. Here, "quantum-fractal-inspired" denotes a computational analogy based on soft oscillator superposition and multi-scale nonlinear responses, rather than a formal quantum-mechanical or fractal-theoretic derivation. QFCQT consists of three main components: (1) a Quantformer-style numerical encoder that directly processes multivariate inputs via linear embedding; (2) a learnable Lee-oscillator activation module that maps scalar pre-activations to dynamic oscillatory responses and summarizes them through Max-over-Time pooling; and (3) a smooth-chaotic gated fusion mechanism that adaptively balances conventional smooth activations and chaos-sensitive responses. Furthermore, instead of using a single fixed oscillator, QFCQT employs a soft superposition of eight parameterized Lee oscillator families to adaptively capture different nonlinear response patterns across regimes. Experiments on ETTh1, ETTh2, and A-share Stock Index benchmarks show that QFCQT consistently outperforms strong baselines, including Informer, LogTrans, LSTMa, HAT, and COTN.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
