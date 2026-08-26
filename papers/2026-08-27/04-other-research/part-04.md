# 📦 其他研究 | 2026年08月27日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-194**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-194**

---

### 151. [TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674)

**<font color=#1a73e8>作者：</font>** Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint text-to-video-audio generation produces synchronized visual and acoustic content, but the long sampling trajectories and heterogeneous multimodal computation of large models make inference prohibitively expensive. We present TurboT2VA, a distillation and inference framework for accelerating a 19B-parameter joint video-audio model. Large-scale T2VA distillation is challenged by modality-imbalanced optimization, the difficulty of continuous-time consistency training at scale, and the quality--diversity trade-off. TurboT2VA addresses these issues with per-modality normalization and a progressive curriculum comprising discrete consistency warm-up, continuous consistency refinement, and joint consistency--distribution matching. The curriculum first establishes a stable, diverse generation trajectory and only then introduces distribution-level refinement. On LTX-2, four-step distillation reduces generator latency from 50.52s to 2.51s at the standard evaluation resolution of 512$\times$768, achieving a 20.1$\times$ speedup while maintaining strong visual quality, audio fidelity, diversity, and video-audio synchronization. We further develop an architecture-aware inference stack that combines guarded W8A8 and fused operators, padded-text compaction, and modality-aware sparse attention while preserving dense cross-modal and text-conditioning paths. Under the high-resolution deployment setting at 1024$\times$1792, the complete stack reduces generator latency from 318.74s to 5.83s on one NVIDIA H20, achieving a 54.67$\times$ generator-only speedup. Inference code and generation demos are available at this https URL.

---


### 152. [Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680)

**<font color=#1a73e8>作者：</font>** Wenxuan Shen, Dongna Jin, Dongping Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video games provide a scalable source of training data for video world models, offering diverse environments, complex interactions, and abundant in-the-wild gameplay videos. However, raw gameplay footage entangles the game world with screen-space interfaces, introducing game-specific biases and irrelevant dynamics that hinder world-model training. To address this problem, we introduce GameUI-Taxonomy and G2WEngine, a full-stack framework that formalizes gameplay UI grounding and removal. G2WEngine automatically extracts reusable UI assets from real gameplay videos and synthesizes temporally coherent UI overlays on clean footage. Using this engine, we construct Game2World, comprising 96K synthetic paired videos with precise reconstruction targets and 1,079 in-the-wild clips from 303 games for realistic evaluation. Its asset library contains 5,132 verified UI elements across 21 taxonomy categories, collected from 1,010 representative gameplay frames. Based on Game2World, we propose GameCleaner, a mask-free gameplay UI removal model that combines multimodal semantic understanding with video editing capabilities. Unlike mask-based methods, GameCleaner directly identifies and removes diverse HUD elements while preserving the underlying scene content and temporal dynamics. In a controlled pilot, world models trained on UI-free gameplay improve overall VideoReward by 6.83% over those trained on UI-overlaid data. On UI-removal evaluation, GameCleaner achieves an average AAR of 95.36 on synthetic videos, outperforming the strongest temporal mask baseline by 57.3%, and obtains the best in-the-wild AAR of 80.05 with 99.8 background preservation. These results demonstrate the scalable potential of transforming Internet gameplay videos into high-quality world-model training data. Code, dataset, and model will be available at this https URL.

---


### 153. [One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output](https://arxiv.org/abs/2608.24683)

**<font color=#1a73e8>作者：</font>** Francesco Vitucci, Michele Lorusso, Francesco Scagliola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One algorithmic composition may require a Csound score, engraved notation, real-time control, and a rehearsal click. Authored separately, their timelines drift. Temporal System is a Wolfram Language paclet that instead compiles one immutable store of typed entities on a rational beat timeline through backend-specific contracts. It emits Csound synthesis, beta MusicXML 4.0, OSC control, and click artifacts that remain synchronized because they share that store. Conversion to seconds, samples, or hertz occurs only at render time. Csound notes use stable named instruments in external .orc files; curves become k-rate signals declared against score p-fields. The click backend derives rehearsal audio from the same meter and tempo and reuses the Csound serializer. We describe the temporal, semantic, and rendering-contract layers, their practical trade-offs, and the limits of this proprietary authoring environment within an otherwise open-source ecosystem. The archived supplement exposes the reported outputs pending paclet release.

---


### 154. [Single State Update Predictive Coding training for Time Series Forecasting and Anomaly Detection](https://arxiv.org/abs/2608.24697)

**<font color=#1a73e8>作者：</font>** Matteo Cardoni, Sam Leroux  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Coding (PC) is a neural learning paradigm that enables parallelizable neural network layer updates. However, the main bottleneck of PC Networks (PCN) is the sequential backwards error propagation. To tackle this, we introduce a training technique that pairs a Generative PCN with a support Encoding PCN. The two PCNs are trained in parallel to match their neural activations, without sequential propagation. We apply this to time series anomaly detection and show that our approach results in more stable, continuous, online learning.

---


### 155. [The Annotation Bottleneck in Persian Text NLP: Persian as an Annotation-Scarce Language](https://arxiv.org/abs/2608.24698)

**<font color=#1a73e8>作者：</font>** MohammadHossein Mortazavi, Mostafa Salehi, Hadi Veisi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persian (Farsi) is often described as a low-resource language in natural language processing, but that label collapses distinct shortages into a single category. This paper argues that Persian is more precisely described as annotation-scarce, provided that the term is understood as a property of its NLP resource ecology rather than an intrinsic property of the language. The review covers 34 representative Persian text resources available by July 2026 and adds three quantitative cross-checks. First, independent web measurements place Persian among roughly the twenty most visible content languages: W3Techs reports Persian on about 0.9% of websites with a known content language, while Common Crawl CC-MAIN-2026-30 identifies Persian as the primary language of 0.7039% of HTML pages. Second, a selective speech review shows a long resource trajectory from FARSDAT to recent corpora containing hundreds or thousands of hours of speech. Third, a matched Persian-English comparison normalizes task-specific annotation volumes by relative Common Crawl web presence. The resulting ratios vary sharply: Persian syntax and news NER are comparatively dense, whereas natural-language inference falls below the web-proportional baseline. The evidence therefore does not support a simple claim that Persian is globally deficient in labeled volume. Instead, annotation scarcity is expressed through uneven task and domain coverage, incompatible schemes, access and documentation friction, and limited supervision for specialist domains, preference data, and varieties beyond standard Iranian Persian.

---


### 156. [Parameter-Level Attribution of Symmetry in Trained Networks Though Parameter-Wise Functional Sensitivity](https://arxiv.org/abs/2608.24700)

**<font color=#1a73e8>作者：</font>** Alan Muriithi, Vedanta Thapar, Torben Berndt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a network has learned a function with a known symmetry, can that symmetry be moved through the parametrisation---is there a motion in parameter space realising the group action in function space? We formulate this as a lifting problem for the realisation map $\Phi:\theta\mapsto f_\theta$, and show that a smooth parameter-space action exists only if the tangent space to the function's symmetry orbit lies within the image of $\mathrm d\Phi_\theta$, whose columns are the \emph{functional sensitivities} of individual parameters. This condition is also sufficient for pointwise first-order lifting. Relaxing it in least squares yields two local parameter directions: one following the symmetry orbit, one descending towards the equivariant subspace, with residuals measuring what the parametrisation cannot reach. On a rotationally invariant classifier we find these directions induce their predicted function-space motion, but only locally: recomputed directions track the orbit and reduce the equivariance defect, while directions held fixed depart from both after training. The same holds for Hamiltonian neural networks trained on a rotationally symmetric potential, even though the architecture does not explicitly enforce the symmetry.

---


### 157. [Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts](https://arxiv.org/abs/2608.24707)

**<font color=#1a73e8>作者：</font>** Meruyert Aristombayeva, Jason S. Lucas, Chaewan Chun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While text-based hallucination detection has been extensively studied, spoken hallucination detection remains largely unexplored, particularly for low-resource languages. We present the first multilingual spoken hallucination benchmark comprising 12,013 news samples across English, Russian, and Kazakh with controlled hallucinations of three types and three severity levels. Samples comprise original articles and aligned hallucinated counterparts in text and audio. We complement the synthetic corpus with 290 fact-checked fake news items collected natively in Russian (225) and Kazakh (65), translated into the other language and rendered through the same TTS-ASR pipeline. We assess fine-tuned multilingual encoders and, in zero-shot in-context settings, multimodal decoder models on transcript-based versus direct audio processing. Transcript-based detection generally outperforms direct audio processing, with binary-task degradation for strong encoders tracking per-language ASR error. On real-world fakes, synthetic-trained detectors transfer strongly (macro-F1 0.82-0.88 on original text), while Russian provenance analysis reveals both veracity-related and model-dependent machine-style signals, quantifying a key confound in synthetic hallucination benchmarks.

---


### 158. [Constrained Hyperparameter Optimization for Streaming Data](https://arxiv.org/abs/2608.24712)

**<font color=#1a73e8>作者：</font>** Bruno Veloso, João Gama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization of hyperparameters is a critical factor to obtain optimal model performance. While existing research has predominantly concentrated on batch-learning scenarios, addressing the complexities inherent in data streams presents a challenge. The deployment of sophisticated methodologies to manage data streams becomes highly important. Consequently, the capacity for self-adjusting hyperparameters during on-line learning phases emerges as a goal. Many hyperparameters exhibit constraints and are confined within bounded search spaces, rendering specific solutions unacceptable upon applying optimization operators. To solve this issue, employing boundary constraint- handling techniques becomes imperative to rectify invalid solutions. This paper presents strategies for effectively managing boundary constraints within constrained numerical optimization problems. Recent methodologies, including heuristic and evolutionary-based optimization, employ a "boundary" strategy, wherein values that surpass boundary thresholds for a given hyperparameter are realigned to the respective limits. Our study introduces four strategies to navigate boundary constraints in online optimization algorithms. Through empirical investigations conducted on established datasets, we demonstrate that adopting boundary strategies outperforms the "boundary" strategy.

---


### 159. [Lifted Model Construction under Approximate Commutativity](https://arxiv.org/abs/2608.24713)

**<font color=#1a73e8>作者：</font>** Malte Luttermann, Jan Speller, Tanya Braun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifted inference algorithms enable scalable probabilistic inference even for large object domains by leveraging the indistinguishability of objects in a probability distribution. An essential prerequisite for constructing a lifted representation is to identify commutative factors, i.e., functions whose output values are invariant under permutations of a subset of their input values, in a potential-based factorisation. In practice, however, parameters learned from data inevitably deviate even if associated objects are indistinguishable, causing their corresponding factors to be only approximately commutative instead of being exactly commutative. We address this problem by introducing the concept of {\epsilon}-commutativity, a relaxation of commutativity where output values are only approximately invariant under permutations of input values. Specifically, we show how {\epsilon}-commutativity can be exploited for lifted model construction, downstream probabilistic inference, and prove strict bounds on the induced approximation error, thereby ensuring the practical applicability of lifted model construction while maintaining highly accurate query results. These theoretical guarantees are confirmed empirically, demonstrating comparable query accuracy at lower runtime.

---


### 160. [Deep Learning Super Resolution for Satellite Cloud Mask Downscaling](https://arxiv.org/abs/2608.24715)

**<font color=#1a73e8>作者：</font>** Angelos Georgakis, Valentina Kanaki, Giorgos Giannopoulos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A vast amount of optical satellite data is being transmitted to Earth-based servers every day, and more than half of this data is affected by haze or clouds. Additionally, this data suffers from the fundamental trade-off between spatial and temporal resolution, which remains largely unresolved, making the acquisition of continuous high-resolution satellite observations of clouds an ongoing challenge. This work addresses this challenge by proposing two Deep Learning super-resolution methods for the accurate downscaling of SEVIRI cloud mask products, as well as a novel cross-sensor cloud mask dataset called SEVMOD-CM, created by spatially and temporally matching MODIS and SEVIRI satellite observations. The two proposed models are a CNN-based (SpatialCNN) and a GAN-based (SpatialGAN) Neural Network. Trained on the SEVIRI spectral and cloud mask products, the proposed methods predict the corresponding MODIS Cloud masks, achieving a 4x spatial enhancement across sensor domains. Both approaches are evaluated experimentally, and compared against the standard bicubic interpolation upsampling technique. The experimental results demonstrate the value of the proposed models and dataset for the remote sensing community, highlighting the benefits of applying super-resolution techniques to geostationary-derived cloud mask products for applications such as atmospheric monitoring, weather forecasting, disaster risk reduction, solar energy forecasting, and climate research.

---


### 161. [Enhancing Bayesian Optimization and Active Learning Through Kernel Diversity](https://arxiv.org/abs/2608.24721)

**<font color=#1a73e8>作者：</font>** Heng Zhang, Haotian Xiang, Qin Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter selection remains a key challenge in Bayesian optimization (BO) and Bayesian active learning (AL), as model misspecification can lead to suboptimal performance, while more accurate fully Bayesian treatments typically rely on computationally expensive MCMC sampling. This paper proposes a unified framework, KENDO (Kernel ENsemble Disagreement-aware Operator), that integrates Ensemble Gaussian Processes (EGP) with disagreement-aware acquisition strategies. The central idea is to replace hyperparameter sampling with a kernel ensemble and adaptive Bayesian weighting, combined with disagreement-aware acquisition strategies. Within this unified framework, we instantiate KENDO-BO for BO and KENDO-AL for Bayesian AL, demonstrating that both arise from a common self-correcting mechanism with task-specific acquisition objectives. We further extend the approach to multi-objective optimization via random scalarization that preserves the single-optimizer conditioning structure. Thorough numerical tests on synthetic and real-world benchmarks across single-objective optimization, multi-objective optimization, and active learning demonstrate that (i) KENDO-BO achieves competitive or superior optimization performance compared to state-of-the-art methods while reducing computational overhead by up to $5\times$ and (ii) KENDO-AL achieves superior predictive calibration over MCMC-based active learning baselines with up to $27\times$ speedup.

---


### 162. [Interpretable Fundus Image Classification via Ring-Based Retinal Vasculature Features](https://arxiv.org/abs/2608.24723)

**<font color=#1a73e8>作者：</font>** Xiaoyan Li, Shixin Xu, Arvind Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal fundus photography is widely used for screening and monitoring ocular diseases, but many modern classification pipelines rely on deep latent representations and provide limited interpretability. This study develops an interpretable fundus image classification framework based on a ring-structured representation of the retinal vasculature centered on the optic disc. The method quantifies vessel geometry, color appearance, oxygenation-related vascular appearance, and vessel--background entropy within concentric retinal regions. These physiologically motivated descriptors are derived from vessel masks, image intensities, and optical-density measurements and aggregated across rings to capture spatial variation in vascular properties. Using only quantitative vascular descriptors, the proposed method achieved strong classification performance across three public fundus datasets. On HRF, it achieved 91.1\% accuracy using automatically generated vessel masks, matching RETFound, a vision transformer pretrained on large-scale retinal fundus image data, under the same evaluation setting. Additional analyses suggest that pretrained image models are sensitive to acquisition-related spatial cues, including fundus scale and retinal position within the field of view, as well as broader non-vessel image characteristics. This framework may support interpretable disease classification, quantitative retinal phenotyping, and retinal biomarker discovery without requiring large task-specific training datasets.

---


### 163. [Arbitrary Polygon Oscillator: Generalizing Polygonal Synthesis to Arbitrary Shapes, Morphing, and Three-Dimensional Polyhedra](https://arxiv.org/abs/2608.24726)

**<font color=#1a73e8>作者：</font>** Antonio Argentieri, Francesco Scagliola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Polygonal synthesis generates audio by traversing the perimeter of a polygon with a phasor; prior work uses a constant angular velocity, whereas the proposed system adopts constant arc-length (perimeter) velocity. Existing formulations operate on regular, parametrically defined polygons, producing smooth timbral transitions within a single family of shapes.
This paper generalizes polygonal synthesis around a unified arc-length engine: vertex data of any origin feed the same DSP pipeline. First, we adapt the oscillator to accept arbitrary vertex configurations from an external buffer, opening the possibility for a broad class of closed polygons -- regular, irregular, or star-shaped -- to function as a waveform generator. Second, a hybrid interpolation algorithm enables smooth morphing between polygons with unequal vertex counts, passing through intermediate shapes that have no parametric description. Third, we extend the paradigm to three dimensions: a convex polyhedron rotated about three axes is sliced by a fixed horizontal plane, and the resulting cross-section yields a continuously variable polygon controlled by the solid's orientation. The system runs in RNBO (Cycling~'74) with a geometry caching strategy that avoids per-sample recomputation. Antialiasing combines a four-point polyBLAMP correction derived from runtime Bézier tangents with adaptive oversampling, adapting the correction geometrically to general vertex configurations without per-shape analytical derivation.

---


### 164. [Parameter-Efficient Self-Supervised Adaptation for EEG-FM under Fixed Computational Budgets](https://arxiv.org/abs/2608.24727)

**<font color=#1a73e8>作者：</font>** Meghal Dani, Stefanie Liebe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models pretrained via self-supervised learning promise transferable representations, but their generalization remains limited, especially across diverse clinical datasets. Full fine-tuning is impractical for resource-constrained clinical settings due to high computational requirements. In this work, we investigate whether parameter-efficient self-supervised adaptation, updating only 9% of parameters suffices to align representations to target tasks. We evaluate our method on two state-of-the-art models with different pretraining objectives: BIOT (contrastive) and CBraMod (masked reconstruction), and evaluate on three clinical EEG datasets for abnormality detection (TUAB), event classification (TUEV), and seizure detection (CHB-MIT) under both in-distribution and out-of-distribution conditions. SSL adaptation yields consistent gains over linear probing, up to 20x AUCPR. Under a fixed compute budget, peak performance requires only 20--50% of available unlabeled data. Critically, when total window count is fixed, performance remains invariant to patient count, suggesting that performance is dependent on overall temporal window diversity only. Our findings demonstrate that parameter-efficient adaptation enables effective deployment of EEG Foundation models (EEG-FM) with minimal computational overhead and data collection burden. Code available at: this https URL

---


### 165. [Optimal Alternating Regret for Online Learning and Games](https://arxiv.org/abs/2608.24731)

**<font color=#1a73e8>作者：</font>** Yixin Tao, Weiqiang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We settle the minimax-optimal alternating regret, a regret notion motivated by alternating learning dynamics in games, for both online linear optimization (OLO) and online convex optimization (OCO).
For OLO over the probability simplex $\Delta_d$, we give an algorithm with $O(\log d)$ alternating regret that remains a constant for any time horizon $T$, and a matching lower bound. Our constant regret bound significantly improves previous results with $O(\log ^{2/3}d \cdot T^{1/3})$ regret [Cevher, Cutkosky, Kavis, Piliouras, Skoulakis, Viano, NeurIPS 2023, Hait, Li, Luo, Zhang, COLT 2025]. As a result, we obtain alternating learning dynamics with $O(\log d /T)$ convergence to Nash equilibria in two-player zero-sum games and $O(\log d /T)$ convergence to coarse correlated equilibria in two-player general-sum games. This is the first uncoupled learning dynamics with $O(1/T)$ convergence to CCE in two-player general-sum games, while all prior works suffer additional $\log T$ factors.
For general OCO over a $d$-dimensional compact convex set, we give an algorithm with $O(d\log (1+T/d))$ alternating regret, improving the previous best of $\widetilde{O}(d^{2/3}T^{1/3})$. We also prove a matching lower bound of $\Omega(d\log (1+T/d))$, showing that the $\Omega(\log T)$ factor is unavoidable.

---


### 166. [TorchMorph: CUDA-accelerated Morphological Transforms](https://arxiv.org/abs/2608.24738)

**<font color=#1a73e8>作者：</font>** Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphological transforms are long-standing tools for shape and mask processing, but the de facto reference implementation in the Python ecosystem, i.e. this http URL, is CPU-only, single-array, and therefore unusable inside a GPU training loop without an expensive device-to-host round trip. GPU vision libraries built on PyTorch cover a narrow subset of these operators, typically restricted to two spatial dimensions and flat structuring elements. We present TorchMorph, a lightweight PyTorch extension that closes this gap. TorchMorph exposes 22 public operators covering binary morphology, greyscale morphology, exact and approximate distance transforms, and entropy-regularised optimal transport, all implemented as fused CUDA kernels that operate directly on (B, C, Spatial...) CUDA tensors with up to eight spatial dimensions. The API deliberately mirrors this http URL argument-for-argument, including border modes, structuring-element origins and pre-allocated outputs, so that existing pipelines port with a change of import. We describe the layered architecture and the kernel designs behind each operator family. Against single-threaded CPU references, batched execution reaches up to 1.1e3 times the throughput of this http URL on greyscale morphology and up to 350x on exact Euclidean distance transforms, while the Sinkhorn solver runs up to 42x faster than POT. Binary and chamfer operators reproduce their SciPy counterparts exactly, and every float-valued operator agrees with the CPU reference to within 1.8e-6 absolute error. TorchMorph is released under the MIT licence at this https URL.

---


### 167. [$(\text{DNN})^2$: Doubly Non-Negative Relaxations for Deep Neural Networks](https://arxiv.org/abs/2608.24743)

**<font color=#1a73e8>作者：</font>** Hanna Jiamei Zhang, Alan Papalia, Michael Everett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing linear program (LP) and semidefinite program (SDP) relaxations for rectified linear unit (ReLU) neural network (NN) verification yield overly-conservative safety guarantees due to significant relaxation gaps. While the completely positive program (CPP) formulation closes this gap, it is NP-hard to solve. Its cheapest tractable relaxation, the doubly non-negative program (DNN), retains critical constraints as an SDP, but one whose size exceeds the reach of interior-point methods at practical scale. While Burer-Monteiro (BM) factorization has been applied to make SDP-based verification scalable, no such result exists for the strictly tighter DNN formulation. A key obstacle is that additional non-negativity constraints in the DNN cause dual multipliers for optimality certification to be non-unique, making standard certification methods inapplicable. We propose a novel eigenvalue maximization procedure that searches the non-unique multiplier space for a valid certificate, i.e. a global optimality guarantee. Experiments demonstrate that our approach $(\text{DNN})^2$ produces bounds consistently tighter than the standard SDP method, often matching the exact solution, and that our certification procedure confirms global optimality when a valid certificate exists. These results are a key step toward providing tight, certifiable, and computationally scalable verification guarantees needed to deploy neural network controllers and perception modules in safety-critical autonomous systems.

---


### 168. [Weakly Supervised Seafloor Segmentation for Seagrass Habitat Mapping in Side-Scan Sonar Imagery](https://arxiv.org/abs/2608.24756)

**<font color=#1a73e8>作者：</font>** Hayat Rajani, Nuno Gracias, Rafael Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Seagrass meadows are crucial blue-carbon habitats, and mapping their extent is a prerequisite for coastal management and carbon inventory. Optical satellite sensors cover large areas but cannot reach deep or turbid water, whereas side-scan sonar (SSS) images the seabed at high resolution and at any depth. Interpreting SSS, however, still relies on dense manual annotation, which is slow and costly. We address this by adapting a weakly supervised semantic segmentation framework to SSS benthic habitat mapping, so that pixel-level maps are learned from image-level labels alone. The framework couples a ViT-based encoder-decoder with a classification branch, extracts class activation maps, and refines them into pseudo-labels with a dense conditional random field that we tune for the noise and weak boundaries of acoustic imagery. It follows an iterative self-training scheme, together with a sampling strategy to cope with the strong class imbalance of the data. We also study the effect of different loss functions on segmentation quality, finding Lovász-Softmax loss the most effective. On a held-out transect, the refined pseudo-labels reached an mIoU of 89.3\% against the ground truth, and the segmentation branch, trained without any pixel-level labels, reached 87.6\%. Self-supervised pretraining on unlabelled SSS added a further 3\% in mean intersection-over-union. Field trials further demonstrate the generalizability of the trained model. These results show that accurate and label-efficient benthic habitat mapping from side-scan sonar is feasible at the scale needed for coast-wide seagrass monitoring.

---


### 169. [ICS Cybersecurity Datasets: A Systematic Meta-Review of Coverage, Evaluation Practice, and Structural Gaps](https://arxiv.org/abs/2608.24757)

**<font color=#1a73e8>作者：</font>** Konstantinos E. Kampourakis, Vyron Kampourakis, Georgios Kambourakis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection research in Industrial Control Systems (ICS) heavily depends on public datasets, yet no prior work has systematically assessed whether the collective dataset corpus supports current evaluation claims. This paper addresses this gap through a meta-review of 18 studies between 2019 and 2026, from which 83 ICS, or ICS directly related, cybersecurity datasets are identified, harmonised, and characterised using a unified five-dimensional taxonomy. The taxonomy reveals that the corpus is structurally skewed: 85.5% of datasets concentrate on late-stage OT Disruption tactics, cross-stage IT/OT progression sequences are present in only 8.4% of cases, field-device evidence at Level 0 of the Purdue hierarchy is effectively absent, and operationally sourced data accounts for only 15.7% of the collection. A parallel audit of evaluation practices shows that zero report streaming evaluation, fewer than half apply disciplined train/test partitioning, and only two satisfy reproducibility requirements. Furthermore, a taxonomy-evaluation coupling analysis shows that dataset imbalances constrain the scope and feasibility of several evaluation practices. Based on these findings, we identify three structural imbalances: i) architectural shallowness, ii) progression compression, and iii) cross-domain substitution, and derive a coordinated research agenda which covers cross-stage corpus construction, temporally structured benchmarking, event-level label standards, and governance frameworks for operational data sharing.

---


### 170. [IDeaL: Data-Free Multi-Teacher Distillation via Improved Dead Leaves](https://arxiv.org/abs/2608.24759)

**<font color=#1a73e8>作者：</font>** Feyza Yavuz, Mert Bülent Sarıyıldız, Diane Larlus  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-teacher distillation has emerged as a way to combine complementary teacher models into a single student model that exhibits the strengths of all its teachers. The student is trained to mimic the output of the teachers on a set of images, typically the union of the individual teacher's training sets, assuming this data is available. In this paper, we question that assumption and explore alternative options. We first study how far one can go when distilling from teachers fed with different types of noise. Then, we show that information contained in the teachers can be leveraged to tailor the noise for multi-teacher distillation: we propose a method that, thanks to decorrelation losses at both patch and image levels, generates teacher-specific, improved samples optimized for data-free distillation. Experiments show that our most effective samples, IDeaL, lead to strong students that successfully capture complementary information from the teachers, yielding surprisingly competitive results that substantially narrow the gap with students distilled from real images. Moreover, given a limited budget of 1K images for distillation, students distilled using our IDeaL samples match or surpass the performance of those distilled using a 1K-image subset of ImageNet.

---


### 171. [ExpConCAD: Experience-Guided Text-to-CAD Generation from Shape Descriptions with Implicit Spatial Constraints](https://arxiv.org/abs/2608.24760)

**<font color=#1a73e8>作者：</font>** Jingyao Liu, Jinkang Tang, Chen Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-CAD aims to generate executable CAD programs from natural-language descriptions. However, real-world descriptions are often underspecified and omit critical spatial constraints required for valid CAD construction, a challenge that has been largely overlooked by existing methods. In this paper, we argue that missing spatial constraints should be inferred with respect to the underlying construction structure and informed by reusable design experience. Based on this insight, we propose ExpConCAD, an experience-enhanced framework for implicit spatial constraint completion. ExpConCAD first recovers the intended construction structure and constraint scopes, then retrieves relevant constraint-completion experience for similar scopes to complete the missing spatial constraints, and finally generates executable CadQuery programs. Extensive experiments demonstrate the effectiveness of ExpConCAD and provide insights into the role of construction structure understanding and experience memory in spatial constraint completion. Our code is available at: this https URL.

---


### 172. [Beyond Uniform Local Isometry and Topology: FactoMap for Disentangled Representations](https://arxiv.org/abs/2608.24762)

**<font color=#1a73e8>作者：</font>** Sohini Gupta, Bahareh Tolooshams  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many disentanglement methods represent generative factors using Euclidean product coordinates, although the underlying factor spaces may wrap, collapse, or have position-dependent geometry. We introduce factor-space structure, combining factor domains, generator-induced identifications, and position-dependent scales to distinguish topologically equivalent spaces with different factor geometries. We show that statistically independent factors need not be geometrically separable: hue and scale produce effects that grow at different rates, yielding anisotropy that no fixed rescaling removes. We propose the Factor-Space Topographic Map (FactoMap), which learns interpretable prototypes indexed by a factor-space lattice. Topographic learning transfers the lattice's periodicity, collapses, and non-uniform extent to the representation. Experiments show that matching this structure preserves factor continuity and enables disentanglement of the underlying factors.

---


### 173. [Ensemble of Convolutional Neural Networks for StrokePrediction: Towards Improved Diagnostic Accuracy](https://arxiv.org/abs/2608.24771)

**<font color=#1a73e8>作者：</font>** Md Shahriar Sajid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain stroke, known for its high mortality and incidence rates, poses significant health risks and requires rapid intervention for survival. Early diagnosis and preventive measures can greatly reduce life loss and disabilities. Recent advancements in deep learning have led to novel computer-aided diagnostic techniques for early stroke detection. This study proposes an intelligent system that predicts potential strokes using eleven features, evaluated through seven supervised machine learning algorithms. The process includes a literature review, dataset visualization, data preprocessing, and model evaluation. Ensemble methods like Random Forest, Stacking Classifier, and Bagging Classifier achieved high accuracies of 99.52%, while Decision Tree reached 98.24%. Other models, including KNN and TabNet, demonstrated reliable performance, achieving accuracies of 96.73% and 96.49%, respectively. The custom feedforward model achieved 94.91%, while SVC and logistic regression had lower accuracies at 88.06% and 77.03%. The results highlight the effectiveness of ensemble methods in stroke classification.

---


### 174. [Linear Probing Provides Robust and Efficient Detection of Machine-Generated Text](https://arxiv.org/abs/2608.24780)

**<font color=#1a73e8>作者：</font>** Gerrit Quaremba, Hanqi Yan, Elizabeth Black 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distinguishing machine-generated text (MGT) from human-written text (HWT) becomes increasingly important due to potential misuse. However, most supervised detectors often degrade out-of-domain (OOD) and require large, diverse training sets. In this work, we analyze the linearity and quality of MGT representations and show that simple linear probes outperform a wide range of detectors while being substantially more sample-efficient. We first show that MGT and HWT latent representations are linearly separable in low-dimensional space, and provide a plausible explanation for this separability through systematic differences in their representation quality. Motivated by these insights, we train two variants of simple linear probes and evaluate them across 4 benchmarks against 16 baselines. Probes consistently improve OOD detection (+11 AUC), requiring solely ${<}100$ samples to reach near-peak performance. We show that this transferability arises because probes recover a shared latent MGT direction that generalizes across diverse settings. Finally, we demonstrate that probing vectors capture a continuous spectrum of ``machineness'', highlighting their potential for fine-grained estimation of AI-edited text. Overall, our work provides insights into latent-space differences between MGT and HWT and demonstrates the potential of linear probes as as robust and sample-efficient MGT detectors. We release our code on~\href{this https URL}{github}.

---


### 175. [Image Difference Quantification Using Autoencoder-Based Latent Representations](https://arxiv.org/abs/2608.24782)

**<font color=#1a73e8>作者：</font>** Manish Sharma, Timothy Yim, Clifton Forlines  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional image similarity metrics such as Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR), and the Structural Similarity Index Measure (SSIM) rely on pixel-level comparisons and often fail to capture perceptually meaningful differences between images. In contrast, latent representations learned by deep neural networks encode high-level semantic information that is more closely aligned with human visual perception. This paper proposes a convolutional autoencoder-based framework for quantifying image differences using cosine similarity in latent space. The learned compact embeddings enable robust differentiation between visually distinct images under variations in illumination, pose, and background. Extensive evaluation on dog-cat images and additional cross-domain datasets demonstrates clear class-wise clustering and strong inter-class separability in the latent space, with 98.4% of dog-cat image pairs exhibiting similarity scores below 0.5. Further validation using the TID2013 dataset shows that latent-space distance correlates positively with human Mean Opinion Scores (MOS), demonstrating sensitivity to perceptually relevant image distortions. The proposed approach provides a computationally efficient and semantically grounded alternative to conventional pixel-based similarity metrics, with potential applications in content-based retrieval, perceptual quality assessment, and semantic similarity analysis.

---


### 176. [Test-Time Collaborative Classification over Multi-Agent Networks](https://arxiv.org/abs/2608.24787)

**<font color=#1a73e8>作者：</font>** Ping Hu, Mert Kayaalp, Ali H. Sayed  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The increasing heterogeneity of multi-agent systems poses significant challenges for jointly training a global model across agents. At the same time, cooperative inference between agents has long been recognized as a powerful mechanism for distributed decision making over networks. Motivated by these observations, we propose a collaboration framework for distributed binary classification over multi-agent networks, where a set of independently trained agents, potentially differing in architecture, feature space, or modality, coordinate their actions during test time to form collective predictions. This coordination is achieved by exchanging local decision statistics through a distributed learning protocol. We develop a theoretical and experimental study of this independent training and cooperative inference paradigm, and examine its performance under different communication budgets and distributed learning rules. We establish classification error guarantees under sufficient, finite-round, and finite-precision communication, together with PAC-style generalization bounds. These results capture the influence of model heterogeneity, network topology, combination policy, and communication constraints on prediction accuracy. Taken together with the experimental results, they reveal both the price of independent training and the benefit of collective prediction for the proposed distributed decision making framework with models learned from data.

---


### 177. [Ten Years Later: Replicating Two Color Discrimination Studies](https://arxiv.org/abs/2608.24789)

**<font color=#1a73e8>作者：</font>** Shadmaan Hye, Andrew M. McNutt, Katherine E. Isaacs  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Color discrimination is a fundamental aspect of visualization as it influences how people interpret visual encodings. Many visualization guidelines are informed by perceptual studies, yet relatively few have been replicated. Acknowledging that the interaction between human perception, visual tasks, and display technology can change over time, we replicate two crowdsourced color discrimination studies conducted 10 years earlier. Specifically, we replicated a visualization-focused color discrimination task (N=144) and a more general perceptual discrimination task (N=394). In both studies, our results reproduced the original perceptual effects. We further use the replication to investigate whether color-related practice influences color discrimination. Specifically, we extended our replication studies by adding questions about participants' engagement with color practices. We then examined whether diverse color-related practices (e.g., artistic hobbies, knowledge of color theory, and cosmetic makeup use) influenced color discrimination. We found no significant difference between participants who reported engaging in color-related practices and those who did not, suggesting that design guidance regarding color discrimination may generalize across viewers regardless of their regular color practice.

---


### 178. [EMFE: A lightweight, explainable machine learning framework for malaria cell classification](https://arxiv.org/abs/2608.24793)

**<font color=#1a73e8>作者：</font>** Md Abdullah Al Kafi, Walayat Hussain, Mousumi Karmakar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated malaria diagnosis from stained blood-smear microscopy is dominated by deep convolutional neural networks that are accurate but computationally expensive, poorly interpretable, and rarely validated with patient-level rigor. We present EMFE (Efficient Mathematical Feature Extraction), a five-feature framework for classifying single red-blood-cell images as parasitized or uninfected using Gray World color normalization, adaptive green-channel thresholding, morphological spot detection, and classical machine learning. Using the NIH LHNCBC malaria dataset (27,558 images from 200 patients), we evaluate Random Forest, Histogram Gradient Boosting, and Support Vector Machine classifiers under patient-grouped nested cross-validation (K_outer=20, K_inner=3), ensuring that cells from each patient remain within a single fold. The optimized Random Forest achieves 94.6% pooled out-of-fold accuracy (95% CI [93.6, 95.7]), corroborated by an untouched 40-patient holdout test (94.3%) and a patient-level permutation test (p<0.001, 1,000 permutations). Ablation experiments quantify the contribution of individual features and pipeline stages. Hardware-matched comparisons with retrained DenseNet121, ResNet50, and MobileNetV2 models assess the accuracy-efficiency trade-off. Synthetic perturbations characterize three failure modes, while explainability analysis identifies spot saturation as the dominant discriminative feature. Patient-level aggregation further quantifies sensitivity-specificity trade-offs and false-positive accumulation. These results demonstrate a statistically rigorous, interpretable, and computationally lightweight alternative to deep learning, while explicitly quantifying its limitations.

---


### 179. [CAFE: Self-Improving Search Agents Need Co-Evolving Feedback](https://arxiv.org/abs/2608.24794)

**<font color=#1a73e8>作者：</font>** Boyang Liu, Senjie Jin, Peixin Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome-supervised search agents learn when and how to retrieve evidence, but terminal rewards neither localize intermediate errors nor redirect an ongoing trajectory before those errors compound. Treating corrective feedback as a learned in-trajectory intervention couples the two roles: the agent must decide when to request and use feedback, while the critic must infer useful corrections from outcome-confounded rollouts whose failure patterns shift as the agent improves. We introduce CAFE (Coupled Agent--Feedback Evolution), a framework in which a shared-parameter model alternates between search-agent and critic roles. CAFE initializes feedback-conditioned recovery from trajectories built around the base agent's own failures, then couples online and offline optimization. During online RL, a comparative feedback estimate uses a prompt-level call--skip success gap to shape request returns, while feedback-aware advantage shaping reweights token advantages before and after feedback. Offline, rollout-derived preference optimization learns feedback from matched successful and unsuccessful trajectories. On seven agentic search benchmarks, CAFE outperforms the evaluated RL-based search agents on average, retains its gains across all six out-of-domain benchmarks, and reduces answer-level hallucinations. One-sided ablations show that improving only the agent or only the critic eventually plateaus, whereas alternating the two updates continues to improve performance. These findings suggest that a self-improving search agent needs feedback that co-evolves with the policy it guides.

---


### 180. [LION: A Clifford Neural Paradigm for Multimodal-Attributed Graph Learning](https://arxiv.org/abs/2608.24795)

**<font color=#1a73e8>作者：</font>** Xunkai Li, Zekai Chen, Zhengyu Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, the rapid advancement of multimodal domains has driven a data-centric paradigm shift in graph ML, transitioning from text-attributed to multimodal-attributed graphs. This advancement significantly enhances data representation and expands the scope of graph downstream tasks, such as modality-oriented tasks, thereby improving the practical utility of graph ML. Despite its promise, limitations exist in the current neural paradigms:(1) Neglect Context in Modality Alignment: Most existing methods adopt topology-constrained or modality-specific operators as this http URL aligners inevitably neglect graph context and inhibit modality interaction, resulting in suboptimal alignment.(2) Lack of Adaptation in Modality Fusion: Most existing methods are simple adaptations for 2-modality graphs and fail to adequately exploit aligned tokens equipped with topology priors during fusion, leading to poor generalizability and performance this http URL address the above issues, we propose LION (c\underline{LI}ff\underline{O}rd \underline{N}eural paradigm) based on the Clifford algebra and decoupled graph neural paradigm (i.e., propagation-then-aggregation) to implement alignment-then-fusion in multimodal-attributed graphs. Specifically, we first construct a modality-aware geometric manifold grounded in Clifford this http URL geometric-induced high-order graph propagation efficiently achieves modality interaction, facilitating modality this http URL, based on the topology-aware Clifford components of aligned tokens, we propose adaptive holographic aggregation. This module integrates component-wise energy and propagation-scale information with learnable parameters to improve modality fusion. Extensive experiments on 9 text-image MAG datasets demonstrate that LION significantly outperforms SOTA baselines across 3 graph and 3 modality downstream tasks.

---


### 181. [Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch](https://arxiv.org/abs/2608.24809)

**<font color=#1a73e8>作者：</font>** Rima Hazra, Sayan Layek, Somnath Banerjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Crase, a bounded and inspectable alternative to deep research agents for scholarly search. Instead of an open-ended search loop, Crase queries a search engine once for seed papers, expands them along their 1.5-hop citation neighborhood, prunes citation edges whose claims lack entailment support, and ranks the remaining papers with a recency-aware random walk. This makes the candidate set, the reason each paper is kept, and the stopping condition explicit and fixed before inference. On LitSearch and one further benchmarks over a 500K-paper arXiv corpus, Crase outperforms deep research agents built on proprietary models by up to 3$\times$ recall@50 at roughly a third of the cost.

---


### 182. [Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core](https://arxiv.org/abs/2608.24810)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has applied Mamba style state space models (SSMs) to video anomaly detection, yet existing approaches still rely on buffering clips or windows internally, lack a theoretical account of how temporal memory relates to detection latency, and benchmark efficiency only through GPU throughput rather than the edge hardware these methods are intended to target. We introduce a strictly causal streaming anomaly detector whose fixed size state is updated in O(1) time and memory per incoming frame, with no lookahead and no clip buffering. Its temporal core is a diagonal linear state space recurrence with an input and state dependent decay gate, trained self supervised through causal next embedding prediction on a frozen visual backbone. We derive a closed form relationship between the recurrence decay spectrum and both detection delay and the shortest anomaly it can reliably capture, then validate empirically on UCSD Ped2 and CUHK Avenue. The settling delay bound predicted from the learned base decay (57 to 59 frames) sits far above the measured detection delay (1.6 and 18.4 frames), showing that the event boundary gate, not the base decay, governs responsiveness. We further report end to end latency and throughput measured directly on Apple M3 Pro hardware, 0.74 ms and 0.77 ms per frame (over 1300 FPS), rather than simulated GPU numbers. With an untuned initial configuration the method reaches 67.9 percent and 70.2 percent frame level AUC on Ped2 and Avenue, trailing prior non causal SSM baselines in accuracy. Ablations over decay rate, state size, and gating reveal that the gate contribution is dataset size dependent, hurting accuracy on the smaller Ped2 training set but helping on the larger Avenue one. Closing this accuracy gap and extending evaluation to a third, larger benchmark are immediate next steps.

---


### 183. [MDTE: Minority-Aware Diffusion over Temporal Edge Events for Imbalanced Node Classification](https://arxiv.org/abs/2608.24812)

**<font color=#1a73e8>作者：</font>** Zhou Zelong, Zhang Tianming, Yang Zhengyi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-imbalanced node classification on temporal graphs is challenging because majority-dominated temporal propagation progressively assimilates minority representations, while conventional node and neighborhood information provides insufficient discriminative evidence for minority classes. To address these issues, we propose MDTE, a minority-aware diffusion framework that reconstructs stable and discriminative temporal edge-event representations through conditional diffusion denoising. Specifically, MDTE introduces Distribution-Aware Selective Propagation, which combines Local Outlier Factor (LOF)-based propagation filtering with cluster-aware low-frequency propagation. The module preserves informative neighborhood dependencies while mitigating harmful propagation and majority-class information assimilation. It further develops Multi-View Discriminative Fusion, which exploits feature reconstruction and topology prediction to characterize class-wise differences in distribution learning and extracts complementary discriminability signals to guide denoising. Experiments on five real-world datasets demonstrate that MDTE consistently achieves the best performance on minority-class-oriented metrics, improving minority-class recall by up to 23.53 percentage points, minority-class F1 by 8.68 percentage points, and AUPRC by 2.67 percentage points over the strongest baselines.

---


### 184. [A Geometric Theory of Robust Fairness Audits](https://arxiv.org/abs/2608.24818)

**<font color=#1a73e8>作者：</font>** Binita Maity  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neighborhood-based fairness audits evaluate individual fairness by comparing predictions among similar individuals in feature space. Despite their widespread use, little is known about the robustness of the auditing procedure itself. Because these audits rely on nearest neighbor relationships, small perturbations in feature space can alter local neighborhoods and produce different fairness assessments even when model predictions remain unchanged. We develop a geometric framework for analyzing the robustness of neighborhood-based fairness audits under bounded perturbations. Our analysis establishes sufficient conditions for neighborhood invariance, quantifies how neighborhood replacement propagates to audit instability, and introduces audit volatility, a measure of the expected sensitivity of fairness audits under repeated perturbations. Experiments on benchmark datasets support the theoretical analysis and show that the proposed framework explains the observed stability of neighborhood-based fairness audits.

---


### 185. [BioKERN: Biological Kernel Regularization for Histology-to-Transcriptomics Neighborhood Retrieval](https://arxiv.org/abs/2608.24823)

**<font color=#1a73e8>作者：</font>** Seungik Cho, Betul Orcan-Ekmekci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatially resolved biology requires representations that preserve biological neighborhood structure rather than only exact cross-modal correspondences. Existing histology--transcriptomics objectives can emphasize instance-level matching even when non-paired spots share molecular or spatial context. We introduce BioKERN, a multimodal spatial representation-learning framework that incorporates biological structure as an explicit, learnable inductive bias. BioKERN constructs a training-time biological kernel by combining transcriptomic similarity and spatial proximity, then uses it to provide graded neighborhood supervision and regularize embedding geometry. Evaluation uses a fixed, model-independent biological neighborhood definition shared by all methods. Across Mouse Brain Visium and Human Liver GSE240429, BioKERN consistently improves biological-neighborhood retrieval over BLEEP in both single- and multi-scale settings. Controlled shared-architecture experiments show that most of the improvement arises from biological-kernel regularization rather than increased model capacity. These results support explicit biological geometry as an interpretable inductive bias for multimodal learning in spatial biology.

---


### 186. [LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training](https://arxiv.org/abs/2608.24845)

**<font color=#1a73e8>作者：</font>** Andreas Hochlehnert, Marianna Nezhurina, Mehdi Cherti 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a total duration of 10 million hours. The dataset is designed for multimodal pre-training across the video, audio, and image modalities. Using content-aware scene detection, we extract clips for which we synthetically generate video and audio captions. Models trained on these data achieve competitive performance on standard video-text and audio-text benchmarks, with consistent improvements as training or model scale increases. Additionally, we explore video frames as an alternative source of image-text data by extracting scene-changing frames. These frames exhibit a visual distribution distinct from standard web image corpora, and models trained on this dataset achieve strong image-text retrieval performance. We release LAION-BVD to the research community. It significantly expands open access to multimodal videos at an unprecedented scale.

---


### 187. [FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs](https://arxiv.org/abs/2608.24846)

**<font color=#1a73e8>作者：</font>** Md Saikat Islam Khan Bappy, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world data for knowledge graph question answering is often distributed across different organizations due to governance and data sovereignty constraints. While centralized systems exist, they cannot answer multi-hop questions when the required facts are split across vertically partitioned silos. In this paper, we propose FedV-KGQA, a framework for multi-hop reasoning over knowledge graphs in which organizations share entities but own disjoint sets of relations. Our approach combines local graph enrichment and knowledge graph embeddings to ensure raw triples and relation parameters never leave each silo, establishing a structural data boundary without requiring centralized graph access. We further introduce a topic entity anchoring mechanism that grounds questions in the correct graph neighborhood without any runtime inter-silo communication. We evaluate 12 model configurations across three benchmarks and show that FedV-KGQA performs strongly, remains close to centralized performance, generalizes to 3-hop reasoning, and is robust to embedding perturbations.

---


### 188. [Research Methodologies for Cybersecurity in Enterprise Environments: A Narrative Review, Synthesis and Executable Guide](https://arxiv.org/abs/2608.24850)

**<font color=#1a73e8>作者：</font>** Tran Duc Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise cybersecurity research draws on a wider range of methods than any single community routinely teaches. Researchers face a selection problem before they face a technical one: a study may simultaneously need a systematic review, a design-science artifact, a controlled detection experiment, an interview study, or an attack-graph model. This paper addresses that problem in two ways. First, it provides a narrative review and synthesis of methodological practices across a verified corpus of 151 works. We organise these practices into eleven methodology families, detailing for each what questions it answers, the strength of its supporting evidence, and its common failure modes. Second, we convert each family into an executable protocol comprising ordered steps, required instruments, evaluation criteria, common validity threats, and a reporting checklist. Every protocol is also visually mapped to make the sequence, decisions, and threats legible at a glance. We also treat contradictions in the literature as evidence. For example, reported rankings of intrusion-detection algorithms are wildly inconsistent across individually careful studies. We argue this pattern is most parsimoniously explained by variations in evaluation design rather than the algorithms themselves, as these studies differ in design dimensions known to shift results by more than the margins separating the algorithms. Ultimately, the evidence supports methodological pluralism disciplined by explicit validity reasoning. We conclude that researchers must match their evaluation design to the decision under study, triangulate technical against organisational evidence, explicitly state the population a result generalises to, and report the conditions under which the result would not hold.

---


### 189. [LeFlow: Generative Latent Flow Planning for World Models](https://arxiv.org/abs/2608.24855)

**<font color=#1a73e8>作者：</font>** Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator. This approach pays the full iterative optimization cost anew at every replanning step and reuses no planning experience across queries. In this work, we ask whether planning itself can be amortized once a latent world model has been learned. We present LeFlow, which learns a reusable latent trajectory prior operating directly in the latent dynamics space from the world model. LeFlow recasts planning as conditional latent trajectory generation: a rectified-flow model imagines a future latent path between the current and goal embeddings, an inverse dynamics decoder turns latent transitions into action chunks, and the frozen world model verifies each candidate by autoregressive rollout. Across four major goal-conditioned pixel-control benchmarks, LeFlow replaces iterative action-space optimization with amortized latent planning and fixed-budget rollout selection, achieving consistent success-rate gains with an order-of-magnitude reduction in planning time. Our results argue that latent world models should support not only prediction but reusable planning priors. Our code is available at this https URL.

---


### 190. [Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement Learning](https://arxiv.org/abs/2608.24858)

**<font color=#1a73e8>作者：</font>** Lars van der Laan, Nathan Kallus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Marginalized importance weighting evaluates a target policy by reweighting offline state-action samples with its discounted occupancy ratio, characterized by an adjoint Bellman equation. Existing minimax, primal-dual, and fitted fixed-point estimators can leave residual occupancy-balance violations because of function-class approximation, regularization, or incomplete optimization. These violations are difficult to diagnose and reduce because the objectives generally lack a direct supervised validation loss for hyperparameter tuning, model selection, and early stopping. We introduce isotonic Bellman calibration, a one-dimensional, model-agnostic post-processing method that reduces these violations while preserving the ranking information in any initial occupancy-ratio estimate. The method corrects the estimate's scale and shape by applying fitted occupancy-ratio evaluation (FORE) over a one-dimensional class of nondecreasing transformations. We characterize Bellman calibration as a conditional fixed-point property equivalent to occupancy-balance against every test function of the calibrated ratio. More generally, we derive a calibration-refinement bound showing that any fitted ratio with small calibration error performs nearly as well as the best post-processing based on its fitted values. For isotonic Bellman calibration, we establish finite-sample calibration guarantees and a KL oracle inequality relative to the best monotone transformation of the initial estimate. Consequently, isotonic Bellman calibration achieves small calibration error and KL risk within statistical error of the best monotone correction, with guarantees for downstream target-occupancy functionals, including policy-value estimation.

---


### 191. [Improving Cross-Problem Vehicle Routing with Locally Augmented Preferences and Representation Disentanglement](https://arxiv.org/abs/2608.24859)

**<font color=#1a73e8>作者：</font>** Arthur Corrêa, Paulo Nascimento, Samuel Moniz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task vehicle routing problem (VRP) solvers seek to handle multiple VRP variants within a single unified model, avoiding the need to train a separate model for every variant. In spite of recent progress, current approaches remain limited on two fronts. On the training side, reinforcement learning suffers from reward-scale disparities and shrinking advantage signals as policies improve, whereas preference optimization stagnates once sampled tours become near-identical and thus fundamentally limited by the quality of the policy's own generated solutions, leaving both paradigms with weak supervision as training progresses. On the architecture side, existing fully shared encoders entangle constraint-dependent representations across heterogeneous variants, which limits generalization. We address these gaps with two model-agnostic contributions. First, we propose Preference Optimization with Locally Augmented Refinement (POLAR), a novel training algorithm that applies a local search refinement pass to the best decoded tour before forming preference pairs, yielding much more informative pairwise margins. Second, a Progressive Layered Extraction (PLE) encoder routes each encoder layer through one shared expert and a set of task-specific experts via a gating mechanism, progressively separating common routing structure from constraint-specific encodings. Through extensive experiments on various VRP variants, we show that POLAR and PLE together elevate the current state-of-the-art among neural multi-task solvers. We reduce the average gap to reference solutions by 21.3% relative to the strongest published baseline on 16 in-distribution variants, and outperform prior neural methods on 27 out of 32 unseen variants. Ablation studies confirm the efficacy of each contribution, showing that both improve cross-problem generalization across multiple backbone model architectures.

---


### 192. [SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL](https://arxiv.org/abs/2608.24870)

**<font color=#1a73e8>作者：</font>** Kai Ruan, Jinghao Lin, Qianshan Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before optimizing a token-mean actor loss. We show that trajectory centering generally does not center the token-weighted quantity consumed by the actor, and fix the mismatch by standardizing terminal-outcome advantages under the action-token measure. We additionally organize prompt evidence by the policy event that generated it rather than learner receipt order. Across matched runs on ALFWorld at two model scales and on Math-TIR, SPO++ improves online learning efficiency over SPO. A paired ablation identifies action-token-measure normalization as the strongest tested component.

---


### 193. [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876)

**<font color=#1a73e8>作者：</font>** Zhaochen Yu, Yingcheng Wu, Zhenfei Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history. This coupling also turns execution into structured evidence that localizes failures to specific memory components. Across tasks, a fixed Meta-Agent turns that evidence into localized, validation-gated updates to Skill Memory that reshape execution and yield new evidence, forming a bounded recursive memory-evolution loop. Across four long-horizon benchmarks and ten models, Recuris improves task success in 35 of the 37 completed model-benchmark pairs, carrying frontier models to SOTA-level task success: on tau-bench it adds +17.8 points to GPT-5.6 Sol and +15.6 to Claude Opus 5, taking Opus 5 to 87.9%, and +16.6/+13.5 points on Qwen3.6-27B/35B on SkillFlow. The advantage widens as the interaction horizon grows, to +32.2 points on the longest tasks, and common long-horizon failures fall by up to 80%. These results position recursively evolving memory as a scalable foundation for RSI, enabling agents to continuously transform accumulated experience into increasingly effective long-horizon behavior. Code: this https URL

---


### 194. [From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms](https://arxiv.org/abs/2608.24877)

**<font color=#1a73e8>作者：</font>** Jiangning Zhang, Haojun Chen, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints. Despite rapid progress in augmented reality, egocentric vision, multimodal models, human-computer interaction, and embodied intelligence, the literature remains fragmented across devices, tasks, and benchmarks. \textit{The key challenge is not whether a model can recognize, answer, remember, or act in isolation, but whether a complete system can sustain a reliable, temporally valid, correctable, and governable perception-state-interaction-action loop.} This survey is \textit{the \textbf{first} to systematically study smart glasses through such a unified framework}. We formalize first-person data flow and constrained task utility, characterize devices along eight verifiable hardware capability axes, organize the literature around seven interdependent foundational capabilities, and introduce an L0-L5 framework spanning capture, reactive perception, contextual assistance, persistent state, governed action, and embodied coupling. Across nine application scenes, we connect tasks with datasets, systems, products, stakeholders, failure consequences, and evidence gaps. We further present a nine-dimensional deployment framework, a claim-conditioned evaluation protocol, and an evidence ladder from controlled measurement to longitudinal field validation and audit. Together, these elements make smart glasses more comparable, deployable, and reproducibly evaluated, while outlining a roadmap toward trustworthy first-person intelligence.

---


> [!TIP]
> 当前位于：**151-194**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-194**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
