# 📦 其他研究 | 2026年06月01日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-317**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-317**

---

### 301. [Functional Attention: From Pairwise Affinities to Functional Correspondences](https://arxiv.org/abs/2605.31559)

**<font color=#1a73e8>作者：</font>** Jiefang Xiao, Maolin Gao, Simon Weber 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning mappings between infinite-dimensional function spaces, or operator learning, is essential for many machine learning applications. Although transformer-based operators are popular, they often rely on token-wise attention. These methods treat continuous fields as discrete tokens and usually ignore the global functional structure. We introduce \emph{Functional Attention}, which reinterprets attention as a functional correspondence between adaptive bases. Inspired by geometric functional maps, our method replaces softmax affinities with structured linear operators. This yields a compact, generalizable, resolution-invariant representation that explicitly captures global dependencies. Experiments demonstrate that \emph{Functional Attention} can match state-of-the-art performance in many operator learning tasks, including solving PDEs, 3D segmentation, and regression, while remaining robust to varying discretizations. Project page is available at this https URL.

---


### 302. [Effective Biological Representation Learning by Masking Gene Expression](https://arxiv.org/abs/2605.31562)

**<font color=#1a73e8>作者：</font>** Kian Kenyon-Dean, Alina Selega, Ihab Bendidi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RNA sequencing produces rich and diverse datasets of gene expression, offering compelling insights into cellular state and function that have many applications in drug discovery. Modeling such data is challenging due to inherent technical noise and experimental batch effects, as evidenced by many existing transcriptomic foundation models (FMs) underperforming relative to linear baselines. Such results raise the question of whether deep representation learning provides a distinct advantage over the direct use of raw transcript counts. Our work explores this by developing a new self-supervised model, TxFM, with a focus on inductive representation learning evaluations. TxFM employs a masked autoencoding approach tailored to diverse RNA-seq count data, and our ablation study empirically identifies crucial architecture configurations required for strong transfer performance. Additionally, we curate a public training corpus, DiverseRNA-1.4M, and find that TxFM trained on this curated dataset yields high-fidelity gene representations that outperform FMs trained on atlas-scale corpora over 100x larger. Overall, our results indicate that inductive self-supervised learning is a viable modeling approach for transcriptomics representation, provided a careful synthesis of model architecture and training data curation.

---


### 303. [Disagreeing Rationales: Rethinking Classification and Explainability Evaluation in Hate Speech Detection](https://arxiv.org/abs/2605.31563)

**<font color=#1a73e8>作者：</font>** Benedetta Muscato, Beiduo Chen, Gizem Gezici 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human disagreement is ubiquitous and well-known in labeling. However, variation in explanations, captured through token-level human rationales, remains far less explored. At the same time, it is unclear how to best evaluate human labels and rationales -- or even how to best aggregate rationales beyond majority vote -- in light of this variation. Yet, rationales may provide additional insights into the richness of human reasoning, that may differ in style, values and interpretations -- especially in subjective NLP tasks like hate speech detection. In this work, we unify diverse models, training strategies, loss functions, and existing evaluation metrics under a single protocol by systematically re-implementing them across different label and rationale representation spaces. Classification metrics are organized around two key properties -- predictive and distributional -- while explainability metrics through three complementary dimensions: plausibility, faithfulness, and complexity. In this unified supervision framework, we evaluate model behavior across classification and explainability metrics, as well as metric sensitivity to the choice of label (hard and soft) and rationale representation space (hard, intermediate and soft). Results show that both hard and soft metrics favor softer representations, highlighting their effectiveness in capturing variation and the need to rethink evaluation in subjective NLP.

---


### 304. [nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving](https://arxiv.org/abs/2605.31572)

**<font color=#1a73e8>作者：</font>** Zhiyu Huang, Johnson Liu, Rui Song 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning is essential for autonomous driving (AD) in long-tail scenarios, where vehicles must apply commonsense knowledge, understand spatial relations, infer agent interactions, and make safe decisions. However, existing AD datasets and benchmarks mainly target perception, prediction, or planning, and provide limited supervision for reasoning over realistic long-tail driving scenes. We introduce nuReasoning, a large-scale real-world dataset and benchmark for reasoning-centric AD. Following the lineage of nuScenes and nuPlan, nuReasoning advances real-world AD datasets and benchmarks toward reasoning in long-tail driving scenarios. The dataset contains 20,000 clips, each 20 seconds long, collected across multiple cities, with synchronized multi-camera images, LiDAR data, HD maps, object annotations, and human-verified reasoning annotations spanning Spatial Reasoning, Decision Reasoning, and Counterfactual Reasoning. Unlike prior datasets that focus primarily on visual question answering, nuReasoning supports both reasoning evaluation and planning evaluation, enabling a direct study of how reasoning supervision affects driving performance. Experiments show that fine-tuning VLMs on nuReasoning substantially improves driving-specific question answering, while incorporating reasoning supervision into VLA training improves planning performance even when textual reasoning outputs are disabled at inference time. These results establish nuReasoning as a foundation for evaluating and improving robust, interpretable, reasoning-driven AD systems in realistic long-tail settings.

---


### 305. [Can Generative AI help people navigate Radical Moral Disagreements? The CONSIDER prototype](https://arxiv.org/abs/2605.31574)

**<font color=#1a73e8>作者：</font>** William Hohnen-Ford, Sarah Chen, Kathryn B. Francis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Radical Moral Disagreements (RMDs) are highly polarising topics that are increasingly censored in everyday life, with growing evidence suggesting that this polarisation carries measurable costs to public mental health. To address these challenges, some researchers have proposed Large Language Models (LLMs) as a means to support more democratic deliberation and better moral reasoning. Yet existing tools are poorly calibrated to help people navigate RMDs, because of their intense and divisive characteristics. This paper introduces CONSIDER, a prototype for a one-to-one AI tool for RMD navigation. Drawing on Mill's account of the epistemic value of disagreement, CONSIDER aims at value clarification through structured disagreement with an opposing LLM-generated opinion. We describe CONSIDER's design logic and analyse potential risks posed by such tools to guide future development.

---


### 306. [Joint Multi-Camera LiDAR Extrinsic Calibration via Learned Pairwise Initialization and Geometric Refinement](https://arxiv.org/abs/2605.31576)

**<font color=#1a73e8>作者：</font>** Aziz Al-Najjar, Marzieh Amini, James R. Green 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most learning-based camera-LiDAR calibration methods treat each camera-LiDAR pair independently, ignoring the rigid geometric coupling in multi-camera platforms. As a result, per-camera estimates may be individually accurate yet inconsistent at the system level. We present a two-stage framework for joint multi-camera LiDAR extrinsic calibration that combines learned pairwise matching with geometric refinement. First, CMRNext is applied independently to each camera to produce initial extrinsic estimates and dense 2D-3D correspondences. These predictions are then jointly refined through a multi-frame bundle adjustment with reprojection, per-camera prior, and relative-pose prior terms. This approach converts pairwise predictions into a globally consistent multi-camera calibration. Experiments on KITTI (in-domain for CMRNext) and Walkley (out-of-domain) datasets show improved per-camera accuracy and inter-camera consistency. On KITTI, the method achieves 0.89 cm translation error and 0.038 rotation error. On Walkley, it reduces translation error from 108.6 cm to 3.1 cm, highlighting the benefit of explicit multi-camera coupling when single-camera predictions are less reliable.

---


### 307. [SurGe: Improved Surface Geometry in Point Maps](https://arxiv.org/abs/2605.31577)

**<font color=#1a73e8>作者：</font>** Karim Knaebel, Gonzalo Martin Garcia, Christian Schmidt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feedforward 3D reconstruction methods predict point maps and estimate global 3D geometry remarkably well. However, their predictions still exhibit inaccurate local surface geometry, which is clearly visible qualitatively but only weakly reflected in common metrics. To make these errors more explicit in evaluation, we introduce a point map normal metric that evaluates the local surface orientation induced by neighboring 3D predictions. To reduce these errors, we propose two complementary components: a point gradient matching loss that supervises depth-normalized 3D finite differences, and a Neighborhood Attention Decoder (NAD) that progressively upsamples features and uses Neighborhood Attention for local feature mixing. Across eight zero-shot monocular geometry benchmarks, our model, SurGe, achieves the best average rank for global point map AbsRel and consistently improves local point map and point map normal evaluations.

---


### 308. [Choosing the Lens: Strategic Perspective Activation in Context-Dependent Argumentation](https://arxiv.org/abs/2605.31581)

**<font color=#1a73e8>作者：</font>** Albert Sadowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The same arguments often need to be evaluated under different external regimes. An agent with influence over the regime has a strategic lever that standard formalisms do not directly capture. We introduce context-dependent argumentation frameworks (CDAFs), an extension of Dung's theory in which a defeat function determines, per context, which attacks succeed. A perspective-labeled specialisation derives the defeat function from a relevance set $\rho$ and a priority $\pi$. The relevance set is the agent's action space. In a small worked example, the agent's target argument is rejected under every full-relevance injective priority, yet accepted under partial activations, one of which no VAF audience can mirror. We define the corresponding decision problem, ACTIVATION-MANIPULATION, and record baseline complexity bounds. Tight bounds and multi-agent variants are left open.

---


### 309. [Recognizing Co-Speech Gestures in-the-Wild](https://arxiv.org/abs/2605.31589)

**<font color=#1a73e8>作者：</font>** Sindhu B Hegde, K R Prajwal, Andrew Zisserman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While humans naturally gesture during speech, only a sparse subset of these movements are visually depictive and semantically linked to specific spoken words. Current multimodal models struggle to capture these semantic co-speech gestures, heavily bottlenecked by a lack of precisely annotated training data. To address this, we introduce the Gesture Recognition in the Wild (GRW) dataset, the first large-scale benchmark designed to map unconstrained human gestures to specific words with frame-accurate temporal boundaries. Comprising 156,688 manually annotated video clips, GRW spans a highly diverse 150-word taxonomy of physical actions, spatial descriptors, and abstract concepts. We leverage GRW to train video models to (a) classify gestures as semantic or not, (b) recognize the word corresponding to a co-speech gesture, and (c) temporally localize the gesture. We also use GRW to establish benchmarks for these three tasks.

---


### 310. [TunerDiT: Training-free Progressive Steering of Diffusion Transformer for Multi-Event Video Generation](https://arxiv.org/abs/2605.31590)

**<font color=#1a73e8>作者：</font>** Ruotong Liao, Guowen Huang, Qing Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) generation faces challenging questions when generating videos with long horizons containing multiple events. Inspired by the intrinsics of the diffusion process, we probe video diffusion transformers (DiTs) and uncover intrinsic turning points in the DiT denoising trajectory where conditioning text affects generation from global layout to fine-grained details. Building on this finding, we present TunerDiT, a simple yet effective progressive steering method that requires no additional training for multi-event generation. TunerDiT comprises two steering handles: (1) Event-Partitioned Masking that enforces event boundaries while allowing cross-event transition bands; (2) Cross-Event Prompt Fusion that injects neighboring event semantics for late-stage refinement. We contribute a self-curated prompt suite for benchmarking multi-event generation, i.e., Meve. TunerDiT achieves state-of-the-art performance across 8 metrics and offers a tunable trade-off between video consistency and event separation, compared with other training-free methods. The improvement in text alignment increases with the event count, indicating a scaling possibility with increasing event count.

---


### 311. [CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference](https://arxiv.org/abs/2605.31591)

**<font color=#1a73e8>作者：</font>** Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Models for AI-based skin cancer screening suffer a severe performance drop when shifting from expert dermoscopic (source) images to consumer-grade clinical (target) images, hindering real-world deployment. Existing domain adaptation methods often ignore crucial semantic invariants, such as clinical concepts. While new foundation models like MONET can provide this semantic information as dense, probabilistic scores, this metadata is unavailable at test time, creating a deployment paradox for practical image-only screening tools. We address this gap by proposing CoFiDA-M, a privileged information framework that learns from concepts at training time but deploys as an image-only model. Our method trains a teacher network that uses MONET concept probabilities to guide a FiLM modulator, transforming visual features into a semantically ``edited" feature space. A lightweight, image-only student is then trained to reproduce this edited representation, not just the teacher's final predictions. This distillation ``bakes" the clinical reasoning into the student's weights. On a challenging multi-dataset benchmark, our image-only student significantly outperforms state-of-the-art approaches, especially in melanoma recall. Our work provides a practical and generalizable framework for leveraging noisy, probabilistic metadata as privileged information, demonstrating strong cross-dataset robustness and potential for real-world deployment beyond dermatology. Implementation code is available at: this https URL

---


### 312. [Stateful Online Monitoring Catches Distributed Agent Attacks](https://arxiv.org/abs/2605.31593)

**<font color=#1a73e8>作者：</font>** Davis Brown, Samarth Bhargav, Arav Santhanam 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language models can find thousands of severe software vulnerabilities, and agents are increasingly being misused for cyberattacks. To avoid detection, attackers frequently distribute their misuse, splitting a harmful task across many user accounts so each individual transcript looks benign. Because safety monitors score only one agent context at a time, they are structurally blind to misuse that is only visible in aggregate, across many accounts. We show this gap is real by building, to our knowledge, the first distributed agent attack, a multi-agent scaffold that completes hard cybersecurity tasks while hiding the harmful objective across subagents with limited contexts, evading a standard monitor that catches it only a fifth as often as prior agent attacks. Towards a defense, we develop an online stateful monitor that uses real-time clustering to collect weak suspiciousness signals across many agent transcripts, and escalates only rarely to a language model that flags misuse across user accounts. In evaluations with large-scale simulated datacenter traffic, our monitor Pareto dominates standard monitors, catching distributed attacks 30% earlier and flagging cyber misuse before it reaches the most harmful stages. Crucially, this comes at negligible additional latency for ~99% of user traffic. This detection advantage persists but narrows as the benign background traffic grows very large. After an extensive red-teaming exercise, we improve the defense and surprisingly also find that it catches standard jailbreaks, since adaptive attackers reuse attack variants across accounts. Our results point toward a new class of safety monitors which reason over groups of users rather than isolated transcripts.

---


### 313. [A Tight Theory of Error Feedback Algorithms in Distributed Optimization](https://arxiv.org/abs/2605.31594)

**<font color=#1a73e8>作者：</font>** Daniel Berg Thomsen, Adrien Taylor, Aymeric Dieuleveut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication costs are a major bottleneck in distributed learning and first-order optimization. A common approach to alleviate this issue is to compress the gradient information exchanged between agents. However, such compression typically degrades the convergence guarantees of gradient-based methods. Error feedback mechanisms provide a simple and computationally cheap remedy for this issue, but numerous variants have been proposed, and their relative performance remains poorly understood. This paper provides tight convergence analyses for two of the main error-feedback algorithms from the literature, the classic Error Feedback method (EF) and Error Feedback 21 (EF21), by identifying optimal step-size choices and constructing optimal Lyapunov functions tailored to each method. The results hold independently of the number of agents and recover the known best guarantees possible in the single-agent regime.

---


### 314. [Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595)

**<font color=#1a73e8>作者：</font>** Mungyeom Kim, Minkyeong Jeon, Honggyu An 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction from monocular video remains a fundamental challenge in computer vision. Existing feed-forward methods predict 3D Gaussians pixel-wise for each frame, suffering from duplicated Gaussians and view-dependent biases that hinder effective learning of scene motion. We present C4G, a feed-forward 4D reconstruction framework built upon a compact set of timestamp-conditioned learnable Gaussian query tokens. Each token aggregates corresponding features across the full temporal context and decodes a 3D Gaussian whose position is modulated by the target timestamp, enabling globally coherent motion modeling without per-scene optimization. To capture fine-grained details, we further introduce a video diffusion model-based rendering enhancement module. Since our framework effectively aggregates features into Gaussians, we extend this capability to feature lifting, producing a 4D feature field that supports point tracking and dynamic scene understanding. C4G achieves strong novel-view synthesis performance using significantly fewer Gaussians and without requiring camera poses, while exhibiting stronger motion modeling and robustness to large temporal gaps.

---


### 315. [KLIP: localized distribution shift detection via KL-divergence with diffusion priors in Inverse Problems](https://arxiv.org/abs/2605.31596)

**<font color=#1a73e8>作者：</font>** Alireza Kheirandish, Jihoon Hong, Sara Fridovich-Keil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown promising performance as data-driven priors for computational imaging, as well as some capacity to detect out-of-distribution (OOD) images. However, existing approaches to OOD detection often require some knowledge of the shifted distribution, fail to detect subtle or localized distribution shifts, and operate on full images, rather than the indirect measurements available in inverse problems. We propose an OOD detection metric based on the Kullback-Leibler divergence between the diffusion prior and the posterior distribution, that (i) does not require any calibration data or knowledge of the shifted distribution, and (ii) can detect whole images as OOD as well as localize OOD patches within an image. Experimentally, we show that this metric can detect subtle yet semantically meaningful distribution shifts, such as the shift from healthy liver CT scans to those with tumors, and generalizes across different types of diffusion models, datasets, and inverse problems. Our code can be found at this https URL.

---


### 316. [Linear Scaling Video VLMs for Long Video Understanding](https://arxiv.org/abs/2605.31598)

**<font color=#1a73e8>作者：</font>** Cristobal Eyzaguirre, Jiajun Wu, Juan Carlos Niebles  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video vision-language models (VLMs) are increasingly used in long-horizon and streaming settings, yet most video encoders still rely on spatiotemporal self-attention, causing compute and latency to grow quadratically with the number of frames. Existing efficiency methods improve scalability but often lose accuracy relative to full self-attention, for example through aggressive frame/token dropping or coarse attention approximations. We introduce StateKV, an inference-time method that adapts pretrained long-video VLMs to linear-time video prefill by carrying cross-frame context in a fixed-capacity, importance-based recurrent state, paired with a second full per-frame cache used for decoding. Across three long-video benchmarks and seven models spanning three families and multiple scales, StateKV remains close to full self-attention and consistently outperforms dominant sliding-window / recency-based streaming approximations, without fine-tuning or architectural changes. StateKV also reduces video-prefill cost measured FLOPs, enabling stronger accuracy at a fixed compute budget by running larger models. These results suggest a practical step toward scalable long-video understanding.

---


### 317. [Lumos-Nexus: Efficient Frequency Bridging with Homogeneous Latent Space for Video Unified Models](https://arxiv.org/abs/2605.31603)

**<font color=#1a73e8>作者：</font>** Jiazheng Xing, Hangjie Yuan, Lingling Cai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Connector-based video unified models have demonstrated strong capability in instruction-grounded video synthesis, but integrating a large high-fidelity generator into the unified training loop is computationally prohibitive, limiting achievable visual quality. We therefore propose Lumos-Nexus, a training-efficient unified video generation framework that facilitates the development of strong reasoning-driven generation capabilities while significantly enhancing visual fidelity. Lumos-Nexus adopts a two-stage design: 1) During training, only a lightweight generator is aligned with the understanding block to learn to take in reasoning-driven semantic control. 2) During inference, we introduce Unified Progressive Frequency Bridging (UPFB) to progressively hand off generation to a high-capacity pretrained generator in the shared latent space, enabling coarse-to-fine refinement and producing high-fidelity videos without compromising reasoning quality. To fill the gap in reasoning-driven video generation benchmarks, we introduce VR-Bench, which assesses a model's capability to translate inferred intent into coherent and semantically aligned video content. Extensive experiments demonstrate that Lumos-Nexus achieves substantial gains in visual realism and temporal coherence on VBench, while exhibiting strong reasoning-based generative performance on VR-Bench. Code and models are available at this https URL.

---


> [!TIP]
> 当前位于：**301-317**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-317**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
