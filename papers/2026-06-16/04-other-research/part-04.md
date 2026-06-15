# 📦 其他研究 | 2026年06月16日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-211](./part-05.md)

---

### 151. [Coping in Crisis: Computational Modeling of Coping Styles in Digital Crisis Discourse During the 2023 Turkiye Earthquake](https://arxiv.org/abs/2606.14420)

**<font color=#1a73e8>作者：</font>** Şevval Çakıcı  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do people cope when disaster strikes and can we detect it at scale, in real time, from what they write? This study addresses that question using over one million Turkish-language tweets posted in the aftermath of the February 6, 2023 earthquake in Turkiye, which unfolded in a deeply polarized political context just months before a national election. Drawing on Lazarus and Folkman's (1984) coping theory, we develop a multi-label BERTurk classifier to detect three coping styles (problem-focused, emotion-focused, and meaning-making) across four theoretically motivated crisis phases. BERTurk achieves a macro F1 of 0.693, substantially outperforming a zero-shot mDeBERTa baseline (macro F1 = 0.324). Applied to the full corpus, the classifier reveals a clear temporal trajectory: problem-focused coping dominates the urgency phase and declines sharply, emotion-focused coping rises and stabilizes, and meaning-making increases monotonically. Anger correlates most strongly with meaning-making (Spearman r = 0.387), suggesting it functions as a mobilizing force toward blame attribution rather than practical action. These findings demonstrate that coping theory can be reliably operationalized in real-world digital crisis data and that doing so can help humanitarian organizations tailor their responses to where a population actually is.

---


### 152. [Breaking TinyML: Why Quantized Neural Networks Need Domain-Specific Security Analysis](https://arxiv.org/abs/2606.14427)

**<font color=#1a73e8>作者：</font>** Jacob Huckelberry, Andrea Mattia Garavagno, Yuke Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most TinyML hardware accelerators focus on supporting Quantized Neural Networks (QNNs) to meet stringent constraints on power consumption and size. Despite this, the security aspects of quantization within TinyML hardware remain largely unexplored. Although previous studies indicate that QNNs demonstrate similar or enhanced robustness when compared to full-precision Deep Neural Networks (DNNs) against typical evasion attacks, no attack strategies tailored specifically for TinyML hardware have been proposed yet. This paper addresses this shortfall by demonstrating how a two-step attack pipeline can surpass the current state-of-the-art in the QNN context and shows the need for more hardware-aware security research.

---


### 153. [MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition](https://arxiv.org/abs/2606.14459)

**<font color=#1a73e8>作者：</font>** Theresa Pekarek Rosin, Matthias Kerzel, Stefan Wermter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern Automatic Speech Recognition (ASR) systems have made remarkable progress on standard benchmarks, yet performance gaps have emerged under real-world distribution shifts, caused by recording conditions, accents, speech impairments, and noise. Existing datasets and benchmarks typically isolate these factors, which overlooks their co-occurrence in real-world applications. In this paper, we argue that model robustness can be treated as a dynamic capability that continually develops, and we introduce MoDiCoL, a Modular Diagnostic Continual Learning dataset designed for controlled analysis of linguistic content, speaker characteristics, and acoustic environments. Furthermore, we propose a real-world-inspired continual learning curriculum to simulate incremental updates and study how robustness is acquired, transferred, and forgotten. We evaluate three continual learning strategies and provide detailed insights into robustness under evolving conditions.

---


### 154. [A Computational Audit of Demographic Association Encoding in ClinicalBERT Language Predictions](https://arxiv.org/abs/2606.14460)

**<font color=#1a73e8>作者：</font>** Kehinde Temitayo Soetan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based clinical language models are increasingly integrated into high-stakes clinical decision support pipelines, yet the computational mechanisms through which demographic associations encoded in medical documentation propagate into model probability distributions remain empirically underspecified. We present a systematic computational audit of representational bias in ClinicalBERT (Alsentzer et al., 2019), a BERT-based model pretrained on MIMIC-III discharge summaries, employing two complementary probing methodologies: Log Probability Bias Analysis (LPBA), which quantifies demographic descriptor-induced shifts in masked token probability distributions across behavioral and evaluative semantic categories, and Masked Language Model-based analysis (MLM), which probes internal representational structure for demographic agency attribution encoding across 98 real clinical sentence templates and eight intersectional race-gender combinations. Corpus frequency analysis operationalizes the distinction between statistical disparity and bias amplification by benchmarking model outputs against empirical term frequencies in the MIMIC-III training corpus. Of 32 statistically significant findings, 65.6% contradict observed corpus distributions, rising to 80% for Black patients and 87.5% for agency attribution under MLM probing, providing direct empirical evidence that representational bias in ClinicalBERT operates predominantly through model-internal amplification rather than training data inheritance. Keywords: natural language processing, clinical documentation, algorithmic auditing, representational bias, health equity 1

---


### 155. [EM-NeSy: Expectation Maximization for Neurosymbolic Learning](https://arxiv.org/abs/2606.14463)

**<font color=#1a73e8>作者：</font>** Annegret Seibt, Luc De Raedt, Giuseppe Marra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic (NeSy) models integrate neural networks and symbolic reasoning for robust and interpretable AI. State-of-the-art NeSy models require that the symbolic component is expressed in a differentiable way, often complicating the use of approximate inference. We propose EM-NeSy which casts probabilistic NeSy learning as an instance of the Expectation-Maximization (EM) algorithm. In the expectation step, we compute the posterior over the neurally predicted symbols conditioned on the label via probabilistic inference. In the maximization step, we update the neural parameters based on this posterior using gradient descent only through the neural component. This formulation unlocks the full potential of the EM algorithm for NeSy learning. It allows NeSy to extend naturally to approximate reasoning without any additional modifications or differentiability requirements of the symbolic component. Furthermore, it recovers the standard end-to-end gradient-based NeSy setting under exact inference. Our experimental results demonstrate the scalability and computational efficiency of EM-NeSy.

---


### 156. [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/abs/2606.14470)

**<font color=#1a73e8>作者：</font>** Pavan C Shekar, Abhishek H S, Aswanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) reasoning is ephemeral: chains of thought vanish with the context window, pruned search branches leave no record, and memory buffers cannot be diffed, merged, or audited. Every other complex software process (code, infrastructure, data, experiments) is version-controlled; reasoning is not. We introduce GitOfThoughts, which stores an agent's reasoning tree as a git repository: every scored thought is a commit, scores are notes, outcomes are tags, and retrieval is "git log" over the agent's own history. This makes reasoning replayable, auditable, and mergeable across agents at near-zero engineering cost.
We then ask the harder question: does memory, in any substrate, actually improve accuracy? Across five substrates (none, markdown, vector, graph, git), two benchmarks, two model scales, and pre-registered replications, the answer for novel problems is no. No memory format reliably helps, and a promising early result collapsed under its own pre-registered replication. Memory pays only above what we call the copyability threshold: when the retrieved case is a near-duplicate of the current problem (similarity >~ 0.8), accuracy jumps sharply; below it, nothing. The gain is answer retrieval, not method transfer: a 4.5x larger model doubles the near-duplicate payoff yet still cannot extract a transferable method from a worked example. The only general lever we find is test-time sampling. The case for git-as-substrate is therefore auditability, provenance, and mergeability at accuracy parity. We document a retracted result and a refuted hypothesis to model the evaluation standard we hold ourselves to.

---


### 157. [Value-order Decomposition for Generalist Anomaly Detection](https://arxiv.org/abs/2606.14475)

**<font color=#1a73e8>作者：</font>** Miaoyun Zhao, Jing Chen, Miaoni Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection suffers from limited data, making cross-domain generalization particularly challenging. Generalist Anomaly Detection (GAD) aims to train a unified model on a source domain that can effectively detect anomalies in unseen target domains. In the initial semantic feature space, strong entanglement between anomalies and object categories or defect types hinders effective generalization across domains. Recent works address this issue by projecting features into a residual space; however, such methods primarily increase cross-domain overlap for normal features, while anomalous features remain specific to object categories, defect types and data domains, leading to poor alignment and generalization. To address this limitation, we propose Value-order Decomposition (VOD), a simple yet effective technique that bridges \textbf{three types of generalization gaps} across object categories, defect types (including real and synthetic defects), and data domains. VOD disentangles and suppresses object-category-, defect-type-, and domain-specific information, promoting alignment within normal and abnormal samples while preserving their separability, thereby enabling robust generalization across the three gaps. Leveraging the strong alignment between real and synthetic defects within the same object, we perform anomaly detection using only normal and synthetic-abnormal reference, and effectively generalize to unseen real defect types. Experiments on diverse industrial and medical benchmarks demonstrate that our method, using a simple cut-and-paste anomaly simulation strategy, achieves strong generalization across the three gaps.

---


### 158. [Recipe-Controlled Decoder Audit for Structural Knowledge-Graph Completion](https://arxiv.org/abs/2606.14492)

**<font color=#1a73e8>作者：</font>** Xihang Shan, Ye Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a recipe-controlled decoder audit (RCDA) for structural transductive knowledge-graph completion (KGC). The audit asks a simple reporting question: before attributing gains to an encoder or training recipe, what changes when the decoder is swapped under the same recipe? Using ComplEx and DistMult as the primary controlled pair, with targeted RotatE/TransE spot-checks, we evaluate seven benchmarks. On five standard KGs, ComplEx-vs-DistMult differences are modest but consistent under our recipe (+0.005 to +0.012 MRR), whereas CompGCN-style encoder effects vary more by dataset. On small KGs, decoder effects become the main diagnostic: Kinship shows a stable ComplEx advantage of +0.143 MRR (6 seeds), while UMLS favours ComplEx by +0.022 MRR in a clean 6-seed server rerun but reverses in an earlier provenance variant. We therefore treat small-KG decoder choice as recipe- and provenance-sensitive rather than as a fixed dataset winner. We further show that decoder choice interacts with encoder depth on WN18RR, and that under our recipe L=0 ComplEx on YAGO3-10 reaches 0.6971 +/- 0.0048 MRR at d=128. The result is a compact audit protocol: report matched decoder rows, log small-KG provenance, and sweep decoder x depth before making encoder-level claims.

---


### 159. [Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks](https://arxiv.org/abs/2606.14504)

**<font color=#1a73e8>作者：</font>** Qinlin He, Zeming Zhuang, Yongji Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical adversarial attacks on vision systems are typically studied through scene manipulation, such as adversarial patches or projections, where the adversary controls what the camera observes. Camera-side attacks using stickers or auxiliary optics have also been explored, but they treat attacks as image-space perturbations from designed patterns. This misses how physical imperfections interact with scene-dependent lighting and optics. We identify a threat: passive lens-side damage that is persistent yet trigger-conditioned, producing optical artifacts that bias geometric inference under particular visual conditions.
We instantiate this threat through Scratch-induced Lens Adversarial Streak Hijacking SLASH, a physical-world attack caused by small scratches on a camera lens or protective cover. Scratches interact with bright light sources and specular reflections to create structured streak artifacts that distort depth cues. Since the perturbation is fixed in the optical path but triggered by the scene, it is both persistent and selective. We formulate the attack in optical space, model the scratch pattern as a trigger-conditioned optical channel, and optimize one fixed configuration across diverse viewing conditions. We evaluate SLASH on monocular depth estimation and monocular 3D object detection in digital and real-world settings. Under the fixed-scratch constraint, directional depth shifts reach up to 32% relative error for monocular depth estimation, with consistent effects on monocular 3D object detection. Physical experiments confirm transfer to real camera recordings, inducing depth shifts above the model's natural prediction baseline. These findings reveal an attack surface where benign-looking hardware imperfections act as latent, scene-triggered adversarial mechanisms, challenging assumptions about physical robustness and motivating defenses for secure vision systems.

---


### 160. [PepALD: Macrocyclic Peptide Generation via Autoregressive Latent Diffusion](https://arxiv.org/abs/2606.14510)

**<font color=#1a73e8>作者：</font>** Junming Zhang, Siyu Yi, Wei Ju 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macrocyclic peptides are promising therapeutic candidates for intracellular targets, but their design requires simultaneous control over non-natural monomer chemistry, ring topology, membrane permeability, and target binding. Existing SMILES- or HELM-string generative models either operate in long atom-level sequence spaces or treat monomers as symbolic tokens with limited chemical grounding. We introduce PepALD, an Autoregressive Latent Diffusion (ALD) foundation model for \textit{de novo} macrocyclic peptide generation. The model represents HELM monomers with structured chemical embeddings, generates each residue through context-conditioned diffusion in chemically informed latent space, predicts R-group-aware ring closures during autoregressive generation, and aligns the denoiser to affinity rewards using winner-protected diffusion-adapted preference optimization. In silico experiments demonstrate PepALD's generation quality and reward-optimization performance against representative peptide generation baselines.

---


### 161. [Fodor and Pylyshyn's Systematicity Challenge Still Stands](https://arxiv.org/abs/2606.14512)

**<font color=#1a73e8>作者：</font>** Michael Goodale, Salvador Mascarenhas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The recent successes of neural networks producing human-like language have caused significant stir in cognitive science, with many researchers arguing that classical puzzles about human cognition and challenges to artificial intelligence are being solved by neural networks. A notable case is the argument from systematicity due to Jerry Fodor and Zenon Pylyshyn, argues that humans display systematic biconditional dependencies. For example, someone can understand the sentence "John saw Mary" just in case that they understand the sentence "Mary saw John." Symbolic systems explain this systematicity of language and thought, while neural networks offer no immediate explanation. Several recent articles argue that this challenge has now been met by neural networks. In particular, Brenden Lake and Marco Baroni argue that their meta-learning for compositionality protocol matches and perhaps explains human systematicity. We demonstrate that these conclusions are premature. Among other results, we found that their model struggles to learn rules that are even slightly out of distribution compared to their training data. Furthermore, the model behaves unsystematically even on many within-distribution problems. We conclude that Fodor and Pylyshyn's challenge to neural networks remains unmet.

---


### 162. [Securing the Future of IoMT in the Post-Quantum Era: An Edge-Native Federated Learning Approach](https://arxiv.org/abs/2606.14515)

**<font color=#1a73e8>作者：</font>** Taym Alshoghri, Deemah H. Tashman, Mohammad Reza Gerami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Medical Things (IoMT) devices operate under strict resource constraints while handling highly sensitive health data, making security and privacy critical concerns. Federated learning (FL) further complicates this landscape, as model updates exchanged during training may unintentionally expose private medical information. Emerging quantum computing capabilities threaten the long-term viability of conventional lightweight cryptographic mechanisms, motivating the integration of Post-Quantum Cryptography (PQC) into IoMT systems. This article discusses key enabling technologies for quantum-resilient IoMT, including post-quantum key establishment, lightweight encryption, and edge-native orchestration. We propose a scalable Kubernetes-based framework that integrates PQC into FL-enabled IoMT environments and validate it on a Raspberry Pi testbed. Results demonstrate that distributed cryptographic processing significantly reduces latency compared to sequential designs while maintaining feasible resource overhead. The primary contribution of this work lies in the design and validation of a secure orchestration and communication framework for FL-enabled IoMT systems. We conclude by outlining future directions toward energy-aware architectures, intelligent security optimization, and resilient next-generation Intelligent Internet of Medical Things (IIoMT) ecosystems.

---


### 163. [Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results](https://arxiv.org/abs/2606.14516)

**<font color=#1a73e8>作者：</font>** Jan Batzner, Sree Harsha Nelaturu, Anastassia Kornilova 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI evaluations are widely used for testing and understanding progress. However, the diverse evaluators bring with them inconsistencies that challenge analysis and comparison. First, results are saved in incompatible formats, scattered across leaderboards, papers, blog posts, evaluation harness logs, and custom repositories. Second, results are created by different evaluation frameworks, which produce divergent scores for nominally identical evaluations and record metadata inconsistently, hindering comparison, cross-community evaluation science, cost reduction, and reuse. We introduce Every Eval Ever, the first shared schema and community-crowdsourced repository for AI evaluation results. The schema standardizes how evaluations are represented in a unified, single JSON document. It is source-agnostic by design, ingesting results from evaluation harnesses and papers alike, and optionally stores per-instance outputs for fine-grained analysis. We contribute: (i) a community-governed metadata schema with a companion instance-level schema, the first standardization effort of its kind; (ii) automatic converters from popular formats, evaluation harnesses, and leaderboards to the unified schema; and (iii) a crowdsourced community database hosted on Hugging Face, currently spanning to date 22,235 models, 2,273 unique benchmarks, and 31 evaluation formats.

---


### 164. [Behavioral Audit of Machine Unlearning Has a Privacy Cost](https://arxiv.org/abs/2606.14518)

**<font color=#1a73e8>作者：</font>** Liou Tang, James Joshi, Ashish Kundu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The removal of learned data from Machine Learning models through Machine Unlearning (MU) has been widely studied; however, there has yet to be an agreed-upon scheme for auditing MU. Existing work has shown that a dishonest model owner can falsify evidence to avoid executing MU, while curious auditors (and adversaries) can infer the privacy-sensitive properties of the model and its training data even with limited access. Yet auditing of MU under mutual distrust between the model owner and the auditor remains unexplored. We provide an information-theoretic proof for this scenario: for convex ML models, a generic audit scheme that relies solely on querying the model for \textit{behavioral} signals cannot identify insufficiently unlearned models without revealing membership information of the retained set. Therefore, auditing MU under the assumption of a dishonest model owner and an honest-but-curious auditor faces an inherent privacy-audit tradeoff. Our empirical results on convex models strongly supports this result, while further experiments demonstrate that this privacy-audit tension persists in non-convex models. Our results call for a more careful consideration of the privacy-audit tension under a realistic auditor threat model, and serve as a foundation for more scrutiny of designs of privacy-preserving audit schemes for the MU pipeline. We also release our code implementation at this https URL.

---


### 165. [Detecting Bot Detection: Prevalence, Techniques, and Implications for Web Measurement Research](https://arxiv.org/abs/2606.14525)

**<font color=#1a73e8>作者：</font>** Ralf Gundelach, Michael Mühlhauser, Dominik Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Browser automation frameworks are essential tools for security and privacy research on the web, yet bot detection scripts increasingly probe their artifacts, threatening measurement validity as automated browsers may be blocked or served different content. Prior work measures detection deployment, while we measure blocking-induced sample loss. Through a literature survey of top-tier security, privacy, and web measurement venues, we find that 83% of papers omit any discussion of bot detection blocking. To address this gap, we conduct a measurement study of 10,000 websites across four browser configurations (40K page visits in total) to quantify detection prevalence and employed techniques. Using custom instrumentation to detect when sites probe for automation, we develop a taxonomy of bot detection techniques and measure how often they appear in practice. Chromium headless encounters a 15% soft block rate compared to 7% for other configurations. Across all conditions, 82% of blocks are attributable to bot detection (59% vendor-confirmed, 23% inferred from condition-dependent blocking), predominantly by providers with integrated bot detection such as Cloudflare (37% block rate) and Akamai (26%). A header spoofing experiment establishes that 75% of Chromium-headless-only blocks are caused by header-level signals alone, yet JavaScript-based environment probing is more extensive than current blocking rates suggest. These findings demonstrate that bot detection creates systematic, provider-correlated sample loss that the web measurement community neither measures nor reports. The downstream effect on specific measurement outcomes remains future work.

---


### 166. [The Risk Shadow of Principal Component Analysis: When 99.9999% Variance Preservation Causes Catastrophic Decision Errors](https://arxiv.org/abs/2606.14533)

**<font color=#1a73e8>作者：</font>** Hamidou Tembine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Principal Component Analysis (PCA) preserves variance, not the information needed to detect rare catastrophic events. This paper proves the existence of a {\it Risk Shadow}: PCA can retain over 99.9999 percent of total variance while completely erasing all signal about rare, high-impact failures. When this happens, even the best possible classifier operating on the PCA representation reduces to a constant predictor. The root cause is a fundamental mismatch between variance maximization and tail risk awareness. To break the shadow, we introduce Expectile PCA (ExPCA) and Tail-Preserving PCA (TP-PCA), two methods that reweight the data covariance toward high-impact events. We prove theoretically that ExPCA strictly outperforms PCA in retaining rare-event information, and we validate our claims on synthetic data and a real-world credit card fraud detection benchmark. Our results call for a fundamental rethinking of variance-based dimensionality reduction in high-stakes decisions.

---


### 167. [A Lightweight Fiducial-Based Pipeline for 3D Hyperspectral Mapping of ex-vivo Lumpectomy Specimens](https://arxiv.org/abs/2606.14534)

**<font color=#1a73e8>作者：</font>** Anna Bicchi, Alberto Rota, Leonardo Passoni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral Imaging (HSI) is a promising modality for intraoperative assessment of resection margins in Breast-Conserving Surgery (BCS), but its clinical translation requires aligning the inherently 2D spectral information onto the 3D shape of the excised tissue so that suspicious regions can be precisely localized for targeted follow-up. We present a fully automated, calibration-free pipeline that produces a 3D hyperspectral point cloud of an ex-vivo lumpectomy specimen from a set of consumer-camera RGB images and a single top-down HSI acquisition. The 3D geometry is reconstructed with a deep-learning Structure-from-Motion backbone, stabilized in a metric reference frame by a custom bundle adjustment that enforces consistency on the corners of four ArUco markers placed around the specimen. The HSI cube is then registered to the reconstruction without recovering the HSI camera pose: the markers, visible in both modalities, define 16 corner correspondences that drive a planar homography, and 3D coordinates are recovered by lookup on an orthographically rendered depth map. Evaluated on two ex-vivo lumpectomy specimens, the pipeline achieves a median 3D registration error below 1~mm and a 2D reprojection error below 0.02 mm, with a total per-specimen processing time under 4 minutes on accelerated hardware. These results support the feasibility of integrating HSI-guided spatial localization into intraoperative margin assessment workflows for breast-conserving surgery.

---


### 168. [Provably Safe, Yet Scalable Reinforcement Learning](https://arxiv.org/abs/2606.14536)

**<font color=#1a73e8>作者：</font>** Kai S. Yun, Zeyang Li, Navid Azizan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning (RL) aims to learn policies that optimize rewards while satisfying constraints. Predominant approaches rely on soft-constrained policy optimization, which has achieved empirical success but does not provide formal safety guarantees for the learned policy. In contrast, methods with strict guarantees typically rely on explicit certificate functions, whose construction requires the direct synthesis and verification of control-invariant sets, a process that scales poorly with state dimension and often yields overly conservative behavior. In this paper, we present the Provably Safe, yet Scalable RL (PS2-RL) framework, a novel two-phase architecture for learning provably safe policies in a scalable manner, designed to overcome the key bottlenecks of prior methods. Rather than explicitly computing invariant sets, PS2-RL leverages a learned backup policy to forward-integrate the system dynamics, generating an implicit control-invariant set online. In the first phase, the backup policy is trained with our proposed safe-arrival value function, which characterizes the optimal backup policy for invariant-set construction. In the second phase, an RL policy is trained end-to-end through a differentiable projection layer that strictly enforces the safety guarantees induced by the learned backup policy. By maximizing the volume of the implicit control-invariant set in the first phase, the resulting PS2 policy from the second phase is performant and scalable, while maintaining provable safety. Crucially, PS2-RL imposes no restrictions on the underlying RL algorithm and can be plugged into any existing training pipeline. We establish theoretical guarantees for the proposed framework and evaluate it on robotic control tasks with state dimensions up to 10, a regime in which prior provably safe RL methods struggle or become impractical.

---


### 169. [Visual Quality Score Assessment of Large White Goods in Remanufacture with Multi-View Deformable-DETR](https://arxiv.org/abs/2606.14556)

**<font color=#1a73e8>作者：</font>** Paul Koch, Vivek Chavan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remanufacturing large white goods is essential for a circular economy, yet visual quality assessment remains a manual bottleneck for training and pricing. Conventional detection methods require extensive annotation and struggle with small defects in high-resolution multi-view data. We present a multi-view framework based on Deformable-DETR for automated quality scoring that aggregates information across redundant views to extract fine-grained features. To enhance robustness with limited labels, we employ self-supervised pretraining followed by supervised fine-tuning on expert-annotated scores. Additionally, a linear projection over frozen feature maps identifies regions of interest to explain model decisions. Evaluated on an industrial multi-view dataset, our approach delivers precise quality assessments while reducing reliance on manual annotation and per-part customization, enabling scalable and transparent inspection for remanufacturing lines.

---


### 170. [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](https://arxiv.org/abs/2606.14571)

**<font color=#1a73e8>作者：</font>** Guanming Liu, Yuqi Ren, Hansu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central role of personal-agent memory is to turn stored information and prior interactions into future-oriented assistance. In daily use, useful cues come from what the agent observes and how the user interacts with the agent, and the agent must carry them forward from the current request to similar future tasks. Existing memory benchmarks usually test dialogue recall or task improvement in isolation, leaving the trajectory from streaming observations to later assistance largely untested. We introduce StreamMemBench, a streaming benchmark that constructs a two-step task sequence around each evidence anchor from EgoLife egocentric streams. The initial task tests evidence use, while the follow-up task tests whether feedback and interaction experience are reused. Four metrics diagnose evidence recall, initial evidence use, feedback incorporation, and follow-up reuse. Experiments with eight memory systems across two backbones show that current systems often fail to use observed evidence or turn feedback into reliable follow-up behavior, even when evidence is stored or feedback is incorporated locally. StreamMemBench is publicly available at this https URL.

---


### 171. [A Qualitative Review of GenAI-Based Methods for Data Generation and Augmentation in Industrial Computer Vision Applications](https://arxiv.org/abs/2606.14578)

**<font color=#1a73e8>作者：</font>** Paul Koch, Paul Hofmann, Ferdinand Waßelewsky 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-driven computer vision applications require a profound database to ensure predictable behaviors and performance. Such predictable behaviors are especially important for industrial applications in gaining trust from users. However, such a database is not readily available in industrial applications, and its acquisition is not trivial either. Active learning methods can be applied to ramp up data within a project deployment to iteratively increase the database, and thus the application predictability. Unfortunately, we observe that this often leads to a loss of user trust in the application, which is difficult to regain once lost. This leads to a "chicken-and-egg" dilemma in which neither the database nor the application is developed. In this work, we review state-of-the-art methods and approaches to further boost the database the initial active data ramp-up phase. Here, we focus on recent advancements in GenAI-based data generation and augmentation methods and review their adaptability on an industrial computer vision classification use case. Although we observe a potential for automatic data ramp-up, we also see a domain miss match in between the source (training environment) and target (industrial use-case) - regarding context defined in natural language and object characteristics.

---


### 172. [VISTA: View-Consistent Self-Verified Training for GUI Grounding](https://arxiv.org/abs/2606.14579)

**<font color=#1a73e8>作者：</font>** Xinyu Qiu, Yunzhu Zhang, Heng Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When applying Group Relative Policy Optimization (GRPO) for GUI Grounding, rollouts are sampled from a single screenshot view; groups often become either all failures on difficult instances or all successes on easy ones, yielding no useful relative advantage. We propose VISTA (View-Consistent Self-Verified Training), a GRPO-based training framework that constructs each comparison group from multiple target-preserving views of the same GUI this http URL view is generated by a crop that keeps the target element visible and remaps its box exactly, so model rollouts are compared across semantically equivalent but geometrically different inputs. To stabilize short coordinate generation without turning reinforcement learning into unconditional imitation, VISTA further adds a self-verified cross-view anchor: an oracle answer optimized with an advantage-weighted loss, excluded from the group baseline and activated only when the model has produced a maximum-reward rollout. Across five GUI-grounding benchmarks and multiple Qwen backbones, VISTA consistently improves grounding this http URL ScreenSpot-Pro, it raises Qwen3-VL 4B/8B/30B-A3B from 55.5/52.7/53.7 to 63.4/65.8/67.0. Robustness analyses further show higher worst-view accuracy and lower prediction flip rates.

---


### 173. [Persuasion Index: A Theory-Guided Framework for Persuasion Analysis](https://arxiv.org/abs/2606.14580)

**<font color=#1a73e8>作者：</font>** Liancheng Gong, Zhiyang Wang, Yiwei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying persuasive rhetorical cues is critical across domains, from detecting information manipulation and improving AI safety to advancing public health communication. We propose Persuasion Index (PI), a taxonomy of 15 dimensions grounded in persuasion theories from psychology and communication, and one transparent implementation using 55 sub-features built from lexicons and rule-based detectors. The taxonomy is modular: individual detectors can be replaced while preserving the theoretical structure. By evaluating PI on four public datasets varying in domain, style, and outcome measures, we show that PI provides a shared feature space for interpreting rhetorical patterns associated with persuasion-related outcomes. Linear models show that PI features carry meaningful predictive signal while remaining computationally lightweight. Dimension-level analyses reveal recurring associations between PI dimensions and persuasion outcomes across datasets, while also highlighting topic- and stance-specific variation. We release PI as an open-source package and web interface for principled and auditable analysis of human and AI-mediated communication.

---


### 174. [A Temporal Planning Framework for Disruption Aware Dynamic Route Optimization in Heterogeneous Railway Systems](https://arxiv.org/abs/2606.14582)

**<font color=#1a73e8>作者：</font>** Pollob Chandra Ray, Sabah Binte Noor, Fazlul Hasan Siddiqui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient route optimization play a vital role in ensuring both safety and punctuality in railway operations. It is very crucial particularly in heterogeneous multi-gauge railway networks with varying train speed, stopping pattern, infrastructure compatibility constraints increase coordination complexity. In single-track systems these challenges are further intensify due to all trains to share the same track and requires frequent track this http URL disruptions events including blocked tracks, blocked trains, engine failure and speed slowdowns introduces additional unpredictability in operations and deviate the timetable. However, existing studies predominantly focuses on high-level timetabling, omitting operational details such as track switching coordination. As a result leaving decision to human operators, increasing safety risks into railway operations. This study proposes a framework based on temporal planning for dynamic route optimization and disruption management in heterogeneous railway systems. The framework formulates railway operations as a temporal planning problem using PDDL 2.1 with explicitly modeling gauge compatibility constraints and diverse disruption scenarios. It generates conflict-free timestamped operational plans specifying both optimized schedules and executable action sequences. To evaluate the proposed framework, we developed a benchmark problem set with 200 instances using up to 1,000 track points and 120 trains. Two state-of-the-art temporal planners and a plan validator were employed to assessed the framework. The experimental results demonstrate that the framework effectively generates temporal operational plans for heterogeneous railway systems and handles multi-gauge constraints, disruptions, and reduces dependence on manual decision making.

---


### 175. [S$^2$COPE: Self-Supervised Concept Discovery via Preference Learning](https://arxiv.org/abs/2606.14586)

**<font color=#1a73e8>作者：</font>** Shilong Xiang, Zirui Zhang, Chengzhi Mao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current representation learning paradigms force a fundamental compromise: self-supervised methods scale to massive datasets but yield opaque features, whereas interpretable models remain bottlenecked by the need for dense human annotation. We introduce Self-Supervised Concept discOvery via Preference lEarning (\model), a label-free framework that resolves this dilemma. Instead of treating Vision-Large-Language Models (VLLMs) as static feature extractors, \model leverages them as active participants in a self-supervised preference optimization loop. By autonomously hypothesizing, validating, and reinforcing candidate visual attributes directly from raw imagery, our framework discovers novel, structured concepts without a single label. Extensive experiments across natural, medical, and physics domains demonstrate that \model successfully extracts domain-specific concepts where standard VLLMs often fail to generate. By amortizing concept discovery directly into the VLLM backbone through our self-supervised preference objective -- rather than relying on static generation and disjoint filtering -- we achieve up to a 24-point absolute improvement in downstream top-1 classification accuracy on unseen data. Our work suggest that interpretability can emerge through a model's autonomous interaction with incidental visual structures, without any human supervision.

---


### 176. [Zero-shot generalization of transformer neural operators to larger domains](https://arxiv.org/abs/2606.14597)

**<font color=#1a73e8>作者：</font>** Armand de Villeroché, Sibo Cheng, Vincent Le Guen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based neural operators have shown remarkable performance for approximating solution operators of partial differential equations on complex geometries. However, existing approaches implicitly assume a fixed domain size, which limits their ability to generalize at inference. In this work, we investigate domain extension, namely zero-shot inference on spatial domains that are significantly larger than those encountered during training. We argue that this setting fundamentally requires spatial locality and translation equivariance. We propose to implement this locality via a decomposable bias in the attention logits computation, enabling finely controllable locality while remaining fully decomposable into query-key inner products and directly compatible with optimized attention kernels. Combined with rotary positional embeddings, it enables expressive embeddings with controllable spatial support without altering the transformer architecture. We empirically show that our approach substantially improves zero-shot generalization to larger domains across two PDE benchmarks and a 3D industrial atmospheric flow application. Our code and datasets are available at this https URL.

---


### 177. [Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0](https://arxiv.org/abs/2606.14598)

**<font color=#1a73e8>作者：</font>** Ali Asaria, Tony Salomone, Deep Gandhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training INT8 (W8A8) quantization of diffusion transformers is widely deployed as a speed optimization, yet on consumer Ampere GPUs it is frequently slower than the FP8 and NF4 alternatives it is meant to beat. We trace this to a software artifact: the production "INT8" forward quantizes weights and activations only to immediately dequantize them back to bf16 and run a bf16 matrix multiply, never engaging the GPU's INT8 tensor cores, so the hardware's compute advantage is left entirely unrealized. We close this gap with a single fused Triton INT8 GEMM (int8xint8->int32 on Ampere tensor cores, with per-token x per-channel dequantization and bias folded into the epilogue, autotuned per GEMM shape) dropped into the Ideogram 4.0 diffusion transformer's linear layers in place of the dequantize-to-bf16 path. In the kernel, the int8xint8->int32 accumulation is bit-exact against torch._int_mm and the dequantized output matches the reference at cosine similarity 1.0 with no NaNs, running 2.8-4.2x faster than bf16 per GEMM. End to end it delivers a ~1.1x (~9-10%) speedup at 768px, and at 1024px it generates an image in 156.5 s on a single RTX 3090, faster than the single-card NF4 (164.5 s) and FP8 (172.9 s) baselines, at no measurable quality cost on these point estimates (PickScore/CLIPScore). INT8 thus goes from the slowest variant to the fastest, and 1024px becomes single-GPU feasible. The primary speed criterion (beat FP8, by ~9.5%) is comfortably met; the NF4 margin (~4.9%, single-run n=4) is within run-to-run variance we did not quantify and is best read as consistent with meeting the stretch target. We close with an honest deployment map: the win is specific to consumer Ampere, and on A100 and B200 the same kernel loses to those cards' fast native bf16/FP8 paths.

---


### 178. [LoSoNA: A Benchmark for Local Social Norm Adaptation in Group Conversations](https://arxiv.org/abs/2606.14600)

**<font color=#1a73e8>作者：</font>** Mateusz Winiarek, Maksymilian Bilski, Mateusz Jacniacki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online group chats are social spaces with local conversational norms that are rarely stated explicitly. The ability and willingness of LLM-based agents to recognize and adapt to these norms remains mostly unexplored. We introduce LoSoNA, a benchmark for local social norm adaptation in multi-party chat. Each scenario gives a subject model a curated group-chat transcript in which non-subject participants demonstrate a hidden local norm, followed by a final elicitor turn that forces a response revealing whether the subject has inferred that norm. We evaluate eight frontier and open-weight models under four prompting conditions that vary how explicitly the model is told to treat the prior conversation as evidence for how it should answer. Naive prompting remains limited for most models; explicit norm-aware prompting helps unevenly, with Gemini 3.1 Pro reaching $84.2\%$ and Claude Fable 5 reaching $81.6\%$, while several other models show small gains or regressions. LoSoNA contributes to recent calls for evaluating LLM social capabilities by testing whether models can infer local conversational norms from precedent and use them in a one-turn group-chat response.

---


### 179. [A Statistical and Machine Learning Framework for Operational Threshold Detection and Deployable Dispatch Controller Development in Hydrogen Multi-Energy Systems](https://arxiv.org/abs/2606.14601)

**<font color=#1a73e8>作者：</font>** Shadi Heenatigala, Hasanika Samarasinghe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents a statistical and machine learning framework for characterizing a hydrogen-based multi-energy system (H-MES) using one year of high-resolution operational data. Statistical analysis revealed a binary operation driven by renewable surplus, with solar irradiance explaining 45.7% of rank-based variance in hydrogen production, a large effect by conventional standards. Only high-irradiance periods triggered meaningful electrolyzer engagement, while electricity demand exerted a weaker inverse suppression effect ($\epsilon^2 = 0.126$). Multiple regression confirmed electrolyzer power as the dominant linear predictor, with a synergistic solar-wind interaction. Notably, Random Forest analysis ranked wind output first in predictive importance despite its weak bivariate correlation (r = 0.167), revealing non-linear dynamics invisible to parametric methods. A sequence model exploited strong 24-hour autocorrelation (r = 0.845) for operational forecasting, while a reinforcement learning agent optimized hydrogen revenue dispatch. The core contribution is demonstrating that statistical and machine learning approaches are complementary for H-MES modeling and control.

---


### 180. [A Comparative Study of Deep Learning Architectures for Multi-Horizon Behavioural Forecasting for Mobile Health](https://arxiv.org/abs/2606.14604)

**<font color=#1a73e8>作者：</font>** Pavlos Nicolaou, Kleanthis Malialis, Artemis Kontou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable devices and smartphones generate rich behavioural time series that can support proactive health interventions, yet systematic comparisons of modern forecasting architectures for these data are lacking. In particular, it remains unclear how models generalise across populations, how different architectures respond to participant-level fine-tuning and how forecasting accuracy degrades across multi-day horizons. We benchmark six deep learning architectures, two zero-shot Foundation Models (FM) and statistical baselines on three public datasets encompassing over 800 participants, reporting per-feature metrics for step counts, screen time and sleep duration across 1-8 day horizons. We further conduct a per-feature personalisation study across all six architectures and assess FM transferability across dataset sizes and temporal granularities. Our key findings are: (i) no single architecture dominates, PatchTST leads among trained models while the three runners-up (TCN, MLP, Transformer) show no meaningful performance difference; (ii) the FM TimesFM matches or exceeds trained models zero-shot, especially in low-data regimes and (iii) participant-level fine-tuning reduces per-feature RMSE by 16-60\%, with sleep benefiting most and step counts least. These results provide practical guidance on architecture selection, FM applicability and personalisation strategies for mobile health forecasting. To the best of our knowledge, this is the first study to jointly evaluate modern deep learning, FMs and personalisation for multi-horizon behavioural forecasting from wearables.

---


### 181. [Expert-Driven Survival Machines: Improving Stratification and Interpretability in Multiple Clinical Cohorts](https://arxiv.org/abs/2606.14608)

**<font color=#1a73e8>作者：</font>** Farica Zhuang, Zixuan Wen, Christos Davatzikos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival prediction plays a central role for healthcare providers and clinical researchers. Accurate risk stratification enables early intervention and improved patient management. Most existing deep survival models learn one common feature representation for all patients, which may hide important differences between patient subgroups. In contrast, a Mixture-of-Experts (MoE) framework allows different parts of the model to focus on different patient patterns, leading to more individualized representations. Therefore, in this work, we propose a mixture-of-experts enhanced adaptive deep clustering survival framework (AdaCSM) for modeling such heterogeneous survival patterns. We introduce a routing-based expert mechanism that enables conditional specialization within a parametric survival modeling framework. The proposed architecture allocates patients to specialized risk predictors dynamically while preserving the patient survival and subtype clustering objectives. We compare our method with state-of-the-art survival and deep clustering models on multiple real-world longitudinal clinical cohorts spanning diverse disease domains. The proposed method demonstrates improved predictive performance and leads to interpretable results in survival analysis.

---


### 182. [StereoGeo: an end-to-end stereo camera calibration method](https://arxiv.org/abs/2606.14619)

**<font color=#1a73e8>作者：</font>** Imane Meddour, Andréa Macario Barros, Cédric Gouy-Pailler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose StereoGeo, an end-to-end network-based approach for stereo camera calibration. Our method estimates the focal lengths and gravity directions of the left and right cameras, as well as the relative extrinsic transformation relating them. Existing methods often rely on calibration patterns in structured environments or address only a single camera configuration, being limited to either intrinsic or extrinsic estimation, and depending on a multi-view setups. StereoGeo extends the GeoCalib algorithm, integrating deep neural network feature extraction with a differentiable optimizer. Extensive experiments on real-world benchmarks demonstrate that StereoGeo achieves competitive performance for intrinsic calibration and provides accurate stereo extrinsic estimation, outperforming existing methods that are limited to monocular settings. The dataset used in this work is partially publicly available at this https URL.

---


### 183. [Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens](https://arxiv.org/abs/2606.14620)

**<font color=#1a73e8>作者：</font>** Ali Asaria, Tony Salomone, Deep Gandhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open diffusion language models are marketed as parallel, non-autoregressive decoders, yet the order in which a shipped checkpoint actually commits its tokens is almost never measured. We instrument DiffusionGemma 26B, a masked discrete-diffusion mixture-of-experts model built on Gemma 4, hooking its sampler's accept step to record which canvas positions commit, when, and at what confidence. Across a 686-prompt, six-regime probe suite we find that its decoding is neither parallel nor block-autoregressive: it follows a partial left-to-right commit bias whose apparent strength depends almost entirely on the granularity at which you look. Order is weak token by token and strengthens smoothly as the analysis is coarsened, so the model's "block size" turns out to be an artifact of the measuring ruler rather than the architecture. The model commits in large simultaneous batches, leaving much of the within-batch order genuinely undefined rather than merely unobserved. The behaviour is regime-dependent: structured JSON is committed in essentially arbitrary order, and a position's commit confidence tracks correctness on mathematical reasoning but carries no signal on factual recall. Commitment is aggressive, finishing in a short late burst well inside the step budget, while task accuracy matches the model's autoregressive Gemma-4 sibling. Beyond these findings, our central contribution is methodological: measuring decoding order honestly demands handling trailing-EOS padding, within-regime confounding, commit non-monotonicity, block-size sensitivity, and large commit-batch ties, each of which can otherwise manufacture a decoding-order result that is not really there.

---


### 184. [Characterizing Cultural Localization in AI-Generated Stories](https://arxiv.org/abs/2606.14626)

**<font color=#1a73e8>作者：</font>** Shaily Bhatt, Supriti Vijay, Jeremiah Milbauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The global use of artificial intelligence has increased interest in assessing the ability to generate culturally localized content, including stories. Cultural localization in stories often occurs through either templated localization -- the use of cultural markers (e.g., names, locations) in a generic narrative -- or holistic localization -- the variation of plots, values, and themes, in addition to cultural markers. We propose a method to measure the degree to which content was generated through templated localization. Specifically, we identify the lexical tokens that distinguish stories across nationalities and measure the similarity of the narratives that remain after removing them. In stories generated by five models on 125 topics for 193 nationalities, our method is able to detect that only a small subset (9-17%) of the vocabulary accounts for the variation across nationalities and that the narratives that remain after removing them contain repeated multi-word sequences, suggesting the presence of a shared culturally-agnostic narrative template. Finally, we characterize the cultural markers for their stereotypicality and offensiveness, finding that markers from 19 countries, mostly located in the Global South, are on average offensive.

---


### 185. [When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks](https://arxiv.org/abs/2606.14629)

**<font color=#1a73e8>作者：</font>** Jianzhe Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Verifier-driven self-DPO is a common recipe for self-improving production visual-language models. In this setup, a frozen verifier scores candidate generations, the top- and bottom-scoring candidates form a preference example, and DPO updates the learner. The deployment-time assumption is monotone: a stronger verifier should yield a stronger student. We show that this assumption can fail because verifier quality is highly task-specific. On a four-rung open-source verifier ladder across MathVista, MMMU, and BLINK, the same verifiers that are above-threshold and improve a Qwen-3-VL-2B student on MathVista become sub-threshold on MMMU, where their task-rubric accuracy drops to 8% to 23%.
In this regime, every verifier we tested silently regresses the student, producing drops of 3.4 to 10.9 percentage points below the frozen baseline while the DPO training loss continues to decrease. The regression replicates on a second student, Qwen-2.5-VL-3B. Moreover, within the failure regime, damage is confidence-inverted: the more accurate-but-still-wrong verifier causes larger regression than a near-random verifier, suggesting that progress-gated replay amplifies confidently wrong preference pairs. We give a compact mechanistic explanation via a variance theorem for progress-gated replay and its direction-mismatch failure mode.
The deployment message is operational rather than purely diagnostic: before running any verifier-driven loop, teams should measure target-task rubric accuracy, rank verifiers by target-task rubric quality rather than parameter count, and treat diminishing returns in above-threshold regimes as a verifier-side compute budget cap.

---


### 186. [SED:Lightweight Saliency prediction for Event-based data via Distillation](https://arxiv.org/abs/2606.14631)

**<font color=#1a73e8>作者：</font>** Romaric Mazna, Jean Martinet, Michele Magno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based saliency prediction has gained attention recently, as combining event cameras with saliency estimation can act as an upstream stage that naturally improves the efficiency of downstream eventbased perception at the edge. However, current approaches are either neuromorphic, underperforming on event-based saliency benchmarks, or too heavy for resource-constrained edge applications due to their reliance on transformers or 3D convolutions. Drawing inspiration from efficient convolutional modules, SED and aiming to exploit the temporal information in event data, we propose a lightweight network, trained through knowledge distillation, built on a Depthwise Spatio-Temporal Block (DSTconv) -- a factorization of the 3D depthwise separable convolution. Relative to its teacher, our model reduces the model size from 180 MB to 0.32 MB (562x) and the parameter count from 45M to 81k (554x), while matching or outperforming it on the N-DHF1K and N-UCF Sports datasets. Moreover, it generalizes strongly beyond its training distribution, transferring from synthetic to real event data where a model trained from scratch fails.

---


### 187. [Graph Diffusion Residuals for Control-Function Instrumental Variables](https://arxiv.org/abs/2606.14636)

**<font color=#1a73e8>作者：</font>** Rui Wu, Zongyuan Chen, Hong Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Control-function instrumental variable estimators need a first-stage residual, not merely a first-stage prediction. High-capacity first stages can interpolate treatment and leave too little residual information for the outcome equation. We study Adaptive Anisotropic Instrumental Heat Flow (A-IHF), a deterministic graph-diffusion residual extractor for flexible control functions. A-IHF treats treatment as a signal on a graph of first-stage features, uses pilot diffusion to detect large treatment jumps, attenuates conductance across those jumps, and computes the generated control with a sparse graph resolvent. Its observational selection rule uses only $(Z,X)$, combining graph generalized cross-validation, roughness, residualized-treatment relevance, and graph-admissibility filtering. The analysis decomposes error into structural leakage, residual attenuation, and residualized treatment variation, yielding finite-sample bounds, graph-admissibility rates under latent piecewise-smooth geometry, and finite-path selection calibration. Across 54 synthetic benchmark cells with tuned graph, kernel, tree, boosting, series, and neural control-function baselines, guarded observational A-IHF has the lowest average structural-response MSE; the A-IHF family beats the best non-A-IHF baseline in 32 cells. Performance is strongest when the graph captures piecewise-smooth first-stage structure.

---


### 188. [Improving Lunar Topography with Deep Learning Schrödinger Bridges](https://arxiv.org/abs/2606.14638)

**<font color=#1a73e8>作者：</font>** Matthew Repasky, Erwan Mazarico, Michael K. Barker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Increasing the resolution of planetary topography models can enable a better understanding of surface processes and geomorphology; however, existing analytical super-resolution methods are expensive and difficult to apply at large scales. Generative models provide the tools to learn complex relationships within data and can be applied at scale due to hardware accelerators and parallelization. We present a diffusion-based Schrödinger Bridge (SB) generative modeling approach for lunar topography super-resolution, connecting the distribution of low-resolution topography to that of high-resolution topography, incorporating physically-constraining optical imagery. Our approach is inspired by existing Shape-from-Shading methods, which improve a priori low-resolution topography by using optical images at the target resolution. We train SBs on a novel dataset of rendered lunar topography, emulating optical imagery from the Lunar Reconnaissance Orbiter Narrow Angle Camera. The result is a flexible approach for topography super-resolution which can provide pixel-level uncertainties in the reconstruction.

---


### 189. [Online Convex Optimization with Sublinear Noisy Probes](https://arxiv.org/abs/2606.14640)

**<font color=#1a73e8>作者：</font>** Simone Di Gregorio, Anupam Gupta, Stefano Leonardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Online Convex Optimization (OCO) over a convex set $K\subseteq \mathbb R^d$, where in each round $t$ the learner selects $x_t\in K$ and then observes a convex loss $f_t:K\to[0,1]$, with the goal of minimizing regret to the best fixed decision in hindsight. We introduce a unified probing model that generalizes two recent lines of work: sublinear best-expert queries in the experts setting, and pairwise (comparison-based) feedback available every round in OCO. In our framework, the learner has a budget of $k\le T$ pairwise probes; on a probed round it may query two points and learn which one has smaller loss.
Our main result shows that even a sublinear and noisy probe budget can provably improve worst-case regret in the full feedback OCO regime. With $k$ $\delta$-noisy pairwise probes, we obtain: $ \text{Reg}_T \le O\left(\min\left\{\sqrt{dT\ln T},\; \frac{dT\ln T}{k|1-2\delta|}\right\}\right) $, which is tight (up to logarithmic factors in $T$) across $T$, $k$ and $\delta$. Specifically regarding the noise parameter $\delta \in [0,1]$, the regret guarantee smoothly degrades as the oracle response approaches a coin flip, i.e., $\delta$ is close to $\frac{1}{2}$. When applying the same techniques to a finite $K$ for the prediction with $d$ experts setting, the resulting rates are instead completely tight in all parameters, including $d$.
Our analysis gives a streamlined treatment of pairwise probing in OCO by quantifying the benefit of probing via a variance reduction effect, combined with a second-order (variance-based) analysis of Continuous Exponential Weights.

---


### 190. [Which Directions Matter? Sparse Design for Affine Robust Optimization](https://arxiv.org/abs/2606.14648)

**<font color=#1a73e8>作者：</font>** Pedro Chumpitaz-Flores, My Duong, Juan S. Borrero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust machine learning and optimization rely on the uncertainty model choice. We investigate which uncertainty directions a model must cover when defined by a finite dictionary and a budget constraint. Selecting a subset forms an atomic uncertainty set with a closed form support function, yielding tractable robust programs for affine objectives. We propose a data driven selection rule based on a coverage objective over evaluation directions, including gradients, adversarial perturbations, or shifts observed on held out data. We prove this objective is monotone and submodular, supporting a greedy method with a $(1-1/e)$ approximation guarantee and a matching hardness barrier. We also provide a certificate bounding the loss from the selected subset and a radius calibration rule with out of sample control.

---


### 191. [Graph Structured Combinatorial Semi-Bandit with Nonlinear Reward Associations through Separable Signals](https://arxiv.org/abs/2606.14650)

**<font color=#1a73e8>作者：</font>** Christoph Bauschmann, Setareh Maghsudi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The identification of optimal structures within vast arrays of interconnected data necessitates significant sampling- and computational effort. Learning and leveraging underlying signal dependencies can improve efficiency and predictive capabilities considerably, but the ubiquity of nonlinear statistical relations amplifies the complexity of such undertakings. In this paper, we develop novel generic and adaptive strategies equipped with routines for graph-based causal reward modeling, analytic reproducing kernel methods, and Taylor approximation of functional processes. We establish theoretical performance guarantees sublinear in time and linear in data volume over time. Our analyses cover robustness to a multitude of uncertainties arising from noise interference, gradual model convergence, and solution space mismatch. The framework's general appeal is substantiated by a minimalistic set of conditions or reliance on prior estimates, while various outlined modifications address specific or extended settings. To demonstrate practical effectiveness, we conduct numerical experiments using both benchmarked synthetic and real-world transportation datasets.

---


### 192. [Abstracting Cross-Domain Action Sequences into Interpretable Workflows](https://arxiv.org/abs/2606.14654)

**<font color=#1a73e8>作者：</font>** Gaurav Verma, Scott Counts  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential or time-stamped interaction logs provide objective records of digital application usage, yet their granularity and noise often obscure meaningful insights into people's work. Such insights are essential for improving digital products in ways grounded in real-world user interactions. Prior research has applied deep learning models to cluster user actions into high-level activities, but these approaches are highly sensitive to noise and struggle to generalize across applications. To address this limitation, we introduce WorkflowView, a framework that uses large language models (LLMs) to abstract low-level action sequences into high-level activities. We establish the effectiveness and generality of our approach across three distinct, challenging sequential tasks and diverse domains: (a) zero-shot task description reconstruction from browser logs (achieving high semantic similarity, $\mu_{sim} = 0.91$), (b) few-shot student dropout prediction using MOOC interaction logs (reaching weighted $F_1 = 0.90$ with only five few-shot examples), and (c) anonymized, privacy-preserving analysis of AI tool integration within document workflows in Microsoft Word. Our work demonstrates that LLM-based abstraction is a robust and efficient path forward for transforming low-level behavioral data into high-level, interpretable, and actionable insights. We also discuss practical considerations for deploying LLM-based inferences within logging infrastructures, including computational efficiency and user privacy.

---


### 193. [HPSv3++: Scaling Reward Models Across the Full Spectrum of Diffusion Model Capabilities](https://arxiv.org/abs/2606.14657)

**<font color=#1a73e8>作者：</font>** Yijun Liu, Jie Huang, Zeyue Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models guide text-to-image (T2I) systems toward outputs aligned with human preferences. However, typical reward models such as HPSv3 are trained on pre-annotated data from earlier T2I models, without accounting for quality discriminative shifts arising from evolving model capabilities and reinforcement learning (RL) iterations, limiting their broader applicability. In this work, we propose HPSv3++, a reward model framework that elevates the HPSv3 model for varying T2I model capabilities and their RL iteration changes across the full capability-iteration spectrum. Specifically, we first introduce HPDv3++, a 212K dual-dimension preference dataset annotated for text fidelity and aesthetic quality using a recent high-capability (Qwen-Image) model with human supervision. We then propose a two-stage training framework. Stage 1 employs data-aware orthogonal gradient projection to incorporate diverse aesthetic perception from HPDv3++ while preserving the original effective human preference knowledge in HPSv3. Stage 2 further leverages unlabeled data from T2I models spanning different capability levels and RL iterations, and introduces a joint capability-iterations conditioned signal for the reward model together with a standard deviation-driven unsupervised guidance mechanism, strengthening reward model across the capability-iteration spectrum. HPSv3++ achieves state-of-the-art preference prediction, outperforming HPSv3 9.8% on HPDv3, 5.5% on GenAI-Bench, while achieving 79.1%/88.1% on our proposed HPDv3++. When used for T2I RL training, it consistently improves GenEval scores across diverse T2I models, demonstrating its wide-range capabilities. The code is available at this https URL.

---


### 194. [Giving AI a Headache: Acoustic Adversarial Attacks to Computer Vision Applications](https://arxiv.org/abs/2606.14658)

**<font color=#1a73e8>作者：</font>** Nicole Villavicencio-Garduño, Maksim Ekin Eren, Milo Prisbrey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is increasingly used to automate a variety of real-world computer vision (CV) applications, such as autonomous vehicle control, facial recognition, and security cameras. Recent research has shown that acoustic vibration can induce real physical motion in cameras, interfering with their internal stabilization mechanisms. Because the motion falls outside the conditions the stabilization system was designed to handle, the system introduces artifacts into the frame, causing AI-based CV models to misclassify, miss targets, or hallucinate objects.
Previous work used ultrasonic frequencies (>20 kHz) to perform short-range attacks, which limits them to short distances due to the attenuation exhibited by high frequencies. In this work, we investigate acoustic attacks using lower frequencies in the audible range (<20 kHz), and we further expand our analysis to include how various image and object features are affected by the attacks.
Specifically, we performed physical experiments to demonstrate the viability of our attacks on an off-the-shelf object detection model (YOLO11) by resonating a commercially available camera with various frequencies. Based on our results, we provide insights into several factors that make an AI CV system more vulnerable to these attacks, which could help inform the development of future mitigation strategies.

---


### 195. [Beyond task performance: Decoding bioacoustic embeddings with speech features](https://arxiv.org/abs/2606.14662)

**<font color=#1a73e8>作者：</font>** Ines Nolasco, Jules Cauzinille, Marius Miron 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained audio embeddings are standard in bioacoustics, yet little is known about which acoustic features these models encode, nor which are useful for a given task. This hinders transparency and limits extension to rare species or data-scarce domains. Here we reveal which speech-like features are encoded in bioacoustic representations. Using the 88~eGeMAPS features across six taxonomic groups, we apply linear and nonlinear regression probes to quantify which acoustic properties each model captures. Results confirm a ``no free lunch'' pattern: no single model captures the full feature space. A concatenated embedding achieves the highest performance, suggesting complementary acoustic space coverage across models. Loudness features are best encoded ($R^2 = 0.76$) while F0 is hardest to recover ($R^2 = 0.33$). By cross-referencing recoverability with per-species feature salience (NMI), we derive data-driven model selection guidance for bioacoustics.

---


### 196. [The Self-Aware Body: A User-Centered Framework for Designing Therapeutic Sonic Interactions](https://arxiv.org/abs/2606.14664)

**<font color=#1a73e8>作者：</font>** Prithvi Ravi Kantan, Sofia Dahl, Erika G. Spaich  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This chapter presents a framework for designing therapeutic sonic interaction technologies, with a focus on movement sonification: the real-time conversion of bodily motion into sound that serves as feedback during motor rehabilitation. Despite growing evidence for their effectiveness, technologies implementing movement sonification are yet to be systematically adopted as part of clinical practice, potentially due to a lack of standardized development methodologies as well as inadequate integration of clinical stakeholder perspectives into interaction design. The framework addresses these barriers through three interconnected contributions. The first is a conceptual reframing of the design task as the calibration of sonic variability to the perceptual affordances of the listener and the demands of the clinical context. The second is a practical design platform inspired by professional audio mixing workflows, which imposes a structured and learnable signal-flow architecture on the interaction design process and enables rapid iterative exploration. The third is a user-centered development methodology adapted from healthcare intervention science, which grounds design decisions in engagement with the clinicians and patients who will use the resulting systems. The HearWalk biofeedback system for hemiparetic gait rehabilitation illustrates the framework, and the chapter concludes by examining where large language models and AI tools can meaningfully assist each stage of this design process, as well as where human clinical and perceptual expertise remains irreplaceable.

---


### 197. [Memento: Reconstruct to Remember for Consistent Long Video Generation](https://arxiv.org/abs/2606.14667)

**<font color=#1a73e8>作者：</font>** Xuan Wei, Longbin Ji, Guan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video generation requires recurring subjects to remain consistent across various shots, viewpoints, motions, and scene transitions. Existing temporal decomposition methods improve scalability by generating videos shot by shot. However, they mainly focus on optimizing plausible next-shot continuations without verifying whether the historical memory preserves identity-critical subject evidence. Consequently, as generation proceeds, recurring subjects may be diluted, overwritten, or forgotten. In this paper, we propose Memento, a subject-reconstruction-guided framework that treats subject preservation as an explicit identity grounding problem, based on the premise that a memory bank faithfully preserving a subject should support reconstructing that subject from memory alone. Specifically, Memento jointly trains autoregressive next-shot generation with memory-based subject reconstruction, recovering target appearances using historical memory and global story captions. To disentangle long-range subject evidence from short-range cues, Memento introduces a dual-query memory mechanism, where one query retrieves identity-relevant memory and the other selects short-context keyframes for coherent continuation. Additionally, a subject-aware cinematic data pipeline provides precise reconstruction supervision via consistent, pronoun-free subject descriptions. Experiments demonstrate that Memento achieves state-of-the-art performance in long-term subject consistency, cross-shot coherence, and visual quality.

---


### 198. [When to Write and When to Suppress: Route-Specialized Dual Adapters for Memory-Assisted Knowledge Editing](https://arxiv.org/abs/2606.14668)

**<font color=#1a73e8>作者：</font>** Yining Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge editing systems must update selected facts while preserving nearby but irrelevant behavior. This paper studies this problem in a memory-assisted setting where an edit memory is retrieved at inference time and a parameter-efficient adapter corrects the model's object preference. We argue that the central design question is not only how to write an edit, but also when to suppress it. We introduce \method{}, a route-specialized dual-adapter editor. A relevance router first decides whether a prompt should receive an edit memory. Routed prompts use an edit adapter trained to prefer the new object over the original object; unrouted non-direct prompts use a separate locality adapter trained to preserve or restore the original-object preference. We evaluate \method{} on three 1,000-case protocols, \cf{}, \zsre{}, and \mquake{}, under the same memory protocol and two 7B/8B base models. On Llama-3.1-8B-Instruct, \method{} obtains the best overall probability-preference accuracy on all three benchmarks: 0.8180 on \cf{}, 0.8946 on \zsre{}, and 0.9922 on \mquake{}. The same trend holds on Qwen3-8B. Router ablations show that the relevant memory boundary differs across datasets: a lexical neural router is safest on \cf{}, while BGE embedding routing is better on \zsre{} and \mquake{}. Component and module ablations show that the gain mainly comes from separating edit injection from off-route suppression rather than from simply increasing LoRA capacity.

---


### 199. [Compressed Computation is (probably) not Computation in Superposition](https://arxiv.org/abs/2606.14673)

**<font color=#1a73e8>作者：</font>** Jai Bhagat, Sara Molas-Medina, Giorgi Giglemiani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether the Compressed Computation (CC) toy model (Braun et al., 2025) is an instance of computation in superposition. The CC model appears to compute 100 ReLU functions with just 50 neurons, achieving a better loss than expected from only representing 50 ReLU functions. We show that the model mixes inputs via its noisy residual stream, corresponding to an unintended mixing matrix in the labels. Splitting the training objective into the ReLU term and the mixing term, we find that performance gains scale with the magnitude of the mixing matrix and vanish when the matrix is removed. The learned neuron directions concentrate in the subspace associated with the top 50 eigenvalues of the mixing matrix, suggesting that the mixing term governs the solution. Finally, a semi-non-negative matrix factorization (SNMF) baseline derived solely from the mixing matrix reproduces the qualitative loss profile and improves on prior baselines, though it does not match the trained model. These results suggest CC is not a suitable toy model of computation in superposition.

---


### 200. [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/abs/2606.14674)

**<font color=#1a73e8>作者：</font>** Jixuan Chen, Jianzhi Shen, Haoqiang Kang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning. While such scaffolds often improve performance, they are often embedded in tightly coupled pipelines, making it difficult to isolate component contributions, compare alternative designs, or understand how module interactions shape agent behavior. We introduce AgentSpec, a modular specification framework that represents embodied agents as typed compositions of reusable policy components with standardized interfaces. AgentSpec standardizes the interfaces among perception, memory, reasoning, reflection, action, and optional learning, enabling components to be swapped and recombined under controlled conditions. We instantiate this framework across DeliveryBench, ALFRED, MiniGrid, and RoboTHOR, and analyze reasoning, memory, reflection, and reinforcement-learning modules across model backbones. Our results show that agent performance is governed by scaffold compatibility and interaction effects rather than isolated module strength. In particular, structured multi-granularity memory improves long-horizon state tracking, reasoning and memory interact non-uniformly across environments, reflection trades off correction and cost, and RL-trained policies compose best when optimized with deployment-time scaffold structure. AgentSpec provides a controlled foundation for studying, comparing, and designing composable LLM agents. Our code, baselines and interactive playground are publicly available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
