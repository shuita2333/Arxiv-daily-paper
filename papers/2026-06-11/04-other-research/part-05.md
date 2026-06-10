# 📦 其他研究 | 2026年06月11日

> 本类共 **269** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-269](./part-06.md)

---

### 201. [Inverse Probability Weighting and Age-of-Information Aggregation for Decentralized Federated Learning under Partial Reception](https://arxiv.org/abs/2606.10774)

**<font color=#1a73e8>作者：</font>** Chanuka A.S. Hewa Kaluannakkage, Rajkumar Buyya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized Federated Learning (DFL) over lossy wireless networks faces two key challenges: selection bias, where updates from poor-quality links are systematically underrepresented due to partial model reception, and update staleness, where asynchronous nodes contribute outdated information. We show that uniform gossip aggregation with local-fill reconstruction introduces persistent link-quality-induced bias, while completeness-based weighting further amplifies this effect. To address these challenges, we propose DFL-AA (Decentralized Federated Learning with Adaptive AoI-weighted Aggregation), which combines Inverse Probability Weighting with online EWMA-based channel estimation to correct selection bias and Age-of-Information-based weighting to mitigate staleness without requiring global synchronization. We theoretically show that DFL-AA removes link-quality distortion in expectation and experimentally demonstrate consistent improvements over state-of-the-art baselines across varying loss rates, network sizes, and heterogeneous wireless conditions.

---


### 202. [Spatially Selective Self-Training for Unsupervised Building Change Detection](https://arxiv.org/abs/2606.10775)

**<font color=#1a73e8>作者：</font>** Wafaa I. M. Hussin, Zhi Lu, Anas M. I. Mohammed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised building change detection aims to learn building-change masks from unlabeled bi-temporal remote sensing images. Existing label-free methods often follow a discrepancy-to-mask paradigm, directly using temporal differences, frozen foundation-model responses, prompt-based outputs, or post-processing results as final change maps. Although these strategies provide annotation-free cues, they do not learn a task-specific building-change detector and remain vulnerable to the gap between generic temporal discrepancies and building-defined structural changes. In practice, such discrepancies are often noisy and task-irrelevant, as appearance shifts, registration errors, and non-building modifications can produce strong but misleading responses. To address this problem, we propose SST-CD, a spatially selective self-training framework that reformulates fully label-free building change detection as end-to-end detector learning under noisy pseudo supervision.
SST-CD uses temporal discrepancies as candidate pseudo labels and trains the detector only on spatially reliable pixels, whose reliability is estimated by a local consistency criterion that filters inconsistent regions from supervision. To further stabilize noisy self-training, a lightweight feature adapter recalibrates bi-temporal features, while a prototype-based decoder produces compact change and no-change representations. Experiments on LEVIR-CD, WHU-CD, and DSIFN-CD show that SST-CD achieves F1 scores of 83.08\%, 91.69\%, and 86.60\%, respectively, outperforming existing unsupervised and label-free baselines. Code will be made publicly available.

---


### 203. [Can we trust our models? Epistemic calibration in second-order classification](https://arxiv.org/abs/2606.10777)

**<font color=#1a73e8>作者：</font>** Arthur Hoarau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation is critical for deploying machine learning models in high-stakes settings. However, classical calibration only assesses the reliability of predicted probabilities and does not evaluate whether epistemic uncertainty estimates are themselves trustworthy. This limitation is particularly relevant for second-order classification models. We introduce epistemic calibration, a principled criterion that measures whether reported epistemic uncertainty faithfully reflects the dispersion of model predictions around the ground truth. We show that epistemic calibration is a strictly stronger notion than classical calibration and captures failure modes invisible to standard metrics. We relate this work to the existing literature through an impossibility theorem that holds under the epistemic calibration hypothesis. To operationalize this concept, we propose the Expected Epistemic Calibration Error (EECE), which we prove to be a consistent estimator of a True Epistemic Calibration Error (TECE). Experiments across a broad range of uncertainty quantification methods show that epistemic calibration is a coherent and meaningful criterion and reveal substantial differences across methods, despite similar predictive performance.

---


### 204. [From Patches to Patients: A study of the tile-to-slide performance transferability in Digital Pathology](https://arxiv.org/abs/2606.10778)

**<font color=#1a73e8>作者：</font>** Sofiène Boutaj, Leo Fillioux, Maria Vakalopoulou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation Models (FMs) have recently redefined the state-of-the-art in histopathology by providing robust representations for whole-slide image (WSI) analysis. However, selecting the optimal foundation model (FM) for a specific clinical cohort currently requires multiple preprocessing steps, followed by computationally expensive feature extraction and the training of a Multiple Instance Learning (MIL) aggregator for every model. In this work, we investigate whether efficient tile-level linear probing can serve as a reliable proxy for slide-level performance, reducing the need to run full slide-level pipelines for every candidate encoder. We benchmark 19 state-of-the-art FMs on 42 slide-level and 16 tile-level tasks, comparing tile probing metrics against slide-level outcomes using ABMIL and Mean Pooling aggregations. We observe a high correlation between tile and slide performance across varying task difficulties, indicating that encoder representation quality is the primary determinant of WSI success. Sensitivity analyses show that transferability is stable across models and is more influenced by cohort sizes and numbers of tiles per slide than by average task difficulty. We also measure the agreement in best performing models between tile and slide-level tasks, showing tile benchmarks reliably shortlist strong candidates. Overall, our study indicates that tile-level benchmarking provides an efficient and practical first step for narrowing down candidate models, while slide-level evaluation remains essential for final validation on clinical tasks.

---


### 205. [A Bayesian Network Approach for Enhancing Security-Focused Decision Support Systems](https://arxiv.org/abs/2606.10782)

**<font color=#1a73e8>作者：</font>** Carolina Fernández-Martínez, Shuaib Siddiqui, Vanesa Daza  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The adoption and integration of heterogeneous stacks in most of today's open-source based networks brings clear benefits like interoperability and availability of advanced features. Yet, on the other hand the increasing number of interconnecting components and moving parts requires maintaining an ever increasing base of interdisciplinary knowledge of different tools in different domains to ensure proper operation. To alleviate such efforts, this work proposes a Decision Support System (DSS) to guide infrastructure operators through the selection of security approaches (e.g. tools) to adopt in their environments. This framework easily captures the end-user high-level requirements on the security triad for different domains and runs inference on the designated models to provide the identified tools (security mechanisms) that better serve such needs. The presented DSS aims at delivering an understandable and extensible framework to accommodate varying requirements and Bayesian Network (BN) models. The architecture and modelling of the system are proposed, aligned with its theoretical framework. Its performance is evaluated in terms of time and prediction accuracy.

---


### 206. [Being and Time in XR: Other-Presentness Beyond Co-Presence](https://arxiv.org/abs/2606.10786)

**<font color=#1a73e8>作者：</font>** Koichi Toida  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research in XR (Extended Reality) has conventionally centred upon concepts such as Presence, Embodiment, Social Presence, and Co-presence. Within these traditions, bodily action, sensory contingencies, synchronous interaction, and possibilities for action have generally been regarded as constitutive conditions for the experience of "being there" and of being with others. XR environments, however, permit the partial separation of conditions that ordinarily co-vary in everyday experience. Bodily co-presence, temporal simultaneity, spatial configuration, and social interaction need not remain inseparable. This paper approaches this possibility as a problem of other-presentness. Other-presentness refers to the conditions under which another individual is experienced as existing "here and now". The contribution of this paper does not lie in arguing that asynchronous others can evoke social responses; such observations have already been addressed within parasocial interaction and social presence research. Rather, the novelty lies in theorising XR as a technological condition capable of separating and operationalising the constitutive elements of other-presentness as design variables. Reconsidering Bodyless Presence as a methodological precedent and drawing upon experimental findings from Immersive Video research, this paper formulates Bodyless Presentness as a condition in which another individual continues to be experienced as presently existing despite attenuated bodily co-presence and weakened real-time simultaneity.

---


### 207. [Accelerating NeurASP with vectorization and caching](https://arxiv.org/abs/2606.10787)

**<font color=#1a73e8>作者：</font>** Alexander Philipp Rader, Alessandra Russo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic AI combines neural networks with symbolic programs to create robust and explainable predictions. One such framework is NeurASP, which trains a neural network to predict concepts and reasons over them using rules written in answer set programming (ASP) to solve downstream tasks. Crucially, labels are only provided for the downstream prediction produced by the symbolic rules, not for the latent concepts this http URL through the non-differentiable ASP component requires expensive probability and gradient calculations, which has hindered scalability to more sophisticated this http URL this paper, we address the current limitations of NeurASP by improving its computational performance through vectorization, batch processing and caching of intermediate computations during training. We compare computation speeds between the original and our new implementation of NeurASP and report speedups of multiple orders of magnitude for larger tasks. To this end, we propose a new dataset of difficult tasks involving playing cards, which we use to test the capabilities of NeurASP's enhanced learning function.

---


### 208. [Closing the Modality Gap in Zero-Shot HAR: Contrastive Training and Separability-Optimized Prototypes on IMU Data](https://arxiv.org/abs/2606.10789)

**<font color=#1a73e8>作者：</font>** Anik Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot learning (ZSL) for inertial measurement unit (IMU)-based human activity recognition (HAR) faces a central challenge: bridging the gap between sensor embeddings and semantic class representations. We systematically evaluate seven configurations combining three inference methods with two training pipelines on the PAMAP2 dataset, using 14 seen and 4 unseen activity classes with subjects 108 and 109 held out for testing. We find that the modality gap is a training-time phenomenon governed by the encoder objective. A temporal convolutional network (TCN) trained with cross-entropy over label-name Sentence- BERT prototypes yields sensor embeddings with a mean cosine similarity of 0.30 to the corresponding text prototypes, while replacing the label-name prototype targets with discriminative activity descriptions raises this to 0.69. This alignment improvement transfers consistently across all three inference methods. The strongest result combines contrastive training with inverted softmax correction, achieving 73.2% accuracy and 0.583 macro F1 on unseen classes, compared to 58.3% accuracy and 0.34 macro F1 for the label-name baseline. A secondary finding is that richer text descriptions reduce inter-prototype separability in Sentence-BERT space, because shared biomechanical vocabulary causes the language model to compress the prototype cloud. This effect does not negate the benefits of contrastive alignment provided prototype descriptions retain sufficient discriminative vocabulary. We also demonstrate that overall accuracy is a misleading primary metric when test-set class distributions are imbalanced, and recommend macro-averaged F1 as the standard reporting metric for ZSL-HAR benchmarks.

---


### 209. [READER: Robust Evidence-based Authorship Decoding via Extracted Representations](https://arxiv.org/abs/2606.10794)

**<font color=#1a73e8>作者：</font>** Jiaxu Liu, Sunnan Mu, Dong Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic applications increasingly route user tasks through official and third-party LLM APIs, provenance becomes an operational question: which model generated a given black-box response? We study Dynamic Black-Box LLM Provenance: identifying the source LLM from generations elicited by query-varying, non-predefined prompts rather than a fixed input set or benchmark suite. This setting is difficult because prompt semantics dominate the text, while model-specific authorship traces are weak and inconsistent at the surface level. We introduce READER (Robust Evidence-based Authorship Decoding via Extracted Representations), a lightweight provenance framework that treats a frozen proxy LLM as a reader of hidden authorship evidence. READER maps black-box outputs into proxy activation space, temporally filters token states within each response, and performs Bayesian Evidence Accumulation by summing single-response log-posterior evidence across independently sampled prompts. This avoids fragile mean-pooling of prompt-specific representations while preserving the query-wise evidence needed for calibrated confidence. On Agent500, a 50-target dataset built from agent-style prompts, READER reaches $31.0$-$42.4\%$ top-1 accuracy from a single response and $70.0$-$84.0\%$ from 50 responses, substantially outperforming sentence-encoder fingerprints. Scaling across nine proxy readers further shows that stronger LLMs expose more linearly decodable authorship structure, suggesting that authorship perception is already present in frozen LLM representations and can be converted into reliable multi-query attribution.

---


### 210. [SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning](https://arxiv.org/abs/2606.10804)

**<font color=#1a73e8>作者：</font>** Wenhao Yan, Fengjia Guo, Zhuoyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controlled character animation requires transferring motion from a driving sequence to a reference character. Prior works heavily rely on intermediate representations, including pose skeletons to represent motion or masked background to represent environment, which inevitably leads to information loss. To address this, we present SCAIL-2, an framework that bypasses those intermediates and achieves \textbf{end-to-end} character animation. By directly concatenating driving videos to the sequence, the model can obtain all the required visual information from the input video. To address lack of end-to-end data, we unify sub-tasks of character animation with decoupled conditions and then curate a pipeline to synthesize MotionPair-60K, an end-to-end motion transfer dataset containing heterogeneous tasks of character animation. To archive the unification, we utilize in-context mask conditioning and mode-specific RoPE as soft guidance beyond textual instructions and raw visual information. To address synthetic discrepancy in detailed regions, we propose Bias-Aware DPO to construct preference items to mitigate the errors. Extensive experiments demonstrate that our method substantially outperforms existing state-of-the-art approaches in various character animation tasks. A large subset of synthetic data as well as model weights will be released at our project page: this https URL.

---


### 211. [Moonshine: An Autonomous Mathematical Research Agent Centered on Conjecture Generation](https://arxiv.org/abs/2606.10806)

**<font color=#1a73e8>作者：</font>** Xiaoyang Chen, Xiang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Moonshine is an autonomous agent whose central objective is to generate mathematical conjectures. Its core capability is to extract structure from classical problems, distill new concepts, and formulate conjectures of mathematical significance. Rather than treating the solution of a single proposition as its endpoint, Moonshine builds an extensible theoretical framework through conjecture generation, bridge building, and obstacle identification. This article uses Moonshine's exploration of the Jacobian conjecture as an example. It shows how the central logic of whether local nondegeneracy can force global injectivity is transferred to one-hidden-layer affine-ridge sigmoid networks. This leads to the formulation of the \emph{Neural Jacobian Conjecture} (NJC): if such a network has strictly positive Jacobian determinant on the whole space, then it must be globally injective. By invoking GPT-5.5-pro and DeepSeek-V4-pro separately, Moonshine obtained independent complete proofs for the case \(N=n+1\). In addition, with the assistance of ChatGPT through interactive use of its web interface with GPT-5.5-pro, a geometric-topological proof was developed. These results provide preliminary evidence for the plausibility of the conjecture. The general higher-width case \(N\ge n+2\), however, remains unresolved and is left for further investigation. This work illustrates Moonshine's ability to autonomously generate meaningful mathematical problems and make rigorous progress on them.

---


### 212. [Deep learning for echo sounder data](https://arxiv.org/abs/2606.10811)

**<font color=#1a73e8>作者：</font>** Ketil Malde  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> There is no doubt that over the last decade, techniques from the field of machine learning have revolutionized how we process and interpret data, especially images and text. For underwater observations acoustics is a primary source of information, and naturally, deep learning methods have been applied to echograms and other acoustics data, but so far with rather modest results. Here, we argue that due to intrinsic properties of acoustic data, substantial advances will likely require research into deep learning methods beyond mere recycling of models and techniques from image processing. Currently, the potential for breakthroughs in method development is hindered by the lack of standard data formats and organization, and even more by the lack of readily available, high quality data sets with established performance goals. To advance the field, these shortcomings should be remedied

---


### 213. [RedAct: Redacting Agent Capability Traces for Procedural Skill Protection](https://arxiv.org/abs/2606.10813)

**<font color=#1a73e8>作者：</font>** Shuwen Xu, Zhitao He, Yi R. 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability. These traces contain rich procedural detail, including tool invocations, intermediate decisions, and error-recovery logic. Yet this detail can expose private procedural skills, allowing downstream methods to recover key formulas, thresholds, and strategies without access to model weights or skill files. To quantify this risk and evaluate protection, we construct \textsc{CapTraceBench}, a benchmark of 75 specialized long-horizon tasks and 154 curated skills across seven domains. We also introduce \textsc{RedAct} this https URL, a protected trace release framework that localizes protected key information, rewrites traces while preserving verifier-critical evidence, and embeds behavioral watermarks for downstream provenance analysis. Across representative trace reuse methods, \textsc{RedAct} reduces normalized skill transfer (NST) from 44.7--67.1\% on raw traces to below the no-skill baseline, while preserving audit evidence. Its standalone behavioral watermarks reach 93.6--100.0\% true detection with a false alarm rate of at most 1.9\%. These results frame public agent traces as security interfaces and show that selective redaction can reduce procedural capability leakage without removing audit evidence.

---


### 214. [Encoding the Euler Characteristic Transform](https://arxiv.org/abs/2606.10824)

**<font color=#1a73e8>作者：</font>** Nello Blaser, Odin Hoff Gardaa, Lars M. Salbu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Euler Characteristic Curve (ECC) records the Euler characteristic of a linearly embedded cell complex as a function of filtration height in a given direction, and the Euler Characteristic Transform (ECT) is the injective shape descriptor obtained by collecting ECCs over many directions. How the ECT is encoded for a neural network is itself an inductive bias, conventionally fixed by discretizing each ECC. We introduce a continuous encoding: for each direction and each vertex it records the net Euler-characteristic change attributed to that vertex, producing a per-direction token sequence that a small transformer maps to a feature vector. We separate the resulting pipeline into two stages on orthogonal axes: an ECC encoder that acts within each direction, mapping its curve to a fixed-length vector, and an ECT representation that acts across directions, aggregating the per-direction vectors into one. We study six ECT representation architectures spanning a range of inductive biases, from a structure-agnostic feedforward baseline to convolutional and complex-valued models that preserve equivariance under planar rotations. Across six classification benchmarks covering point clouds, graphs, cubical complexes, and meshes, the continuous encoding improves accuracy on five of six datasets, and control experiments attribute the gain to the tokenization itself rather than to the added transformer capacity. The representation architecture matters less than the encoding, and the payoff from its inductive biases depends on the encoding: a feedforward network performs best under continuous encoding but is less robust under discretization than convolutional architectures.

---


### 215. [MODIP: Efficient Model-Based Optimization for Diffusion Policies](https://arxiv.org/abs/2606.10825)

**<font color=#1a73e8>作者：</font>** Zakariae El Asri, Philippe Gratias-Quiquandon, Nicolas Thome 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion policies (DPs) have emerged as expressive policy representations for robot learning, often used with imitation learning methods such as behavioral cloning (BC). However, while their success has largely been confined to BC, direct reinforcement learning (RL) fine-tuning remains challenging because actions are generated through a multi-step denoising process. In this work, we propose MODIP, a framework for the offline-to-online fine-tuning of DPs. Rather than directly applying RL to the DPs, MODIP leverages a world model (WM) to guide policy adaptation and keeps the simplicity and stability of BC. We utilize model predictive control (MPC) to generate high-quality trajectories within the WM, and use them as supervised targets for fine-tuning the DP. To make MPC planning efficient, MODIP uses a terminal state value instead of a policy-dependent state-action value, reducing inference time. Additionally, MODIP trains critics with policy-independent TD targets, reducing training time. Experiments on D4RL (MuJoCo, Kitchen) and RoboMimic tasks show that MODIP improves diffusion policies beyond BC, and is competitive with or outperforms diffusion policy RL fine-tuning methods and strong model-based baselines such as TD-MPC2.

---


### 216. [Do VLMs Reason Like Engineers? A Benchmark and a Stage-wise Evaluation](https://arxiv.org/abs/2606.10833)

**<font color=#1a73e8>作者：</font>** Syed Wasiq, Syed Mohamad Tawseeq, Yashwant Pravinrao Bangde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) demonstrate strong performance on general multimodal reasoning benchmarks, yet their ability to perform engineering reasoning remains largely unexplored. Unlike general visual question answering, engineering problem solving requires interpreting technical diagrams, selecting governing physical principles, and maintaining physically consistent multi-step reasoning. These capabilities are increasingly important for AI systems used in engineering education, scientific assistance, and technical decision-making, where reasoning failures may produce physically invalid yet superficially plausible solutions. Existing benchmarks primarily evaluate final answers and provide limited assessment of intermediate reasoning processes. We introduce EngVQA, a multimodal benchmark for evaluating engineering reasoning across 5 engineering subjects containing 696 problems. We introduce an 8-stage automatic evaluation framework for assessing VLM-generated solutions. The framework independently evaluates each stage of the solution, enabling fine-grained analysis of reasoning failures. We benchmark multiple state-of-the-art open and closed source VLMs on our evaluation framework and demonstrate substantial limitations in current engineering reasoning capabilities. Human evaluation shows strong agreement with our automated framework, achieving a Pearson correlation of 0.975 and a mean absolute error of 0.67 on a 10-point grading scale. Our results highlight the importance of process-oriented evaluation for reliable assessment of multimodal engineering reasoning systems.

---


### 217. [HarmoView: Harmonizing Multi-View Constraints for Identity-Consistent Video Generation](https://arxiv.org/abs/2606.10839)

**<font color=#1a73e8>作者：</font>** Cong Wang, Zhentao Yu, Hongmei Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current identity-consistent video generation methods struggle to preserve appearance fidelity under large viewpoint changes. While introducing multi-view reference input offers a natural solution, progress remains constrained by the lack of effective frameworks for multi-view inputs and the scarcity of multi-view data. We address these challenges by proposing HarmoView, a robust framework for identity-consistent video generation that effectively integrates multi-view cues through three architectural refinements complemented by a staged training curriculum. Specifically, we first introduce Multi-level Feature Injection to anchor identity fidelity; by injecting raw ViT features from frontal references alongside text tokens via cross-attention, MFI provides persistent low-level appearance anchors that complement the high-level identity features within DiT blocks, leading to enhanced identity preservation. Then, we employ learnable proxy tokens to unify heterogeneous reference layouts across single-/multi-view settings while simultaneously resolving the reference-view mismatch problem. Jump-RoPE is further developed for identity-wise feature isolation to reduce identity crosstalk. To activate these structural capabilities while preserving the original generative priors, we propose the Progressive View Curriculum. This four-stage training strategy employs view dropout to facilitate a stable transition from vanilla T2V generation to high-fidelity, identity-persistent spatial reasoning. Furthermore, we construct a large-scale multi-view dataset to address the issue of data scarcity. Extensive evaluation on our multi-view benchmark, comprising 100 manually-curated cases spanning 52 unique identities, demonstrates that HarmoView significantly outperforms open-source baselines and matches leading closed-source engines, achieving state-of-the-art performance in identity-consistent video generation.

---


### 218. [ConvMemory v2: A Recall-Preserving Top-10 Evidence Reranker for Conversational Memory Retrieval](https://arxiv.org/abs/2606.10842)

**<font color=#1a73e8>作者：</font>** Taiheng Pan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe ConvMemory v2, an opt-in token-evidence reranker that sits after the lightweight ConvMemory v1 reranker and reorders only v1's protected top-10 candidate set. v2 is a fine-tuned ms-marco-MiniLM-L-6-v2 cross-encoder (22,713,601 parameters, measured from the released checkpoint) applied to the ten (query, memory) pairs that v1 has already selected; it does not change which ten memories are returned, so Recall@10 and Hit@10 are identical to v1 by construction, not by statistical coincidence. On the LoCoMo conversational memory benchmark (5 seeds, n = 4955 test rows), v2 raises FULL MRR from v1's 0.5824 to 0.6560 (paired bootstrap +0.0734, 95% CI [+0.0645, +0.0827]) and H@1 from 0.4440 to 0.5474. v2 closes most but not all of the gap to a much more expensive full-pool cross-encoder reference (mxbai-rerank-large-v1 over the top-500, MRR 0.6688): on FULL MRR v2 sits 0.013 below mxbai_top500, but on two raw-dense-hard slices (where v1's protected top-10 has higher recall than mxbai's own top-10) v2 exceeds mxbai_top500. A four-arm load-bearing ablation shows candidate-specific memory text is the mechanism: removing, shuffling, or replacing it collapses MRR below raw dense retrieval. v2 is best understood as a standard recall-preserving cascade pattern with LoCoMo-specific fine-tuning, an explicit anti-shortcut inference contract, and disciplined load-bearing analysis; its advantage over mxbai is slice-specific rather than a general dominance claim. This report extends the v1 technical report (arXiv:2605.28062).

---


### 219. [LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination](https://arxiv.org/abs/2606.10862)

**<font color=#1a73e8>作者：</font>** Taishan Li, Jiwen Zhang, Siyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VLAs suffer substantial performance degradation under occlusion. To address this issue, we propose \textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an occluded primary observation and conditions action prediction on both observed and imagined evidence. VIM improves robustness across task suites, occlusion types, and severity levels without requiring additional cameras at deployment time, suggesting that viewpoint imagination is an promising mechanism for perception completion in partially observable manipulation. Our benchmark and corresponding code are available at: \href{this https URL}{this https URL}.

---


### 220. [When Do Autoregressive Sequence Models Forecast Physical Wavefields? A Controlled Study on Synthetic Seismograms](https://arxiv.org/abs/2606.10868)

**<font color=#1a73e8>作者：</font>** Waleed Esmail, Stuart Russell, Jana Klinge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon autoregressive forecasting of oscillatory physical signals, such as seismograms, gravitational-wave strain, and similar wavefields is limited by error accumulation: as a causal model is fed its own outputs over hundreds of steps, small per-step errors compound into phase drift that pointwise metrics fail to detect. We ask when such rollout stays stable, using synthetic three-component seismograms as a physically structured testbed and the \textsc{SeismoGPT} autoregressive forecaster as the model under study. Through controlled, intra-architecture ablations evaluated on free-running rollout with paired significance tests, we isolate the contribution of each design choice. Multi-token prediction is the dominant stabilizer, accounting for almost the entire improvement over a single-token baseline ($+0.040$ median NCC); a horizon-embedding hybrid prediction head and a cross-horizon STFT-magnitude coherence loss each add a small but consistent further gain. Performance depends sharply on a context-ratio threshold near one, roughly the full P-S interval of observed signal, below which rollout generalization collapses. The dominant residual failure is a polarity inversion that a magnitude-based spectral loss cannot, by construction, penalize, identifying phase-aware objectives as the natural next step. We frame this as a controlled study of rollout stability on oscillatory wavefields, not a benchmark of forecasting architectures.

---


### 221. [Schmidt Decomposition-Based Methods for Efficient Quantum Image Encoding](https://arxiv.org/abs/2606.10874)

**<font color=#1a73e8>作者：</font>** Ana-Maria Pangeva, Yassine Ferhi, Alexander Geng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In quantum image processing, a fundamental step is encoding classical image data into quantum states. This can be achieved using methods such as Flexible Representation of Quantum Images (FRQI), Quantum Probability Image Encoding (QPIE), and Novel Enhanced Quantum Representation (NEQR). However, on real quantum hardware, these encodings can quickly lead to circuits with many gates, large circuit depth, and high qubit usage, which is a problem for Noisy Intermediate-Scale Quantum (NISQ) devices. In this work, we investigate whether low-rank state approximation, formulated via Schmidt decomposition, can help reduce this complexity. The method keeps only the most significant parts of a quantum state's entanglement structure, making state preparation more efficient while preserving most of the image information. We compare the three encoding techniques in their original form and with low-rank approximation, evaluating metrics such as circuit depth, CNOT count, MSE, and visual quality of reconstructed images. The results reveal meaningful trade-offs between accuracy and resource efficiency, with the FRQI model achieving a 97 percent reduction in circuit depth while maintaining a near-perfect reconstruction (MSE of about 0.27). This demonstrates the potential of low-rank techniques for advancing practical quantum image processing on near-term hardware.

---


### 222. [Advancing Wood Identification in the Philippines: Utilizing the Xylorix Platform for Efficient AI Model Development and Deployment for Five Key Species](https://arxiv.org/abs/2606.10876)

**<font color=#1a73e8>作者：</font>** Rosalie C. Mendoza, Vivian C. Daracan, Arlene D. Romano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illegal logging and timber trade continue to pose significant challenges in the Philippines, where accurate wood species identification is essential for enforcement but limited by the need for specialised equipment and expertise. This study aims to evaluate whether AI models for macroscopic wood identification can be developed and deployed by wood scientists without programming expertise using the Xylorix platform, focusing on five Philippine hardwood species: Mangium (Acacia mangium Willd.), Rain Tree [Samanea saman (Jacq.) Merr.], Banuyo (Wallaceodendron celebicum Koord.), Tindalo [Afzelia rhomboidea (Blanco) Vidal], and Ipil [Intsia bijuga (Colebr.) O. Kuntze]. Binary classifiers were trained on 10,663 verified cross-section images from 260 specimens and evaluated using specimen-level mean scoring to mirror operational field conditions. Area Under the ROC Curve (AUC) values ranged from 0.969 (Ipil) to 1.000 (Mangium), and Average Precision (AP) values ranged from 0.589 (Samanea) to 1.000 (Mangium). Four of five species achieved AA grade (AUC and AP both \geq 0.90); Rain Tree received AE (AUC \geq 0.90, AP < 0.60) due to AP compression from its small positive test set (3 specimens). All five classifiers rank their target specimens above non-target specimens with near-perfect fidelity. Specimen-level error analysis revealed 9 false negatives from Ipil, primarily stemming from localized image artifacts and 3 false positives for Rain Tree and 1 false positive for Tindalo caused by shared tribal-level anatomical traits. These findings demonstrate that Xylorix non-programmers can leverage the Xylorix platform to construct operationally reliable wood identification models suitable for field deployment at supply chain checkpoints.

---


### 223. [XtrAIn: Training-Guided Occlusion for Feature Attribution](https://arxiv.org/abs/2606.10877)

**<font color=#1a73e8>作者：</font>** Thodoris Lymperopoulos, Ioannis Kakogeorgiou, Denia Kanellopoulou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Occlusion-based attribution methods provide an intuitive way to estimate feature importance by perturbing input features and measuring the resulting change in model output. However, their reliability is strongly affected by how feature removal is implemented: externally selected baselines can introduce bias, out-of-distribution samples, and unstable explanations, while in nonlinear models the occlusion of a set of features can also alter the contribution of non-occluded features. We refer to this effect as attribution shift, as the attribution scores of the non-occluded features drift from their initial values. To challenge these major issues that render explanations unstable, we introduce XtrAIn, a training-guided attribution method that transfers the occlusion operation from the input space to the parameter space. Instead of replacing input values with hand-crafted baselines, XtrAIn follows the model's training trajectory and measures how feature-associated parameter updates affect the output logits. We further introduce Xstep, a lightweight approximation for reducing computational cost, and XtrAIn+, a target-focused variant that emphasizes updates aligned with the target class. Experiments on controlled image datasets and PAM50 breast-cancer subtype classification show that the proposed methods produce cleaner and more interpretable attribution patterns than standard attribution baselines. Overall, XtrAIn provides a training-aware perspective on feature attribution and offers a useful diagnostic tool for studying how feature-level evidence is formed during training.

---


### 224. [Large-scale semantic mapping of learner agency and autonomy reveals what measurement and generative AI research overlook](https://arxiv.org/abs/2606.10881)

**<font color=#1a73e8>作者：</font>** Fei Qin, Xiaobo Liu, Yaowen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learner agency and autonomy are foundational to personal development, yet a pervasive "jingle-jangle" fallacy (i.e. identical terms denoting different constructs, distinct terms denoting identical ones) has substantially hindered cumulative knowledge. Treating meaning as a phenomenon constituted through use in linguistic practice, we extracted 8,954 definitions and 2,700 scale items from over 14,000 publications, to investigate how researchers actually used learner agency and autonomy with a semantic analysis pipeline. The definitional landscape of two constructs resolves into three dimensions: regulation and control of learning (task), intrinsic motivation and internal decision-making (person), and social-relational action (sociocultural), thereby empirically quantifying the jingle-jangle fallacy. Existing scales, however, systematically underrepresent the sociocultural dimension. Critically, current generative AI research in education concentrates on learning regulation and control, narrowing the behavioral repertoire that AI-mediated learning environments are designed to cultivate. Beyond conceptual clarification, this work carries direct implications for conceptualization, measurement, and practice towards supporting the multidimensional learner agency and autonomy.

---


### 225. [Listen, Look, and Learn: Learning Without Forgetting through SAM-Audio](https://arxiv.org/abs/2606.10887)

**<font color=#1a73e8>作者：</font>** Avi Gupta, Nilotpal Sinha, Vishnu Raj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) aims to continuously learn new classes without forgetting previously acquired knowledge. While recent CIL advances have spurred significant interest across various modalities, the audio-visual setting remains underexplored. Furthermore, although foundational multimodal models like SAM-Audio encapsulate rich static priors, our empirical analysis reveals that these representations struggle in incremental settings. This work bridges this gap by integrating SAM-Audio's audio-visual priors into the CIL setting. Specifically, we leverage its dense audio and visual representations and employ a novel guided attention strategy where the audio features contextually guide the visual representations. To further mitigate catastrophic forgetting, we introduce dual-level distillation objectives at both the feature and logit levels. Extensive evaluations on audio-visual CIL benchmarks demonstrate that our approach consistently outperforms state-of-the-art methods.

---


### 226. [The 1st PortraitCraft Challenge: A CVPR 2026 Workshop Competition on Portrait Composition Understanding and Generation](https://arxiv.org/abs/2606.10894)

**<font color=#1a73e8>作者：</font>** Zijie Lou, Youyun Tang, Xiaochao Qu 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the inaugural PortraitCraft Challenge, held as one of the official competitions at CVPR 2026. The challenge focuses on portrait composition understanding and generation, aiming to advance AI research in portrait aesthetics analysis and controllable image synthesis. Unlike existing datasets and tasks that primarily focus on global aesthetic scoring, PortraitCraft introduces a unified evaluation framework comprising two complementary tracks. Track 1 requires models to perform structured portrait composition understanding, and Track 2 requires models to generate portrait images from structured composition descriptions under explicit compositional constraints. To support the challenge, we constructed and publicly released a large-scale portrait composition dataset consisting of approximately 50,000 curated real portrait images, providing multi-level supervision. This report describes the challenge setup, evaluation protocols, dataset composition, and final results, along with an analysis of the technical characteristics of the submitted solutions. The PortraitCraft Challenge provides a standardized and reproducible platform for research on portrait composition understanding and generation, and is expected to foster further progress in the fields of portrait aesthetics and controllable image generation.

---


### 227. [Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering](https://arxiv.org/abs/2606.10896)

**<font color=#1a73e8>作者：</font>** Gal Bloch, Ariel Gera, Matan Orbach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present \textbf{Flash-GMM}, a fused Triton kernel for efficient computation of Gaussian Mixture Models (GMMs) over large-scale data in a single GPU pass. By eliminating the need to materialize the full responsibility matrix in GPU memory, Flash-GMM achieves a \textbf{20$\times$} speedup over existing implementations and enables training on datasets more than \textbf{100$\times$} larger than previously feasible on one device. To demonstrate its impact, we integrate Flash-GMM into the IVF coarse quantizer for approximate nearest-neighbor (ANN) search. We show that soft GMM clustering is now a viable drop-in replacement for $k$-means, and that GMM responsibilities can be leveraged to assign border vectors to multiple clusters. Our approach reaches fixed recall targets with up to $1.7\times$ fewer distance computations, or equivalently, yields $+2$--$12$ recall@10 at matched computational cost. We release the kernel as an open-source project.

---


### 228. [Conservation Laws from Data Symmetry in Neural Networks](https://arxiv.org/abs/2606.10913)

**<font color=#1a73e8>作者：</font>** Jakob Galley, Vahid Shahverdi, Axel Flinth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We explore whether intrinsic symmetries of the training data lead to conserved quantities during gradient-flow training of neural networks. Under the assumption that the loss function is analytic and non-polynomial, we prove that data symmetries generically do not induce any additional integrals of motion. For mean squared error (MSE) loss, on the other hand, there are situations in which data augmentation yields extra conserved quantities. We build a framework, utilizing \emph{tensorizable networks} to describe this phenomenon. Tensorizable networks are a family of architectures whose dependence on parameters and inputs can be separated using an intermediate representation. They include linear and polynomial networks, as well as Lightning Attention.

---


### 229. [Recoverable but Not Stationary:Local Linear Structures in Weights and Activations](https://arxiv.org/abs/2606.10929)

**<font color=#1a73e8>作者：</font>** Irina Piontkovskaia, Sergey Nikolenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task vectors, LoRA, activation steering, and random search around pretrained weights all suggest that learned behaviour can be controlled by linear directions. We ask which linear structures actually exist and on what scale. In a synthetic multitask transformer and LoRA adapters on DistilGPT-2 / GPT-2 we find strong local low-rank task-gradient structure but reject the fixed-task-plane hypothesis: static bases miss the recovery direction, and the useful basis drifts substantially within 100 steps. However, the first recovery updates form a trajectory-prefix basis capturing 77% of the LoRA recovery displacement. We develop random search theory with a Gaussian local-linear theorem that justifies the effectiveness of random parameter search even in very high dimensions. We also study the relation between parameter perturbations and activation steering: a single gradient step produces an activation shift with 0.58 cosine to a labelled-contrast CAA steering vector, with a similar steering effect on Qwen-0.5B BoolQ statements. We validate our results with experiments on synthetic Transformers and LLMs. Our results suggest that linear structures in trained networks are not global task directions, but evolving local geometries that partially persist across parameter and activation spaces.

---


### 230. [Density Field State Space Models: 1-Bit Distillation, Efficient Inference, and Knowledge Organization in Mamba-2](https://arxiv.org/abs/2606.10932)

**<font color=#1a73e8>作者：</font>** Chirag Shinde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Density Field State Space Models (DF-SSM), a framework for compressing SSMs to a 1-bit scaffold with int8 low-rank correction. Applied to Mamba-2 1.3B, we achieve a 278 MB model (9.7x smaller than the 2.7 GB FP16 teacher) that runs at 21.4x faster inference on GPU (batch=1, relative to the mamba-ssm reference implementation) while maintaining downstream task performance within 2-4 percentage points of BitMamba-2, a 1.58-bit model trained from scratch on 150B tokens. The distillation itself requires only 32M tokens and 6 hours on a single A100 GPU, though it presupposes a pretrained FP16 teacher. We develop an optimized inference pipeline combining cuBLAS INT8 tensor cores for the scaffold matmul, custom CUDA kernels for stateful SSM and convolution operations, and an AVX-512 CPU backend for efficient deployment on both GPU and CPU. Beyond compression, we investigate the internal knowledge organization of the resulting model, discovering three distinct processing phases: intent classification (layers 0-3, operating in an abstract space with no vocabulary alignment), knowledge retrieval (layers 25-35, where factual associations localize to a 5-layer window), and output formatting (layers 36-47, where category structure dissolves). Through systematic analysis of 445 factual prompts across 19 categories, we find that early-layer classification is syntactic (driven by template structure) rather than semantic, and that the model exhibits well-organized knowledge representations despite weak factual recall--suggesting that representational structure may precede factual strength.

---


### 231. [CLP: Collocation-Length Prediction for Zero-Loss Adaptive Multi-Token Inference](https://arxiv.org/abs/2606.10935)

**<font color=#1a73e8>作者：</font>** Xuezhen Xie, Zhiqiang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model inference is bottlenecked by autoregressive decoding, where each token requires a full forward pass. Multi-token prediction (MTP) offers a promising acceleration path, but existing approaches suffer from a fundamental architectural flaw: the MTP head for the first token competes with the backbone's own language model (LM) head, leading to severe quality degradation when predictions are accepted. We identify this head-backbone competition as the root cause of repetitive and incoherent outputs in prior MTP-based acceleration methods. To address this, we propose Backbone-as-Architect, a design principle where the backbone LM head always generates the first token, and MTP heads are responsible only for subsequent tokens. Building on this principle, we introduce CLP (Collocation-Length Predictor), a lightweight span-level decision layer that predicts how many additional tokens can be safely accepted at each decoding step. CLP uses only a single linear layer (4.6K--7.7K parameters), replacing the over-engineered 1M-parameter gate networks used in prior work. Experiments on Qwen2.5 models (0.5B, 1.5B, 7B) show that CLP achieves 1.20x--1.29x speedup on 1.5B and 1.14x--1.20x on 7B, with zero quality degradation (repetition ratio < 0.02), while gate-based approaches fail to accelerate (1.07x) or produce severely degraded outputs (repetition ratio > 0.5%). We further demonstrate that shorter prediction horizons (k=2) recover 24% higher MTP head accuracy on large models, establishing a scaling-aware design principle. We identify MTP head prediction accuracy as the binding constraint on acceleration and establish a clear roadmap for future improvements.

---


### 232. [A Systematic Approach for Selecting Trajectories for Data Augmentation](https://arxiv.org/abs/2606.10938)

**<font color=#1a73e8>作者：</font>** Adam Nordling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory data augmentation is a promising approach to mitigate data scarcity in machine learning applications, but its utility has been limited by the complexity of preserving spatio-temporal coherence. Although prior work demonstrated the viability of geometric perturbation, it relied on naive random selection, leaving a critical gap in understanding which trajectories should be augmented for maximal benefit. This thesis addresses this gap by developing a systematic and scalable framework to evaluate five systematic selection strategies: Outlierness, Diversity, Representativeness, Uncertainty, and Random selection. These strategies were rigorously tested across four datasets covering animal behavior (Foxes and Starkey), maritime traffic (AIS), and urban traffic (Car) using a suite of linear and non-linear machine learning models. As part of this evaluation, an Optuna-based hyperparameter optimization loop was integrated to empirically identify the best-performing augmentation parameters for each dataset within the explored search space. The results indicate that, while systematic selection is not a universal solution, it offers distinct advantages over the random baseline. Systematic strategies, particularly Outlierness and Uncertainty, demonstrated higher stability and were less prone to performance degradation observed with random sampling in dense datasets. However, the findings also reveal that the value of augmentation is strictly conditional. Visual analysis via UMAP demonstrates that while systematic augmentation successfully repairs topological fragmentation in sparse datasets, it can act as a corrupting noise signal in high-quality, dense datasets. Furthermore, the study identified physical limitations in high-velocity domains, where standard perturbation techniques lead to divergence in feature space...

---


### 233. [PENet+: A Lightweight Residual Transformer Framework for Efficient Image Steganalysis](https://arxiv.org/abs/2606.10939)

**<font color=#1a73e8>作者：</font>** Jincheol AN, Dongsu Kim, Haneol Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image steganalysis, the detection of hidden information embedded in digital images, is a core component of modern cybersecurity and digital forensics. Recent residual Transformer architectures, such as the Pixel-Difference-Convolution and Enhanced-Transformer-Network (PENet) [1], achieve strong detection accuracy, but their computational and memory demands hinder deployment in resource-constrained settings. We present PENet+, a lightweight steganalysis framework that preserves PENet's discriminative structure while substantially improving efficiency. Rather than redesigning or compressing the attention blocks, we retain PENet's self-attention topology for reproducibility and add a classifier-streamlining stage that progressively narrows the SPP-to-FC1 input channels (SPP: spatial pyramid pooling; FC1: first fully connected layer), yielding large reductions in parameters and FLOPs with negligible accuracy loss. We further refine the high-pass-filter (HPF) stem with an activation-aware mechanism that aggregates HPF responses early and selects a balanced SRM-Gabor top-K subset, and we replace PENet's backbone with a MobileNetV2-style inverted residual network. A balanced configuration with K=31 filters (16 Gabor + 15 SRM) matches or surpasses heavier settings at lower compute. Finally, we motivate PReLU from a steganalysis standpoint, arguing that preserving negative responses helps capture weak stego cues that ReLU suppresses. On a disjoint ALASKA2 JPEG QF90 protocol at 512x512 resolution (5,000 cover images for training, validation, and internal testing; a separate 19,000-cover evaluation set), PENet+ achieves up to 45.5% fewer parameters and about 97% fewer FLOPs than the re-evaluated PENet baseline, offering a computationally efficient direction for resource-constrained steganalysis. Device-level latency and power measurements remain future work.

---


### 234. [Democratising Camera Trap AI: An Open-Source Model for Detecting UK Mammals](https://arxiv.org/abs/2606.10940)

**<font color=#1a73e8>作者：</font>** Paul Fergus, Philip Stephens, Russell A. Hill 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera traps have become a cornerstone of biodiversity monitoring, but the artificial intelligence that turns vast quantities of images into usable ecological data is often locked behind commercial platforms or trained on fauna that does not match that of the British Isles. In an attempt to remove barriers and increase uptake, we release an open-source object detection model for 31 classes, 28 common UK mammal and bird species, plus utility classes for humans, calibration poles, and vehicles, drawn from a curated dataset of 48,165 labelled instances assembled from multiple sites over a decade of operational deployment through Conservation AI and its successor, Trap Tracker. The model, a YOLO26x detector trained and tested on an 80/10/10 class-stratified split, achieves a mean Average Precision of 0.984 at Intersection over Union (IoU) of 0.5 (0.956 at IoU 0.5-0.95) on the held-out validation set, with precision 0.988 and recall 0.965. On an unseen held-out test split, mean per-species confidence ranged from 0.96 to 0.99 across the 31 classes, with a 0.17% false-negative rate concentrated in difficult night-time, distant, or occluded images. These metrics are from data from the same pool of sites and cameras as training, so performance at entirely new sites is left to future work. We release the trained weights in ONNX format under a non-commercial licence, with local desktop and real-time camera support, aimed explicitly at ecologists with no machine-learning experience. This release is a deliberate counterweight to the multiple paid for models that have developed over the last decade.

---


### 235. [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949)

**<font color=#1a73e8>作者：</font>** Shelly Bensal, Axel Magnuson, Aparna Balagopalan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time. We show they also make models less correct by systematically amplifying sycophancy, wherein models prioritize agreement with users over accuracy. We conduct the first systematic evaluation of this effect, introducing MIST: a benchmark of synthetically generated multi-turn conversations where users express plausible misconceptions in scientific, medical, and moral reasoning domains. Testing across three state-of-the-art memory systems and five model families reveals that memory amplifies sycophantic behavior across all conditions, with up to 25x higher sycophancy rates than in-context baselines. Error analyses suggest memory extraction as the primary culprit: lossy compression into discrete snippets encodes user misconceptions while discarding corrective context. Based on these results, we propose two lightweight mitigations that substantially reduce sycophancy while matching or exceeding memory systems at factual recall.

---


### 236. [Population-Aware Physics-Informed Neural Particle Flow for Bayesian Update](https://arxiv.org/abs/2606.10959)

**<font color=#1a73e8>作者：</font>** Batu Candan, Simone Servadio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural particle flow (PINPF) learns a deterministic transport field that moves particles from a prior distribution toward a Bayesian posterior while enforcing the governing probability-evolution equation. However, the standard PINPF velocity model processes particles independently and therefore does not explicitly condition its transport decisions on the empirical particle population. This paper introduces population-aware PINPF (PA-PINPF), which augments each particle update with a permutation-invariant Deep Sets representation of the full particle set. We investigate two population encoders. PA-PINPF-State summarizes the particle states, whereas PA-PINPF-Feature summarizes the complete local physics-informed feature vectors, including particle position, pseudo-time, measurement information, likelihood values, and score information. The latter allows the population context to represent not only particle-cloud geometry, but also the population-level Bayesian transport geometry. The methods retain the original unsupervised physics-informed residual objective and require no ground-truth posterior samples during training. Experiments on range-measurement tasks and nonlinear time-difference-of-arrival posterior transport demonstrate that both population-aware variants improve over particle-wise PINPF, while feature-population encoding provides the strongest performance. These results show that population-level physics features provide useful global information for learned Bayesian particle transport.

---


### 237. [Learning Doubly Sparse Explicitly Conditioned Transforms](https://arxiv.org/abs/2606.10975)

**<font color=#1a73e8>作者：</font>** Tudor Pistol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding convenient spaces in which certain hypotheses regarding an assumed sparse structure of natural signals hold true has become a desirable result in recent research, its implications being reflected in areas such as data compression, noise reduction and feature extraction. While the extensively used analytical transforms, such as DFT or DCT, already provide efficient algorithms and robust sparse representations, they assume a fixed prior about the data, failing to accurately capture the specific structure of more restrictive classes of signals. To address this, the concept of a data-adaptive, learnt transform has been introduced in the literature, allowing for the reduction of a residual term in the transform domain. More recent studies have shown that the condition number serves as a good metric in this context, where the desired outcome alternates between a generalizing tendency and one that achieves minimal approximation error. Motivated by these considerations, we introduce the learning of a structured, explicitly conditioned transform formulated as the product of a fixed canonical matrix and a refining data-adaptive sparse component. This approach seeks to preserve the advantages of fast and stable analytical transforms, while introducing controllable adaptivity to the data. No references that concern this specific formulation have been identified so far, indicating its novelty. The proposed algorithm is motivated within the framework of inexact proximal methods, leveraging a newly derived closed-form projection operator. Empirical observations demonstrate state-of-the-art results on the doubly sparse transform learning problem and comparable performance with its dense variant at significantly lower computational costs and sometimes faster convergence and better avoidance of bad local minima.

---


### 238. [AnimaSpark: A Feed-Forward Method for Animating Arbitrary 3D Objects](https://arxiv.org/abs/2606.10988)

**<font color=#1a73e8>作者：</font>** Yiming Zhao, Haoyu Sun, Aoyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advancements in generative AI have substantially accelerated static 3D model creation workflows, the synthesis of category-agnostic 3D animations remains a significant bottleneck in 3D asset production. Current methods for category-agnostic animation generation exhibit critical limitations in inference speed, motion quality, and adherence to textual prompts, thereby leaving the process dependent on labor-intensive manual artistry. To address these challenges, this paper introduces AnimaSpark, a novel pipeline for category-agnostic 3D animation generation. Our approach is motivated by the key insight that for many fundamental motions in the 3D world, the corresponding joint transformations can often be effectively modeled within a two-dimensional subspace. The pipeline begins by rendering a rigged static 3D model into multi-layered image representations of its mesh and skeleton, which are subsequently fed into a video generation model. We then employ a keypoint tracking algorithm on the generated video to capture the motion of the skeletal joints projected onto the camera's viewing plane. In the final stage, we distill the planar translations and rotations from these tracked keypoints and lift them from the 2D domain into 3D space to animate the character. Comprehensive evaluations reveal that our method achieves superior performance over existing state-of-the-art techniques across key metrics, including text-motion alignment, quality of motion, and computational efficiency.

---


### 239. [IPSM-Bench: A New Intermediate Phase Segmentation Benchmark in Microstructure Images of Zinc-Based Absorbable Biomaterials](https://arxiv.org/abs/2606.11001)

**<font color=#1a73e8>作者：</font>** Jinglin Xu, Shangyan Zhao, Jiabo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zinc-based alloys are indispensable emerging absorbable metallic biomaterials, and their macroscopic performance is governed by microstructural characteristics. Intermediate phases-key microstructural constituents-are pivotal in regulating mechanical and functional properties. However, intermediate phase segmentation in zinc alloy microstructures faces formidable challenges: scarce annotated datasets, low contrast, difficulty detecting small targets, and heterogeneous morphologies. To this end, we construct IPSM-Bench, the largest high-quality dataset for zinc-alloy intermediate phase segmentation. Furthermore, we propose SCoP-SAM, a new Spatial Context Prior-guided SAM method that leverages the gradient structure and grayscale properties of intermediate phases to capture spatial context priors and incorporates them into the entire SAM encoding-decoding process, improving segmentation performance. Based on the proposed IPSM-Bench, we establish a new benchmark for intermediate phase segmentation to systematically evaluate state-of-the-art (SOTA) methods and advance research on zinc alloy microstructure analysis. Extensive experiments on IPSM-Bench and additional public alloy benchmarks demonstrate that our SCoP-SAM not only achieves SOTA performance for zinc-alloy intermediate phase segmentation but also generalizes remarkably well to other alloy scenarios.

---


### 240. [A Case Study Reexamining the Cold-Start Problem in Knowledge Tracing Models and Implications for SafeInsights, an Education Research Infrastructure](https://arxiv.org/abs/2606.11004)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Ryan S. Baker, Debshila Basu Mallick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) models are widely used to predict students' evolving knowledge states from their learning history. However, many KT models are evaluated using specific datasets, platforms, and learning contexts, raising questions about whether reported model performance replicates and generalizes across newer datasets that vary in context. This paper replicates and extends Zhang et al. (2021), which examined the cold-start problem in KT models and found that deep-learning-based KT models performed better, partly because of stronger predictions when students began practicing a skill. Using a more recent ASSISTments dataset, FoundationalASSIST, we replicate the previous analysis by evaluating model performance across opportunities to practice and extend the analysis by examining performance across problem types, including fill-in-the-blank, multiple-choice select-one, multiple-choice select-all, and order/sort problems. Results show that KT model performance varies across both student practice trajectories and problem types. Beyond the empirical replication, this study identifies practical challenges in reproducing educational data mining studies and serves as a proof of concept, showing how privacy-preserving research infrastructures such as SafeInsights can be leveraged to facilitate educational research and support replication analyses.

---


### 241. [Understanding and mitigating the risks of OpenClaw for non-technical users: A practical guide with Skill](https://arxiv.org/abs/2606.11007)

**<font color=#1a73e8>作者：</font>** Junchang Zheng, Junfeng Tan, Jialiang Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> OpenClaw has rapidly emerged as a transformative artificial intelligence (AI) agent framework, and its ability to autonomously execute complex, multi-step tasks has attracted an ever-growing and diverse user base. However, this capability comes with significant risks. While existing research has made important strides in characterizing these threats, such work is predominantly directed at technically sophisticated audiences. It remains largely inaccessible to non-technical users. This demographic now makes up an increasingly large and underserved portion of the community, yet it is these very users who most urgently need practical and straightforward guidance. In response, we bridge this gap through a series of interconnected efforts designed to lower the risk barrier for non-technical OpenClaw users. First, we identify and categorize seven core risks that OpenClaw users may encounter in daily usage, explaining each in plain language so that non-technical users can readily grasp the nature and potential consequences of these threats. Second, for each identified risk, we distill a set of corresponding defensive strategies into clear and actionable operational steps that are easy to follow. Third, to make protection even easier, we provide a companion OpenClaw Skill that automates key security configurations, enabling users to safeguard their systems with minimal manual intervention. Through this work, we demonstrate that safeguarding against the risks of intelligent agents need not be the exclusive domain of security experts, and that non-technical users can meaningfully participate in reducing these risks through simple, practical actions.

---


### 242. [An Uncertainty Estimation Framework for Dose Accumulation in Adaptive Radiotherapy: Application to CBCT-Guided Radiotherapy for Cervical Cancer](https://arxiv.org/abs/2606.11012)

**<font color=#1a73e8>作者：</font>** Cedric Hemon, Delphine Lebret, Jean-Claude Nunes 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and purpose: oART enables daily plan adaptation to interfraction anatomical variations, but cumulative dose estimation remains limited by DIR, segmentation, and anatomical uncertainties. We introduce IMPACT-DoseAcc, an uncertainty-aware dose accumulation framework, within IMPACT for semantic feature-driven image analysis. The framework is modality- and disease-agnostic and is applied to CBCT-guided oART for cervical cancer (LACC).
Material and Methods: Nine LACC patients were retrospectively analyzed using daily CBCT-derived virtual CTs for dose recalculation. IMPACT-DoseAcc focuses on uncertainty from DIR, without modeling vCT-generation uncertainty. Two DIR uncertainty strategies were tested within IMPACT-Reg: a Bayesian segmentation-guided approach using one probabilistic model to quantify anatomical uncertainty, and an ensemble of segmentation models targeting structures to capture epistemic variability. Voxel-wise uncertainty maps were propagated through dose warping and accumulation to generate probabilistic dose-volume histograms. Ensemble uncertainty was quantified from voxel-wise standard deviation across deformation fields, and geometric error was assessed using surface distance between warped and validated contours. Anatomical-variability weighting refined aggregation.
Results: Ensemble DIR uncertainty correlated with geometric error, with Pearson coefficients of 0.63 for CTVt and 0.66 for bladder. For CTVt, pDVHs achieved 96.3 +/- 3.9% coverage, showing calibration of propagated uncertainty. Weighting stabilized estimates across fractions and organs.
Conclusions: IMPACT-DoseAcc propagates registration-driven uncertainty to cumulative dose metrics, improving interpretation of accumulated dose under anatomical variations. Its 3DSlicer integration supports reproducible, uncertainty-informed ART workflows.

---


### 243. [Data-Driven Runway and Taxiway Exits Prediction of Landing Aircraft: A Case Study at Hartsfield-Jackson Atlanta International Airport](https://arxiv.org/abs/2606.11017)

**<font color=#1a73e8>作者：</font>** Alex Porcayo, Yutian Pang, Maria Thomas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Airport surface operations increasingly constrain performance at high-throughput hubs. This study examines arrival taxi-in decisions at Hartsfield-Jackson Atlanta International Airport (KATL) and proposes a two-stage, data-driven decision aid that mirrors controller workflow. Stage I predicts the runway exit selected by an arriving aircraft. Stage II predicts whether, given that exit, the aircraft will cross the active departure runway at a designated point or use the end-around taxiway. Models are trained using ASDE-X surface trajectories, aircraft characteristics, ramp destinations, short-horizon traffic rates, and weather across multiple look-back windows. We benchmark nine classifiers, including Random Forest, XGBoost, LightGBM, and CatBoost, and evaluate accuracy, macro-F1, precision-recall behavior, confusion matrices, Brier score, and Expected Calibration Error. Across east and west flows, XGBoost and LightGBM outperform Random Forest. Stage I achieves 0.86-0.89 accuracy with macro-F1 scores of 0.40-0.50, while Stage II achieves 0.70-0.74 accuracy with macro-F1 scores of 0.28-0.55. Feature-importance analysis shows that approach speed is the main driver of exit choice. Departure rate, crossing rate, ramp destination, and, for west flow, the selected exit are the strongest predictors of crossing versus end-around routing. Minority classes remain harder to predict because of feature-space overlap, as shown by t-SNE and UMAP analyses. The proposed framework supports controller situational awareness through calibrated, explainable predictions while preserving human responsibility for final routing decisions.

---


### 244. [When Discovery Outpaces Remediation: Modeling AI-Accelerated Vulnerability Discovery in Interconnected Systems](https://arxiv.org/abs/2606.11022)

**<font color=#1a73e8>作者：</font>** Mohamamad Reza Faghani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced AI systems for code analysis, binary analysis, fuzzing orchestration, and penetration-test planningmay significantly increase the rate at which latent vulnerabilities are discovered. While improved discovery can benefit defenders, it can also overload remediation pipelines and accelerate adversarial weaponization. This paper develops a queueing and network-theoretic model of AI-accelerated vulnerability discovery in interconnected systems. We represent an enterprise as a weighted dependency graph with replenishing vulnerability pools, finite remediation capacity, triage degradation, exploit window compression, and dynamic compromise propagation. We derive stability conditions for vulnerability backlogs, formulate a dynamic coupling between unresolved backlog and cascade risk, and evaluate mitigation strategies through simulation. Results indicate that when actionable discovery arrivals exceed remediation throughput, backlogs grow rapidly and systemic risk increases nonlinearly. In hub-dominated topologies, segmentation can reduce propagated compromise more effectively than remediation speed alone, while the strongest defense combines remediation automation with reduced network coupling.

---


### 245. [Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models](https://arxiv.org/abs/2606.11025)

**<font color=#1a73e8>作者：</font>** Bowen Ping, Xiangxin Zhou, Penghui Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has demonstrated that online reinforcement learning (RL) can substantially improve the quality and alignment of flow matching models for image and video generation. Methods such as Flow-GRPO and CPS cast the denoising process as a Markov Decision Process and apply PPO-style ratio clipping to enforce a trust region. However, we argue that ratio clipping is structurally ill-suited for flow models: the probability ratio between new and old policies is a noisy, single-sample estimate of the true policy divergence, leading to over-constraining in some regions of the trajectory and under-constraining in others. We propose Flow-DPPO (Flow Divergence Proximal Policy Optimization), which replaces ratio clipping with a divergence proximal constraint. A key observation is that the per-step policy in flow models is Gaussian, enabling exact and cheap computation of the KL divergence between old and new policies. Flow-DPPO employs an asymmetric divergence mask that blocks gradient updates only when they simultaneously move away from the trusted region and violate the divergence threshold. Experiments show that Flow-DPPO achieves higher rewards with better KL-proximal efficiency, alleviates catastrophic forgetting, promotes balanced multi-objective optimization, and enables stable multi-epoch training where ratio clipping degrades. Code and models are available at this https URL.

---


### 246. [U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training](https://arxiv.org/abs/2606.11032)

**<font color=#1a73e8>作者：</font>** Zhiwen Yang, Jiayin Li, Hao Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning models for Positron Emission Tomography (PET) image denoising often suffer from severe performance degradation under distribution shifts, fundamentally restricting their robust clinical deployment. This lack of generalization stems from the conventional paradigm of fixed-parameter models that cannot adapt to variations in test data (e.g., dose levels or scanner types) after training. To overcome this limitation and achieve robust generalization, we introduce U-TTT, a novel U-shaped model that integrates Test-Time Training (TTT) layers to dynamically adjust model parameters during inference through self-supervision, thereby adapting to the specific characteristics of each test instance. Furthermore, to comprehensively capture the complex degradations of 3D PET data, U-TTT features a dual-domain adaptation mechanism comprising a Spatial Test-Time Training (S-TTT) layer and a Frequency Test-Time Training (F-TTT) layer. The S-TTT layer captures and corrects spatial structural degradations, while the F-TTT layer suppresses global noise spectra and restores delicate high-frequency details. Extensive experiments demonstrate that U-TTT achieves state-of-the-art PET denoising performance and exhibits superior generalization under challenging distribution shifts, including both unseen dose levels and unseen scanners. Our code will be available at this https URL.

---


### 247. [What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents](https://arxiv.org/abs/2606.11045)

**<font color=#1a73e8>作者：</font>** Martin Andres Bertran, Aaron Roth, Zhiwei Steven Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusing a held-out benchmark adaptively should, in principle, invite overfitting. Yet benchmark-driven machine learning (ML) has produced surprisingly little overfitting in practice. An attractive hypothesis is that successful ML strategies are highly compressible. We study this in the setting of LLM-driven research agents, where the hypothesis becomes directly testable via two complementary information bottlenecks. In \emph{output compression}, an exploration agent adaptively searches for high-performance models using a validation set, and we test whether a fresh ``reproducer agent'' can reproduce its performance given only an extremely short prompt and the training data. In \emph{input compression}, the explorer receives only one-bit feedback indicating whether each submitted model improves on the running best. Across 8 datasets spanning tabular classification, vision, language modeling, diffusion modeling, and reward modeling, we find that these bottlenecks have little effect on performance: short prompts and compressible feedback are sufficient to reproduce and find high-performance models. The hypothesis is falsifiable: when we deliberately induce validation-set overfitting, the results fail to reproduce with short prompts. Taken together, our results support a description-length explanation for the lack of overfitting in benchmark-driven ML: successful strategies occupy a low-complexity region of strategy space.

---


### 248. [Flexible Kernels for Protein Property Prediction](https://arxiv.org/abs/2606.11057)

**<font color=#1a73e8>作者：</font>** Martin Jankowiak, Yerdos Ordabayev, Rudraksh Tuwani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite its importance to applications in protein design, predicting protein properties like binding affinity and thermostability from sparse experimental data remains a significant challenge. Accordingly, we introduce a class of sequence kernels that exploit evolutionary substitution matrices as well as local linearity and demonstrate that the resulting Gaussian processes provide data-efficient models of protein property landscapes, frequently outperforming alternatives that rely on foundation model embeddings. Furthermore--by learning what are in effect structure-aware substitution matrices--we show that our kernels can readily incorporate structural information from foundation models. We demonstrate that these structure-conditioned kernels are well suited to multi-task learning across multiple protein property landscapes and can decisively outperform local supervised learning methods.

---


### 249. [GRAFT: Gain-Recalibrated Adapters for Transformer-Based Neural Population Activity Modeling](https://arxiv.org/abs/2606.11066)

**<font color=#1a73e8>作者：</font>** Xiangsheng Ge, Yang Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural population activity models can recover rich temporal structure from binned spikes, but their read-in and readout layers often remain tied to a fixed set of recorded neurons. This coupling limits reuse in long-term brain-computer interfaces, where recorded neuron identities, counts, and response statistics can change across days. We introduce GRAFT, a Transformer-based neural population activity model that separates reusable temporal dynamics from a recalibratable neuron interface. The neuron interface controls how recorded neurons enter and leave the shared backbone, and auxiliary gain and positional mechanisms support neural activity modeling inside the Transformer. On MC Maze under the standard NLB'21 protocol, GRAFT reaches 0.3866 co-bps as an ensemble, setting a new state of the art on the primary co-bps metric among public and reported NLB'21 results. In a cross-day protocol constructed from the NLB'21 MC Maze dataset series, GRAFT recalibrates from MC Maze to the scaled MC Maze datasets (Large/Medium/Small) by updating only 9.21% of parameters, reaching 0.3749, 0.3112, and 0.3152 co-bps with restricted target-day support sets. These results show that the same interface-backbone separation supports both strong Transformer-based neural population activity modeling and data-efficient cross-day recalibration.

---


### 250. [Exploring the Design Space of Reward Backpropagation for Flow Matching](https://arxiv.org/abs/2606.11075)

**<font color=#1a73e8>作者：</font>** Ruoyu Wang, Boye Niu, Xiangxin Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning text-to-image flow matching models with human preferences via direct reward backpropagation is sample-efficient but hampered by two well-known pathologies: activations cannot be stored across the full sampling trajectory at modern model scale, and chained Jacobian products across steps inflate the reward gradient as it travels back to early indices. Connector-based methods, such as LeapAlign, address these issues by replacing the full backward trajectory with a short pinned path, highlighting a useful decoupling between sampling and optimization. However, the quality of the resulting gradient depends on how accurately this short path approximates the full rollout, especially over long intervals. We propose FlowBP, a unified surrogate-trajectory framework that treats the backward trajectory itself as the design object. FlowBP keeps a no-gradient cached rollout for sampling, then builds a lightweight backward surrogate from cached and selectively re-forwarded velocities. This view separates four choices: the reward-model input, active set, integration weights, and bridge coupling, and recovers prior direct-gradient methods as particular settings. Within this framework, we instantiate three variants: FlowBP-Sparse uses sparse Euler reconstruction, FlowBP-Bridge adds controlled bridge coupling, and FlowBP-Lagrange raises the order of leap quadrature. All three bound memory by the active-set size and limit gradient chaining to at most one Jacobian factor. Across SD3.5-M, FLUX.1-dev, and FLUX.2-Klein-base on preference, quality, and compositional metrics, the three variants improve over direct-gradient baselines on most metrics.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-269](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
