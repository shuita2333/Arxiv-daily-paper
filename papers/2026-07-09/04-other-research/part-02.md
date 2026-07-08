# 📦 其他研究 | 2026年07月09日

> 本类共 **195** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-195](./part-04.md)

---

### 51. [Where to cut, how deep: BPE and Unigram-LM on chemistry SMILES](https://arxiv.org/abs/2607.05691)

**<font color=#1a73e8>作者：</font>** Hunter Heidenreich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every chemical language model reading SMILES begins with a tokenizer, yet the field has inherited byte-pair encoding (BPE) from natural language with little scrutiny. In natural language, BPE's principal alternative, Unigram-LM, is known to build structurally different vocabularies. Whether that contrast survives in chemistry was open. We report a controlled comparison of BPE and Unigram-LM over a fixed 165-token chemistry base, at the small vocabulary sizes where token embeddings are learnable, across three corpus typologies (diverse, drug-like, natural-products) and both pre-tokenization boundary policies. The two do not converge. In all 22 matched conditions they build near-disjoint subword vocabularies: cross-algorithm Jaccard overlap on the learned pieces never exceeds 0.161, and at most 0.05 once weighted toward the high-frequency pieces a model updates most. Unigram-LM also segments held-out molecules into 29-41% more tokens; the arms largely agree on where to cut but not how deeply, so BPE's segmentation is a strict coarsening of Unigram-LM's on 80-99% of molecules. The separation holds across corpus, boundary, and vocabulary size, persisting even at eight times that scale. The subword algorithm is therefore a modeling decision, not a free default. The study trains no language models.

---


### 52. [Robust Face Super-Resolution and Recognition Through Multi-Feature Aggregation in Diffusion Models](https://arxiv.org/abs/2607.05702)

**<font color=#1a73e8>作者：</font>** Marcelo dos Santos, Rayson Laroca, João Carlos Raposo Neves 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images acquired in surveillance environments often suffer from conditions such as low resolution, variations in pose, irregular illumination, and occlusions. Due to the low quality of these images, face recognition algorithms often struggle. This major limitation can be addressed by employing super-resolution techniques that enhance the details of the image. However, due to the high degree of difficulty of the problem, most super-resolution algorithms tend to cause distortions in the image and in the individual's identity. Thus, additional information must be incorporated into the processing to improve recognition robustness. In this regard, surveillance cameras can capture multiple images, even at low quality, and the data extracted from these images, such as consecutive video frames, can significantly enhance both super-resolution and facial recognition. In this work, we introduce FASR++, a diffusion-model-based super-resolution algorithm. It leverages a reference low-resolution image and features extracted from multiple auxiliary low-quality images to generate a super-resolved output, minimizing distortions in the individual's identity. Our approach recovers facial features without explicitly providing soft attributes or computing a function gradient to guide the reconstruction process. FASR++ generates high-quality images that can considerably improve performance in face recognition tasks when used as a pre-processing step. We validate our approach on two standard face recognition datasets and attain state-of-the-art results for verification, face recognition, and image quality metrics such as PSNR, SSIM, and LPIPS.

---


### 53. [Plainbook: Data Science, in Plain Language](https://arxiv.org/abs/2607.05717)

**<font color=#1a73e8>作者：</font>** Luca de Alfaro, Mathis Aubert, Ranjit Jhala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Jupyter Notebooks have become widely adopted in data science, as they allow the sharing of reproducible computational analysis. They are, however, accessible only to people who understand computer code. To reach the broader audience of scientists interested in data analysis and computation, but unfamiliar with code, we introduce Plainbook, notebooks centered on natural language rather than code.
Plainbook is based on two principles: promote the natural language descriptions, and verify the values. In plainbook, the natural language descriptions are preserved, rather than the resulting code; the code is generated automatically from the cell descriptions. As natural language is read top to bottom, Plainbook adopts a linear execution semantics, in which cells are guaranteed to be executed in the order in which they appear; there is no "hidden state" or out-of-order execution as in Jupyter. To allow users who may not understand code to verify the correctness of the computation, we have built into Plainbook verification mechanisms centered on values and value inspection. These include mechanisms that focus on individual cells, akin to unit tests, as well as global mechanisms. Both the linear execution semantics, and the verification mechanisms, are underpinned by a snapshot kernel that caches execution states and makes execution and verification efficient.

---


### 54. [Low-Overhead Error-Corrected QCNNs Using Bivariate Bicycle Codes](https://arxiv.org/abs/2607.05724)

**<font color=#1a73e8>作者：</font>** Alejandro Rosales, Animesh Yadav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum convolutional neural networks (QCNNs) combine the power of quantum computing and classical CNN for computational speedup in classification tasks. However, noise levels on state-of-the-art quantum devices remain too high for practical QCNN execution. In addition, despite the reliable surface code providing a method for error rates below a threshold value, they have a prohibitively large qubit cost. Recently introduced bivariate bicycle (BB) codes are of particular interest for their high error threshold, constant encoding rate, and linear code distance. Through simulation with realistic hardware noise sources, we demonstrate that a 4-qubit unprotected QCNN fails to converge and exhibits a worse learning rate compared to numerical simulations. Addressing both limitations, we propose a distance-4 BB quantum error-correction (QEC) technique for QCNNs. In doing so, we validate that our low-overhead QEC technique for QCNNS represents a step toward practical QCNNs.

---


### 55. [Association Restoration Test: Revealing Restorable Shortcuts after Unlearning](https://arxiv.org/abs/2607.05726)

**<font color=#1a73e8>作者：</font>** Amy Lu, Changxiu Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Association unlearning aims to disable learned label-attribute shortcuts while preserving task performance. Existing evaluations mainly measure output-level robustness or probe whether shortcut attributes remain readable in frozen features, but neither test determines whether a retained association remains functionally usable by the original classifier. We propose the Association Restoration Test (ART), a post-hoc diagnostic for functional shortcut restorability. ART estimates class-conditional association directions, amplifies residual components, and evaluates the modified features with the original classifier head. Across Waterbirds, CelebA, SpuCoDogs, and an ISIC timestamp-artifact extension, we show that output metrics, representation probes, and ART characterize distinct aspects of shortcut mitigation. These findings motivate restoration-aware evaluation for unlearning and shortcut-mitigation methods that target learned associations rather than individual classes or concepts.

---


### 56. [SAMPLe: SAM-based Optimizer for Prompt Learning in VLMs](https://arxiv.org/abs/2607.05727)

**<font color=#1a73e8>作者：</font>** Hossein Rajoli, Fatemeh Lotfi, Niloufar Alipour Talemi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained Vision-Language Models (VLMs) like CLIP have proven highly effective as foundation models for various downstream applications. However, prompt learning in VLMs encounters a performance-generalization dilemma: while prompts can be tuned to achieve high accuracy on seen distributions, this tuning process often undermines their generalizability to unseen data. The limited set of learnable prompts, which contextualize and condition the input to steer it toward the task within the pretrained VLM, tends to overfit the training data, leading to a trade-off between task-specific performance and preserving generalization. To address this dilemma, we introduce SAMPLe (Sharpness-Aware Minimization Prompt Learning), a plug-in sharpness-aware optimizer that enhances prompt generalizability by accounting for loss landscape sharpness. Unlike conventional methods, SAMPLe balances exploration and exploitation by satisfying objective function constraints at each step, dynamically adapting to the current optimization state based on the local curvature and gradient properties. This approach reduces overfitting on seen distributions and improves adaptability to unseen data, preserving the generalization potential of pre-trained VLM models. We integrate SAMPLe into multiple prompt learning frameworks, including CoOp, CoCoOp, MaPLe, TCP, and Co-Prompt, demonstrating its effectiveness across diverse methods. Experiments show that SAMPLe elevates prompt learning frameworks and consistently outperforms existing optimizers across diverse settings, establishing itself as a robust, model-agnostic solution for prompt learning.

---


### 57. [ARMS: Anchor-Relational Motion Streaming for Seamless Solo-Social Motion Transitions](https://arxiv.org/abs/2607.05733)

**<font color=#1a73e8>作者：</font>** Huakun Liu, Qing Yu, Kent Fujiwara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating temporally continuous and socially coherent human motion from text remains a fundamental challenge, particularly in realistic streams where people act alone, enter interactions, and later disengage. Most existing methods generate fixed-length motion clips under static agent configurations, which makes them brittle to solo-social transitions and unsuitable for incremental generation over long horizons. We propose ARMS, an Anchor-Relational Motion Streaming framework that unifies solo motion and human-human interaction within a single causal generative process. ARMS introduces a dynamics-asymmetric representation that decouples per-person temporal evolution from inter-person alignment via a partner-referenced relative-translation term, enabling seamless switching of social coupling without sacrificing long-horizon stability or spatial consistency between agents. On top of a causal latent space, a causal relational diffusion model progressively refines motion segment by segment using only past context, capturing both intra-person temporal dependencies and inter-person relations. Mode-aware relational gating activates or masks cross-agent connections, allowing the same model to support both solo and interaction generation. Experiments show that ARMS improves transition smoothness and social coherence compared to interaction-centric baselines, while also achieving competitive results on human-human interaction benchmarks.

---


### 58. [Optimized Adaptive Loop Filter in Versatile Video Coding](https://arxiv.org/abs/2607.05737)

**<font color=#1a73e8>作者：</font>** Meng Xuewei, Zhang Jiaqi, Jia Chuanmin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the Versatile Video Coding~(VVC) standard, adaptive loop filter~(ALF), including Geometry transformation-based Adaptive Loop Filter~(GALF) and Cross Component Adaptive Loop Filter~(CCALF), plays an essential role in reducing compression artifacts. However, it also has high coding complexity and requires many picture buffer accesses in the encoder that will increase external memory access and is unfriendly to the software and hardware design. Therefore, we propose an optimized ALF framework, including the parallel design of GALF and CCALF, the adaptive parameter decision of GALF, and one-pass CCALF scheme by effectively estimating the CCALF filtering distortion without conducting filter operation. Compared to VTM-8.0, the proposed method can reduce the picture buffer access from 152 to 1 and achieve roughly 25\% time-savings of the ALF module with negligible coding performance change under RA configuration. Some of the proposed methods have been adopted in the VVC reference software.

---


### 59. [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](https://arxiv.org/abs/2607.05743)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents now read repositories, call tools, and execute shell commands with limited human oversight, and a fast-growing body of work studies whether the execution layer around them is actually safe. That literature is scattered. Papers on sandbox isolation, capability and access control, policy enforcement, time-of-check-to-time-of-use (TOCTOU) races, Model Context Protocol (MCP) threats, identity delegation, execution provenance, network egress control, and static analysis of agent-generated code are published independently and rarely cite one another. We systematize 39 papers published between 2023 and 2026 into 17 categories, each verified directly against its source. The same verification protocol also confirms four disclosed, patched CVEs directly affecting production agent harnesses. Reading across categories surfaces five cross-cutting gaps that no single paper addresses. (1) Isolation architectures and capability models are almost never evaluated against one another on a shared benchmark. (2) Policy-enforcement studies report failure rates from 69% to 98% of real denylists, yet no isolation paper re-evaluates its own defense under that adversarial setting. (3) TOCTOU and MCP threats are analyzed as separate literatures despite both being instances of the same state-validation problem. (4) Every enforcement mechanism assumes an honest policy author, leaving policy-authoring error itself unaddressed. (5) Benign but out-of-scope agent actions occurring at rates up to 17.1% under realistic prompting are addressed by no access-control or capability paper in the corpus. Existing broader surveys of agentic AI security discuss sandboxing only as one item among many defenses, leaving execution security without a dedicated systematization. This paper is written to fill that gap. We conclude with a research agenda directed at the five gaps.

---


### 60. [Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol: An Approval-View Fidelity Gap Across Three Independent Server Implementations](https://arxiv.org/abs/2607.05744)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) is the dominant way coding agents discover and invoke external tools. A server advertises each tool through a tools/list handshake that returns a name, a natural-language description, and a JSON input schema. The client renders this metadata once, in a one-time approval dialog, and then injects it verbatim into the model's context on every subsequent turn. Nothing in the protocol requires the rendered approval view and the bytes delivered to the model to match. We isolate that gap as a single structural mechanism, concealment encoding, and show with a model-free, protocol-free analysis that Unicode's TAG block (U+E0000 to U+E007F) has no assigned glyph in any mainstream terminal, chat, or IDE renderer, so a payload written in it is absent from what a human reviewer sees while surviving byte-for-byte into the model's tokenizer. We then measure whether this mechanism actually defeats today's client-side defenses, building a proof-of-concept that speaks the real MCP JSON-RPC/stdio protocol against a genuine client and server. Across 5 distinct MCP metadata surfaces we implement 8 concrete techniques with a deterministic, protocol-level harness. All 8/8 techniques deliver an attacker-controlled payload into the model's context, 4/8 evade a representative string-matching sanitizer, and exactly as the mechanism analysis predicts, only the TAG-block encoding (1/8) is invisible in the human approval view while still reaching the model verbatim. MCP forces re-approval for 0/8 techniques even under a time-of-check to time-of-use rug-pull. To test whether these outcomes are a property of the protocol or an artifact of one server codebase, we re-implement the catalogue against 3 independently developed Python MCP server libraries and find total agreement across all 32 cross-library outcome cells. The baseline sanitizer flags 0 of 25 benign descriptions.

---


### 61. [Two Sides of the Same Coin: Learning the Backdoor to Remove the Backdoor](https://arxiv.org/abs/2607.05748)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Christian Wressnegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The community has recently developed various training-time defenses to counter neural backdoors introduced through data poisoning. In light of the observation that a model learns poisonous samples responsible for the backdoor easier than benign samples, these approaches either use a fixed threshold of the training loss for splitting or iteratively learn a reference model as an oracle for identifying benign samples. In particular, the latter has proven effective for anti-backdoor learning.
Our method, HARVEY, leverages a similar yet crucially different technique: learning an oracle for poisonous rather than benign samples. Learning a backdoored reference model is significantly easier than learning a reference model on benign data. Consequently, we can identify poisonous samples much more accurately than related work identifies benign samples. This crucial difference enables near-perfect backdoor removal as we demonstrate in our evaluation. HARVEY substantially outperforms related approaches across attack types, datasets, and architectures, lowering the attack success rate to the very minimum at a negligible loss in natural accuracy. The figure below shows an overview of our methods working principle.

---


### 62. [ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation](https://arxiv.org/abs/2607.05750)

**<font color=#1a73e8>作者：</font>** Yunhan Xu, Qifeng Wu, Xunjin Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-aided design (CAD) for industrial components requires long-horizon procedural modeling, robust feature dependencies, editable parametric geometry, and production-grade B-Rep execution. Existing text-to-CAD methods have made promising progress in generating CAD programs from natural-language descriptions, but they still struggle when user prompts are ambiguous, underspecified, or only describe high-level design intent. They also rarely exploit expert procedural knowledge naturally available in industrial workflows, such as CATIA operation recordings, macro logs, drawing notes, and engineering descriptions. We present \algname, a skill-guided industrial CAD agent with expert-grounded knowledge distillation. The core of \algname is CAD intermediate representation (CAD-IR), an executable procedural representation that encodes parameters, ordered operations, MCP tool bindings, dependencies, generated entities, and verification rules. CAD-IR plays two key roles: it first serves as the carrier for distilling expert CAD procedures into reusable parameterized skills; then it provides a procedural scaffold that turns vague or intermediate-level prompts into complete executable CAD operations. \algname retrieves expert-derived skills, instantiates and revises CAD-IR, executes the resulting procedure through a dedicated CATIA-MCP backend, and uses multi-view visual feedback for iterative refinement, and finally generates production-ready B-Rep models. On the Text2CAD benchmark, CAD-IR improves generation from intermediate prompts by reducing mean Chamfer Distance from $14.83$ to $9.88$, showing its ability to bridge ambiguous textual intent and executable CAD construction. On four complex automotive components, CAD-IR enables expert CATIA recordings to be distilled into reusable skills, allowing \algname to generate editable CATIA-native B-Rep models for new variant requests.

---


### 63. [Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator](https://arxiv.org/abs/2607.05765)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Seungjun Lee, Yinghao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied navigation aims to build agents that interpret multimodal goals, reason in 3D space, and reach target destinations reliably in the real world. However, progress remains constrained by the lack of scalable, high-fidelity, and physically grounded interactive environments. Although real-world scanned datasets offer visual realism, they are limited by scale. In contrast, synthetic simulators scale more easily but often exhibit large sim-to-real gaps. We introduce Image2Sim, a real-time neural simulation framework that constructs high-quality interactive environments from posed RGB-D image sequences. The central idea is to decouple 3D spatial anchoring from photorealistic observation synthesis. For scene construction, Image2Sim uses a feed-forward feature Gaussian model that lifts posed RGB-D observations into a 3D feature-Gaussian representation in a single pass. For rendering, we propose a Geometry-Aware One-Step Pixel Flow model that transforms sparse and noisy Gaussian projections into high-quality panoramic RGB-D observations. Image2Sim also serves as a fully automated embodied data engine that generates high-fidelity observations, executable actions, and diverse navigation instructions at scale. It converts large collections of videos and images into nearly 20K interactive scenes and synthesizes more than 10 million navigation training samples. Navigation models trained entirely in these neural environments achieve strong improvements on major benchmarks and transfer effectively to real-world zero-shot settings. These results suggest that scalable neural simulation can serve as a practical training substrate for embodied navigation at scale.

---


### 64. [DeSeG: Decoupling Semantic Intent and Geometric Constraints for Physically Plausible Human-Scene Interaction](https://arxiv.org/abs/2607.05787)

**<font color=#1a73e8>作者：</font>** Jiakun Li, Zhe Li, Wenqiang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing physically plausible human-scene interactions (HSI) remains a critical challenge in computer vision and the development of human avatars. Although recent generative models enable diverse motion synthesis, they suffer from an inductive bias referred to as semantic-geometric entanglement. Because spatial constraints often strongly correlate with specific actions in training data, monolithic models will learn the shortcut bias, aggressively overriding the semantic intent when faced with strict geometric cues. Furthermore, this entanglement exacerbates physical hallucinations, such as body-scene penetrations. To address these limitations, we propose DeSeG, a hierarchical framework that explicitly decouples semantic intent from geometric constraints. First, we introduce a Residual Semantic Planner that encodes textual instructions and canonicalized goal voxels into a compact latent space, enabling fine-grained semantic control independent of spatial trajectories. Second, we propose a physics regularized diffusion executor that incorporates differentiable repulsive potential fields directly into the diffusion objective, enforcing collision-aware motion generation. Extensive experiments on the Lingo dataset demonstrate that DeSeG achieves state-of-the-art performance, reducing mean scene penetration by 47% and improving semantic alignment by 29% over the SOTA baselines.

---


### 65. [From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space](https://arxiv.org/abs/2607.05794)

**<font color=#1a73e8>作者：</font>** Yue Xu, Yutao Sun, Yihao Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term user memory is essential for personalized conversational agents, yet many memory systems still expose memory through passive retrieval interfaces, making the model a consumer of pre-selected evidence. We introduce NapMem, a framework for learning to use long-term user memory as a structured action space rather than passively retrieved context. NapMem organizes user history into a linked multi-granularity memory pyramid, where raw conversations, typed memory records, topic tracks, and user profiles are connected through provenance relations, and exposes these levels through memory tools. The agent is trained to select memory according to the query and intermediate evidence, allowing it to inspect different memory granularities before answering. Experiments on PersonaMem-v2, LongMemEval, and LoCoMo show that a NapMem agent trained with memory-tool reinforcement learning is competitive across diverse memory-intensive tasks, while evaluations on non-memory tasks suggest that the learned policy largely preserves general reasoning and tool-use abilities. Additional analyses examine storage, inference cost, tool-use behavior, and ablations over navigation, memory granularity, and RL training. Our results suggest that long-term user memory benefits from coupling structured storage with a learned policy for using memory at the appropriate granularity.

---


### 66. [TRIG: Trajectory-Rig Decoupled Metric Geometry Learning](https://arxiv.org/abs/2607.05801)

**<font color=#1a73e8>作者：</font>** Lizhou Liao, Wentao Xu, Handong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-centric autonomous driving requires accurate metric geometry and ego-motion estimation from synchronized multi-camera observations. Recent visual geometry models show strong performance in pose estimation, depth prediction, and 3D reconstruction, but are not tailored to rigid multi-camera driving systems. They often encode camera poses as entangled representations, in which time-varying ego-motion and static camera-rig geometry are jointly modeled, limiting the utilization of vehicle-side geometric priors. We propose Trajectory-Rig Decoupled Metric Geometry Learning (TRIG), a geometry perception framework for autonomous driving. TRIG factorizes camera poses into ego-trajectory and camera-rig components, enabling separate modeling of ego-motion and static multi-camera topology. We introduce decoupled pose encoding and supervision, which separately constrain trajectory evolution and rig geometry for metric-consistent learning. Moreover, sparse Temporal--Spatial attention separates cross-camera interaction from temporal aggregation, reducing global attention cost while preserving geometric reasoning. Experiments on five autonomous driving benchmarks show that TRIG achieves state-of-the-art performance in pose estimation, metric depth prediction, and 3D reconstruction.

---


### 67. [TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training](https://arxiv.org/abs/2607.05804)

**<font color=#1a73e8>作者：</font>** Yuhang Zhou, Kai Zheng, Haoling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens, leaving deeper decision turns under-trained once initial behaviors are aligned. To address these challenges, we propose TurnOPD, a turn-level budgeting strategy for efficient on-policy distillation of long-horizon agents. TurnOPD consists of two budget controllers: adaptive rollout-depth budgeting, which uses probe-based turn statistics to determine rollout length, and progressive turn-normalized loss budgeting, which gradually shifts KL weighting from token-level to turn-balanced supervision. Experiments on ALFWorld, WebShop, and Multi-Hop Search with task-specialized teacher models show that TurnOPD achieves superior validation accuracy under equal wall-clock training budgets and advances the accuracy--time frontier beyond vanilla OPD.

---


### 68. [Heckman-Corrected Epistemic Uncertainty: Selection on Unobservables Defeats Importance Weighting](https://arxiv.org/abs/2607.05806)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data for machine learning is routinely collected by a selection process the model never sees: loans are observed only when granted, outcomes only when a test was ordered. The standard fixes -- importance weighting, covariate-shift correction, MAR imputation -- assume selection is ignorable given observables. Econometrics solved the harder case in 1979: Heckman's two-equation model jointly fits a probit selection equation and an outcome equation linked through correlated errors, and the inverse-Mills-ratio term corrects for selection on unobservables, where importance weighting is structurally helpless. We instantiate this for deep epistemic uncertainty: a deep outcome network, a linear selection head, and a joint bivariate-normal likelihood over all units, ensembled for predictive variance. In a controlled generator where sampling probability depends on an unobservable correlated (rho up to 0.9) with the outcome noise, deep ensembles, MC dropout, and GP baselines are overconfident exactly where data was avoided: coverage of nominal-90% intervals falls to 64.4% at rho=0.9, and importance weighting with oracle propensities does not fix it (43.1%) -- reweighting corrects the covariate distribution, not the conditional bias E[y|x,selected] != E[y|x]. The Heckman correction restores coverage (88.9%) when the selection equation has an instrument -- a variable affecting selection but not the outcome -- and degrades measurably without one (40.3%); we chart this honesty curve rather than hide it. On real tabular data with induced MNAR selection, the corrected intervals are the best-calibrated (lowest region-ECE) non-oracle method in selected-against regions; baselines matching its raw coverage do so only by over-widening everywhere. Our estimators reproduce classic Stata output to seven digits. We state which identification regime a practitioner is in, and release the code.

---


### 69. [Level-Crossing Density as a Mesh-Free High-Frequency Auxiliary Loss for Implicit Neural Representations](https://arxiv.org/abs/2607.05815)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Minkowski functionals of a field's excursion sets -- area, boundary measure, and Euler characteristic -- describe its level-set morphology; the Euler characteristic is the cheapest handle on topology. We derive smooth Monte-Carlo estimators for all three of a continuous neural field, evaluated at scattered points via the co-area formula and Gauss-Bonnet, using only autodiff: no grid, no complex, no persistence. The estimator is accurate to 1-3% against exact topology in 2D and 3D, and costs about 3 ms per iteration where a persistent-homology (PH) loss on a cubical grid costs 650-1000 ms -- a 250x gap. We establish four design rules without which these losses silently fail: a dense level ladder (invariants are flat in the parameters away from transitions), a $C^2$ backbone (ReLU nets hide curvature in kinks), the full Minkowski vector (Euler characteristic alone is an alternating sum, gamed by debris-hole cancellation; pricing perimeter closes the channel), and sampling-scale coverage. In 2D the vector-valued cap is the only method in a controlled comparison that both repairs topology (3/3 seeds) and preserves fidelity -- uniform smoothing repairs at 11-17x the fidelity cost, and the Euler term alone repairs nothing. In 3D neural-SDF fitting, however, a failure mode we believe general to any sampled soft topology objective appears: gradient descent adversarially hides topological noise below the sampling density, where the estimator is blind -- spurious-feature counts are invariant to 4x more samples, and closing the window needs cubically many points, erasing the cost advantage. A grid-based PH baseline, whose complex is the evaluation resolution, solves the same benchmark ($4/9$ exact; median $b_1$ error 1 vs. ours above $10^4$). The 250x cost of persistence is, at present, the price of having no null space. We release estimators, receipts, and benchmarks.

---


### 70. [Complementary Roles of Image Classification and Vessel Segmentation in AI-Based Screening for Retinopathy of Prematurity Plus Disease in a Kenyan Preterm Cohort](https://arxiv.org/abs/2607.05825)

**<font color=#1a73e8>作者：</font>** Fred Mutisya, Oscar Onyango, Sarah Sitati 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. Retinopathy of prematurity (ROP) is a preventable cause of childhood blindness, with rising burden in low- and middle-income countries where ROP-trained ophthalmologists are scarce. Plus disease, marked by retinal vessel dilation and tortuosity, triggers treatment but is subjective and variable. Automated screening could extend specialist reach, but African evidence remains limited.
Methods. We analysed 121 Kenyan preterm infants, covering 237 eyes and 1,635 fundus images graded as No Plus, Pre-Plus or Plus. Vessel annotations from two graders supported segmentation training. Eleven configurations were evaluated for eye-level Plus detection using patient-grouped nested cross-validation, including image classifiers, multiple-instance learning, multi-task segmentation-classification, and segment-then-classify pipelines.
Results. Vessel segmentation was feasible, achieving pooled Dice 0.533, IoU 0.368, sensitivity 0.623 and specificity 0.979 on held-out images. RGB classifiers were highly sensitive but over-referred, while segmentation-coupled models were more specific. Combining approaches improved performance: an OR-based screen achieved the highest sensitivity, an AND-based confirmation achieved the highest specificity, and a probability ensemble gave the best balanced performance, with sensitivity 0.692, specificity 0.914 and balanced accuracy 0.803, outperforming the vision classifier alone.
Conclusions. Classification and vessel segmentation are complementary for ROP Plus detection in Kenyan data. Classifiers support sensitive case-finding, while segmentation improves specificity and reduces over-referral. African ROP AI systems should use combined workflows and undergo prospective multi-site validation.

---


### 71. [Decision-Focused Scenario Generation and Selection for Efficient and Robust Grid Dispatch](https://arxiv.org/abs/2607.05830)

**<font color=#1a73e8>作者：</font>** Yangze Zhou, Yihong Zhou, Thomas Morstyn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing uncertainty from flexible demand and renewable generation has made distributionally robust optimization (DRO) an important tool for robust power system dispatch. DRO relies on forecast scenarios to construct ambiguity sets, but conventional scenario generation pipelines are often trained in an accuracy-oriented manner and may neglect spatial correlations among uncertainties. This mismatch can produce ambiguity sets that are statistically plausible but suboptimal for downstream operation. This work proposes a decision-focused generative framework for correlated scenario generation in DRO-based dispatch. Instead of training generative models solely to fit the historical uncertainty distribution, the proposed framework optimizes generated scenarios according to their induced downstream operational cost. The proposed framework is tailored to mainstream generative models, including variational autoencoders, generative adversarial networks, and diffusion models, while capturing the joint distribution of uncertainties across buses. To improve computational tractability, we further develop a differentiable scenario selector that selects decision-relevant scenarios from a generated pool and can be trained within the same decision-focused pipeline. Case studies demonstrate that the proposed framework effectively reduces 0.80%-2.02% operational cost across different generative models compared to accuracy-oriented methods.

---


### 72. [Withdrawability in Fiat-Shamir with aborts constructions](https://arxiv.org/abs/2607.05831)

**<font color=#1a73e8>作者：</font>** Ramses Fernandez-Valencia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This article presents an extension of the work performed by Liu, Baek and Susilo on withdrawable signatures to the Fiat-Shamir with aborts paradigm. We introduce an abstract construction, and provide security proofs for this proposal. As an instantiation, we provide a concrete withdrawable signature scheme based on a no-hint, full-t Dilithium-style Fiat-Shamir with aborts construction; adapting to production ML-DSA (with hints) introduces a small epsilon term.

---


### 73. [Realistic Compound-Lens Defocus Blur Synthesis](https://arxiv.org/abs/2607.05837)

**<font color=#1a73e8>作者：</font>** Yunkyu Lee, Woohyeok Kim, Sunghyun Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Defocus blur degrades fine image structures and limits visual perception, which can adversely affect downstream vision tasks. Although recent deep learning deblurring methods have achieved strong performance, their effectiveness depends on training data and often degrades across cameras and lenses due to limited optical diversity and realism in existing datasets. In this paper, we propose a pipeline for synthesizing realistic defocus deblurring datasets for diverse compound lenses. It integrates efficient wave-optics PSF computation via Debye CZT propagation, depth-aware defocus rendering with occlusion handling, and blur synthesis in the radiometrically linear space with camera ISP simulation. This unified pipeline enables the scalable generation of photorealistic defocus datasets with diverse lens characteristics. Using our pipeline, we generate CLDefocus, a large-scale synthetic dataset containing lens-diverse defocus image pairs. We further analyze the limitations of real-captured defocus datasets and show that such imperfections can bias full-reference evaluation. Extensive experiments demonstrate that models trained on CLDefocus achieve improved cross-device generalization compared to models trained on existing real and synthetic datasets.

---


### 74. [VisTCP: A Visualization Framework to Construct Knowledge-Graph-Based Representation for Traditional Chinese Painting](https://arxiv.org/abs/2607.05841)

**<font color=#1a73e8>作者：</font>** Zhiguang Zhou, Fengling Zheng, Miaoxin Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Structured representation can characterize semantic objects and relationships in images. It provides a possible effective way for the semantic understanding of Traditional Chinese Paintings (TCPs) to better support archaeology and art history research. However, most image-oriented structured representation methods perform poorly on TCPs, due to two major challenges: 1) the objects and events of TCPs exhibit substantial differences from modern natural images, which results in semantic misunderstandings of TCPs; and 2) it is difficult to achieve accurate identification of ancient objects and events in TCPs, even for domain this http URL this paper, we propose VisTCP, a visualization framework that combines a TCP-oriented intelligent model and expert knowledge, which enables art historians to achieve trustworthy structured representations of TCPs in a human-in-the-loop manner. Firstly, we conduct a pilot study with three domain experts to build a semantic taxonomy of TCPs. Then, expert-annotated data are used to train a TCP-oriented structured representation model, which can automatically extract meaningful objects and their relationships in TCPs. To inform users of the model uncertainty, we design a joint embedding visualization view to show the differences between expert annotations and model predictions. This allows users to refine the structured representation based on their domain knowledge, enabling iterative optimization of the model. Finally, we conduct a case study, a usage scenario, and expert interviews on a real dataset to demonstrate the effectiveness of VisTCP in supporting the structured representation and semantic understanding of TCPs.

---


### 75. [StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems](https://arxiv.org/abs/2607.05844)

**<font color=#1a73e8>作者：</font>** Sergey Volkov, Yang Li, Ye Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (claim_id / claim_ref), deterministic predicate contracts, and projection-time resolution that cannot rewrite replicated state.
We evaluate StateFuse against flat multi-value, raw-log, provenance-style, and collapsed baselines under matched resolver and verification policies. On a 282-question official conflict-bearing MemoryAgentBench slice, the compared methods tie on answer accuracy, but conflict-preserving surfaces keep contradictions visible while collapsed surfaces do not. In a controlled agent loop with uniform verification, preserving ambiguity enables safer abstention and correction than early collapse. A correction-handle ablation further shows that semantic handles matter when exact prior identifiers are unavailable.
The resulting claim is narrow: StateFuse is best supported as a safer public memory contract for contradiction surfacing, abstention, and auditable correction, not as a universal accuracy gain.

---


### 76. [CoPiT: Cognitive Pivot Translation for Digraphic Low-Resource Mongolian in the Traditional Script](https://arxiv.org/abs/2607.05849)

**<font color=#1a73e8>作者：</font>** Burte Bayarsaikhan, Serynn Kim, Buru Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource languages remain challenging for machine translation, and Mongolian is a representative case. As a digraphic language, Mongolian is written in both Cyrillic and Traditional scripts, which exhibit a severe imbalance in data availability. While the Cyrillic script is relatively well-resourced, the Traditional script remains extremely data-scarce and orthographically ambiguous, leading to substantial performance degradation in direct translation. We propose CoPiT, a cognitively motivated pivot-based translation pipeline that exploits this internal resource hierarchy by routing translation through the Cyrillic script. The pipeline explicitly resolves script-induced ambiguity in the Traditional script before translation, enabling more stable and accurate meaning transfer. Across multiple backbone models and target languages, CoPiT consistently outperforms direct translation, achieving substantial absolute BLEU improvements together with consistent 1.5-1.6x COMET gains. These gains allow strong open-source models to match or outperform GPT-4.1 under comparable evaluation settings. Beyond inference-time improvements, CoPiT enables the construction of synthetic parallel data directly from Traditional-script text, mitigating data scarcity in realistic low-resource scenarios. We release a new multi-script parallel dataset covering Mongolian in both scripts alongside English, Korean, and Russian. All datasets and code are publicly available at this https URL.

---


### 77. [Breaking Spurious Correlations via Generative Randomization and Cross-Variant Self-Supervised Learning](https://arxiv.org/abs/2607.05850)

**<font color=#1a73e8>作者：</font>** Suraj Yadav, Anjaneya Sharma, Siddharth Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks trained with Empirical Risk Minimization (ERM) often fail under distribution shifts because they exploit spurious correlations between object labels and background context. Recent generative approaches address this issue by creating counterfactual images with altered contexts, but typically use these samples as standard data augmentation, leaving the model free to retain background-sensitive representations. We propose a two-stage framework that uses generative intervention to explicitly learn background-invariant visual representations. First, we isolate the foreground object using zero-shot segmentation and generate context-shifted variants with a structure-preserving diffusion model, preserving object identity while varying the surrounding environment. We then introduce Cross-Variant Self-Supervised Learning, where variants of the same object under different backgrounds form positive pairs in a contrastive objective. This encourages the encoder to align object-centric representations while suppressing background-specific cues. Then, we fine-tune the pretrained encoder using an ERM warm-up followed by GroupDRO with layer-wise learning rates. Experiments on distribution-shift benchmarks demonstrate best worst-group performance, achieving 92.5% on Waterbirds, 81.7% on MetaShift, and 87.4% on NICO++. Code: this https URL

---


### 78. [Unsupervised Anomaly Detection of Information Operations Users via Behavioral and Language Patterns](https://arxiv.org/abs/2607.05855)

**<font color=#1a73e8>作者：</font>** Sishun Liu, Sajal Halder, Ke Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information Operations on social media networks have been identified as a significant threat to democracy and modern society, but they are challenging and expensive to detect by humans. Existing supervised IO detection methods fail to capture the dynamic nature of evolving IO user behavior, while existing unsupervised approaches rely on oversimplified assumptions of coordination among IO users that may not exist in practice. To overcome the limitations of existing methods, we formulate IO user detection as an anomaly detection problem and propose a novel unsupervised IO user detection approach called Temporal-bEhavior-laNguage Signals for information Operation Recognition (TENSOR), which leverages multimodal data, including temporal online user behavior, such as message posting activities, and the textual content of the messages. The motivation is that IO users are typically a very small fraction of all online users and have unique temporal behavioral and language patterns. Specifically, we train a Temporal Point Process (TPP) to capture abnormal temporal behavioral patterns of IO users because they are known to behave in a coordinated manner for IO campaigns. We further introduce a novel evidence function that converts LLM responses, which are generated from user post timelines, into quantitative scores to adjust the TPP outputs for better IO user detection. Experimental results show that TENSOR outperforms the baselines on five real-world IO datasets. Code is available at this https URL.

---


### 79. [MSCENet: A Multi-Scale Correlation Enhanced Network for Anomaly Detection](https://arxiv.org/abs/2607.05864)

**<font color=#1a73e8>作者：</font>** Long Zhao, Shixun Ji, Zhipeng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the field of multivariate time series anomaly detection, against the backdrop of increasing data complexity and complex dependencies across multiple temporal scales, traditional methods often struggle to simultaneously capture temporal dynamic features and intricate inter-series correlations. To address this, we propose an innovative framework, MSCENet, which leverages advanced spatio-temporal learning and multi-scale learning techniques to enhance detection accuracy. MSCENet includes a fine-grained temporal convolution module that captures complex temporal dependencies through dilated convolutions, enabling the detection of both short- and long-term patterns. Additionally, the framework models inter-series relationships as a graph structure, using Mixhop graph convolutions to adaptively capture spatial dependencies across varying time scales. To support robust anomaly detection, the multi-scale gated convolution module in MSCENet integrates spatial and temporal attributes through gated mechanisms, facilitating the detection of subtle variations across multiple scales. Experimental evaluations on real-world datasets: SMD, PSM, and SWaT. It provides an adaptable and high-performance solution for anomaly detection in complex time series data environments.

---


### 80. [Differentially Private Natural Gradient Descent](https://arxiv.org/abs/2607.05866)

**<font color=#1a73e8>作者：</font>** Pan Li, Kai Chen, Shuai Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under a fixed privacy budget, the utility of differentially private (DP) training is ultimately determined by its optimization efficiency. Standard first-order DP optimizers such as DP-SGD rely solely on local gradients and ignore the underlying loss curvature. This geometric blindness causes severe zigzagging in ill-conditioned landscapes, squandering precious privacy budgets on inefficient iterations. Practitioners are thus trapped in a bind: either stop training prematurely or inject massive per-step noise, both of which critically compromise final model utility. Natural Gradient Descent (NGD) resolves this by preconditioning gradients with curvature, aligning updates with the loss geometry and extracting more efficient signal from every noisy step, offering a principled pathway to break the privacy-utility bottleneck.
Despite its theoretical appeal, directly integrating NGD with DP introduces fundamental challenges: curvature estimation itself consumes prohibitive privacy budgets, isotropic DP operations conflict with the anisotropic scaling of NGD, and the inverse curvature catastrophically amplify parameter updates in flat directions, causing training instability. We propose DP-NGD, a practical framework that systematically addresses these obstacles by decoupling curvature estimation from private data, reconciling isotropic DP constraints with anisotropic second-order optimization via a whitened-space mechanism, and dynamically clamping the curvature to stabilize training. Extensive experiments on standard benchmarks demonstrate that DP-NGD achieves state-of-the-art accuracy, breaking through the utility ceilings of first-order baselines while delivering up to a $10\times$ convergence speedup under the same privacy budget.

---


### 81. [No Subspace to Track: Non-Identifiability and Optimizer State in Low-Rank Training](https://arxiv.org/abs/2607.05872)

**<font color=#1a73e8>作者：</font>** Noel Thomas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-efficient optimizers such as GaLore train large language models by projecting gradients onto a rank-r subspace recomputed every T steps, assuming this subspace is a slowly drifting object that can be tracked. We show that beyond a small reproducible core, there is no such object. Two estimates of the top-r subspace computed at the same step from disjoint minibatches disagree as much as estimates computed T steps apart (0.73 vs 0.74 of the maximal chordal distance sqrt(2r), at Pythia-160M with r=128): the apparent rotation at each refresh is dominated by estimator noise. This holds across four model families in three architecture classes from 70M to 6.9B parameters, strengthening with scale, and more weakly in a vision transformer. Only ~39 of 128 directions are reproducible across minibatches, and averaging cannot recover the rest: under N-fold averaging the gradient's spectral tail shrinks as N^(-1/4) rather than the N^(-1/2) of pure noise, so no averaging budget makes the subspace well defined. What helps instead follows from treating each refresh as a change of coordinates for Adam's state. Carrying the second moment blindly is provably about (r-k*)/2 worse than the best rotation-blind estimator, while the first moment transports exactly through the rotation, the optimal linear map under isotropic gradients and the rule LDAdam uses. At 1B over 40k steps (3 seeds), full LDAdam reaches 18.7 perplexity at beta2=0.999, beating untransported GaLore after its best beta2 fix (19.3); shortening the second-moment memory to beta2=0.99 helps the refreshing optimizers, though for canonical GaLore the effect is small and a full-rank control reverses it. One measurable fact, subspace non-identifiability, clarifies why GaLore works, which patches work, and what to check before trusting a low-rank assumption: the reproducible rank k*.

---


### 82. [i-EXAM: Instructable and Explainable Attack Connectivity Graph Modeler](https://arxiv.org/abs/2607.05888)

**<font color=#1a73e8>作者：</font>** Rakesh Podder, Wadia Ganim, Sarath Sreedharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> i-EXAM is a planning-powered tool that helps system administrators to create security profiles of complex networks and perform what-if analyses to identify network hardening strategies. It leverages planning compilation that provides soundness and completeness guarantees to identify attack paths, evaluate security metrics, generate diverse hardening strategies, and explain these strategies in natural language using Large Language Models.

---


### 83. [Few-Medoids: An Embarrassingly Simple Coreset Selection Method for Few-Shot Knowledge Distillation](https://arxiv.org/abs/2607.05891)

**<font color=#1a73e8>作者：</font>** Cemil-Andrei Dilmac, Florinel-Alin Croitoru, Radu Tudor Ionescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coreset selection aims to identify a small and highly representative subset of a massive dataset for efficient model training. The problem remains challenging even in the few-shot knowledge distillation (KD) setup, where a full-scale pre-trained teacher informs the student network. Typical sample selection strategies often struggle to surpass the random selection baseline. In this paper, we showcase few-medoids, an embarrassingly simple coreset selection strategy that chooses the samples closest to the centroid (average image) of each class. We present extensive KD experiments on four datasets, covering a wide range of image classification problems, and three teacher-student model pairs, comprising both convolutional and transformer networks. Although the proposed method is embarrassingly simple, our empirical results indicate that few-medoids is able to consistently surpass the random selection baseline, as well as the other coreset selection strategies. We therefore consider that few-medoids can be used as a drop-in replacement for commonly-used baselines (e.g. herding or k-center Greedy), in future research on coreset selection. To reproduce the reported results, we publicly release our code at this https URL.

---


### 84. [Auditing of Unlearning Algorithms](https://arxiv.org/abs/2607.05898)

**<font color=#1a73e8>作者：</font>** Sahasrajit Sarmasarkar, Anastasia Koloskova, Sanmi Koyejo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating whether unlearning algorithms truly remove training data influence remains an open challenge. We propose a practical auditor that computes data-dependent lower bounds on the unlearning parameter $\varepsilon$ using membership inference attacks. Evaluating multiple unlearning algorithms, we find a sharp separation: algorithms with rigorous guarantees, such as model clipping and rewind-to-delete, achieve very small $\varepsilon$ bounds that do not falsify their unlearning guarantees, whereas empirical methods such as Hessian-based unlearning, interleaved ascent-descent, ascent on the forget set, and fine-tuning on the retain set exhibit large bounds, indicating poor unlearning. Our auditor provides a practical tool for empirically falsifying unlearning claims through a hypothesis-testing framework, and we validate it on CIFAR-100 and Shakespeare text.

---


### 85. [Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking](https://arxiv.org/abs/2607.05901)

**<font color=#1a73e8>作者：</font>** Manning Gao, Tingyi Liu, Leheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic depression detection using audio-visual data faces significant challenges, particularly in disentangling overlapping feature distributions and establishing robust decision boundaries. To address this, we propose a fine-grained multimodal framework featuring a temporal encoder and a mutual transformer to facilitate deep cross-modal fusion. Our core contribution is the Binary Advantage-weighting Ranking Loss, which optimizes the latent space distribution through two complementary mechanisms: Advantage-weighted Separation, which mines hard pairs by computing a pairwise prediction difference matrix and dynamically weighting them based on their difficulty; and Advantage-weighted Compactness, which minimizes intra-class variance to force features to cluster around their respective class centers. Extensive experiments on D-vlog and LMVD demonstrate that our model reconstructs the latent ordinal structure by prioritizing hard pairs, thereby achieving state-of-the-art performance.

---


### 86. [K-ABENA: K-Adaptive Backpropagation with Error-based N-exclusion Algorithm : (Compensated Loss-Based Sample Exclusion with Unbiased Gradient Estimation)](https://arxiv.org/abs/2607.05903)

**<font color=#1a73e8>作者：</font>** Jean-Francois Bonbhel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present K-ABENA (K-Adaptive Backpropagation with Error-based N-exclusion Algorithm), a selective gradient computation framework that reduces per-iteration training cost by excluding a fraction of low-loss ("minor") observations from the backward pass. Its canonical form (v3) combines a defensive-mixture sampling design over the minor set with Horvitz-Thompson inverse-probability reweighting, yielding a design-unbiased Horvitz-Thompson gradient estimator (Lemma 2) and whose self-normalized practical variant carries a bias of order O(1/m) with an explicit constant (Lemma 3). We prove an O(1/sqrt(T)) non-convex convergence guarantee for SGD under the estimator, with an additive term that quantifies the residual bias (Theorem 1). We further prove that uncompensated loss-based selection - a family that includes OHEM, SBP, and the two earlier K-ABENA variants - admits no stationary point at any minimizer where its selection bias is bounded away from zero (Proposition 2), and we quantify this failure empirically: at 0.17% class imbalance, uncompensated variants reach test AUC 0.53-0.62 versus 0.9998 for full-batch SGD, while the compensated estimator attains 0.9991 at identical 28.4% compute savings. On real datasets (Breast Cancer, Digits, Wine, Diabetes) the compensated estimator is statistically indistinguishable from full-batch SGD (paired permutation tests, p >= 0.5; Section 7) while saving 28-54% of per-epoch gradient computation. A biased "regularized mode" (the earlier half-domain variant) is retained as an option with a proven exact bias decomposition (Lemma 5) and quantified contraindications: it collapses to 0.386 accuracy under 40% label noise (baseline: 0.832) and to 0.53 AUC under extreme imbalance. Every advantage and every limitation reported in this paper is either proved or measured; all experiments are CPU-scale (NumPy/scikit-learn) and their scope is stated explicitly.

---


### 87. [Drift Happens: An Empirical Study of Neural Architecture Robustness to Temporal Distribution Shift](https://arxiv.org/abs/2607.05908)

**<font color=#1a73e8>作者：</font>** Robin Holzinger, Riccardo Colletti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world data distributions evolve over time, inducing temporal distribution shift that can substantially degrade the reliability of deployed machine learning systems. However, the extent to which architectural choices and their associated inductive biases affect temporal robustness remains insufficiently understood.
We present a systematic empirical comparison of temporal robustness across three heterogeneous, time-indexed domains encompassing image classification, multi-label text classification, and text regression tasks. Using a unified evaluation framework based on temporal drift matrices, we train models on cumulative historical data and evaluate their performance on both earlier and later time periods, thereby quantifying cross-temporal generalization. Our study spans model families ranging from simple multilayer perceptrons and convolutional networks to recurrent networks and pretrained Transformer-based encoders.
Collectively, the results show that architectural inductive biases systematically shape temporal robustness: models whose inductive biases lead them to exploit localized, highly discriminative features attain the highest in-distribution accuracy, yet those features are often the ones that change most over time, so these models degrade fastest, while pretrained encoders that draw on coarser, more stable representations drift more gradually. These observations offer practical guidance for selecting architectures for real-world systems subject to temporal drift.

---


### 88. [PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails](https://arxiv.org/abs/2607.05910)

**<font color=#1a73e8>作者：</font>** Mingyang Song, Luxin Xu, Haoyu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image guardrails are typically trained and evaluated under a fixed safety policy, implicitly treating safety as an intrinsic property of an image. Real deployments are different: the same image may be allowed in one product, restricted in another, and newly disallowed when a policy boundary changes. We study policy-adaptive image guardrailing, where a model must decide whether an image violates the currently supplied policy and generalize to held-out policy definitions. We introduce PolicyShiftBench, a comprehensive benchmark with 2,000 policy-discriminative instances over 265 images, where each image is paired with 7.55 policy-conditioned prompts on average to test whether models adapt to the active policy rather than relying on image-level safety priors. We then propose PolicyShiftGuard, a compact policy-conditioned guardrail trained with a two-stage training recipe that combines Randomized Policy SFT (RP-SFT) with Boundary-Pair Policy Adaptation (BP-Adapt). BP-Adapt trains matched prompts for the same image and risk category using standard label supervision and a pairwise comparison loss that separates blocking policies from passing policies. Experiments show that existing VLMs and specialized guardrails remain brittle under policy shifts, while PolicyShiftGuard substantially improves policy-sensitive performance. The 7B model achieves SOTA performance of 76.9 Avg. F1 and 72.1 Avg. PSS on PolicyShiftBench, transfers well to UnSafeBench and SafeEditBench, and improves the latency-performance trade-off with a concise output format. Ablations confirm that matched pass/block boundary pairs are essential for stable policy adaptation.

---


### 89. [Progressive Reasoning with Primitive Correction for Compositional Zero-Shot Learning](https://arxiv.org/abs/2607.05911)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Haoyan Shi, Sunhan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional Zero-Shot Learning (CZSL) aims to combine known attributes and objects as primitives for recognizing previously unseen attribute-object pairs. Prior works either predict attributes and objects independently, missing their strong contextual dependency, or use unidirectional conditional modeling (e.g., object-guided attribute prediction), which is prone to error propagation. We propose PRPC, a Progressive Reasoning framework with Primitive Correction, which explicitly models the bidirectional dependency between attributes and objects via step-wise inference. PRPC performs mutual correction of primitives to suppress prediction errors in earlier steps. Specifically, we formulate CZSL as structured, Q&A-style Chain-of-Thought reasoning process and constrain the MLLM to follow predefined semantic steps to generate intermediate decisions. To further enhance the reliability and logical consistency of intermediate reasoning, we introduce reinforcement learning post-training with a GRPO-based objective, providing step-level rewards aligned with the progressive inference procedure. Extensive experiments on three CZSL benchmarks demonstrate that PRPC achieves state-of-the-art performance, validating the effectiveness of progressive reasoning and bidirectional correction for robust compositional generalization.

---


### 90. [Reproducible Validation of Voucher-Based L2 Interoperability: Diagnosing an ERC-4337 Compatibility Issue in an EIL SDK Implementation](https://arxiv.org/abs/2607.05914)

**<font color=#1a73e8>作者：</font>** Cheng-En Lee, Yu-Chien Huang, Yun-Cheng Tsai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ethereum Layer-2 (L2) ecosystems improve scalability but also fragment users, liquidity, gas funding, and execution across rollups. Consequently, cross-rollup interoperability is not only a bridging problem but also a wallet, execution, and validation problem. Ethereum Interop Layer (EIL) proposes a voucher-based architecture in which users create voucher requests on an origin chain and redeem XLP-signed vouchers on a destination chain. When reproducing the evaluated SDK version in a controlled local environment, we observed a compatibility issue in the \texttt{UserOperation} path: paymaster-related data can differ after signing, preventing a stable comparison between the user-authorized representation and the representation later inspected by the local validation flow.
This paper presents a reproducible two-L2 validation framework and a controlled compatibility mitigation for that issue. We build a deterministic local testbed over Arbitrum- and Optimism-style development chains, deploy the core paymaster and bridge-related components, implement mock bundlers and event-driven XLP providers, and introduce a sanitized paymaster-data handling path together with a compatible multichain account wrapper. Using this framework, we execute the core voucher lifecycle from request creation to destination-chain voucher redemption and asset release.
The contribution is an empirical diagnosis of an implementation-level compatibility barrier, a bounded mitigation that restores controlled end-to-end execution, and an inspectable validation artifact for studying voucher-based interoperability. The work does not claim a new interoperability protocol, universal wallet compatibility, or production readiness; it identifies the remaining gaps toward standard-account validation, one-signature multichain authorization, and full dispute-settlement support.

---


### 91. [PCBWorld: A Benchmark Environment for Engine-Grounded PCB Design Automation](https://arxiv.org/abs/2607.05915)

**<font color=#1a73e8>作者：</font>** Hyungseok Song, Junseok Park, Won-Seok Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> PCB routing is the task of connecting the nets of a board with copper traces under strict design rules, yet learning-based methods still lag behind rule-based routers. We introduce PCBWorld, an open-source engine-grounded PCB routing environment built on the KiCad EDA engine. As a human engineer does, agents in PCBWorld interactively route a board through the engine's native operations, using its Design Rule Check (DRC) feedback to keep the routing within the design rules. The environment supports both RL policies and tool-using LLM agents. Alongside the environment, PCBWorld-Bench provides three dataset families in KiCad's native board format (.kicad_pcb), covering two types of controllable synthetic instances and 679 real open-source boards. It scores any completed board with eight engine-checked evaluation metrics, regardless of the routing method. In our experiments, agents in PCBWorld consistently outperformed grid-action RL policies and open-loop LLM baselines, and an RL policy trained only on synthetic boards transferred zero-shot to real boards, approaching rule-based routers. These results position the engine-grounded, interactive approach of PCBWorld as a promising foundation for advancing the routing ability of both RL and LLM agents.

---


### 92. [LibFHE: A Numba-Based CUDA-Python Library for Non-RNS CKKS-BGV Fully Homomorphic Encryption on GPUs](https://arxiv.org/abs/2607.05920)

**<font color=#1a73e8>作者：</font>** John Chiang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> It has been a decade since the fourth-generation FHE framework, CKKS, was proposed; yet, there is still no indicator pointing toward a fifth-generation successor; and in recent years, numerous studies have explored GPU acceleration to improve the efficiency of homomorphic computations. In this paper, we propose LibFHE, a high-performance GPU-accelerated framework that features CUDA-Python bindings to achieve both high-level programmability and bare-metal GPU performance for homomorphic workloads. A large majority of state-of-the-art implementations adopt the RNS-CKKS variant. In contrast, this work deliberately revisits the original (non-RNS) CKKS-BGV framework, and develops a GPU-based implementation along with corresponding optimizations. Experimental results demonstrate that optimized CUDA-Python implementations can achieve performance comparable to highly optimized C++ FHE libraries, while significantly reducing implementation complexity and improving programmability.

---


### 93. [From Regression to Prior-Aware Inference: Solving the ILWE Family in Randomness Leakage Attacks against ML-DSA](https://arxiv.org/abs/2607.05921)

**<font color=#1a73e8>作者：</font>** Peiheng Zhang, Yuejun Liu, Wei Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ML-DSA is a representative lattice-based signature scheme standardized by NIST. It relies on signing randomness and rejection sampling to ensure that released signatures are statistically independent of the secret key. Practical implementations, however, may leak partial information about this randomness, and such leakage can transform public signatures into ILWE-type problems, resulting in secret key disclosure risks.
Such randomness leakage attack can be formulated as a two-stage key-recovery procedure, in which leaked partial information and public signatures are first transformed into an ILWE-family instance, and then a recovery solver is applied to recover the secret key. Existing work has mainly focused on the first stage by constructing such instances under different leakage models. By contrast, the role of solver in the subsequent instance-solving stage remains under-explored, and existing attacks often rely on ad-hoc model-specific solvers. To address this gap, we propose a unified framework to systematically evaluate different recovery solvers on leakage-derived ILWE-family instances. The framework covers three ILWE instances, including the ordinary ILWE, Fiat-Shamir ILWE (FS-ILWE) and Concealed ILWE (CILWE) under different scenarios.
Within our framework, we explore three classes of solvers. Our experiments show that the solver has a significant impact on the secret-key recovery efficiency. In particular, on FS-ILWE, prior-aware discrete-inference reduces the number of informative relations by one to two orders of magnitude compared to the baselines: Compared with OLS, BP constitutes a reduction by a factor of 15.4x-64.9x in noise-free settings, and by a factor of 10.5x-73.9x in noisy settings. Overall, this work provides a systematic evaluation on different solvers in randomness leakage attacks, and presents new benchmarks for future analysis on ML-DSA.

---


### 94. [NegROI: Click-Centric Uncertainty-Guided Refinement with Scene-Conditioned Negative Prompts for Robust Interactive 3D Segmentation](https://arxiv.org/abs/2607.05955)

**<font color=#1a73e8>作者：</font>** Shuheng Zhang, Feng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive 3D segmentation aims to extract object masks in point clouds with minimal user clicks. Despite recent progress, most existing approaches still struggle with (i) coarse voxel resolution that blurs fine boundaries under limited clicks and (ii) hard false positives caused by confusing background structures. These issues are exacerbated by density and scale shifts across datasets (e.g., dense RGB-D reconstructions vs. sparse LiDAR scans), where fixed refinement heuristics and purely click-driven decoding generalize poorly. To address them, we propose NegROI -- a novel transformer-based interactive framework that couples click-centric multi-resolution refinement with scene-conditioned negative prompts. Given a coarse voxel prediction, it refines only a local Region Of Interest (ROI) around the current click on a finer grid and fuses refined logits back to the coarse mask. To improve robustness and efficiency, we introduce uncertainty-driven selective refinement that prioritizes ambiguous regions. Meanwhile, we model hard background patterns via a set of scene-conditioned negative prompts obtained by cross-attention over scene tokens. We further stabilize these prompts with a diversity regularizer. Finally, we propose boundary-aware hard negative mining to supervise negative-prompt attention toward boundary-proximal, high-confidence false positives. Our experiments on common benchmark datasets (i.e., ScanNet, S3DIS, and KITTI) demonstrate improved click efficiency and reduced false positives, with stronger cross-dataset robustness than the state-of-the-art baselines.

---


### 95. [Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments](https://arxiv.org/abs/2607.05964)

**<font color=#1a73e8>作者：</font>** Ivan Porupski, Branimir Dropuljić, Nikola Ljubešić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Filled pauses (FPs) are a universal feature of spontaneous speech, yet most studies rely on small, single-language corpora, limiting the generalisability of their findings. We analyse ~4,000 hours of parliamentary speech across four related Slavic languages (Croatian, Czech, Polish, Serbian). FP occurrence is obtained via transformer-based automatic detection, while FP rate is modelled using Generalised Estimating Equations (GEE) with Mundlak correction to distinguish within- from between- speaker effects. We replicate a negative association of age and speech rate with FP rate, but find that gender effects are language-specific and directionally opposite to most prior literature. Novel analyses of sentiment, political orientation, and power status reveal a consistent positive association between sentiment and FP rate, alongside parliament-specific modulation by orientation and power status, with opposition speakers tending toward lower FP rates than governing coalition speakers.

---


### 96. [Decoupled Single-Mask Annotation Noise Detection via Cross-Sectional Patch Self-Consistency](https://arxiv.org/abs/2607.05965)

**<font color=#1a73e8>作者：</font>** Yinheng Zhu, Xiaowei Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vascular computed tomography datasets are commonly annotated only once per scan, yielding the pervasive yet under addressed problem of single mask annotation noise. Existing solutions either require costly multirater fusion or are coupled with network training, preventing explicit auditing of where and why labels fail. We introduce a decoupled framework for single-mask annotation noise detection that leverages cross-sectional patch self-consistency to produce interpretable and auditable noise evidence. Tubular anatomy exhibits strong cross-sectional recurrence: patches extracted orthogonally along vessel centrelines recur in appearance across locations and subjects. Thus, anatomically similar patches should have consistent masks, and disagreement signals unreliable annotation. Our method samples cross-sectional patches, retrieves intensity-equivalent neighbours via scalable vector search, and computes a patch-level noise score from statistical mask disagreement, yielding explicit image-mask evidence for every flagged region. Aggregating scores produces scan-level quality maps for dataset quality assessment or quality-weighted training. Experiments on the coronary CT dataset validate the detected noise for improving training robustness and reveal systematic annotation biases. Specifically, transverse and oblique vessels exhibit 5.1 times higher error rates than axis-aligned structures, with additional correlations to cross-sectional area and intensity. Code is available here.

---


### 97. [InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost](https://arxiv.org/abs/2607.05968)

**<font color=#1a73e8>作者：</font>** Krittanon Kaewtawee, Petmongkon Pornpichitsuwan, Natchaya Temyingyong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Matching influencers (KOLs) to free-form, multi-part Thai marketing criteria is today served either by keyword search over structured profiles, which misses semantic fit, or by prompting frontier LLMs over every candidate, which is accurate but slow and expensive. We present InfluMatch, a low-cost three-stage cascade -- retrieval $\rightarrow$ rerank $\rightarrow$ reason -- built entirely from small open-weight models: dense retrieval returns 50 candidates, a 4B pointwise reranker scores each by the log-probability of a single Yes token and keeps 10, and a 4B reasoner grades the shortlist per criterion on a rubric with a Thai rationale. The cascade is designed for cost: reasoning over a filtered top-10 halves token spend versus reasoning over all 50 while scoring 14 points higher. End-to-end against human relevance labels on an 11-query set with all 50 candidates labeled, the full cascade reaches 94.1% P@5, versus a retrieval-only baseline near random; it matches the frontier model Kimi-K2.6 (91.8%) while emitting ${\sim}35\times$ fewer output tokens and serving a 50-KOL query in ${\sim}20$ s on one A100. Notably, the only fine-tuning that pays off is pairwise: a SimPO-tuned reranker matches the frontier baseline's best-pick accuracy (78.0 EM), whereas fine-tuning the reasoner on pointwise per-criterion labels improves offline scores yet degrades end-to-end ranking -- an inversion we trace to the design of the absolute labeling task -- leaving the untuned base model as the strongest deployed reasoner. The result is a deployable, explainable KOL search system at a small fraction of frontier serving cost.

---


### 98. [Learning Sparsest Linear Causal DAGs with Latent Confounders via Higher-Order Cumulants](https://arxiv.org/abs/2607.05984)

**<font color=#1a73e8>作者：</font>** Ming Cai, Hisayuki Hara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering the exact directed acyclic graph (DAG) in linear non-Gaussian acyclic models with latent confounders (LvLiNGAM) remains a challenging problem. Although LvLiNGAM is identifiable only up to an observational equivalence class, each equivalence class is characterized by a unique sparsest DAG. Recovering the sparsest DAG from finite samples, however, remains difficult. Although existing methods are asymptotically consistent, they do not provide an explicit finite-sample procedure for recovering the unique sparsest DAG, nor do they handle models with an arbitrary number of latent confounders.
In this paper, we propose a finite-sample method for recovering the sparsest DAG without imposing any restriction on the number of latent confounders. Simulation studies and real-data analyses demonstrate that the proposed method achieves superior finite-sample performance compared with existing approaches.

---


### 99. [SpecTrack: Spectral Prompt Guided Adaptive Experts for Multispectral Object Tracking](https://arxiv.org/abs/2607.05988)

**<font color=#1a73e8>作者：</font>** Xingyu Tan, Yunrong Qin, Mengjie Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral image(MSI) and hyperspectral image(HSI) object tracking object tracking exploits recorded band-wise observations to improve target--background discrimination under similar RGB appearance, mixed pixels, illumination variation, occlusion, and clutter. However, existing trackers commonly process all search regions through a fixed capacity spectral--spatial path, ignoring that tracking difficulty varies substantially across frames and target states. Clear regions may require only lightweight local discrimination, whereas ambiguous boundaries and spectrally similar distractors often demand stronger contextual reasoning. To address this limitation, we propose SpecTrack, a spectral--spatial complexity-aware tracker that formulates MSI tracking as search-region-level adaptive capacity allocation. Its core component, the Spectral Adaptive Mixture-of-Experts (SAMoE) module, provides a capacity-ordered expert pool with progressively increasing latent rank, receptive field, and depth. Expert selection is guided by a Spectral Prompt Router, which fuses semantic context, spatial boundary cues, and a latent channel-variation cue computed after multispectral patch embedding to activate a sparse subset of SAMoE experts for each search region. In parallel, a Shared Global Expert supplies common latent spectral--spatial context to reduce fragmented sparse-routing decisions. Experiments on MUST, MSITrack, and HOTC20 demonstrate a favorable accuracy--efficiency trade-off. The accuracy-oriented SpecTrack-L384 achieves state-of-the-art or highly competitive AUCs of 65.2\%, 51.9\%, and 72.6\% on the three benchmarks, while the balanced SpecTrack-B224 reaches 62.4\% AUC at 43.7 FPS on MUST. An additional GOT-10k evaluation indicates RGB-domain architectural generalization, with SpecTrack-L384 achieving 79.3\% AO.

---


### 100. [ProvICS: A Provenance-based Intrusion Detection for Industrial Control Systems](https://arxiv.org/abs/2607.05989)

**<font color=#1a73e8>作者：</font>** Md Neyamul Islam Shibbir, Deepak K Tosh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The convergence of Information Technology and Operational Technology has exposed Industrial Control Systems (ICS) to multi-stage cyberattacks that traverse software, network, and physical process layers simultaneously. Although Provenance-based Intrusion Detection Systems (PIDS) are effective in Information Technology (IT) environments, their applicability to Industrial Cyber-Physical Systems (CPS) remains largely unexplored because of the absence of datasets that jointly capture host-level causal behavior, industrial network semantics, and physical process state. To address this gap, we design an open-source, Hardware-in-the-Loop (HIL) CPS testbed that replicates an industrial chemical reactor control architecture across the Purdue model layers. Using this testbed, we propose ProvICS, a multimodal provenance dataset purpose-built for CPS intrusion detection, which synchronously captures four streams: whole-system provenance graphs from the supervisory host and the resource-constrained PLC, decoded Modbus deep-packet inspection records, and physical process telemetry. The collection comprises a 48-hour benign phase and a 22-hour attack phase across four campaigns covering 20 ICS ATT&CK techniques over 32 attack events, ranging from reconnaissance to physical process manipulation. Comparative analysis shows that ProvICS is among the few existing ICS/CPS benchmarks with multi-host kernel-level provenance, real PLC hardware-in-the-loop execution, decoded Modbus traffic, physical process-state measurements, and auxiliary raw PCAP traces in a time-synchronized collection. Baseline detection further confirms that cross-modal fusion can detect all 32 labeled attack events (F1 = 0.913, false-positive rate (FPR) = 1.40%), demonstrating the dataset's ability to expose complementary attack signals across modalities and addressing a gap not covered by prior benchmarks.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-195](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
