# 📦 其他研究 | 2026年07月17日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-202](./part-05.md)

---

### 151. [Implementations of Quantum and Classical Topology-Aligned Architectures for Molecular Property Prediction](https://arxiv.org/abs/2607.13737)

**<font color=#1a73e8>作者：</font>** James T. Pegg, Hubert Okadome Valencia, Ronin Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For low-data and resource-constrained regimes typical of quantum chemistry, parameter-efficient learning is a key objective. Here, we propose a topology-aligned inductive bias in which the model architecture mirrors the molecular bond graph: atoms map to a fixed register of computational units, and bonds determine which pairs interact through shared learnable parameters. This principle is instantiated in two architectures: a variational quantum circuit (Iso-QGNN), and a parameter-matched classical message-passing model (Iso-CGNN). The models are benchmarked on HOMO-LUMO and dipole moment binary classification tasks over the QM9 benchmark. With 64 trainable parameters, the implementations achieve test AUCs of approximately 0.88 (quantum) and 0.91 (classical) on the gap task, and close to 0.78 (both) on the dipole task. The models reach 90% of asymptotic performance within about 250 training molecules and gradient norms remain stable throughout training. These results indicate that the topology-aligned inductive bias is the active ingredient driving parameter efficiency at QM9 scale, with implications for matched-baseline benchmarking in quantum machine learning.

---


### 152. [Anatomically Faithful but Temporally Blind: Auditing Attribution for Left-Ventricular Ejection-Fraction Estimation from Echocardiography](https://arxiv.org/abs/2607.13738)

**<font color=#1a73e8>作者：</font>** Hyunkyung Han, Min Jung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Deep video models estimate left-ventricular ejection fraction (EF) from echocardiography with near-expert accuracy, and post-hoc attribution (Chefer relevance for transformers, Grad-CAM for CNNs) is increasingly used to certify that models "look at the right place." Yet whether these explanations are faithful both spatially and temporally is unaudited. Because EF is defined by the end-systolic (ES) and end-diastolic (ED) frames, a faithful explanation must localize the left ventricle (space) and the decisive frames (time).
Methods: We fine-tune two distinct EF regressors on EchoNet-Dynamic -- a self-supervised VideoMAE transformer and a Kinetics-pretrained R(2+1)D CNN -- and audit each with architecture-matched attribution along three axes: intersection-over-relevance (IoR) against LV masks, deletion AUC, and a temporal localization index on ES/ED frames, each relative to chance with per-case 95% CIs over 50 studies. A tubelet-occlusion probe separates attribution failure from model behavior.
Results: Both models are anatomically faithful -- IoR 2.91x (VideoMAE) and 1.98x (R(2+1)D) above chance -- yet temporally blind: temporal localization is indistinguishable from chance (0.97--1.00) and no better than random attribution. Occlusion shows the models do not preferentially rely on ES/ED (0.90x chance), so temporal blindness reflects model behavior, not an attribution artifact.
Conclusions: Spatial faithfulness does not imply temporal faithfulness. Attribution can certify anatomical grounding while masking that a model ignores the clinically decisive frames -- a caution for XAI-based validation of video diagnostic models and a call for temporally-aware training and evaluation.

---


### 153. [Algebraic Representability as the Limiting Regime of Grokking: An Exactly Solvable Model with Holomorphic Activations](https://arxiv.org/abs/2607.13749)

**<font color=#1a73e8>作者：</font>** Chon-Fai Kam, Xavier Cadet, Miloud Bessafi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks trained on modular arithmetic exhibit grokking, a delayed transition from memorisation to generalisation known to depend on model capacity: too little and the network memorises slowly or not at all, too much and it generalises almost immediately. What happens at the extreme of this spectrum, when the architecture's expressible function class collapses to a finite-dimensional algebraic variety? We study two-layer networks with a holomorphic monomial activation sigma(z)=z^k, trained on modular tasks encoded via roots of unity. Here the network output, regardless of hidden width, is confined to a (k+1)-dimensional subspace of characters of (Z_p)^2, an O(k/p^2) slice of the full function space. We give a complete algebraic characterisation of this subspace: a task is representable if and only if its discrete Fourier support lies on the diagonal u+v = k (mod p), which for linear-phase targets reduces to the arithmetic criterion m+n=k. This is not merely a constraint on eventual generalisation but on memorisation itself: because the outputs are algebraically confined, a non-representable target cannot be fit even on the training set, and we prove a positive lower bound on the training loss, independent of width. Across 585 runs the algebraic prediction matches the observed outcome with 99.8% accuracy, with no memorisation regime and no grokking; outcomes split cleanly into instant success and outright failure. This binary behaviour is the limiting case of the capacity-grokking relationship: when the expressible class shrinks to a fixed algebraic object, the question of when a network will grok dissolves into whether it can represent the target at all. A bottleneck ablation connects this extreme to standard networks, tracing a continuous path from representational failure, through memorisation without generalisation, to grokking with a shrinking gap as capacity grows.

---


### 154. [PriEval-Protect: A Unified Framework for Privacy Evaluation and Protection in Healthcare Systems](https://arxiv.org/abs/2607.13754)

**<font color=#1a73e8>作者：</font>** Ilef Chebil, Asma El Hadj, Souheib Yousfi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safeguarding patient privacy while enabling meaningful healthcare data use remains critical under GDPR and HIPAA. Existing compliance methods are manual, error-prone, and separate policy audits from data-level assessments. This paper presents PriEval-Protect, a two-phase framework for unified privacy risk evaluation and mitigation. The evaluation phase combines regulatory compliance scoring using a fine-tuned legal LLM with RAG, and technical analysis via encryption type, data architecture, and metrics including similarity, uncertainty, adversary success, and information gain/loss. A composite risk score uses weighted aggregation via Analytic Hierarchy Process. The protection phase recommends countermeasures including federated learning and differential privacy based on assessed risk. Results on hospital documents and datasets demonstrate regulation-aligned, explainable assessments, bridging legal conformance and data-level risk analysis.

---


### 155. [ZipLine: Visual Analysis of Multivariate Graphs with Predicate Logic](https://arxiv.org/abs/2607.13767)

**<font color=#1a73e8>作者：</font>** Sjoerd Vink, Suyang Li, Brian Montambault 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multivariate graphs unite two distinct data perspectives: a topological structure defined by nodes and edges, and attribute data associated with each node. Analyzing such graphs therefore requires reasoning across two complementary spaces. However, existing systems typically emphasize the analysis of one space at a time, focusing either on topology or on attributes. As a result, exploration, analysis, and pattern discovery that depend on their interaction remain difficult. In this paper, we present ZipLine, a system designed to support integrative analysis of multivariate graphs by bridging both topology and attribute spaces. ZipLine introduces a predicate language that enables analysts to express patterns involving topology, node attributes, and neighborhood relations with a unified formalism. The system further provides a predicate-learning algorithm that maps analyst interactions across both topology (e.g., subgraph selection) and attribute views (e.g., value brushing), into the predicate language, enabling learned expressions that bridge the two spaces. This integrative approach supports iterative analysis by enabling analysts to refine patterns through coordinated reasoning over topology and attributes. We demonstrate ZipLine through three case studies in energy infrastructure, cybersecurity, and drug discovery analysis. The results show that ZipLine enables expressive multivariate graph analysis through unified reasoning across topology and attributes.

---


### 156. [Mono-Z Dark Matter Search with Neural Spline Flows Using CMS Run 2015D Open Data](https://arxiv.org/abs/2607.13771)

**<font color=#1a73e8>作者：</font>** Hitesh Rasineni, Bhavishya Chebrolu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We report a search for dark matter (DM) produced in association with a leptonically decaying \(Z\) boson at \(\sqrt{s}=13\) TeV using CMS Run 2015D open data corresponding to an integrated luminosity of \(2.32\,\mathrm{fb}^{-1}\) together with simplified-model Monte Carlo simulation. Events are selected in the mono-\(Z\rightarrow\ell^+\ell^-\) final state in both the \(\mu\mu\) and \(ee\) channels. Forty kinematic observables are extracted from MINIAOD and MINIAODSIM, cleaned with physics-motivated selections, and reduced to a 37-dimensional feature vector. Five Neural Spline Flows are trained independently to model Standard Model background and mediator-specific DM signal densities. The per-event test statistic is constructed from the log-likelihood ratio between the signal and background density estimates, providing sensitivity across the full kinematic phase space without requiring a hard upper \(\mathrm{MET}\) threshold. A simultaneous profile-likelihood fit combining the two channels yields observed (expected) 95\% confidence level upper limits on the signal-strength parameter of \(\mu<0.0177\) (\(0.0018\)) for the scalar mediator, \(\mu<0.0362\) (\(0.0039\)) for the vector mediator, and \(\mu<0.0498\) (\(0.0069\)) for the axial-vector mediator. The observed limits are weaker than expected because of a residual high-\(\mathrm{MET}\) background-modeling discrepancy rather than evidence for a DM signal. To our knowledge, this is the first application of Neural Spline Flow likelihood-ratio scoring to a mono-\(Z\) dark matter search using CMS Run 2015D open data simultaneously in the \(\mu\mu\) and \(ee\) channels.

---


### 157. [EgoProceVQA: A Novel Egocentric Procedural Understanding Task with Self-Skill-Exploration Agent](https://arxiv.org/abs/2607.13792)

**<font color=#1a73e8>作者：</font>** Junlong Li, Junxi Li, Yuxiang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most daily activities are inherently procedural. However, existing evaluations for egocentric video understanding seldom address procedural understanding and largely overlook complex key-step-level reasoning under the widely used video question answering (VQA) paradigm for MLLMs. Such capabilities are crucial for building procedural AI assistants deployable on wearable devices. To bridge this gap, we introduce the Egocentric Procedural Understanding VQA task (EgoProceVQA), which systematically evaluates egocentric procedural reasoning abilities of current MLLMs and agents through six types of key-step-centric questions. Furthermore, we develop EgoProceGen, a data generation platform that efficiently constructs QA data tailored to different question types. Based on this platform, we build a benchmark with 3,600 questions, four common procedural scenarios, and 31 everyday procedural tasks. Evaluations on EgoProceVQA show that existing MLLMs and agents still have substantial room for improvement in procedural understanding. Therefore, we further propose EgoProceAgent, a self-skill-exploration agentic framework. We design a generic tool library for procedural understanding and a standardized sub-skill library shared across tools and models, enabling self-exploration without ground-truth supervision. By exploring how to compose and select sub-skills, the agent discovers effective skill strategies for diverse problems, and attains state-of-the-art performance among open-source models on multiple tasks. Together, our benchmark, generation platform, and agentic framework establish a unified foundation for EgoProceVQA. Project page: this https URL.

---


### 158. [Prospective clinical indication, post-hoc report leakage, and fusion design in multi-image chest radiograph classification: a patient-clustered evaluation](https://arxiv.org/abs/2607.13800)

**<font color=#1a73e8>作者：</font>** Kamran Shahid, Muhammad Munwar Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest radiograph datasets often combine multiple images with Clinical Indication, Findings, and Impression, although these inputs are produced at different stages of care. We evaluated 15,000 ReXGradient-160K studies with two readable images and five CheXbert-derived report observations. Frozen DenseNet-121 and Bio+ClinicalBERT encoders were used to compare image-only, Indication-only, fixed-order multimodal, random-swap, DeepSets, and SectionGuard-MI models. Findings and Impression were evaluated only as post-hoc leakage controls. Models were trained with five seeds, and public-test uncertainty was estimated with 2,000 patient-cluster bootstrap replicates. Under U-Ones, macro AUROC was 0.643 for the primary image, 0.694 for two images, 0.749 for Indication, and 0.780 for ordinary two-image-plus-Indication fusion. SectionGuard-MI achieved AUROC 0.783 and AUPRC 0.260. Relative to ordinary fusion, its paired AUROC difference was 0.0031 (95% CI, -0.0042 to 0.0104; adjusted p=0.374), while its AUPRC difference was 0.0289 (95% CI, 0.0095 to 0.0413; adjusted p=0.004). DeepSets had the highest prospective AUROC point estimate (0.787), and random-swap fusion had the highest prospective AUPRC point estimate (0.265) with better calibration than SectionGuard-MI. Full report text alone reached AUROC 0.979 and AUPRC 0.836; AUROC remained above 0.973 after exact or expanded masking. These results show that prospective Indication is strongly associated with report-derived targets, permutation-aware fusion is competitive, and post-hoc report text creates substantial report-label circularity.

---


### 159. [RainDancer: RGB-Event Video Deraining with Rain-Oriented Spiking Dynamics](https://arxiv.org/abs/2607.13802)

**<font color=#1a73e8>作者：</font>** Kui Jiang, Runzhe Li, Zhaocheng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video deraining aims to recover clean visual content from rainy videos for reliable perception under adverse weather. Existing methods mainly rely on RGB sequences and temporal redundancy, but RGB-only restoration remains ambiguous in dynamic rainy scenes, where rain streaks, textures, boundaries, motion, and occlusions may share similar visual patterns. Event cameras provide complementary motion-sensitive cues with high temporal resolution, but event streams also contain sensor noise and background-triggered responses, so direct RGB-Event fusion may introduce cross-modal interference. To address this issue, we propose RainDancer, a progressive RGB-Event video deraining framework based on a decompose-before-interact paradigm. The core idea is to separate rain and background components within each modality before cross-modal interaction. In the RGB branch, frame features are progressively decomposed into rain and background representations. In the event branch, a rain-oriented spiking neural network module captures sparse and bursty event dynamics associated with rain motion. Component-level fusion is then performed between semantically aligned representations for structure preservation and rain suppression. We further introduce event-domain supervision to regularize sparse event reconstruction, structural consistency, and gradient orientation. Experiments on synthetic and real RGB-Event video deraining datasets demonstrate superior quantitative performance, visual quality, and downstream perception robustness. Code is available at this https URL.

---


### 160. [AspectCLIP: Optimizing CLIP Representation Space via Aspect-Guided Consistency Regularization](https://arxiv.org/abs/2607.13805)

**<font color=#1a73e8>作者：</font>** Yiyang Yao, Shanglin Liu, Jianming Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pretraining learns a shared representation space through large-scale contrastive learning. However, existing methods that enforce global consistency regularization overlook a key challenge: the inherent information asymmetry between images and text: captions typically describe only one specific aspect of an image, thus images with similar visual content can be paired with completely divergent textual content and semantic information. Consequently, global regularizers inadvertently impose constraints between visually similar images whose captions describe divergent aspects, introducing semantic distortion into the representation space. We propose AspectCLIP, a framework that reformulates consistency regularization to respect this one-to-many structure. AspectCLIP first partitions training samples into attribute clusters based on textual similarity to identify aspect-coherent groups, then applies full cyclic consistency within each cluster while restricting cross-cluster regularization to prototype-level comparisons. This aspect-guided regularization enforces strict geometric alignment only when images and texts describe a consistent facet, while allowing flexibility across divergent aspects. Extensive experiments on downstream tasks demonstrate that AspectCLIP consistently outperforms traditional methods and achieves a more structured representation space.

---


### 161. [Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808)

**<font color=#1a73e8>作者：</font>** Neel Kelkar, Simon Niedermayr, Kaloian Petkov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent extensions of 3D Gaussian Splatting (3DGS) capture fine color details using hash-grid-based appearance parameterization but incur high computational cost during fragment rendering. We introduce a decoupled radiance representation that models low-frequency geometry and view dependent appearance features with 2D surfels while representing high-frequency textures via a view-independent spatial hash grid that is baked into a compact texture atlas. By including sparsity-enhancing optimizations that penalize semi-transparency and per-primitive falloff, our method aggressively prunes insignificant surfels and achieves significantly faster and sparser reconstructions than prior work. Exploiting geometric sparsity and efficient GPU texture mapping, our approach achieves up to a fivefold speedup over 3DGS while preserving state-of-the-art visual fidelity, enabling real-time 4K rendering at 60 FPS on consumer hardware.

---


### 162. [Assessing the Forensic Viability of Android Memory Analysis Across Production Builds: A Cross-Version Study of Security Hardening and Structure Preservation](https://arxiv.org/abs/2607.13821)

**<font color=#1a73e8>作者：</font>** Jayasimha Nannapanen, Sneha Sudhakaran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android memory forensics recovers evidence that never touches disk: decrypted messages, session credentials, and the live internal state of a running application. The tools that perform this recovery depend on debug symbols embedded in this http URL, the Android Runtime library, to locate data structures and interpret their layout. Across recent releases Google has stripped most of that information from the binaries that ship on consumer phones as part of a broader security hardening effort, yet no prior work has measured how far the stripping has progressed on the devices examiners actually encounter, or whether the memory architecture beneath the stripped surface still resembles what the forensics literature describes. This paper measures the gap between the unstripped development builds researchers use and the production builds that ship on real hardware, using binaries extracted from Pixel factory images across Android 8 through Android 15. Static symbols fell from 20,495 entries to zero, dynamic symbols dropped by roughly 60 percent, and source file references disappeared entirely. A compressed fallback section in the Android 15 binary restores thousands of function names but carries no structure layouts. Source code review and memory map comparisons across Android 8 and 15 show that the heap spaces, garbage collector infrastructure, and allocation bitmaps remain structurally intact, with visible changes limited to naming and arithmetic optimization. Live validation on a rooted, fully stripped Pixel 7 confirms that the runtime entry point is still locatable through the dynamic symbol table, and that structural offsets pulled from a version-matched development build resolve to valid pointers inside production memory.

---


### 163. [Reveal, Correct, Then Pay: Encrypted Mempools and Perpetual Funding Security](https://arxiv.org/abs/2607.13832)

**<font color=#1a73e8>作者：</font>** Benjamin Marsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted mempools are designed to hide transaction contents until execution order is fixed, preventing many victim dependent forms of maximal extractable value. This paper studies a different class of attack in the form of self-authored state manipulation, in which the attacker knows its own transaction and owns a downstream claim on the state that transaction changes. Perpetual futures funding is a canonical example. The funding signal determines a transfer rate, while receiving side open interest is the transfer base. In a commit then reveal mempool, an adaptive corrective transaction cannot enter the already committed batch. Privacy can therefore create an economic reaction gap even when cryptographic decryption overhead is negligible. We microfound correction through executable arbitrage opportunities. Correctors choose order size against local price impact and inventory cost, while the protocol information schedule determines which opportunities are actionable. The ordering barrier removes ordinary adaptive searchers from the closed stage. It therefore yields a closed stage correction rate below the adaptive correction rate whenever positive adaptive capacity becomes available after reveal. The distortion entering a funding window is multiplied by an explicit response factor. Transaction privacy can also reduce capitalization of predictable funding into entry prices, producing a second amplification channel. The resulting local security index separates attacker blindness, correction shielding, and capitalization shielding.

---


### 164. [NodeImport: Imbalanced Node Classification with Node Importance Assessment](https://arxiv.org/abs/2607.13837)

**<font color=#1a73e8>作者：</font>** Nan Chen, Zemin Liu, Bryan Hooi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In real-world applications, node classification on graphs often faces the challenge of class imbalance, where majority classes dominate training, resulting in biased model performance. Traditional GNNs often struggle in such scenarios, as they tend to overfit to majority classes while underrepresenting minority classes. Existing solutions, which either prioritize nodes based on class size or synthesize new nodes for minority classes, often fall short of effectively addressing this imbalance issue. This paper introduces an approach to class-imbalanced node classification by utilizing a balanced meta-set for importance measurement, where a training node is considered significant if it enhances model performance under an unbiased setting. Our method identifies important nodes that can counteract class imbalance and utilizes them for model training, allowing for fine-grained and dynamic node selection throughout the training process. We theoretically derive a formula to directly assess node importance, reducing computational overhead and providing an intuitive threshold for node selection. Guided by this metric, we develop a novel framework that filters valuable labeled, unlabeled, and synthetic nodes that enhance model performance in an unbiased context. A key advantage of this framework is its separation of the synthetic node generation process from the filtering process, ensuring compatibility with various node generation methods. Furthermore, we introduce a strategy to construct a high-quality meta-set that closely approximates the overall feature distribution, ensuring robust representation of each class. We evaluate our framework, NodeImport, across multiple datasets using popular GNN architectures, demonstrating its superiority over existing baselines. Our results highlight the flexibility and effectiveness of the framework in mitigating class imbalance, leading to improved outcomes.

---


### 165. [Heavy-Tailed Flow Matching via Random Clocks](https://arxiv.org/abs/2607.13841)

**<font color=#1a73e8>作者：</font>** Zhouhao Yang, Yezhen Wang, Kenji Kawaguchi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heavy-tailed data arise in many domains where rare events carry disproportionate importance, such as imbalanced image datasets, financial returns, and weather extremes. Standard diffusion and flow-matching models typically begin from Gaussian noise or Gaussian source distributions, which yield tractable training targets but provide a poor inductive match for heavy-tailed data. We propose Heavy-Tailed Flow Matching via Random Clocks (HTFM), a framework that portrays heavy-tailed sources as mixtures of clock-conditioned Gaussian sources. Conditioning on a given clock path, the source distribution and flow are Gaussian; marginalizing over the clock gives a Gaussian scale mixture covering Gaussian, $\alpha$-stable, and Student-t families. To make the clock-conditioned vector field practical, we encode the path-valued clock using truncated logsignature features, allowing the velocity field to adapt to the realized conditional space with negligible overhead. Empirically, on 2D imbalanced $\alpha$-stable mixtures, CIFAR10-LT, and HRRR weather fields, HTFM improves mode coverage, sample quality, and tail-statistic recovery over Gaussian flow matching and competitive heavy-tailed baselines, while retaining the low-NFE sampling advantage of flow matching. Moreover, the random-clock formulation further provides a practical tail-control interface: by varying only the clock law or tail parameter, the same architecture can calibrate the ``heaviness'' of generated tails across different distribution families.

---


### 166. [From Classification to Consistent Templates: Multiple Permuted-Label Classifier Encoding for Biometric Template Protection](https://arxiv.org/abs/2607.13845)

**<font color=#1a73e8>作者：</font>** Baogang Song, Zhongshu Zhao, Qianrong Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Biometric template protection (BTP) must secure stored templates while tolerating intra-class variations. Existing methods rely on protected-domain similarity matching, error correction, or predefined-template mappings, potentially retaining exploitable similarity structures, introducing helper-data risks, depending on artificial targets, or coupling protection to specific modalities. Storing only cryptographic hash digests eliminates directly comparable representations and conceals pre-hash templates, but hash-based exact-match verification requires genuine samples to generate identical intermediate templates before hashing. Identity classification is naturally suited to this requirement because it maps variable biometric samples to stable and discriminative identity-level outputs. Based on this insight, we propose Multiple Permuted-Label Classifier Encoding (MPLCE). Through classifier-specific label permutations, MPLCE assigns each identity different labels across multiple classifiers. The predicted labels are encoded and concatenated to form an intermediate template, preventing repeated encodings of a single identity label and enlarging the effective candidate space while preserving classification consistency. The template is randomized with an application-specific XOR string and cryptographically hashed, enabling exact-match verification without error correction codes or biometric-dependent helper data. Using modality-specific classifiers, MPLCE retains the same template generation and protection procedure across modalities. On four face and two iris datasets, MPLCE achieves competitive performance, including a GAR of 98.61\% at a FAR of 5.51\(\times\)10\textsuperscript{-5}\% on YTF and a GAR of 99.10\% at a FAR of 0.00\% on CASIA-Iris-Lamp. Security analyses and attack evaluations support its irreversibility, revocability, and unlinkability under the threat model.

---


### 167. [Relevance-Aware Rule: Structural Deletion of Irrelevant Conditions in Decision Trees](https://arxiv.org/abs/2607.13874)

**<font color=#1a73e8>作者：</font>** Jung-Sik Hong, Jeongeon Lee, Min Kyu Sim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees generate interpretable if--then rules, yet they contain irrelevant conditions (IRCs). These IRCs arise from the structural mechanism of tree splitting and persist even in modern optimal sparse tree induction algorithms. Existing IRC deletion methods overlook this structural mechanism; therefore, they either preserve the original tree too loosely to remain reliable, or too strictly to achieve meaningful simplification. This study provides theoretical foundations for reliable IRC deletion by establishing theorems and propositions related to the underlying IRC mechanism. The key finding is that a binary split shifts class proportions in opposite directions relative to the parent. Specifically, an increase in the class-1 proportion along one branch necessitates an increase in the class-0 proportion along its sibling, thereby generating a C1-link and a C0-link. Based on this structural fact, we propose a structural IRC deletion framework. Relative to each leaf, links that increase the leaf-class proportion are matched, whereas links that increase the proportion of the opposite leaf-class are mismatched. These mismatched links are flagged as structurally suspicious IRC candidates. Rather than deleting them outright, the framework rigorously diagnoses their relevance by assessing prediction reliability. It selectively deletes conditions that are structurally and empirically irrelevant, while strictly protecting those whose deletion would reduce the rule's reliability. Experimental results confirm that the proposed framework achieves substantial rule simplification without sacrificing the reliability of the original tree.

---


### 168. [AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling](https://arxiv.org/abs/2607.13877)

**<font color=#1a73e8>作者：</font>** Wenxi Liu, Michael Trimboli, Xianqi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain tumor progression exhibits spatially heterogeneous growth, patient-specific treatment response, and complex interactions with surrounding anatomy, making accurate long-term prediction challenging. We propose an AI-augmented adaptive digital twin (DT) framework for brain tumor evolution prediction and treatment scheduling. The framework integrates an interpretable reaction--diffusion (RD) model, a 3D residual learning module for model-form correction, patient-specific DT updating during recursive rollout, and model predictive control (MPC) for constrained chemotherapy and radiotherapy scheduling. Experiments on 387 synthetic tumor trajectories with 120-step evolution show that the baseline RD model captures tumor location and overall temporal behavior but underestimates heterogeneous tumor burden during long-horizon prediction. Hybrid RD--residual modeling reduces masked voxel-wise mean squared error by 84.3% and increases Dice overlap by 43.5% relative to the RD baseline under dense simulated observations. Online DT updating further reduces mean squared error by 45.9% and improves Dice overlap by 9.6% compared with the non-updated hybrid model. In MPC-based scheduling simulations, the updated DT controller reduces final tumor burden by 22.4% relative to a fixed treatment schedule under the terminal-burden objective. Together, these results demonstrate a unified framework for patient-specific initialization, mechanistic modeling, adaptive learning, and constrained treatment optimization. Although validated using patient-data-informed synthetic trajectories rather than clinical longitudinal data, the proposed framework establishes a foundation for future translation to real-world adaptive treatment planning.

---


### 169. [Task-Oriented Sensing and Covert Transmissions for Collaborative Multi-AUV Systems](https://arxiv.org/abs/2607.13880)

**<font color=#1a73e8>作者：</font>** Xueyao Zhang, Chenyang Yan, Bo Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In underwater covert cooperative missions, autonomous underwater vehicles (AUVs) often cannot rely on active sonar to continuously obtain complete information, since active sensing and frequent communications increase the risk of exposure. As a result, AUVs primarily rely on passive observation, an approach that yields incomplete local perception and limited task efficiency. Although underwater acoustic communications can mitigate this limitation through information sharing, they are simultaneously constrained by long delays, severe interference, low reliability, and the risk of covert exposure. Existing communications-oriented multi-agent reinforcement learning (MARL) studies often model communication as an ideal information flow, whereas traditional communication optimization primarily focuses on link-level performance. However, both are insufficient to characterize the actual contribution of perceptual information to cooperative tasks under realistic conditions of covert physical communications. This paper proposes a Sensed Information Value Realization Multi-Agent Reinforcement Learning (SVR-MARL) framework that leverages practical information to characterize the utility of information for cooperative tasks and learns distributed cooperative policies under realistic communication and covert constraints. Through a case study of covert multi-AUV cooperative localization and tracking, the potential of the proposed framework to improve collaborative task efficiency while reducing unnecessary communication and exposure risks is demonstrated.

---


### 170. [PiVoT: A Variational Solution for Real-time Large-scale Multi-object Detection and Tracking under Heavy Clutter](https://arxiv.org/abs/2607.13891)

**<font color=#1a73e8>作者：</font>** Runze Gan, Qing Li, Simon J. Godsill 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-object detection and tracking from noisy point clouds remain challenging in many data-scarce radar applications. Current Bayesian trackers based on Poisson measurement models offer a training-free solution but struggle to achieve accuracy and efficiency under severe clutter, large object populations, and full-resolution Doppler point clouds. We address this with PiVoT, a fast, clutter-resilient multi-object tracker for both positional and Doppler measurements. PiVoT performs end-to-end detection and tracking of a large and time-varying number of objects without external clustering or detectors, through joint inference of object states, shapes, existence probabilities, data association, and measurement rates. Its efficiency is driven by several variational inference innovations, such as theoretically justified birth pruning, quadratic-to-linear complexity reductions for exact updates, and a computationally efficient Doppler Poisson model. Experiments show that PiVoT substantially outperforms existing Bayesian trackers in challenging scenes, while also demonstrating exceptional scalability to a thousand objects, robustness to clutter visually inseparable from objects, and real-time operation on full-scale modern automotive radar datasets, where it attains performance comparable to a deep-learning detection benchmark as a training-free joint detector and tracker.

---


### 171. [Fine-Grained Vision-Language Pretraining with Organ-Conditioned Pattern Tokens for CT Understanding](https://arxiv.org/abs/2607.13892)

**<font color=#1a73e8>作者：</font>** Guoliang You, Xiaomeng Chu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) vision-language pretraining from paired volumes and radiology reports is a scalable yet challenging task. Existing methods commonly adopt global scan-report contrast, which is scalable but obscures heterogeneous organ evidence. Meanwhile, direct organ-level alignment remains coarse, since the same anatomy can exhibit multiple distinct radiological appearances. Therefore, pretraining requires a finer alignment unit: the organ-conditioned radiological pattern. In this work, we propose OCP-CT, an organ-conditioned pattern-token alignment framework for CT vision-language pretraining. Specifically, OCP-CT preserves a stable global CT-report contrastive branch and introduces an organ pattern interface: sparse Mixture-of-Experts (MoE) routes image and text tokens according to latent radiological patterns, learnable slots query the routed tokens into continuous pattern tokens, and paired token contrast aligns image-text pattern tokens with structured soft targets built from report-derived clinical similarity. On the publicly available CT-RATE and RAD-ChestCT benchmarks, OCP-CT achieves average AUROCs of 84.5% and 69.9% for zero-shot abnormality diagnosis, respectively. Compared with the strongest prior reported results, these results yield absolute AUROC gains of 6.7 and 0.8 percentage points.

---


### 172. [RF Spectrogram Anomaly Detection with Quantum Kitchen Sinks: Architecture, Representation, and Hardware Validation](https://arxiv.org/abs/2607.13897)

**<font color=#1a73e8>作者：</font>** Abdallah Aaraba, Alexis Vieloszynski, Remon Polus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The broadcast nature of wireless channels exposes radio-frequency (RF) networks to anomalous and malicious transmissions, making anomaly detection a fundamental requirement for secure spectrum management. Quantum Kitchen Sinks (QKS) offer a lightweight hybrid quantum feature map suitable for near-term quantum devices, yet their behavior on structured signal data remains poorly understood. In this paper, we extend the standard QKS template with multi-depth data re-uploading and ring entanglement, and evaluate the resulting pipeline on controlled RF spectrogram anomaly detection. We introduce a validation-locked five-stage ablation protocol that systematically separates the effects of shallow architecture, re-uploading depth, episode budget, input representation, and classical readout. Across the completed benchmark, Discrete Cosine Transform (DCT) representations consistently dominate raw and Principal Component Analysis (PCA) inputs, moderate-depth entangled QKS configurations form the strongest operating regime, and QKS improves over matched classical direct-readout baselines across all evaluated representation-readout pairs on the held-out test set, with the best configuration reaching a test Area Under the Receiver Operating Characteristic curve (AUROC) of 0.8778 and a test F1 of 0.7995. The study bridges two levels of realism: real measured sub-6\,GHz cellular signals on the data side and real-device validation on the ibm_quebec Quantum Processing Unit (QPU) on the computing side, with AUROC deviations below 0.013 relative to simulation. These results provide a practical, reproducible framework for deploying QKS-based anomaly detection in wireless networks.

---


### 173. [AIMO Interpretability Challenge](https://arxiv.org/abs/2607.13899)

**<font color=#1a73e8>作者：</font>** Michal Štefánik, Philipp Mondorf, Andreas Waldis 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models' internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together with resources from the Fields Model Initiative, the competition will provide (1) newly-published olympiad-level math reasoning problems and their symbolic representations, allowing generation of novel functional variants, (2) access to frontier reasoning models, and (3) assessments of models' adversarial robustness on these problems. Participants will use these resources, along with our computing infrastructure support, to develop methods for identifying which models solve problems robustly. Our competition will also create a new, open robustness benchmark and baseline systems, aiming to provide a lasting foundation for standard benchmarking in mathematical reasoning and interpretability. Scientifically, the competition connects interpretability and generalization research around a central question in AI research: can we determine if, and to what extent, the decision-making of frontier AI models is generalizable and thus, reliable?

---


### 174. [High-Order Question Generation in a Multilingual Educational Context](https://arxiv.org/abs/2607.13901)

**<font color=#1a73e8>作者：</font>** Suna-Şeyma Uçar, Itziar Aldabe, Nora Aranberri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Critical thinking is a fundamental skill that helps learners move beyond simple memorization. One way to develop this skill is through high-order questioning. However, crafting such questions remains a challenge for educators, and classroom practices tend to rely on low-order questions. Large Language Models have demonstrated strong capabilities in generating high-order questions, especially when guided by prompts based on Bloom's Taxonomy. Yet, existing research has largely centered on this framework and focused only on English. This study addresses these gaps by introducing prompts grounded in two alternative frameworks: Claim-Evidence-Reasoning and Divergent Questioning within a multilingual context using Basque, Spanish, and English. Results indicate that while both an open-source and a proprietary model rather effectively generate questions in all three languages, only about half of the answerable questions are recognized by teachers as high-order. A positive finding is that the alternative frameworks produce structurally and conceptually varied questions, suggesting they could complement each other and provide viable alternatives to Bloom's Taxonomy.

---


### 175. [The 2nd International StepUP Competition for Biometric Footstep Recognition: From Steps to Strides](https://arxiv.org/abs/2607.13905)

**<font color=#1a73e8>作者：</font>** Robyn Larracy, Anant Gupta, Gourav Gupta 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The International StepUP Competition Series was launched to advance research in pressure-based footstep biometrics through a standardized and challenging evaluation framework. Using the large-scale StepUP-P150 dataset (with more than 200,000 high-resolution dynamic footsteps from 150 individuals) and a previously unreleased test set, the 2nd edition of the competition addressed three key challenges: (1) generalization to unseen users with limited enrollment data, (2) robustness to domain shift caused by variations in footwear and walking speed and (3) effective fusion of paired left-right footsteps. While the first two challenges built on the inaugural competition, this edition introduced more extreme cross-domain conditions and moved beyond isolated footsteps to stride-level verification, enabling new opportunities for representation learning and inter-step information fusion. The competition attracted 26 registrants from academia and industry, with a best equal error rate of 8.00% achieved by the ArogyaPandit Research Team using a spatiotemporal CNN combined with an ensemble-based scoring strategy. The top solutions showcase the value of harnessing temporal patterns and of incorporating inference-time normalization and calibration strategies to improve scoring. However, the results also reveal that recognizing users in unseen personal footwear remains a challenge, especially in the presence of distractors with similar characteristics.

---


### 176. [An Efficient Newton Algorithm for Nonnegative Matrix Factorization with the Kullback-Leibler Divergence](https://arxiv.org/abs/2607.13919)

**<font color=#1a73e8>作者：</font>** Damien Lesens, Jérémy E. Cohen, Bora Uçar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonnegative Matrix Factorization (NMF) is a fundamental tool in unsupervised learning, which approximates a nonnegative matrix by the product of two low-rank nonnegative factors. The Kullback-Leibler (KL) divergence is best suited to measure the data to model discrepancy when the decomposed data sample follows a Poisson distribution, which is the case for count datasets such as term-document matrices or images. Most KL-NMF algorithms in the literature minimize a separable majorant of the loss to find their next iterate. We argue that this method has reached its limits and propose to use instead the second-order Taylor expansion of the loss, leading to a Newton-type method. We minimize this non-separable surrogate by proposing a generalization of the well-known HALS algorithm. This yields an efficient KL-NMF algorithm which provably converges and which competes favorably with state-of-the-art algorithms on a large variety of datasets.

---


### 177. [DeepStress: Stress-Testing Deep Search Agents](https://arxiv.org/abs/2607.13920)

**<font color=#1a73e8>作者：</font>** Ismael Rousseau, Geraldine Damnati, Frederic Bechet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic benchmarks but can lead to dramatic failure in real life applications. Therefore in this study we propose DeepStress, a stress testing framework that controls the frequency of challenging evidence by replacing the retrieval module of search agents with a controlled synthetic environment. We use this framework to control three dimensions that can affect document reliability: trustworthiness, relevance, and factuality. Testing several search agents on HotpotQA and BrowseCompPlus, we demonstrate that agents exhibit substantial differences in their ability to handle unreliable information and propose new metrics that better document systems outcomes as well as the interactions between conflicting parametric and retrieved knowledge.

---


### 178. [ExpressionCueLens: A Cross-Cultural Analysis of Human-AI Companion Conversations on Social Media](https://arxiv.org/abs/2607.13924)

**<font color=#1a73e8>作者：</font>** Lynnette Hui Xian Ng, Yunze Xiao, Lionel Z. Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based AI companion agents are increasingly being perceived not only as tools but also as social companions. On social media, people recount conversations where these agents comfort, negotiate and assert boundaries, reflecting a growing attribution of human-like qualities. To profile how agency is perceived in human-AI (HAI) interactions, we introduce the ExpressionCueLens framework, which organizes linguistic, cognitive, behavioral and perceptual cues into ten categories of anthropomorphism expressions. We apply this framework to $\sim$3500 Reddit and XiaoHongShu posts that discuss HAI companionship. Through iterative expert annotation and LLM-assisted labeling, our cross-platform analysis indicates patterns consistent with the hypothesis that XiaoHongShu users use significantly more expressions of vulnerability and emotions, and more non-perceptual cues. Reddit users employ more perceptual cues with temporality and embodiment expressions. These findings suggest that cultural and platform norms shape the way that companion agents are treated as active, agentic partners, and provides design implications for culturally sensitive HAI companion agents.

---


### 179. [Thresholded Cross-Attention for Reliable Intensity-Chromaticity Fusion in Low-Light Image Enhancement](https://arxiv.org/abs/2607.13925)

**<font color=#1a73e8>作者：</font>** Yanyi Wu, Xu Zhang, Junkai Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-Light Image Enhancement (LLIE) requires a careful balance among noise suppression, color fidelity, and efficiency. Recent HVI-based methods alleviate color entanglement by decoupling intensity and chromaticity, yet how reliably the two streams are fused again is an overlooked factor that largely determines the final quality. We observe that the confidence of cross-stream attention is strongly layer-dependent, so the fixed-quota selection of Top-K sparse attention is mismatched to it, discarding informative dependencies in some layers while retaining noisy ones in others. Motivated by this observation, we propose TCA-Net, a network built around Thresholded Cross-Attention that targets reliable intensity-chromaticity fusion in the HVI space rather than introducing yet another color representation. At its core, TCA replaces the rigid Top-K quota with a fixed confidence threshold whose retained cardinality is input- and layer-adaptive, retaining only high-confidence cross-stream interactions while suppressing unreliable ones. Around this core, two complementary designs clean up the fusion before and after it: a Phase-guided Fourier Interaction Module provides a structure-aware brightness initialization for the intensity stream prior to fusion, and a Decoupled Dual-Stream Guidance Module constructs residual intensity features to suppress chromaticity leakage during reconstruction. A Scale-Aware Consistency Regularization further improves structural robustness under scale perturbations during training. Extensive experiments on LOL-v1, LOL-v2, Sony-Total-Dark, and LSRW-Huawei demonstrate that TCA-Net delivers competitive restoration accuracy, improved color fidelity, and a compact parameter size.

---


### 180. [Cyclone: Diffusion Model for Cycle-Consistent Weather Editing from Unpaired Driving Data](https://arxiv.org/abs/2607.13927)

**<font color=#1a73e8>作者：</font>** Thang-Anh-Quan Nguyen, Moussab Bennehar, Luis Guillermo Roldao Jimenez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable perception under diverse weather conditions remains a major challenge for autonomous driving systems. A common strategy to improve robustness is either to synthesize adverse weather conditions for training perception models or to apply weather-removal techniques to recover clean inputs. However, existing approaches typically rely on synthetic data augmentation or physics-based, task-specific models that require paired training data and often struggle to generate realistic weather effects or generalize robustly to out-of-domain scenarios. Toward this problem, we present Cyclone, a unified framework for weather editing based on latent diffusion, equipped with cycle-consistent constraints and knowledge from image-text models. Cyclone enables the generation of multiple weather conditions across diverse scenes while eliminating the need for paired data. Experimental results show that our approach produces more realistic, structure-preserving outputs than existing baselines and leads to consistent improvements across several downstream driving perception tasks. Furthermore, we demonstrate that Cyclone can be distilled to a video diffusion model for temporally consistent weather editing.

---


### 181. [Plausible Deniability Guarantees for Whistleblowers](https://arxiv.org/abs/2607.13928)

**<font color=#1a73e8>作者：</font>** Leo Richter, Matt J. Kusner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Whistleblowers are a key safeguard against organizational wrongdoing, but the threat of retaliation deters reporting. Existing whistleblower-protection proposals lack formal privacy guarantees, and existing differential privacy mechanisms do not directly target the natural threat model -- one in which the audited organization itself observes auditor selection decisions and uses them to identify reporters. We formalize protection against a strong-adversary threat model as per-report $(0, \delta)$-differential privacy on the transcript of audit selections. Within this framework we prove that a natural approach -- randomized response applied at the selection step -- can never outperform uniform random auditing by more than $\delta$ at any horizon. We then give a generic mechanism that reduces private auditing to private continual counting: any $(0, \delta)$-DP continual counter plugs in by post-processing, and the audit transcript inherits the same per-report guarantee. Instantiating the reduction with a recent work in continual counting yields per-report $(0, \delta)$-DP with noise scaling as $O(\sqrt{\log T})$ across a horizon of $T$ audit decisions. A utility theorem shows that the selection error vanishes whenever the noisy report gap between the most-reported organization and the runner-up grows faster than $\sqrt{\log T}$. Simulations show a substantial improvement over randomized response.

---


### 182. [VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling](https://arxiv.org/abs/2607.13929)

**<font color=#1a73e8>作者：</font>** Yiming Ma, Xinyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial observations are continuous, heterogeneous, and noisy, whereas decoder-only next-token models are usually built around discrete symbolic inputs. We introduce Vector-Input Autoregressive Inference for Ordinal-Return Modeling (VAIOM), a decoder-only Transformer for probabilistic next-return modeling on one-hour foreign-exchange bars. VAIOM separates input representation from output likelihood: continuous multivariate financial-event vectors preserve numerical structure at the input, while a categorical distribution over the next volatility-normalized return bucket supports cross-entropy training and likelihood evaluation. The selected 0.9M Hybrid Continuous Input model combines continuous event features with categorical asset metadata, a Mixture-of-Market-States return head, Gap, volatility-regime, and Ordinal auxiliary objectives, and full-sequence supervision. Models and preprocessing are fit using pre-2024 Train data; models are selected on 2024H2 Validation and evaluated without refitting on two 2025 Test periods. Across three independent training seeds, every model outperforms fixed single-bar LightGBM baseline in both Test halves. For the canonical checkpoint, paired gains over LightGBM are 0.029 and 0.043 bits per event. Validation experiments show that continuous input improves over discrete-token input under the same categorical return objective, full-sequence supervision improves over last-position training, and auxiliary representation shaping together with a mixture-structured return head improves return likelihood in controlled comparisons. A supporting capacity study finds that the smallest evaluated complete architecture rung achieves the strongest Validation likelihood on the present corpus.

---


### 183. [HORCRUX: A Complete PQC RISC-V eXtension Architecture](https://arxiv.org/abs/2607.13939)

**<font color=#1a73e8>作者：</font>** Alessandra Dolmeta, Valeria Piscopo, Michael Hutter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work presents a compact RISC-V extension for Post-Quantum Cryptography (PQC) called HORCRUX, which provides a unified Instruction-Set Extension (ISE) supporting all NIST-approved PQC algorithms. HORCRUX addresses the difficult trade-off between crypto-agility, high performance, and low resource consumption in constrained environments, a balance typically missing in hardware extensions that focus on limited PQC subsets. By targeting shared kernels across ML-KEM, MLDSA, SLH-DSA, HQC, and Falcon, the extension introduces new RISC-V instructions executed by a resource-efficient, tightly coupled coprocessor. This architecture is specifically optimized for embedded systems with strict energy budgets and limited area. Experimental evaluation on a Zynq UltraScale+ FPGA demonstrates speedups of up to 129x for hash-based, 9x for lattice-based, and 27x for code-based schemes, while adding fewer than 21k LUTs and 4.4k FFs. ASIC results from postsynthesis characterization in 65 nm CMOS are also reported, alongside a rigorous power characterization to validate the architecture's energy efficiency. The extension's modular structure maintains backward compatibility with standard RISC-V cores, offering a scalable solution for deploying PQC on constrained embedded systems.

---


### 184. [A Self-Evolving Agent for Longitudinal Personal Health Management](https://arxiv.org/abs/2607.13940)

**<font color=#1a73e8>作者：</font>** Haoran Li, Jiebi Deng, Tong Jin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support as a person's routines, preferences, measurements and risks change. It separates shared safety rules and medical knowledge from private longitudinal memory containing profile facts, reusable procedures and episodic traces. After each episode, induction determines what should update the profile, revise a procedure, remain episodic or be excluded. We evaluated HealthClaw with a synthetic year-long benchmark and nine 200-case biomedical tasks. Across 900 longitudinal support probes, answer accuracy increased from 0.2% with current-query prompting to 45.7% with HealthClaw, while prompt-side context exposure was 71.7% lower than with full-history prompting. In 100 privacy probes, HealthClaw produced higher privacy-aware answer quality and fewer unsafe disclosures than both baselines. Across the biomedical tasks, the mean absolute gain in the task-specific primary metric was 27.0 percentage points, and seven gains remained significant after false-discovery-rate correction. These offline benchmarks support governed, self-evolving memory for longitudinal personal health agents, although clinical effectiveness requires prospective evaluation. HealthClaw is publicly available at this https URL.

---


### 185. [Peak-End-Net: A Peak-End Rule Inspired Framework for Generalizable Video Aesthetic Assessment](https://arxiv.org/abs/2607.13941)

**<font color=#1a73e8>作者：</font>** Geng Li, Haiwen Li, Rui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video aesthetic assessment (VAA) aims to predict how aesthetically pleasing a video is, yet remains far less explored than other visual assessment tasks. Its progress is hindered not only by the scarcity of large-scale benchmarks, but also by the intrinsic subjectivity of aesthetic judgment, which is shaped by human perception. In this paper, we revisit VAA from a psychological perspective and propose \textit{Peak-End-Net}, a lightweight and interpretable framework inspired by the \textit{peak-end rule}, which suggests that people tend to judge a temporal experience mainly according to its salient moments and the ending. Building on this intuition, we first transfer knowledge from image aesthetic assessment (IAA) to VAA by introducing a pretrained IAA head to produce frame-wise aesthetic priors, which serve as surrogate signals for identifying aesthetically salient moments and guiding \textit{peak-end rule}-based temporal aggregation. To further capture how a video evolves aesthetically over time, we design an aesthetic rhythm encoder that models temporal progression beyond isolated moments. Additionally, we refine the overall assessment through a dynamic gated fusion mechanism to improve robustness under distribution shift. Our method is built on a frozen vision transformer (ViT) and requires only a small number of trainable parameters, making it scalable and parameter-efficient. Extensive experiments on two existing VAA benchmarks, including in-domain evaluation on VADB and cross-domain testing on DIVIDE-3K, demonstrate that our approach achieves state-of-the-art performance, affirming the value of psychologically grounded modeling for VAA. Our code and models are available at this https URL.

---


### 186. [PlumeQuant: Uncertainty-aware consistency assessment of methane plume masks and emission-rate estimates](https://arxiv.org/abs/2607.13945)

**<font color=#1a73e8>作者：</font>** Parisa Masnadi Khiabani, Wolfgang Jentner, Alireza Rangrazjeddi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging spectrometers increasingly distribute source-resolved methane plume products in which the plume mask, integrated mass enhancement (IME), plume length, emission rate, and uncertainty are physically and algorithmically linked. Using 63 EMIT-derived Carbon Mapper plume records from 27 scenes, we show that these published scalar quantities do not uniquely constrain the plume boundary: substantially different yet plausible masks reproduce the same IME, plume length, and emission rate. Genetic-algorithm (GA) ensembles conditioned on the published IME and plume length make this equifinality explicit: the high-confidence core selected by nearly all target-consistent masks covers a median of 13% of the plausible footprint envelope, and ambiguity is largest for weak, low-overlap plumes. The diagnostics come from PlumeQuant, which recomputes IME, plume length, emission rate, and five-term uncertainty from distributed product components under stated conventions and evaluates four mask representations: the distributed reference mask, a transparent Carbon Mapper-informed analogue (CM-like), the GA ensemble, and optional expert edits. The CM-like mask is generated per plume without access to the reference mask or published quantities, with settings fixed once on a scene-disjoint 44-plume development split. It reproduced published IME with +0.72% median difference and emission rate with +0.16% (6.98% mean absolute), reached 0.843 median intersection-over-union against the reference masks, and matched the published uncertainty scale (median ratio 1.01). Holdout mean absolute errors were 7.6% (IME), 9.5% (length), and 6.1% (rate). These are product-level consistency diagnostics, not independent validation. They flag weak, offset, or ambiguous plumes for expert review.

---


### 187. [DeltaMerge-LowRes: Composing Language and Task Deltas for Low-Resource Adaptation](https://arxiv.org/abs/2607.13967)

**<font color=#1a73e8>作者：</font>** Son Ha Xuan, Xuan-Bach Le, Phat T. Tran-Truong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting a multilingual encoder to a new language \emph{and} a new task with only a few hundred gold examples is a common low-resource NLP setting, yet the two axes are usually fused via an expensive language--task fine-tuning run. We ask whether they can instead be trained separately and recombined in weight space. \DeltaMergeLowRes{} learns a language delta $\Delta_L$ from unlabeled monolingual text and a task delta $\Delta_T$ from labeled English data, then composes them at inference under one of four rules: additive, activation-guided, sparsity-aware, and a novel \emph{cross-axis TIES}. The new rule adapts the TIES-Merging steps of trimming, sign election, and merging to the language and task axes rather than to two task axes. Holding $(\Delta_L,\Delta_T)$ fixed across rules on four task families and four African languages ($158$ evaluated cells, $10{,}000$-sample paired bootstrap per cell), we find: (i) cross-axis TIES wins summarisation on $3/4$ languages by $+4$ to $+7$ chrF (chrF $18.59$ vs.\ $13.80$ task-only); (ii) it improves QA F1 by $+2.32$ and EM by $+2.91$; and (iii) sparsity-aware merging cuts classification ECE by $36\%$ at parity macro-F1. The composition rule materially changes what the merged model preserves, suppresses, and calibrates. We release all JSON traces and a claim ledger.

---


### 188. [CF-Net: Conflict Fusion with Speaker Normalisation and Certainty Weighting for Ambivalence/Hesitancy Recognition](https://arxiv.org/abs/2607.13976)

**<font color=#1a73e8>作者：</font>** Tung Hung Bui, Hong Hai Nguyen, Van Thong Huynh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting ambivalence and hesitancy (AH) in unconstrained video is challenging because the target signal is inherently ambiguous and expressed through subtle cross-modal incongruence rather than prototypical affect. We present CF-Net, a deep multimodal network submitted to the 3rd Edition of the AH Video Recognition Challenge (ABAW 11th, ECCV 2026), targeting the BAH dataset. CF-Net encodes visual, audio, and transcript streams with frozen SigLIP2, HuBERT, and DistilBERT backbones, normalises backbone features per speaker to reduce identity leakage, and fuses them via a ConflictFusion module that explicitly computes pairwise cross-modal incongruence. Training combines certainty-weighted focal loss, manifold mixup, and modality dropout; an auxiliary certainty-regression head leverages ambiguity annotations to stabilise learning on genuinely borderline samples. CF-Net achieves a Macro F1 of 0.7155 on the BAH validation set and 0.7364 (AP = 0.7492) on the private challenge test set.

---


### 189. [Constraint-Aware Counterfactual Editing for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2607.13977)

**<font color=#1a73e8>作者：</font>** S M Rafiuddin, Vamsi Krishna Pavuluri, Atriya Sen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-Based Sentiment Analysis (ABSA) requires models to identify sentiment toward specific aspects rather than relying on the global polarity of a sentence. This makes counterfactual evaluation especially challenging: a valid counterfactual should flip the sentiment of one target aspect while preserving the sentiment of all non-target aspects, semantic meaning, fluency, and factual consistency. Existing counterfactual generation methods often focus on sentence-level label flipping and may produce edits that are fluent but aspect-invalid, semantically drifting, or contradictory. To address this limitation, we propose CAVE-ABSA, a Constraint-Aware Validated Editing framework for generating and validating aspect-level counterfactuals. CAVE-ABSA localizes the opinion span associated with the target aspect, performs controlled counterfactual rewriting, refines candidates through a repair module, and filters them using aspect-level verification, semantic similarity, AMR-guided structural preservation, edit minimality, fluency, and contradiction detection. The framework is designed to construct validated counterfactual ABSA datasets for robustness evaluation and data augmentation. By explicitly separating generation from validation, CAVE-ABSA provides a principled approach for producing meaningful aspect-local counterfactuals and for testing whether ABSA models truly rely on aspect-grounded sentiment reasoning.

---


### 190. [Music-to-Dance Generation via Atomic Movements](https://arxiv.org/abs/2607.13978)

**<font color=#1a73e8>作者：</font>** Xinhao Cai, Yixuan Sun, Minghang Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Music-driven dance generation aims to produce human motion that is both rhythmically synchronized and semantically consistent with music. While recent neural approaches have achieved impressive visual realism, they typically model motion as a continuous signal and neglect its compositional nature, making generated dances structurally incoherent and difficult to control. In this work, we introduce a structure-aware framework that models choreography as a sequence of atomic movements-semantically interpretable motion events that serve as the building blocks of dance. To construct this atomic movement vocabulary, we first segment large-scale dance data and cluster them into atomic movement groups. We then employ a large language model to semantically relabel and refine the clusters, yielding a set of interpretable and reusable atomic movements. Based on these atomic movement annotations, we design a two-stage generation framework that mirrors the human choreography process. In the atomic movement planning stage, the model predicts the type, duration, and timing of atomic movements conditioned on the input music, forming a symbolic dance allocation. In the completion stage, a transition-aware generator synthesizes smooth and stylistically coherent motion conditioned on the planned structure. Extensive experiments demonstrate that our method produces dances with significantly improved structural coherence, rhythmic alignment, and perceptual naturalness compared to existing baselines, while providing enhanced interpretability and controllable editing through explicit structural representation.

---


### 191. [Screening Is Effective for Visual Recognition](https://arxiv.org/abs/2607.13983)

**<font color=#1a73e8>作者：</font>** Shunya Shimomura, Kazuhiro Hotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) has been widely used as a powerful framework for modeling global dependencies among image patches. However, its core component, self-attention assigns softmax-normalized relative weights to all patches, making it difficult to evaluate the relevance between patches independently. In visual recognition, images often contain many background or redundant patches, yet self-attention cannot explicitly reject such irrelevant patches, which may introduce unnecessary information into feature aggregation. To address this limitation, Screening has been proposed in the field of language modeling, where the relevance of each token is independently evaluated based on query-key similarity and low-relevance tokens are explicitly excluded through thresholding. In this work, we propose VisionScreen, a new vision model that extends Screening mechanism to visual recognition. VisionScreen treats image patches as tokens arranged on a two-dimensional grid and extends absolute relevance estimation based on query-key similarity to the two-dimensional spatial domain. This allows each patch to selectively aggregate only content-wise and spatially relevant patches without relying on competition among patches. Experiments on image classification benchmarks demonstrate that the proposed method outperforms conventional ViT. These results suggest that Screening can be effective for visual recognition, offering an alternative to relative feature aggregation based on softmax attention.

---


### 192. [Task-Specific Feature Fusion Method for Multi-Task Affective Behavior Analysis](https://arxiv.org/abs/2607.13986)

**<font color=#1a73e8>作者：</font>** Jiajun Sun, Zhe Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 11th Affective Behavior Analysis in-the-wild (ABAW11) Multi-Task Learning Challenge requires a unified system to predict valence-arousal, categorical expressions, and facial action units from the official s-Aff-Wild2 images. Although these tasks are naturally related through facial behavior, our validation experiments show that they benefit from different visual features, temporal processing strategies, fusion mechanisms, and calibration procedures. In this paper, we study task-adaptive feature fusion for ABAW11 multi-task affective behavior analysis. We first adapt two pretrained visual backbones, DINOv2 ViT-L and DINOv3 ConvNeXt-base, on an external expression-oriented facial image set and then freeze them to extract complementary frame-level features from the official ABAW11 data. On top of these frozen features, we systematically compare frame-level prediction heads, temporal convolutional heads, post-hoc temporal smoothing, LightGBM models, feature concatenation, gated fusion, residual fusion, late logit fusion, threshold calibration, and shared MTL structures. The final system selects task-specific fusion and prediction strategies rather than forcing all tasks to share a single architecture. On the ABAW11 validation set, the selected system achieves an EXPR macro-F1 of 0.4222, an AU macro-F1 of 0.5402, and a mean VA CCC of 0.6717, resulting in an overall validation score of 1.6341. The results suggest that task-adaptive fusion of frozen visual features is a simple and effective strategy for ABAW-style multi-task affective behavior analysis.

---


### 193. [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation](https://arxiv.org/abs/2607.13987)

**<font color=#1a73e8>作者：</font>** Sanket Badhe, Priyanka Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and runtime execution, leaving security risks throughout the broader skill lifecycle largely unexplored. In this paper, we present SkillSec-Eval, a lifecycle-aware framework for systematically evaluating the security of reusable agent skills. We first characterize the skill lifecycle and develop a threat taxonomy spanning repository admission, semantic retrieval, planner selection, execution, and skill evolution. We then instantiate this taxonomy in SkillSec-Eval and conduct a comprehensive empirical evaluation using a repository of 327 real-world skills. Our study demonstrates that vulnerabilities arise at multiple lifecycle stages beyond execution, highlighting the need for lifecycle-aware security analysis of reusable agent skills.

---


### 194. [Lyapunov Exponent as Physics-Informed Dense Reward: RL Discovery of Stabilization Beyond the Kapitza Pendulum](https://arxiv.org/abs/2607.14001)

**<font color=#1a73e8>作者：</font>** Slava Andrejev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We suggest using the Lyapunov characteristic exponent (LCE) as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion. With LCE, the agent not only successfully found the oscillatory motion known as the Kapitza pendulum but also damped the pendulum's pivoting, leaving it in a strictly upright position.

---


### 195. [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](https://arxiv.org/abs/2607.14004)

**<font color=#1a73e8>作者：</font>** Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven gains compound: after an agent has been optimized once, can it be optimized again on newly arrived tasks without eroding the gains the first round produced? We study this question with a two-phase continual-learning evaluation built from hard tasks in Terminal-Bench 2.0, comparing three approaches to agent-harness optimization (GEPA, Meta Harness, and RELAI's Verifiable Continual Learning, RELAI-VCL) under identical optimization budgets. All three methods improve over the baseline agent in the conventional, static, single-phase setting. However, once new tasks are introduced, the methods diverge sharply: GEPA's optimized agent transfers below the unoptimized baseline, Meta Harness transfers well but fails to improve further once given a second optimization budget, and RELAI-VCL is the only method that both transfers positively to unseen tasks and continues improving after those tasks are folded into the optimization objective, reaching the highest pass rate at every evaluated stage and the highest lifelong average pass rate overall (76.4% vs. 66.0% for GEPA, 64.6% for Meta Harness, and 58.7% for the baseline). Our key observation was that optimization gains compounded only when regression control was built into the optimization loop, providing an inductive bias against shortcut solutions that fail to generalize.

---


### 196. [Rethinking Penetration Testing for AI-Enabled Systems: From Resource Compromise to Behavioral Objective Violation](https://arxiv.org/abs/2607.14006)

**<font color=#1a73e8>作者：</font>** Mohammad Allahbakhsh, Mohammad Hassan Bahari, Moslem Attar-Raouf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Penetration testing traditionally evaluates whether adversaries can exploit weaknesses in software, infrastructure, configurations, or operational controls to achieve security-relevant compromise. This paradigm remains necessary for AI-enabled systems, but it is no longer sufficient. In such systems, adversaries may influence prompts, retrieved content, sensor inputs, training data, memory, tools, or human-AI interaction loops to alter system behavior without directly compromising the underlying infrastructure. This paper reframes penetration testing for AI-enabled systems as objective-driven behavioral evaluation. We define an AI-enabled system as one in which learned models materially influence behavior affecting operational outcomes, and we define AI-enabled penetration as the feasible induction of AI-governed behavior that violates one or more operational objectives under an explicit threat model. This definition preserves conventional penetration testing while extending it to adversarial pathways such as prompt injection, indirect prompt injection, data poisoning, sensor manipulation, retrieval poisoning, tool misuse, and agentic misalignment. We further propose a testing workflow that identifies operational objectives, maps AI-governed behavior, analyzes adversarial influence surfaces, defines behavioral failure criteria, executes scenario-based tests, and reports evidence linking adversarial action to objective violation. A running example involving an AI-enabled security operations center assistant illustrates how penetration may occur through behavioral influence rather than infrastructure compromise. Together, the definitions, workflow, and example provide a technical framework for evaluating adversarial success in deployed AI-enabled systems.

---


### 197. [Lighthouse RL: Sample-Efficient Circuit Optimization via Strategic Reset Points](https://arxiv.org/abs/2607.14008)

**<font color=#1a73e8>作者：</font>** Mustafa Emre Gürsoy, Stefan Uhlich, Ryoga Matsuo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce Lighthouse RL, a sample-efficient reinforcement learning (RL) approach for analog circuit sizing. Traditional methods lack generalization across different performance targets, while standard RL approaches waste resources exploring unpromising regions. Our method addresses these inefficiencies through a strategic reset strategy that initializes episodes from high-performing configurations discovered during training, called "lighthouses". These states, which are closer to the target objectives, guide exploration toward promising regions. When compared to RL and Bayesian optimization methods from the literature, we demonstrate the effectiveness of our approach on a 2D benchmark problem and on two analog circuits, showing significant improvements in sample efficiency (up to 1.72x faster), optimization performance (100% vs. 0-87% success rate), generalization (75% vs. 0-50% extrapolation success), and objective maximization. This efficiency is particularly valuable for computationally expensive black-box optimization problems, and our reset strategy can be used as a plug-and-play enhancement for any RL-based optimization approach.

---


### 198. [Transforming Rank: How Architecture Navigates the Spectral Pathologies of Depth](https://arxiv.org/abs/2607.14018)

**<font color=#1a73e8>作者：</font>** Katie Everett  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate how each component of the Transformer feedforward block architecture design determines how much rank survives across depth at initialization. We reinterpret skip connections and normalization, long understood as controlling magnitude, as mechanisms for preserving gradient rank across depth, since the very matrix multiplications and nonlinear activations that make the network expressive also reduce the rank. We show that skip connections trade off rank collapse against ensemble-like behavior, controlled by the relative scales of the branch and the skip: skip connections route the gradient around the residual branch, where rank is lost, rather than along the long gradient paths that encourage the layers to compose. The placement of the normalization layer controls this same tradeoff by setting the branch-to-skip ratio across depth, unifying much of the normalization placement and depth scaling literature, in particular why rank collapses for Post-Norm but plateaus for Pre-Norm. Other aspects of the architecture, like the two-matrix structure that expands and contracts the width, use additional parameters to preserve the representation or branch Jacobian rank. The second matrix decorrelates a coherent mean spike that would grow across blocks with a single matrix and uncentered activation, preventing the residual representation from collapsing. The width expansion between the two matrices keeps the branch Jacobian full rank: applying the rank-reducing activation in this expanded space leaves enough directions to span the original, at a width that follows a Marchenko--Pastur law. The initialization rank of the input--output Jacobian predicts which networks train on CIFAR-10. Taken together, we recast architecture design for deep networks as navigating an intrinsic tradeoff among rank collapse, ensemble-like behavior, and parameter count.

---


### 199. [Improving Wind and Solar Power Prediction with Efficient Wrapper-based Feature Selection: An Empirical Study](https://arxiv.org/abs/2607.14024)

**<font color=#1a73e8>作者：</font>** Daniel Grillmeyer, Marius Hadry, Michael Stenger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With rising global energy demand and growing awareness of climate change and its impacts, the share of renewable energies in the global energy mix continues to grow. Unlike conventional power generation, the output of renewable energy sources cannot be controlled as consistently due to their dependence on environmental conditions. Therefore, reliable prediction of current and future energy production is essential. In this paper, we report findings from two structured literature reviews on real-world renewable energy prediction tasks: wind turbine power curve modeling and photovoltaic power prediction. For the former, we conducted a comprehensive literature review ourselves, while for the latter, we synthesize the key findings regarding frequently selected input features based on an existing survey. Across both domains, our analysis reveals that despite the large number of available monitoring and environmental variables, only limited or unsystematic methods for feature selection exist. To address this gap, we propose Cluster-based Sequential Feature Selection (CSFS), a novel, model-agnostic, clustering-based wrapper method for automatic, efficient, and reliable feature selection in renewable energy prediction pipelines. To support reproducibility and reuse, we provide an open-source implementation of CSFS on GitHub. We empirically evaluate the proposed approach on both use cases and compare it with established feature selection techniques such as wrapper-based sequential feature selection (SFS), filter-based methods, and Random Forest's embedded feature importance. The results show that the wrapper-based methods overall provide better-performing selections of features. CSFS achieves a predictive performance comparable to SFS while reducing computational cost by an average of 21%.

---


### 200. [Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study](https://arxiv.org/abs/2607.14041)

**<font color=#1a73e8>作者：</font>** Zhan Chen, Jiqiao Ma, Chih-wen Kuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical Manchu OCR must accommodate various visually distinct writing styles, including regular script, running script, and the semi-cursive chancery hand used in palace memorials, despite limited labeled data. We study a multi-expert system that reuses checkpoints from an iterative fine-tuning process as domain specialists and uses a lightweight page-level image classifier to dispatch pages by visual style. When the checkpoint pool lacks a suitable specialist, we train an additional expert for that domain. On three frozen test sets, the routed system matches the selected specialist for each style at two-decimal precision: 0.30 percent CER on regular script, 1.57 percent on memorials, and 4.83 percent on running script. The router achieves 99.3 percent page-level domain accuracy and matches the domain-label oracle at the same precision. Two of the three selected specialists were not trained specifically for their final domain; only the running-script expert was trained with that domain as its target. We report the evaluation protocol, router design, and per-page predictions to make the comparison reproducible.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
