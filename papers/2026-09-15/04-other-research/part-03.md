# 📦 其他研究 | 2026年09月15日

> 本类共 **201** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-201](./part-05.md)

---

### 101. [$\text{GSF-}χ$: Global Stereochemical Fields for Chiral Graph Transformers](https://arxiv.org/abs/2609.12532)

**<font color=#1a73e8>作者：</font>** Jiaqing Xie, Yuxin Wang, Xipeng Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enantiomers share atoms, bonds, and pairwise distances yet can behave differently in chiral environments, so molecular encoders must respect atom relabelings and proper rotations without becoming blind to reflection. We introduce GSF-$\chi$, a graph transformer in which stereogenic units modulate all pairwise interactions rather than single out one atom as special. Each central or axial stereogenic unit creates a reflection-even phase field over all atoms, a handedness pseudoscalar $\chi$ sets the direction of a relative rotation on latent query--key blocks, giving a \textbf{Chiral-RoPE} that reflection inverts rather than leaves fixed. A $C_2$ projection separates mirror-even ECD peak counts and positions from mirror-odd peak signs. We prove the operator's even--odd decomposition and its annotation-inversion, permutation, and unit-order identities under explicit canonical-role conditions; property tests and a coordinate-reflection audit verify the laws end to end. GSF-$\chi$ leads every central-ECD output and improves axial Rotation and Symbol by $12.6\%$ and $7.9\%$ over the strongest baseline. Equal-budget controls attribute the Rotation advantage to global signed support rather than parameter or edge count; the $C_2$ projection yields exact enantiomer-pair consistency at a small raw-accuracy cost under complete supervision and becomes predictive when mirror supervision is scarce.

---


### 102. [Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541)

**<font color=#1a73e8>作者：</font>** Mengzhao Jia, Yang Lin, Xixin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We demonstrate that a general-purpose agent can directly drive a physical robot throughout task execution without any task-specific or environment-specific training. We introduce Agent as Policy (AGP), which places task planning and execution under the agent's control. Given a task and a robot interface, the agent interprets visual evidence, writes executable programs, issues motion commands, and revises its actions in response to physical outcomes. This brings the agent's reasoning and programming capabilities into continuous interaction with the physical world. We study AGP across multiple real-world manipulation tasks spanning precision manipulation, dynamic motions, and deformable objects. These include assembly from human videos, block construction from goal images, die reorientation, targeted throwing, and bimanual towel folding. AGP achieves success rates of 100%, 100%, and 80% on three block construction configurations. These findings establish a path for general-purpose agents to act as robotic policies, extending their autonomy to physical manipulation through runtime reasoning, programming, and interaction.

---


### 103. [Meddies-PII: A Multilingual Framework for Personally Identifiable Information Extraction in Clinical De-identification](https://arxiv.org/abs/2609.12544)

**<font color=#1a73e8>作者：</font>** Linh Uyen Le, Christian Hoang, Huy Hoang Ha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical de-identification relies on accurately identifying personally identifiable information (PII). However, manually annotated datasets are costly to construct, while existing synthetic alternatives often provide limited details about their generation process or rely on relatively simple synthesis strategies. We introduce Meddies-PII-Dataset, a corpus of one million synthetic clinical documents spanning seventeen languages and nine PII labels. The documents are generated using attribute-conditioned prompts and validated through thirteen deterministic gates that enforce structural and annotation consistency. To evaluate the dataset's utility, we train Meddies-PII-Model, a BIOES token classifier, and compare it with existing PII extraction systems using exact-match entity-level F1. Meddies-PII-Model achieves the highest performance among the evaluated systems on all reported benchmarks, with a mean F1 of 0.827 across fifteen external benchmarks, compared with 0.658 for the strongest baseline. Upon acceptance, we will publicly release the dataset, benchmark suite, model, generation framework, and evaluation code to support research on multilingual clinical de-identification.

---


### 104. [Omniscience for the Masses: New Threats in the Metaverse's Democratized World Creation](https://arxiv.org/abs/2609.12554)

**<font color=#1a73e8>作者：</font>** Andrea Mengascini, Ryan Aurelio, Jason Polakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Metaverse platforms increasingly derive their success from user-generated virtual worlds: self-contained social and interactive environments, which can be created by any ordinary user and scale to billions of visits. Platforms such as Roblox, Horizon Worlds, and VRChat now host millions of creator-built worlds that govern how users see, hear, and interact with one another. While this model enables rapid growth and creativity, it fundamentally delegates control over social interactions and world behavior to untrusted users. In this paper, we present the first systematic security and privacy assessment of metaverse world creators. We survey 25 platforms that support user-created worlds and analyze their world-creation capabilities. Guided by this analysis, we design and implement five novel attacks that exploit creator-provided tools to violate spatial, visual, and auditory constraints in immersive environments, enabling covert user surveillance and manipulation without software vulnerabilities or developer-level privileges. We further show that five previously-proposed attacks can be replicated using only standard world-creation features. Finally, we find that existing platform vetting, runtime protections, and creator policies are insufficient to mitigate malicious world-creator behavior, revealing a fundamental mismatch between users' privacy expectations and the powers granted to world creators.

---


### 105. [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)

**<font color=#1a73e8>作者：</font>** Lanke Frank Tarimo Fu, Maurice Fallon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration. Given query images and a reference 3D point cloud, the model predicts the scan pose and point map alongside the poses and point maps of each camera, all expressed in the first camera's frame. It additionally predicts a coarse-to- fine pyramid of per-point and per-pixel features for direct reprojective alignment of the scan to the first image. This formulation unifies downstream tasks such as camera-LiDAR calibration in autonomous driving and indoor camera-to-map relocalization. A single DRS-VPT model achieves state-of-the-art performance for image-to-LiDAR registration in autonomous driving, competitive indoor relocalization without training map-specific weights, and strong zero-shot transfer to unseen environments. We also show qualitatively that the model learns complex scan-to-image projection properties such as occlusion of back-facing points.

---


### 106. [KAD-Net: Kinematics-Aware Decoupled Learning for Robust 3D Hand Pose Estimation from a Single Depth Image](https://arxiv.org/abs/2609.12559)

**<font color=#1a73e8>作者：</font>** Jun Lu, Zhenming Chen, Lin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the complexity of hand kinematics and self-occlusion, existing 3D hand pose estimation methods based on single depth images struggle to comprehensively model the topological dependencies among hand joints. Furthermore, traditional hierarchical multitask architectures enforce a shared feature space for both 2D joint localization and depth estimation, which can induce mutual interference. To address these challenges, we propose a Kinematics-Aware Decoupled Learning Network (KAD-Net) for robust 3D hand pose estimation. Specifically, we first design a Finger Topology Constraint (FTC) module to enhance the representation of distal joints. This module utilizes three consecutive finger joints to construct a local kinematic representation to impose topological constraints, which supplements the kinematic features of the distal joints. The FTC module leverages the structural context from visible joints to assist in locating occluded distal joints, thereby improving robustness to occlusion. Additionally, we propose a task-decoupled hierarchical multitask framework. This framework separates 2D joint localization from depth estimation and incorporates a dedicated multitask learning strategy for depth regression, effectively isolating the UV and depth features to mitigate mutual interference and negative transfer. Extensive experiments demonstrate that KAD-Net outperforms existing methods on several benchmark datasets (ICVL, NYU, and MSRA), achieving state-of-the-art accuracy in 3D hand pose estimation. Potential applications of KAD-Net include human-computer interaction, virtual reality and gesture-based control systems.

---


### 107. [TokenMapper: A Step Toward Interoperable Speech Token Translation](https://arxiv.org/abs/2609.12563)

**<font color=#1a73e8>作者：</font>** Tal Kozakov, Tal Rosenwein, Eliya Nachmani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural audio codecs discretize speech into token sequences, but the resulting token spaces differ in vocabulary and codebook structure, preventing direct communication across models. This limitation affects applications such as conversational voice agents and speech to speech translation systems where multiple speech models must interact. As a result, transferring information between speech systems typically requires decoding to waveform audio and re-encoding with a second tokenizer, increasing latency and introducing potential information loss. To address these limitations, we present TokenMapper, a direction aware framework for direct token to token translation between heterogeneous speech tokenizers in the discrete domain. TokenMapper supports structurally mismatched token spaces, including mappings between single codebook and multi codebook representations, under a shared effective token rate. Experiments on GLM-4-Voice, MiMi and DualCodec show consistent cross model performance. Specifically, translation WER approaches native reconstructions within 2.5-6.8% absolute WER, human MOS for TokenMapper outputs ranges from 2.29 to 4.39, following the same direction level trends as UTMOS and end to end latency is reduced by 4.8-94.5% relative to waveform bridging, reaching up to 972 ms per utterance. These results provide a practical step toward cross model speech token interoperability without intermediate waveform reconstruction.

---


### 108. [An Ultra-Widefield Swept-Source OCTA Dataset and a Polar-Gated Mamba Network for Retinal Vessel Segmentation](https://arxiv.org/abs/2609.12574)

**<font color=#1a73e8>作者：</font>** Yang Liu, Yibing Shen, Keming Zhao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-widefield (UWF) swept-source optical coherence tomography angiography (SS-OCTA) enables large-area retinal vascular imaging, yet vessel segmentation at this scale lacks dedicated public benchmarks and comprehensive evaluation for quantitative vascular analysis. We introduce WOIVES, to our knowledge the first publicly available UWF SS-OCTA vessel-segmentation dataset, comprising 206 eyes from 152 participants with a 24x20mm^2 field of view. WOIVES spans emmetropia to high myopia and provides soft probability vessel annotations. We further propose PG-Mamba, a visual state space model that enhances conventional directional scans with two complementary polar-coordinate scan orders. An auxiliary Dynamic FOV Gating module performs spatial modulation at the bottleneck. PG-Mamba outperformed seven competitive approaches on broad segmentation metrics under cross-validation. It achieved the lowest median absolute errors for vessel density, fractal dimension, and vessel length density. WOIVES is publicly available on Zenodo (DOI: https://doi.org/10.5281/zenodo.21904672), and the PG-Mamba code is available at this https URL.

---


### 109. [SCORE: SubDistribution-aware Collaborative Knowledge Reinforcing for Cloth-Hybrid Lifelong Person Re-Identification](https://arxiv.org/abs/2609.12577)

**<font color=#1a73e8>作者：</font>** Kunlun Xu, Liangyu Ma, Jiangmeng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong Person Re-Identification (LReID) aims to train a unified person retrieval model from a non-stationary data stream. Existing LReID methods mainly focus on scenarios where the clothing of each person is consistent. Recently, the Cloth-Hybrid LReID (CH-LReID) where cloth-consistent and cloth-changing data alternately occur, has emerged as a more practical and challenging scenario. Due to the conflict between clothing-relevant and clothing-irrelevant knowledge, the well-known catastrophic forgetting problem is significantly exacerbated in this task. To address this issue, we propose a SubDistribution-aware COllaborative Knowledge REinforcing (SCORE) framework, where our key idea is explicitly modeling the intra-identity diversity to continually consolidate distinct cloth-consistent and cloth-changing knowledge. Specifically, an Adaptive SubDistribution Modeling mechanism is developed, where a set of distributional subprototypes is assigned to each identity to capture the intra-identity diversity, improving the compatibility between cloth-consistent and cloth-changing knowledge. Then, a Distributional Knowledge Reinforcement scheme is introduced, where the knowledge of old distributional subprototypes is retained in the new ones by a collaborative aligning mechanism. Extensive experiments show that our SCORE achieves the state-of-the-art performance.
Our code is available at this https URL

---


### 110. [MicroHasTEE: Bare-Metal Haskell for Type-Level Peripheral Ownership on Armv8-M](https://arxiv.org/abs/2609.12580)

**<font color=#1a73e8>作者：</font>** Robert Krook  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Arm TrustZone for Armv8-M isolates Secure and Non-secure software, but developers must still coordinate peripheral attribution, interrupt routing, initialization, and gateway interfaces across separately built firmware images. Inconsistent assumptions between these images can compile successfully and emerge only as faults on the target device.
We present MicroHasTEE, a multiparty programming framework that expresses both firmware applications as participants in one typed Haskell program. MicroHasTEE represents peripheral authority with type-level capability ledgers and uses indexed setup computations to track resource acquisition, configuration, transfer, and finalization. Domain-specific effect types restrict peripheral operations and interrupt callbacks to the participant that holds the corresponding authority, while typed callable handles describe the Secure services available to Non-secure code. MicroHs compiles the shared program twice to produce separate bare-metal Secure and Non-secure firmware images.
We implement MicroHasTEE for an STM32U5 Nucleo board, including TrustZone configuration, peripheral drivers, and a serialized gateway for cross-domain Haskell calls. For programs expressed through its interface, MicroHasTEE rejects inconsistent resource use, attribution changes after configuration, callbacks in the wrong domain, and calls to unregistered Secure services. A door-lock case study demonstrates feasibility, with firmware images occupying 232.7 KiB and 228.4 KiB of flash and approximately 220 KiB of SRAM per domain.

---


### 111. [NovaFabric: Tamper-Evident, Replayable Evidence for Autonomous AI Agent Runs](https://arxiv.org/abs/2609.12582)

**<font color=#1a73e8>作者：</font>** Mohsen Seyedkazemi Ardebili  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an autonomous AI agent does something consequential, what can be proven about what it did? Agent-observability platforms capture traces, but a trace is mutable: alterable undetected, with no recipe for re-executing it, silent on whether captured secrets were removed. Regulation (EU AI Act, ISO 42001, NIST AI RMF) presumes records an independent party can check.
We present NovaFabric, producing audit-grade execution evidence: provider-neutral, tamper-evident, replayable, shareable. It records an agent run, without modifying agent logic, into a portable Run Capsule (fifteen-entity schema), sealed with a holistic DSSE signature, RFC 3161 timestamp, Merkle log and redaction attestation. Sealed runs are re-executable under a four-mode replay protocol and exportable as an Evidence Bundle for third-party verification with stock tooling (specified, not evaluated). The contribution is integration, not new cryptography: OpenTelemetry, DSSE/in-toto and W3C PROV.
We evaluate eight research questions at measured scope. Mocked replay serves every model response from the capsule (no live model call, 10/10) but is offline w.r.t. models, not the network; only 2/10 tool-using workloads completed; the gap is missing tool-response substitution. Tampering is rejected across three tested classes. Declared-stream completeness is 0.652 (95% CI +/-0.064, ten scenarios). A repaired rule pack redacts 14/14 credential types, preserving 9/9 decoys; diff localises 140/140 mutations. Blast-radius queries: 45.5ms p99 over 10M edges (3.3x faster than a columnar baseline), 167.9ms over 100M (1 client, n=30). A 314-machine, ten-region run finds capsule REST ingest lossless but capped at 61.6 req/s (p99 26.8s) by per-worker serialisation. Six defects found in NovaFabric and its evaluation corpus: four fixed, one withdrawn, one open.
Verification is conditional on a stated trusted computing base.

---


### 112. [Poisson-Corrector Complexity Bounds for Moreau--Yosida Unadjusted Langevin Sampling](https://arxiv.org/abs/2609.12594)

**<font color=#1a73e8>作者：</font>** Yuchen Xin, Zhihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the classical Moreau--Yosida unadjusted Langevin algorithm (MYULA) for $\pi(\,\mathrm{d} x)\propto e^{-f(x)-g(x)}\,\mathrm{d} x$, where $f\in C^2(\mathbb{R}^d)$ is $m$-strongly convex with $L_f$-Lipschitz gradient and $g:\mathbb{R}^d\to\mathbb{R}$ is convex and globally $G$-Lipschitz. For the Moreau-smoothed target $\pi_\lambda$ and the MYULA invariant law $\widehat\pi_{\lambda,h}$, we prove \[
\sqrt m\,W_2(\pi_\lambda,\widehat\pi_{\lambda,h})
=O(h)+\widetilde O(h^{3/4}) \] under $0<h(L_f+\lambda^{-1})\le c$, with only logarithmic dependence on $\lambda^{-1}$ in the error coefficients. Combining this estimate with the Moreau approximation bias yields $\widetilde O(\varepsilon^{-4/3})$ iterations to achieve $\sqrt m\,W_2(\mu_N,\pi)\le\varepsilon$, for fixed model parameters and initialization. The proof combines a discrete Poisson corrector with active-trace estimates and a shared-noise bound for the exact--Euler two-point curvature.

---


### 113. [SIMS: Scale-Invariant Merit-Function-Based Scalarization for Multi-Task Learning](https://arxiv.org/abs/2609.12599)

**<font color=#1a73e8>作者：</font>** Zebin Chen, Fei Xing, Yang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) requires navigating unavoidable trade-offs among competing objectives. This paradigm is frequently formulated as multi-objective optimization (MOO), where the scalarization is favored to reduce an MOO problem to a single objective. We empirically find that existing merit-function-based scalarization approaches are sensitive to the relative scales of different objectives in practical MTL, where task losses commonly differ by orders of magnitude. The optimization process often favors objectives with larger scales even though the underlying Pareto optimal solutions remains invariant to rescaling (i.e., multiplying an objective by a positive constant). To address this issue, we propose Scale-Invariant Merit-function-based Scalarization (SIMS) for MTL. Specifically, SIMS adopts a transformation-induced merit function to convert the MOO problem of MTL to a single objective that renders optimization invariant to the magnitudes of losses. Theoretically, we prove that the requirement for scale invariance uniquely determines this transformation to be logarithmic. We further show that this general transformation-induced merit function preserves weak Pareto optimality and admits a smooth surrogate with controllable approximation error. Extensive experiments on representative multi-task benchmarks demonstrate that SIMS consistently outperforms existing scalarization methods and achieves state-of-the-art performance.

---


### 114. [A Feature-Rich Embedded NIDS with eBPF/XDP: Detector and Architecture Trade-offs](https://arxiv.org/abs/2609.12605)

**<font color=#1a73e8>作者：</font>** Shiqi Wu, Oleksii Koshovyi, Georgios Pseiridis Pseiras 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed Denial-of-Service (DDoS) attacks remain a serious threat to transport networks, with recent attack volumes exceeding 30 Tbps, and the telecommunications industry being the main target. Recent work has yet to study the impact of the hosting software architecture on network monitoring solutions, or to assess recent algorithms for improving attack detection. This paper presents a Network Intrusion Detection System (NIDS) for DDoS detection in transport networks, developed in collaboration with Ericsson. Building on a statistical baseline, we improve detection effectiveness with an Isolation Forest trained on a wider set of flow features, extracted by GoFlowMeter, our open-source Go implementation of CICFlowMeter, and we integrate eBPF/XDP so that the NIDS filters real traffic at the kernel level. We further compare three deployments, monolithic, Kafka-based, and gRPC-based microservices, on a Raspberry Pi 5 testbed replaying the CIC-DDoS2019 dataset as real network traffic. Detection quality is governed mainly by the choice of detector rather than by the transport: the Isolation Forest raises recall and F1 score (0.965 live in the monolithic variant) over the baseline by flagging low-volume attack windows that the baseline misses. The transport is not neutral, however: gRPC reaches almost the same accuracy as the monolithic variant while adding less than 2 milliseconds of transport time per window, whereas the asynchronous Kafka pipeline trails by roughly nine percentage points and adds about 27 milliseconds. These findings clarify the trade-off between detection quality and architectural overhead when deploying a NIDS on resource-constrained hardware.

---


### 115. [Correlation-Guided Fast Machine Unlearning via Hessian Analysis](https://arxiv.org/abs/2609.12620)

**<font color=#1a73e8>作者：</font>** Ayushi Thakur, Ruchir Gupta, Amit Kumar Jaiswal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of machine learning in network and distributed security systems has created an urgent need for mechanisms that can selectively and efficiently remove the influence of specific training data to eliminate compromised or adversarial data points from production models. Privacy regulations such as GDPR's \emph{right to be forgotten} also pose similar requirements. However, existing approximate unlearning techniques remain computationally prohibitive for deployment in real-world security systems, as they require repeated expensive Hessian-inverse-vector computations for each data point removal, creating a bottleneck when processing multiple related requests in scenarios such as intrusion detection systems, spam filters, and threat intelligence platforms. Thus, we introduce a computationally efficient unlearning framework that identifies correlated data points in the training set and applies a theoretically derived closed-form parameter update rule, achieving an $82\times$ wall-clock speedup over standard influence function unlearning while preserving model utility with a $10^{-2}$ improvement in accuracy over state-of-the-art baselines. Our method establishes theoretical guarantees and ensures numerical stability through Hessian damping. Our evaluation across seven diverse dataset architecture combinations, including large-scale CIFAR-100 with ResNet-50, demonstrates superior forgetting effectiveness, with membership inference attack success rates of 0.660 and tug-of-war scores of 0.950.

---


### 116. [RA-SOD: Reliability-Aware RGB-T Salient Object Detection under Modality Degradation](https://arxiv.org/abs/2609.12622)

**<font color=#1a73e8>作者：</font>** Hongbo Gao, Zhengyu Li, Xueru Nie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Thermal (RGB-T) salient object detection leverages complementary cues from visible and thermal modalities to improve robustness in challenging environments. However, in real-world scenarios, the reliability of each modality is inherently unstable: RGB images degrade under low illumination, motion blur, and noise, while thermal imagery often suffers from contrast compression and sensor artifacts. Such degradation introduces unreliable perceptual evidence that can mislead cross-modal fusion and significantly deteriorate detection performance. To address this challenge, we propose RA-SOD, a reliability-aware RGB-T salient object detection framework that explicitly models modality reliability and integrates it into feature learning and cross-modal fusion. First, we introduce a reliability-conditioned representation that adaptively compensates degraded modality features while preserving structural cues. Second, an uncertainty-guided dual-stream refinement strategy progressively corrects cross-modal representations while suppressing unreliable evidence. Finally, we propose a pixel-wise modality competition mechanism that dynamically selects modality cues according to spatial reliability for fine-grained fusion. Extensive experiments on four benchmarks (VT821, VT1000, VT5000, and VT-IMAG) demonstrate that RA-SOD achieves state-of-the-art performance and exhibits strong robustness under severe modality degradation. Code and models are available at this https URL.

---


### 117. [SteerDuplex: Steerable Duplex Speech Dialogue Models](https://arxiv.org/abs/2609.12623)

**<font color=#1a73e8>作者：</font>** Utkarsh Tyagi, Ramaneswaran Selvakumar, Advait Gosai 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models support low-latency turn taking, interruption handling, and backchanneling, yet a key capability remains underexplored: steerability, the ability to reliably shift conversational behavior along attributes such as tone, persona, speaking rate, and voice style in response to user instructions. We introduce a taxonomy of text- and audio-based steerability that identifies substantial gaps in current full-duplex models. To address this gap, we introduce SteerDuplex, a Moshi-based full-duplex speech model fine-tuned on natural conversations and synthetic dialogues targeting instruction following, vocal delivery, reasoning, and duplex interaction. We further apply two-stage reinforcement learning (RL) with hybrid rewards, combining verifiable interaction checks and judge-based semantic feedback to improve timing and response continuity. To evaluate full-duplex spoken steerability, we introduce SteerBench, a benchmark with 390 spoken prompts and 1,067 human-authored binary audio and text rubrics spanning tone, persona, style/accent, and speed/length. On SteerBench, supervised training improves audio-steering average pass rate by 44.5 percentage points over the strongest evaluated open baseline. On Audio MultiChallenge, task average pass rate improves by 7 points over its strongest evaluated open baseline. RL further raises source-clean interruption response from 72.5% to 82.5% and reduces synthetic pause barge-in from 26.5% to 9%. Steering and aggregate task scores remain comparable or higher, while reward probes reveal reward hacking through incomplete responses. Our model and benchmark support systematic research on spoken steerability, with reward analysis showing why timing gains must be evaluated alongside response completeness.

---


### 118. [Subgroup Packing for Batched PASTA Transciphering](https://arxiv.org/abs/2609.12624)

**<font color=#1a73e8>作者：</font>** Mugurel Barcau, Vicenţiu Paşol, George C. Ţurcaş  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With transciphering, a server converts symmetrically encrypted records into homomorphic ciphertexts without learning the records or the symmetric key. For the PASTA cipher, this conversion involves dense linear maps whose implementation depends on how record words are arranged in the ciphertext. We ask whether rearranging a fixed batch can reduce its conversion cost. Instead of storing each record's words in a contiguous block, our layout interleaves records so that cyclic word shifts preserve each record's positions, which form a coset of a cyclic subgroup. For direct evaluation as a sum of masked translations, we characterize the required displacements and relate their counts, 255 for the contiguous layout and 128 for the subgroup layout, to a prior transversal-difference invariant.
We implement three equally batched schedules for complete PASTA-3 conversion and subsequent public subset-sum queries in HElib. Across twelve paired corpora under six homomorphic keys, all 24 direct and subgroup conversions and all 48 subsequent queries return the expected values and required zeroes. The median paired ratio of direct to subgroup server cost is 1.60, including fresh public generation, conversion and two queries. The reduction comes with less remaining noise capacity. These results establish a packing-dependent cost--noise tradeoff.

---


### 119. [Geometric-to-Semantic Spherical Transfer Learning for Cortical Sulci Labeling](https://arxiv.org/abs/2609.12627)

**<font color=#1a73e8>作者：</font>** Saeb Tounsi, Joël Chavas, Pietro Gori 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning on cortical surfaces faces a dilemma: capturing the complex topology of over 60 nomenclature-dependent sulci per hemisphere requires high-capacity models, yet the extreme scarcity of expert annotations ($N=62$ subjects) inevitably causes overfitting. Standard supervised approaches fail to generalize in this data-scarce regime, particularly for variable and small sulci where topological ambiguity is high. To overcome this limitation, we introduce a Geometric-to-Semantic Spherical Transfer Learning framework.
First, we leverage massive unlabeled data (UK Biobank, $\approx$30,000 subjects) to pre-train a spherical encoder using a locally-optimized strategy. By relying solely on continuous surface features (curvature and depth), the relevance of this pre-training is confirmed by the model's ability to detect localized and rare topological traits, such as sulcal interruptions. The downstream labeling task, however, introduces extracted sulcal fundi (lines) as an explicit semantic input. To bridge this dimensional domain gap (from purely geometric to semantic) without causing catastrophic forgetting, these anatomical lines are integrated into the pre-trained backbone via a soft-initialized Topological Prior Injector.
Our experiments demonstrate that this approach outperforms fully supervised baselines trained from scratch, achieving a mean Dice of 0.77. Crucially, a local analysis reveals that the self-supervised geometric priors yield the largest performance gains on variable and tertiary sulci (up to 14.8%), confirming that learning the cortex shape is highly beneficial for identifying its rarest parts.

---


### 120. [Explaining Time Series Forecasting with Horizon-Resolved Attribution](https://arxiv.org/abs/2609.12639)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Jaehoon Lee 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in explaining time series (TS) models have produced methods that identify which past values a prediction depends on. However, most existing methods return a single importance vector, assuming that every predicted step depends on the same past values. In this paper, we show that this assumption does not hold, as different forecast steps depend on different past values. Motivated by this observation, we propose Horizon-Resolved eXplanation (HRX), which adds a horizon axis to the explanation, so that every forecast step receives its own importance map. HRX is a simple yet effective plug-in framework with three components: 1) an estimator that reads these maps out of any differentiable forecaster without modifying the TS backbone, 2) an evaluation protocol that validates the horizon axis by measuring how much a single forecast step changes when the inputs an importance map ranks highest are removed, and 3) a rank criterion that predicts in advance whether the axis is worth resolving on a given TS. We further show that this step-wise dependence is low-dimensional, as the explanations of all steps are built from a few shared maps whose number does not grow with the forecast length. Extensive experiments across various backbones and datasets show that the improvement comes from the horizon axis and holds for estimators of previous explanation methods. Code is available at this https URL.

---


### 121. [Reconstruction and Reflection of Positive Experiences through Resurfacing Laughter-indexed Everyday Moments](https://arxiv.org/abs/2609.12642)

**<font color=#1a73e8>作者：</font>** Jun Fang, Jiajin Li, Yuntao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Positive everyday moments often escape deliberate recording, while continuous self-tracking can generate extensive records that are difficult to revisit. We explore laughter as a naturally occurring, sparse index for constructing contextualized personal records to support later reconstruction and reflection. A formative study with 12 participants characterized laughter as an affective but semantically incomplete index and informed \textit{LaughAnchor}, a mobile and wearable self-tracking system. During participant-initiated recording, the system assembles detected laughter and aligned context into candidate moments for later reconstruction and reflection, with layered context disclosure, user-controlled curation, and near-term and long-term resurfacing. In a three-week field deployment with 12 participants, passive indexing preserved moments they considered unlikely to record deliberately but valued retrospectively. During resurfacing, participants attributed affective re-experiencing to laughter and used additional context both to reconstruct episodes and to explore already-recalled experiences. Across moments and reviews, resurfacing supported rediscovery and broader awareness of relationships, routines, and emotional states. These findings inform self-tracking designs that use sparse affective indices to organize contextual records for reconstruction and reflection, while keeping interpretation and retention under user control.

---


### 122. [Poster: Towards Selecting Threat Appropriate Industrial Intrusion Detection Systems](https://arxiv.org/abs/2609.12646)

**<font color=#1a73e8>作者：</font>** Stefan Lenz, Johannes Weidmann, Martin Henze  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the threat landscape against industrial control systems is dynamic, effective security requires detection strategies capable of timely reactions to these evolving threat situations. To address this problem, we propose the idea of a counter-threat intelligence sharing based mechanism to select appropriate detectors for current circumstances. To highlight the potential of this mechanism, we conduct attack-level performance evaluations of various intrusion detection systems. Results show the variance of intrusion detection performance depending on the attack scenario, emphasizing the benefits of such a mechanism for industrial control system security

---


### 123. [ProactiveBench: Can Streaming Video Models Really Interact Like Humans?](https://arxiv.org/abs/2609.12658)

**<font color=#1a73e8>作者：</font>** Kaixuan Du, Xin Wan, YuKun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires models to process continuous multimodal input while maintaining temporal context. Existing evaluations are predominantly reactive: they query a model at a selected timestamp and therefore do not assess when it should respond. Proactive interaction instead requires monitoring a standing request, responding within an appropriate interval after the target event, and otherwise remaining silent. We introduce ProactiveBench, which evaluates models at one-second stream intervals without an explicit response cue. Its six subtasks vary trigger ambiguity and timing tolerance. Event Sensitivity geometrically combines response and silence rates on the same recording; four window-based subtasks distinguish early, in-window, and missed responses; and Duplicate Counting penalizes omissions and repetitions. Premature responses outnumber missed responses for four of the six evaluated systems, revealing a substantial gap in the temporal decision-making required for human-like interaction.

---


### 124. [Beyond Ambiguous Visual Cues: Studying Physiological Disruptions and Cross-Modal Inconsistencies in Deepfake Videos](https://arxiv.org/abs/2609.12668)

**<font color=#1a73e8>作者：</font>** Chenxi Yang, Yassine Ouzar, Larbi Boubchir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deepfake detection studies increasingly suggest remote photoplethysmography (rPPG) signals as an authenticity cue. However, existing benchmarks lack physiological ground truth, and current detectors underexplore the cross-level relationship between facial features and physiological dynamics, often relying on late fusion or rPPG features alone. In this paper, we construct high-fidelity deepfake manipulations on established real rPPG datasets (COHFACE and UBFC-rPPG) to investigate how forgeries disrupt natural physiological signals and facial behavior at the same time. Building on this analysis, we propose a bidirectional co-attention fusion detector that jointly models rPPG and facial behavior tokens. This mechanism explicitly captures the cross-level dependencies between pulse dynamics and facial motion to learn a robust, joint authenticity representation. Extensive experiments using a subject-disjoint 5-fold evaluation demonstrate the superiority of our approach. Achieving a 92.80\% AUC on constructed datasets using face swapping and 96.78\% AUC on motion transfer, our model outperforms both the rPPG-only single modality baseline and the best feature-level fusion methods. Furthermore, transfer-learning result of the fusion detector on Celeb-DF-v2 while keeping both feature extractors fixed achieves 91.20\% accuracy and 86.08\% AUC, which suggests applicability under target-domain adaptation.

---


### 125. [NOVA-GS: Noise-Aware View-Consistent Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2609.12682)

**<font color=#1a73e8>作者：</font>** Shaurya Pavan A, Vemunuri Divya Madhuri, Yash Pradeep Gawande 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scenes under real-world low-light conditions remains challenging due to severe sensor noise, low signal-to-noise ratios, and degraded photometric consistency, which destabilize geometry estimation and novel view synthesis. Existing approaches often rely on well-lit reference data for reliable Structure-from-Motion (SfM) initialization under degraded inputs or apply per-view enhancement methods that introduce cross-view inconsistencies. To address these limitations, we propose \textbf{NOVA-GS}, a unified noise-aware framework for low-light 3D Gaussian Splatting that subsumes enhancement, denoising, and geometry optimization within a single process. Our method leverages VGGT-based feed-forward estimation to obtain robust camera poses and geometry directly from degraded inputs, eliminating the need for SfM. Building on this initialization, NOVA-GS integrates three coupled components: a structure-aware enhancement module for exposure correction, a self-supervised denoising module with blind-spot masking for pseudo-supervision, and a consistency-driven Gaussian Splatting optimization enforcing cross-view geometric coherence. We further introduce a noise-guided spherical harmonic regularization to suppress view-dependent artifacts in noisy regions. Extensive experiments on diverse real-world low-light datasets demonstrate improved geometric fidelity, color consistency, and robustness without requiring paired supervision or well-lit references. this https URL

---


### 126. [SIFPBPNet: A Dual-Path Network for Wearable and Cuffless Blood Pressure Estimation via Individualized Steady-state Representation](https://arxiv.org/abs/2609.12690)

**<font color=#1a73e8>作者：</font>** Shuailong Tang, Xiaoyu Li, Donglin Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous and cuffless blood pressure (BP) monitoring using photoplethysmography (PPG) is of great interest for low-cost and personalized cardiovascular health management. However, significant population heterogeneity and the "one-to-many mapping" problem, where similar waveforms across individuals correspond to different BP levels, limit the accuracy of conventional population-based models. To address this challenge, we propose a dual-path architecture termed SIFPBPNet, which separately represents steady-state and instantaneous features, through a Steady-state Feature Path (SFP) and an Instantaneous Feature Path (IFP). The SFP employs a Graph Attention Network (GAT) to extract individual-specific and long-term characteristics from multi-day historical PPG trajectories. In parallel, the IFP captures short-term dynamics from current PPG segments and incorporates the steady-state prior via a cross-attention mechanism. Experiments on a large-scale wearable dataset demonstrate that SIFPBPNet achieves a Mean Absolute Error (MAE) of 8.57 and 5.97 mmHg for systolic and diastolic BP, respectively, outperforming state-of-the-art models. Furthermore, the SFP module consistently improves performance when integrated into various backbone architectures, yielding 2.8-13.1% relative MAE reductions for systolic BP. These results highlight the strong generalizability and plug-and-play transferability of the SFP module, underscoring its great potential for accurate cuffless BP monitoring.

---


### 127. [Understanding Game Coaching on Gig Platforms](https://arxiv.org/abs/2609.12695)

**<font color=#1a73e8>作者：</font>** Hwijoon Lee, Saiph Savage  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Freelance game coaches monetize their gaming expertise by offering personalized instruction to players seeking to improve, working through gig platforms, yet little is known about how they operate. To address this gap, we conducted semi-structured interviews with 20 experienced freelance coaches across 17 competitive games on Fiverr. Despite lacking shared formal training, these coaches converged on similar practices centered on rapport-building, individualized diagnosis, and adaptive feedback. We identify two structural conditions shaping this work: dual precarity, in which coaches navigate both gig platform instability and the lifecycle volatility of live-service games; and earned authority, in which coaches must continually establish legitimacy through visible competitive achievement within the same gaming spaces as their students. These coaches welcomed AI for administrative and analytic support but resisted its use in live interactions where trust, relational engagement, and situated judgment remained central. We discuss implications for Games HCI and the design of computational coaching systems.

---


### 128. [Enabling and Understanding Personalization in AI-Generated Advertising Imagery](https://arxiv.org/abs/2609.12697)

**<font color=#1a73e8>作者：</font>** Victor Kolominsky-Rabas, Leopold Müller, Claudius Budcke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized marketing traditionally matches static products to customers, while dynamic creative optimization focuses mainly on AI-driven text personalization or basic product image modifications. We address this gap by developing and implementing an AI-based framework that generates personalized advertising imagery directly from customer data. We evaluate this framework in a two-stage within-subject study with N=100 participants across four products and three levels of personalization, varied by the amount and specificity of customer data used. Participants rated each image on attitude toward the advertisement, attitude toward the product, and purchase intention. Results show that participants perceive differences across personalization levels and evaluate AI-generated advertising imagery most positively at a moderate level of personalization. High personalization increases perceived personalization, which is positively associated with all three outcome measures, but also increases perceived creepiness, which is negatively associated with the outcomes and dominates the total effect.

---


### 129. [Write on Paper and Get the Online Digital Trace:\newline A New Era for Handwriting](https://arxiv.org/abs/2609.12702)

**<font color=#1a73e8>作者：</font>** Florent Imbert, Yann Soullard, Eric Anquetil 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capturing the digital trace of handwriting usually requires a specific stylus and a compatible substrate, be it a capacitive touchscreen, an ElectroMagnetic Resonance (EMR) tablet as used in Wacom systems or special paper. While writing on regular paper offers rich haptics, no latency and is well known for improving information retention, no low-cost and widely accepted, effective solution exists to digitize such a pen trace. The challenge is to accurately track the pen's trajectory without an external reference system while allowing unrestricted freedom of pen movement across a surface. We propose an innovative solution that combines a digital pen, advanced artificial intelligence algorithms, and adaptive AI techniques to reconstruct the digital trace of handwriting. Our approach integrates hardware development, focusing on a sensor-equipped pen, with software innovations to optimize trajectory reconstruction and processing in real time using an embedded AI. This work aims to advance the state-of-the-art in automated trace reconstruction of handwriting, enabling a seamless connection between traditional handwriting on paper and capturing the trace digitally.

---


### 130. [InRTL: Effective Intra-Inter Interaction Learning for Relational Tables](https://arxiv.org/abs/2609.12712)

**<font color=#1a73e8>作者：</font>** Weichen Li, Ken Zhong, Zheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational table learning has recently emerged as an important research direction for modeling multiple tables connected through primary key-foreign key (PK-FK) relationships. Despite recent advances, a principled modeling framework tailored to this task remains underexplored. In this paper, we propose Intra-Inter Relational Table Learning (InRTL), a unified framework that explicitly models dependencies both within and across relational tables. Specifically, InRTL formalizes two complementary interaction patterns: intra-table interactions, describing associations among rows within the same table, and inter-table interactions, describing dependencies between rows across PK-FK-linked tables. To model these dependencies, we develop a column-aware table encoder to generate initial row representations, followed by Transformer-based self-attention and cross-attention modules for intra-table and inter-table learning, respectively. To further improve scalability, InRTL incorporates linearized attention and heterogeneous graph neural networks to simplify the self-attention and cross-attention operations. Extensive experiments on ten datasets covering 24 real-world tasks demonstrate the effectiveness of our approach. Code is available at this https URL.

---


### 131. [Multimodal Floorplan Encoding: Learning Dense Modality-Invariant Representations](https://arxiv.org/abs/2609.12723)

**<font color=#1a73e8>作者：</font>** Xavier Anadón, Rémi Pautrat, Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Floorplans arise in many forms, from vector CAD drawings to raster renderings and sensor-derived density maps. This heterogeneity makes it difficult to build learning systems that transfer across modalities and support geometry-centric tasks such as alignment and retrieval. We introduce the Multimodal Floorplan Encoder (MMFE), which maps diverse 2D indoor representations into a shared dense latent grid. MMFE combines a frozen DINOv3 backbone with a trainable Dense Prediction Transformer (DPT) head, and is trained with a per-cell Information Noise-Contrastive Estimation (InfoNCE) objective that aligns spatially corresponding regions across modalities while using all other cells as negatives. To improve robustness to geometric distortions, we incorporate controlled similarity transformations and enforce geometric consistency through feature-grid warping. On Structured3D, a held-out out-of-domain dataset, MMFE improves cross-modal dense matching, enables robust similarity alignment with RANSAC, and yields strong retrieval when paired with learned aggregation.

---


### 132. [Fresh-Challenge VDF Attestations for Model-Relative Response Latency](https://arxiv.org/abs/2609.12727)

**<font color=#1a73e8>作者：</font>** Ansar Yesmukhanov, Aruzhan Tlessova  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can a finite verifier obtain public, model-relative evidence about response latency for sequential computation? Verifiable delay functions (VDFs) make this possible in principle: evaluation requires T sequential steps, whereas verification is efficient in the security parameter and polylogarithmic in the numerical value of T for standard constructions. Thus a delay can be astronomically large to evaluate yet succinctly represented and feasibly checked. A VDF proof for a chosen message alone is insufficient because it may be precomputed. We specify and analyze Fresh-Challenge VDF Attestations (FCLA), a protocol composition that binds a VDF to an unpredictable public challenge, a message, and independently auditable release and receipt records. Under explicit assumptions about VDF sequentiality, the challenge source, witness logs, and a calibrated upper bound on an adversary's sequential evaluation rate, an accepted FCLA transcript is inconsistent with post-challenge generation by an adversary in that bounded model. The result neither identifies a named claimant nor excludes relaying, outsourcing, or a faster unmodeled machine. A benchmark of the public reference implementation confirms the expected empirical separation between evaluation and verification on one documented machine. Our contribution is a protocol/design analysis and benchmarked reference implementation layer, not a new VDF construction or cryptographic primitive.

---


### 133. [GRACE: Adaptive Concept Erasure with Geometry-Guided Retention in Diffusion Models](https://arxiv.org/abs/2609.12731)

**<font color=#1a73e8>作者：</font>** Qinghui Gong, Yihuai Liang, Yuanlun Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models inevitably internalize sensitive or non-compliant concepts from large-scale pretraining data, necessitating post-hoc concept erasure. However, existing erasure methods often lack explicit constraints on parameter updates, leading to over-intervention and unintended semantic drift. In addition, many methods rely on manually crafted counterfactual supervision, such as surrogate prompts, which incurs substantial data construction costs that limit scalability to new concepts. To address these limitations, we propose GRACE, a structured concept erasure framework designed to enable localized and selective intervention. Specifically, we introduce a semantically weighted sensitive subspace estimation to precisely lock intervention directions, and employ lightweight subspace-constrained adapters to prevent global semantic disturbance. To eliminate the dependency on manual prompt engineering, we design an automatically decoupled safe-anchor mechanism. To mitigate semantic drift induced by excessive intervention, we introduce an energy-driven dynamic gating mechanism that adaptively controls the timing and strength of intervention at inference. Extensive experiments demonstrate that our method achieves a superior balance between erasure effectiveness and generation fidelity. Compared with the average performance of five state-of-the-art (SOTA) concept erasure methods, our method improves the fine-grained NSFW reduction rate by $17.86\%$, while reducing the macro-averaged target CLIP Score and preservation-oriented Fréchet Inception Distance (FID) by $4.75\%$ and $50.58\%$, respectively, indicating stronger concept suppression with substantially improved preservation of the original model's generative utility.

---


### 134. [Physics-Guided Synthetic High-Frequency Ultrasound Generation for Skin Layer Segmentation](https://arxiv.org/abs/2609.12735)

**<font color=#1a73e8>作者：</font>** Junkyung ju, Kyungho Yoon, Minwoo Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-frequency ultrasound (HFUS) enables noninvasive visualization of superficial skin structures, but automated skin-layer analysis is limited by the scarcity of densely annotated data. Existing real HFUS datasets commonly provide annotations for superficial targets such as the epidermis and subepidermal low-echogenic band (SLEB), while dense labels for deeper structures such as dermis, subcutaneous tissue, fascia, and muscle are rarely available. We propose a physics-guided synthetic HFUS generation framework for skin layer segmentation. The framework constructs multilayer acoustic skin phantoms, assigns layer dependent acoustic properties, and uses k-Wave simulation to generate paired synthetic HFUS images, dense layer masks, and simulation metadata. To evaluate whether the generated data provide transferable supervision, we use it for downstream segmentation pretraining and fine-tune the models on real Mendeley HFUS data. Synthetic pretraining followed by real fine-tuning achieved real-domain performance comparable to real-only training and improved mean Dice/IoU in three of four evaluated trainable architectures. These results suggest that physics-guided synthetic HFUS images contain transferable anatomical and textural cues for real-domain skin layer segmentation, although further reduction of the synthetic-real appearance gap is needed to enable greater gains. The code and data are available at: this https URL.

---


### 135. [AquaCubeAI-Powered Monitoring Turbidity on-board Φsat-2](https://arxiv.org/abs/2609.12744)

**<font color=#1a73e8>作者：</font>** Pietro Di Stasio, Francesca Razzano, Elisa Liparulo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely monitoring of coastal water quality is critical for environmental protection, yet conventional satellite workflows rely on downlink and ground processing, introducing latency that can limit responsiveness to rapidly evolving turbidity events. To address this limitation, we propose AquaCubeAI, a lightweight machine-learning approach for onboard estimation of coastal water turbidity from {\Phi}sat-2 multispectral imagery. By shifting inference from the ground segment to the satellite, AquaCubeAI aims to enable lower-latency, more responsive, and more operationally useful turbidity monitoring under the strict compute and bandwidth constraints of spaceborne platforms. The model is trained on simulated {\Phi}sat-2 acquisitions spatially aligned with Copernicus Marine Service (CMEMS) High-Resolution Ocean Color (HR-OC) turbidity products over selected localized coastal sites spanning four European marine macro-regions. To provide a realistic evaluation of generalization in the presence of spatial correlation, we adopt a spatial block splitting protocol that mitigates data leakage between training and evaluation subsets. The main contributions of this work are: (i) a scalable dataset generation pipeline pairing simulated {\Phi}sat-2 multispectral patches with CMEMS HR-OC turbidity labels across selected localized European coastal sites; (ii) a compact Multi-Layer Perceptron (MLP)-based turbidity regressor trained under a leakage-aware geospatial split and tailored to embedded constraints; and (iii) a reformulation for dense spatial prediction via parameter sharing, enabling turbidity mapping and simple threshold-based anomaly masks for onboard decision logic. Embedded deployment on an Intel Myriad Vision Processing Unit (VPU) further confirms the feasibility of low-power hardware and supports low-latency inference from multispectral inputs.

---


### 136. [SCQ: Stabilizing Conservative Q-Learning with Sigmoid-Bounded Entropy](https://arxiv.org/abs/2609.12749)

**<font color=#1a73e8>作者：</font>** Xiefeng Wu, Shu Zhang, Zhaojie Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline-to-online reinforcement learning reduces interaction cost for real-world robot learning but suffers from persistent value estimation instability. Existing methods address this through pessimistic regularization, lower-bound calibration, and architectural normalization, but an overlooked source of instability lies in the entropy formulation: the standard log-entropy term can become negative, destabilizing policy updates. We introduce SCQ (Sigmoid-Bounded Conservative Q-Learning), which replaces this term with a sigmoid-bounded formulation that stays strictly positive. SCQ retains conservative Q regularization and return-based lower-bound calibration, stabilizing policy optimization without sacrificing exploration. We evaluate SCQ on D4RL (Minari) benchmarks under both single-demonstration and standard dataset settings, as well as on simulation and real-world visual tasks. SCQ matches or exceeds baseline performance while exhibiting more stable training dynamics across state-based and visual benchmarks, and transfers to four real-robot platforms including manipulation, wheeled, quadruped, and humanoid systems. A direct clipping intervention that removes negative log-probability contributions, together with gradient-matched positive-score controls, indicates that positivity rather than a particular score shape alone drives much of the improvement. Project website: this https URL.

---


### 137. [Optimizing for the decision not the prediction: an exploration of Smooth Net Benefit as a training objective](https://arxiv.org/abs/2609.12752)

**<font color=#1a73e8>作者：</font>** Koen M.F. Gorgels, Lasai Barreñada, Maarten van Smeden 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective Prediction models are commonly trained using objectives such as Bernoulli negative log-likelihood (NLL), although downstream clinical decisions may depend on specific risk thresholds. We introduce Smooth Net Benefit ($\sigma$NB), a differentiable approximation of Net Benefit designed to align model training with threshold-specific clinical utility.
Materials and Methods We evaluated $\sigma$NB as a training objective for logistic regression, generalized additive models (GAMs), and XGBoost with three Hessian implementations. Experiments used the Framingham cardiovascular risk dataset and 44 TabZilla datasets comprising 72 dataset-threshold combinations.
Results $\sigma$NB training did not consistently improve Net Benefit in Framingham. Across the TabZilla benchmark, mean standardized Net Benefit for logistic regression increased from 0.5669 with NLL to 0.5765 with $\sigma$NB (mean difference 0.0096, 95% CI -0.0001 to 0.0193). For GAMs, mean standardized Net Benefit decreased from 0.5921 to 0.5625 (mean difference -0.0296, 95% CI -0.0721 to 0.0129). For XGBoost, NLL achieved 0.6745 compared with 0.6723--0.6735 across $\sigma$NB implementations. In logistic regression, $\sigma$NB gains were positively associated with the performance advantage of XGBoost over NLL-trained logistic regression.
Discussion The effect of $\sigma$NB was context dependent, with modest gains concentrated in logistic regression and little benefit for more flexible model classes. This suggests that decision-focused optimization may be most useful when limited model flexibility leaves greater scope for improvement.
Conclusion Our results do not support $\sigma$NB as a general replacement for NLL training, but support further investigation of decision-focused objectives in settings where conventional likelihood-based training may not adequately capture decision-relevant structure.

---


### 138. [Curriculum-Based Adversarial Heterogeneous Agent Reinforcement Learning for Autonomous Quad-Copter Landing in Maritime Settings](https://arxiv.org/abs/2609.12758)

**<font color=#1a73e8>作者：</font>** Allan Minh-Tam Nguyen, Sree Showrya Kotala, Stefan Banioi-Crijman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering unmanned aerial vehicles (UAVs) in maritime environments is challenging due to wind turbulence and ship-deck motion, making it a valuable test case for alternative control and learning approaches as conventional landing approaches often become unreliable. We study simulated mid-air capture of quadrotor UAVs by a ship-mounted robotic arm, learning robust cooperative control policies with Heterogeneous-Agent Proximal Policy Optimization (HAPPO) Reinforcement Learning. We train with HAPPO using a curriculum and an adversarial wind agent (HARL-AC) in NVIDIA Isaac Lab, and compare the obtained control policies against those generated through curriculum-based domain randomization and a benchmark trained on a single sea state. In-distribution evaluation on sea states $0/4/5$ shows comparable success for HARL-AC and domain randomization of up to $97.5\%$. On out-of-distribution sea states $7/8/10$, HARL-AC generalizes better, achieving up to $16\%$ higher median success rate at sea state 10, and substantially lower crash rates of up to $14\%$ compared to the domain randomization policy. Furthermore, we show that the adversarially trained policy shows more cautious behavior, slightly increasing timeouts by $<3\%$, but yields safer recovery behavior in severe, unseen conditions.

---


### 139. [Same Encoder, Different Winner: A Paired-View Framework for Cell Painting Encoder Evaluation](https://arxiv.org/abs/2609.12761)

**<font color=#1a73e8>作者：</font>** Tim Treis, Nikita Moshkov, Johan Fredin Haslum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision encoders for Cell Painting are typically ranked by a single evaluation, commonly replicate mean average precision (mAP). We introduce CP-BG-Bench, a paired-view evaluation framework that holds the central cell fixed across four matched views (raw crop C, segmented S, and density-augmented variants CD and SD), ablating or augmenting surrounding pixels as a controlled intervention. Instantiating the framework on three datasets (JUMP-CP, RxRx1, RxRx3-core) and three encoders (DINOv3 ViT-B/16, OpenPhenom, SubCell) under four community-standard protocols (replicate mAP, scIB batch integration, CellProfiler feature prediction, cross-batch perturbation recall), we find that the four protocols rank the same encoders systematically differently, with disagreements decomposing along three axes: cell versus background, morphology versus context, and within-study versus across-batch. The largest effect: on RxRx3-core, SubCell with segmented inputs retains 94% of crop replicate mAP but only 32% of crop R@10, so the within-study signal preserved under segmentation is largely non-transferable; density augmentation recovers 84% of the within-study C-to-S gap but only 8% of the cross-batch gap. Segmented views predict CellProfiler features as well as or better than crops on two of three datasets, inverting the replicate-mAP ranking, and the C-to-S gap varies by an order of magnitude across datasets while remaining similar across encoders, indicating that background-driven gain is set by experimental design rather than by the encoder. Single-metric ranking of Cell Painting encoders is therefore sensitive to the protocol used, and protocol disagreements are interpretable as projections onto the three axes the paired-view design exposes. We will release the paired-view datasets, reconstruction pipelines, 36 trained checkpoints, aggregated embeddings, and the full evaluation suite.

---


### 140. [Unified Agentic Video Editing Across Levels of Complexity and Creativity](https://arxiv.org/abs/2609.12769)

**<font color=#1a73e8>作者：</font>** Surabhi S. Nath, Kim Ferres, Milan Petrović 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Editing is a core component of video production, requiring creative planning and decisions under multiple constraints. Here, we report methods for agentic tooling for automated video editing across three tasks varying in editorial goal, complexity and creativity, namely scene previews, video summaries and cinematic trailers. We evaluate the outputs and discuss implications for automation and agency.

---


### 141. [MPT: Missing Prototype Tracking via Barycentric Reconstruction in Vehicular Federated Learning](https://arxiv.org/abs/2609.12771)

**<font color=#1a73e8>作者：</font>** Hanju Jang, Gyeongmin Han, Sungmin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-vehicle federated learning enables vehicles to collaboratively improve perception models while keeping locally collected driving data private. However, vehicle participation is transient, and a vehicle may depart before training converges while permanently taking its local data. When this departing vehicle holds most samples of a target class, the class becomes rare in the remaining FL network, and its recognition can silently degrade as the shared backbone continues to evolve. Recovering the class is difficult since the few remaining samples provide a noisy prototype estimate, while FL privacy constraints prevent centralized access to raw data or per-sample features. This paper presents MPT, a cross-vehicle FL framework that maintains rare-class recognition by reconstructing its prototype at every round from privacy-preserving class-level statistics. MPT combines a barycentric decomposition that tracks drift shared with remaining-class prototypes, a covariance-based residual prediction that estimates out-of-span drift, and an adaptive calibration that weighs the remaining rare-class samples according to their reliability. We evaluate MPT on three vehicle classification tasks and four backbones against representative calibration and drift-compensation baselines. MPT outperforms all baselines in rare class F1, reaching 0.516 on the nuImages dataset with only 1\% of rare-class samples remaining, without raw data, per-sample features, or retraining.

---


### 142. [Convergence of Stochastic Gradient Methods under Heavy-Tailed Noise and Hölder Smoothness](https://arxiv.org/abs/2609.12785)

**<font color=#1a73e8>作者：</font>** Misbah Uz Zaman, Anirbit Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical convergence guarantees for stochastic gradient methods typically assume Lipschitz-smooth objectives and finite-variance gradient noise, both frequently violated in practice. In contrast, we study nonconvex stochastic optimization under the joint relaxation of these assumptions: objectives with $(L,s)$-Hölder continuous gradients, $s\in(0,1]$, and gradient noise satisfying only a bounded $\alpha$-th moment condition for $\alpha\in(1,2]$. We establish three convergence results. Firstly, that standard SGD converges at rate $O(T^{-s/(1+s)})$ whenever $\alpha\ge1+s$, extending the classical nonconvex SGD rate to heavy-tailed noise and Hölder smoothness simultaneously. Secondly, we analyze $\delta$-regularized gradient clipping ($\delta$-GClip), a provable trainer of wide and deep nets, and establish a stationarity rate of $O(T^{-2s(\alpha-1)/[(1+s)(2\alpha-1)]})$ under the same condition. Thirdly, we analyze standard gradient clipping (G-Clip) and show that it recovers the above rate for $\alpha\ge1+s$ while in the very heavy-tailed regime $\alpha<1+s$, it has a convergence rate $O(T^{-2s(\alpha-1)/[(\alpha-1)+s(2\alpha-1)]})$ --- the first convergence guarantee in this regime for any stochastic gradient based method.

---


### 143. [LG-PF: Lightweight Confidence-Guided Polarization Image Fusion](https://arxiv.org/abs/2609.12787)

**<font color=#1a73e8>作者：</font>** Zhuangfan Huang, Zhenyu Kuang, Gao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarization image fusion combines the stable luminance and structural information of the total- intensity image S0 with the material-sensitive details of the degree of linear polarization (DoLP) image. However, the reliability of DoLP varies spatially, and indiscriminate polarization transfer may amplify unstable responses or disturb the structural appearance anchored by S0. We therefore propose LG-PF, a lightweight confidence-guided framework that formulates polarization fusion as a selective residual transfer process. A Polarization Confidence Prior estimates spatially reliable polarization responses, a Mask-guided Multi-scale Fusion module regulates their transfer across three feature scales, and a Lightweight Context-aware Bounded Correction Head stabilizes local photometric and structural transitions. Confidence guidance is also incorporated into the optimization objectives to preserve reliable polarization details while suppressing unsupported responses. We also construct MSP, a multi-scene polarization fusion dataset containing 1000 pixel-aligned image pairs from 17 indoor and outdoor scene categories. LG-PF achieves the best results across all six evaluated metrics on MSP, while subset-based evaluations on PIF and GAND show promising transferability without fine-tuning. With only 0.2936 M parameters and an inference time of 21.712 ms per image, LG-PF achieves competitive fusion quality with low computational cost. The source code, dataset, and official data splits will be made publicly available upon publication.

---


### 144. [VertiFuseX: Generalizable Financial Forecasting via Multi-Stream Temporal Fusion](https://arxiv.org/abs/2609.12793)

**<font color=#1a73e8>作者：</font>** Aashish Bohra, Vivek Vijay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stock price prediction remains challenging due to the non-stationary and noisy nature of financial time series. Existing deep learning models often rely on rigid decision-level fusion, ad hoc hyperparameter tuning, and compressed final-layer outputs, causing information loss, overfitting, and limited cross-market generalization. We propose VertiFuseX, a hybrid LSTM architecture using penultimate-layer vertical fusion of multi-scale temporal representations. VertiFuseX stacks and reweights penultimate features from LSTM, Bi-LSTM, and St-LSTM branches, integrates a parallel DNN stream, and jointly optimizes all components via backpropagation under a fixed hyperparameter configuration. This preserves richer intermediate temporal information across scales. Evaluated on 15 years (2010-2024) of closing prices from 10 global equity indices using strict chronological out-of-sample testing with the final 365 trading days held out, VertiFuseX achieves 30-54% MAPE reductions and over 40% improvements in MAE and RMSE versus LSTM-based baselines, and outperforms seven state-of-the-art models across 33 metric-dataset comparisons. Ablation studies confirm penultimate-layer fusion drives these gains over final-layer fusion and decision-level ensembling. Gradient-based saliency analysis shows consistent emphasis on mid-range dependencies at lags 9-15 days. Economic validation via algorithmic trading simulation under extreme market regimes shows reduced maximum drawdowns and superior risk-adjusted returns. With 675k parameters, a 2.6 MB memory footprint, and 1.5 ms/sample inference latency, VertiFuseX offers a lightweight, interpretable, deployment-ready framework for robust financial forecasting.

---


### 145. [LGFN: Lightweight Gated RGB-Polarization Fusion with Modality-Availability Conditioning for Camouflaged Object Detection](https://arxiv.org/abs/2609.12798)

**<font color=#1a73e8>作者：</font>** Zhuangfan Huang, Xiaosong Li, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection (COD) is an important engineering task in intelligent optical perception, but it remains challenging when targets closely resemble their surroundings. Polarization imaging provides complementary physical cues, whereas existing methods typically assume fixed multimodal input configurations and entangle intra-polarization coordination with interaction between red-green-blue (RGB) and polarization representations. We propose LGFN, a lightweight gated RGB-polarization fusion framework supporting separately optimized RGB-only and polarization-assisted configurations. A deterministic Modality Router selects the appropriate configuration according to polarization availability. In the multimodal configuration, an availability-conditioned Modality Gate calibrates the available polarization branches; the Gated Polarization Hub coordinates learned degree of linear polarization (DoLP) and angle of polarization (AoP) representations with explicit polarization cues; and RGB-Polarization Cross Fusion introduces the coordinated representation into the RGB hierarchy through controlled residual interaction. The multimodal configuration requires neither sample-dependent statistics nor handcrafted quality descriptors during inference. On the complete 230-image PCOD_1200 test set, the RGB-only configuration achieves a mean absolute error of 0.0090, a Dice score of 0.8806, and an intersection over union of 0.8144, obtaining the best results on all six metrics among the evaluated RGB-based methods. Under a common local reevaluation protocol, the multimodal configuration outperforms PolarNet and IPNet on all six metrics. Relative to IPNet, it reduces the parameter count, floating-point operations, and latency by 53.1%, 73.6%, and 63.0%, respectively.

---


### 146. [Interpreting the predictions of neural network classification based on a Taylor Coefficient Analysis (TCA)](https://arxiv.org/abs/2609.12801)

**<font color=#1a73e8>作者：</font>** Markus Klute, Artur Monsch, Lars Sowa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a rigid and comprehensive taxonomy and paradigm for characterizing the influence of the input feature space $X$ on the predictions $\hat{y}$ of a neural network (NN) used for event classification, based on a Taylor expansion of $\hat{y}$ in $X$. The complete process of introspection we refer to as Taylor Coefficient Analysis (TCA). Based on two simplistic example tasks, which can be easily understood and bencmarked, we illustrate the power of the TCA when it comes to revealing, what properties of $X$ have led to what value of $\hat{y}$, of a given NN model, building up intuition for the method. A more complex application is meant to represent $X$ of a typical classification task at a CERN LHC experiment. Based on this application, we play through the different levels of introspection that the TCA offers and discuss a number of practical aspects for a TCA application typical for the analysis of CERN LHC data. We conclude with a study to support the assumption that those properties of $X$ most relevant for tasks of the complexity typical for a CERN LHC experiment, are usually caught by a TCA up to the second order.

---


### 147. [Batten the Hatches: Cybersecurity with Military Mariners](https://arxiv.org/abs/2609.12810)

**<font color=#1a73e8>作者：</font>** Ryan Von Brock, Anna Raymaker, Animesh Chhotaray 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyberwarfare has become a key component of contemporary geopolitical conflict. However, there has been extremely limited systematic investigation into how cybersecurity is handled by military organizations and personnel. The military context is unique compared to other operational ones, with immense resource availability (U.S. military spending approached 1 trillion dollars in 2024), a rigid chain of command, and extraordinary consequences for its actions. Thus, military cybersecurity is a distinct yet understudied topic.
In this paper, we take an early step at understanding military cybersecurity by investigating how service members understand, recognize, and respond to cyber risk. We focus on maritime services and carefully consider organizational barriers to design an unclassified study and conduct semi-structured interviews with 20 military mariners from U.S. Navy and Coast Guard vessels. Through our investigation, we identify unique consequences of compromising military systems, including weapon takeover and purposeful geopolitical escalation. We find that cybersecurity is organizationally abstract on ships, so mariners build cyber risk models from informal experience rather than formal instruction. They nonetheless make cybersecurity actionable by recognizing operational impacts and responding with a safety-oriented incident-response model that creates resilience but may delay cyber attribution and containment. These findings inform actionable recommendations to help military operators frame cyber threats, merge longstanding nautical doctrine with modern systems, and apply military insights to the civilian sector, all to secure the broader maritime environment.

---


### 148. [RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States](https://arxiv.org/abs/2609.12814)

**<font color=#1a73e8>作者：</font>** Luca Herranz-Celotti, Vincent Guigue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention and state-space models provide linear-time sequence modeling, but their recurrent memory remains a second-order tensor (a matrix), limiting the order of interactions that can be represented in the state. We introduce the RunningTensor, which generalizes this memory to an order-$o$ tensor, updated by a rank-1 outer product and read by contracting against $o-1$ vector queries. Order $2$ recovers linear attention; we study order $3$ as a proof of concept, retaining both recurrent and parallel forms while remaining linear in sequence length $T$ and improving working memory capacity from $\mathcal{O}(W^2)$ to $\mathcal{O}(W^o)$. On synthetic multi-query associative recall, RunningTensor outperforms linear-attention and SSM baselines. After pretraining, it also improves performance on language-understanding and non-synthetic retrieval tasks, suggesting that higher-order recurrent state can provide useful additional memory capacity beyond matrix-valued state.

---


### 149. [SCDM: Spatial-Contextual Disentanglement Mamba via Differential Inference for Efficient Image Classification](https://arxiv.org/abs/2609.12825)

**<font color=#1a73e8>作者：</font>** Mustafa Bora Çelik, Hayriye Aktaş Dinçer, Ayse Keles  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs), particularly VMamba, have emerged as efficient alternatives for modeling long-range dependencies in medical image analysis. However, distinguishing subtle pathological features from visually similar anatomical backgrounds remains a significant challenge. Existing SSM architectures often learn entangled representations, lacking explicit mechanisms to separate disease-specific signals from normal anatomy. To address this limitation, we propose Spatial-Contextual Differential Mamba (SCDM), an asymmetric dual-branch architecture designed for selective representational disentanglement. SCDM introduces a Positive Branch for extracting discriminative features and a Negative Branch that actively models and suppresses normal anatomical context. This separation is achieved through a similarity-driven repulsion gate and a differential inference rule, which promote competitive feature learning without requiring additional branch labels or increasing model capacity. Evaluated on the RSNA Pneumonia dataset, SCDM achieves competitive classification performance (AUC of 0.858) while requiring significantly fewer parameters (29.4M) and FLOPs (1.44G) compared to standard VMamba and vision transformer baselines. Furthermore, activation analyses demonstrate that our differential mechanism yields highly precise localization, effectively isolating lesions by inhibiting irrelevant anatomical distractors.

---


### 150. [CoralscapesV2: Panoptic and Fine-Grained Visual Scene Understanding in Coral Reefs](https://arxiv.org/abs/2609.12826)

**<font color=#1a73e8>作者：</font>** Jonathan Sauder, Thomas Ruckli, Gabrielė Strodomskytė 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In order to design conservation and restoration strategies to counter the global decline of coral reefs, ecological monitoring of reefs needs to be scaled up dramatically. Computer vision methods are increasingly used to tackle the vast amount of data: as the paradigm of data collection in reefs shifts from highly standardized and constrained survey images to unconstrained imagery on scalable platforms, it is necessary to design machine learning methods that help to get a fine-grained understanding of reefs from general-purpose reef imagery. This paper provides CoralscapesV2, an extension of the Coralscapes dataset for general-purpose visual scene understanding in reefs. CoralscapesV2 increases the dataset size, scope, label completeness and quality for semantic segmentation, and extends the number of classes from 39 to 95 fine-grained visual categories. Furthermore, CoralscapesV2 provides 65k exhaustive fish instance mask annotations, meticulously annotated to completeness by using the video, revealing that annotation of fish based on only static images is insufficient. CoralscapesV2 is the first dataset for panoptic segmentation in coral reefs, capturing a wide range of scenarios in the wild, posing a challenging benchmark for contemporary semantic segmentation and instance segmentation models. CoralscapesV2 is an important step towards general-purpose panoptic segmentation in coral reefs, which has substantial implications for scaling up coral reef monitoring, as it can be employed in a wide range of applications from benthic cover mapping from robot or handheld videos to designing methods for automated quantification and understanding of fish behavior and fish-reef interactions.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-201](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
