# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 201. [Graph Classification via Network Usable Information: From Representation Evaluation to Structure Selection](https://arxiv.org/abs/2607.03587)

**<font color=#1a73e8>作者：</font>** Abdullah Shaik, Anwar Said  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose NetinfoGC, a framework for graph classification that extends the Network Usable Information (NUI) paradigm to graph-level learning. Unlike conventional graph neural network approaches that rely on end-to-end training of black-box embeddings, NetinfoGC constructs a family of permutation-invariant graph representations derived from propagation-based mechanisms and classical structural descriptors, including graph centrality measures.
To evaluate representation quality, we introduce a training-free NUI estimation procedure based on clustering consistency with ground-truth labels, providing a proxy for task-relevant information without supervised learning. We further exploit the same representations using sparse-group LASSO regularization, enabling automatic selection of informative structural descriptors while suppressing redundant ones.
Experiments on benchmark datasets show that classical centrality measures are highly competitive with learned propagation-based representations, and in several cases yield superior performance. Moreover, we observe a strong correlation between estimated NUI and downstream classification accuracy, validating NUI as an effective measure of representation utility.
Overall, NetinfoGC provides a unified and interpretable framework for evaluating and exploiting graph representations without requiring end-to-end neural training.

---


### 202. [Vision Non-Causal Trapezoidal Mamba: Eliminating Directional Scanning in Vision SSMs with Second-Order Dynamics](https://arxiv.org/abs/2607.03589)

**<font color=#1a73e8>作者：</font>** Anvitha Ramachandran, Dhruv Parikh, Haoyang Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have emerged as an alternative to Vision Transformers, yet most vision SSMs inherit directional token scanning from causal sequence modeling. While effective for sequential data, directional scanning introduces spatial bias and orientation-sensitive representations. We present Vision Non-Causal Trapezoidal Mamba (VNCT), a second-order non-causal vision SSM that enables all image tokens to interact in a single pass, eliminating direSctional scanning and achieving low single-image inference latency. VNCT exhibits more orientation-robust representations, showing reduced performance degradation under image rotations and flips, while improving Boundary IoU by up to 3.7 points, leading to more accurate boundary preservation and object localization. Across ImageNet-1K classification, COCO object detection and instance segmentation, and ADE20K semantic segmentation, VNCT consistently outperforms both directional-scanning vision SSMs and first-order non-causal SSMs. These results show that directional scanning is unnecessary for high-performance vision SSMs and that second-order non-causal state-space modeling offers a simple, efficient, and robust alternative for visual recognition.

---


### 203. [They Infer What You Meant: Models Represent Communicative Intent More Reliably Than They Act On It](https://arxiv.org/abs/2607.03598)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a person shares something with a language model, the model often answers the surface of the message rather than what the sender was doing by sending it: share a finished project and it critiques the code; share a raw late-night line and it runs a wellness check. We treat the sender's communicative intent, the Gricean what-was-meant, as a first-class interpretability object, and show the failure is one of readout on top of a robust representation. A linear probe decodes the sender's intent, whether they want a thing recognized or evaluated, from a model's default-pass hidden states, cleanly and surface-independently, across six models and four families and in the base checkpoints. The representation generalizes further, to intent that is only pragmatically inferred, and to a second, lexically clean intent (support versus help). The behavioral half of the story, and every causal test, is established on the recognize/evaluate contrast, where what varies is whether the default output acts on the intent. The readout lags the representation in depth within a model (the intent is decodable several layers before it drives the output); across models, which ones act on it by default is model-specific, an observed stratification (three of six show the failure) that we do not read as a scaling law. Where the gap is open, a direction closely tied to the representation, the discriminative direction at a searched-for layer, is a causal handle: steering it recovers the intended behavior, as well as an explicit instruction does and with no prompt at all. This direction is near-orthogonal to the feedback-offering axis, so it routes a represented intent rather than a generic feedback knob, though at the recovery dose the routed intent can override an explicit request. We support each link with controls against obvious deflations and report the nulls as plainly as the confirmations.

---


### 204. [Observer-Quotient Security: Composable Leakage Bounds for Hidden State Continuations](https://arxiv.org/abs/2607.03610)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Levent Sarioglu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Observer-quotient security studies interactive cryptographic systems whose security depends on what an admissible observer can distinguish across transcripts, leakage traces, and hidden implementation continuations. The paper defines observer-indexed experiments with session identifiers, adaptive schedulers, oracle forwarding, simulators, ideal quotient functionalities, and nonuniform environments, and proves a real/ideal emulation theorem in which sequential morphism defects add, parallel defects obey a product-TV bound, and adaptive observer choice is absorbed by an explicit wrapper construction. The resulting advantage bound is indexed by $\delta_{\mathrm{obs},t}$, $\delta_{K,t}$, $\delta_{\mathrm{post},t}$, $\delta_{\mathrm{sim},t}$, $\eta_t$, and the residual floor $\rho_T(\mathbb E Z_T)$. The framework is instantiated for IND-CPA encryption with timing leakage, deterministic encryption with entropy ledgers, and finite-state side-channel refinement under transcript, timing, cache, power, EM, and profiled observers. The optimization/control component identifies hidden continuations with observability kernels, treats sensor redesign as quotient refinement, and converts dissipativity, PL-type rates, and ISS residual bounds into concrete reductions in distinguishing advantage. Ancillary code and synthetic data reproduce the finite-state leakage audit and LTI observer-design benchmark.

---


### 205. [SAF3R: Dynamic Sparse Attention for Feed-Forward 3D Reconstruction Transformers](https://arxiv.org/abs/2607.03612)

**<font color=#1a73e8>作者：</font>** Jianing Deng, Yuanzhe Li, Jialu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction (F3R) transformers have recently achieved remarkable success. However, scaling them to long image sequences remains challenging, as the quadratic complexity of cross-view global attention quickly becomes the dominant computational bottleneck. While recent efforts attempt to improve efficiency through compressed or sparse attention, they fail to fully exploit the inherent sparsity and dynamic behavior of global attention. In this work, we present a comprehensive analysis of global attention across multiple F3R transformers and reveal that attention patterns are highly heterogeneous, dynamic, and extremely sparse across layers and attention heads. Motivated by these findings, we propose SAF3R, a training-free dynamic sparse attention framework tailored to F3R transformers. SAF3R integrates tailored sparse attention mechanisms with offline head profiling and an efficient online adaptation strategy to match input-dependent attention behaviors. Extensive experiments demonstrate that SAF3R achieves high sparsity ratios while preserving camera pose estimation and 3D reconstruction quality, translating into substantial end-to-end speedup on F3R transformers compared to existing methods. Code is available at this https URL

---


### 206. [Implicit Bias of SGD in Multivariate ReLU Networks: Effective Width Collapse](https://arxiv.org/abs/2607.03613)

**<font color=#1a73e8>作者：</font>** Shuang Liang, Tom Jacobs, Guido Montúfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the implicit bias of noisy stochastic gradient descent in training wide two-layer ReLU networks for multivariate regression. In a mean-field regime, the training dynamics are approximated by a Wasserstein gradient flow that converges to a unique stationary measure. We characterize the structure of this stationary measure and the predictor it represents. We show that, despite the network being infinitely overparameterized, the learned predictor admits an effectively finite representation: the input weights and biases align along finitely many directions, leading to an effective width collapse. In particular, the solution function is continuous piecewise affine, with affine regions determined by the cells of a finite hyperplane arrangement. The number of learned directions, and hence hyperplanes, is bounded above by $2\mathcal{P}-1$, where $\mathcal{P}$ denotes the number of linear dichotomies realizable on the training inputs. We further establish a non-redundancy property of the learned representation by proving that each learned direction induces a unique ternary activation pattern on the training data. Consequently, the complexity of the learned predictor is governed by the combinatorial geometry of the training data.

---


### 207. [IDEAL-Bench: Indoor Dataset and Evaluation suite for Analyzing 3D Layout reasoning](https://arxiv.org/abs/2607.03614)

**<font color=#1a73e8>作者：</font>** Yuening Cai, Junwei Zhou, Youran Qu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial question answering is the dominant paradigm for evaluating spatial intelligence in Vision-Language Models (VLMs), but it leaves a complementary axis of spatial competence under-evaluated: holistic 3D layout inference, which predicts every visible object's pose and extent from a single image in a structured form. To this end, we introduce IDEAL-Bench, an evaluation suite that requires VLMs to predict structured 3D layouts on photorealistic indoor scenes across 10 room types, scored along five numerical dimensions and a perceptual render-and-compare protocol. By operating on semantically realistic scenes with full asset substitution under controlled lighting and viewpoint, IDEAL-Bench moves beyond CLEVR-style simple geometric primitives so that any image-space discrepancy reflects spatial reasoning alone. The benchmark is built on IDEAL-Scenes, a procedurally generated dataset of 1,000 re-renderable Blender environments with ground-truth layouts. Evaluating 15 prominent VLMs reveals three findings: the task remains substantially unsolved, with the strongest model reaching only 62.1/100 overall; all models exhibit a sharp asymmetry between object recognition and geometric regression, indicating that current VLMs are trained to describe scenes rather than to measure them; model rankings partially diverge from those on QA-based and primitive-reconstruction benchmarks: top-tier consensus holds, but mid-tier rankings shift substantially. Collectively, these findings establish IDEAL-Bench as a diagnostic suite, targeting the geometric and structural competencies that QA-based evaluation cannot surface, and paving the way towards more rigorous evaluation of spatial intelligence in next-generation VLMs. Together, these findings position IDEAL-Bench as a principled diagnostic for whether future VLMs achieve genuine spatial understanding rather than linguistic approximations of it.

---


### 208. [Reflected Schrödinger Bridge Matching](https://arxiv.org/abs/2607.03626)

**<font color=#1a73e8>作者：</font>** Marcus Häggbom, Viktor Nilsson, Pierre Nyquist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative modeling have enabled the efficient computation of Schrödinger bridges (SB) in high-dimensional settings by leveraging partially simulation-free training methods inspired by flow matching. However, these have not covered SBs with reflecting dynamics, a useful model choice with built-in guarantees that generated samples stay in the data domain. Existing alternatives for reflected SBs instead rely on more complex training based on forward--backward SDE theory, requiring expensive higher-order derivatives and sampling entire paths during training. In this article, we introduce a partially simulation-free framework that allows reflected SBs to be trained similarly to flow matching, using a new sampling method and regression target. We demonstrate our results by coupling pairs of well-known high-dimensional image datasets. Using reflected dynamics incurs negligible additional wall-clock time during both training and inference while maintaining or slightly improving generative performance.

---


### 209. [Swarm-Driven Multi-Agent Reasoning for Smart City Security](https://arxiv.org/abs/2607.03628)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi, Kawser Wazed Nafi, Carol Fung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern smart cities are interconnected cyber-physical ecosystems where heterogeneous devices exchange data and control commands. Coordinated attacks may appear as weak and distributed indicators, including low-rate scanning, abnormal credential use, protocol misuse, or delayed lateral movement, with each signal remaining below local alert thresholds. Therefore, smart-city security is not only an anomaly detection task but also a reasoning task under uncertainty, partial observability, and adversarial manipulation. This work presents TPSC-Sec, an LLM-based multi-agent approach for stable security reasoning in smart cities. TPSC-Sec decomposes analysis across specialized agents that inspect traffic behavior, protocol interactions, identity usage, and temporal attack progression. Their independent threat hypotheses are aggregated by the proposed Threat-Pheromone Swarm Consensus mechanism, which reinforces supported hypotheses, suppresses contradictions, and preserves temporal consistency, thereby driving competing interpretations toward a stable collective decision. We further introduce Adaptive Verified TPSC, which adds verification-aware calibration, context-sensitive weighting, and disagreement-adaptive control to reduce unsupported LLM outputs and reasoning inconsistency. Experiments over 500 runs show that TPSC-Sec achieves a high consensus acceptance rate of 0.97 plus or minus 0.02, hypothesis-support concentration above 0.99, a consensus margin of 2.08 plus or minus 0.21, low aggregate risk of 0.23 plus or minus 0.04, high inter-agent agreement of 0.82 plus or minus 0.06, and strong support-quality correlation of r equals 0.93. Adaptive agent selection reduces the number of active agents by 50 percent while improving system fitness by 11.6 percent. These results demonstrate robust, interpretable, and efficient security reasoning for adversary-resilient smart-city environments.

---


### 210. [Rotation-Optimal Noncommutative Prefix Scans in Bit-Reversed Homomorphic Layouts](https://arxiv.org/abs/2607.03631)

**<font color=#1a73e8>作者：</font>** Anis Bkakria, Madicke-Diadji Mbodj, Mawloud Omar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Packed homomorphic encryption evaluates slotwise operations in parallel, but nonlocal communication is realized by cyclic rotations whose cost depends on the physical slot layout. We study ordered prefix computation on $n=2^m$ elements of an associative, possibly noncommutative monoid stored in bit-reversed order. A direct transported-predecessor scan uses $m\cdot(m+1)/2$ rotations because one logical shift decomposes into several cyclic displacement classes. We introduce a replicated-aggregate invariant: every slot of an aligned logical block stores the same complete block aggregate. Since these copies are semantically interchangeable, one global rotation per level supplies each slot with a valid sibling aggregate, without reaching the exact logical partner. The resulting inclusive or exclusive scan uses $m$ rotations, depth $m$, two live state vectors, and at most $2\cdot m-1$ packed monoid compositions.
In a model where all non-routing operations are slotwise and every cyclic rotation invocation is counted, these bounds are exact: $D^\star(m)=R^\star(m)=m$. Equality is rigid: the $m$ offsets contain exactly one representative of each $2$-adic valuation. With at most $K$ directly keyed offsets, we prove a product lower bound and an exact frontier $K\cdot(2^{m/K}-1)$ whenever $K$ divides $m$. We instantiate the exclusive scan for radix carry and borrow in bit-reversed \CKKS slots, avoiding layout restoration and the final logical-predecessor shift. In our implementation at $m=7$, the replicated scan reduces the direct bit-reversed baseline from $28$ to $7$ rotations, lowers evaluation-key storage by $70.0\%$, lowers peak heap usage by $63.9\%$, and improves isolated scan latency by $19.9\%$. In a depth-$5$ downstream pipeline, retaining six additional modulus levels avoids one bootstrap and gives a mean paired speedup of $4.31\times$ with $95\%$ confidence interval $[3.69,4.92]$.

---


### 211. [Probing Identity-Specific Motion Signatures: A Controlled Diagnostic Study](https://arxiv.org/abs/2607.03633)

**<font color=#1a73e8>作者：</font>** Yingtie Lei, Fangxun Liu, Baicheng Wu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity recognition (e.g., person, animal re-identification) has traditionally relied heavily on static appearance cues. Yet motion--consistent, individual-specific dynamics--can provide a complementary and potentially more robust signature, especially when appearance is weak or variable. This raises a fundamental question: when identity-specific motion cues are clearly present, to what extent do modern video models use them for recognition? To investigate this question, we conduct a systematic diagnostic study and introduce BALLER120, a controlled benchmark of 120 professional basketball players performing free-throws. By focusing on the same multi-phase action across individuals, BALLER120 reduces action-level variation and identity-correlated acquisition biases, enabling fine-grained analysis of identity-specific kinematic patterns. We find that modern video models can predict identity accurately from RGB videos, but often rely on static appearance cues such as faces and jersey regions, even when informative motion cues are available. Strikingly, when appearance is suppressed through silhouette-only or skeleton-only inputs, the same model architectures shift toward motion micro-patterns (e.g., foot placement and elbow bending). Despite containing less visual information, appearance-suppressed representations achieve competitive accuracy and stronger robustness to appearance shifts. Our qualitative analyses further show that appearance-suppressed models attend to distinctive motion patterns across individuals. Overall, our study demonstrates that identity-specific motion signatures are present, informative, and learnable, but modern video models may overlook them in favor of easier static shortcuts unless appearance cues are explicitly suppressed.

---


### 212. [The Role of Rigor in Artificial Intelligence](https://arxiv.org/abs/2607.03634)

**<font color=#1a73e8>作者：</font>** Timothy Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has achieved extraordinary capabilities despite lacking many of the conceptual and scientific foundations associated with mature disciplines. Unlike traditional sciences, where reliable technology typically emerges from theoretical understanding, modern AI has progressed largely through performance-driven iteration and "alchemical" experimentation. This tension motivates a systematic analysis of AI through the lens of rigor. We introduce a three-part framework consisting of conceptual rigor (clarifying foundational concepts), epistemic rigor (establishing scientific understanding), and operational rigor (ensuring reliable performance and deployment). Using this framework, we analyze competing conceptions of intelligence and understanding, the strengths and limitations of the empirical approach to deep learning, the power and pitfalls of benchmarks, and the obstacles to theory development posed by modern AI systems. We argue that the distinctive trajectory of AI arises from how forms of rigor interact across paradigms, resulting in the primacy of operational rigor in modern deep learning. This perspective helps explain both AI's rapid advances and its persistent uncertainties, while clarifying the challenges involved in transforming AI into a mature science and reliable technology.

---


### 213. [Revealing Hidden Model Behaviors with Task-Specific Self-Reports](https://arxiv.org/abs/2607.03640)

**<font color=#1a73e8>作者：</font>** Taras Kutsyk, Bartosz Zieliński  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning can give a language model a hidden behavior--it may give false answers under a narrow condition, or give harmful advice only when a prompt touches a particular topic. We introduce the Stabilized Adapter for self-Report (SAR), a lightweight LoRA adapter that makes a fine-tuned model describe its own hidden behavior in plain language, using only the model and the dataset it was trained on. Across seven implanted behaviors (plus a no-behavior control), SAR detects the hidden behavior in every one--even when the model has generalized into broad misalignment that the training data alone does not predict. Introspection Adapters (IA), the closest existing baseline, detects some behaviors from our suite but misses others entirely--and where it misses, it hallucinates, consistently reporting wrong behaviors. SAR retains positive signal on every setting where IA fails and halves the rate of hallucinations. This makes it much easier for practitioners to audit their models and obtain reliable answers to "what did my model actually learn?" type of questions.

---


### 214. [ClinOCR-Bench: A Comprehensive Clinical Scanned Document Dataset for Optical Character Recognition Model Evaluation](https://arxiv.org/abs/2607.03650)

**<font color=#1a73e8>作者：</font>** Enshuo Hsu, Jin Zhou, Kirk Roberts  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting textual information from scanned medical documents, such as external laboratory reports and manually filled forms, has been a major challenge in modern electronic health records (EHRs). Recent advancements in vision language models (VLMs) have shown great promise over traditional OCR tools. However, at this point, most clinical OCR studies were conducted on private, institutional data. To our knowledge, there are few publicly available datasets for evaluating OCR models in the clinical domain. Furthermore, common scanning artifacts that undermine OCR performance are not reflected in those datasets, leaving a systematic evaluation unfeasible. Therefore, we release a publicly available, realistic-looking OCR benchmark dataset, ClinOCR-Bench, with 384 scanned images across 6 subsets: Normal, Handwriting, Poor Quality, Rotation, Tables, and Mix-artifacts. ClinOCR-Bench features: 1) diverse document types and layouts, 2) full coverage of common EHR scan artifacts, 3) protected health information-free, 4) template-aware train/test split, and 5) adequate sample size for OCR benchmarking. Baseline OCR performance was evaluated using state-of-the-art open-weight and proprietary VLMs. The dataset and documentation are available on GitHub (this https URL).

---


### 215. [ThreatVisionAI: A Hybrid CNN-ViT Framework for Image-Based Malware Classification](https://arxiv.org/abs/2607.03653)

**<font color=#1a73e8>作者：</font>** Allyson Taylor, Prashanth BusiReddyGari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional malware detection methods struggle to generalize to obfuscated or previously unseen threats. This paper introduces ThreatVisionAI, a hybrid malware family classification framework that integrates a raw-image CNN, a wavelet-based CNN, and a Vision Transformer (ViT) to capture complementary spatial, frequency-domain, and global relational features in malware images. The wavelet-based CNN captures multi-scale frequency information that helps distinguish closely related families, while the ViT branch models long-range dependencies across the image. Evaluated on the Malimg dataset, ThreatVisionAI achieves 98.01% accuracy and a weighted F1 score of 0.9742, with wavelet-domain features providing measurable gains on minority and visually similar families. These results confirm that frequency-aware and transformer-based representations improve image-based malware family classification.

---


### 216. [Phase-Preserving Trimodal Transformer for Tropical Forest Biomass Estimation Using Optical and PolInSAR Data](https://arxiv.org/abs/2607.03663)

**<font color=#1a73e8>作者：</font>** Luiz Felipe Parente Santiago, Rosiane Rodrigues de Freitas, Daniel Rodrigues dos Santos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The accurate estimation of Above-Ground Biomass (AGB) in mature tropical forests remains a critical challenge in remote sensing, primarily due to the saturation of Synthetic Aperture Radar (SAR) signals in high-density areas and persistent cloud cover affecting optical imagery. To overcome these physical limitations, we propose the Trimodal Coherent Co-attention Transformer (TCCT), a physics-informed deep learning architecture. The TCCT natively fuses optical surface reflectance (Landsat-5) with complex-valued Polarimetric SAR Interferometry (PolInSAR) data from both P and L bands. Unlike traditional fusion methods, our architecture employs complex-valued encoders to preserve spatial phase coherence, coupled with a dynamic co-attention mechanism that acts as an adaptive gating module, reducing the weight of cloud-corrupted optical pixels and shifting reliance to microwave phase data. We also derived a localized spatial allometric calibration model via Levenberg-Marquardt optimization, tailored to the specific wood density of the Paracou region in the Amazon basin. Evaluated using a two-stage protocol, the TCCT first underwent a rigorous 5-fold cross-validation to establish robust global weights (achieving a global RMSE of 4.19 m). Subsequently, following a localized spatial fine-tuning phase over 200 epochs, the model attained an absolute RMSE of 3.78 m and an $R^2$ of 0.33 for Canopy Height Models (CHM), outperforming standard Random Forest, CNN, and Vision Transformer baselines. Our ablation study confirms that preserving phase coherence mitigates deep-canopy signal saturation. When converted to AGB, the fine-tuned TCCT map yielded a Relative RMSE (rRMSE) of 4.51% in dense forest areas above 50 Mg/ha. By meeting the European Space Agency (ESA) BIOMASS mission requirement of less than 20% error, the TCCT provides a robust framework for continuous carbon stock mapping in tropical biomes.

---


### 217. [A Structural Interpretation of GELU and Threshold-Transmission Activations via the First-Order Loss Function](https://arxiv.org/abs/2607.03664)

**<font color=#1a73e8>作者：</font>** Roberto Rossi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Gaussian Error Linear Unit is usually motivated as the expected output of an input-dependent stochastic Bernoulli gate. This work gives a complementary interpretation based on the Gaussian complementary first-order loss function: GELU is the signal-transmission term of the expected surplus of a hard linear gate with a Gaussian random threshold. This view separates loss accounting from forward signal transmission and generalises to a threshold-transmission family that includes ReLU, GELU, SiLU/Swish, and hard swish as special cases. The uniform-threshold case recovers a hard-swish-like compact piecewise-polynomial gate with an explicit threshold-width parameter, yielding fixed- and learned-width variants. Controlled experiments on compact vision and language models show that calibrated or learned uniform-threshold gates are consistently competitive with GELU, ReLU, and SiLU/Swish, improve over them in most tested settings, and use the finite transition region nontrivially.

---


### 218. [Validation-Induced Shapley Shifts: How Validation Structure Distorts Data Valuation](https://arxiv.org/abs/2607.03675)

**<font color=#1a73e8>作者：</font>** Yinan Shen, Ziao Yang, Hongfu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley values are widely used to attribute value to training data based on their marginal contribution to performance on a validation set. Existing practice often assumes these values are stable once the training data and model are fixed. In this work, we uncover a systematic vulnerability: even modest changes to the validation set, such as introducing noises, cause directional shifts in Shapley distributions. As noises are added, Shapley values of training samples compress toward zero. We trace this to a noise-induced neighborhood reshuffling effect: perturbations alter the local rank order between validation and training samples, flattening the valuation landscape. Using the KNN-Shapley framework, we show through synthetic and real data that these shifts are consistent and reproducible. Our findings challenge the assumption of Shapley stability and reveal a new axis of fragility in data valuation. We propose normalization and boundary-aware validation strategies to mitigate these distortions and enable more robust, interpretable valuation in machine learning marketplaces.

---


### 219. [Rethinking AI-Generated Text Detection: A Strong Baseline and the Distribution-Shift Problem That Remains](https://arxiv.org/abs/2607.03680)

**<font color=#1a73e8>作者：</font>** Zhuoer Shen, Mingyi Wang, Shaofeng Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent AI-generated text detection work often introduces a new benchmark together with a specialized detector tailored to it. We revisit this practice from a baseline-first perspective. Across several benchmarks, we show that a plain, fully fine-tuned RoBERTa matches or exceeds the specialized detectors those benchmarks are built around. This suggests that much of the recent architectural complexity is not what drives strong in-distribution detection. The remaining challenge is the distribution shift. The same strong baseline degrades sharply when the topic domain or generating model changes at test time, and simply adding more source data does not close the gap. We identify a key failure mode: under distribution shift, the detector can assign high-confidence machine labels to human-written text from unseen domains. We then study two lightweight domain adaptation methods to address this problem: $K$-shot adaptation with first-order MAML over LoRA adapters, and a per-sample confidence-weighted ensemble built on top of the adapted detector. Overall, our results suggest that progress in AI-generated text detection should be measured not only by in-distribution performance, but also by robustness under distribution shift.

---


### 220. [Annotating Korean adnominal ending constructions in corpus data: Beyond relative-clause identification](https://arxiv.org/abs/2607.03681)

**<font color=#1a73e8>作者：</font>** Jungyeul Park, Chulwoo Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Korean adnominal ending \texttt{ETM} occurs in diverse noun-modifying constructions, including relative-clause-like modifiers, adjectival and copular forms, bound-noun constructions, and lexicalized expressions. This paper argues that \texttt{ETM} is not a direct marker of relative-clause structure, but a morphological exponent shared by several adnominal constructions. We propose a corpus-based typology that distinguishes these constructions using predicate type, auxiliary structure, argument-structural compatibility, head-noun restriction, and lexicalized patterns. We operationalize the typology as a construction-sensitive annotation layer for the KLUE dependency treebank, implemented through an ordered rule-based procedure and evaluated by manual validation. Productive relative-clause-like uses account for 39.4\% of the analyzed instances; the remainder consists mainly of adjectival, copular, bound-nominal, modal, temporal, and collocational constructions. The findings show that Korean relative-clause-like modification cannot be identified from adnominal morphology alone.

---


### 221. [PIEFS: Physics-Informed Eigenfunction Features with Learnable Scaling](https://arxiv.org/abs/2607.03692)

**<font color=#1a73e8>作者：</font>** Varvara Nazarenkko, Timur Lidzhiev, Alexander Tarakanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral methods are widely used to construct representations from the geometry of data, but they often rely on a fixed kernel, graph Laplacian, or manually selected feature scaling. We propose Physics-Informed Eigenfunction Features with Learnable Scaling (PIEFS), a supervised neural representation-learning framework with a spectral inductive bias, based on a modified Dirichlet energy. In PIEFS, scalar coordinate maps are trained under empirical Gram orthogonality, a supervised linear readout, and a Dirichlet penalty in which the input gradient is transformed by a learnable metric $A(x)=\Lambda(x)U(x)$. The diagonal factor $\Lambda(x)$ controls anisotropic scaling, while the orthogonal factor $U(x)$ is parameterized by a structured product of Givens rotations. This construction yields task-adaptive Dirichlet-regularized coordinates rather than eigenfunctions of a fixed supervision-independent operator. Experiments on synthetic, tabular, and image-based benchmarks study the effect of identity, diagonal, and rotation-scaling metrics, and compare the resulting coordinates with classical baselines and NeuralEF. The results support PIEFS as a compact supervised spectral representation method and identify optimization stability, validation on explicit operator eigenproblems, and richer metric parameterizations as the main directions for future work.

---


### 222. [Robust Feasible Route Construction through Collaborative Partition Optimization](https://arxiv.org/abs/2607.03694)

**<font color=#1a73e8>作者：</font>** Oguzhan Karaahmetoglu, Hyong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale Capacitated Vehicle Routing Problems (CVRPs) are commonly solved by partitioning customers into smaller routing problems that can be optimized independently. While this substantially reduces computational complexity, independently constructed routing solutions may leave some customer demand unserved even when sufficient resources exist elsewhere in the fleet. We present Collaborative Routing Constructors (CoRC), a routing framework that enables independently solved subproblems to exchange customers and vehicles during optimization rather than relying solely on a fixed partition or a subsequent global re-optimization stage. Computational experiments on AGS benchmark instances and synthetic instances containing up to 200,000 customers compare CoRC against independent routing, post-routing global re-optimization, and state-of-the-art, end-to-end routing frameworks. Across all evaluated partitioning strategies, CoRC consistently constructs feasible routing solutions where competing partition-based methods do not. Furthermore, it remains effective on problem instances for which the evaluated end-to-end routing frameworks did not produce solutions under the same computational budget. These results demonstrate that collaboration between routing subproblems provides a robust and scalable approach for feasible large-scale route construction.

---


### 223. [IPDiff: Diffusion-driven ORSI Salient Object Detection with Information Reconstruction and Multi-Prior Guidance](https://arxiv.org/abs/2607.03696)

**<font color=#1a73e8>作者：</font>** Gongyang Li, Zhen Bai, Runmin Cong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Salient Object Detection in Optical Remote Sensing Image (ORSI-SOD) methods mainly adopt the static inference strategy, which uses fixed trained model parameters for saliency inference in the testing phase. This means that even if the generated saliency map has errors, it cannot be further optimized. In this paper, we propose the novel IPDiff, a Diffusion-driven ORSI-SOD method with Information Reconstruction and Multi-Prior Guidance. We build IPDiff based on a unique dynamic optimization strategy, which endows IPDiff with the ability to iteratively optimize saliency maps with a dynamic parameter. Specifically, we formulate ORSI-SOD as a conditional diffusion problem in IPDiff. IPDiff first extracts informative conditional priors from ORSIs, including the saliency prior and the hierarchical priors, in the prior network with the assistance of the information reconstruction-driven attention module. The saliency prior can provide positional information of salient objects, while the hierarchical priors can provide specific detail and semantic information of salient objects. Under the guidance of these priors, IPDiff then iteratively denoises random noise as the timestep dynamically changes in the denoising network, generating saliency maps that are close to ground truths. Notably, we simultaneously supervise IPDiff in both spatial and spectral domains through a hybrid loss function to achieve efficient network training. Comprehensive experiments on public ORSSD, EORSSD, and ORSI-4199 datasets demonstrate that our proposed IPDiff achieves the best performance compared to 46 state-of-the-art methods. The code and results of our method are available at this https URL.

---


### 224. [Explainable Reinforcement Learning for Adaptive Traffic Signal Control](https://arxiv.org/abs/2607.03703)

**<font color=#1a73e8>作者：</font>** Dickens Kwesiga, Nishu Choudhary, Angshuman Guin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a powerful paradigm for adaptive traffic signal control. However, in safety-critical infrastructure like traffic control, the opaque, black-box nature of deep RL models poses challenges for transportation agency acceptance, regulatory compliance, operational trust, troubleshooting, and fine-tuning. To bridge this gap between high-performance optimization and human-comprehensible interpretability, this effort introduces a novel, explainable entity centric RL framework for safe and transparent traffic signal control. Rather than processing traffic states through monolithic, flat vectors, the proposed architecture disaggregates real-time intersection observations into distinct, high-dimensional lane entities and phase temporal configurations to inherently preserve the structural topology and geometric configurations of the intersection. Relational dependencies and inter-lane conflicts are dynamically extracted via a dual-stage attention network featuring sequential multi-head cross-attention and self-attention blocks. This design yields a real time affinity matrix that quantifies the direct influence of signal phases on specific approach volumes and queues, providing full visual and analytical interpretability. To ensure strict operational reliability, a deterministic action-masking interface is integrated directly into the Proximal Policy Optimization pipeline, explicitly blocking invalid phase transitions to guarantee absolute compliance with established signal timing and safety constraints. Evaluated in a microscopic simulation environment, outperforms state-of-the-art baselines in delay minimization. More importantly, the emergent attention weights align precisely with established traffic engineering principles, offering an auditable, trust-enabling, and deployable architecture for next-generation adaptive traffic control systems.

---


### 225. [GRASP: Graph-Reasoning Aided Survey Planning for High-Fidelity Related Work Generation](https://arxiv.org/abs/2607.03709)

**<font color=#1a73e8>作者：</font>** Haoming Li, Jessica Ouyang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Writing a literature review requires a deep understanding of the relationships among cited papers: how they build on, challenge, or offer alternative perspectives to one another. We present Graph-Reasoning Aided Survey Planning (GRASP), a framework combining LLM planning for related work generation with graph algorithms to extract key relationships among cited papers. Our two-layer graph structure consists of a Graph of Thoughts and an Argument-Counterargument Planning Network, representing the cited papers at different levels of granularity, and we apply topology-aware pruning via a Steiner tree to identify the core inter-paper relationships captured in our graph. Our citation analysis-based evaluation shows that GRASP generates related work sections (RWS) that closely match human-written targets in terms of the discourse roles, intents, and grouping of citations.

---


### 226. [Between Knowledge and Care: A Mixed-Methods Evaluation of Generative AI for T2DM Self-Management from Patient and Physician Perspectives](https://arxiv.org/abs/2607.03720)

**<font color=#1a73e8>作者：</font>** Ruiqi Chen, Yibo Meng, Huidi Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is increasingly used for everyday health guidance, yet its clinical appropriateness in chronic disease contexts remains poorly understood. This paper presents a two-part mixed-methods study on \revise{Type 2 Diabetes Mellitus (T2DM)}, examining how patients and physicians assess AI-generated health information. \revise{Study~1} analyzes 784 \revise{participant reported} patient queries to characterize seven informational need categories and \revise{develops a structured five dimensional physician rating rubric informed by patient query categories and clinician priorities} (\textit{Accuracy, Safety, Clarity, Integrity, Action Orientation}). \revise{Study~2} engages seven physicians scoring responses from four AI models and discussing evaluative reasoning through in-depth interviews. Models perform well on factual explanation and lifestyle guidance but consistently underperform on medication reasoning and emotional support. Two \revise{analytic concepts} emerge \revise{from the data}. The \textit{pre-visit primer} \revise{frames AI as preparation for clinical encounters rather than as a replacement for physicians}. The \textit{fluency illusion} \revise{describes how polished language may convey epistemic authority that the clinical content does not support}. Patients and physicians converged on three shared limitations (role boundaries, emotional inadequacy, personalization gaps) while diverging in evaluative emphasis, \revise{which informed} four design directions, task-aware orchestration, risk-aware fallback, dynamic personalization, and emotionally attuned interaction.

---


### 227. [SelfMem: Self-Optimizing Memory for AI Agents](https://arxiv.org/abs/2607.03726)

**<font color=#1a73e8>作者：</font>** Shu Yang, Junchao Wu, Derek F. Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While current AI agents support increasingly long context windows, tool use, and skill execution for long-horizon tasks, they still require memory systems to effectively leverage historical experience. Existing memory frameworks typically rely on fixed storage, retrieval, and summarization mechanisms, which can be rigid across different tasks and often require manual tuning. To address this limitation, we propose SelfMem, a self-optimizing memory framework. Inspired by prior work on self-improving AI, we follow the principle of "teaching an agent to fish rather than giving it a fish." Instead of forcing the model to follow a predefined memory strategy or format, SelfMem provides an environment with memory tools and feedback signals that allow the agent to explore, evaluate, and refine its own memory strategy. Our results show that SelfMem consistently outperforms retrieval, compression, and agent-memory baselines on BEAM across conversation scales from 100K to 1M tokens. Compared with the strongest baseline, SelfMem improves the official score by 48.7%, 40.8%, and 41.9% at 100K, 500K, and 1M, respectively. Further question-type analysis shows broad robustness across diverse memory demands, and our optimization study shows that model-guided strategy refinement further improves performance.

---


### 228. [ProACT: Towards Breakdown-Aware Proactive Agent in Multi-User Collaboration](https://arxiv.org/abs/2607.03730)

**<font color=#1a73e8>作者：</font>** Shu Yang, Difei Xu, Jiaxin Pei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational agents are increasingly embedded in human collaborative work, yet they remain fundamentally passive and reactive: they respond to explicit user requests rather than proactively recognizing moments when a team would benefit from timely intervention as human collaborators often do. This reactive design substantially limits the use of agents as active participants in multi-user collaboration, where disagreements, ambiguous goals, forgotten constraints, underspecified plans, discussion loops, and imbalanced participation can gradually undermine group progress. To move agents from passive assistants toward active participants in multi-user collaboration, we introduce ProACT, a breakdown-aware agent framework grounded in theories of common ground, collaborative planning, and coordination work. ProACT observes the speaker-attributed conversation history, determines whether the current turn contains a collaboration breakdown requiring intervention, decides whether the agent should stay silent or speak, and, when speaking is needed, routes the case to a targeted collaboration skill. We further introduce the first multi-user collaboration benchmark for evaluating proactive agents across project planning, product design, research collaboration, logistics, education, and resource-constrained decision making. Across 3,244 turn-level examples and five LLM backbones, ProACT consistently improves collaborative appropriateness, non-interruptiveness, conciseness, and judged intervention quality over direct chat.

---


### 229. [ProxyUp: Training-Free Proxy-Conditioned Video Generation for Controllable Dynamics](https://arxiv.org/abs/2607.03732)

**<font color=#1a73e8>作者：</font>** Zanwei Zhou, Jiazhong Cen, Jiemin Fang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise control over complex dynamics remains challenging for modern video generative models, as text prompts alone often cannot specify physically plausible, fine-grained motion and interactions. We introduce $\textit{proxy-conditioned video generation}$, where a coarse proxy video from physics-based simulation or real-world recording serves as a dynamics carrier to control foreground object motion. Given a proxy video and a text prompt, the goal is to synthesize a new video that preserves the proxy dynamics while generating novel content and plausible interactions aligned with the prompt. Since paired proxy-target videos are difficult to obtain, we propose $\textbf{ProxyUp}$, a training-free framework built on pretrained video generative models. ProxyUp first inverts the proxy video into an intermediate latent representation and applies $\textbf{region-wise latent noising}$, preserving motion-critical proxy latents while injecting noise into regions intended for text-driven regeneration. To mitigate the distribution mismatch and weak foreground-background coupling introduced by this heuristic latent composition, we further propose $\textbf{Stochastic Flow Relaxation (SFR)}$, which progressively relaxes the composed latent toward the model's learned distribution before ODE sampling. Experiments on both simulation and real-world proxies show that ProxyUp outperforms strong video editing and motion transfer baselines in dynamic fidelity and text alignment.

---


### 230. [Can Conversational Temporal Dynamics Improve Depression Detection in Dyads? A Preliminary Investigation in Multi-Modality Perspectives](https://arxiv.org/abs/2607.03744)

**<font color=#1a73e8>作者：</font>** Hanie Kang, Huang-Cheng Chou, Sudarsana Reddy Kadiri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic depression detection from clinical interviews typically models the semantic content and acoustic characteristics of participant speech. However, the interactional timing between the clinician and participant remains comparatively under-modeled. We investigate conversational temporal dynamics, specifically dyadic turn-pair timing, as a primary modality fused with self-supervised encoders. Evaluated on the DAIC-WOZ dataset, we compare a compact 24-dimensional timing module against frozen WavLM-large and RoBERTa-large baseline detectors. This temporal module achieves the highest single-modality performance on the development set. Furthermore, a convex-weighted late fusion strategy improves overall performance to 0.804 and 0.669 macro-F1 on the development and test sets, respectively. The learned fusion effectively assigns zero weight to acoustics, demonstrating that conversational timing serves as a lightweight, interpretable complement for dyadic depression screening.

---


### 231. [Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process](https://arxiv.org/abs/2607.03748)

**<font color=#1a73e8>作者：</font>** Zican Hu, Xuyang Hu, Yiming Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified multi-modal models (UMMs) have shown promising interleaved text-image reasoning capabilities, yet effectively optimizing such multi-turn generation via reinforcement learning (RL) remains an open challenge. Existing approaches apply RL exclusively to text steps, relegating image generation to supervised surrogates, preventing policy gradients from propagating through the full interleaved trajectory across heterogeneous modalities. This leaves the potential of RL for UMMs largely untapped. In the paper, we introduce \textbf{BRAID} (\textbf{B}ridging inte\textbf{R}le\textbf{A}ved mult\textbf{I}-modal reasoning as a unified \textbf{D}ecision process), a simple framework that casts multi-turn text-image-text reasoning as a unified Markov decision process (MDP), enabling joint optimization of textual and visual generation via a single, principled RL objective. BRAID computes a shared trajectory-level advantage and propagates it coherently into both text tokens and image denoising paths, each optimized through its modality-native policy gradient mechanism. To further address long-horizon credit assignment, BRAID employs a vision-language model (VLM) judge that scores each intermediate image on its reasoning utility, supplying dense turn-level feedback to sharpen learning at critical visual branches. Experiments on spatial reasoning and visual perception benchmarks show that BRAID consistently outperforms various baselines, confirming that a unified MDP formulation with vision-thinking guidance is essential for effective multi-modal reasoning.

---


### 232. [EmCom-Diffusion: Probing Visual Reflection in Emergent Languages via Image Generation](https://arxiv.org/abs/2607.03752)

**<font color=#1a73e8>作者：</font>** Haruumi Omoto, Tadahiro Taniguchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measuring the extent to which emergent languages encode the visual content of their inputs is an open problem. We refer to this property as visual reflection: the extent to which emergent messages preserve information about their source images that can be recovered without appeal to the speaker-listener pair that produced them. Existing metrics measure it only indirectly, through proxies such as human-defined concept inventories, natural-language captions, structural distance correlations, or Referential Game accuracy, each of which can either miss visual content the message encodes or credit content it does not. We propose EmCom-Diffusion, an evaluation framework that measures visual reflection directly: it reconstructs each input image from its emergent message and compares the reconstruction with the original image itself, rather than with human-defined targets. Concretely, it finetunes a pretrained text-to-image diffusion model on (image, emergent-message) pairs and scores visual reflection as the perceptual similarity between the reconstructed and original images, operating generatively rather than discriminatively. Instantiating it on MS-COCO with a Referential Game, we validate the metric against random and fixed-token baselines under three pretrained visual encoders, and compare it against four existing metrics (CBM, supervised translation, TopSim, and R@1). EmCom-Diffusion captures visual content the other metrics miss.

---


### 233. [Exploring SAM Supervision for Fine-Grained UAV Target Segmentation under Data Scarcity](https://arxiv.org/abs/2607.03754)

**<font color=#1a73e8>作者：</font>** Le-Anh Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) target segmentation remains challenging due to the small size of objects, appearance variations, cluttered backgrounds, and the scarcity of densely annotated data. These factors hinder the performance and practical deployment of lightweight segmentation models in real-world UAV applications. To address this problem, this paper investigates the use of SAM3 (Segment Anything Model 3) as a pseudo-label generator for training compact segmentation networks. Specifically, two supervision paradigms are explored: (i) direct pseudo-supervision using unaltered SAM3-generated masks, and (ii) a refinement strategy that re-applies SAM3 to localized image patches for improved mask quality. Based on these paradigms, a two-stage SAM3-guided pseudo-label generation framework is proposed. In the first stage, SAM3 generates coarse masks for initial object localization. The localized regions are subsequently cropped into patches and processed by SAM3 again to generate fine masks with accurate object boundaries and discard false positives. The resulting coarse and fine masks are then used as pseudo-labels to optimize a lightweight network, termed IPS-Seg, which consists of three components: an IdentityFormer backbone for feature extraction, an Atrous Spatial Pyramid Pooling module for multi-scale context aggregation, and a PixelShuffle-based decoder for spatial resolution recovery. Extensive experiments under multiple supervision settings demonstrate the effectiveness of the proposed framework. The results show that IPS-Seg achieves a favorable trade-off between segmentation accuracy and computational efficiency while benefiting consistently from the proposed pseudo-label generation strategy. These findings highlight the potential of large-scale foundation models as annotation sources for training compact task-specific segmentation networks in low-label vision domains.

---


### 234. [SAVER: Stochastic Adaptive Variance-Driven Exploration and Reconstruction for Low-Dose Computed Tomography](https://arxiv.org/abs/2607.03761)

**<font color=#1a73e8>作者：</font>** Shunta Nonaga, Koji Tabata, Junya Honda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computed Tomography (CT) is indispensable in clinical diagnostics, yet minimizing radiation dose without compromising image quality remains a critical challenge. Conventional low-dose protocols often rely on fixed, uniform angular sampling, independent of the underlying structural complexity of organs of individual patients. We propose ``Stochastic Adaptive Variance-Driven Exploration and Reconstruction'' (SAVER), an adaptive data acquisition framework that selects projection angles in real-time based on the statistical variance of acquired data. Utilizing a Softmax-based stochastic scheduling scheme with simulated annealing, SAVER prioritizes directions with high structural information while maintaining necessary exploration. Numerical experiments across 8 diverse phantoms demonstrate that SAVER achieves consistently higher reconstruction fidelity than conventional random sampling, particularly for objects with high structural anisotropy. Furthermore, the proposed method exhibits robust performance under significant measurement noise. By dynamically reallocating radiation dose to the most informative projections, SAVER provides a mathematically-grounded approach to maximize diagnostic quality per unit of radiation dose, marking a shift toward sample-dependent, data-driven CT acquisition.

---


### 235. [FedACT: Federated Adaptive Coordinate Trust Modulation for Robust Transformer Training under Data Heterogeneity](https://arxiv.org/abs/2607.03763)

**<font color=#1a73e8>作者：</font>** Shuai Li, Qinglin Wang, Ping Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Transformer training increasingly relies on local AdamW, whose adaptive updates can provide much stronger local progress than SGD-based training. However, under heterogeneous client data, even globally corrected AdamW updates may remain highly uneven in coordinate-wise reliability. We refer to this phenomenon as coordinate trust mismatch. Existing federated adaptive optimizers mainly address mismatch at the client-update or communication-round level, but still apply the corrected adaptive direction densely and uniformly across coordinates. In this paper, we propose FedACT, a global-aware coordinate trust modulation method for federated AdamW training. FedACT first forms a globally corrected adaptive direction and then reallocates update magnitudes according to a coordinate-wise trust score, assigning larger steps to coordinates jointly supported by local gradients and global correction, while preserving smaller non-zero updates on the remaining coordinates. Extensive experiments on federated vision Transformers, CNNs, LLM pre-training, and LLM fine-tuning show that FedACT consistently improves over strong federated adaptive baselines, with the largest gains on Transformer models under stronger data heterogeneity. Mechanism analyses further show that FedACT improves cross-client direction consistency, suggesting that coordinate-level trust allocation effectively complements round-level global-local correction. Code will be released.

---


### 236. [Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765)

**<font color=#1a73e8>作者：</font>** Liang Han, Bangcai Wei, Junsheng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction from sparse views is a challenging task in 3D computer vision. Recent studies on 3D Gaussian Splatting (3DGS) have achieved remarkable results with sparse views in novel view synthesis, yet reconstructing high-quality geometric surfaces from sparse views remains a challenge, due to the limited geometry clues and the discreteness of Gaussians. In this paper, we propose a novel 3DGS-based method for high-fidelity surface reconstruction from sparse views. Our key insight is to introduce a normal-guided depth propagation approach, which can extend depth information from high-confidence regions to constrain the depth in low-confidence areas. Additionally, we propose an abnormal depth edge-aware regularization to address depth discontinuities caused by the discreteness of Gaussians. Extensive experiments on DTU and Tanks-and-Temples datasets demonstrate that our method outperforms the state-of-the-art methods in sparse view surface reconstruction. Project page: this https URL.

---


### 237. [Self-Improving Diffusion Classifiers with Minority Preference Optimization](https://arxiv.org/abs/2607.03770)

**<font color=#1a73e8>作者：</font>** Hyunsoo Kim, Jungmyung Wi, Soobin Um 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior studies have demonstrated that diffusion classifiers achieve robust zero-shot classification performance. However, their effectiveness is strongly tied to the pretraining data distribution: they perform well in majority, high-density regions of the data manifold, but are significantly less accurate in minority, low-density regions. Although prior works on minority sampling have focused on generating more minority-like images, what minority sampling fundamentally enables beyond generation remains underexplored. In this paper, we reveal a direct relationship between minority sampling in generation and the perception capability of diffusion classifiers. Specifically, we show that enhancing minority sampling broadens the coverage of underrepresented regions on the data manifold, thereby improving diffusion-based recognition. To exploit this connection, we propose \textit{Self-Improving Diffusion Classifiers with Minority Preference Optimization} (MiPO), which fine-tunes a pretrained diffusion model using minority preference rewards. Using only arbitrary caption data, MiPO generates candidate samples, rewards those that better cover minority regions, and optimizes the model with LoRA and Group Relative Policy Optimization, without additional image data, external foundation models, or external reward models. This enables stable, prompt-adaptive minority sampling and translates low-density generative coverage into improved zero-shot diffusion classification. To sum up, we show that diffusion classifier perception is biased toward majority regions, demonstrate that this bias can be alleviated through minority preference optimization, and evaluate MiPO on five standard datasets.

---


### 238. [City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771)

**<font color=#1a73e8>作者：</font>** Liang Han, Wenyuan Zhang, Junsheng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view 3D surface reconstruction is a longstanding challenge in computer vision. Although recent large-scale reconstruction methods based on 3D Gaussian Splatting (3DGS) achieve impressive novel-view synthesis, producing high-quality surfaces over large scenes remains difficult, due to complex geometry, long optimization, and limited memory. In this paper, we propose a novel yet simple partitioning method to efficiently and faithfully reconstruct large-scale scene surfaces. Our key insight lies in a scene partitioning method based on viewpoint orientation. This partitioning approach ensures that views with similar orientations are jointly involved for more accurate depth estimations, leading to precise surface reconstructions and balanced computation on multiple GPUs in parallel. In addition, we propose a strategy to detect and repair missing regions in the initial point cloud caused by sparse viewpoints or insufficient textures, thereby further improving the geometric quality. Extensive experiments on the GauU-Scene, MatrixCity, and UrbanScene3D datasets demonstrate that our method outperforms the state-of-the-art approaches in surface reconstruction for large-scale scenes. Project page: this https URL.

---


### 239. [Conservative Subject Invariant EMG-based Gesture Recognition](https://arxiv.org/abs/2607.03783)

**<font color=#1a73e8>作者：</font>** Hamed Rafiei, Ali Mousavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject generalization remains a fundamental challenge in surface electromyography (sEMG)-based gesture recognition. Although deep learning methods have improved within-subject performance, they often rely on subject-specific data and struggle to balance invariance and discriminability. In this work, we propose a conservative multi-objective learning framework for subject-invariant sEMG gesture recognition. The proposed model adopts a multi-head architecture that jointly optimizes gesture classification, adversarial subject confusion through gradient reversal, and triplet-based metric learning to encourage discriminative and subject-invariant representations. To improve optimization stability, a Lipschitz-inspired adaptive weighting mechanism is introduced to dynamically balance the auxiliary objectives according to their relative magnitudes during training. The proposed method is evaluated on two benchmark datasets: UCI EMG (36 subjects, 6 gestures) and NinaPro DB5 (10 subjects, 10 gestures). On the UCI EMG dataset, the method achieves 84.48\% accuracy compared to 78.2\% reported by state-of-the-art methods. On NinaPro DB5, it achieves 61.44\% accuracy versus 41.30\%, corresponding to a 49\% relative improvement. In addition, the proposed framework reduces cross-subject prediction variance and produces more structured latent representations. These results indicate that jointly enforcing invariance and discriminability through adaptive multi-objective optimization leads to more stable training and improved cross-subject generalization in sEMG-based gesture recognition systems.

---


### 240. [Rethinking Depth Pruning for Vision Transformers: A Heterogeneity-Aware Perspective](https://arxiv.org/abs/2607.03784)

**<font color=#1a73e8>作者：</font>** Zhenfeng Su, Kang Zhao, Han Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While prior studies have successfully compressed vision Transformers (ViTs) through various pruning techniques, most have concentrated on width pruning to achieve significant reductions in model size. Depth pruning, which removes entire layers from a ViT, is notoriously difficult for accuracy recovery despite its potential to deliver higher speedups, limiting the acceleration achieved by existing joint width-and-depth pruning methods. In this work, we reveal that the failure of existing depth pruning methods lies in their neglect of heterogeneity between different layers, and we introduce HetDPT, a heterogeneity-aware depth pruning method that avoids dimension mismatch. Comprehensive experiments on ImageNet-1K, CIFAR-100, COCO, and ADE20K validate our method: HetDPT achieves a 1.58$\times$ speedup for DeiT-B while maintaining accuracy and a 1.39$\times$ speedup for DeiT-S with nearly no accuracy degradation. Furthermore, when combined with width pruning, HetDPT+ sets a new state-of-the-art record in extreme ViT pruning, enhancing the acceleration ratio from 4.24$\times$ to 5.19$\times$ for the Isomorphic-Pruning-2.6G configuration while maintaining near-lossless accuracy; our code is available at this https URL.

---


### 241. [Folding, Reasoning, and Scaling with Open-source Drug Discovery Engine](https://arxiv.org/abs/2607.03787)

**<font color=#1a73e8>作者：</font>** Aureka AI OpenDDE project  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately modeling biomolecular interactions is a central bottleneck in biology and therapeutic discovery. Here, we introduce Open Drug Discovery Engine (OpenDDE), an open-source, all-atom biomolecular foundation model that uses co-folding as the entry point to a scalable AI-driven drug discovery engine. Rather than treating structure prediction as an isolated endpoint, OpenDDE is designed as a shared structural reasoning layer for modeling sequence-structure-function relationships across biomolecular complexes, enabling complex structure prediction today while providing a foundation for de novo design, affinity estimation, structure-conditioned optimization, and more. OpenDDE integrates advances in all-atom architecture, atomic latent reasoning, inference optimization, and large-scale data processing to achieve IsoDDE-level co-folding accuracy within a reproducible and openly accessible framework. We also identify two scaling-law directions for co-folding models, revealing practical routes for continued improvement through data, model, inference, and training scaling. By releasing training code, inference pipelines, checkpoints, and benchmarks, OpenDDE aims to democratize access to frontier biomolecular intelligence, accelerate global collaboration, and lay an open foundation for next-generation drug discovery systems that can move from predicting molecular structures toward designing, scoring, and optimizing therapeutic candidates for human health.

---


### 242. [Tensor-Train Joint Modeling for Few-Step Discrete Diffusion](https://arxiv.org/abs/2607.03788)

**<font color=#1a73e8>作者：</font>** Byoungkwon Kim, Minhyuk Sung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion promises orders-of-magnitude faster generation than autoregressive (AR) models for sequential discrete data, yet its full potential of few-step generation has remained out of reach due to a fundamental structural limitation. The conditional-independence assumption underlying current discrete diffusion models introduces a systematic parallelization bias that compounds with the number of tokens unmasked per step, becoming severe in the few-step regime that fast generation requires. We address this with the first framework for explicit joint distribution modeling in discrete diffusion via tensor decomposition, which represents the conditional clean distribution as a low-rank tensor with controllable expressivity. The framework supports both Canonical Polyadic (CPD) and Tensor-Train (TTD) decompositions, and we identify a structural bias of TTD toward dependencies between nearby tokens, formalized through Oseledets' theorem relating TT-rank to unfolding-matrix rank, which is well-suited to sequential data such as natural language and line notations for molecular data. To enable efficient generation, we present an iterative marginal inference procedure with specialization for predetermined position schedules. Our framework integrates into pretrained MDMs through lightweight fine-tuning, yielding substantial improvements in few-step generation at a fraction of the cost of training from scratch.

---


### 243. [G$^2$TAM: Geometry Grounded Track Anything Model](https://arxiv.org/abs/2607.03789)

**<font color=#1a73e8>作者：</font>** Chenming Zhu, Peizhou Cao, Jingli Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human spatial understanding arises from jointly perceiving geometry and semantics, enabling consistent object identification and localization across viewpoints and time. Current video segmentation models depend on explicit object appearance memory banks for instance tracking, yet they remain vulnerable to large viewpoint changes and long-term occlusions. Leveraging the spatial consistency afforded by modern feed-forward 3D reconstruction models, we propose the Geometry Grounded Tracking Anything Model (G$^2$TAM), a unified framework for promptable instance tracking in 3D using only unordered RGB images or videos. G$^2$TAM employs spatially aligned geometric representations as implicit memory, ensuring stable instance identity and localization across frames and views. At its core is a cross-modal spatial encoder that integrates visual and textual prompts into a shared geometric space, enabling end-to-end spatial reconstruction and instance-consistent mask prediction. To support training and evaluation, we construct InsTrack, a large-scale dataset with a dedicated validation split for benchmarking. Extensive experiments show that G$^2$TAM delivers strong cross-view consistency, promptable instance spatial tracking, video object segmentation and spatial reconstruction, establishing a foundation for interactive, geometry-grounded spatial reasoning.

---


### 244. [InfraNet: Quality-Aware RGB Guidance for Efficient Infrared Object Detection](https://arxiv.org/abs/2607.03795)

**<font color=#1a73e8>作者：</font>** Zichao Feng, Haodong Zhu, Jingying Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust object detection under adverse visual conditions remains a long-standing challenge for multi-modal perception systems. Existing fusion-based methods typically require both RGB and infrared (IR) inputs, and treat them equally during both training and inference, which compromises their robustness when the RGB modality becomes unreliable or unavailable. In this case, we propose \textbf{InfraNet}, an IR-centric quality-aware framework that regulates RGB guidance during training and supports flexible RGB--IR or IR-only deployment. InfraNet employs an asymmetric architecture where the primary IR pathway extracts multi-scale infrared features for predictions, while the auxiliary RGB pathway provides reliability-controlled supervisory signals. The core of InfraNet is \textbf{QualGate}, a quality-aware fusion module that learns a task-oriented control signal to suppress unreliable RGB guidance and compensate IR features during cross-modal training. Built upon InfraNet, we design two architectural variants: a lightweight IR-only architecture InfraNet-IR and an RGB--IR architecture InfraNet-RGB-IR. Our method is evaluated through extensive experiments on four benchmark datasets (LLVIP, FLIR-Aligned, M$^3$FD, and DroneVehicle), showing strong or competitive accuracy in challenging low-light and adverse weather conditions. Notably, InfraNet maintains high efficiency in IR-only inference, making it both accurate and computationally efficient.

---


### 245. [Probabilistic Robustness in Medical Image Classification](https://arxiv.org/abs/2607.03797)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Siddartha Khastgir, Xingyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning (DL) has shown strong performance in medical image classification, but its trustworthy deployment remains challenging in safety-critical clinical settings, where prediction errors under perturbations may lead to severe consequences. Existing studies mainly focus on adversarial robustness (AR) from a worst-case perspective; however, such settings may be less representative of real medical applications. In this work, we investigate probabilistic robustness (PR) as a more practical measure of model trustworthiness. To this end, we construct a set of natural corruption settings for medical image classification and systematically evaluate commonly used DL models on MedMNIST v2 dataset. Our study provides a statistically grounded perspective on assessing the trustworthiness of DL models, thereby supporting their more trustworthy deployment in medical imaging applications.

---


### 246. [Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks](https://arxiv.org/abs/2607.03798)

**<font color=#1a73e8>作者：</font>** Yoshihiro Maruyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetry is everywhere in nature and society. Geometric deep learning exploits symmetries in data to improve the performance and efficiency of deep learning systems. In this paper, we extend geometric deep learning to utilize richer symmetry structures. Specifically, we develop order-equivariant neural networks (OENN), which generalize standard graph message passing and sheaf neural networks via the theory of equivariant bundles over face posets (face categories). We (i) characterize all linear order-equivariant maps, (ii) build OENN layers, and (iii) prove universal approximation theorems (UATs) for continuous order-equivariant maps, which are new results even when restricted to sheaf neural networks (for which no UAT was known before). We illustrate the framework on graph and sheaf models. Our results can also be seen as extending the known UAT for graph neural networks to a more general setting that subsumes sheaf neural networks as well. In addition, we show that OENN can be extended further to CENN, Category-Equivariant Neural Network, which gives the general form of equivariant neural networks as well as of equivariant universal approximation theorems, allowing us to leverage categorical symmetry in data (e.g., non-invertible symmetries on multiple objects with compositional relations on those symmetries).

---


### 247. [CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion Generation](https://arxiv.org/abs/2607.03803)

**<font color=#1a73e8>作者：</font>** Xuyao Huang, Zelai Deng, Xu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing demand for image-to-video creation on mobile devices has increasingly focused on cinematic motion effects like bullet time, dolly zoom, slow motion, etc. While Diffusion Transformers (DiTs) exhibit strong performance in video generation, their large parameter sizes and multi-step iterative denoising processes lead to substantial computational overhead, making efficient generation on mobile devices challenging. We propose CineMobile to bridge the gap. In particular, CineMobile adopts a three-fold optimization strategy: (1) leveraging a distillation-guided pruning approach to derive a compact yet efficient model that retains the essential video generation capabilities required for cinematic effects; (2) optimizing the compressed model into a 4-step generator via a combination of diffusion distillation and reinforcement learning; (3) employing a hybrid post-training quantization strategy to compress the model footprint to under 1 GB. Experimental results show that compared to the teacher model with the Wan 2.1 architecture, CineMobile achieves a 40x speedup in generation while maintaining comparable visual quality. Specifically, CineMobile generates 49-frame 480p videos with a per-step denoising latency of 0.6s on an NVIDIA H200 GPU and 20s on the MediaTek Dimensity 8400 Ultimate 5G platform, with a peak memory usage of 1.8 GB, demonstrating its practical applicability for mobile-based image-to-video creation.

---


### 248. [TRISTAR: Triple-Signal Stair Recognition and Vision-Only Indoor Navigation for Search-and-Rescue Micro-UAVs](https://arxiv.org/abs/2607.03818)

**<font color=#1a73e8>作者：</font>** Octavian Gîngu, Stelian Spînu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor search-and-rescue (SAR) operations often require rapid situational awareness where GNSS signals are unavailable and human access is difficult or hazardous. While most autonomous aerial systems rely on LiDAR, stereo vision, or specialized depth cameras, such solutions increase both hardware complexity and deployment costs. This paper presents a complete autonomous indoor navigation framework for low-cost unmanned aerial vehicles based exclusively on monocular vision. Implemented on a DJI Tello platform, the system combines monocular depth estimation using Depth Anything V2 with classical computer vision and lightweight deep learning models for scene understanding, victim detection, and hazard recognition. The framework consists of two independent behaviors: (i) corridor exploration with automatic door detection, room entry, OCR-based room identification, and victim inspection; and (ii) autonomous stair ascent based on TRISTAR (TRI-Signal STair Ascent Recognition), a novel triple-sensor fusion method that integrates structural cues (Sobel filtering), texture analysis (multi-scale Gabor filtering), and geometric depth from monocular depth estimation. Evaluation used real indoor flights in a university building. Depth calibration reduced relative depth error from 27.4% to below 10%, while the door detection algorithm reached a precision of 0.93 and an F1-score of 0.91. A dedicated ablation study shows that multi-sensor fusion significantly improves stair-recognition robustness compared to individual sensing modalities, and a failure-case analysis delineates the limits of monocular perception under challenging lighting and reflective surfaces. The results demonstrate that reliable indoor exploration and stair traversal are achievable on resource-constrained platforms without specialized ranging hardware, a practical, cost-effective solution for rapid SAR deployment.

---


### 249. [DualView: Preventing Indirect Prompt Injection in Personal AI Agents](https://arxiv.org/abs/2607.03821)

**<font color=#1a73e8>作者：</font>** Juhee Kim, Woohyuk Choi, Taehyun Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personal AI agents that run on the user's local machine, such as OpenClaw, automate daily tasks including web search, email, and file management. Their access to computer resources, including the network, file system, and shell, exposes them to indirect prompt injection (IPI) attacks. Prior Dual LLM defenses block IPI by replacing untrusted data with symbols that the agent can reference but not read. However, they track untrusted data only inside the agent's context, so when the agent saves and later rereads untrusted data, that data, possibly an attacker's prompt, can return as trusted data rather than as a symbol, which we call stored IPI.
Operating on the user's real environment, which humans and programs share, is what makes agents like OpenClaw practical, and is exactly why a defense that ignores it is incomplete. Preserving symbols in such an environment is hard, because humans and programs need original data. We present DualView, which extends untrusted data tracking from the agent's context to the user's environment, including the file system, shell, network, and other agents, by giving each channel two views. In AgentView, the agent sees untrusted data as symbols even after writing it out and reading it back, blocking stored IPI, while HumanView preserves original data for humans and tools. DualView routes each tool call to the right view and synchronizes data across the two views. DualView deploys as an OpenClaw plugin using only tool hooks, without changing the agent's tool-call logic or tool implementations. Since DualView isolates untrusted data by design, its protection is not limited to known attack templates. In our evaluation on an IPI benchmark and PinchBench, DualView blocked every IPI attack, including stored IPI, while keeping utility close to the unprotected baseline.

---


### 250. [FDR-Occ: Factorized Dense Routing for Full-Spectrum 3D Occupancy Prediction](https://arxiv.org/abs/2607.03822)

**<font color=#1a73e8>作者：</font>** Dubing Chen, Huan Zheng, Tianyi Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based 3D occupancy prediction fundamentally relies on the 2D-to-3D view transformation. Current paradigms predominantly utilize explicit physical projection, which artificially restricts the routing matrix to strict, sparse camera rays. While computationally efficient, this imposes a severe Locality Bottleneck, preventing the network from constructing holistic contextual understanding and degrading sharply when camera extrinsics are unreliable or absent. To break this bottleneck, we abstract view transformation as unconstrained bipartite routing and propose Factorized Dense Routing (FDR). By approximating dense 2D-to-3D mixing through hierarchical tensor contractions, FDR guarantees a fully-global receptive field with tractable, sub-quadratic complexity. Crucially, the mandatory spatial contraction in dense routing exposes a fundamental Resolution-Context Trade-off. To address this, we introduce a Resolution-Context Decoupled Architecture. We factorize the 3D space into a global macroscopic topological anchor (via FDR) and precise local geometric planes (via explicit projection). This decoupling enables global semantic inference and exact surface localization to complement each other without mutual compromise. Extensive experiments demonstrate that our framework achieves state-of-the-art performance on the Occ3D-nuScenes and Occ3D-Waymo benchmarks. More notably, in an uncalibrated setting where physical extrinsics are withheld, our global routing internalizes the implicit multi-camera rig topology and exhibits substantially stronger structural robustness than physical-projection baselines under the same protocol.

---


> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
