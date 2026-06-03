# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-312](./part-07.md)

---

### 201. [Analyzing Stream Collapse in Hyper-Connections: From Diagnosis to Mitigation](https://arxiv.org/abs/2606.03483)

**<font color=#1a73e8>作者：</font>** Ekaterina Alimaskina, Gleb Molodtsov, Aleksandr Beznosikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections (HC) replace the single Transformer residual stream with multiple streams, introducing a permutation symmetry over stream indices. We study how this symmetry is resolved in practice: whether streams specialize in a balanced way or exhibit dominant-stream usage. Using fine-grained diagnostics for HC-based language models, we trace how multi-stream representations are actually used. We find that after an early seeding stage, residual mixing often remains close to identity, limiting a core HC mechanism for exchanging information between streams. Moreover, both signal and interpretable features concentrate in a dominant stream, and the nominally multi-stream residual connection can underutilize its capacity, behaving closer to a single-stream residual pathway. Finally, we show that breaking symmetry at stream initialization reduces dominant behavior and improves performance across \textit{m}HC variants. Our code is publicly available.

---


### 202. [Analyzing Visual Attention Patterns During Band Rehearsal with Mobile Eye Tracking](https://arxiv.org/abs/2606.03485)

**<font color=#1a73e8>作者：</font>** Arvind Srinivasan, Tobias Rau, Michael Sedlmair  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual attention is central to ensemble coordination, yet how musicians allocate gaze during naturalistic rehearsal remains poorly understood. We present a pilot study using mobile eye tracking to examine gaze behaviour in a four-member band across three songs, each practiced twice. Musicians wore Pupil Labs Neon eye trackers, and YOLOv8-assisted scene annotations mapped fixations to ensemble members and objects in view. Analyzing fixation matrices, transition matrices, temporal scarf plots, and dwell-transition correlations, we uncover a hub-and-spoke attention topology: the session leader was the dominant gaze target for all members, while the learning guitarist concentrated up to 97% of interpersonal dwell on this single reference. Between attempts, gaze transitions decreased by up to 65% on average for unfamiliar material (up to 82% for individual participants) as scanning stabilized. Scarf plots reveal how teaching breakdowns fragment attention and uninterrupted runs consolidate it. Post-session participant reflections align with the quantitative patterns, and we discuss implications for gaze-aware tools in ensemble pedagogy.

---


### 203. [NeuroArmor: Safe-Variant-Guided Representation Consistency for Selective Re-Anchoring in Jailbreak Defense](https://arxiv.org/abs/2606.03486)

**<font color=#1a73e8>作者：</font>** Zhongyang Lin, Ziran Zhao, Feifei Zhai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models remain vulnerable to jailbreak attacks that hide harmful intent behind seemingly ordinary requests such as role-play, translation, encoding, adversarial suffixes, and multi-turn buildup. Existing defenses still struggle to handle these attacks without over-blocking benign but sensitive requests, partly because they often apply the same action to every prompt and therefore fail to balance safety and helpfulness. We propose NeuroArmor, a white-box runtime defense that uses prompt-specific safe variants as a local safety reference for deciding when intervention is needed and, once triggered, as safe targets for intervention. For each prompt, NeuroArmor builds K safe variants, compares the prompt state against this local safe reference in hidden-state space, and routes anomalies either to a refusal branch for malicious prompts or to a helpful recovery branch for borderline benign prompts. On Llama-3-8B-Instruct, NeuroArmor reduces malicious attack success rate (ASR) from 41.56% to 1.57% while lowering benign false positive rate (FPR) on the shared benign pool from 30.26% to 22.05%; matched baselines remain substantially weaker on this trade-off. External-judge and manual behavioral evaluations further show that the remaining non-blocked outputs are much less likely to be operationally harmful. Overall, NeuroArmor provides a more effective runtime strategy for jailbreak defense by combining prompt-specific consistency checking, routing, and selective intervention.

---


### 204. [TrAction: Action Recognition with Sparse Trajectories](https://arxiv.org/abs/2606.03490)

**<font color=#1a73e8>作者：</font>** Jan F. Meier, Felix B. Mueller, Alexander Ecker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern action recognition models operate on memory- and compute-intensive dense RGB video volumes and frequently exploit appearance and background shortcuts, for example, predicting actions from objects or scenes instead of characteristic motion. We investigate an efficient alternative input modality that is largely free of such biases by construction: sparse point trajectories. To this end, we develop a simple transformer architecture for 2.5D trajectory-based recognition together with a masked-trajectory pretraining, which we show to substantially improve downstream action recognition accuracy. Despite using only a fraction of the dense RGB input, our method reaches 45% top-1 on Something-Something V2 and 54% on EPIC-Kitchens-100, and surpasses V-JEPA on time-reversal sensitivity. More importantly, we find trajectory features to be complementary to state-of-the-art appearance-based features. Fusing our pretrained model with DINOv2 and V-JEPA 2 improves top-1 accuracy on Something-Something V2 by 8.7 and 1.6 points, respectively. Code: this https URL

---


### 205. [The Attention-Aware Pipeline: Design Tensions from Making Attention Visible in XR](https://arxiv.org/abs/2606.03492)

**<font color=#1a73e8>作者：</font>** Arvind Srinivasan, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Where people look during shared activity carries coordination cues that speech and gesture cannot replace, but these patterns remain invisible to participants. XR headsets make gaze available as real-time input, yet few systems feed it back visually. We frame our work using the Attention-Aware Pipeline (Capture, Record, Revisualize), whose feedback loop means the systems visual response alters what users attend to next, triggering further responses. This generates design tensions whose form depends on each stages configuration. We trace the pipeline through three systems casting attention as a mirror (reflecting gaze history), a medium (sharing it across collaborators), and a mediator (intervening through diminished reality). Each encountered a tension the loop predicted, motivating the next. A formative eye-tracking study of four musicians surfaced attentional tunneling and near-total disconnection, confirming the need for intervention. We present these tensions and a next step: testing whether subtractive intervention reduces tunneling for a single sight-reader.

---


### 206. [Low-Frequency Shortcuts in Texture-Driven Visual Learning](https://arxiv.org/abs/2606.03493)

**<font color=#1a73e8>作者：</font>** Utku Şirin, Cathy Hou, David Alvarez-Melis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural networks suffer from shortcut learning, where learned features generalize well to the training set but not to in-distribution (ID) or out-of-distribution (OOD) test sets. Existing studies are all based on a few standard benchmarks, which are shape-driven. Numerous application domains, however, are texture-driven. In this work, we present shortcut learning analysis for texture-driven domains, and compare it with that of a standard benchmark. We show that texture-driven domains suffer from low-frequency shortcuts. They make the majority of their decisions based on a few low-frequency components (LFCs) with a skewed spectral behavior, despite that their classification information is in higher-frequency, fine-grained details. Pruning LFCs from training and test sets eliminates the shortcut and provides a more balanced spectral behavior, improving the ID accuracy by up to 8%. We show that low-frequency shortcuts make the models highly vulnerable to OOD corruptions, leading up to 70% accuracy drop compared to the ID accuracy. Pruning LFCs significantly improves robustness to low-frequency corruptions, by up to 40%, and introduces a trade-off for high-frequency corruptions; the balanced spectral behavior provides a better generalization performance, whereas the increased dependence on high-frequency features reduces it. OOD accuracy depends on the interaction between these two factors.

---


### 207. [HiSE: A Lightweight Hierarchical Semantic Explainer for Heterogeneous Graph Neural Networks](https://arxiv.org/abs/2606.03495)

**<font color=#1a73e8>作者：</font>** Zongrui Li, Yuhang Zhao, Ying Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous graph neural networks (HGNNs) have demonstrated remarkable performance in modeling complex relational data, however their interpretability in high-stakes applications remains a critical challenge. Existing explanation methods suffer from two major limitations: on the one hand, the generated explanations fail to reflect the inherent semantic hierarchy of HGNNs, resulting in a lack of fidelity to the model's internal decision-making mechanism; on the other hand, feature explanations often rely on complex search or perturbation mechanisms, leading to excessive computational complexity and poor efficiency. To address these issues, we propose HiSE, a lightweight feature-oriented interpretable model for HGNNs. HiSE achieves semantically aware feature explanations through hierarchical semantic modeling: at the semantic level, local surrogate models based on the Least Absolute Shrinkage and Selection Operator (LASSO) are employed to learn sparse feature representations under each semantic view; at the cross-semantic level, the contributions of different semantic views are adaptively characterized via KL divergence to produce a unified explanation. Extensive experiments demonstrate that HiSE outperforms existing methods in terms of fidelity, robustness, and cross-semantic explanation capability, while its lightweight framework incurs low computational overhead, enabling efficient application to large-scale, complex real-world heterogeneous graphs.

---


### 208. [Demystifying Pipeline Parallelism: First Theory for PipeDream](https://arxiv.org/abs/2606.03498)

**<font color=#1a73e8>作者：</font>** Ivan Ilin, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training modern machine learning models increasingly requires computation to be distributed across many accelerators. Data parallelism remains the default choice and is often paired with tensor-parallel sharding, but model parallelism becomes unavoidable once parameters, activations, or optimizer states no longer fit on a single device. This paper studies pipeline model parallelism through the lens of PipeDream (PD) (Harlap et al., 2018). Our first contribution is theoretical: we introduce Randomized PipeDream (RPD), a stale block-SGD abstraction that yields, to our knowledge, the first clean nonconvex convergence guarantee for a PD-style method. Our second contribution is a scaling diagnosis: we prove that the delay induced by steady-state PD grows as $S^2 - S/2 + O(1)$ for $S$ stages, so the stale-read contribution in the convergence theorem scales as $\Theta(\gamma^2 S^4)$, equivalently as $\Theta(S^4/K)$ in the tuned-rate form. Our third contribution is a comparison with LocalSGD, whose periodic model averaging trades weight staleness for synchronization bubbles. In our reported simulated-time experiments, the better-performing method depends on the objective: PD performs better on the quadratic objective and on a small language-modeling training-loss task, while for logistic regression LocalSGD becomes superior as the number of stages increases.

---


### 209. [Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark](https://arxiv.org/abs/2606.03499)

**<font color=#1a73e8>作者：</font>** Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has rapidly emerged as a leading representation for real-time novel view synthesis, but recent work shows it is vulnerable to diverse poisoning attacks, including illusory object injection, computation cost amplification, and post hoc model watermarking. Despite this expanding threat surface, existing studies focus mainly on attack success, while defense and detection remain underexplored. From a detection perspective, a key challenge and opportunity arise from the multi-stage nature of the 3DGS reconstruction pipeline, which produces heterogeneous intermediate representations. Forensic signals for detecting poisoning are inherently stage dependent: an attack introduced at one stage may produce signals that emerge only at later stages. This motivates a stage-wise view of detectability that goes beyond single-stage evaluation. We introduce Poison-3DGS, a benchmark for stage-wise characterization of poisoning detection in 3DGS. It exposes stage-specific artifacts, including multi-view images, geometry, training dynamics, and Gaussian parameters, across a diverse set of scenes and attacks. Using it, we conduct a systematic study of detectability across pipeline stages. Our analysis reveals several insights. First, detectability varies significantly across stages, and no single stage consistently dominates across attack types. Second, different attacks exhibit distinct stage-specific forensic signals, so detection effectiveness depends critically on where signals are observed. Third, later-stage signals such as training dynamics and Gaussian parameter statistics provide strong cues not observable at earlier stages. Overall, our work provides a principled benchmark and the first systematic characterization of stage-dependent detectability in 3DGS, offering a foundation for future research on robust and reliable 3DGS systems.

---


### 210. [BaltiVoice: A Speech Corpus and Fine-tuned Whisper ASR System for the Balti Language](https://arxiv.org/abs/2606.03504)

**<font color=#1a73e8>作者：</font>** Muhammad Ali  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present BaltiVoice, a 16.8-hour read-speech corpus for Balti (ISO 639-3: bft), a Tibetic language spoken in Gilgit-Baltistan, Pakistan, with no prior publicly available ASR resources. The corpus contains 10,060 validated utterances in native Nastaliq script, derived from Mozilla Common Voice recordings. We fine-tune OpenAI Whisper-small on this corpus and report a Word Error Rate (WER) of 30.07% on a held-out validation set of 538 utterances, down from a measured zero-shot baseline of 182.18% for Whisper-small on Balti. The dataset, fine-tuned model, and a live transcription demo are publicly available on HuggingFace.

---


### 211. [AvatarMix: Identity-Preserving Cross-Avatar Composition for Outfit Personalization](https://arxiv.org/abs/2606.03506)

**<font color=#1a73e8>作者：</font>** Zhaorong Wang, Yoshihiro Kanamori, Yuki Endo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D avatar outfit transfer methods face distinct challenges: approaches that lift 2D edits to 3D often suffer from outfit or identity quality degradation, while those that separately model body and clothing layers are prone to intersection artifacts. We introduce AvatarMix, a compositional paradigm that bypasses these issues by directly composing the head and body from two high-fidelity Gaussian avatars. While this paradigm inherently preserves outfit quality and avoids intersections, it introduces challenges in creating a seamless join and maintaining appearance fidelity after body reshaping. To this end, we propose a two-tier refinement strategy: SeamFix, a localized diffusion module that refines hair and neck to ensure an artifact-free join, and an optional full-body refinement, FullbodyFix, that restores garment appearance when retargeting degrades the clothed body. Both operate on renders from an already 3D-consistent Gaussian avatar, which limits multi-view artifacts compared to 2D-to-3D lifting. To preserve the user's body identity, our mesh-based Gaussian representation enables the adaptation of a robust mesh retargeting technique, precisely reshaping the clothed body to the user's physique and robustly handling diverse body shapes. Extensive experiments demonstrate that our method achieves state-of-the-art results in outfit fidelity and identity preservation, providing a new perspective for realistic 3D outfit personalization. Project page: this https URL

---


### 212. [Structure-Guided Mixed Masked Pretraining and Spatial Continuity Regularization for Printed Circuit Board Defect Detection](https://arxiv.org/abs/2606.03508)

**<font color=#1a73e8>作者：</font>** Peitong Wang, Nuo Wang, Enxin Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Printed circuit board (PCB) defect detection is an essential part of automated optical inspection (AOI); yet it remains challenging in practice because many defects are tiny, low-contrast, and embedded in dense circuit backgrounds. To address these issues, this paper presents a two-phase PCB defect detection framework that combines structure-guided mixed masked pretraining with spatial continuity regularization. In the pretraining stage, we design a sparse convolutional masked pretraining scheme to exploit unlabeled PCB images, where structure-guided mixed masking is used to construct informative masked inputs. The sparse convolutional reconstruction pipeline suppresses invalid responses from masked regions and enables the detector backbone to infer missing PCB structures from visible conductive patterns, thereby learning PCB structural priors. In the fine-tuning stage, the pretrained backbone is transferred to the downstream defect detection task. For the task, a spatial continuity regularization term is introduced during fine-tuning. This term constrains dispersed positive predictions assigned to the same defect instance and promotes more compact localization on elongated defect regions. Experiments on the DsPCBSD+ dataset show that the proposed method achieves 85.5% mAP0.5 and 52.3% mAP0.5:0.95, outperforming several strong baseline detectors. Ablation studies and qualitative results further confirm the effectiveness of the proposed framework for robust PCB defect detection in industrial AOI scenarios.

---


### 213. [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509)

**<font color=#1a73e8>作者：</font>** Zuhao Ge, Xiaosong Jia, Chao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building memory is essential for long-horizon planning in zero-shot embodied navigation. Detector-centric scene graphs often compress observations into sparse nodes, discarding fine-grained visual evidence and accumulating noise, while 3D reconstruction-based methods remain computationally prohibitive. We present EvoMemNav, an efficient, self-evolving, fine-grained memory framework for zero-shot embodied navigation. EvoMemNav constructs a Visual-Semantic Memory Graph (VSMGraph) that keeps raw views as first-class memory and organizes them with lightweight semantic cues and topological relations into a room-view-object hierarchy, preserving fine-grained details for disambiguation and Stop verification. To scale to growing memory, we introduce a budgeted coarse-to-fine policy: a coarse stage compresses the search space into promising regions, and a fine stage invokes a VLM only for targeted verification and decision. Beyond static memories, EvoMemNav performs reflection-driven write-back after each subtask, updating graph-attached priors that encode accumulated environmental knowledge to refine future decisions without retraining. Experiments on GOAT-Bench and HM3D across object, text-description, and image-goal modalities show consistent gains in SR/SPL, with better multi-instance disambiguation, fewer premature stops, and stronger zero-shot generalization.

---


### 214. [Privacy-Preserving High-Resolution Image Gradient Computation Based on Fully Homomorphic Encryption](https://arxiv.org/abs/2606.03513)

**<font color=#1a73e8>作者：</font>** Yufei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With growing emphasis on privacy protection, homomorphic encryption (HE) has emerged as a core method for privacy-preserving image processing, as it enables operations directly on encrypted data. However, existing research predominantly focuses on low-resolution image processing, and techniques for privacy-preserving high-resolution image processing remain underexplored. As the image size increases, the HE parameters must be adjusted accordingly, and directly applying existing methods can lead to significant computational overhead. In this work, we propose a multi-ciphertext privacy-preserving framework for large images, enabling efficient image encryption and computation under the semi-honest model. Specifically, we divide the large image into multiple sub-images, which allows us to maintain smaller HE parameters and reduce key size. By parallel processing the sub-image ciphertexts and introducing a new bootstrapping placement strategy, we significantly reduce encryption overhead and enhance user experience. On the server side, we optimize the large image convolution operation through a repeated packing technique and implement the Sobel operator computation based on HE. To improve gradient direction calculation for the Sobel operator, we introduce a new polynomial approximation method for the reciprocal function based on the sign function, which can be applied to other HE-based protocols.

---


### 215. [Post-Hoc Robustness for Model-Based Reinforcement Learning](https://arxiv.org/abs/2606.03521)

**<font color=#1a73e8>作者：</font>** Siemen Herremans, Ali Anwar, Siegfried Mercelis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To improve the real-world applicability of reinforcement learning (RL), the field of adversarially robust RL studies how to train agents under adversarial environment perturbations. In this setting, a protagonist agent optimizes a policy under environmental perturbations from an adversary, resulting in a zero-sum Markov game. When adversarially robust RL is combined with model-based RL, the adversary can target a learned transition model instead of the training environment. Extending this idea, this work introduces post-hoc robustification of deep RL agents at inference time. By using the learned model in combination with a trained nominal policy, our approach performs a robust policy improvement step. The goal is to improve robustness without any additional training of neural networks. Specifically, we utilize model-predictive control under adversarial rollouts, which are approximated via projected gradient descent within a bounded uncertainty set. Furthermore, these offline rollouts are performed while considering and mitigating out-of-distribution issues. The proposed methodology is validated by demonstrating significant improvements in robustness when the algorithm is evaluated in perturbed Gymnasium MuJoCo environments, while considering the computational limitations of the post-hoc inference setting.

---


### 216. [High-Precision APT Malware Attribution with Out-of-Scope Resilience](https://arxiv.org/abs/2606.03523)

**<font color=#1a73e8>作者：</font>** Peter Williams, Adam Sobey, Erisa Karafili  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Early attribution of Advanced Persistent Threat (APT) activity can help defenders prioritise investigation, select countermeasures, and reduce the impact of an intrusion. Malware provides useful attribution evidence, but automated APT malware attribution remains difficult in practice. Existing approaches are typically trained and evaluated as closed-set classifiers over a limited number of known APT groups. In operational environments, however, classifiers are likely to encounter samples from groups not represented during training. Closed-set classifiers are then forced to assign such samples to known groups, producing unsupported and potentially misleading attributions. We present a high-precision APT malware attribution method based on ranked binary classifiers with explicit abstention. Rather than training a single multi-class classifier, our approach trains and tunes two binary classifiers per APT group, ranks the classifiers by validation performance, and applies them sequentially. A sample is attributed only when a classifier provides sufficient evidence; otherwise, it abstains. We evaluate the method on the APT Malware dataset and on a larger combined dataset designed to stress-test out-of-scope behaviour. On the APT Malware dataset, the method achieves higher precision than previously published results on the same dataset. In the most challenging setting, where 87% of test samples came from 60 APT groups excluded from training, the method abstained on 94% of out-of-scope samples while maintaining 92% precision and 95% selective accuracy on the samples it classified.

---


### 217. [When Should the Teacher Move? Temporal Coupling and Stability in Self On-Policy Distillation](https://arxiv.org/abs/2606.03532)

**<font color=#1a73e8>作者：</font>** Haowei Guo, Baolong Bi, Ruicheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self on-policy distillation trains a student policy against a teacher derived from its own parameter history, yet the teacher's update schedule -- which governs the \emph{temporal coupling} between teacher and student -- has not been systematically studied as a stability variable. Through a controlled schedule sweep on Qwen3-8B, we establish that \emph{isolation periods}, defined as complete teacher freezing between updates, are the key structural property enabling stable learning, not teacher age. To characterize these underlying training dynamics, we introduce a diagnostic framework of temporal KL structure, refresh shock, and length-tail risk. This framework further uncovers \emph{state-oblivious collapse}: optimal short-horizon fixed schedules catastrophically fail under long-horizon training because a clock-driven refresh can copy a transiently drifting student into the teacher in a single, irreversible step. This failure mode is invisible under short-horizon evaluation and mechanistically distinct from EMA's chronic contamination. To address this, we propose \emph{Consolidation-Gated Teacher Refresh} (CGTR), which preserves isolation periods while gating each refresh on joint evidence of reward improvement and length-tail safety, ensuring every teacher movement responds to genuine student consolidation rather than a clock signal. With a single shared parameter set and no per-dataset retuning, CGTR achieves \textbf{zero collapse} and the best final score on all four tasks (Chemistry, Biology, Physics, ToolUse), self-regulating its refresh frequency to each task's learning dynamics.

---


### 218. [Knowledge-Preserved Model Tuning in Null-Space for Robust Spatio-Temporal Video Grounding](https://arxiv.org/abs/2606.03539)

**<font color=#1a73e8>作者：</font>** Haoxuan Chen, Xianqin Liu, Jian-Fang Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Video Grounding aims to localize object tubes based on textual queries. While recent methods have achieved remarkable success, they mainly focus on high-quality(HQ) inputs, neglecting the widespread presence of low-quality(LQ) videos in real-world scenarios. Although tuning methods like LoRA can adapt to degraded inputs, they inevitably disrupt pre-trained knowledge. To address this, we propose Null-Space Tuning (NST). This framework exploits the geometric property that adding vectors within the null-space of frozen weights to the layer input does not affect the output. Leveraging this, NST injects learnable residuals into input features that can be selectively invisible to the pre-trained backbone. Specifically, NST combines the Quality-Adaptive Unit and Dual-Space Reparameterization to synthesize these residuals by confining components for HQ inputs to the null-space, while directing restoration components for LQ inputs to the non-null space. As the frozen weights eliminate null-space components, we effectively rectify degraded inputs while preserving pre-trained knowledge for HQ inputs. Extensive experiments show that NST outperforms state-of-the-art methods on our Mixed-Quality benchmark.

---


### 219. [D2MDT: Department-aware Multidisciplinary Team Consultation with Deliberation for Efficient Clinical Prediction](https://arxiv.org/abs/2606.03543)

**<font color=#1a73e8>作者：</font>** Yongqi Liang, Qidong Liu, Chunze Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Electronic health records (EHRs) are central to clinical prediction, but existing methods either rely on correlation-driven deep models or use single large language models (LLMs), making it difficult to support multidisciplinary clinical reasoning. Recent multi-agent systems (MAS) provide a promising alternative, yet current EHR-grounded MAS methods still suffer from weak evidence differentiation across agents and redundant multi-round interaction. We propose D2MDT, a Department-aware MultiDisciplinary Team Consultation with Deliberation for Efficient clinical prediction. D2MDT first constructs structured EHR evidence and consultation-ready semantic evidence for multi-agent consultation. It then assigns patient-specific department perspectives to doctor agents and retrieves complementary evidence for collaborative consultation. To improve efficiency, D2MDT further introduces residual deliberation, which updates only unresolved consensus rather than replaying the full discussion history. Finally, D2MDT fuses the refined consensus report with structured EHR representations for prediction. Experiments on mortality prediction show that D2MDT improves both predictive performance and consultation efficiency. We release the code online to ease the reproducibility of this paper.

---


### 220. [SAGE: A Quantitative Evaluation of Socialized Evolution in Agent Ecosystems](https://arxiv.org/abs/2606.03544)

**<font color=#1a73e8>作者：</font>** Linyue Pan, Yaoming Zhu, Lin Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving language agents are typically evaluated in isolation: an agent attempts a task, receives feedback, and iteratively refines its own behavior. Yet agents increasingly operate alongside peers whose strategies and outcomes are publicly visible. This raises an under-studied question: when does shared experience produce improvements that self-improvement alone cannot achieve? We introduce SAGE (Social Agent Group Evolution),an evaluation framework that compares two compute-matched conditions: SocialEvo, where agents from five distinct model families co-evolve with access to all peers' histories; and SelfEvo, where each agent receives the same number of task attempts but sees only its own past, which is conventional in self-improving agent studies. We instantiate SAGE in three arenas: open-ended ML research, long-horizon economic planning, and strategic multiplayer play, evaluated across multiple evolutionary rounds. We find that group history is not a universal amplifier: the strongest agent does not exceed its self-evolution ceiling. However, agents that plateau under self-improvement can achieve significant breakthroughs when peer experience is available. In competitive settings, counterfactual controls reveal that agents improve generally rather than developing opponent-specific strategies. Across different forms of shared history, filtered peer traces and reflective summaries often outperform raw logs, indicating that social gains depend on abstraction rather than exposure volume. These findings reveal that peer-history gains are agent-specific, arena-dependent, and contingent on the capacity to abstract transferable knowledge from public traces.

---


### 221. [How Many Trees in a Random Forest? A Revisited Approach with Plateau Search and Optuna Integration](https://arxiv.org/abs/2606.03549)

**<font color=#1a73e8>作者：</font>** Vadim Porvatov, Andrey Dukhovny, Andrey Lange  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter optimization (HPO) for Random Forest faces a specific difficulty in tuning the number of trees: the predictive score typically improves monotonically with ensemble size, so standard methods such as Tree-structured Parzen Estimator (TPE) and Hyperband require a predefined search range and often drive the estimate toward its right boundary. Early-stopping strategies avoid fixing such a range, but can be sensitive to score noise and prone to premature stopping. To address this, we propose an integrated triplet-based plateau-search algorithm that removes the number of trees from the direct TPE search space and still exploits information accumulated across HPO trials. The method adaptively tracks a near-minimal sufficient ensemble size by monitoring relative changes in the out-of-bag (OOB) score across a triplet of forest sizes and shifting this triplet accordingly. This yields an automated and user-interpretable procedure based on a tolerance parameter. We also provide a theoretical analysis: we relate the proposed relative OOB-score criterion to the gap between the current and limiting scores, and derive an asymptotic variance estimate for the corresponding OOB-based absolute relative difference. Experiments show that the selected number of trees can differ substantially from the common heuristic: for most classical benchmark datasets it is smaller, whereas for some high-dimensional bioinformatics datasets, such as Arcene and Dorothea, it is larger. The source code and reproducible experiments are available at this https URL.

---


### 222. [From Prompt to Service: An SLM-Based Agent Orchestration Gateway for AI-Driven Virtual Worlds](https://arxiv.org/abs/2606.03557)

**<font color=#1a73e8>作者：</font>** Louis Nisiotis, Aimilios Hadjiliasi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative AI capabilities expand, AI-driven virtual worlds face a growing architectural challenge. Users interact through in-world interfaces in multimodal ways, yet their requests demand fundamentally different AI backend models and computational resources. Embedding these capabilities directly into virtual world systems reduces extensibility, complicates maintenance, and limits the ability to coordinate services distributed across edge and cloud infrastructure. This paper presents an SLM-based Agent Orchestration Gateway, a lightweight runtime coordination mechanism that decouples a virtual world client from heterogeneous AI backends through intent-driven service routing. An edge-deployed SLM classifies the semantic intent of each user prompt, a configurable service registry validates and resolves the routing decision, and the selected backend is invoked transparently, enabling new AI capabilities to be introduced in the virtual world without modifying the client application. The gateway is implemented and evaluated within the InterwovenXR virtual museum testbed. The evaluation shows that compact SLMs can serve as reliable intent routers on edge hardware, and that task-specific fine-tuning can transform sub-billion-parameter models into practical, low-latency routers. A layered configuration pairing a fine-tuned sub billion-parameter model as router with a larger SLM for conversational response generation is shown to be deployable on mid-range edge hardware and more efficient than delegating both responsibilities to a single model. The findings show that SLMs can support practical AI service orchestration in virtual worlds and the work contributes an evaluated architecture for scalable, extensible, and edge-supported AI interaction, enabling virtual agents become access points to distributed generative AI services.

---


### 223. [Analytical Evaluation of DCA Convergence Properties for Minimizing Prediction Functions of Gaussian RBF Support Vector Regression](https://arxiv.org/abs/2606.03559)

**<font color=#1a73e8>作者：</font>** Yohei Kakimoto, Yuto Omae, Hirotaka Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For nonconvex optimization problems whose objective is the prediction function of a trained Support Vector Regression (SVR) model with the Gaussian radial basis function (RBF) kernel (RBF-SVR), we present a framework that applies the difference of convex functions (DC) algorithm (DCA) by exploiting the analytical structure of the RBF kernel to construct an explicit DC decomposition. Specifically, we derive in closed form both the lower bound $\mu$ of the strong convexity parameter of the DC components and the upper bound $L$ of the gradient Lipschitz constant of the subproblem. Both $\mu$ and $L$ are determined solely by the post-training dual-coefficient sum $C_{\alpha}$ and the RBF kernel parameter $\gamma$, together with the DC decomposition parameter $\rho$, and they share a common leading term $C_{\alpha}\rho$. Through numerical experiments on six benchmark functions, we show that $C_{\alpha}\rho$ is the primary single quantity characterizing both the convergence properties and the initial-point dependence of DCA, and further demonstrate that it decomposes into two independent pathways, $C \to C_{\alpha}$ and $\gamma \to \rho$, with its primary variation governed by the SVR hyperparameters $(C, \gamma)$. Together, these results allow the convergence properties of DCA on RBF-SVR to be assessed in advance through the single scalar quantity $C_{\alpha}\rho$: approximately from $(C, \gamma)$ before training, and exactly in closed form after training.

---


### 224. [The Comparative Trap: How Social Comparison Orientation Drives Problematic Generative AI (GenAI) Use](https://arxiv.org/abs/2606.03560)

**<font color=#1a73e8>作者：</font>** Xuchao Zhang, Jihye Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although Generative AI (GenAI) improves task efficiency in the short term, it creates competitive pressures that perpetuate individuals' fear of being eliminated, thereby increasing the risk of problematic use. Existing research has focused on the perspective of individual psychological vulnerability, but has neglected the social comparison context caused by GenAI. This study examines the direct effects of social comparison orientation on problematic GenAI use and explores their indirect effects via emotional and cognitive mechanisms, grounded in the Person-Affect-Cognition-Execution (I-PACE) model. The research analyzed data from 396 Chinese GenAI users using SEM and bootstrap methods. Findings show that social comparison orientation has a significant direct impact on problematic GenAI use and can additionally influence AI flow and perceived irreplaceability through fear of missing out (FoMO), finally leading to problematic GenAI use.

---


### 225. [Efficient Transformer-Based Localized Patch Sampling for Choroid Plexus Segmentation in Multiple Sclerosis](https://arxiv.org/abs/2606.03566)

**<font color=#1a73e8>作者：</font>** Po-Jui Lu, Alessandro Cagol, Mario Ocampo-Pineda 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: The lateral ventricle choroid plexus (LVCP) is gaining recognition as a key imaging biomarker for multiple sclerosis (MS) related to physical disability and neuroinflammation. Yet, manual segmentation of the LVCP is highly tedious, restricting its use in broad clinical trials and longitudinal assessments. This research aims to develop a SwinUNETR-driven pipeline that leverages targeted intra- and peri-ventricular small patch sampling to automatically segment the LVCP in MS from both standalone and multi-modal MRI inputs. Methods: We retrospectively assessed 3T MRI scans across three sets of data stemming from two separate MS-dominant cohorts (Dataset 1: n=177; Dataset 2: n=177; expanded test set: n=388). Our method employed a SwinUNETR architecture trained on 32x32x32 voxel patches, benchmarking it against the 3D UXNET model. The primary metric for evaluation was the Dice Similarity Coefficient (DSC), supplemented by computational demand (GFLOPs) and the 95th percentile Hausdorff Distance (HD95). Results: On the extended test set, the SwinUNETR model secured a mean DSC of 0.868 (95% CI: 0.863-0.872) with MPRAGE and FLAIR combined, showing a statistically significant gain over UXNET (DSC: 0.858 [95% CI: 0.853-0.862], p<0.0001). When restricted to standalone FLAIR inputs, the transformer-based approach sustained a high DSC of 0.863, while the spatial localization of UXNET worsened considerably (HD95: 1.86 vs. 3.00 mm). Importantly, the proposed framework lowered computational load by 99% (91.8 vs. 22,080 GFLOPs). By integrating localized patch sampling with a SwinUNETR architecture, this methodology offers an accurate, robust, and statistically superior alternative to current leading models for LVCP segmentation. Its vast reduction in computational cost makes it ideal for widespread implementation in clinical and research environments.

---


### 226. [Learned Non-Maximum Suppression for 3D Object Detection](https://arxiv.org/abs/2606.03568)

**<font color=#1a73e8>作者：</font>** Timo Osterburg, Stefan Schütte, Torsten Bertram  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-processing is a critical stage in LiDAR-based 3D object detection, where dense and overlapping proposals must be filtered for compact and reliable perception. This work introduces two learned filtering modules that replace heuristic non-maximum suppression (NMS) by leveraging relations among detections. D2D-Rescore employs transformer-based detection-to-detection (D2D) attention, while GossipNet3D adapts the 2D GossipNet concept to 3D through localized message passing in bird's-eye view. A metric-aware matching strategy aligned with the nuScenes evaluation protocol ensures consistent training and validation behavior, improving overall detection performance. Both approaches improve mean average precision (mAP), nuScenes detection score (NDS), and true positive quality compared to CircleNMS, particularly for small and infrequent classes, while adding minimal computational overhead. These results demonstrate that learned, detection-level filtering can enhance 3D detector reliability without modifying the base network, offering a principled alternative to heuristic suppression. Code is available at this https URL .

---


### 227. [Channel Chart Location Privacy Based on Geo-Indistinguishability](https://arxiv.org/abs/2606.03571)

**<font color=#1a73e8>作者：</font>** Atsu Kokuvi Angélo Passah, Rodrigo C. de Lamare, Arsenia Chorti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Channel charting enables location-based services (LBSs) without requiring explicit position information by using pseudo-locations from the channel chart. While this property implies inherent privacy advantages, it does not provide formal privacy guarantees. In this work, we address location privacy in channel charting referred to as chart location indistinguishability (CLI), which extends geo-indistinguishability (GI) to channel charting representations. In order to achieve CLI, a standard planar Laplace mechanism is investigated and a geometry-aware Mahalanobis norm planar Laplace (MNPL) mechanism is devised. The proposed MNPL mechanism perturbs the channel chart by injecting noise aligned with the local structure of the chart. In the CLI framework with MNPL, privacy is defined in latent channel chart manifolds using locally adaptive covariance derived from chart neighborhoods, while preserving manifold topology under privacy constraints. In addition, differential privacy is considered as a privacy baseline. The proposed approach is evaluated across multiple channel charting schemes. The performance is assessed using utility metrics such as quality loss (QL) and range query error (RQE), as well as geometry-aware metrics including trustworthiness (TW) and continuity (CT). Numerical results demonstrate that the proposed privacy mechanism provides strong privacy guarantees while preserving the channel chart for LBSs tasks.

---


### 228. [Diffusing in the Right Space: A Systematic Study of Latent Diffusability](https://arxiv.org/abs/2606.03578)

**<font color=#1a73e8>作者：</font>** Tianxiong Zhong, Xingye Tian, Xuebo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models leverage visual tokenizers to compress images into latent spaces for efficient generative modeling. However, better reconstruction quality of a tokenizer does not necessarily translate into better generation quality, suggesting that latent representations should be evaluated not only by fidelity but also by their diffusability. Recent studies have proposed diverse explanations for diffusion-friendly latent spaces, including semantic separability, affine equivariance, distribution uniformity, spatial structure, spectral smoothness, and manifold continuity. Yet these properties are often validated on a limited set of tokenizers, leaving it unclear which factors are most predictive of downstream generation quality and whether such conclusions hold beyond the specific settings in which they are introduced. In this work, we conduct a systematic study of latent diffusability by training a large collection of tokenizers with diverse regularization strategies, architectures, and latent configurations, and evaluating them with multiple downstream diffusion backbones. Our analysis identifies several latent properties that consistently correlate with generation quality and exhibit strong generalization across experimental settings. Beyond existing metrics, we introduce Velocity Irreducible Variance (VIV), a measure of velocity ambiguity induced by trajectory crossings. Extensive experiments show that VIV is one of the most stable predictors of generation quality.

---


### 229. [UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion](https://arxiv.org/abs/2606.03581)

**<font color=#1a73e8>作者：</font>** Ye Wu, Ruiqi Song, Baiyong Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unstructured scenes present unique challenges for autonomous driving, as irregular obstacles and sparse scene layouts undermine the effectiveness of traditional perception methods such as 3D object detection. 3D semantic occupancy prediction has emerged as a prominent focus due to its ability to provide dense spatial representations by assigning semantic labels to individual voxels in 3D space. However, directly applying 3D semantic occupancy prediction to unstructured scenes remains challenging because scene sparsity hinders effective cross-modal fusion and the more severe long-tail distribution in these scenarios further degrades prediction performance. To validate the effectiveness of our approach, we construct a dedicated dataset of unstructured scenes collected from open-pit mines. Based on this, we propose UnsOcc, a multi-modal 3D semantic occupancy prediction framework that improves robustness in unstructured environments. At its core, we introduce a rendering-based fusion module, RenderFusion, which enhances cross-modal feature alignment through bidirectional rendering supervision. Furthermore, we propose GSRefinement, a detail-aware auxiliary supervision method based on Gaussian Splatting that projects sparse 3D occupancy predictions into dense 2D semantic segmentation maps, enabling effective supervision for long-tail categories. Extensive experiments on both the open-pit mine dataset and the nuScenes dataset demonstrate that our method significantly outperforms existing state-of-the-art approaches.

---


### 230. [Training a Predictive Coding Network on ImageNet using Equilibrium Propagation](https://arxiv.org/abs/2606.03584)

**<font color=#1a73e8>作者：</font>** Tugdual Kerjan, Rasmus Høier, Benjamin Scellier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equilibrium Propagation (EP) is a physics-based training framework that has primarily been employed in energy-based models, including continuous Hopfield networks, nonlinear resistive networks and coupled phase oscillators. However, EP's practical applications have so far remained limited to relatively small-scale problems. Predictive coding networks (PCNs), another class of energy-based models rooted in computational neuroscience, are typically trained with a specialized algorithm and have likewise not yet been demonstrated at large scale. In this work, we develop an EP-based training method for PCNs which combines the centered variant of EP with a novel equilibration scheme for PCNs. Using this approach, we train a 10-layer convolutional PCN (VGG10) on full-size ImageNet, achieving 13.23\% test error rate on the top-5 classification task, close to the 12.2\% backpropagation baseline. To our knowledge, this is the first demonstration of both PCNs and EP-based training at ImageNet scale. These results significantly extend the scalability of both approaches and suggest that the primary challenges in scaling EP in other physical systems may come more from the computational properties of these systems than from inherent limitations of the EP framework.

---


### 231. [Exploiting Verification-Generation Gap: Test-Time Reinforcement Learning with Confidence-Conditioned Verification](https://arxiv.org/abs/2606.03608)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Jianfeng Shan, Wenpei Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning has emerged as a promising paradigm for enhancing the complex reasoning abilities of large language models in a completely label-free manner. Despite existing studies focusing on Pass@1 performance, optimizing Pass@k remains under-explored yet critical in label-free settings, which measures generation coverage for sustained exploration. Optimizing Pass@k in label-free setting is highly non-trivial, as directly applying the Pass@k advantage designs effective for RLVR yields unsatisfactory performance. Through in-depth empirical analysis, we discover the root causes hindering performance: pseudo-label estimations for low-confidence samples have a high probability of being incorrect, while candidate answers for high-confidence samples suffer from severe diversity collapse. To overcome these hurdles, we propose TTRL-CoCoV (Test-Time Reinforcement Learning with Confidence-Conditioned Verification), a novel confidence-adaptive framework that expands Pass@k coverage and improves Pass@1 performance. Based on our key insight that verification capability generally leads generation capability, TTRL-CoCoV employs a confidence-conditioned mechanism: for high-confidence samples, it bootstraps verifier and applies an exploration-enhancing reward to prevent diversity collapse; for low-confidence samples, it delegates pseudo-label selection to the verifier to filter incorrect pseudo-labels; and for medium-confidence samples, it bypasses verification entirely. Extensive experiments demonstrate that TTRL-CoCoV outperforms the best competing methods across 6 widely-recognized benchmarks, achieves average absolute gains of +9.8% in Pass@1 and +18.7% in Pass@16 over TTRL, and even achieves absolute Pass@1 improvements of up to +5.0% across multiple reasoning benchmarks when compared against fully supervised RL methods. Our code repository: this https URL.

---


### 232. [SkelHCC: A Hyperbolic CLIP-Driven Cache Adaptation Framework for Skeleton-based One-Shot Action Recognition](https://arxiv.org/abs/2606.03610)

**<font color=#1a73e8>作者：</font>** Yanan Liu, Anqi Zhu, Jingmin Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition aims to understand human behaviors from body joint sequences and is especially challenging in the one-shot setting, where only a single labeled exemplar is available for each novel action. A key challenge is learning representations that capture the hierarchical and compositional structure of human motion while aligning effectively with high-level action semantics under extreme data scarcity. Existing approaches, largely based on Euclidean embeddings and low-level motion cues, struggle to model the tree-like organization of skeleton data, limiting cross-modal alignment and generalization to unseen action categories. We propose SkelHCC, a unified skeleton hyperbolic CLIP-driven cache adaptation framework for one-shot skeleton-based action recognition. SkelHCC introduces an Explicitly Hierarchical Hyperbolic CLIP (EH-HCLIP) module that embeds skeleton sequences and action language into a shared hyperbolic space. By leveraging the negative curvature and exponential volume growth of hyperbolic geometry, EH-HCLIP naturally encodes the joint-part-body hierarchy of human anatomy and yields structurally consistent cross-modal representations. To support efficient one-shot adaptation, SkelHCC further integrates a training-free LLM-guided Multi-granularity Voting Cache (LMV-Cache) for context-aware inference. Experiments on NTU RGB+D 60, NTU RGB+D 120, and PKU-MMD demonstrate that SkelHCC consistently outperforms state-of-the-art methods.

---


### 233. [Q-FE: A Quantum-Native 6G Far-Edge Architecture Securing Industrial IoT Digital Twins via CSIDH-PQC and Asynchronous Federated Learning](https://arxiv.org/abs/2606.03611)

**<font color=#1a73e8>作者：</font>** Vincenzo Sammartino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sixth-generation (6G) wireless networks will underpin ultra-dense Industrial IoT (IIoT) ecosystems in which resource-constrained Far-Edge devices -- autonomous mobile robots, industrial actuators, connected vehicles -- must simultaneously satisfy sub-millisecond latency, $10^{-7}$-class reliability, and decades-long cryptographic security. Current architectures delegate Digital Twin (DT) computation to centralised cloud or Mobile Edge Computing (MEC) servers, incurring prohibitive round-trip latency, and rely on classical public-key cryptography vulnerable to quantum attacks under the harvest-now, decrypt-later (HNDL) threat model. We propose Q-FE, a Quantum-Native 6G Far-Edge architecture integrating three co-designed components: (i) Micro-Digital Twins ($\mu$DTs) co-located with 6G base stations and high-capability endpoints; (ii) a Cross-Layer Post-Quantum Key Exchange module embedding CSIDH-512 isogeny key material directly within MAC-layer control frames, exploiting the scheme's uniquely compact keys ($\le 64$ bytes) to avoid packet fragmentation; and (iii) an Asynchronous Federated Learning (AFL) protocol governed by lightweight DAG smart contracts at MEC nodes, eliminating straggler bottlenecks and preventing model-poisoning and Sybil attacks without exposing raw data. End-to-end simulations (NS-3 + PySyft) demonstrate that Q-FE reduces MAC-layer overhead by 62% versus ML-KEM/Kyber-1024, maintains P99.9 URLLC latency at 0.78 ms, and accelerates global-model convergence by 31% over synchronous Federated Learning. Protocol complexity analysis confirms $O(N \log R)$ per aggregation round, and $\mu$DT handover migration completes in $1.9 \pm 0.3$ ms across $10^4$ simulated events. A formal threat model confirms resilience against quantum eavesdropping, model-poisoning, and Sybil attacks.

---


### 234. [Physics-Guided Policy Optimization with Self-Distillation](https://arxiv.org/abs/2606.03620)

**<font color=#1a73e8>作者：</font>** Ke Wang, Yuning Wu, Haoran Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distilled policy optimization (SDPO) has become a popular paradigm for LLM post-training, where a model learns from its own predictions conditioned on privileged information. SDPO, however, is sensitive to how much each update step should be trusted: corrections from a self-teacher can be highly informative on some batches and misleading on others, and applying them uniformly with a fixed step size can destabilize training. Drawing inspiration from viscous-fluid dynamics and formalizing the analogy at the SDE level, we propose Physics-Guided Policy Optimization (PGPO), which introduces an information-modulated step-size multiplier derived from a mutual-information estimate between the student's predictions and the feedback-conditioned teacher. We show that this modulation preserves the order-1 weak-approximation guarantees of vanilla SGD, and incurs negligible overhead per iteration. We evaluate PGPO on the Science-QA dataset, where it outperforms SDPO on 3 of the 4 domains with gains of up to +4.5 points, while remaining stable in a setting where SDPO collapses late in training.

---


### 235. [Building Reliable Long-Form Generation via Hallucination Rejection Sampling](https://arxiv.org/abs/2606.03628)

**<font color=#1a73e8>作者：</font>** Lin Li, Georgia Channing, Suhaas M Bhat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable progress in open-ended text generation, yet they remain prone to hallucinating incorrect or unsupported content, which undermines their reliability. This issue is exacerbated in long-form generation due to hallucination snowballing, a phenomenon where early errors propagate and compound into subsequent outputs. To address this challenge, we propose a novel inference-time hallucination mitigation framework, named Segment-wise HAllucination Rejection Sampling (SHARS), which uses an arbitrary hallucination detector to identify and reject hallucinated segments during generation and resample until faithful content is produced. By retaining only confident information and building subsequent generations upon it, the framework mitigates hallucination accumulation and enhances factual consistency. To instantiate this framework, we adopt semantic uncertainty as the detector and introduce several vital modifications to address its limitations and better adapt it to long-form text. Our method enables models to self-correct hallucinations without requiring external resources such as web search or knowledge bases, while remaining compatible with them for future extensions. Empirical evaluations on standardized hallucination benchmarks demonstrate that our method substantially reduces hallucinations in long-form generation while preserving or even improving the informativeness of generation. Code is available at: this https URL.

---


### 236. [VidMsg: A Benchmark for Implicit Message Inference in Short Videos](https://arxiv.org/abs/2606.03635)

**<font color=#1a73e8>作者：</font>** Issar Tzachor, Michael Green, Rami Ben-Ari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding short online videos involves more than identifying visible objects and actions; video makers often include an underlying message or purpose in the clip. We introduce VidMsg, a benchmark for evaluating implicit message understanding in short, internet-native video clips. VidMsg contains 400 YouTube-derived clips across 9 practical topic areas and 52 fine-grained target messages, covering domains such as career and finance, education, health and well-being, culture, safety, sustainability, and lifestyle. VidMsg is constructed through a message-first pipeline: an LLM first translates target messages into indirect search scenarios, which are used to retrieve candidate clips. Human annotators then retain clips that convey the intended message without being overly explicit. VidMsg is designed primarily for bidirectional message-clip retrieval for scalable applications such as video search and recommendation, where systems must capture holistic video understanding. In addition to retrieval, VidMsg includes a diagnostic multiple-choice QA benchmark, where models select the intended message of a clip from semantically related alternatives. Experiments with contemporary video-language and retrieval models show that strong models often fail on VidMsg, because the task requires pragmatic inference, integration of contextual cues, and discrimination among semantically close messages. We also introduce VidVec-Msg, a baseline method that improves message-oriented retrieval while leaving substantial headroom for future work.

---


### 237. [A Benchmark for Semi-supervised Multi-modal Crowd Counting](https://arxiv.org/abs/2606.03646)

**<font color=#1a73e8>作者：</font>** Haoliang Meng, Xiaopeng Hong, Yabin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper constructs the first benchmark on semi-supervised multi-modal crowd counting. To lay the foundation for this unexplored task, we first formulate the semi-supervised multi-modal setting and a standardized protocol that specifies the labeled-unlabeled data partition across different labeled ratios. Next, to establish solid reference points, we carefully tailor a diverse set of representative baselines, including existing fully supervised multi-modal methods and semi-supervised single-modal methods. Then, we carefully evaluate their performance under our proposed benchmark. Codes and the data partition will be released on this https URL.

---


### 238. [Graph Regularized Non-negative Reduced Biquaternion Matrix Factorization for Color Image Recognition](https://arxiv.org/abs/2606.03654)

**<font color=#1a73e8>作者：</font>** Hailang Wu, Yonghe Liu, Bingxuan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-negative reduced biquaternion matrix factorization (NRBMF) uses the product of reduced biquaternion (RB) matrices to incorporate the non-negativity constraints of color image pixels into the factorization process. However, NRBMF mainly focuses on reconstruction accuracy and does not exploit the local geometric structure of image data, which may limit the discriminative ability of the learned low-dimensional features. To address this issue, we propose a graph regularized non-negative reduced biquaternion matrix factorization (GNRBMF) model for color image recognition. The proposed model incorporates a graph Laplacian regularizer into the reduced biquaternion coefficient matrix, encouraging nearby samples in the original space to have similar representations in the learned feature space. Meanwhile, GNRBMF retains the non-negativity-preserving property of NRBMF in the reduced biquaternion domain. To solve the optimization problem, a component-wise alternating projected gradient algorithm is derived, and its convergence properties are analyzed. Experimental results demonstrate that the proposed GNRBMF model achieves competitive or superior recognition performance in some tested settings.

---


### 239. [Towards Non-Monotonic Entailment in Propositional Defeasible Standpoint Logic](https://arxiv.org/abs/2606.03655)

**<font color=#1a73e8>作者：</font>** Nicholas Leisegang, Thomas Meyer, Ivan Varzniczak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work in defeasible reasoning has seen notions of preferential semantics and entailment in the style of Kraus et al. applied to modal logics. However, work in this field has focussed primarily on satisfiability checking, and monotonic notions of entailment, which may be inferentially weak. One particular modal logic where this has been introduced is propositional standpoint logics, where modalities can express the views of different viewpoints. This has resulted in the formalisation of propositional defeasible standpoint logic (PDSL). In this paper, we propose a means of lifting the class of (non-monotonic) rational entailment relations from traditional KLM-style reasoning to a fragment of PDSL. In order to do so, we extend the expressivity of PDSL via situated standpoint conditionals, allowing us to talk about a defeasible conditional holding in the context of a given standpoint. This allows us to re-characterise the syntax of PDSL in terms of situated conditionals, and shows that a large fragment of PDSL is expressible as a set of situated conditionals. We then focus on characterising non-monotonic entailment in this fragment, defining a method to transport any ranking-based entailment relation from the propositional case into the PDSL case. This is first described in the general case and then considered in the specific cases of rational and lexicographic closures, providing a faithful translation of each inference into PDSL. We also show that entailment-checking in this fragment of PDSL can be done largely using algorithms from the propositional case, while preserving complexity bounds.

---


### 240. [Beyond Single Solution: Multi-Hypothesis Collaborative Deep Unfolding Network for Image Compressive Sensing](https://arxiv.org/abs/2606.03666)

**<font color=#1a73e8>作者：</font>** Wenxue Cui, Hualin Li, Yuhang Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deep unfolding networks (DUNs) have advanced Compressive Sensing (CS) by effectively integrating iterative optimization with deep learning architectures. However, most CS approaches predominantly confine their inference to a single solution space, neglecting the inherent ill-posedness of CS problems that intrinsically permits multiple plausible candidate hypotheses. In this paper, a novel Multi-Hypothesis Collaborative Deep Unfolding CS Network (MHC-DUN) is proposed, which explicitly models and leverages multiple hypotheses by jointly optimizing across diverse solution spaces. Specifically, following the Proximal Gradient Descent algorithm, MHC-DUN jointly performs gradient descent and proximal mapping within this multi-hypothesis paradigm. i) For gradient descent, a well-designed AlphaNet is introduced to dynamically predict spatially varying step sizes for all hypotheses, enabling collaborative gradient updates across multiple solutions. ii) For proximal operator, a sophisticated multi-hypothesis collaborative proximal mapping module is designed, which leverages both intra-hypothesis and inter-hypothesis correlation priors to jointly refine multiple solutions. To enable end-to-end training, a novel composite loss function is designed, which balances measurement fidelity, hypothesis diversity, and reconstruction accuracy, encouraging exploration of complementary solutions while maintaining reconstruction fidelity. Experimental results reveal that the proposed CS method outperforms existing CS networks.

---


### 241. [A Fast Methane Detection Pipeline on Board Satellites Based on Mag1c-SAS and LinkNet](https://arxiv.org/abs/2606.03675)

**<font color=#1a73e8>作者：</font>** Jonáš Herec, Vít Růžička, Rado Pitoňák 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methane is a potent greenhouse gas, and detecting leaks early via hyperspectral satellite imagery can help climate change mitigation efforts. Meanwhile, many existing hyperspectral missions only capture areas manually targeted by operators, thus missing potential events of interest. To overcome slow downlink rates cost-effectively, onboard detection is a viable solution. However, traditional methane detection methods are too computationally demanding for resource-limited onboard hardware. This work accelerates methane detection by focusing on efficient, low-power algorithms. In particular, we test fast target detection ACE and CEM methods that have not been previously used for methane detection and propose Mag1c-SAS -- a significantly faster variant of the current state-of-the-art Mag1c algorithm. To explore their detection potential, we integrate them with a machine learning model based on U-Net and LinkNet. We evaluate our methods on the STARCOP dataset and a novel EMIT-MSeg dataset, which we introduce and open-source alongside a high-quality annotation strategy. The proposed Mag1c-SAS approach proves highly effective by operating ~80x faster than the original Mag1c approach, providing a visually similar, but noisier result. When additionally paired with the lightweight LinkNet approach, it effectively reduces noise, achieving AUPRC score improvements of over 30 pp on EMIT-MSeg compared to the baseline Mag1c approach, and an F1 score on STARCOP ~4 pp higher. We evaluate two novel band selection strategies and confirm the system's onboard viability through hardware profiling, demonstrating marginal power consumption and efficient CPU/RAM utilization. We release the final system in a user-friendly and lightweight PyPI library at: this https URL, alongside all experimental code, models, and data at: this https URL.

---


### 242. [SkillPyramid: A Hierarchical Skill Consolidation Framework for Self-Evolving Agents](https://arxiv.org/abs/2606.03692)

**<font color=#1a73e8>作者：</font>** Yuan Xiong, Ziqi Miao, Qian Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI agents can flexibly invoke skills to solve complex tasks, but their long-term improvement is fundamentally constrained by a lack of systematic skill construction, accumulation, and transfer. In particular, without a unified framework for skill consolidation, agents tend to redundantly construct similar capabilities across different tasks, are unable to effectively transform experience into reusable assets, and struggle to generalize task-specific skills to novel scenarios. To address this limitation, we propose SkillPyramid, a skill consolidation framework that reuses existing skill experience for broader task generalization. Operating on a hierarchical skill topology, SkillPyramid further introduces a self-evolution mechanism that enables agents to compose, validate, and incorporate new skills during task execution. Experiments on ALFWorld, WebShop, and ScienceWorld across four backbone models show that SkillPyramid substantially increases the average reward by 38.0% and reduces execution steps by 27.7%. Overall, our method transforms a skill collection from a static resource pool into a dynamic evolution system.

---


### 243. [Don't Forget Your Embeddings: Robust Knowledge Erasure via Precise Editing of Embeddings](https://arxiv.org/abs/2606.03695)

**<font color=#1a73e8>作者：</font>** Clara Haya Suslik, Or Shafran, Mor Geva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models are increasingly deployed in real-world applications, the ability to erase specific knowledge from them becomes critical for safety and compliance. Prominent methods seek persistent removal by updating the model's parameters, yet the target knowledge often can be recovered through adversarial prompting or relearning. In this work, we hypothesize this limitation stems in part from existing methods overlooking the embedding layer. To address this, we introduce EMBedding ERasure (EMBER), a plug-n-play erasure module that leverages Sparse Matrix Factorization for precise erasure of concept-related features from token embeddings. Through comprehensive evaluations across diverse concepts on Gemma-2-2B-it and Llama-3.1-8B-Instruct, we find that augmenting existing methods with EMBER consistently improves erasure efficacy and specificity across task formats, with minimal coherence loss. Moreover, it dramatically improves robustness to relearning, reducing regained accuracy by up to 50%, limiting it to 35% on Llama compared to 70%-76% for prior methods. Further analysis shows that the coherence cost is localized, affecting only a small set of concept-exclusive tokens. Our work establishes that precise embedding-level intervention is necessary for robust concept erasure, and demonstrates that existing methods can benefit from such augmentation.

---


### 244. [Ghost: Plausible Yet Unlearnable Trajectories via On-Manifold Substitution for Next-POI Privacy](https://arxiv.org/abs/2606.03711)

**<font color=#1a73e8>作者：</font>** Zhenyu Yu, Jihong Guan, Shuigeng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A publisher who releases check-in trajectories inadvertently publishes a strong predictor of every user's future locations. We address this risk by generating unlearnable trajectories, perturbed sequences that yield victim models with degraded next-Point-of-Interest (next-POI) accuracy on clean test inputs. Direct ports of image-domain unlearnable examples fail on two counts. The published data must remain geographically and semantically plausible, and the perturbation must resist purification adversaries that exploit the structure of randomized defences. We propose Ghost, a manifold-aligned framework whose perturbations look like plausible human check-in sequences yet leave no learnable signal behind. Ghost steers each substitution onto the real-trajectory manifold through a frozen trajectory language model, so a denoising-bridge adversary has nothing to invert and a context-free frequency-table adversary recovers a near-uniform distribution. Across two standard benchmarks, and four attacker postures, Ghost achieves protection-gap competitive with the strongest deterministic baseline (PGD) while attaining the lowest restored accuracy under the bigram adaptive purification adversary on both datasets, and lies within one per-cell standard deviation of PGD on the protection-versus-purification-resistance plane. Ablations confirm the manifold prior subsumes the entropy-floor knob of prior randomized defences, with the frequency-table adversary's survival gap remaining within 0.04 even when twenty percent of the pairs are leaked.

---


### 245. [Don't Trust Us: A privacy-by-design android malware detection pipeline](https://arxiv.org/abs/2606.03714)

**<font color=#1a73e8>作者：</font>** Emmanuele Massidda, Diego Soi, Giorgio Giacinto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android malware detection increasingly relies on collecting and processing sensitive user data, including device identifiers, network artifacts, and runtime traces, while privacy is too often treated as a secondary concern. Existing privacy-aware approaches typically enforce privacy after data collection, for example, through anonymization, encryption, or federated learning, yet still require access to user information and therefore demand a high level of user trust in systems that already operate with privileged access to device activity. We argue that this requirement should be removed rather than managed. Android malware detection should be privacy-aware by design, so that effective analysis does not depend on sensitive data being accessed in the first place. To this end, we first formalize a set of design requirements for privacy-by-design detection and then implement each requirement in a comprehensive pipeline. First, static analysis is performed to extract relevant data from each APK, following the Drebin representation, which is then submitted to an SVM after vectorization. The model is equipped with a dual-reject threshold rule that either commits to a confident decision or defers uncertain samples to a dynamic analysis stage within a sandboxed environment, so that genuine user information never enters the analysis loop. Results confirm that, on a temporally split dataset spanning from 2024 to 2025, the pipeline achieves an F1 score of 0.87 with the first static analysis stage, deferring only 6.7% of test samples to secondary dynamic analysis. Additionally, dynamic sandboxing helps recognize applications' maliciousness with high confidence without extracting any sensitive data. These results demonstrate that strong detection performance is achievable without sacrificing user privacy.

---


### 246. [Text-to-Image Models Need Less from Text Encoders Than You Think](https://arxiv.org/abs/2606.03715)

**<font color=#1a73e8>作者：</font>** Nurit Spingarn, Noa Cohen, Tamar Rott Shaham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models rely on text prompts as their primary interface to human intent. Prompts are encoded by a text encoder into embeddings that condition the image generation process. Beyond individual token meanings, text embeddings encode contextual information across the full prompt, such as compositionality and attribute binding. However, whether image models actually exploit this richer information remains underexplored. Here, we address the question: Which aspects of text representation are essential for image generation? We show that text-to-image diffusion transformer-based models commonly rely only on two relatively straightforward aspects of text representations: (i) the merging of adjacent tokens into a word representation, for words spanning multiple tokens, and (ii) word order, which is imprinted by the positional embedding of the text-encoder. To show this, we construct a new text embedding that encodes only individual word meanings and order but lacks any contextual information about the full prompt. We find that this bag of position-tagged words representation is sufficient to successfully guide image generation, achieving visual quality and text fidelity that are on par with full text embedding-guided generation. This demonstrates that, contrary to common belief, text-to-image models often do not use the rich information encoded in the text embedding beyond individual word meanings and word order. Instead, the decoding of complex linguistic structures is performed by the image model itself. Project webpage: this https URL

---


### 247. [Unveiling the Structure of Do-Calculus Reasoning via Derivation Graphs](https://arxiv.org/abs/2606.03719)

**<font color=#1a73e8>作者：</font>** Clément Yvernes, Emilie Devijver, Marianne Clausel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The do-calculus defines a general system of inference for interventional queries, allowing causal quantities to be transformed through successive applications of its rules. This process induces a rich space of equivalent interventional expressions, but combining and ordering these rules remains challenging. In this work, we introduce derivation graphs, which represent how do-calculus rules are applied and combined, and characterize the full space of observational and interventional probabilities which are equivalent under the do-calculus. The structure of these graphs yields a simple procedure that uses at most four applications of do-calculus rules. Finally, we show how applying identification algorithms to equivalent causal queries produces multiple valid estimands for the same causal quantity, eventually yielding more efficient estimators.

---


### 248. [Compress then Merge: From Multiple LoRAs into One Low-Rank Adapter](https://arxiv.org/abs/2606.03723)

**<font color=#1a73e8>作者：</font>** Zhengbao He, Ruiqi Ding, Zhehao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) enables parameter-efficient specialization of foundation models, but the proliferation of task-specific adapters fragments capabilities across many adapters, complicating reuse and deployment. We study the problem of merging $T$ LoRAs into a single rank-$r$ LoRA, thereby preserving the benefits of low-rank structure. Existing Merge-then-Compress pipelines treat the rank constraint as an afterthought: they merge adapters in the full parameter space, then compress the merged result to rank $r$ via truncated SVD. However, full-parameter merging may destroy the low-rank structure, making it difficult for subsequent compression to recover an effective rank-$r$ LoRA. We propose Compress-then-Merge (CtM), a reversed pipeline that enforces the rank-$r$ bottleneck before merging: CtM computes shared $r$-dimensional subspaces using only the LoRA weights to capture cross-adapter common structure, projects each adapter into the shared subspaces to obtain $r\times r$ coordinates, and then applies standard merging rules in this reduced space. CtM guarantees a rank-$r$ LoRA by construction, avoiding post-hoc truncation, and enables efficient computation in the core space spanned by concatenated LoRA factors. Experiments across multiple models and tasks show that CtM consistently outperforms existing single-LoRA-output baselines while narrowing the performance gap to full-parameter merging methods.

---


### 249. [Same Weights, Different Robot: A Deployment Safety View of VLA Policies](https://arxiv.org/abs/2606.03724)

**<font color=#1a73e8>作者：</font>** Jianwei Tai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies are often treated as checkpoint-defined objects: if the weights, prompt, and benchmark suite match, the deployment is assumed to be the same policy. Robot execution breaks this assumption because the same normalized model output can become a different physical action after action unnormalization and controller conventions are applied. This creates a deployment-safety gap: safety review can certify the checkpoint while missing the executable robot policy that reaches the controller. We formalize this gap as an executable policy specification problem: a VLA policy includes the learned model, action representation, metadata-selected unnormalizer, and controller-facing conventions. Under this view, identical checkpoints can be executable-inequivalent. For quantile-style action normalization, we derive a closed-form metadata mismatch transform and an ExecSpec certificate that measures action-space semantic drift without model inference or rollout. On LIBERO-Goal replay, substituting a plausible sibling metadata key yields mean drift 0.199 over six non-gripper action dimensions and reduces success from 28/28 to 2/28 under full substitution. On LIBERO-Spatial replay, the same substituted key reduces success from 26/26 to 0/26. The same full-substitution protocol gives 0/28 success for all four Object substitutions and 0/23 or 1/23 success on Long. Identity-key, replay-validity, no-op filtering, raw-vs-correct replay, mask/gripper, synthetic upper-bound, and OpenVLA-style unnormalizer interface checks rule out several simpler explanations. These results do not certify closed-loop or hardware safety. They support a narrower deployment-safety view: action-space metadata is part of the executable policy and should be checked before rollout.

---


### 250. [When to Re-Plan: Subgoal Persistence in Hierarchical Latent Reasoning](https://arxiv.org/abs/2606.03741)

**<font color=#1a73e8>作者：</font>** Ayushi Chadha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon reasoning requires a system to commit to medium-horizon intent without becoming rigid: re-plan too often and computation never coheres into multi-step structure; commit too long and the plan goes stale. We study this stability-adaptivity tradeoff in the latent reasoning setting, where multi-step computation occurs inside hidden state rather than externalized token traces. We extend the Hierarchical Reasoning Model (HRM) with a feudal-style manager-worker interface: a slow high-level module periodically emits a normalized directional subgoal that persists for P low-level steps, biasing the worker's hidden-state updates and supplying an intrinsic cosine alignment loss. On ARC and ConceptARC, we find that subgoal persistence -- not subgoal injection alone -- is the central knob: moderate periods P in [3, 6] consistently outperform both very frequent (P=1) and very long horizons, with a clear minimum LM loss at P=3 (1.544 vs. 1.674 at P=1, 1.640 baseline; replicated over 5 seeds at mean 1.595, std 0.045). The intrinsic alignment weight lambda shows a complementary narrow optimum (lambda approximately 0.05). A controlled ablation at past-sweet-spot lambda isolates learned directional structure -- not architectural capacity or auxiliary loss alone -- as the source of interference when the alignment signal exceeds its optimum. Together these findings implicate a design principle for compositional planning in latent reasoning systems: medium-horizon intent must be coherent across enough computational steps for compositional structure to form.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-312](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
