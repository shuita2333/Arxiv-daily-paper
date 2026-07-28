# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-442**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-442**

---

### 401. [From Machine Learning to Large-Scale EO Products: Best Practices for Making Maps](https://arxiv.org/abs/2607.24532)

**<font color=#1a73e8>作者：</font>** Ghjulia Sialelli, Robin Young, Yuchang Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have seen a rapid expansion in the production of large-scale geospatial maps derived from Earth observation (EO) data, driven largely by advances in machine learning (ML) and large computing infrastructure. Although the barrier to generating such maps has dropped substantially, established best practices have yet to emerge, and design decisions made early in the pipeline can quietly propagate errors into the final product. Producing a technically sound and scientifically credible product remains challenging. Choices made at every stage are tightly coupled: preprocessing decisions shape the training signal, dataset design governs what the model can learn and how reliably its performance can be assessed, and global-scale inference introduces engineering challenges in compute and data access at scale, as well as artifact mitigation. Furthermore, uncertainty quantification and independent map validation each require dedicated methodological attention that is often underestimated. This paper presents a concise, end-to-end account of the recommended practices spanning the pipeline from satellite data to an operational map product. We organize the discussion around six interconnected themes: the EO data infrastructure landscape, data selection and preprocessing, ML dataset construction and model training, uncertainty quantification, map production and distribution, and validation. This paper is a condensed version of a longer guide that provides greater depth across all stages, accessible online at this http URL.

---


### 402. [RemiAssist: A Therapist-Supporting System for Photo-Based Reminiscence Therapy in Dementia Care](https://arxiv.org/abs/2607.24536)

**<font color=#1a73e8>作者：</font>** Shuchang Xu, Minglong Tang, Junyan Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite growing interest in applying AI to photo-based reminiscence therapy (PRT) for people with dementia (PwD), existing systems primarily focus on PwD-AI interaction and often overlook therapists' critical role in practical PRT delivery. We present RemiAssist, a system that supports therapist-in-the-loop PRT through AI-assisted planning and real-time facilitation. RemiAssist incorporates two core techniques: (1) a Memory Graph, which organizes key life events from a PwD's photo collection into a hierarchical graph to support theme-centered intervention planning; and (2) a Context-Aware Guiding Strategy, which provides real-time suggestions to help therapists guide reminiscence conversations and respond to sensitive situations. A field study with eight therapist-PwD dyads suggests that RemiAssist was associated with a 44% improvement in planning efficiency and a 54% increase in conversation duration, and provided timely support for handling sensitive situations. We highlight opportunities for AI systems to empower therapists and enable more personalized reminiscence therapy in dementia care.

---


### 403. [The K-SCAN Clustering Algorithm](https://arxiv.org/abs/2607.24537)

**<font color=#1a73e8>作者：</font>** Filip Kosiorowski, Grzegorz Sroka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the Big Data era, the scalability of clustering algorithms constitutes a key challenge. Traditional density-based methods (e.g., DBSCAN) offer robustness to noise and the ability to detect non-linear clusters, yet their quadratic time complexity $O(N^2)$ drastically limits their applicability. Conversely, partitional algorithms (e.g., K-Means), with their linear complexity $O(N)$, impose sphericity on the resulting groups and fail in the presence of outliers. This paper presents K-SCAN -- a novel hybrid algorithm that optimizes this trade-off. The method integrates preliminary vector quantization (stochastic Mini-Batch K-Means) to extract a reduced set of weighted micro-clusters, followed by a subsequent density-based structural analysis. Empirical evaluation on datasets of up to $10^6$ samples confirms the linear computational complexity of the proposed solution. K-SCAN achieves more than a 3-fold speed-up over the hierarchical BIRCH algorithm, avoiding the costly management of tree-based structures. The method precisely identifies non-linear manifolds while maintaining structural stability (Adjusted Rand Index > 0.99), even with noise levels reaching 55\% of the data volume. The main limitation of the proposed algorithm, which could not be fully eliminated in the present study, remains its susceptibility to over-smoothing and its difficulty in separating clusters with highly heterogeneous local density. In complex visual spaces, this can lead to the loss of the finest topological details.

---


### 404. [From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages](https://arxiv.org/abs/2607.24542)

**<font color=#1a73e8>作者：</font>** Th{é}otime de la Selle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Text Recognition (ATR) now supplies digital humanities with large volumes of unstructured, heterogeneous, and often noisy text in ancient languages. Downstream semantic analysestext reuse identification, alignment, and semantic search-rely on sentence embeddings, yet existing methods transfer poorly to ancient languages: generic multilingual encoders underperform, specialized language models yield anisotropic representation spaces, and labeled similarity data is unavailable. We study two fully unsupervised strategies - TSDAE and contrastive sentence embedding (CSE) - that adapt a specialized token-level language model into a corpus-specific sentence encoder using only raw sentences. On the philologically central case of biblical reuse in patristic literature (2,935 expert-verified parallels in Latin and Ancient Greek, from Augustine, Jerome, and Athanasius), we decompose reuse identification into two separately evaluated tasks-binary detection and correspondence retrieval-and benchmark the adapted encoders against multilingual, specialized, distilled, and supervised fine-tuned baselines, as well as on artificially noised data simulating HTR artifacts and scribal abbreviations. The adapted encoders outperform all baselines on both tasks, with complementary profiles: TSDAE leads detection given a large in-domain corpus, while CSE leads retrieval, reaches its optimum with as few as 4-8k raw in-domain sentences-a few tens of seconds of training on a laptop GPU-and transfers across works and authors, including to noisy post-ATR text when retrained directly on it. UMAP atlases relate the geometric effect of each strategy to the measured gains, and the full pipeline-segmentation, fine-tuning, cross-corpus semantic search-is made available to non-specialists through the online tool Paraphrasis.

---


### 405. [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](https://arxiv.org/abs/2607.24552)

**<font color=#1a73e8>作者：</font>** Sofia Della Penna, Lorenzo Parracino, Luciano Pianese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise networks are continuously targeted by Advanced Persistent Threats (APTs), attack campaigns exploiting software vulnerabilities to compromise critical assets over time. As disclosed vulnerabilities grow, resource-constrained organizations must prioritize which ones to patch. Existing prioritization standards score vulnerabilities individually and cannot capture how a patching policy performs against an adversary that progresses through the network over time. Previous tools have simulated attack campaigns through Reinforcement Learning (RL), but either omit vulnerability management, leaving the attacker unopposed, or rely on synthetic networks disconnected from real threat data, and so cannot assess how a policy would fare against a realistic adversary. To fill this gap, we propose VulnGym, a simulation tool to evaluate vulnerability management policies. VulnGym simulates an RL-trained attacker, calibrated on real APT profiles, against a defender executing a configurable patching policy over a network with real Common Vulnerabilities and Exposures (CVEs). Both agents act on a shared, evolving network representation, so the attacker's progress is directly shaped by the defender's patching activity, allowing a given policy to be stress-tested against a realistic attack campaign. Experiments based on real-world vulnerabilities and two APTs show that vulnerability management must be tailored to organizational context, adversarial behavior, network topology, and asset criticality.

---


### 406. [LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding](https://arxiv.org/abs/2607.24555)

**<font color=#1a73e8>作者：</font>** Junsung Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving large language models at long context is bottlenecked by the key-value (KV) cache, which is read in full at every decode step. Attention keys are locally low-rank though globally high-rank: shared low-rank bases discard page-specific directions that a page's own compact basis retains. LOCKS gives every page its own spectral summary (resident, about a tenth the cache's size), reconstructs within-page logits, estimates each page's attention mass by log-sum-exp, and attends only the top pages; selection itself reads no candidate keys or values. Selecting on this summary alone stays within about a point of the full cache on long-document QA (LongBench-v1), tracks the read-every-key oracle on retrieval-dense RULER down to the smallest budgets, and shows its largest margins on long-form reasoning (AIME26, MATH-500), where baseline selectors collapse. At its shipped $2048$-token budget LOCKS matches FullKV aggregate quality at $100$K$+$ context while attending about $2\%$ of the tokens, and halves per-token decode latency ($2.0\times$ at $1$M tokens) against dense attention. LOCKS ships as a drop-in plugin for unmodified vLLM, with batched decode running in full CUDA graphs.

---


### 407. [BettiSplit: Topology-Guided Privacy-Aware Split Learning Against Feature Inversion and Gradient Leakage](https://arxiv.org/abs/2607.24556)

**<font color=#1a73e8>作者：</font>** Akarsh K.Nair, Muhammad Arifur Rahman, David Brown 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split learning enables collaborative model training by partitioning neural networks across clients and servers. However, improper split placement can lead to severe privacy leakage through intermediate representations. In this work, we propose a topology-guided framework for privacy-aware split learning based on the persistent Betti complexity of smashed activations. Through comprehensive layer-wise analysis, we show that privacy risk in split learning is highly non-uniform across layers and exhibits sharp transition regions that are not captured by architectural depth alone. In particular, feature inversion fidelity increases from negligible reconstruction to as high as 0.98 SSIM at deeper, privacy-critical split points. We further demonstrate that Betti complexity consistently identifies representation regimes associated with elevated feature-space privacy leakage across architectures and datasets. Leveraging this observation, we introduce BettiSafe, a topology-guided split selection strategy that identifies privacy-sensitive layers without requiring explicit attack execution. BettiSafe improves resistance to feature inversion by 2 to 5 times compared to depth-based heuristics while preserving classification accuracy. In addition, Betti-based regularisation increases inversion difficulty by nearly 5 x without degrading model utility, enabling a favourable privacy utility tradeoff. Overall, our results highlight topological complexity as a promising structural descriptor for secure, adaptive, and representation-aware split learning in real-world collaborative systems

---


### 408. [Proceedings of The First Reflection in Creative Experience (RiCE) Workshop](https://arxiv.org/abs/2607.24558)

**<font color=#1a73e8>作者：</font>** Corey Ford, Olga Sutskova, Samuel Rhys Cox 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reflection and metacognition are central to the creative user experience. However, most HCI research on reflection focuses on clear, task-oriented goals such as to reflect on personal data or pedagogical outcomes. This contrasts with the open-ended and challenging to articulate goals of creative user experiences. For the first time, this workshop brings together interdisciplinary researchers, designers, educators, and artists across HCI, Cognitive Science, Design, AI, Learning Sciences, and Digital Art to examine reflection in creative interaction. The workshop will discuss themes, drawn from earlier discussions with HCI researchers and artists, on: how best to capture reflection in creative contexts, how to leverage the arts to support reflection for ethical change, and how to design creative AI that enhances - not hinders - critical thinking. By bringing interdisciplinary perspectives on reflection into discussion, the workshop will develop a guiding taxonomy for reflection in creative interaction to inform future creative practice and tool development.

---


### 409. [EgoPlay: Event-Triggered Video Editing for Egocentric Streams](https://arxiv.org/abs/2607.24560)

**<font color=#1a73e8>作者：</font>** Jinjie Mai, Gordon Guocheng Qian, Willi Menapace 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EgoPlay, an event-triggered video-to-video editor for egocentric streams, obtained by fine-tuning a pretrained V2V diffusion transformer on event-conditioned data built primarily from Ego4D. Given a monocular video and an event-triggered prompt of the form "when X happens, do Y," EgoPlay infers whether and when event X occurs, preserves pre-event frames, and applies edit Y only to the post-event continuation. Rather than cascading a separate event detector with an editor, EgoPlay learns event recognition, temporal restraint, and pixel-level editing jointly in a single end-to-end model, while also handling negative and multi-event prompts. To support this, we construct a large-scale dataset of 106K event-triggered clip-prompt pairs spanning positive triggers, fabricated-trigger negatives, and multi-event prompts. We then train a bidirectional video diffusion editor with event-triggered supervision and derive a causal variant for chunk-by-chunk streamable inference. We further introduce an event-aware evaluation protocol that separately measures post-trigger editing quality, pre-trigger preservation, and false-trigger robustness. On the Ego4D benchmark, EgoPlay substantially outperforms EgoEdit, the state-of-the-art instruction-based egocentric video editing baseline, with relative gains of 17.7%, 16.9%, and 16.4% in editing quality, visual quality, and background consistency. It also surpasses a VLM-guided detector-editor baseline by 15.7%, 14.5%, and 13.5% on the same metrics, while using less than half the GPU memory.

---


### 410. [TRACE-CTI: Auditable Post-Extraction Governance of TTP Claims with Knowledge Graphs](https://arxiv.org/abs/2607.24563)

**<font color=#1a73e8>作者：</font>** Federico Valletta, Giacomo Longo, Enrico Russo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Security Operations Centers increasingly rely on automated mapping of Cyber Threat Intelligence reports to MITRE ATT&CK, yet extractor outputs remain fallible and are often stored without the evidence, provenance, and validation history needed to decide whether an individual mapping should be trusted. We present TRACE- CTI, a post-extraction claim-governance framework that preserves run-level Predictions, aggregates them into configuration-level GraphAssertions, materializes setup-deduplicated corroboration as ConsensusAssertions, and exposes only GraphAssertions backed by policy-compliant validation grounds. The framework retains native evidence granularity, complete extraction provenance, versioned trust decisions, and non-destructive revocation history. We evaluate TRACE-CTI on two public CTI corpora comprising 65 reports and 5,303 sentences, using a controlled 2 x 3 matrix of retrievers and generator families, incrementally ingested across six GraphVersions. All setups are incorporated without schema modification; provenance paths remain complete, operational scopes remain disjoint, and every trusted GraphAssertion has an active qualifying validation ground. Cross-generator-family setup pairs exhibit greater output diversity than same-family pairs. At the final graph state, increasing setup support from k >= 1 to six-setup unanimity raises gold-aligned precision from 25.3% to 90.6%, while recall decreases from 88.2% to 16.3%. The graph also directly answers seven questions about provenance, trust, versioning, dependency, disagreement, and review-queue that the evaluated minimal flat output cannot fully answer without enrichment or reprocessing. These results support explicit, auditable governance of extracted TTP claims; the observed corroboration trajectory is descriptive and does not establish statistical independence or a causal model-family effect.

---


### 411. [DSCH-Loss: A Dynamic Semantic Channel Objective for Deep Semantic Hashing](https://arxiv.org/abs/2607.24567)

**<font color=#1a73e8>作者：</font>** Tobias J. Bauer, Christian Riess, Daniel Loebenberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic hashing methods for generating short binary hash codes that allow efficient approximate nearest neighbor search in high-dimensional data spaces have gained extensive consideration in recent years. Deep learning-based methods offer better semantic capturing capabilities than traditional approaches relying on manual feature engineering. Moreover, they enable a data-driven approach to semantic hashing across diverse data modalities, yielding high-quality cross-modal hash codes within a shared Hamming space. Previous work investigated the properties of this Hamming space and introduced a loss function based on predefined so-called semantic channels with fixed width and Hamming distances derived from label similarities. However, this formulation also introduced discontinuities into the loss landscape, complicating optimization. Based on these observations, we propose a newly designed loss function, Dynamic Semantic Channel Hashing (DSCH), using dynamically sized and positioned semantic channels in order to avoid loss landscape discontinuities. Furthermore, we endorse the use of tie-aware Mean Average Precision (mAP) as evaluation metric as it addresses the ambiguity in sample retrieval ordering, which emerges from the discreteness of hash code distances. Finally, multiple experimental settings conducted on two popular datasets and incorporating two different model architectures provide strong evidence that training using the DSCH objective outperforms training using other state-of-the-art loss functions. In a total of 35 out of 40 cross-modal and intra-modal retrieval tasks, models trained with DSCH achieve significantly higher tie-aware mAP scores across all four tested hash code lengths, showing compelling results across model architecture and used dataset. The mAP score uplifts are consistent and amount up to 1.75 percentage points compared to the respective second best.

---


### 412. [Bit-Accurate FPGA Evaluation of Learned Feature Gating in a Fixed-Point Fourier-Feature Automatic Modulation Classifier](https://arxiv.org/abs/2607.24568)

**<font color=#1a73e8>作者：</font>** Gawthaman Senthilvelan, Luthira Abeykoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned feature reweighting can improve automatic modulation classification (AMC) in software, but the same operation introduces additional arithmetic and latency when implemented on an FPGA. This work measures that trade-off in a compact fixed-point classifier using 24 sparse DFT-energy features, 8 phase/statistical features, and a 32-to-128-to-11 multilayer perceptron. A second architecture inserts a learned 32-element, 8-bit, input-dependent gate before the classifier. Gated and ungated models are trained using post-training quantization (PTQ) and quantization-aware training (QAT) with two matched training seeds. The resulting eight checkpoints are compiled independently for an Intel Cyclone V FPGA and evaluated over 352,000 physical-board classifications. Ungated models achieve higher test accuracy in all four matched gate comparisons, with mean gated-minus-ungated differences of -0.784 percentage points under PTQ and -0.616 percentage points under QAT. The effect of QAT changes direction between the two training seeds. In hardware, the gate adds an average of 1,318 adaptive logic modules (ALMs), 1,557 registers, 4 DSP blocks, and 3,140 processing cycles. All 352,000 board predictions agree exactly with an independent integer reference, and 3,760 captured intermediate values from one training seed also match. For this feature representation and implementation, learned gating increases FPGA cost without improving classification accuracy.

---


### 413. [Designing Within the Lines: Practitioners' Perspectives and Visualisation Tool Evaluation in the Arabic Context](https://arxiv.org/abs/2607.24571)

**<font color=#1a73e8>作者：</font>** Muna Alebri, Noëlle Rakotondravony, Yassine Bechqito 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Design guidelines and best practices serve as references that support designers throughout the visualisation design process. While considerable effort has identified the elements that contribute to effective data visualisations, little attention has been paid to how language (scripts and reading direction), tool support, and cultural context also shape design decisions. As a result, assumptions of homogeneity persist, with visualisation practices predominantly benefiting users of English and left-to-right (LTR) scripts while overlooking the needs of over two billion Arabic script users. We investigate how Arabic-speaking visualisation practitioners design for right-to-left (RTL) scripts. We report on an analytical evaluation of seven popular GUI-based visualisation authoring tools using an Arabic dataset complemented by interviews with 11 Arabic-speaking practitioners across journalism, design, and data analysis. Our findings reveal that visualisation practitioners constantly negotiate tensions between Arabic reading conventions, "universal" LTR visual norms, and limited tool support for Arabic text, Eastern numerals, and maps. They engage in substantial labour, such as manually mirroring charts, fixing alignment issues, and stitching together multi-tool workflows, while making strategic compromises in language choice, interactivity, and chart type. Our tool analysis further reveals fragmented, inconsistent support for RTL mirroring, poor numeral rendering, and map defaults that encode geopolitical assumptions. In light of these findings, we discuss how RTL visualisation work is carried out under many constraints that affect agency and creativity. We argue that visualisation tools and defaults operationalise linguistic and geopolitical power in RTL contexts, and offer research directions and design implications that more robustly support RTL practitioners.

---


### 414. [Evaluating Fuzz Testing for Reinforcement Learning Agents](https://arxiv.org/abs/2607.24577)

**<font color=#1a73e8>作者：</font>** Zhibin Kang, Hanmo You, Dong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) agents are increasingly deployed in safety-critical domains such as robotics, autonomous driving, and drone control, where unexpected behaviors may lead to severe real-world consequences. Fuzz testing has recently emerged as a promising method for exploring the vast state spaces of RL agents and exposing crashes. Although numerous RL fuzzing methods have been proposed, existing studies often differ in evaluation settings, baselines, and metrics, making it difficult to draw reliable conclusions about their relative effectiveness and practical usefulness. To address this gap, we present the first comprehensive empirical study that systematically evaluates RL fuzzing methods from four complementary perspectives: effectiveness, diversity, efficiency, and practical utility. We benchmark five state-of-the-art methods alongside random testing under unified configurations across three environments of increasing complexity (MountainCar, BipedalWalker, and CARLA), and further assess the downstream usefulness of detected crashes for agent robustness improvement and safety monitoring. Our results reveal several key insights. For instance,throughput-oriented methods like MDPFuzz demonstrate superior effectiveness and efficiency in crash discovery, while methods explicitly designed to encourage exploration like SeqDivFuzz excel at uncovering diverse crash behaviors. We also show that fuzzing-generated crashes can meaningfully improve agent robustness and enable accurate safety monitoring with strong cross-method generalization. Beyond these empirical findings, we distill actionable guidance for both researchers and practitioners, highlighting the benefits of combining complementary fuzzing strategies and adopting multi-level diversity analysis to achieve more comprehensive and practical RL testing.

---


### 415. [CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding](https://arxiv.org/abs/2607.24582)

**<font color=#1a73e8>作者：</font>** Jinlong Yang, Wenhao Zhang, Kuanwei Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty. This uniform strategy invokes unnecessary tool-assisted processing for easy questions and provides limited control when difficult questions require fine-grained temporal evidence. We propose CADER (Confidence-Aware Dynamic Evidence Reasoning), a training-free framework for adaptive and reliable long-video reasoning. CADER first performs global reasoning over uniformly sampled frames and estimates answer confidence with a logit-margin signal, allowing high-confidence examples to exit early. For uncertain examples, CADER activates a second-stage tool-augmented loop that combines temporal cropping, lightweight semantic verification, and Relevance-Guided Resampling to progressively localize question-relevant evidence. This design treats tool use as a sample-level decision: a single global pass handles easy cases, while additional reasoning is reserved for examples where uncertainty suggests that more evidence is needed. Experiments on multiple VideoQA benchmarks show that CADER improves long-video reasoning while bypassing Stage~2 for high-confidence samples. Moreover, when applied to a backbone trained only with tool-free chain-of-thought supervision, CADER achieves competitive performance against specialized tool-augmented frameworks, suggesting a practical inference-time route for adaptive long-video reasoning.

---


### 416. [PYPM-GGD: Pitman-Yor Process Mixture with Generalized Gaussian Density using ADAM](https://arxiv.org/abs/2607.24583)

**<font color=#1a73e8>作者：</font>** Kart-Leong Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large scale Bayesian nonparametrics (BNP) learner such as Stochastic Variational Inference (SVI) can handle datasets with large class number and large training size at fractional cost. Like its predecessor, SVI rely on the assumption of conjugate variational posterior to approximate the true posterior. A more challenging problem is to consider large scale learning on non-conjugate posterior. Recent works in this direction are mostly associated with using Monte Carlo methods for approximating the learner. However, these works are usually demonstrated on non-BNP related task and less complex models such as logistic regression, due to higher computational complexity. In order to overcome the issue faced by SVI, we develop a novel approach based on the recently proposed constant stepsize stochastic gradient ascent to allow large scale learning on non-conjugate posterior. Unlike SVI, our new learner does not require closed- form expression for the variational posterior expectatations. Our only requirement is that the variational posterior is differentiable. In order to ensure convergence in stochastic settings, SVI rely on decaying step-sizes to slow its learning. Inspired by SVI and Adam, we propose the novel use of adaptive stepsizes in our method to significantly improve its learning. We show that our proposed methods is compatible with ResNet features when applied to large class number datasets such as MIT67 and SUN397. Finally, we compare our proposed learner with several recent works such as deep clustering algorithms and showed we were able to produce on-par or outperform the state-of-the-art methods in terms of clustering measures.

---


### 417. [Artificial Intelligence and Innovation Ecosystem: Evolutionary Developments, Challenges, and Future Directions](https://arxiv.org/abs/2607.24589)

**<font color=#1a73e8>作者：</font>** Zhimin Zhang, Chengzhen Ma, Jia Chai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of the Innovative Ecosystem (IE) presents a new paradigm for economic integration, collaborative advancement, and shared achievements. The rise of Artificial Intelligence (AI) has significantly accelerated the global processes of digitization, informatization, and intelligence. Exploring how AI can leverage inherent characteristics to influence the development trajectory of IE is a topic that warrants further investigation. Given AI's increasing prominence and role within IE, the paper analyzes this new form, examining both AI's unique contributions to IE and its potential challenges. Firstly, the paper synthesizes the conceptual frameworks surrounding IE, decomposing them into manifestations in physical, social, and thinking spaces. Furthermore, the concept of Artificial Intelligence IE (AIIE) is introduced from a spatial perspective, with an exploration of the characteristics AI contributes to IE. Subsequently, the paper employs an evolutionary perspective to analyze the roles provided by AI during different development periods of AIIE. The paper then verifies the feasibility, effectiveness, and rationality of the AIIE's definition and analyzes AIIE development from an evolutionary perspective using enterprise development examples. Finally, acknowledging AI's inherent limitations, the paper examines potential challenges facing AIIE in the future from four perspectives, aiming to identify new research avenues for the further development of AIIE.

---


### 418. [CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Yanhong Zeng, Ka Leong Cheng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CameraAnything, the first unified framework for camera controlled video editing that enables joint control of both intrinsic and extrinsic camera parameters. Existing approaches either rely on expensive 3D reconstruction to achieve full camera functionality or restrict editing to extrinsic parameter manipulation. Moreover, the coupled influence of intrinsic and extrinsic parameters on video appearance makes disentangled modeling particularly challenging. To address this, we adopt per-pixel Plücker ray injection alongside resolution-aware 3D RoPE in self-attention, building both camera conditioning and spatial positional encoding on the target latent to jointly control camera position, focal length, and native resolution editing without cropping or outpainting. To overcome the scarcity of paired training data, we further develop a scalable synthetic pipeline that constructs diverse dynamic scenes through structured multi-camera recording and generates synchronized videos with varied camera configurations. With a tailored orthogonal training strategy, CameraAnything enables expressive video reshooting with arbitrary viewpoint control, focal length adjustment, resolution adaptation, and multi-shot transitions within a single generation process, offering strong practical value for cinematic video editing and cross-platform content adaptation in video production.

---


### 419. [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](https://arxiv.org/abs/2607.24593)

**<font color=#1a73e8>作者：</font>** Hong Liu, Yuan Cheng, Lin Niu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it. To select the top-k tokens for each query, the indexer must still score every preceding token, incurring a cost of O(L^2) per layer for a sequence of length L. We observe that this per-query scan is largely redundant: nearby queries select highly overlapping top-k tokens, and the indexer scores are long-tailed along the key axis. We exploit these properties in PIVOT, Proxy Indexing Via One full-prefix Traversal, a training-free, drop-in replacement for the DSA indexer that shares one prefix scan across a group of nearby queries. PIVOT aggregates a group into a single proxy query, performs one shared full-prefix scan to obtain a candidate set, and then selects a top-k for each query from that set. Two variants trade speed for fidelity: PIVOT-Reuse shares the proxy top-k across the group for maximum speed, whereas PIVOT-Refine re-scores the candidate set with the indexer of each query and then selects an individual top-k, matching the dense indexer at a small additional cost. A single algorithm covers both inference phases, differing only in how groups are formed: fixed-size groups of consecutive queries in prefill, and the queries decoded together in one multi-token prediction (MTP) step in decode. On DeepSeek-V3.2 and GLM-5.1 across LongBench and RULER, PIVOT matches the accuracy of the dense DSA indexer while accelerating it by up to 4x and reducing end-to-end latency by up to 1.6x at long context.

---


### 420. [QueenVIS: Rethinking Image-Only Training for Video Instance Segmentation via Query Enrichment](https://arxiv.org/abs/2607.24598)

**<font color=#1a73e8>作者：</font>** Arian Kheirandish, Fardin Ayar, Ehsan Javanmardi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video instance segmentation (VIS) requires models to detect, segment, and track object identities across frames, and most methods enforce temporal consistency through video-level supervision. Image-only training approaches, with MinVIS as one prominent example, have challenged this assumption, reaching competitive VIS without video training by treating frames as independent images and associating instances only at inference. The field has nonetheless moved toward ever more elaborate video-trained trackers, which depend on costly identity-consistent annotations, leaving the image-only direction under-explored. A diagnostic analysis identifies object query quality as the bottleneck: queries trained only to localize objects within a frame drift apart across frames and destabilize association. QueenVIS introduces a query-centric framework for strengthening image-trained VIS. During single-frame training, we enrich Mask2Former queries with two auxiliary heads: a feature-prediction loss that aligns each query with the pooled backbone descriptor of its instance, and a center-prediction loss that injects spatial structure. Both heads are discarded at inference, adding zero parameters, and temporal identity is maintained by a training-free query-propagation and memory-bank scheme. On YouTube-VIS and OVIS with a ResNet-50 backbone, QueenVIS improves over MinVIS, up to +6.7 AP on YouTube-VIS, +4.8 AP on OVIS, and +10.3 AP on the long-sequence YouTube-VIS split. QueenVIS achieves 50.9 AP on YouTube-VIS and remains competitive with recent video-supervised state-of-the-art, without processing a single video clip during training. Our findings suggest that strengthening the discriminative power and temporal stability of object queries is an important, underexplored axis for VIS. Code and models: this https URL

---


### 421. [Characterizing In-the-Wild Personal Listening Device Use to Inform Earable Application Design](https://arxiv.org/abs/2607.24603)

**<font color=#1a73e8>作者：</font>** Supraja Ramesh, Jonas Hummel, Silvia Becker 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ear-worn devices are evolving from audio-playback tools into sensing platforms for health, interaction, and context-awareness. Yet, earable systems are typically designed and evaluated under strong assumptions about how long, how often, and in which situations people actually wear personal listening devices (PLDs). To ground these assumptions in-the-wild behavior, we combine a survey of 330 adults with multi-year, passively logged headphone audio-exposure records donated via Apple Health by 90 of them. We characterize where and when people use PLDs, how logged use has changed in recent years, and how psychological traits and social context associate with PLD usage. Our results show that logged mean daily use has increased from 37 minutes in 2020 to 64 minutes in 2024. Listening was intermittent: no listening was logged on 48% of participant-days in 2024, and sessions were fewer but longer on weekends. Sensation seeking, particularly disinhibition, showed small to medium positive associations with self-reported PLD use. Younger adults listened at higher volumes than the 25-34 group. High-volume exposure was uncommon, with only 4% of participant-weeks exceeding World Health Organization (WHO) safe-listening limits. Finally, most participants also reported avoiding PLD use in social situations. We translate these findings into implications for earable computing: realistic expectations of intermittent rather than continuous wear, contextual coverage that anticipates systematic gaps, targeted safe-listening interventions, and personalization grounded in psychosocial and demographic profiles rather than assumptions of uniform use.

---


### 422. [Attribution and Uncertainty Behavior of Learned Residual Gyro Correction for Gyro-Stellar Estimation](https://arxiv.org/abs/2607.24608)

**<font color=#1a73e8>作者：</font>** Mariela De Lucas Álvarez, Melvin Laux, Arthur de Freitas Precht 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates uncertainty decomposition and explainability in a deep learning-based framework for gyroscope bias correction. A 1-D Convolutional Neural Network is trained to predict residual angular rate corrections from multi-sensor inputs, including gyroscope and star tracker measurements. The bias corrections are sent to a flight-representative Gyro-Stellar Estimator. The network produces both mean corrections and input-dependent (heteroscedastic) aleatoric uncertainty, while epistemic uncertainty is estimated via an ensemble of independently trained models.
The proposed approach is trained under nominal conditions and evaluated in both nominal and structured perturbations that include additive and temporally correlated noise. Gradient-based attribution methods are applied to both the correction and uncertainty outputs, enabling a decomposition of the evidence that drives state updates and uncertainty estimates. By aggregating attribution patterns across rotational axes and regimes, we reveal axis-specific behaviors and characterize how structured perturbations influence the collaboration between aleatoric and epistemic uncertainty.
Uncertainty analysis shows that aleatoric uncertainty increases with perturbation intensity, but the distributions overlap and the calibration is not consistent across regimes. On the other hand, epistemic uncertainty gives a clear signal that gets clearer as the distributional shift happens, showing that the models disagree more. These results show that aleatoric and epistemic uncertainty work well together and that epistemic uncertainty is better at distinguishing between nominal and perturbed operating conditions. The results provide insight into the behavior of hybrid learning-based state estimation components and motivate the use of uncertainty for downstream monitoring and fault detection.

---


### 423. [Leveling the Playing Field: Temporal Video Segmentation for Individuals with ADHD in Computing Education](https://arxiv.org/abs/2607.24612)

**<font color=#1a73e8>作者：</font>** Veronica Pimenova, Chris Lee, Baramee Bhakdibhumi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Individuals with Attention-Deficit/Hyperactivity Disorder (ADHD) often face significant barriers in computing education. In asynchronous learning environments, instructional videos can impose high extraneous cognitive load, often relying on assumptions about sustained attention and working memory that do not align with ADHD neurocognitive profiles. In this work, we evaluate a post-hoc video processing intervention that segments instructional content into single-instruction chunks followed by fixed-length pauses to reduce cognitive load. In a within-participants controlled study with 17 individuals with ADHD and 10 without, we find that the intervention has an equalizing effect. Although it improved performance for all participants, gains were larger for those with ADHD, reducing their errors and hesitations to levels comparable to those of participants without ADHD under the same intervention. These results align with the goals of Universal Design for Learning (UDL), by showing that cognitively-aligned, post-hoc instructional video modifications can reduce performance disparities across diverse neurocognitive profiles.

---


### 424. [Modeling Local Exploit Hazard - A Bayesian Framework for Quantifying Exploit Risk and Operational Efficiency](https://arxiv.org/abs/2607.24618)

**<font color=#1a73e8>作者：</font>** Stephen Shaffer, Laura Voicu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a local exploit hazard model : a Bayesian framework that converts the global probabilities produced by an exploit likelihood model (ELM), such as the Exploit Prediction Scoring System (EPSS), into a daily exploit hazard rate for an organization's own assets. The model measures the exploit-prevention effectiveness of deployed controls as a probability distribution. That distribution is seeded from a subject-matter-expert opinion pool and updated through Beta-Binomial inference from telemetry, breach-and-attack simulation, or penetration testing, then applied to ELM scores by attack-vector alignment. The resulting per-vulnerability exploitation likelihoods are converted into hazard rates using standard survival-analysis techniques, supporting both a constant exponential hazard and a Weibull hazard whose shape parameter, calibrated from Known Exploited Vulnerabilities catalog timing, captures the empirical decay of exploitation risk as a vulnerability ages. Because hazards are additive under independence, per-vulnerability rates aggregate by summation up to host, network, business unit, and organization. Candidate remediation actions are simulated and ranked by projected hazard reduction, giving defenders a defensible, quantitative basis for prioritization under fixed capacity. Future work includes extensions for incident likelihood and financial loss modeling.

---


### 425. [Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects](https://arxiv.org/abs/2607.24645)

**<font color=#1a73e8>作者：</font>** Phu Gia Hoang, Anwoy Chatterjee, Tanmoy Chakraborty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior. Features with clear activation descriptions may have weak or unexpected causal effects; steering can vary across prompts or oppose the intended direction; and activation-based feature selection can miss features that produce the desired output change. Prior work has studied feature geometry inside the model, where features are computed. We instead study the geometry of changes in model logits caused by feature interventions. We introduce Feature-Effect Geometry Analysis (FEGA), an unsupervised framework that removes the same active SAE feature across contexts and analyzes the resulting cloud of logit changes. Across SAE variants, consistent one-dimensional effects are rare: few features behave like reusable directions. To interpret this variation, we distinguish value-like features, tied to static information such as factual attributes, from pointer-like features, associated with context-dependent operations. Value-like features more often exhibit structured, low-dimensional effects, although these effects typically span several directions. Pointer-like features, by contrast, predominantly exhibit diffuse effects. Our results show that a feature can be interpretable and causally relevant without providing a stable direction for steering.

---


### 426. [Efficiency Matters in Autonomous Research](https://arxiv.org/abs/2607.24647)

**<font color=#1a73e8>作者：</font>** Haiqian Yang, Yuan Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outcome. In this paper, we argue that the efficiency of the solution-search process is an equally important but often overlooked dimension of performance. A strong AR system should not only produce high-quality results, but also reach them with as small a budget as possible. Search efficiency will become increasingly important as AR expands from domains with inexpensive verification, such as mathematics and coding, to real-world scientific settings in which solution evaluation may require costly physical experiments. To capture this dimension, we propose evaluating AR systems using the area under the curve (AUC) of the Pareto frontier, alongside final outcome quality. We compare several families of search algorithms, including hill climbing, beam search, tree search, and evolutionary search, across twelve systems-optimization tasks. We find that no single search structure is consistently the most efficient. We also show that search efficiency and final outcome quality are distinct performance dimensions: a method that eventually achieves the best result may nevertheless improve slowly and consume substantially more evaluation budget before reaching that result. Because the most effective search policy is generally unknown in advance, we introduce an adaptive procedure called fluid search, which uses a portfolio bandit to dynamically allocate a fixed evaluation budget across a forest of search processes. Across the evaluated tasks, fluid search achieves the highest overall search efficiency, closely matching the performance of a per-task oracle that is given the best search structure for each task in advance.

---


### 427. [Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels](https://arxiv.org/abs/2607.24651)

**<font color=#1a73e8>作者：</font>** Zhuchenyang Liu, Yao Zhang, Yu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the document. Under this interface, vision-language models often fail to identify the right regions even when the answer is correct, a failure known as Attribution Hallucination. We present a study that investigates whether this failure is partially limited by what the model can express through coordinates. On a verified bilingual CiteVQA subset, we compare the coordinate interface with a language interface in which the model outputs only text, quoting its evidence verbatim, and a multimodal retriever returns the location of each quote as a page region proposed by a layout parser (tables and figures are quoted through their captions or notes); the comparison is repeated over six open vision-language models. Compared with the coordinate interface, evidence recall rises from at most 8 points to between 26 and 47 and the hallucination rate roughly halves, with little change in answer quality. Building on this comparison, we use the same quote-and-retrieve pipeline as a training scaffold: because region-level evidence labels are expensive to collect for long documents, we introduce a GRPO recipe whose reward is a judge's reading of the gold answer and crops of the retrieved regions, training the model to quote better evidence without any region labels and raising an 8B backbone's strict attributed accuracy from 22.4 to 33.8. These findings indicate a practical path to improve attribution"without a coordinate interface and without costly region-level supervision.

---


### 428. [When Can You Correct Distribution Drift in Temporal Graph Generation? A Sharpening--Drift Tension and an Impossibility for Observation-Based Correction](https://arxiv.org/abs/2607.24662)

**<font color=#1a73e8>作者：</font>** Tianpeng Li, Xuan Guo, Wenjun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models of temporal graphs are trained on one stretch of an evolving network and deployed on the next, and they degrade badly in the gap. We show this degradation is derivable, general, and not fixable from observations. The masked flow-matching loss decomposes exactly, with no independence assumption, into an irreducible entropy plus a divergence whose derivative along the training path is positive precisely for structures rare during training and common at deployment, diverging as their training probability goes to zero. Empirically the trade-off is a power law with exponent $-0.605$ ($R^2=0.9977$), and drift raises the sampler's error floor without changing how many steps reach it: across seven well-powered conditions the drift-period marginal error varies by at most $6\%$ over a $50\times$ range of sampling budgets, while the floor sits $2.2\times$ to $34.3\times$ above the in-period floor. Because the deployment period is observed, correction looks like a matter of measurement. It is not. We prove that any corrector measurable with respect to past observations leaves at least the conditional variance of the statistic it tracks, and that trend extrapolation beats trusting the last observation only when $\mu^2>v(1-2\rho)$. Both premises are measurable and both go the wrong way: the drift is trendless and mean-reverting, with a one-step innovation as large as the drift itself. An oracle removes $60\%$ of the error, the best observation-based corrector recovers $5.7\%$ of that, and extrapolation is strictly worse than doing nothing clever.

---


### 429. [Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating](https://arxiv.org/abs/2607.24667)

**<font color=#1a73e8>作者：</font>** Maruthi Vemula, Neeraj Praneeth Gajula  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A language model with a bounded working memory must repeatedly decide which stored items to keep. Every deployed method decides the moment an item arrives, from the past (StreamingLLM, H2O) or from a guess about the future (SnapKV). We recast the choice as an estimation problem on a hidden signal, whether an item will be reused, placing existing methods on one axis, the commit lag $H$: online filters and learned predictors commit at $H=0$, while Belady's offline optimum sits where the whole future is known. The missing regime in between, fixed-lag smoothing, waits a bounded number of steps, observes which items a correct near-future prediction attended to, and only then commits. This measurement, demonstrated utility, turns Belady's unobservable future request into something we read off the model itself. We instantiate it as a training-free policy, RMM, a strict generalization of H2O that reduces to it exactly when the measurement is uniform. In controlled settings where reuse is endogenous and separated in time, demonstrated utility identifies used memory far better than accumulated attention, and a small bounded memory behaves like a much larger one. But on independent third-party benchmarks, run inside NVIDIA's KVPress harness against its own SnapKV, H2O, and StreamingLLM implementations, the advantage mostly disappears: RMM is on par with H2O for single-turn question answering and loses to both H2O and SnapKV in a streaming multi-turn setting. The cause is simple: on natural text the model is correct about most tokens, so weighting attention by correctness barely changes it, and demonstrated utility collapses onto accumulated attention unless reuse is sharp and endogenous, which standard benchmarks do not exercise. Our contribution is the framework and an honest map of when measuring beats accumulating, not a new state of the art.

---


### 430. [Explainable Reinforcement Learning via Physics-Aware Policy Distillation](https://arxiv.org/abs/2607.24672)

**<font color=#1a73e8>作者：</font>** Shaker Al-Tamari, Waled Kadour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum benchmark. A high-performance Twin Delayed DDPG (TD3) agent serves as an opaque, continuous teacher model, whose policy is distilled into an interpretable student surrogate based on a shallow Decision Tree. By leveraging a custom physics-aware feature and "Noisy Oracle Rollouts" for dataset generation, the distillation process achieves performance equivalent to the expert teacher. Furthermore, comparative control theory analysis reveals a fundamental trade-off: transitioning from continuous to discrete rule-based control induces high-frequency Bang-Bang actuation and a stable bimodal limit cycle. Simulation results indicate that Bounded-Input Bounded-Output (BIBO) stability is maintained while providing both global and local interpretability for safe autonomous systems.

---


### 431. [Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary Time Series](https://arxiv.org/abs/2607.24673)

**<font color=#1a73e8>作者：</font>** Mohammad Fesanghary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We describe Causal-TS, an open-source Python library for causal discovery in high-dimensional and nonstationary multivariate time series. Causal-TS provides four specialized algorithms-CDNOTS, CDNOTS+, CEDAR, and GRACE-along with wrappers for GES, Granger, LASSO-VAR, and LGES, all sharing a unified conditional independence (CI) test layer with GPU acceleration via PyTorch. A regime discovery pipeline detects structural breaks via pluggable changepoint detectors and runs discovery per regime with regime-specific parameters. A command-line interface, synthetic data generators, and optional DoWhy integration provide an end-to-end pipeline from raw time series to causal effect estimates. The library is pip-installable, tested on Python 3.10--3.12, and available at this https URL.

---


### 432. [Co-Learning for Missing Arbitrary Modalities in Multi-modal Classification](https://arxiv.org/abs/2607.24683)

**<font color=#1a73e8>作者：</font>** Francisco Mena, Dino Ienco, Roberto Interdonato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal classification leverages complementary information across diverse data sources to enhance predictive performance. However, real-world scenarios subject to operational constraints, such as sensor failures or privacy restrictions, lead to inconsistent modality availability between training and inference times. To handle missing modalities, prior studies have mainly covered bimodal data setups and focused on designing robust fusion processes. Instead, we adopt a multi-modal co-learning framework that prioritizes inter-modal collaboration rather than multi-modal fusion. Specifically, we consider that any subset of modalities may be absent, without assuming predefined missing-modality patterns, an inference scenario we refer to as missing arbitrary modalities. To address this challenge, we introduce two alternative approaches that leverage information at both feature- and decision-level. Experiments on two multi-modal classification benchmarks demonstrate significant robustness gains in various missing modality conditions. The first method shows more robust behavior under minimal missing conditions, where a single modality is absent, whereas the second performs better under extreme missing conditions, where all-but-one modalities are missing. Our code is available at this https URL.

---


### 433. [Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking](https://arxiv.org/abs/2607.24701)

**<font color=#1a73e8>作者：</font>** Andong Lu, Ziyi Zha, Jiandong Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing modalities from available ones, but the quality of data generated in challenging scenarios might be unsatisfactory. In addition, current approaches exhibit limited flexibility in processing both missing and complete data. To overcome these limitations, we propose a Spatio-temporal Conditional Denoising Transformer (SCDT), which integrates the spatial cues and the temporal context to adaptively perform information reconstruction of missing modalities and feature enhancement of weak modalities in a unified framework, for robust modality-missing RGBT tracking. In particular, SCDT leverages the short-term temporal cues from recent historical frames to capture the fine-grained temporal correlations and the long-term temporal cues encoding modality evolution to capture the global context. By jointly exploiting long short-term temporal contexts as the conditions, SCDT progressively guides noisy features of available modalities to learn reliable and temporally consistent multimodal representations. Furthermore, SCDT introduces a noisemodulated adaptation mechanism that dynamically adjusts its behavior according to the modal availability, enabling a single framework to unify feature learning under both modality-missing and complete scenarios without changing the architecture or parameters. Extensive experiments on three public benchmark datasets demonstrate that our method consistently outperforms state-of-the-art methods. The code is available here.

---


### 434. [Panda: Unsupervised Pelvic Anomaly Detection for Real-Time MR Imaging](https://arxiv.org/abs/2607.24703)

**<font color=#1a73e8>作者：</font>** Anika Knupfer, Maximilian Lindholz, Johanna Paula Müller 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Female pelvic diseases remain an under researched area characterized by often delayed diagnosis. While pelvic MRI offers superior soft-tissue contrast for diagnosis and image-guided procedures, real-time anomaly detection remains challenging due to physiological motion, tissue deformation, and instrument artifacts. Existing supervised approaches are impractical, as adverse events are rare, heterogeneous, and difficult to annotate. We present a Dinomaly-based unsupervised anomaly detection framework adapted for pelvic MRI that learns normative representations from healthy cases and flags deviations without requiring labels. Our approach leverages a frozen DINOv3 Vision Transformer encoder combined with a noisy MLP bottleneck and Linear Attention decoder to prevent identity mapping while maintaining computational efficiency. Anomalies are localized via per-token cosine distance between encoder and decoder representations, yielding spatial anomaly maps that provide immediate feedback at the scanner to support radiologist decision-making and adaptive protocol adjustment. Evaluated on a curated subset of the Uterine Myoma Dataset, the framework achieves a pixel-level AUROC of 88.06% and high specificity (95.45%) at frame level at 40.5 slices/s, meeting real-time clinical deployment requirements. The spatial anomaly maps and frame-level scores provide immediate, localized feedback at the scanner to support radiologist decision-making and adaptive protocol adjustment during active procedures.

---


### 435. [SADe: Sparse-Atom Support Decontamination for Few-Shot Segmentation with Weak Support Annotations](https://arxiv.org/abs/2607.24706)

**<font color=#1a73e8>作者：</font>** Hang Xing, Guangjun Liu, Yan Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot segmentation (FSS) commonly assumes clean pixel-level support masks, yet practical support supervision often uses boxes, scribbles, coarse masks, or pseudo-masks. These weak annotations may include texture-similar distractors and background context alongside the target, contaminating class prototypes or visual prompts before query prediction. We introduce SADe, a predictor-agnostic support decontamination layer that estimates the reliability of selected support patches without query information. Central to SADe is sparse autoencoder (SAE) atom evidence: dense similarity may respond to both target and texture-similar context, whereas contrasting atom activations inside and outside the weak-support region provides factor-level reliability cues. A lightweight router combines atom evidence with dense similarity and episode statistics to predict patch reliability and generate a cleaned support mask. Trained once on synthetic weak-support episodes from FSS-1000, the router is frozen for all target evaluations. The resulting mask supports standalone prediction or can be supplied to heterogeneous FSS models through native support interfaces without altering query-side inference. Under a matched weak-support protocol, SADe achieves the highest query mIoU in six of nine standalone prompt-shot combinations. With the same ProMi query head, it is within 0.03 mIoU of SAM3-derived masks under tight boxes and surpasses them by 11.17 and 19.49 points under box-r2 and box-r4, respectively. As a plug-in, SADe improves over raw support in 70 of 72 matched box-family comparisons across four frozen downstream models and two datasets. On point and scribble prompts, its average performance remains close to the corresponding raw-support baseline. Ablations and atom-removal controls show that atom evidence contributes reliability information beyond dense similarity.

---


### 436. [DreamStyle3D: Efficient 3D Stylized Asset Generation via Dual-Attention Disentanglement](https://arxiv.org/abs/2607.24721)

**<font color=#1a73e8>作者：</font>** Kai Wang, Ziheng Ouyang, Xuying Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growth of gaming, animation, and virtual reality industries, the demand for efficient generation of stylized 3D assets is rapidly increasing. However, existing approaches still struggle to jointly preserve style fidelity, geometric consistency, and generation efficiency, as most of them still rely on indirect 2D-to-3D stylization pipelines. This motivates a native 3D stylization framework that can explicitly disentangle style from geometry while remaining efficient. To this end, we propose DreamStyle3D, an efficient framework for stylized 3D asset generation built on a Decoupled Dual Cross-Attention mechanism. Our method explicitly separates geometric and stylistic features to enable efficient style injection while preserving structural consistency, and further adopts a lightweight training strategy to enhance style consistency and model generalization. In addition, we build an automated data pipeline and construct a dataset of about 15K content-style-stylized triplets for training and evaluation. Extensive experiments demonstrate that our DreamStyle3D can generate high-fidelity, geometrically consistent stylized 3D assets within 10 seconds, substantially improving efficiency while maintaining superior style quality and offering a new solution for 3D content creation. The code and data are available at this https URL.

---


### 437. [Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs](https://arxiv.org/abs/2607.24726)

**<font color=#1a73e8>作者：</font>** Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) have become widely-used methods for solving partial differential equations (PDEs) in the rapidly growing field of scientific machine learning. In these methods, a neural network is trained to approximate the PDE solution by using (stochastic) gradient descent to minimize the PDE residual of the neural network. Due to the non-convexity of the PDE residual objective function, the trained neural network may, in principle, only converge to a local minimizer of the objective function (which would not be a solution of the PDE). Therefore, there is a longstanding question regarding the mathematical foundations of these algorithms, and it is highly valuable to establish that the trained neural network will converge to the PDE solution. For a class of semi-linear PDEs (nonlinear in the solution and its first derivative), we prove that neural networks trained with gradient descent to minimize the PDE residual objective function will converge to the PDE solution.

---


### 438. [Infrared Imaging Empowered by Artificial Intelligence for Pediatric Skeletal Triage: A Narrative Review and Future Perspectives](https://arxiv.org/abs/2607.24727)

**<font color=#1a73e8>作者：</font>** Sajad Amiri, Pardis Afshar, Elham Anjomshoa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. Pediatric musculoskeletal trauma represents up to 18% of pediatric ED visits, yet diagnosis still depends on ionizing radiography. Cumulative low-dose radiation in early life raises lifetime leukemia and brain malignancy risk, motivating radiation-free triage alternatives. Objective. To synthesize evidence for a hybrid framework coupling broad-spectrum infrared (IR) imaging with deep-learning cross-modal translation to generate clinically interpretable synthetic-radiograph reconstructions from non-ionizing data.
Approach. We review five IR spectral windows spanning 650 nm to 1 mm - NIR-I, NIR-II, SWIR, MIR/LWIR, and THz - and how dual-geometry (transmission/reflection) acquisition exploits wavelength-specific tissue depth and biochemical sensitivity. We summarize image-to-image translation networks (Pix2Pix, CycleGAN, Swin-Unet) and feature-matching algorithms (SuperPoint, SuperGlue, ALIKED, LightGlue) used to align and fuse IR data into radiograph-equivalent reconstructions.
Implications. Pediatric anatomy - smaller cross-sections, thinner cortical bone - favors IR penetration, enabling compact, portable, non-ionizing triage hardware. Feasibility is grounded in fNIRS and transcranial photobiomodulation evidence: near-infrared light passes through skin, skull, and cortex with sufficient signal for hemodynamic monitoring - a longer, more attenuating path than through a pediatric forearm or distal leg. Key barriers: paired IR/X-ray dataset construction, AI-as-medical-device regulatory pathways, generalization across body habitus and skin pigmentation, and acquisition-protocol standardization.
Conclusions. Integrated multi-spectral IR+AI imaging is a promising radiation-free complement to pediatric skeletal radiography. Progress requires multi-center paired datasets, externally validated models, and IR source safety qualification under IEC 60825-1.

---


### 439. [MicroZoom: Structure-Preserving Detail Synthesis at Extreme Scale](https://arxiv.org/abs/2607.24729)

**<font color=#1a73e8>作者：</font>** Huy Huynh, Jingwei Ma, Brian Curless 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce MicroZoom, a generative framework for gigapixel image synthesis at the microscopic scale. Given a standard photograph and a sparse set of consumer-grade microscope close-ups, MicroZoom synthesizes a seamless, gigapixel-resolution image grounded in the material character of the real references, enabling exploratory visualization of microscopic texture across the full spatial extent of an object. Our goal is plausible synthesis, not exact reconstruction. We focus on full-image, reference-based, extreme-scale super-resolution at magnification levels of up to 350x, a setting that introduces two major challenges: (1) recovering texture-specific detail from highly lossy inputs near ambiguous material boundaries, and (2) preserving correct large-scale pattern structure, such as the repeating geometry of a fabric weave, across millions of local predictions. We address these with a two-stage cascaded design, where the first stage recovers global pattern coherence and the second refines local texture detail, supplemented by a segmentation mask to guide synthesis at ambiguous boundaries. We verify our approach on a collection of self-captured everyday objects and demonstrate globally coherent, materially grounded gigapixel imagery.

---


### 440. [KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability](https://arxiv.org/abs/2607.24730)

**<font color=#1a73e8>作者：</font>** Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V. 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are increasingly paired with Vision-Language Models (VLMs) to generate natural-language explanations. However, these systems add linguistic fluency without addressing the underlying opacity of the visual model. With the emergence of Kolmogorov-Arnold Networks (KANs), whose spline-based components provide inherently interpretable functional units, we investigate whether this architectural transparency can be leveraged to produce more trustworthy textual explanations. We introduce KANEx, the first ever framework that leverages the symbolic transparency of KANs to ground VLM reasoning. This interpretability also made it possible to design KAN-Map, a novel heatmap generation method derived directly from KAN models rather than gradient approximations. We feed these grounded contexts into downstream VLMs for enhanced explainability. Benchmarked on the MIMIC-CXR dataset, we demonstrate that KAN-based architectures with ResNet/ViT baselines demonstrate improved semantic similarity while producing significantly more faithful saliency maps. KAN architectures improve visual localization and downstream reasoning quality by 10%. Our findings suggest that grounding linguistic explanations and visual attributions in mathematically interpretable units is a necessary step toward trustworthy medical AI.

---


### 441. [Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation](https://arxiv.org/abs/2607.24731)

**<font color=#1a73e8>作者：</font>** Bingnan Li, Haozhe Wang, Haozhong Xiong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) adapts diffusion models by querying a teacher along trajectories generated by the current student, but how it should behave under classifier-free guidance (CFG), a default component of modern diffusion systems, remains poorly understood. Existing OPD methods naturally extend velocity matching to the CFG-composed prediction, directly matching teacher and student guided velocities. We show that this objective is under-identified at the branch level: positive- and negative-branch errors can compensate in the guided prediction. Through two contrasting cases, we find that naive matching remains effective under shared negative conditioning, where both branch errors decrease jointly. When the model's native CFG schema retains privileged information in the teacher's negative branch that is unavailable to the student, however, this joint reduction breaks down and the composed objective induces antagonistic branch-error dynamics, reducing the positive-branch error while increasing the negative-branch error. We term this failure mode Negative Branch Asymmetry (NBA). To address NBA, we introduce Positive--Direction Matching (PDM), a branch-aware OPD objective that separately constrains the positive prediction and the CFG conditional direction. We apply PDM to dense-to-sparse video control, where naive guided matching is highly sensitive to inference guidance scales, while branch-aware supervision enables more robust and effective knowledge transfer.

---


### 442. [Make or Take: How Students Navigate Self-Created and Instructor-Provided Cheat Sheets](https://arxiv.org/abs/2607.24736)

**<font color=#1a73e8>作者：</font>** Helen Weixu Chen, Victoria Sakhnini, Lesley Istead  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The use of cheat sheets in exams is often framed as a way to reduce cognitive load and support student performance. However, little is known about how students choose between self-created and instructor-provided cheat sheets, or how these choices relate to their broader approaches to exam preparation. We conducted a longitudinal study in a senior-level undergraduate software requirements course, where students could use either an instructor-provided or a self-created cheat sheet for both the midterm and final exams. Across three survey waves, we received 53, 50, and 44 responses, respectively. 41 students completed all three surveys and formed the longitudinal cohort used to examine how choices and experiences evolved over time, while exam-specific analyses used all available responses from the corresponding wave. Our findings identify several considerations that shaped students' choices, including trust in instructor expertise, the desire for personalization, and preparation efficiency. We further show how students' attitudes shifted over time and how their preferences were reflected in patterns of cheat sheet use, perceived content coverage, and challenges encountered during the exams.

---


> [!TIP]
> 当前位于：**401-442**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-442**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
