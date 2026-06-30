# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 151. [Articulating then Matching: Zero-Shot Shape Matching for Uncurated Data](https://arxiv.org/abs/2606.29167)

**<font color=#1a73e8>作者：</font>** Qilong Liu, Qinfeng Xiao, Chenyuan Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding dense correspondences between 3D shapes is a fundamental yet unresolved challenge, especially in real-world environments. These environments present severe challenges, including the lack of time and sufficient samples for training, the prevalence of uncurated extreme-high resolution data with topological distortions, and the need to handle diverse 3D representations. In this paper, we present ATM, a zero-shot framework that requires no correspondence-specific training and robustly addresses these issues at once through an articulate-then-match paradigm. Rather than relying on intrinsic geometric properties, we leverage powerful pretrained vision foundation models and parametric shape priors to estimate parametric shape models from multi-view renderings, and systematically ground these estimations via multi-view geometric consistency. By mapping diverse inputs into a shared canonical parametric space, we inherently establish robust coarse correspondences that bypass topological noise, which are then refined into precise dense mappings via spectral refinement. Operating purely on test-time optimized parametric reconstructions, ATM requires no correspondence training data, is naturally immune to connectivity artifacts, and seamlessly handles diverse 3D modalities, including meshes, point clouds, and 3D Gaussians. Extensive experiments demonstrate that our method achieves strong results on non-isometric benchmarks (average geodesic errors of 2.4-TOPKIDS, 3.8-SMAL), reducing errors by 73% and 37% respectively compared to the baseline URSSM. Furthermore, it exhibits unprecedented robustness on in-the-wild raw scans of up to 200k vertices per shape while maintaining near-constant computation time and consistent superior accuracy.

---


### 152. [Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies](https://arxiv.org/abs/2606.29171)

**<font color=#1a73e8>作者：</font>** Reza Habibi, Darian Lee, Magy Seif El-Nasr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While existing data attribution methods can identify which training examples build specific mechanistic circuits, they cannot explain how training data shapes the high-level behavioral decisions a model learns to make. To bridge this gap, we introduce Symbolic Mechanistic Data Attribution (SMDA), a framework that attributes training pairs to the interpretable symbolic policies governing model behavior. SMDA fits a closed-form Ridge regression over sparse autoencoder (SAE) features to model a target behavior, then analytically decomposes how each supervised fine-tuning example shifts that policy through feature-activation Delta_X and output-probability Delta_Y pathways. We distill a symbolic policy for refusal behavior in Llama-3.2-3B-Instruct and analyze 200 SFT training pairs. Our analysis reveals that (1) the symbolic policy's coefficients expose systematic gaps in the base model's safety behavior for categories like religious stereotyping; (2) per-feature Delta_X/Delta_Y decomposition can mechanistically explain why harmful and harmless pairs exert qualitatively different influences on certain features; and (3) individual training pairs routinely exhibit cross-feature interference, allowing SMDA to identify training pairs whose dominant effect falls on unintended features. These results demonstrate that combining mechanistic interpretability with data attribution yields a diagnostic tool that is both more fine-grained than black-box influence functions and more scalable than manual circuit analysis.

---


### 153. [Direct Causation in International Humanitarian Law and the Challenge of AI-Mediated Civilian Cyber Operations](https://arxiv.org/abs/2606.29175)

**<font color=#1a73e8>作者：</font>** Alice Saito, Harold Godsoe, Phan Xuan Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> International humanitarian law protects civilians from direct attack unless and for such time as they take direct part in hostilities, with the ICRC's 2009 Interpretive Guidance operationalising this rule through a three-criterion cumulative test. This paper argues that AI-mediated civilian cyber operations challenge the direct causation element of this test in a structurally specific way: when a civilian deploys an autonomous multi-agent cyber system of the kind recently demonstrated in offensive AI research, the "one causal step" standard fails because harm is produced by system-generated decisions made after human disengagement, and the integral-part requirement does not extend because it presupposes downstream human contributors whose conduct can be independently classified. The framework therefore defaults to treating such deployments as indirect participation, in tension with its purpose of capturing civilians who personally take part in hostilities. Beyond the doctrinal analysis, this paper identifies goal-specification granularity as the property on which the integral-part test's concreteness component implicitly turns, classifies AI-mediated operations along a five-level spectrum, and argues that existing technical AI governance instruments do not log or report this property.

---


### 154. [Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks](https://arxiv.org/abs/2606.29176)

**<font color=#1a73e8>作者：</font>** Tejas Pradeep Shirodkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A deep network's loss is invariant to continuous symmetries of its parameters: the logit shift, the ReLU rescaling, the LayerNorm scale, the per-head attention rotation. Adam's per-coordinate preconditioner drifts along each symmetry orbit, which pulls the trajectory off the symmetry quotient where the optimization lives and blurs the singular-learning rate the quotient makes readable. We build DDC, a Dead-Direction Conditioner that lifts a base optimizer into a $G$-equivariant one: it conditions the optimizer's state in the orbit decomposition of a $G$-invariant metric, so the trajectory stays a preconditioned gradient flow on the quotient $\bar\Theta = \Theta/G$. The construction carries four architectural gauges (cross-entropy shift, ReLU and SwiGLU rescaling, LayerNorm and RMSNorm scale, and a per-head $O(d_{\rm head})$ attention rotation matched to RoPE), proves exactly equivariant on an Adam base, and composes with a Muon base through a gauge-equivariant orthogonaliser. Respecting the symmetry changes both the minimum the optimizer reaches and what it leaves measurable there. On a language model trained past the point of fit, DDCAdam resists the over-training collapse AdamW falls into, holding a validation-train loss gap of 0.67 against 5.88, and reads the dead-direction rate in 32 of 65 layer-by-observable cells where AdamW reads it in 7. A vision transformer trained from scratch reaches lower validation loss (1.71 against 2.12) while compressing spare feed-forward capacity a matched AdamW leaves intact. On a Muon base, where the rotation gauge composes exactly, DDCMuon groks ten of eleven seeds at depth 24 that a plain Muon never reaches. Built into the optimizer, a network's gauge symmetry sharpens the minimum it finds and turns that minimum's geometry into something the trajectory can measure.

---


### 155. [Measuring Graph-to-Graph Semantic Similarity in Knowledge Graphs: An Empirical Evaluation of Knowledge Graph Embeddings](https://arxiv.org/abs/2606.29180)

**<font color=#1a73e8>作者：</font>** Seungryeol Baek, Wooseok Sim, Hogun Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A Knowledge Graph (KG) represents facts as structured triples and is widely used to organize relational knowledge across diverse domains. Just as textual information ranges from words and sentences to complete documents, KG information can be interpreted at multiple levels, from entities, relations, and triples to subgraphs and entire KGs. However, existing KG embedding methods mainly focus on entities, relations, and triples, leaving graph-level semantics largely unaddressed. Conventional graph-level methods, which typically compare graphs based on structural patterns, are also insufficient because structural similarity alone cannot guarantee semantic similarity between KGs. To evaluate how well different methods capture such graph-level semantic information, we study graph-to-graph semantic similarity, which determines whether a pair of KGs represents semantically corresponding underlying information. To obtain reliable ground-truth correspondences, we construct a semantic matching dataset by modifying text documents, extracting KGs from both original and modified documents, and transferring their known correspondences to KG pairs. We compare text-based, structure-based, and KG embedding-based approaches on each dataset. For the KG embedding-based approach, we introduce two scoring functions: \textit{EmbPairSim}, which uses maximal pairwise entity similarity, and \textit{AvgEmbSim}, which uses a frequency-weighted centroid. Experiments on WikiText-2 and CC-News show that \textit{EmbPairSim} achieves up to 5.3 pp higher MRR than Sentence-BERT while using substantially fewer parameters. These results suggest that KGE representations can serve as compact and effective signals for graph-to-graph semantic similarity in KGs. Our code is available at this https URL.

---


### 156. [Anomaly Factory 3D: A Modular Framework for Diverse Pseudo-Anomaly Synthesis in Unsupervised 3D Anomaly Detection](https://arxiv.org/abs/2606.29181)

**<font color=#1a73e8>作者：</font>** Ali Balapour, Faraz Hach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting and localizing defects in 3D point clouds is challenging because abnormal samples are scarce and diverse, while training is often limited to normal data. We propose Anomaly Factory 3D (AF3AD), a modular framework that synthesizes diverse pseudo-anomalies from normal point clouds to expand the training data for unsupervised 3D anomaly detection methods that rely on pseudo-anomalies. AF3AD uses a center-conditioned parametric deformation model defined in local PCA frames, with kernel-controlled spatial falloff, anisotropy, directional gating, and normal/tangential displacement fields, enabling a broad set of geometric defect presets. We demonstrate its ease-of-use and effectiveness by integrating AF3AD with an offset-prediction detector and a reconstruction-based anomaly detection method, showing that AF3AD transfers across detection paradigms. Experiments on AnomalyShapeNet and Real3D-AD show consistent improvements in object- and point-level detection and localization, supported by ablations on preset groups and robustness under noise. AF3AD is designed as a standalone synthesis tool to facilitate adoption across different 3D anomaly detection paradigms. Code is available at this http URL.

---


### 157. [AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution](https://arxiv.org/abs/2606.29194)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Siyuan Liu, Bingjun Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated alpha mining holds the scoring function fixed and varies the search algorithm over it. A search that converges against a fixed scorer overfits whatever the scorer cannot penalize, a primary cause of the out-of-sample generalization gap. We treat the scoring function as a search artifact alongside the alpha factors and study what conditions make this joint search admissible. Sealed Joint Search (SJS) is a framework: a set of structural conditions on information flow in an autonomous-discovery system that prevent joint search from collapsing into self-confirmation while keeping the evaluator sealed. Conditions cover role decomposition, typed inter-role communication, provenance-sealed reads, versioned stores, and substrate-local promotion. Agora tests SJS empirically: five LLM agent classes communicate via three channels, evolving eight skill libraries, with alpha libraries built on AlphaGen operators. Three evaluators write reports aggregated into one brief, carrying forward disagreement instead of voting. We run Agora for 100 rounds on CSI 1000 and evaluate on a 91-day 2026 holdout sealed from all LLM inputs. Agora achieves holdout Sharpe +1.87; best baseline +1.334 at favorable seed and -0.755 cross-seed mean. Pre-loading Agora's two metrics into a frozen-library ablation recovers only +0.40 of the +2.25 Sharpe gap, and adding PPO without library evolution worsens the gap. The two metrics emerge rather than being designed. Caveats: single-seed run, short-side concentrated signal, intended for long-short.

---


### 158. [DTI: Dynamic Trajectory Initialization for Generative Face Video Super-Resolution](https://arxiv.org/abs/2606.29198)

**<font color=#1a73e8>作者：</font>** Yingwei Tang, Chen Yan, Wendi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As the most perceptually powerful Face Video Super-Resolution (FVSR) method, existing works in Generative FVSR (GFVSR) mainly exploit the generative prior of pretrained diffusion models. However, viewed as full generation, they suffer from fixed sampling and expensive inference costs if without large-scale auxiliary training. Furthermore, an excessive pursuit of generic perceptual metrics often results in low fidelity. To address these issues, we present Dynamic Trajectory Initialization (DTI) paradigm for GFVSR, which reformulates GFVSR as an input-driven directional restoration. With a novel enhancement-and-injection conditioning mechanism for pretrained DiT backbone, fidelity of our model has been significantly improved without compromising perceptual quality. To dynamically set the starting sampling point, we propose a Discriminative Guide (DG) trained via objective Signal-to-Noise Ratio (SNR) alignment. With only minor model adaptation and fine-tuning, our method achieves a SOTA overall performance across diverse metrics and benchmarks. An analysis of relationship between actual comprehensive quality and common metrics is also conducted, which demonstrates the perception-distortion trade-off and that the LPIPS is the most convincing metric in our case.

---


### 159. [BrainRiem: Riemannian Prototype Learning for Source-Free Cross-Site Brain Network Diagnosis](https://arxiv.org/abs/2606.29200)

**<font color=#1a73e8>作者：</font>** Kunyu Zhang, Tianxiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-site functional MRI (fMRI) studies are essential for robust neuropsychiatric diagnosis yet suffer severe domain shifts from scanner heterogeneity, demographics, and site-specific acquisition protocols. Traditional domain adaptation requires concurrent source and target data access, violating clinical privacy regulations. Moreover, functional connectivity matrices lie on the Symmetric Positive Definite (SPD) manifold, where Euclidean operations cause geometric distortions corrupting diagnostic patterns. We propose BrainRiem, a source-free domain adaptation framework learning compact Riemannian brain prototypes via manifold-aware bi-level optimization. It employs the Log-Euclidean Metric to ensure prototypes remain valid SPD matrices, while Dirichlet Energy spectral calibration aligns their frequency characteristics with real brain networks. Only anonymized prototypes are transmitted to target sites, serving as stable anchors for training local models without source data access and reducing leakage under the evaluated attacks. Comprehensive experiments on ABIDE and REST-meta-MDD show BrainRiem consistently outperforms state-of-the-art source-free, traditional, and graph domain adaptation methods across diverse scanners and demographics. Notably, learned prototypes exhibit biologically interpretable connectivity patterns aligning with established neuroscience findings, validating the necessity of Riemannian geometry for brain network analysis.

---


### 160. [Bayesian Best-Arm Identification with Abstention: A Polynomial-to-Exponential Phase Transition](https://arxiv.org/abs/2606.29203)

**<font color=#1a73e8>作者：</font>** Yuqi Huang, Yunlong Hou, Vincent Y. F. Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the Bayesian fixed-budget best-arm identification problem in which a learner can abstain from making a terminal recommendation. Subject to an abstention budget $\alpha$, we analyze the probability of undetected error--the risk of recommending a suboptimal arm without abstaining. Our central finding is that abstention induces a phase transition: without abstention, the error probability decays polynomially in the sampling budget $T$; in contrast, introducing any small positive abstention budget shifts this to an exponential decay. For Gaussian priors and rewards, in the regime $T\to\infty$ followed by $\alpha\downarrow0$, we establish exact matching information-theoretic lower bounds and algorithmic upper bounds on the optimal error exponent, which takes the form $\exp(-\frac{\alpha^{2}T}{8\kappa_{\nu}^{2}})$. The hardness parameter $\kappa_{\nu}$ represents the prior density of the top-two gap at zero, highlighting that nearly tied instances drive the fundamental error. We introduce an adaptive algorithm, PGWS, that successfully achieves this optimal exponent by expending its abstention budget on statistically ambiguous instances. We further demonstrate that this polynomial-to-exponential improvement is exclusively a Bayesian phenomenon--in the frequentist setting, abstention only affects lower-order exponent terms. We also extend our results beyond the Gaussian model.

---


### 161. [Zero-Gated Language-conditioned Human Motion Prediction](https://arxiv.org/abs/2606.29208)

**<font color=#1a73e8>作者：</font>** Guanhui Qiao, Lu Zhou, Ding Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose histories provide the core kinematic evidence for 3D human motion prediction, but they lack explicit high-level semantic guidance. This paper introduces ZGL, a lightweight language-conditioned predictor that uses captions of the observed motion as a semantic prior while preserving a strong motion backbone as the main source of dynamics. We render only the observed poses, generate a one-sentence description with a vision-language model, encode the caption with a frozen CLIP-L text tower, and project it into a small set of conditioning tokens. These tokens are injected into a DCT-based spatial-temporal Transformer by compact crossattention adapters with zero gates: each adapter output is multiplied by a learnable gate initialized to zero, so the full network is numerically identical to the pose-only baseline at initialization and can learn to use language only when it reduces prediction error. On Human3.6M, ZGL improves overall MPJPE over representative motion-prediction baselines in our comparison. Results on CMUMocap further show that compact caption conditioning transfers to a second benchmark and provides a practical semantic cue for 3D human motion prediction.

---


### 162. [A Cognition-Emotion-Personality Framework for Modeling Human-Like Awareness and Behavior in Emergency Evacuations](https://arxiv.org/abs/2606.29212)

**<font color=#1a73e8>作者：</font>** Zoi Lygizou, Michalis Zervas, Helena G. Theodoropoulou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-based evacuation simulations are widely used to study crowd behavior during emergencies, but many models rely on assumptions such as perfect event awareness, complete exit knowledge, and fully rational decision-making. This paper presents an extended evacuation framework that integrates cognitive, emotional, social, and personality-related mechanisms into a unified model of human behavior under uncertainty. The framework incorporates a dynamic event-awareness mechanism based on a continuous Event Certainty Level, a memory-based representation of exit knowledge subject to acquisition, forgetting, and recall, a continuous fear model in which panic emerges as a high-intensity state, and an OCEAN-based personality representation. Neuroticism is explicitly integrated into the emotional model, influencing fear generation, escalation, social contagion, and recovery. Behavioral heterogeneity is further captured through individualized decision thresholds that affect responses to perceived risk. The framework is evaluated through simulation experiments examining the effects of spatial familiarity, memory robustness, decision sensitivity, emotional dynamics, and personality variation. Results show that cognitive, emotional, and personality-driven processes substantially influence evacuation dynamics, reducing evacuation efficiency and generating realistic crowd phenomena such as delays, confusion, injuries, and socially influenced behaviors. The proposed framework provides a more realistic representation of human behavior in emergency evacuations and supports systematic investigation of the interactions between cognition, emotion, personality, and crowd dynamics.

---


### 163. [A Linear Matching Bandit Approach to Online Multi-Human Multi-Robot Teaming](https://arxiv.org/abs/2606.29221)

**<font color=#1a73e8>作者：</font>** Yaohui Guo, X. Jessie Yang, Cong Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of online multi-human multi-robot teaming through the lens of a linear matching bandit framework, where a learner assigns robots with unknown features from a fixed pool to distinct sets of human agents over multiple rounds. To solve this problem, we propose LinMatch, an online learning algorithm that updates the confidence intervals of the unknown features and makes the optimistic matching under uncertainty. The contributions and novelty of this work are twofold. First, we recast the optimistic matching problem in each round as a linear program of maximum weighted matching, efficiently solvable by the celebrated Hungarian algorithm. Second, we provide novel bounds for matching with linear feature problems, showing an upper bound of $\tilde{O}(d\sqrt{MKT})$ and a minimax lower bound of $\Omega(d\sqrt{MKT})$, establishing a tight optimal regret rate of $\tilde{\Theta}(d\sqrt{MKT})$. This demonstrates that LinMatch achieves strictly optimal achievable regret with respect to the total number of rounds $T$, the feature dimension $d$, and the matching parameters $M$ and $K$. The proposed algorithm and bounds apply to a wide range of matching problems with applications beyond human-robot matching, such as housing allocation, recommendation systems, and more.

---


### 164. [Again-Pose: Anchor-Guided Adaptive Inter-Frame Motion Cues Propagating for High-quality Human Pose Reconstruction](https://arxiv.org/abs/2606.29230)

**<font color=#1a73e8>作者：</font>** Shuaikang Zhu, Yiding Sun, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous 3D human poses from unconstrained videos is challenging, especially in extreme motion scenarios involving severe motion blur and occlusion. Current state-of-the-art methods typically rely on implicit temporal attention to aggregate features across frames. However, under severe visual degradation, input features often suffer from collapse, rendering them indistinguishable from noise. In such cases, implicit aggregation fails to distinguish valid signals, leading to catastrophic reconstruction errors. To address this robustness gap, we propose a simple yet effective framework called Anchor-guided adaptive inter-frame motion cues propagating (Again-Pose), reformulating pose estimation in degraded frames as a motion-guided recovery task. Instead of blindly smoothing features, we explicitly identify high-quality Anchor Frames based on feature saliency and propagate reliable kinematic cues to "inpaint" the poses of degraded intermediate frames. Specifically, a Dual-path Motion-aware Module captures fine-grained inter-frame dynamics, while a Difference-weighted Fusion Module adaptively propagates these cues to suppress drift. Extensive experiments on standard benchmarks (Human3.6M, 3DPW, PoseTrack) and the challenging FineDiving dataset demonstrate that Again-Pose significantly outperforms state-of-the-art methods in robustness and stability, effectively recovering plausible poses where other methods fail.

---


### 165. [On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse](https://arxiv.org/abs/2606.29238)

**<font color=#1a73e8>作者：</font>** Amritansh Mishra, Supriyo Chakraborty, Berkcan Kapusuzoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) eliminates the learned critic in PPO by using the mean reward of grouped rollouts as a baseline. We provide a rigorous derivation of GRPO from first principles of the policy gradient theorem, revealing a fundamental credit assignment failure: under output-only reward, every token in a rollout receives identical advantage, collapsing token-level credit to a single scalar. We prove this induces gradient sparsity that intensifies over training, and demonstrate empirically via SVD analysis of GRPO gradients on Nemotron-4B/GSM8K that the gradient matrix has effective rank $\approx$ 2 regardless of group size $R \in \{2, 4, 8\}$. We formalize this as an intrinsic rank-2 structure arising from the zero-sum constraint on advantages and derive conditions under which GRPO's baseline is optimal. Our results characterize when GRPO's simplicity is theoretically justified and identify the credit assignment bottleneck as the key limitation for multi-step reasoning.

---


### 166. [Blackknife: Hard-Label Query-Limited Black-Box Attacks on Heterogeneous Graph Neural Networks](https://arxiv.org/abs/2606.29240)

**<font color=#1a73e8>作者：</font>** Honglin Gao, Junhao Ren, Lan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous graph neural networks (HGNNs) have achieved strong performance in modeling complex graph-structured data with multiple node and relation types. However, their robustness under realistic black-box adversarial settings remains insufficiently explored. Existing attacks on HGNNs usually assume access to model gradients, soft prediction scores, or the complete graph structure, which is often unavailable when HGNN-based services are deployed as closed systems. In this paper, we propose Blackknife, a hard-label, query-limited, and structure-limited black-box evasion attack framework for heterogeneous graph neural networks. Blackknife assumes no access to the victim model architecture, parameters, gradients, logits, confidence scores, or the full graph structure. Instead, it only relies on locally observable one-hop heterogeneous structures and a small number of hard-label queries. To generate effective perturbations under these strict constraints, Blackknife first constructs a local relation-aware surrogate model from observable heterogeneous neighborhoods. It then relaxes discrete edge addition and deletion operations into continuous soft weights and optimizes them through projected gradient descent. Finally, the optimized perturbations are discretized into relation-preserving structural rewiring operations and verified using limited hard-label feedback from the victim model. Extensive experiments on three benchmark heterogeneous graph datasets, including ACM, DBLP, and IMDB, demonstrate that Blackknife consistently achieves strong attack success rates against representative HGNN models. The results further show that Blackknife remains effective under topology-based defense strategies, revealing the vulnerability of HGNNs to local structure-limited black-box attacks.

---


### 167. [KrishokChat: A Citation-Grounded Dataset and Benchmark for Bengali Agricultural Advisory](https://arxiv.org/abs/2606.29243)

**<font color=#1a73e8>作者：</font>** Khan Raiyan Ibne Reza, Omar Ibne Shahid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present KrishokChat, the first citation-grounded Bengali agricultural instruction-tuning dataset for crop advisory in low-resource settings. We establish a foundation of 290 hierarchical Knowledge Nodes, extracting disease symptoms, management practices, chemical dosages, and verbatim citations from 129 domain-filtered agricultural manuals. Every training instance inherits a verified citation header, guaranteeing 100% citation provenance. Using a Partitioned Seed Generation Matrix, these nodes are expanded into 139,200 supervised fine-tuning pairs, and augmented with 5,300 chemical safety and 1,000 adversarial safety instances, yielding 145,500 QA pairs across 18 crop categories. To evaluate real-world performance, we introduce the Farmer Benchmark, comprising 1,001 authentic farmer queries curated from field surveys and digital portals. Empirical evaluation on Gemma-4-E2B reveals that while fine-tuning on KrishokChat vastly improves structured formatting, standalone models still struggle with exact chemical dosage generalization. This highlights the dataset's true value as a verified knowledge base for retrieval-augmented generation (RAG) rather than mere parametric memorization. All data, code, and benchmarks are released under CC-BY-4.0.

---


### 168. [SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics](https://arxiv.org/abs/2606.29247)

**<font color=#1a73e8>作者：</font>** Jiashuo Sun, Yue He, Wenxuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models represent a promising direction for embodied intelligence in surgical robotics. Despite the prevalence of VLA benchmarks for general robotics, standardized evaluation platforms specifically designed for surgical contexts remain absent. To address this limitation, we present SurgVLA-Bench, the first comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics. Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy ranging from atomic actions to complete surgical procedures, complemented by a multi-dimensional evaluation framework assessing action accuracy and semantic consistency. We then systematically evaluate two representative paradigms, including autoregressive models such as OpenVLA, and flow matching models such as $\pi_{0}$, $\pi_{0.5}$, and SmolVLA. Our experiments show that autoregressive models tend to excel in semantic understanding, while flow matching models often achieve higher task precision but may face generalization trade-offs. However, even the best-performing models remain far from satisfactory, as the constrained endoscopic field of view, restricted viewing angles, and frequent occlusions persist as fundamental physical bottlenecks. The code and data are available at this https URL

---


### 169. [When Prices Double in a Week: Forecasting of Agricultural Volatility in Import-Isolated Markets](https://arxiv.org/abs/2606.29248)

**<font color=#1a73e8>作者：</font>** Ranuga Weerasekara, Heshan Nethmina, Manuja Ranathunga 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vegetable prices in Sri Lanka are highly volatile because the market is largely import-isolated, so supply disruptions quickly drive prices up. This study develops a machine learning framework to forecast such volatility by incorporating supply-chain-aware features and explicitly modelling the country's two cultivation seasons, Maha (October-April) and Yala (May-September). An integrated dataset was constructed by combining retail and farmer-gate prices with origin-aligned weather variables, diesel costs, and exchange rates across 12 vegetable varieties and 14 market centres from 2013 to 2019. A gradient-boosted ensemble model (XGBoost and LightGBM) was trained and optimised using Optuna, and unified and season-specific configurations were compared. Results show that season-specific models improve within-season fit, with the Yala-specific model achieving the highest R2 of 0.9420 (95% CI [0.690, 1.000]), while the unified model delivers the best overall predictive accuracy of 90.84% (95% CI [88.34%, 91.52%]) and an R2 of 0.9281 (95% CI [0.760, 1.000]). Notably, the unified model maintains 85.96% accuracy on a completely unseen 2024 hyperinflationary period without retraining, successfully tracking major price surges. These findings suggest that agricultural price movements in import-constrained markets are meaningfully predictable when models capture supply-chain dynamics, offering practical value for early warning and decision making by farmers, traders, and policymakers. Existing studies on Sri Lankan vegetable prices are confined to Autoregressive Integrated Moving Average (ARIMA) and Generalized Autoregressive Conditional Heteroskedasticity (GARCH) applied to single markets, with no supply-chain features, seasonal segmentation, or cross-regime validation.

---


### 170. [Learning to Bid in Discriminatory Auctions with Budget Constraints](https://arxiv.org/abs/2606.29252)

**<font color=#1a73e8>作者：</font>** Negin Golrezaei, Sourav Sahoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study repeated bidding in multi-unit discriminatory (pay-as-bid) auctions for a single bidder with per-round utility equal to value minus $\alpha$ times payment, where $\alpha\in[0,1]$ is a cost-of-capital parameter. The bidder aims to maximize cumulative utility over $T$ rounds subject to a total budget $B$. The problem is challenging even without budgets: the action space is exponential in $M$, the maximum demand of the bidder and the valuation vector (context) varies over time. Exploiting a decomposition of utility across units, we develop polynomial-time learning algorithms based on shortest paths in a directed acyclic graph, obtaining sublinear regret under both full-information and bandit feedback. In the bandit setting, the regret is independent of the number of contexts due to complete cross-learning: observing the utility of the chosen action under the realized context reveals the utility for the same action under all counterfactual contexts. With budget constraints, when the average normalized per-round budget $\rho=\frac{B}{MT}<1$, we design a coupled primal-dual algorithm in which the DAG-based procedure uses dual-adjusted edge weights for primal updates, while online gradient descent updates the dual variable, yielding $\rho$-approximate sublinear regret. Finally, we give implementations whose per-round time and space are independent of the number of contexts, enabling scalability to large or even infinite context spaces.

---


### 171. [Confidence-feedback-weighted graph matching network: online-offline laser-induced damage site matching under complex interference](https://arxiv.org/abs/2606.29255)

**<font color=#1a73e8>作者：</font>** Yueyue Han, Guanhua Chen, Hangcheng Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online inspection images of final optics in high-power laser facilities contain pseudo-damage sites that closely resemble true damage sites. Determining the authenticity of online-detected sites is therefore difficult and requires accurate matching to offline ground-truth sites. However, this matching remains highly challenging due to limited match-discriminative features, local geometric distortions, and numerous distractor sites. Existing matching models mainly suppress distractors implicitly through loss-function supervision. We propose a confidence-feedback-weighted graph matching network that requires only damage-site centroid coordinates as input. It estimates node matchability confidence from each round of matching scores and feeds it back as a reliability weight to guide subsequent edge-feature aggregation, thereby suppressing distractor propagation and enhancing cross-graph discriminability. Within this framework, a geometric consistency constraint calibrates spurious high-confidence matchability estimates, while a hard-example mining loss improves discrimination between structurally similar sites. Experiments on our Complex-Scene dataset show that the proposed method achieves a matching F1-score of 96.36$\%$ with robust and efficient performance.

---


### 172. [Nonlinear mixture model motivated subspace clustering](https://arxiv.org/abs/2606.29261)

**<font color=#1a73e8>作者：</font>** Ivica Kopriva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We derive the linear union-of-subspaces (UoS) model for subspace clustering (SC) from the nonlinear mixture model (NMM) used in blind source separation (BSS) to represent a D-dimensional observation vector as an unknown multivariate nonlinear mapping of C latent variables. Assuming the mapping is differentiable up to an unknown order K, we approximate NMM by a K-th order Taylor expansion, yielding a model equivalent to the linear UoS framework underlying SC. This establishes that: (i) the smoothness order K corresponds to the unknown subspace dimension d; (ii) KC equals the number of anchors; and (iii) the sparsity of the representation vector equals K (i.e., d). These relationships enable estimation of bounds on subspace dimension, and that is validated on six benchmark datasets using five established SC algorithms. Established theoretical results are important for post-processing of self-representation matrices estimated by SC algorithms.

---


### 173. [PCGD: Physics-Guided Conditional Graph Diffusion for TCAD Device Simulation](https://arxiv.org/abs/2606.29272)

**<font color=#1a73e8>作者：</font>** Yihan Zhang, Zhiteng Zhang, Kun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Technology computer-aided design (TCAD) semiconductor device simulation is fundamentally constrained by the high computational cost of iteratively solving coupled drift-diffusion equations. Existing ML surrogates either reduce internal physics to macroscopic scalar regressions, or rely on single-step mappings that lack the iterative refinement required to resolve stiff, coupled fields. To address this, we introduce PCGD, a Physics-Guided Conditional Graph Diffusion framework operating natively on unstructured TCAD meshes to predict coupled electrostatic and carrier density fields. PCGD employs a Condition-Aware MeshGraphNet denoiser that explicitly injects boundary conditions and device structure context via global cross-attention. By augmenting data-driven denoising with a physics-guided hybrid objective that integrates exponent-free quasi-Fermi gradient matching with noise-aware PDE residuals, PCGD progressively enforce physical constraints in the iterative diffusion trajectory. This strategy successfully bypasses the numerical instabilities typical of stiff drift-diffusion equations. Evaluated on a challenging mixed PN/MOS benchmark, PCGD significantly outperforms deterministic one-step regression (1.207% error) and local diffusion (1.585% error) baselines by achieving a sub-percent mean relative field error of 0.835%, while concurrently reducing maximum PDE residual errors by nearly three orders of magnitude compared to pure diffusion. It also transfers robustly to unseen SOI topologies (0.815% error) via LoRA adaptation, using 5.30$\times$ less data and 14.34$\times$ fewer parameters than full fine-tuning. Ultimately, PCGD bridges the computational efficiency of generative surrogates with the rigorous physical fidelity of traditional TCAD, unlocking highly scalable, field-level analysis for robust device engineering.

---


### 174. [The Complexity Ceiling Benchmark: A Multi-Domain Evaluation of Sequential Reasoning Under Depth Scaling](https://arxiv.org/abs/2606.29278)

**<font color=#1a73e8>作者：</font>** Shubh Chapra, Dhruv Kumar, Murari Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Complexity Ceiling Benchmark (CCB), a controlled evaluation of how language-model reasoning decays as the number of required sequential steps grows. CCB fixes the semantic content of a task and varies only its depth N in {5,...,50} across three structurally distinct regimes: grounded spatial state-tracking, abstract symbolic pointer manipulation, and transitive relational inference. Across 6,000 trials over five frontier and open-weight LLMs we find a consistent pattern of geometric per-step decay with widely separated domain ceilings: on the first two regimes the strongest models retain pd>0.92 across N=50; on the third every model collapses by N=5, with the best model's 50%-success horizon at H0.5~4.7 steps despite pd=0.863. A trace-level metric (TFBC) shows that 14.5% of correct answers across the benchmark are reached via incorrect intermediate reasoning. Forced verbose state-tracking does not move the ceiling (McNemar p=1.000), and the mean step at which reasoning first diverges, k*, predicts within-domain accuracy better than parameter count. CCB and the geometric decay model together reduce a model's long-horizon reasoning profile to one interpretable number per task family.

---


### 175. [Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts](https://arxiv.org/abs/2606.29279)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents carry conclusions across steps and sessions in compressed memory, and memory products (e.g., mem0, LangMem) rewrite conversation into stored "facts" that later steps trust. We show this rewriting manufactures confidence: across our constructed agent settings, a casual, hedged remark becomes a confident, dated assertion the agent then obeys like a verified fact, granting every above-clearance request it faces. No attacker is needed: a role that was true once and never corrected is stored as a flat fact and acted on like a deliberate injection. We then isolate what the agent responds to. It is not the source: attributed, unattributed, and even forged "system of record" claims all grant alike. It is the confidence of the phrasing. A hedge is discounted, a flat assertion is obeyed, and this holds with no special keyword. Not all hedges are equal, though: the evidential register is the least-discounted, with "reportedly" obeyed like a flat assertion on most models. The obvious fixes fail. A passive "unverified" tag is ignored, and an active "do not trust this" instruction escalates even correct memory, so it is safe only by refusing to decide. The real fix lives in the store: keep the tentative phrasing rather than upgrade it. But that is hygiene, not a defense against an attacker who can simply write a confident lie. The deployable lesson is narrower and constructive: a single load-bearing memory is the hazard, and one redundant source restores correct decisions. We release the harness and demonstrations.

---


### 176. [ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation](https://arxiv.org/abs/2606.29282)

**<font color=#1a73e8>作者：</font>** Cong Wang, Haiyu Wu, Zhiwei Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to prevent image generative models from producing unsafe content while preserving their general generative capability. Meanwhile, next-scale autoregressive (AR) image generation has recently emerged as a new generative paradigm characterized by next-scale prediction, for which concept erasure remains largely unexplored. In this paradigm, semantic information is highly compressed at early scales, leading to severe entanglement between unsafe and unrelated semantics. In this paper, we propose ScaleErasure, an inference-time concept erasure method that performs minimal intervention. ScaleErasure precisely selects and guides predicted logits that are most relevant to the unsafe concept, thereby enabling effective erasure under severe semantic entanglement. Specifically, ScaleErasure performs two additional forward passes conditioned on the unsafe concept and the corresponding safe concept, and leverages their outputs to guide the target logits away from unsafe concepts toward safe concepts. To enable precise and minimal intervention, logits selection and guidance are conducted across three dimensions: scales, tokens, and bit channels. Experiments demonstrate that ScaleErasure outperforms adapted baselines in the next-scale AR paradigm, achieving more precise concept erasure while largely preserving general generative capability. The code is available at this https URL.

---


### 177. [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)

**<font color=#1a73e8>作者：</font>** Dingyi Yao, Xinqi Zhang, Lihui Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data mitigates the data scarcity problem in autonomous driving perception. However, the synthetic-to-real gap leads to performance degradation, hindering real-world model generalization. Although current methods leverage diffusion models for photorealistic style transfer to bridge this gap, they critically ignore a practical asymmetry: while synthetic data possesses perfect pixel-level annotations, real-world style reference images generally lack corresponding labels. Consequently, existing methods relying on symmetric semantic guidance suffer from either prohibitive annotation costs or severe semantic misalignment. To address this dilemma, we formally propose a novel task: Asymmetric Style Transfer for Autonomous Driving (ASTAD), which requires semantically consistent transfer using only labeled synthetic content and unlabeled real-world references. We further introduce the ASTModel, a training-free two-stage framework designed to bridge this domain gap under asymmetric constraints. ASTModel first extracts a coarse semantic prior from the unlabeled target, followed by dynamic prior refinement and class-consistent style injection during the denoising process. Extensive experiments demonstrate that ASTModel significantly outperforms existing methods in downstream perception utility and structural fidelity, while offering a 3.2$\times$ inference speedup. This work aligns synthetic-to-real adaptation with practical constraints, holding the potential to accelerate the scalable deployment of robust autonomous driving systems. Code: this https URL.

---


### 178. [Pointer-CAD v2: Plan-Then-Construct CAD Generation with Dimension-Aware Parametric Precision](https://arxiv.org/abs/2606.29301)

**<font color=#1a73e8>作者：</font>** Dacheng Qi, Chenyu Wang, Jingwei Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-aided design (CAD) plays a fundamental role in modern manufacturing by providing the high precision required for industrial production. Recent large language model based approaches formulate CAD generation as a sequence prediction problem and have achieved promising results. However, existing methods and evaluation protocols primarily emphasize visual similarity, while overlooking precise geometric parameters and correct metric scale. Small numerical deviations that are negligible at the shape-level may still violate industrial tolerance requirements, a problem further compounded by current autoregressive paradigms that utilize command sequence representations, aggressively quantize numerical parameters to ease LLM prediction. In this work, we present Pointer-CAD v2. Compared with v1 (arXiv:2603.04337), this version directly predicts continuous values, bypassing the need for quantized numerical parameters and thereby eliminating quantization errors. Specifically, we propose a unified framework that decouples parameter reasoning from geometric construction through a Plan-Then-Construct paradigm. Our method first produces a structured design plan with explicit metric scale parameters. These parameters are organized into a dictionary and directly referenced during sequence generation via a pointer mechanism, eliminating discretization errors and ensuring dimensionally consistent execution. In addition, we construct a new large-scale dataset with plan-level annotation and introduce three hierarchical geometry accuracy metrics to evaluate parametric fidelity at the vertex, edge, and face levels. Extensive experiments demonstrate that Pointer-CAD v2 consistently outperforms existing baselines and achieves substantial improvements in geometric accuracy, enabling reliable CAD generation for precision-critical engineering applications.

---


### 179. [Occlusion-Robust Multi-Object Decoupling for Physics-Based Interaction](https://arxiv.org/abs/2606.29303)

**<font color=#1a73e8>作者：</font>** Xin Dong, Wenfeng Deng, Yansong Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a mask-free method for lossless multi-object 3D reconstruction from sparse and occluded real-world views, enabling physically plausible interaction via Material Point Method (MPM) simulation. Our key insight is that object coupling stems from occlusion and limited viewpoints, which we address by formulating multi-object decoupling as a sparse-view reconstruction problem. Using 3D Gaussian Splatting as base representation, we first obtain coarse instance partitions with a SAM2-trained segmentation field. Rather than relying on masks, we reconstruct fragmented geometries by leveraging a joint Score Distillation Sampling (SDS) process, which integrates reference-view supervision with novel-view synthesis guided by 2D and 3D diffusion priors to enforce both texture fidelity and 3D consistency. Furthermore, we incorporate geometry-aware priors such as intra-object and inter-object similarity to regularize geometric reasoning. Experimental results demonstrate that our method produces complete, simulation-ready 3D objects without requiring manual masks, enabling realistic dynamic interactions on both synthetic and real-world datasets.

---


### 180. [MirrorPPR: Exemplar-Based Portrait Photo Retouching](https://arxiv.org/abs/2606.29308)

**<font color=#1a73e8>作者：</font>** Zhihong Liu, Zheng Li, Jiachun Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While text-guided image editing has made remarkable progress, it remains limited in structural portrait retouching. Textual descriptions struggle to convey fine-grained changes to facial features and body proportions. To address this gap, we introduce Exemplar-Based Portrait Photo Retouching, where the model is given an exemplar pair and tasked with inferring and applying the same retouching operations to a new query image. Existing exemplar-based editing methods primarily focus on tasks with pronounced visual transformations. In contrast, structural portrait retouching involves extremely delicate and localized modifications, making accurate extraction and transfer of these edits challenging. To tackle this, we propose MirrorPPR, a novel framework designed to capture and transfer subtle structural retouching operations. Our method uses a Retouching Operation Extractor to capture the subtle differences from the exemplar pair. The extracted representations are then injected into a pre-trained Diffusion Transformer (DiT) through a connector and Low-Rank Adaptation (LoRA) modules. Furthermore, constructing perfectly aligned cross-identity training pairs is severely hindered by operation misalignment. To overcome this, we propose an advanced data self-augmentation paradigm that ensures strictly aligned retouching operations. To alleviate data scarcity and support this novel task, we introduce MirrorPPR47M, a large-scale dataset with over 47 million retouched pairs. By structuring the dataset into simulated and professional subsets, we enable progressive curriculum learning to smoothly optimize the network. Extensive experiments demonstrate that MirrorPPR significantly outperforms existing baselines in both retouching quality and identity preservation. The project page is available at this https URL.

---


### 181. [D$^{2}$R$^{2}$OSR: Degradation-Disentangled Representation for Real-World Omnidirectional Image Super-Resolution](https://arxiv.org/abs/2606.29314)

**<font color=#1a73e8>作者：</font>** Hongyu An, Xinfeng Zhang, Xu Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growing demand for immersive visual experiences, high-quality omnidirectional images (ODIs) have become increasingly important. However, limitations in imaging devices and transmission bandwidth often lead to low-resolution ODIs, hindering the rendering of fine-grained 360° details, especially in the presence of real-world degradations and geometric distortions. Existing real-world super-resolution (Real-SR) methods are inadequate for ODIs, as their degradation models fail to account for the complex imaging pipeline involving fisheye capture and Equirectangular Projection (ERP), introducing severe aliasing and projection-specific distortions. To address these challenges, we propose D$^{2}$R$^{2}$OSR, a Degradation-Disentangled Representation framework for Real-world Omnidirectional image Super-Resolution. D$^{2}$R$^{2}$OSR explicitly models degradations arising from both fisheye imaging and ERP projection, guided by two key insights: (1) projection priors play a critical role in shaping real-world degradations, and (2) human perception in immersive environments is inherently viewpoint-centric. Accordingly, we introduce a Perspective Projection Representation (PPR) operating alongside the ERP branch to capture viewpoint-aware features, together with a Degradation-Specific Module (DSM) that jointly models ERP-induced geometric distortions and PPR-specific real-world degradations. Extensive experiments demonstrate that D$^{2}$R$^{2}$OSR achieves state-of-the-art performance and produces visually compelling, high-fidelity omnidirectional Real-SR results while maintaining favorable computational efficiency for low-resource deployment.

---


### 182. [FDM-MFVT: Few-step Sampling Diffusion Model for Mask-Free Virtual Try-On](https://arxiv.org/abs/2606.29319)

**<font color=#1a73e8>作者：</font>** Jiaxin Liu, Xiaoye Liang, Lai Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based Virtual Try-On (IVTON) has greatly advanced through diffusion models, yet existing methods require many sampling steps and depend on masks with costly auxiliary networks. In addition, the absence of large-scale mask-free paired datasets further limits the development of mask-free IVTON. We propose FDM-MFVT, a few-step diffusion model for mask-free IVTON, integrating an Outfit-aware Noise Optimization Module (OANO) and an Instruction-driven Try-on Module (IDT) to enhance efficiency and this http URL OANO module initializes the alignment space with noise using the input image and only needs 6 steps to generate a higher-fidelity try-on image compared to 30 this http URL IDT module uses virtual try-on prompts and efficient adaptation to generate high-quality results from garment and person images alone. We further introduce MFVT, a 30,000-pair mask-free IVTON dataset. Experiments show that FDM-MFVT achieves superior quantitative and qualitative results with fewer inference steps than mask-based and mask-free baseline methods.

---


### 183. [SP-CACW: Convergence-Aware Client Weighting for Selfish Personalized Learning](https://arxiv.org/abs/2606.29322)

**<font color=#1a73e8>作者：</font>** Yaron Kiselman, Kfir Y. Levy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative learning is sustainable only when it benefits each participant. Standard federated learning optimizes a global average objective, which can under perform for clients whose data distributions differ substantially from the population. We study selfish personalization: how a designated target client can use peer gradients to minimize its own risk while avoiding negative transfer. We propose SP-CACW, a convergence-aware client-weighting framework that selects aggregation weights by minimizing an upper bound on the target client's convergence error. The resulting rule explicitly trades off peer bias against stochastic variance and can assign zero weight to harmful peers. We provide convergence guarantees under smoothness and bounded-variance assumptions and evaluate the method on MNIST, CIFAR-100, and LEAF Shakespeare, where it is competitive with or improves over strong personalized and clustering baselines.

---


### 184. [Deciphering Region-Level Signatures from Latency Measurements in LEO Satellite Internet](https://arxiv.org/abs/2606.29324)

**<font color=#1a73e8>作者：</font>** Xiang Shi, Yifei Zhang, Peng Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Earth orbit (LEO) satellite Internet has become an indispensable infrastructure that provide growing coverage for global users. Despite extensive measurement efforts, the principles underlying region-level performance characteristics remain insufficiently understood, limiting the ability to identify region-specific latency signatures under dynamic network conditions. In this paper, we formulate the problem of region-level latency characterization using Starlink round-trip time (RTT) measurements from the public LENS dataset. We then propose a hierarchical analytical framework that transforms raw RTT sequences into multi-scale statistical features for cross-region comparison. Using data from five geographically representative regions, we demonstrate that latency differences are strongly associated with deployment factors, particularly infrastructure availability and Starlink dish-to-Point-of-Presence distance. Mutual information analysis identifies minimum RTT as the most discriminative feature, which is further supported by XGBoost-based feature importance. The proposed model well achieves 83% accuracy on short-term data. However, its performance degrades over longer periods, indicating limited temporal generalization and motivating the need for adaptive models and feature representations for long-term performance in the future.

---


### 185. [Sample Complexity of Scientific Discovery: PAC Learnability of Compositional Function Trees](https://arxiv.org/abs/2606.29331)

**<font color=#1a73e8>作者：</font>** Şuayp Talha Kocabay, Talha Rüzgar Akkuş, Kerem Yalçın  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery via symbolic regression is often viewed as statistically and computationally intractable because the hypothesis space of expressions grows combinatorially with depth. This paper revisits the statistical side through the lens of PAC learning, focusing on compositional function trees built from a finite vocabulary of smooth operators (e.g., $\{+,\times,\sin,\exp\}$ and affine maps). We prove that the relevant generalization quantity, Rademacher complexity, hence the excess risk, does not necessarily blow up exponentially with the number of distinct symbolic structures, but is controlled by (i) the depth $d$ and (ii) the Lipschitz constants of the base operators along the composed computation graph. Concretely, under mild Lipschitz conditions on operators and bounded affine leaves, a finite-union bound over a vocabulary of size $K=|\mathcal{H}_{\mathrm{base}}|$ together with Maurer-type vector contraction yields $\mathfrak{R}_n(\mathcal{H}_{\mathrm{comp}}^{d}) \leq (Kb\sqrt{2}L)^{d-1}\mathfrak{R}_n(\mathcal{H}_{\mathrm{comp}}^{1})$ with arity bound $b$; corresponding high-probability risk bounds scale as $\mathcal{O}(L^{d}/\sqrt{n})$ when $K,b=O(1)$ and $\mathfrak{R}_n(\mathcal{H}_{\mathrm{comp}}^{1})=O(n^{-1/2})$. We complement the theory with a modular codebase that trains differentiable operator trees (not MLPs) on synthetic "physics-like" targets of controlled depth and shows that the empirical generalization gap correlates positively with the predicted complexity term $(\widehat{L}^{d})/\sqrt{n}$.

---


### 186. [HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333)

**<font color=#1a73e8>作者：</font>** Yiming Jiang, Hanzhang Tu, Wenfeng Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncalibrated volumetric video streaming for human reconstruction is essential for holographic communication and AR/VR, yet remains challenging due to the need for temporal consistency and computational efficiency from sparse-view inputs. Existing methods rely on per-scene optimization or calibrated cameras, while recent feed-forward models are limited to low-resolution (0.5K) single-frame synthesis. We present HiReFF, a feed-forward method for 2K-resolution 360° human video reconstruction from uncalibrated sparse-view videos. Our framework decomposes the problem into two key tasks: foreground 3D Gaussian reconstruction from sparse-view videos (four views separated by 90°) and computationally efficient high-resolution synthesis. To enable the former, we propose Scale-synchronized Camera Calibration to resolve scale ambiguity for multi-view supervision, and Gaussian-wise Foreground Masking to reconstruct clean foregrounds by modulating Gaussian parameters. For efficient high-resolution synthesis, our High-resolution Side-tuning achieves 2K rendering by augmenting the Gaussian head with supplementary features while keeping the backbone at 0.5K, drastically reducing computational overhead. Experiments demonstrate that HiReFF significantly outperforms existing methods in high-resolution streaming volumetric video reconstruction. this https URL

---


### 187. [Multi-scale Object-Aware Gaze Estimation via Geometric Reasoning](https://arxiv.org/abs/2606.29334)

**<font color=#1a73e8>作者：</font>** Jiajie Mi, Xinyu Liu, Mengke Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze target estimation aims to predict the semantic object an observer fixates upon within an image, a task deeply rooted in the object-oriented nature of human gaze. Observers tend to select a specific semantic entity as the attentional target, rather than responding randomly across arbitrary regions of the image. However, existing methods typically model this task as a direct mapping from global features to gaze heatmaps, essentially treating it as a pixel-level regression problem. This approach fails to explicitly represent the gazed object as a distinct entity, making it difficult to produce stable and semantically consistent predictions in complex scenes. To address this, we propose a two-stage gaze estimation framework guided by object semantics, reformulating gaze target estimation as a hierarchical reasoning process. Our method incorporates object-level representations during feature encoding to align image features with discrete semantic entities, then introduces multi-scale feature fusion and geometric constraints from head pose and gaze direction for fine-grained localization and object-level discrimination. Extensive experiments on GazeFollow, VideoAttentionTarget, ChildPlay, and GOO-Real demonstrate that our method achieves AUC of 0.961, 0.948, 0.987, and 0.977 respectively, delivering strong performance across all benchmarks while maintaining a compact parameter size of 7.1M.

---


### 188. [W4A4 Quantization for Inference on Wan2.2-I2V-A14B](https://arxiv.org/abs/2606.29337)

**<font color=#1a73e8>作者：</font>** Yidong Chen, Chengyu Shi, Jiahao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We summarize our submission to Sub-Challenge 1: W4A4 Quantization for Inference (HiF4 / MXFP4) of the ICME 2026 Low-Bit-width Large-Model Quantization Challenge. The sub-challenge targets 4-bit weight and 4-bit activation inference on Wan-AI/Wan2.2-I2V-A14B under HiF4 or MXFP4 numerical formats. We adapt two complementary ideas from LLM quantization, MixQ-style mixed precision for sparse activation outliers and SmoothQuant-style per-channel smoothing, together with block-wise HiF4 packing for Wan2.2 feed-forward linear layers. Calibration on representative OpenS2V-5M batches identifies heavy-tailed activation channels; smoothing rebalances dynamic range before W4A4 rounding; and a dual-branch GEMM preserves outlier columns in higher precision while the bulk of channels use strict W4A4. On official VBench I2V metrics, our pipeline stays within 2-3.5 percent of FP16 on most quality axes and improves motion smoothness, outperforming a native HiFloat4 baseline that degrades roughly 5 percent relative to FP16 across all reported scores.

---


### 189. [PHF: Privileged Hidden Flow for On-Policy Self-Distillation](https://arxiv.org/abs/2606.29340)

**<font color=#1a73e8>作者：</font>** Yuhan Li, Mingxu Zhang, Dazhong Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a reasoning model on rollouts sampled from its own policy by matching a privileged teacher that also sees verified reference solutions. Existing OPSD objectives supervise only the output distribution, so privileged context affects training through a token-level divergence without directly supervising the internal computation that produced that distribution. We propose Privileged Hidden Flow (PHF), which additionally distills how a privileged teacher's hidden states move along the same rollout. Rather than forcing each student hidden vector to match the teacher vector at the same token position, PHF aligns token-to-token transition directions and trajectory geometry over selected generated positions. The all-layer recipe also includes an adjacent-layer relation computed from these same transitions, without pointwise hidden-state imitation. Under the same 100-step training schedule, PHF improves the Average@12 aggregate over our reproduced OPSD baseline on Qwen3-1.7B, 4B, and 8B, with observed gains of about +2.2, +1.5, and +1.7 points. The transport objective is exactly invariant to shared trajectory offsets; its local geometry term is also invariant to orthogonal transformations of transition directions. Ablations distinguish the fixed PHF recipe from pointwise hidden-state matching, single-channel transition losses, and layer-subset choices, supporting PHF as a compact hidden-flow extension to OPSD.

---


### 190. [Reliability, Faithfulness, and the Limits of Post-hoc Explanations of Opaque Scientific Models](https://arxiv.org/abs/2606.29346)

**<font color=#1a73e8>作者：</font>** Nick Oh, Helen Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc explanation methods are routinely used to interpret scientific machine learning models, with the deliverable understood to be insight into the phenomenon the model has been trained on. The transition may be taken to be secured once the model is reliable enough and the explanation faithful enough. We argue it is not. Reliability checks that the model's predictions match the phenomenon's outcomes, and faithfulness checks that the explanation matches the model, but neither checks whether the model works as the phenomenon works, which is what a claim about structure requires. The chain can support candidate hypotheses under external corroboration, but it cannot, on its own, support claims about how the phenomenon is in fact structured.

---


### 191. [Adaptive Financial Transformer with Regime-Gated Attention for Stock Return Prediction](https://arxiv.org/abs/2606.29347)

**<font color=#1a73e8>作者：</font>** Dishan Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive Financial Transformer (AFT) is proposed for stock return prediction under non-stationary financial markets. The model incorporates a Market Regime Encoder, an Adaptive Gate Network, and an Adaptive Financial Context module to dynamically bias self-attention based on semantic relationships between financial indicators. Unlike conventional Transformer architectures that treat all input features uniformly, the proposed approach groups 95 engineered financial features into 11 semantic categories and adapts attention according to latent market regimes. The study also identifies and corrects sequence alignment and backtesting issues that can inflate reported trading performance, and introduces a financially-aware composite objective that jointly optimizes prediction error, directional accuracy, and non-overlapping Sharpe ratio. Extensive experiments compare the proposed architecture against classical machine learning models, recurrent neural networks, and Transformer baselines using chronological evaluation, five random seeds, ablation studies, hyperparameter optimization, explainability analysis, and multi-stock validation. Results demonstrate competitive predictive performance while reducing model complexity by 15.2% and improving parameter efficiency through feature selection, providing an interpretable Transformer architecture for financial time-series forecasting.

---


### 192. [Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs](https://arxiv.org/abs/2606.29350)

**<font color=#1a73e8>作者：</font>** Junzhou Chen, Jindong Wang, Gang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models and vision-language action models endow the robot with unprecedented capabilities. However, the input of video and high-resolution images yields a massive number of visual tokens, leading to extremely high inference latency and severely hindering the robot's real-time control. To break through this computational bottleneck, we propose ST-Merge, a plug-and-play, training-free framework that efficiently fuses redundant tokens directly during the visual encoding phase. By explicitly constructing 3D spatiotemporal coordinates, it employs a multi-queue parallel matching and weighted aggregation mechanism to achieve efficient and geometrically consistent fusion of redundant tokens across frames. In addition, we introduce a post-merge positional correction mechanism that effectively eliminates spatial deviation caused by merging by dynamically re-evaluating the rotational position code of the weighted centroid of the vision token, thereby ensuring the high-precision spatial awareness required for dexterous operation. In the Video Question Answering task on the mainstream VLM, Qwen2.5-VL, ST-Merge achieves a 2$\times$ inference speedup with only a tiny 1\% loss in precision. When deployed on the $\pi_{0.5}$ VLA policy, ST-Merge achieves an 8.3$\times$ speedup at 1024 $\times$ 1024 resolution and matches the baseline success rate at this high-resolution setting. At lower resolutions, it introduces a small drop in accuracy.

---


### 193. [SAFE-DiT: Semantics-Aware Fast-path Execution for High-Resolution Diffusion Transformers](https://arxiv.org/abs/2606.29360)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Yuxuan Jia, Chuanzhi Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution Diffusion Transformer (DiT) inference contains substantial spatial redundancy, but many spatially adaptive implementations encode regional computation as attention masks, which can inadvertently move scaled dot-product attention (SDPA) away from FlashAttention fast paths. We identify this avoidable systems bottleneck as Mask-Induced Dispatch Tax (MIDT) and show that it grows with latent sequence length. We introduce SAFE-DiT, a training-free Semantics-Aware Fast-path Execution framework that separates exact mask elision from approximation-based spatial scheduling. SAFE-DiT removes only provenance-certified image self-attention masks that induce a row-wise constant shift in attention logits, preserves semantics-bearing masks such as text-padding masks, and realizes spatial adaptation through prompt-conditioned token partitioning, selective state updates with global context, and periodic context refresh. We call this acceleration-only configuration SAFE-Core and report sensitivity-weighted classifier-free guidance separately as SAFE-DiT+SW. On the evaluated PyTorch SDPA stack, redundant masks make long-sequence attention $4.1\times$ to $5.8\times$ slower than the mask-free path. On Lumina-Next, SAFE-DiT achieves $2.69\times$ end-to-end acceleration at $1024^2$ resolution and $5.09\times$ at $2560^2$, reduces peak memory at $2560^2$ from 94.1 to 27.9 GB, and enables $3072^2$ generation when dense inference runs out of memory. Paired metrics, component ablations, and a blinded human study support visual non-inferiority of SAFE-Core to the dense fast-path baseline, while SAFE-DiT+SW provides a separate prompt-alignment operating point without reintroducing spatial self-attention masks. Code is available at this https URL.

---


### 194. [L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction](https://arxiv.org/abs/2606.29374)

**<font color=#1a73e8>作者：</font>** Zetian Song, Chenming Wu, Junnan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense multi-view observations consistently. This paper presents L2D2-GS, a unified framework that reformulates generalizable reconstruction not as a one-shot regression, but as a robust iterative process of optimization and densification. To resolve the ambiguity of supervision in primitive generation, we propose a self-supervised densification policy that derives explicit reward signals from global reconstruction gains to guide local densification. Furthermore, we mitigate irreversible early-stage artifacts through a geometric regularization mechanism, utilizing reparameterization to constrain the optimization manifold and prevent convergence to poor local optima. Extensive experiments on the PandaSet and Waymo datasets demonstrate that our method achieves state-of-the-art reconstruction fidelity and strong zero-shot generalization, while using fewer primitives than competing baselines.

---


### 195. [SAD-GS: Learning Reliable 3D Semantic Gaussian Fields via Dynamic Geo-Semantic Anchoring](https://arxiv.org/abs/2606.29376)

**<font color=#1a73e8>作者：</font>** Yufei Zhang, Chenlu Zhan, Gaoang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D semantic Gaussian field learning relies on multi-view 2D supervision, whose semantic targets and spatial assignments are often unreliable. Across varying viewpoints, view-dependent features cause semantic identity drift, while propagated tracker masks introduce boundary leakage and identity switches. Directly optimizing against these unreliable 2D targets forces the 3D representation to absorb multi-view contradictions, leading to severe error accumulation. To resolve this limitation, we propose SAD-GS, a framework for learning reliable 3D semantic Gaussian fields via dynamic geo-semantic anchoring. Specifically, Semantic Anchor Distillation (SAD) distills per-view visual embeddings into consensus text anchors to establish a viewpoint-invariant semantic identity. Concurrently, the Geo-Semantic Feedback Loop (GSFL) leverages the evolving 3D field to actively filter tracker anomalies and refine spatial mask assignments via a conservative three-gate update rule. Extensive evaluations on LERF-OVS, 3D-OVS, and Mip-NeRF360 show that SAD-GS consistently achieves the best overall performance in both open-vocabulary localization and semantic segmentation. These comprehensive improvements validate the effectiveness and robustness of dynamic geo-semantic anchoring for reliable 3D semantic Gaussian field learning.

---


### 196. [Cross-Temporal Sinhala OCR: Page-Level Adaptation and Diachronic Analysis](https://arxiv.org/abs/2606.29378)

**<font color=#1a73e8>作者：</font>** Avisha Dilhara, Nevidu Jayatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sinhala is a morphologically rich abugida spoken by roughly 16 million people in Sri Lanka, and to date, there are no publicly available real-world datasets for page-level Sinhala OCR. All previous studies for assessing Sinhala OCR models have used artificially generated data. To bridge the gap, we introduce sinhala-ocr-lk-acts-1010, an annotated dataset of 1,010 page-level images and their transcriptions collected from Sri Lankan Legislative Acts published between 1981-1989 and 2000-2019, split into 707 training examples, 101 validation examples, and 202 testing examples. Three models based on deep learning-based visual language processing, namely DeepSeek-OCR V1, DeepSeek-OCR V2, and LightOnOCR-2-1B, are fine-tuned using QLoRA in 8 experiments conducted on consumer and cloud GPUs. LightOnOCR-2-1B is the top performer, achieving a CER of 1.05% across all test examples, outperforming state-of-the-art open-source OCR models such as Surya-OCR (8.84%) and Tesseract v5 (10.69%), as well as commercially available OCR models such as Google Document AI (2.06%). Our results suggest that LightOnOCR-2-1B outperforms other baselines on real-world OCR tasks and maintains consistent performance across all print periods, even when documents are severely degraded.

---


### 197. [DR-GS: Physically-Based Deformable and Relightable 2D Gaussians](https://arxiv.org/abs/2606.29379)

**<font color=#1a73e8>作者：</font>** Jiaxin Li, Tong Wu, Yi Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting (GS) has garnered significant attention in VR/AR and digital content creation due to its explicit parameterization and efficient rendering capabilities. However, existing GS-based methods for deformable objects face two key limitations: (i) illumination is erroneously baked into textures, causing physically inconsistent responses under dynamic deformations and lighting changes; (ii) snapshot-based reconstruction restricts post-reconstruction material editing. To address these challenges, we propose Deformable and Relightable GS (DR-GS), a unified Gaussian framework that integrates physically-based inverse rendering, relighting, and deformation-aware manipulation. Through explicitly disentangling geometry, illumination, and material representations, DR-GS overcomes the limitations of static snapshots, resolving unrealistic appearance under varying conditions while enabling post-reconstruction parameter editing. Extensive experiments show that DR-GS achieves leading visual quality across static reconstruction, dynamic deformation, and relighting, reliably preserving reflections and specular highlights on glossy surfaces. It further establishes a fully decoupled geometry-illumination-material pipeline, enabling high-quality 3D asset creation and comprehensive post-editing.

---


### 198. [Event-VLA: Action-Conditioned Event Fusion for Robust Vision-Language-Action Model](https://arxiv.org/abs/2606.29384)

**<font color=#1a73e8>作者：</font>** Jiaxin Liu, Xun Xu, Zhenhao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have become an important paradigm of embodied AI. However, existing VLA models typically assume well-lit and stable indoor settings, while real-world embodied manipulation may involve degraded RGB observations caused by illumination shifts, posing critical challenges for robust robotic manipulation. To address this gap, we propose \textbf{Event-VLA}, an event-enhanced VLA framework for generalizable manipulation across varying illumination conditions. We formulate VLA-based manipulation under degraded visibility as a practical robustness problem for RGB-centric policies, and introduce event streams as an illumination-robust, motion-sensitive complementary observation to improve robustness across visibility levels. Specifically, unlike conventional multimodal fusion that directly merges event features into the global semantic token space, Event-VLA injects event information through an action-query routing pathway. It uses learnable action queries to extract task-relevant semantics from the VLA reasoning process, and selectively aggregates event tokens via gated cross-attention to construct event-aware action representations. This design preserves the pretrained RGB-language semantic priors while effectively leveraging event information for robust action prediction. Experiments in simulation and real-world deployment show that Event-VLA maintains strong manipulation performance under normal lighting and improves success rates under low-light degradation and near-dark real-world settings.

---


### 199. [Interventional Flow Matching: Prospective Dose-Response Forecasting with Velocity-Field Jacobian Regularization](https://arxiv.org/abs/2606.29386)

**<font color=#1a73e8>作者：</font>** Amirreza Dolatpour Fathkouhi, Justin Lee, Heman Shakeri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting a patient's physiological trajectory under a planned treatment sequence is a prospective interventional problem, not standard time-series extrapolation. We study this problem in glucose management, where insulin and carbohydrate records are policy-dependent: future drivers are coupled to patient state, behavior, and clinical decision rules, so observational forecasting accuracy alone does not guarantee correct responses to planned interventions.
We introduce Interventional Flow Matching (IFM), a continuous-time generative framework for physiologically constrained prospective forecasting. IFM conditions a flow-matching velocity field on patient history and planned future drivers in a bounded latent glucose space. Rather than embedding strict mechanistic glucose--insulin ODE equations or enforcing causality through rollout-based simulations, IFM uses a solver-free regularization: it penalizes the Jacobian of the instantaneous velocity field with respect to smoothed treatment drivers. This imposes signed, dose-bounded local sensitivities directly on the learned dynamics: insulin lowers glucose, carbohydrates raise it, and both responses remain within plausible ranges.
On a simulated UVA/Padova type 1 diabetes cohort, IFM achieves the strongest balance between observed-driver RMSE and interventional response metrics. Across experiments, it consistently produces physiologically correct responses to both insulin and carbohydrate drivers while maintaining high directional, and ranking consistency.

---


### 200. [Exploring the Cryptographic Limits of Transformer Networks](https://arxiv.org/abs/2606.29389)

**<font color=#1a73e8>作者：</font>** Stefan Domunco, Andis Draguns, Philip Torr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent work it has been shown that colluding AI agents can use steganographic methods to exchange malicious information. Whether a transformer can implement steganographic methods depends on what cryptographic functions it can implement, since a transformer that can implement a cryptographic function within its layers has source-free randomness access. Despite existing circuit-complexity results, no prior work maps specific cryptographic constructions to transformer architectures. As Merrill et al. have shown that saturated transformers can be seen as threshold circuits, we first generate threshold circuits for three different cryptographic constructions (Keccak functions, Merkle--Damgard constructions and Merkle Trees) and then map these circuits to different transformer architectures. We derive verified scaling laws for the width and depth of the circuits which implement each cryptographic construction and propose two different mappings: no-attention mapping, tokens-as-gates mapping. Beyond its security implications, this work contributes to by establishing a methodology for deriving structural guarantees on transformer computational capacity. Specifically, we derive constructive upper bounds on what a transformer of a given depth and width could plausibly compute, providing a principled foundation for capability evaluations of transformer-based AI systems.

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
