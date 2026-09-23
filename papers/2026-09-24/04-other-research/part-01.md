# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

---

### 1. [What Does 99% Accuracy Measure? A Reproducible Audit of Shortcut Learning in a Widely Used Fake News Corpus](https://arxiv.org/abs/2609.25006)

**<font color=#1a73e8>作者：</font>** Yuvraj Verma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text classifiers trained on the ISOT/Kaggle "Fake and Real News" corpus routinely report accuracy and F1 above 0.98, a level of performance that sits uneasily beside the difficulty of assessing veracity. Using a transparent TF-IDF and linear-classifier pipeline as a measurement instrument, we audit the corpus along three leakage channels and two distribution-shift protocols, releasing all code and derived numbers. First, the benchmark is partly degenerate: a classifier given only the subject metadata field, with the article text discarded, attains F1 = 1.000, since the two classes have disjoint subjects. Second, removing all three leakage channels, metadata, a newswire source tag present in 99.2% of real articles, and 6,251 duplicate documents contaminating 19.4% of a naive test split, lowers F1 by only 1.21 points (0.9935 to 0.9814); the residual signal is diffuse editorial style rather than a few giveaway tokens, since deleting the 1,000 highest-weight unigrams still leaves F1 = 0.926. Third, this style signal does not transfer: under a topic-disjoint protocol, average precision falls from 0.9995 to 0.9475 and deployed F1 from 0.9905 to 0.8067, with a prior-matched analysis confirming a genuine 5.2-point loss of discrimination, while temporal transfer is nearly lossless. A fine-tuned DistilBERT is stronger in-distribution (F1 = 0.9993) but degrades far more under topic shift, losing 12.9 average-precision points against the linear model's 5.2. Transferred to the independent LIAR benchmark, all three models fall to near-chance ranking (ROC-AUC 0.54-0.57), none beating a majority-class baseline. We conclude that within-corpus scores here quantify source and topic separability rather than veracity, that added capacity exploits the shortcut rather than avoiding it, and we recommend metadata-only, small-sample, and topic-disjoint baselines as inexpensive diagnostics for future work.

---


### 2. [A Computational Approach to Measuring Semantic Change in Sanskrit Literature](https://arxiv.org/abs/2609.25012)

**<font color=#1a73e8>作者：</font>** Tanay Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diachronic word embeddings have become the modern standard for tracking semantic change, yet they have been largely validated on modern, high-resource, and well-segmented languages. This paper tests whether the paradigm transfers to Sanskrit, an ancient, low-resource language whose phonological fusion (sandhi), morphological inflection, compounding, and polysemy pose a unique challenge. I assemble a 2.7M-token corpus spanning four canonical periods, recover word boundaries with a neural byte-level sandhi splitter and lemmatizer, and train per-period embeddings across configurations. To evaluate the system, I curate a validation set from historical scholarship and test recovery directionally with anchor displacement. Of 21 testable shifts, 19 move in the philologically attested direction (sign test, p=0.00011). I further show which configuration the language forces and comment on opportunities for improvement.

---


### 3. [Do Existing Preconditioners Improve Biomedical Tabular Foundation Learning? An Empirical Study on TabPFN Optimization](https://arxiv.org/abs/2609.25013)

**<font color=#1a73e8>作者：</font>** M. Sajid, Pinki Khatun, M. Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models have recently shown strong potential for structured biomedical data analysis. Among them, TabPFN has emerged as an effective approach for low-data tabular classification tasks. However, the impact of optimization and preconditioning strategies on biomedical fine-tuning remains largely unexplored. In this work, we present a comprehensive empirical investigation of five AdamW-based preconditioning strategies for fine-tuning TabPFN v2.5 on 59 biomedical datasets spanning Alzheimer's disease, breast cancer, schizophrenia, significant memory concern (SMC), KEEL biomedical datasets, and UCI biomedical benchmarks. The evaluation considers predictive performance, computational efficiency, and statistical significance analysis. Experimental results demonstrate that the original AdamW optimizer consistently achieves the best overall performance and statistical ranking, while existing curvature-aware preconditioners fail to provide reliable improvements across diverse biomedical learning scenarios. The findings suggest that generic preconditioning approaches may not adequately capture the optimization characteristics of biomedical tabular learning, motivating the development of biomedical-aware preconditioners specifically tailored for healthcare-oriented tabular foundation models.

---


### 4. [Deepfakes and Synthetic Media: Generation, Detection, and Governance](https://arxiv.org/abs/2609.25017)

**<font color=#1a73e8>作者：</font>** Alexandros Gazis, Efstathios Karypidis, Kleanthi Santamouri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfakes, synthetic audiovisual content produced by deep generative models, have escalated into a critical threat across civilian and military domains, enabling identity fraud, disinformation campaigns, and evidence fabrication. In high-stakes environments, ranging from journalism and finance to healthcare and legal contexts, the consequences extend to severe misinformation, market manipulation, identity fraud, and the erosion of institutional trust. This entry explores how modern visual intelligence and computer vision techniques are used to detect deepfakes. It outlines key deepfake generation models, such as GANs, autoencoders, neural rendering, and diffusion systems, while also explaining how adversarial methods enhance realism and challenge existing detectors. The overview highlights visual artifacts, digital patterns, and physiological cues commonly leveraged in detection and reviews major CNN, transformer, and frequency-based approaches. It also summarizes evaluation practices and the difficulty of achieving strong generalization. Finally, it identifies emerging directions, including modern intelligence techniques for civilian and military content verification. This survey covers generation architectures (GANs, latent diffusion, neural rendering, video synthesis), the spatial, temporal, frequency-domain, and physiological artifacts they produce, and the detector families that exploit them. We examine evaluation benchmarks and protocols, highlighting cross-generator generalization as the field's central open challenge. Beyond detection, we discuss cryptographic provenance standards, watermarking, and regulatory frameworks (EU AI Act, DSA, GDPR). We conclude that effective deepfake governance requires defense-in-depth integrating forensic detection, verifiable provenance, and institutional accountability.

---


### 5. [Retrieved-Span Training for Efficient Query-Focused Meeting Summarization on QMSum](https://arxiv.org/abs/2609.25028)

**<font color=#1a73e8>作者：</font>** Edward Xi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> QMSum provides no scorer, making query-focused meeting summarization results difficult to compare. We rescore or generate 15 systems under one implementation. Through a common inference port, a released 406M Fusion-in-Decoder specialist loses 6.30 ROUGE-1 when moved from capped long input to 2,000-word retrieved spans. Fine-tuning it on this span regime recovers the loss. On test it scores 36.33 ROUGE-1 versus 35.41 for our 1.2B system; the meeting-cluster 95% interval for the difference is [-0.27, +2.22], so QMSum does not statistically separate them. The smaller system uses about one-third as many total parameters and less than half the peak inference memory. Within the fixed 1.2B base, span-regime fine-tuning adds 5.29 [+4.02, +6.56], while replacing the first 4,500 transcript words with 2,000 retrieved words adds 1.55 on test and 0.29 on validation. Separately, under one concise prompt and reference-overlap scorer, a released 406M specialist exceeds five proprietary hosted models by at least 6.2 ROUGE-1, but output length and absent human or factuality evaluation limit this ordering. Conclusions are limited to QMSum and automatic metrics.

---


### 6. [From Tone to Trajectory: Continuous Sentiment and the Shape of Monetary Policy Communication](https://arxiv.org/abs/2609.25034)

**<font color=#1a73e8>作者：</font>** Martin Feldkircher, Márton Kardos, Kristoffer Laigaard Nielbo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Central bank press conferences are not merely information releases --- they are structured narratives. We study whether the shape of sentiment within a statement, not just its average tone, carries policy-relevant signals. Constructing sentiment arcs for ECB and Fed press conferences along three dimensions --- monetary stance, economic outlook, and uncertainty --- we assess their predictive content for policy rate changes, inflation expectations, and forecaster disagreement. Our findings show that arc shape robustly predicts rate decisions beyond lexicon-based benchmarks at both institutions --- it is not merely whether a statement sounds hawkish or economically optimistic on average, but how these sentiments are sequenced and emphasized across the statement, that carries the policy signal. Arc features also shape how professional forecasters update inflation expectations and how much they disagree, pointing to a receiver-side effect distinct from the direct policy signal. These findings suggest that communication design --- the sequencing and emphasis of policy language across a statement --- is a first-order feature of the policy signal, not a second-order refinement.

---


### 7. [4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.25036)

**<font color=#1a73e8>作者：</font>** Yongchao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic Gaussian Splatting provides an explicit representation of evolving 3D scenes, but existing approaches are primarily optimized for reconstruction, future-state generation, or rendering rather than for learning reusable predictive dynamics. We propose 4DGS-JEPA, a Gaussian-native joint-embedding predictive architecture for causal multi-horizon prediction over dynamic Gaussian scenes. The model uses a hierarchical scene-, motion-group-, and Gaussian-level representation together with a horizon-conditioned transition operator that supports both direct prediction and recursive rollout. Its central principle is temporal composition: different chronological transition paths reaching the same future endpoint should produce compatible predictive states. Endpoint and multi-horizon path supervision anchor these predictions to future target embeddings, while a selective geometry decoder and geometry-level composition ground the learned dynamics in consistent group motion and Gaussian geometry without requiring complete future appearance reconstruction. We further introduce a hybrid correspondence mechanism that combines persistent canonical identity with residual optimal-transport matching under reordering and topology change. We characterize zero-loss path agreement and finite-error rollout accumulation theoretically. Three controlled experiments provide mechanism-level evidence that temporal composition reduces latent path dependence while retaining predictive accuracy, geometry-level composition improves consistency of decoded motion, and hybrid correspondence preserves reliable identity while remaining robust when correspondence becomes ambiguous. Together, 4DGS-JEPA provides a predictive, temporally compositional formulation of dynamic Gaussian worlds.

---


### 8. [Graph-Based Inference for Feedback-Driven Word Deduction: A Scalable Framework for the Jotto Problem](https://arxiv.org/abs/2609.25056)

**<font color=#1a73e8>作者：</font>** Dakshi Arora, Prakhar Kumar Srivastava, Ranjib Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A feedback-based word deduction framework based on the Jotto problem is proposed, and the problem space is represented as a weighted graph where all valid words correspond to nodes, and the edge weight is defined by the number of common letters between the two words. Finally, the gameplay is defined as an iterative constraint propagation mechanism where feedback is used to iteratively narrow the incompatible space of the graph, facilitating the reduction of the hypothesis space in a structured and interpretable manner.
In contrast to existing approaches, where the problem space is typically defined for fixed-length isograms, the proposed framework generalizes to variable-length words (between 3 and 8 letters) and naturally extends to repeated letter cases, facilitating the treatment of realistic Jotto problem instances within a unified framework for the first time. The proposed framework's applicability and solver dynamics are also discussed through an interactive implementation and a qualitative case study, respectively.
Significant automated tests on approximately 3,000 simulated gameplay scenarios identify a novel convergence behavior: the expected number of iterations diminishes with increasing word length. A strong relationship is confirmed using statistical tests to verify a logarithmic relationship, which is also verified using regression modeling and goodness-of-fit tests.
In addition to the initial problem statement, this formulation introduces graph pruning as a viable paradigm for feedback-driven inference with interpretability and its association with symbolic reasoning and interactive intelligent systems.

---


### 9. [SPARC: SuperPixel-Aware Region Contrastive Learning for Self-Supervised Dense Prediction](https://arxiv.org/abs/2609.25067)

**<font color=#1a73e8>作者：</font>** David Szczecina, Yuanpei Xiang, Jitao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has become an effective approach for learning visual representations without manual annotations. Among SSL approaches, contrastive learning has been widely used for visual representation learning. However, existing contrastive SSL methods have focused primarily on image-level or pixel-level representation learning, while region-level representation learning remains less explored. We propose SPARC, a region-level contrastive learning framework that leverages superpixels to establish explicit correspondence between augmented image views. SPARC introduces a region contrastive branch that performs superpixel-based feature pooling and optimizes a region-level contrastive objective jointly with a global image-level objective. Under identical settings, SPARC consistently outperforms previous methods such as MoCo-v2 and DenseCL, achieving improvements of up to +9.79 mIoU for semantic segmentation and +4.88 AP for object detection. Ablation studies further demonstrate that region-level objectives produce the strongest performance. Thus, region-level contrastive learning is an effective approach for improving self-supervised visual pretraining for dense prediction tasks. Code repository can be accessed at this https URL.

---


### 10. [Federating Quantum and Classical Computing: A Privacy-Preserving Hybrid Approach](https://arxiv.org/abs/2609.25082)

**<font color=#1a73e8>作者：</font>** Carlos Cano, Daniel M. Jimenez-Gutierrez, Diego Sal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum machine learning (QML) is increasingly recognized as one of the most promising near-term applications of quantum computing, viewed as a next-frontier candidate beyond purely classical approaches. Hybrid quantum-classical models operationalize this potential by embedding a parameterized quantum circuit within a model where all other components remain classical-a design already applied to chemistry simulation, financial modeling, and image classification. However, their deployment in privacy-sensitive, multi-party settings is constrained by the need to avoid centralizing raw data and by the requirement that modern quantum circuits remain parameter-efficient to stay trainable at scale.
In this paper, we address these constraints by evaluating federated learning (FL) as a means of combining a hybrid quantum-classical active party with a classical passive party, using this http URL's Blind Vertical FL (SBVFL) protocol to avoid centralizing raw data, while drastically reducing communication. We construct the split multiplicative periodic parity (SMPP) benchmark, following common QML design practice. On this task, our simulations show that SBVFL raises accuracy from 0.7227 to 0.8757 compared to local training, closely approaching non-private centralized accuracy, and that the hybrid quantum-classical model achieves this with substantially fewer trainable parameters than the classical neural networks and random forest alternatives. These results show that FL enables high-performing, privacy-preserving quantum-classical collaboration without centralizing raw data.

---


### 11. [CPyGraph: A Version-Aware Static Analysis Framework for Native CPython Bytecode](https://arxiv.org/abs/2609.25083)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Wen Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static analysis of Python packages must recover both program structure and object flow across first-class functions, dynamic dispatch, implicit protocol calls, exceptions, closures, and module execution. Native CPython bytecode provides the executable lowering of these behaviors, but its instruction, call, stack, and exception representations change across releases. This creates a need for a version-aware analysis foundation whose graph products share the same bytecode identities and semantics. We present CPyGraph, a C++ framework for package-level analysis of native CPython bytecode. Version- specific adapters expose stack, control, call, lexical, protocol, and exception semantics through a shared interface while preserving code-object identities and native bytecode offsets. An operand-stack-aware Andersen points- to analysis and call graph grow together to a fixed point. Their shared state supports exception-aware CFGs, block-level CDGs, and interprocedural DDGs, with optional function-level flow, context, and bounded path sensitivity. The framework also records unresolved dynamic behavior through typed coverage summaries. We evaluate CPyGraph with PYGBench, 201 package-level programs and 1,733 fixed candidates. On CPython 3.10, the default analysis reaches 91.40% candidate precision and 100% recall; complete sensitivity reaches 94.97% precision with the same recall. Across CPython 3.10-3.14, 1,328 of 1,334 version-invariant queries agree, and CPyGraph matches PyCG on its 112-program call-graph benchmark.

---


### 12. [An Accurate and Interpretable Hyper Graph Neural Network for GBM Survival Prediction](https://arxiv.org/abs/2609.25088)

**<font color=#1a73e8>作者：</font>** Mushahid Intesum  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Survival prediction for glioblastoma multiforme (GBM) demands models that are both accurate and interpretable, yet existing approaches treat these objectives as com- peting, where performant models sacrifice transparency, while interpretable models accept degraded predictive power. We argue that this trade-off is not inherent. Graph neural net- works offer a structural foundation for extracting interpretable, explainable representations without compromising discriminative ability. Furthermore, current methods typically rely on a single imaging modality, underutilizing the complementary information available across multi-modal MRI and clinical metadata. We propose a multi-modal framework that inte- grates three components to address both objectives simultaneously: (1) a sheaf hypergraph neural network that captures higher-order relationships among tissue patches through direc- tional, asymmetric message passing; (2) a concept bottleneck layer that compresses learned representations into clinically grounded concepts, enforcing ante-hoc interpretability; and (3) an extension sufficiency test (EST) regularizer that penalizes unfaithful explanations during training, ensuring that model explanations genuinely reflect the internal decision process. Clinical and genomic features are incorporated through gated fusion, preserving the dominant prognostic signal of molecular markers while retaining concept-level traceabil- ity. Evaluated on 593 patients from the UPenn-GBM dataset under 5-fold cross-validation, our framework achieves a concordance index of 0.643 with the lowest fold-level variance among all compared models (std = 0.015). To our knowledge, this is the first work to unify sheaf hypergraph convolution, concept bottleneck supervision, and EST regularization for interpretable survival prediction from brain MRI

---


### 13. [You've Seen Enough: Quality-Constrained Image Coding for Machines](https://arxiv.org/abs/2609.25108)

**<font color=#1a73e8>作者：</font>** Khoa Pham-Dinh, Sanaz Nami, Hamed Rezazadegan Tavakoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual data is increasingly consumed by machine-vision systems rather than by human observers. Image Coding for Machines (ICM) compresses images assuming the main observer is a computer vision application and that the human observer needs to inspect or validate the decisions. Inspired by just-noticeable distortion, which sets the quality to the just-acceptable level for human observers, we aim to cap the human-observed quality at a desired level, with the goal of using the remaining coding capacity to improve the machine performance. We recast joint compression-segmentation training as a constrained optimization problem in which the codec must meet a predefined acceptable target visual quality while a task term consumes the remaining coding capacity. We solve this by designing a penalty function to guide the quality to the desired target. We propose two penalty functions, an absolute function and a bilinear function, the latter applying a steeper slope once the target visual quality is exceeded. Experimental results show that, under the quality constraint, the proposed method achieves a BD-rate of $-22.82\%$ over an unconstrained joint rate--distortion--task optimization and $-29.81\%$ over a simple rate--distortion baseline, showcasing bitrate reduction with the same task performance. This is achieved while the codec also meets the target visual quality with a reasonable error and without adding any complexity overhead.

---


### 14. [Entropy Can Flow, or It Can Guide. Be Entropy. LEDFlow: Introducing Entropy-guided Generation Order into Uniform Discrete Flow](https://arxiv.org/abs/2609.25131)

**<font color=#1a73e8>作者：</font>** Tung Sum Thomas Kwok, Yidong Ouyang, Yingjia Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform discrete flow permits repeated updates at every generation position. While continued revision supports correction of wrong tokens, it also exposes correct intermediate predictions to later errors. An experiment on Sudoku puzzles shows that 9.4% of generated cells are correct at an intermediate step but incorrect in the final output. We introduce generation order into uniform discrete flow through selective absorption, which fixes chosen predictions while preserving the uniform-flow velocity at active positions. To prevent absorbing incorrect predictions, we propose Low-Entropy Discrete Flow (LEDFlow), a training-free sampler that adaptively orders absorption by local entropy. By decomposing absorption error into joint dependence and conditional prediction terms, we show that selecting the lowest-entropy positions under a fixed absorption budget minimizes an upper bound on the conditional term. We further support the choice of local entropy by showing that the decision-error bound of global lookahead grows with the lookahead window under an imperfect denoiser. Across reasoning benchmarks, LEDFlow attains 0.845 Nikoli Sudoku solve accuracy, with the largest gains on strongly constrained tasks. On text-to-image generation it attains the best overall score, and on multimodal understanding it improves over the native sampler on all six benchmarks, at an inference cost comparable to standard flow sampling.

---


### 15. [Stable Unsupervised Continual Chunking with Sheaf SyncMap](https://arxiv.org/abs/2609.25143)

**<font color=#1a73e8>作者：</font>** Xueyuan Li, Danilo Vasconcellos Vargas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Continual chunking is a fundamental problem in machine learning and neuroscience, where the goal is to identify groups of states that frequently co-occur in temporal sequences. A key challenge is to form accurate chunks while maintaining their stability over time. In this work, we propose sheaf regularization to reduce local inconsistencies in Decentralized SyncMap, a self-organizing system, and thereby stabilize its chunking dynamics. We introduce a radial sheaf structure that penalizes distance-dependent radial motion between pairs of variables. Experimental results show that the proposed method achieves the highest normalized mutual information (NMI) among the evaluated SyncMap variants on 12 of 18 probabilistic Continual General Chunking Problem (CGCP) graphs with two-state memory and on 17 of 18 graphs with dynamic memory. In the sequential adaptation experiment, Sheaf SyncMap also achieves high NMI after shifts in the input distribution, indicating that it can adapt to new knowledge while avoiding the negative transfer commonly observed in modern machine learning systems such as neural networks.

---


### 16. [Brain-Inspired Hierarchical Modularity for General Continual Learning](https://arxiv.org/abs/2609.25146)

**<font color=#1a73e8>作者：</font>** Hongwei Yan, Kanglei Zhou, Qi Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning, the ability to learn from sequential experience while retaining and adapting prior knowledge, is central to intelligent systems operating in changing environments. However, conventional continual learning is typically studied with offline task-wise training and clear task boundaries, leaving a substantial gap from general continual learning under online, uncertain, and evolving data streams. In this regime, intelligent systems must separate conflicting experience to reduce interference while integrating compatible experience to promote generalization. Inspired by the organization of the Drosophila learning and memory system, we identify a hierarchical modular principle that coordinates both functions through expert specialization and ensemble integration. We instantiate this principle as lightweight modular adaptation of pretrained foundation models, combining brain-inspired random expansion for expert routing and diversified modular integration across spatial and temporal scales. Across visual recognition, vision-language understanding, ego-exo video understanding, and embodied vision-language-action learning, our method consistently improves learning under online and uncertain data streams, with gains exceeding 50 percentage points over replay-free alternatives in embodied manipulation. These findings support hierarchical modularity as a biologically grounded path for learning from dynamic experience.

---


### 17. [Dual-GNN Multilevel Coarsening for Maximum Independent Set](https://arxiv.org/abs/2609.25149)

**<font color=#1a73e8>作者：</font>** Tianfeng Chen, Xianyue Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving large-scale instances of the Traveling Salesman Problem (TSP) exactly is computationally expensive. Researchers often employ graph sparsification methods to improve computational efficiency. Traditional sparsification methods typically rely on fixed heuristics and fail to fully exploit instance-specific structural information. In this paper, we propose Graph Edge Sparsification (GES), a learning-based sparsification approach for Euclidean TSP. By incorporating geometric structural information and combinatorial optimization technology, our proposed method adaptively generates a sparsification graph for different instances, significantly reducing the graph size and accelerating the solving process. Experimental results demonstrate that our sparsification method can prune up to 95\% of edges on the MATILDA dataset, while keeping the solution gap within 1\% of the optimal value. Moreover, our approach exhibits strong generalization capability on the TSPLIB this http URL some large-scale instances, the pruning rate exceeds 99\%, while the optimality gap remains below 1\%.

---


### 18. [Exposing Blind Spots in Deep Imbalanced Regression Evaluation](https://arxiv.org/abs/2609.25152)

**<font color=#1a73e8>作者：</font>** Noah C. Puetz, Jens U. Brandt, Marc Hilbert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Imbalanced Regression (DIR) addresses a common failure mode of regression models: target distributions are highly non-uniform, causing models to perform best in densely populated target regions even when reliable performance is required across the full target range. Despite rapid methodological progress, DIR evaluation remains constrained by three blind spots: it is dominated by image-based benchmarks, its standard many-/medium-/few-shot protocol is diagnostic but not decision-complete, and tail-region stability across random seeds has not been systematically evaluated. We revisit DIR evaluation along these three axes. First, we broaden the data domain by evaluating DIR on a multimodal virtual sensing benchmark (\textsc{MuViS}) with nine time-series extrinsic regression tasks across six physical domains, where rare target values often correspond to operationally meaningful regimes. Second, we adopt balanced MAE (\emph{bMAE}) and introduce balanced Mean Absolute Scaled Error (\emph{bMASE}), a scale-normalized metric for decision-complete comparison across methods and datasets. Third, through a repeated reevaluation of six representative DIR methods across multiple random seeds, we show that the tail regions targeted by DIR exhibit particularly high sensitivity to seed-level variability. Our results show that standard virtual-sensing models exhibit substantial tail degradation hidden by global MAE, that existing DIR methods can improve balanced performance but transfer unevenly to multimodal time-series data, and that tail-region instability remains a largely hidden failure mode under current DIR evaluation practice. Together, these findings and our publicly available code provide a reproducible basis for future DIR research toward regression systems that capture rare target regimes as reliably as common ones.

---


### 19. [Benchmarking Neural Defend ARCAS 1B: A Foundational Multimodal Deepfake Detection Model](https://arxiv.org/abs/2609.25154)

**<font color=#1a73e8>作者：</font>** Sivashankar Selvarajan, Piyush Verma, Sumit Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-generated imagery evolves faster than benchmark-specific detector evaluations, making a single score an incomplete account of generalization. This paper evaluates Neural Defend ARCAS 1B across benchmark families without benchmark-specific parameter updates. We retain native aggregation and supplement it with record-level measures, coverage accounting, and subgroup diagnostics. Each Results subsection identifies the release and evaluation population, reports the official metric, and describes observed error patterns. A combined analysis synthesizes shared patterns while preserving the distinction between native and pooled quantities. Cross-paper comparisons are restricted to aligned evidence; differences in release, population, preprocessing, training, or benchmark exposure are context rather than rank. The findings characterize performance on evaluated records, not universal reliability, calibration, attribution, or future adaptive attacks. By keeping benchmark-native outcomes distinct from pooled summaries, the study makes test-population, class-balance, and missing-record-coverage differences visible. It supports interpretation of detector results in research, platform-safety, and forensic-review settings, foregrounding traceable protocol conditions over claims or leaderboard comparisons.

---


### 20. [Learning Neural Feedback Linearization for Data-driven Systems via Augmented Lagrangian](https://arxiv.org/abs/2609.25163)

**<font color=#1a73e8>作者：</font>** Lakshmi Priya P. K., Andreas Schwung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paper proposes a novel data-driven framework for designing and training a feedback linearizing controller by explicitly incorporating relative degree based conditions into the learning process. This enables the conventional feedback controller components to be replaced by neural Lie derivatives, thereby facilitating a fully data-driven feedback linearization framework. Furthermore, practical closed-loop stability is established by deriving sufficient conditions under which bounded identification errors lead to bounded tracking errors. The derived theoretical results are validated through their application to an armature controlled DC motor.

---


### 21. [Mitigating Sequential Reappearance in Diffusion Data-Point Unlearning](https://arxiv.org/abs/2609.25166)

**<font color=#1a73e8>作者：</font>** Donghyun Kim, Taehyuk Lee, Jinyeong Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion data-point unlearning is typically evaluated immediately after each deletion, even though subsequent requests may repeatedly update the same model. We identify sequential reappearance, a failure mode in which an instance that is initially judged to be forgotten later returns to the memorized regime without reuse of the deleted data or adversarial fine-tuning. To capture this behavior, we introduce a target-level evaluation protocol that tracks whether each target is forgotten immediately, remains forgotten at the end of the sequence, or reappears during subsequent deletions. We further find that targets that later reappear exhibit sharper local denoising-loss geometry after deletion than targets that remain forgotten.

---


### 22. [Multi-Term Fourier Graph Neural Network with Sample Relationship Learning for Enhanced Remaining Useful Life Prediction](https://arxiv.org/abs/2609.25179)

**<font color=#1a73e8>作者：</font>** Ya Song, Laurens Bliek, Yaoxin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the remaining useful life (RUL) is essential for effective predictive maintenance. Spatio-Temporal Graph Neural Networks (ST-GNNs), which can model both temporal and spatial relationships by representing time series data as a sequence of graphs, have shown exceptional performance in RUL prediction. However, current ST-GNNs face several drawbacks. First, they require domain expertise or significant computational power to establish graph structures prior to deploying GNNs. Second, the models are restricted to capture temporal dependencies within a predefined fixed-size lookback window. This restriction ignores the common issue of varying time series lengths, leading the prediction model to miss short-term or long-term dependencies. Finally, conventional models often fail to capture the inherent relationships between samples generated from adjacent time windows, which are crucial for improving both the accuracy and robustness of predictions. To address the aforementioned issues, we introduce a novel framework called Multi-Term Fourier Graph Neural Network with Sample Relationship Learning (MTFGN-SRL). Rather than treating the sample as a sequence of graphs, we consider it as a single complete graph and utilize a Fourier Graph Neural Network (FGN) to capture the spatio-temporal information in the frequency domain. We propose a multi-term learning module that utilizes multiple lookback windows to generate samples with varying terms, which are then fed into the FGN to enhance the extraction of useful information from the data. Finally, we develop a sample relationship learning module by training a heterogeneous GNN to identify inter-sample relationships, resulting in enhanced accuracy and robustness in predictions. Evaluations on the CMAPSS dataset demonstrate MTFGN-SRL's superior performance over state-of-the-art methods in RUL prediction.

---


### 23. [Lean Pool: An AI-Maintained Archive of Formalized Mathematics](https://arxiv.org/abs/2609.25199)

**<font color=#1a73e8>作者：</font>** Vasily Ilin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lean Pool is a repository of formalized mathematics. It is grown, maintained and optimized by AI agents.

---


### 24. [How Children Design and Reason about Trustworthy AI Chatbots](https://arxiv.org/abs/2609.25244)

**<font color=#1a73e8>作者：</font>** Deniz Ozturk, Jiayu Li, Daksh Pratap Singh 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Children increasingly interact with AI chatbots, making trust calibration essential to AI literacy. Prior research has examined children's trust in AI mainly as users evaluating systems built by others, rather than as designers of their own chatbots. We developed a chatbot-building environment with adjustable trust-relevant traits (e.g., confidence, transparency, formality, assertiveness), rules, and persona. We conducted mixed-methods study with 115 learners (ages 8-18) who made 119 chatbots. We examined how children configured their chatbots, reasoned about trustworthiness, and how closely chatbot behavior aligned with their designs. Younger students (age 10-13) set significantly higher confidence than older students (age 14-18), and some deliberately built chatbots that gave wrong answers on purpose, yet still called them trustworthy, arguing that a chatbot does what it was built to do. Younger students equated trust with purpose-fulfillment, while older students linked it to transparent, calibrated design. Students also calibrated academic chatbots to be more transparent and formal than hobby chatbots. We identify seven design dimensions describing what children believe makes a chatbot trustworthy, and discuss implications for AI literacy tools.

---


### 25. [Geometric and Semantic Coupling for Interaction Understanding in 3D Scenes](https://arxiv.org/abs/2609.25247)

**<font color=#1a73e8>作者：</font>** Hanyang Kong, Xingyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interaction understanding in 3D scenes requires a joint description of movable parts, their motion, and the regions through which they can be operated. We present Segment-Snap, which connects these outputs through the physical relationship between parts and handles. Learned predictors identify broad part surfaces and small handles. A geometric decoder uses planar and upright priors to constrain motion, then selects hinge lines using predicted handle locations, without training a motion regressor. Conversely, a joint part-and-handle predictor supplies additional handle candidates, whose motion classes are refined using containing parts. Each information transfer is applied once, without iterative feedback. On Articulate3D validation, handle guidance raises motion-gated AP from 13.74% to 40.98% at fixed masks and axes. Additional handle candidates raise handle AP from 24.63% to 29.65%; part-based class correction adds 0.98 points, and full context reaches 30.99%. Repeated training, learned-decoder controls and paired visualizations establish the benefits and limitations of combining geometric and semantic evidence for interaction understanding.

---


### 26. [Partition-Matched Evaluation of Community Features under Distribution Shift in Android Malware Function-Call Graphs](https://arxiv.org/abs/2609.25256)

**<font color=#1a73e8>作者：</font>** Junru Zhu, Yixin Yang, Xiaoqing Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph-based Android malware classifiers can lose accuracy under malware-type or family shifts. We test whether mesoscopic organization in function-call graphs provides shift-stable information beyond local degree profiles (LDP), global statistics, lightweight metadata, and size-matched random partitions. Using 15,000 MalNet-Tiny, Common, and Distinct graphs, six Leiden descriptors specified before evaluation, and five optimizer seeds, communities raise Tiny macro F1 from 78.7% to 81.3% but yield 29.4-point source-only Common degradation. One size-matched random partition yields 27.8-point degradation. Across five random partitions, mean degradation is 27.9 points; the 95% two-level bootstrap interval for random minus community degradation is [-4.2, 1.2] points. With metadata, the corresponding difference is -0.2 points with interval [-1.1, 0.6]. Removing modularity raises structure-only Common macro F1 from 51.9% to 53.6%. The tested signature adds IID signal but shows no repeatable shift-stability advantage, demonstrating why mesoscopic graph claims need partition-matched controls and repeated null draws.

---


### 27. [MedGate-Fusion: Integrating First-Encounter Semantic Narratives and Physiological Biomarkers for Prospective Stroke Risk Stratification](https://arxiv.org/abs/2609.25272)

**<font color=#1a73e8>作者：</font>** Hemn Khdr, Mohammad Noaeen, Karim Keshavjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prospective stroke risk stratification in primary care is challenging because early risk signals are distributed across routine biomarkers and unstructured clinical narratives. We propose MedGate-Fusion, a multi-modal gated architecture that integrates transformer-based embeddings of first-encounter narratives with ten routinely recorded risk markers. We used electronic medical record data from the Canadian Primary Care Sentinel Surveillance Network (CPCSSN). Starting from 808,921 encounter-level observations, we constructed a first-encounter cohort and retained 102,736 unique patient records with non-empty narratives and sufficient data to evaluate a five-year stroke outcome. To reduce explicit target leakage from diagnostic mentions in notes, we applied dictionary-based redaction of stroke-related terms prior to semantic encoding.

---


### 28. [A Case Study in Accessible Redesign of a Wastewater Dashboard](https://arxiv.org/abs/2609.25273)

**<font color=#1a73e8>作者：</font>** Tingying He, Jake Wagoner, Md Rahat-uz- Zaman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public health dashboards communicate data that can inform important decisions, but they often raise accessibility challenges. We present a case study redesigning the Utah Wastewater Surveillance System dashboard to improve accessibility and usability across desktop and mobile settings. The redesign was informed by WCAG and developed iteratively with Utah DHHS collaborators, and we collected feedback on the final design from an external blind researcher. Our case study highlights that accessible dashboard design requires aligning accessibility guidelines with user needs, stakeholder workflows, and technical constraints. It also suggests that simple, targeted technical solutions tailored to the existing environment can provide practical value for dashboard redesign in government contexts.

---


### 29. [Controller-Only False Confirmation in Passive RF UAV Link Detection](https://arxiv.org/abs/2609.25294)

**<font color=#1a73e8>作者：</font>** Rajendra Upadhyay, Rajendra Paudyal, Al Nahian Bin Emran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Passive radio frequency (RF) sensing is widely used for counter-unmanned-aerial-vehicle (counter-UAV) detection. Existing studies commonly report high accuracy against background RF or WiFi/Bluetooth interference, but rarely isolate controller-only operation without a linked aircraft. We present a dual-band software-defined radio (SDR) measurement study with ambient, controller-only, and linked states for three commercial UAV platforms (DJI Phantom 3 4K, Hubsan H501S, DJI Mavic Mini). Two USRP B210 receivers simultaneously scan eight 2.4 GHz and twelve 5.8 GHz observation windows across twenty rounds. We first train an energy-based detector using linked and ambient scans only. At four ranked concurrent dwell steps (8 s), it achieves 0.992 linked-versus-ambient balanced accuracy but false-confirms 30 out of 60 controller-only scans (FCRctrl = 0.500). We then include controller-only scans in training and use confirm, reject, and defer outputs under an explicit controller-only false-confirmation-rate (FCR) constraint. For the pooled all-platform analysis, the constraint reduces observed FCRctrl from 0.350 to 0.050, while confirm-linked TPR decreases from 0.900 to 0.400 and 42.1% of scans are deferred. The corresponding compact scan performs substantially better for Hubsan and Mavic than for Phantom. A hardware-in-loop experiment reduces measured wall-clock time from 82.9 s to 28.9 s. These measurements show that linked-versus-background accuracy does not measure controller-only false confirmation and that this error should be reported separately.

---


### 30. [Correcting Within-Group Self-Selection Bias in Prioritized Replay](https://arxiv.org/abs/2609.25297)

**<font color=#1a73e8>作者：</font>** Oscar Miró López-Feliu, Herke van Hoof  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prioritized experience replay (PER) improves sample efficiency by replaying high-priority transitions, usually according to absolute temporal-difference error. In stochastic environments, PER can distort the distribution of realized outcomes replayed from transitions with the same state-action pair. We call this within-group self-selection. We quantify the resulting changes in within-group outcome frequencies and mean Bellman targets. We decompose PER into between-group allocation and conditional sibling selection, and derive fixed-buffer corrections that preserve current group-level priority mass: SAMPLE selects a group through PER and trains on a uniformly sampled sibling; AVG averages sibling Bellman targets; and MODEL samples from an empirical full-outcome model. In exact state-action environments with rare high-magnitude outcomes, sibling-aware replay improves learning efficiency over PER, although matched parameter sweeps show that tuning can narrow some gaps. In MinAtar, approximate VQ-VAE groups with SAMPLE mitigate degradation under mean-preserving reward tails in four of five games. Sibling-aware replay thus retains the focus on high-priority state-action regions while recovering their empirical outcome frequencies.

---


### 31. [Making Agents More Consistent: Skills Should Form Habits for Repeat Tasks](https://arxiv.org/abs/2609.25299)

**<font color=#1a73e8>作者：</font>** Travis Weber, Rohit Taneja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On repeated work, agents are inconsistent. We ran 42 tasks three times each and found that, depending on the model, 38% to 74% returned answers that did not agree. Consistency is what a buyer, an auditor, or a regulator requires, and agents do not have it. They are wasteful too: 95.3% to 97.2% of what an agent generates goes to re-deriving a plan the system already knows.
We propose skill habit formation. An agent mines its own execution history for candidate skills, deterministic variants that compete against the incumbent rather than replacing it. A candidate declares the region of input space it claims, so the common case runs as a script and the rest falls through to reasoning. Four gates of ascending cost admit candidates; the central one tests a candidate's execution trace against a retained reference, within a tolerance measured from that reference's own run-to-run variability.
On text-to-SQL, three of four reasoning arms reproduced their own output on 11 to 13 of 42 repeated questions and the fourth on 26 of 42, while a habit-formed variant reproduced on all 456 dispatches we repeated and was non-inferior to every arm it replaced (p<0.0001). It also used 14% to 56% fewer tokens, turning net positive after 7 to 53 reuses.
We measured what this costs in accuracy. The guard admitted work it should have deferred on 2.6% of natural paraphrases and 26% of inputs near its boundary, and 11 of 13 such failures were invisible to the trace-conformance gate at any threshold. Deterministic errors repeat exactly: a bad habit is as reliable as a good one, and that is the price of the property that makes the system auditable. Separating routing from parameter extraction raised end-to-end accuracy from 0.888 to 0.952 at 43% of the cost.

---


### 32. [Topological Signal Processing With Unoriented Operators](https://arxiv.org/abs/2609.25310)

**<font color=#1a73e8>作者：</font>** Andrea Cavallo, Varun Sarathchandran, Geert Leus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological signal processing (TSP) processes signals on simplicial complexes with oriented boundary operators, which is the natural choice for flow signals or when the topological invariants play a role for the task at hand. However, many higher-order signals carry no orientation, and applying oriented operators to them is not well-defined since it introduces an arbitrary choice of simplex orientation. We study an unoriented TSP (UTSP) framework that replaces oriented boundaries with unoriented incidence matrices. First, we show that unoriented incidence and Laplacian matrices between arbitrary simplicial levels admit graph-like spectral properties. Second, since dropping orientation removes the Hodge decomposition, we introduce an unoriented counterpart, termed interaction-order decomposition, which quantifies how much of a higher-order signal is explained by aggregating lower-order signals. Third, we use this decomposition to derive regularizers for signal reconstruction that penalize each interaction order separately. Experiments on real-world data show that the order-aware regularizers outperform oriented baselines, with the largest gains when the signal energy is unevenly distributed across orders.

---


### 33. ["I Talked an AI Chatbot, So What's Next?" How U.S. Young Adults Imagine Responsible AI for Emotion Coping](https://arxiv.org/abs/2609.25311)

**<font color=#1a73e8>作者：</font>** Jiaying Liu, Nimra Ishfaq  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Emotion coping is inherently relational, unfolding through interactions with friends, family, professionals, and communities. Yet AI chatbots are largely designed around a user--AI dyad. Learning from the ethics of care, we examine how AI chatbots shape the relational conditions of emotion coping. We conducted a scenario-based study with 17 U.S. young adults across four emotion coping scenarios. Participants identified eight roles through which AI could support relational conditions, alongside three challenges: flattening distinct relational conditions, discouraging reciprocity, and shifting relational labor onto users. This study contributed a relational perspective of responsible AI in emotion coping. We argue that responsible AI should respond to individuals' situated relational conditions rather than provide general-purpose support. We further identify two design principles: fostering reciprocity by supplying materials to engage with others, and strengthening emotional self-efficacy. Together, we position responsible AI as AI in the loop of human relationships.

---


### 34. [Uncertainty-Aware 3D Residual Wavelet Diffusion for Ultra Low-Field MRI Super-Resolution](https://arxiv.org/abs/2609.25319)

**<font color=#1a73e8>作者：</font>** Rui W. Yeow, Millie Beament, Fred Dick 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra low-field MRI expands global access to neuroimaging but produces scans with low signal-to-noise ratio, reduced contrast, and thick slices. While regression-based super-resolution can recover anatomical detail for segmentation, it returns a single deterministic estimate that gives no indication of regions where the low-field input leaves anatomy underdetermined. Generative diffusion models offer an alternative by sampling the posterior distribution of plausible high-field images, quantifying this anatomical ambiguity. However, applying them to 3D whole-brain MRI is restricted by memory bottlenecks, slow sampling, and scanner domain shifts. We propose a 3D residual wavelet diffusion model that combines three ideas to overcome these hurdles. A lossless wavelet reparameterisation shrinks the spatial grid to fit a whole brain on a single GPU, residual shifting accelerates sampling by starting from the low-field input, and domain randomisation promotes scanner generalisation without paired training data. As the high-field reference is not a voxel-aligned ground truth, we evaluate downstream volumetric agreement. On a healthy cohort (n=19) imaged at 0.064T and 3T, our method matches a leading general-purpose regression approach in volumetric accuracy while additionally generating per-voxel uncertainty maps highlighting underdetermined regions. Furthermore, on a pilot dataset (n=11) of participants with cognitive impairment, disease-relevant atrophy is preserved rather than normalised towards a healthy prior. Our framework brings whole-brain posterior sampling to low-field super-resolution without sacrificing volumetric accuracy.

---


### 35. [Spatiotemporal Kronecker Covariance Neural Networks](https://arxiv.org/abs/2609.25326)

**<font color=#1a73e8>作者：</font>** Andrea Cavallo, Athanasios Georgoutsos, Elvin Isufi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series contain complex patterns that span across both space and time. While covariance-based statistical tools like spatiotemporal Principal Component Analysis (ST-PCA) help identify these patterns, they are limited to linear operations and prone to estimation errors with limited data. Recent covariance-based spatiotemporal neural networks offer more stable, non-linear alternatives, but they ignore correlations across different time steps. To solve this, we introduce the Kronecker coVariance Neural Network (KVNN), a temporal graph neural network that represents the spatiotemporal covariance matrix via a sum of Kronecker products where spatial and temporal dependencies are decoupled. By implementing filtering operations on spatial and temporal components, KVNNs achieve expressive processing capabilities, admit a rigorous spectral analysis, and are provably stable to finite-sample estimation errors, ultimately addressing all of ST-PCA's limitations. We show on five real-world datasets that KVNNs achieve strong forecasting performance, often requiring significantly fewer trainable parameters than competitive methods, and are consistent under estimation noise.

---


### 36. [MirrorDistill: Illumination-Aware Latent Distillation for Efficient Low-Light Restoration](https://arxiv.org/abs/2609.25331)

**<font color=#1a73e8>作者：</font>** Farida Mohsen, Tala Zaim, Nurul Izni Rusli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) is an im- portant component of visual sensing systems operating under degraded illumination, including nighttime surveillance, au- tonomous navigation, remote sensing, and inspection in poorly lit industrial environments. Most LLIE methods rely on output- level reconstruction losses that supervise only the final restored image, leaving the intermediate feature recovery process weakly constrained. This paper proposes MirrorDistill, an illumination- aware latent distillation framework that links the low-light and clean domains through feature mirroring. During training, a shared encoder and an exponential-moving-average teacher decoder process the clean reference image to generate clean- domain latent targets. These targets supervise the low-light student at two levels: raw encoder features and standardized multi-scale decoder projections. The alignment is applied layer by layer, while a proposed illumination-aware weighting scheme gives greater emphasis to underexposed regions. The teacher and reference branches are used only during training, so inference requires only the lightweight student encoder-decoder and in- troduces no teacher-side computational cost. Under evaluation on the standard LOL benchmarks, MirrorDistill outperforms the state-of-the-art methods on the real-captured LOL-v2-Real set, while having the lowest compute complexity (GMACs) and while remaining competitive on the LOL-v1 and LOL-v2-Synthetic datasets. Ablation studies further show the contributions of the encoder mirror, decoder mirror, and illumination-aware weighting. Finally, we release our code as open-source for the benefit of future research.

---


### 37. [Concept Drift from a Causal Perspective](https://arxiv.org/abs/2609.25340)

**<font color=#1a73e8>作者：</font>** Eduardo V. L. Barboza, Jean Paul Barddal, Robert Sabourin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept drift is a common phenomenon in real-world data streams, in which changes in the data-generating distribution can degrade predictive model performance. Most existing definitions characterize drift as changes in the joint distribution $P(\mathbf{x}, y)$, without distinguishing which component of the data-generating process has changed. In this work, we introduce a causal perspective on concept drift based on Structural Causal Models (SCMs). We propose a taxonomy that categorizes drift events by their causal origin, including changes in exogenous variables, endogenous mechanisms, confounders, and target-generating processes. Building on this framework, we develop an SCM-based data stream generator that simulates controlled mechanism-level drift events. Our experiments empirically characterize the distributional effects of each drift type and show that drifts with different causal origins induce distinct patterns of distribution shift and predictive behavior. Furthermore, by integrating causal discovery methods, we use our framework to construct data streams grounded in real-world dependency structures, enabling more realistic and informative evaluation scenarios. We also demonstrate that leveraging the generated data can improve downstream performance. These results highlight the importance of accounting for causal structure when studying and evaluating adaptive learning methods, and establish a foundation for causally-aware evaluation in non-stationary environments.

---


### 38. [Quantum ROP: Using Quantum Algorithms for ROP Chain Selection in Exploit Construction](https://arxiv.org/abs/2609.25364)

**<font color=#1a73e8>作者：</font>** Carlos Benitez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The quantum computing threat to cybersecurity is nowadays predominantly framed around Shor's algorithm and its eventual capacity to break asymmetric cryptography. Beyond cryptanalysis, however, quantum computing may also enable other capabilities in offensive security. This work explores one such direction: the application of quantum combinatorial optimization to Return-Oriented Programming (ROP) gadget selection for exploit construction. We formulate gadget selection as a Quadratic Unconstrained Binary Optimization (QUBO) problem that captures individual gadget cost and inter-gadget register-clobbering interactions, and solve it using QAOA on real IBM Heron r2 hardware. Applied to a Linux kernel exploitation scenario, the QAOA-selected chain achieves privilege escalation to uid=0 with SMEP and SMAP active. Across eight Linux binaries and 16 benchmark instances, QAOA recovered the lowest-cost valid chain in 11 cases; in the remaining five, it did not recover the optimum, with the failures associated with excessive circuit depth on current limited hardware.

---


### 39. [Extending FunctionGemma for Practical On-Device Mobile Function Calling](https://arxiv.org/abs/2609.25373)

**<font color=#1a73e8>作者：</font>** Ali Rezagholizadeh, Soheila Samiee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED, a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories, including messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight control, and application management. We fine-tune the 270M model with TRL supervised fine-tuning under completion-only loss, producing an extended specialist and a combined model trained jointly with Google's MOBILEACTIONSGOOGLE. On MOBILEACTIONSEXTENDED, end-to-end accuracy improves from 29.3% for the base model and 17.2% for Google's Mobile-Actions variant to 76.5%. The combined model retains 76.5% on MOBILEACTIONSEXTENDED and reaches 82.3% on MOBILEACTIONSGOOGLE, down from the 90.3% of Google's Mobile-Actions specialist, representing an 8.0-percentage-point trade-off in return for doubling category coverage. We release the dataset, fine-tuned models, reproducible training/evaluation pipeline, and an Android demo, highlighting compact local function calling as a practical path towards low-latency and privacy-preserving mobile assistants.

---


### 40. [Sex Estimation from Footwear Outsole Impressions Using CNN Transfer Learning and Interpretable Image Statistics](https://arxiv.org/abs/2609.25386)

**<font color=#1a73e8>作者：</font>** Jinyi Niu, Ziyi Song, Weining Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Footwear outsole impressions are a common form of forensic pattern evidence, yet quantitative methods for estimating wearer attributes from these images remain relatively underdeveloped. We investigate binary sex estimation from footwear outsole impressions by comparing convolutional neural network (CNN) transfer learning with traditional feature-based classification. Using a publicly available outsole-impression dataset, we adopt a shoe-level training and test partition that keeps replicate scans of the same physical shoe together to reduce data leakage. We evaluate pretrained CNNs through end-to-end fine-tuning, frozen feature extraction followed by support vector machine classification, and hybrid feature fusion incorporating handcrafted, geometric, and metadata-derived descriptors. Fine-tuned CNNs achieve the strongest overall predictive performance and substantially outperform traditional classifiers trained on the manually specified descriptors alone, while frozen-feature approaches offer a less computationally demanding alternative. Exploratory analysis of low-dimensional CNN representations reveals associations with frequency threshold ratio, image contrast, and wavelet-based summaries, providing a connection between learned representations and measurable properties of outsole impressions. These findings suggest that CNN transfer learning captures discriminative information beyond the descriptors considered and offers a promising approach to footwear-based forensic screening. Further validation on independently collected and casework-like impressions is needed before operational use.

---


### 41. [Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing](https://arxiv.org/abs/2609.25397)

**<font color=#1a73e8>作者：</font>** M. Aslı Aydın  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The one-dimensional bin packing problem (1D-BPP) is a classical NP-hard combinatorial optimization problem with applications ranging from logistics and manufacturing to cloud resource management. Although deep reinforcement learning (DRL) has become a competitive paradigm for data-driven optimization, most learned packing methods target 2D and 3D variants, and intelligent learned solvers for 1D-BPP remain scarce. In this paper, we present a novel end-to-end, size-agnostic graph reinforcement learning framework for 1D-BPP. We formulate the packing process as a Markov decision process on an item-compatibility graph, serving as a structural knowledge representation in which every action merges two partial bins that fit together. A graph neural network actor-critic policy extracts relational features from this representation and is trained through reinforcement learning and decoded by stochastic beam search, enabling a single trained model to generalize zero-shot to instances of any size. We conduct a systematic empirical study across graph encoders, DRL algorithms, reward functions, training distributions, and hyperparameters. Evaluated zero-shot on the full BPPLIB benchmark against a constructive heuristic, a grouping genetic algorithm, and recent learned methods, our data-driven policy lowers the mean optimality gap of the constructive heuristic from 2.66\% to 2.31\%, with the largest gains on structured instances. Against learned baselines evaluated on the same benchmark, it attains a lower gap on most of the nine families and is far more stable across instance distributions. On the hardest benchmark family, it outperforms a state-of-the-art learned solver that relies on column generation and integer programming, while using no solver at all. A grouping genetic algorithm remains ahead overall, and we analyze where and why the residual gap arises.

---


### 42. [Robust Failure, Conservative Repair: Textual Knowledge Distillation from Cross-Model Failures](https://arxiv.org/abs/2609.25400)

**<font color=#1a73e8>作者：</font>** Andrew Ren, Haokun Liu, Chenhao Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Failure-based textual knowledge distillation aims to discover gaps in a model's knowledge by examining its task errors. The distilled knowledge can be useful for the reasoning of both this model ("source model") and other models. However, this transfer of knowledge may not be stable. We define a rule atom to be a standalone rule injected into a model's textual input at inference time. A rule atom can encode transferable task knowledge or model-specific reasoning patches that can confuse other models. Also, the injected rule atoms can be misapplied to unrelated cases, causing the model to incorrectly flip its answer based on irrelevant information. Building on a pipeline that distills training examples into task-specific cheat sheets that aid model reasoning, we examine when failure-derived rules can improve these cheat sheets. Our early experiment shows rule distillation from a single model's failures underperforms the baseline cheat sheet on non-source model families. This motivates Robust Failure, Conservative Repair (RFCR), a textual distillation procedure that derives rules from failures shared across models, sharpens their application boundaries using boundary cases, and abstains when no useful rule is found. On a 400-item BIG-Bench Hard task set, RFCR improves the baseline cheat sheets from 68.50% to 71.25% (+2.75 pp; 95% CI [+1.25,+4.50]) without performance degradation on previously correct cases. Ablations and cross-model diagnostics support that accuracy gains come from both new knowledge injection and strict rule-application control.

---


### 43. [From Offline Proxies to Online Decisions: A Layered Engagement Evaluation Framework for Conversational AI](https://arxiv.org/abs/2609.25408)

**<font color=#1a73e8>作者：</font>** Xuanyi Li, Vaskar Nath, Hossein Amirkhani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online A/B experiments are the decision standard for user engagement, but traffic and readout time limit how many conversational-AI changes can be tested. We ask whether an offline signal designed to be computable without treatment-arm user exposure agrees with the outcomes of those experiments. We contribute a reusable construction and diagnosis checklist that treats an offline proxy as a chain of three alignments: behavioral label to product outcome, learned classifier to candidate-assistant behavior, and aggregated offline signal to experiment effect. A companion evaluation protocol audits the whole composite by interval-aware decision agreement, which compares offline and online confidence intervals instead of point estimates, and by within-experiment ranking. The instantiation we evaluate comprises a fixed evaluation suite on which candidate behavior is scored, an engagement classifier trained to predict session/prompt level engagements, and a calibration layer mapping sample-level score differences to online model-level engagement deltas. We then report the audit: 489 paired offline-online contrasts (one candidate arm against its control) from 27 experiments on a deployed multi-turn assistant, spanning model checkpoints to system-prompt tuning. Our primary test uses the 113 contrasts from eight experiments that ran after the map was frozen: on these the composite reaches 81.1% F1, against 34.3% for the raw classifier score it is built on, and makes no wrong-direction calls where that raw score makes 31. Every offline prediction was computed before its experiment ran to prevent overfitting. The evidence supports using the composite to prioritize candidates before scarce experiment traffic is allocated---in our deployment of the experiment, selecting among training checkpoints and tuning system prompts.

---


### 44. [Beyond Task Performance: Lessons Learned from Evaluating an Exploratory VR Interaction Technique](https://arxiv.org/abs/2609.25414)

**<font color=#1a73e8>作者：</font>** Nevzat Umut Demirseren, Corey Pittman, Isayas Berhe Adhanom 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dense virtual environments present significant challenges for object selection and manipulation, motivating the development of novel interaction techniques. This paper presents RodCast as an exploratory case study to investigate explicit trajectory visualization for interaction in dense virtual environments. We conducted a within-subjects user study comparing RodCast with Go-Go Hand and FlowerCone across three representative interaction tasks using objective performance measures, subjective evaluations, and qualitative feedback. The results revealed that the proposed implementation incurred performance costs on more demanding manipulation tasks, while qualitative feedback suggested that participants attributed these challenges to the complexity of the bimanual control scheme. Additionally, subjective evaluations and qualitative feedback identified benefits in spatial awareness and target accessibility that were not fully reflected by conventional performance measures. Together, these findings highlight the importance of control simplicity in interaction technique design and emphasize that incorporating qualitative feedback into the evaluation process is essential for distinguishing implementation limitations from the potential of the interaction concept. Collectively, these lessons provide guidance for the design and evaluation of future interaction techniques.

---


### 45. [How Early Can You Tell? Early Eye Gaze Dynamics and Cybersickness Progression in Virtual Reality](https://arxiv.org/abs/2609.25422)

**<font color=#1a73e8>作者：</font>** Nevzat Umut Demirseren, Isayas Berhe Adhanom  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybersickness remains one of the primary barriers to prolonged and comfortable virtual reality (VR) use, yet the temporal development of cybersickness remains poorly understood because its onset and progression vary substantially across individuals. Eye tracking provides a continuous and unobtrusive measure of user behavior, making it well suited for investigating how users respond throughout VR exposure. However, existing work has mainly focused on aggregate gaze measures or post-exposure assessments, leaving the relationship between early eye-movement dynamics and discomfort progression underexplored. In this paper, we investigate whether early eye-movement dynamics characterize the subsequent progression of cybersickness. Using trajectories of fixation duration, fixation dispersion, saccade amplitude, saccade velocity, and gaze eccentricity computed over the first one to five minutes of VR exposure, we evaluate their association with subsequent discomfort progression and compare early gaze dynamics between participants with low and high post-exposure cybersickness severity. Our results show that early fixation dispersion is consistently associated with subsequent discomfort progression, whereas no significant differences are observed between cybersickness severity groups. These findings suggest that early fixation dispersion can characterize the progression of discomfort rather than the final cybersickness severity. Overall, this work provides new insight into the temporal relationship between early eye-movement behavior and cybersickness progression, contributing to the understanding of gaze dynamics during immersive experiences.

---


### 46. [Directional Total Variation-Regularized Implicit Neural Representations (DTV-INR) for Continuous Super-Resolution in Degraded Imaging Domains](https://arxiv.org/abs/2609.25429)

**<font color=#1a73e8>作者：</font>** Mahmoud Saeedi Kelishami  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce the Directional Total Variation-Regularized Implicit Neural Representation (DTV-INR), an advanced variational paradigm that synergistically integrates coordinate-driven implicit neural networks with an anisotropic, structure-tensor-informed total variation regularizer tailored for resolution-agnostic image super-resolution. Casting the continuous-to-discrete acquisition process into an ill-posed inverse problem framework, our formulation equips a SIREN-architected coordinate network with a dynamic Riemannian metric tensor field D(x). By leveraging its spectral decomposition, the proposed regularizer preferentially directs diffusion parallel to dominant structural contours while penalizing cross-edge dissipation, successfully circumventing the classical staircasing artifacts inherent to scalar total variation schemes. We rigorously prove the well-posedness of this formulation in H^1(Omega) by establishing the existence, uniqueness, and metric stability of the variational minimizer, and realize this via an alternating projected optimization algorithm that decouples network parameter tuning from adaptive tensor field updates. Comprehensive experiments conducted on clinical brain magnetic resonance imaging (MRI) and biomedical transmission electron microscopy confirm substantial quantitative and qualitative improvements, yielding PSNR enhancements reaching +5.05 dB over baseline unregularized INRs and +1.71-2.85 dB over isotropic TV-INR across continuous (non-integer) upsampling factors, alongside remarkable noise robustness up to sigma_eta = 0.10 and monotonic preconditioned convergence behavior.

---


### 47. [Predictive Uncertainty for Neural CAE Surrogates](https://arxiv.org/abs/2609.25430)

**<font color=#1a73e8>作者：</font>** Kaustubh Tangsali, Mohammad Amin Nabian, Kelvin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates can substantially accelerate computer-aided engineering (CAE) workflows, but their use in design requires uncertainty estimates that remain meaningful across varying geometries, spatial prediction fields, and engineering quantities of interest. We investigate how established uncertainty quantification (UQ) approaches behave when adapted to geometry-conditioned neural surrogates. We compare one closed-form and two sampling-based approaches-a Gaussian process (GP)-based method, concrete Monte Carlo (MC) dropout, and deep ensembles-and evaluate them on three large, industry-relevant CAE datasets for external aerodynamics and crash dynamics.
We examine whether predicted uncertainties have credible magnitudes, identify locations with larger prediction errors, respond to unfamiliar inputs, and remain informative for derived engineering quantities. On the DrivAerStar dataset, where all three methods are compared, each generally assigns higher uncertainty to locations with larger prediction errors, and validation-based rescaling brings interval coverage close to nominal on a disjoint in-distribution test set. Results on AirFRANS and automotive crash also show useful error ranking and interval estimates, but the relative performance of the methods changes with the dataset and evaluation criterion. UQ methods and evaluation metrics should therefore be selected based on the intended downstream CAE decision.

---


### 48. [Lightweight Ranking Heads: Accelerating Multi-Task Experimentation in Production Recommender Systems](https://arxiv.org/abs/2609.25433)

**<font color=#1a73e8>作者：</font>** Sanjay Surendranath Girija, Aniruddh Nath, Li Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern production-scale recommender systems rely on complex, multi-task ranking models. Introducing new prediction tasks into these massive systems often causes bottlenecks - it risks negative task conflicts with existing tasks, and can lead to long development and experimentation cycles due to the expensive retraining of backbone models and downstream models or tuning of reward combination formulas. To address the critical challenge of slow experimentation velocity, we introduce the Lightweight Ranking Heads (Light Heads) framework. Designed for continuous online learning environments, Light Heads enable the dynamic injection of new tasks into existing multi-task ranking models, effectively obviating the need for model cold-starting and retraining of backbone models. By utilizing stop-gradients and stateless daily training, this design strictly isolates new tasks, mitigating the risk of adverse task conflicts. Crucially, this framework uses a centralized configuration that allows Light Heads to be added to multiple models simultaneously, unblocking faster training data generation and co-training of downstream models. Successfully deployed at YouTube scale, this approach reduces the iteration cycle for multi-task experimentation from several weeks to days. In this paper, we detail the system architecture, analyze the training dynamics of stateless cold-started heads, compare their performance to full heads, and demonstrate how Light Heads have enabled the rapid A/B experimentation and deployment of new ranking tasks that yield measurable production value.

---


### 49. [Mining Legal Arguments in U.S. Corporate Case Law](https://arxiv.org/abs/2609.25441)

**<font color=#1a73e8>作者：</font>** Luis Brena, William Jurayj, Gregory Deyesu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal argument mining supports passage classification, retrieval, and argument completion. This work introduces an expert-annotated dataset of 42 U.S. federal tax opinions on corporate reorganizations under I.R.C. §368. To our knowledge, it is the first expert-annotated, tree-structured argument corpus for this domain. Explicit spans receive one of five functional labels: Rule, Analysis, Conclusion, Background Facts, and Procedural History. Rule, Analysis, and Conclusion spans can be linked into directed support trees, while Background Facts and Procedural History serve a contextual function. The corpus provides span-based, sentence-based, flat, and tree-structured representations. Agreement analysis shows that functional node labels are more reliable than directed support edges and implicit intermediate conclusions. Directed-path agreement is stronger than direct-edge agreement, which indicates that broad reachability is more stable than exact local decomposition. Classification experiments show that functional labels are learnable under case-disjoint evaluation. Retrieval experiments show that supervised fine-tuning improves within-case retrieval. However, cross-case generalization remains weak. The dataset supports legal passage classification and provides a conservative benchmark for structured argument mining in U.S. federal tax case law.

---


### 50. [ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes](https://arxiv.org/abs/2609.25443)

**<font color=#1a73e8>作者：</font>** Zexun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Moving authorization earlier can shorten an agent's dispatch boundary without removing authorization work. It can also admit an action whose payload, authority, or relevant state has changed. ZeroGate separates exact-action approval from durable local admission: an issuer signs a short-lived ActionPass, and a trusted runtime adapter reconstructs the final action before a local gate checks its binding and consumes its nonce. A SQLite transaction couples nonce consumption, applicable quota updates, and an admission receipt. We state a conditional decision-preservation proposition: successful local admission implies that a specified synchronous policy would authorize the same action at the admission point, provided approval is sound, all policy dependencies are represented and current, observations are faithful, and consumption is atomic. The implementation alone establishes neither current-world freshness nor exactly-once remote effects. Evaluation separates authored semantic fixtures, controlled concurrency and crash experiments, and an Azure Blob study comparing synchronous and prepared execution through the same issuer and gate. Both modes mint an exact-action pass; lifecycle latency includes preparation and prepared-batch dwell. Across 4800 cloud attempts, prepared worker-admission-to-dispatch p95 ranges from 9.802 to 11.374 ms, versus 25.018 to 334.000 ms synchronously, across the tested concurrency levels. Prepared mean complete lifecycle is longer at every level: the boundary improvement is not a net speedup. The contribution is an explicit revalidation contract, a durable reference boundary, and an auditable comparison of where authorization cost is paid, not a new cryptographic primitive or a universal performance frontier.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
