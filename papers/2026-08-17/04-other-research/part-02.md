# 📦 其他研究 | 2026年08月17日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-199](./part-04.md)

---

### 51. [The Impact of Temporal Context Length and Encoding Strategies on Self-Supervised ECG Representation Learning](https://arxiv.org/abs/2608.12695)

**<font color=#1a73e8>作者：</font>** Ahmed Sameh, Ramzi Al-Sharawi, Yogatheesan Varatharajah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised electrocardiogram (ECG) models are often trained on a few seconds of ECG signal and, increasingly, on discretized token sequences. It remains unclear whether these choices sacrifice information needed for rhythm inference and longitudinal consistency in real-world ambulatory recordings. We present a controlled study on the Icentia11k single-lead dataset that varies (i) the input horizon (16 seconds, 1 minute, 5 minutes, and 10 minutes) and (ii) the front-end representation (continuous convolutional patch embeddings vs. fixed vector-quantized tokens), while holding the Transformer backbone and training protocol constant. Representations are assessed by downstream abnormal rhythm detection and by patient-level retrieval that probes cross-session stability. Our results show that increasing temporal context beyond 16-second snapshots yields stronger transfer and higher retrieval accuracy, with the strongest performance achieved by the 5- and 10-minute models, indicating improved capture of slow-varying rhythm dynamics and individual-specific structure. Across all evaluated horizons, continuous patch embeddings outperform discretized tokens, suggesting that quantization can discard clinically relevant waveform detail. These findings motivate ECG foundation models that emphasize extended context and continuous encoders for clinical prediction and similarity-based applications. Our code and pretrained models are publicly available at this https URL.

---


### 52. [Class Geometry as Supervision for Sample-Efficient Open-World Detection](https://arxiv.org/abs/2608.12698)

**<font color=#1a73e8>作者：</font>** Akash Rao, Zhou Chen, Revanth Reddy Palem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world object detection requires models to recognize known categories, reject unfamiliar objects, and incorporate new classes over time. This is especially challenging in scarce-data settings such as biomedical and scientific imaging, where rare categories may have only a few annotated examples and fine-grained classes differ by subtle morphology. Prototype-based detectors are natural for this regime, but they typically learn class prototypes as independent anchors, ignoring relational structure among classes. We propose class-geometry supervision (CGS), a general framework that constrains learned prototype or class-representation spaces to preserve visual or semantic class dissimilarities estimated from training data. CGS introduces a dissimilarity-preserving objective that aligns pairwise distances among learned class representations with a target class-geometry matrix while retaining the standard task loss. We instantiate the same objective across prototype recognition, few-shot biomedical object detection, open-set detection, novel-class insertion, and OWOD adaptation on COCO. Experiments show that CGS improves sample efficiency in recognition and ova detection, substantially strengthens novel-class insertion, and improves unknown recall on COCO while retaining much of the known-class detection performance. Ablations show that meaningful visual geometry provides the most reliable gains, while random geometry can help novel separation but is less consistent for few-shot detection. These results suggest that relational class geometry is an effective supervisory signal for building calibrated and extensible open-world detectors under limited supervision.

---


### 53. [Federated Compositional Muon Optimizer for Matrix-Wise Models](https://arxiv.org/abs/2608.12710)

**<font color=#1a73e8>作者：</font>** Wang Yan, Feihu Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon, a more recently developed optimizer, is useful for matrix-wise models in AI areas. Although many works have studied Muon and its variants, these methods are still not particularly well-suited for hierarchical structured problems. To fill this gap, we propose an effective federated compositional Muon (FedCoMuon) optimizer to solve distributed matrix-wise compositional optimization problems. Specifically, our FedCoMuon optimizer builds on compositional gradient tracking and orthogonalized momentum. Moreover, we propose a variance reduced variant of FedCoMuon (FedCoMuon-VR) based on a momentum-based variance reduced technique. In theory, we analyze the convergence properties of our algorithms under the non-i.i.d. and non-convex settings. In particular, we prove that our FedCoMuon-VR obtains a lower sample complexity of $O(\epsilon^{-3})$ for finding an $\epsilon$-stationary solution than the existing FedMuon algorithms. Extensive numerical experiments on robust federated learning and task-distributed risk-sensitive meta learning show that our proposed methods are competitive with existing compositional baselines and achieve the best reported accuracy in several settings.

---


### 54. [Towards Sparsely Annotated Open-World Object Detection](https://arxiv.org/abs/2608.12714)

**<font color=#1a73e8>作者：</font>** HeeJu Han, AJeong Kim, Jinsun Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world object detection operates under ambiguous supervision, where unlabeled regions may correspond to missing annotations of known objects or genuinely unknown categories. These challenges have been addressed separately in Sparsely Annotated Object Detection (SAOD) and Open-World Object Detection (OWOD). In practice, their co-occurrence remains an open problem. To address this problem, we introduce Sparsely Annotated Open-World Object Detection (SA-OWOD), a new task that jointly considers sparse supervision and the presence of unseen categories. We propose Dual-Perspective Object Discovery (DPOD), a unified framework that jointly models unlabeled known and unknown instances via two complementary mechanisms. The Known Target Recovery Module (KTRM) recovers supervision for unlabeled known instances and explicitly regularizes the feature space to separate known and unknown representations. Complementarily, the Dual-Disagreement Target Generator (DDTG) identifies reliable unknown candidates through cross-view semantic inconsistency. By integrating these modules, DPOD resolves contradictory supervision signals caused by ambiguous unlabeled regions. As a result, it prevents misclassification between known and unknown objects and stabilizes the decision boundaries. Experimental results on sparsely annotated open-world benchmarks demonstrate that the proposed method outperforms existing open-world detection methods, particularly in detecting unknown objects.

---


### 55. [A Generative Approach for Improving Multi-Label Defect Classification in Photovoltaic Modules](https://arxiv.org/abs/2608.12725)

**<font color=#1a73e8>作者：</font>** Abdul Mueez, Yogesh S. Rawat, Shruti Vyas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of multi-label defect classification in electroluminescence (EL) images of photovoltaic (PV) cells. Training models on images where multiple defects co-occur creates learning ambiguity, making it difficult to disentangle visual features for specific defect types, a problem compounded by the scarcity of examples for individual classes. To tackle this, we introduce Generative Defect Isolation (GDI), utilizing the LaMa inpainting model with Fast Fourier Convolutions to remove selected defects and generate realistic, single-defect training samples. Extensive experiments on Vision Transformer (ViT-S, ViT-L) and EfficientNetV2-L architectures demonstrate that GDI significantly outperforms baselines. The performance gains are most pronounced in low-data scenarios; class-wise analysis shows substantial improvements, boosting the F1-Score for rare defect classes by up to 63.6%. Furthermore, GDI effectively resolves learning ambiguity from co-occurring defects, yielding a 26% reduction in such co-occurring classification errors. Our work establishes GDI as an effective method for maximizing the value of existing segmentation datasets and sets a new performance benchmark for multi-label classification in this domain.

---


### 56. [Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding](https://arxiv.org/abs/2608.12748)

**<font color=#1a73e8>作者：</font>** Junyi Hu, Tian Bai, Fengyi Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Expression Comprehension (REC) is commonly studied under dataset-specific fine-tuning, resulting in specialist models with limited cross-dataset generalization. In this work, we revisit REC from the perspective of unified open-vocabulary grounding and identify representation degeneration as a key obstacle to scaling a single generalist model. To preserve representation diversity, we propose a holistic data-model co-design framework. Architecturally, we introduce the Modulated Attention-Contrastive Head (mACH) for efficient token-level vision-language alignment and a text-conditioned JEPA auxiliary stream that provides complementary gradient support to preserve alignment-active representations without inference overhead. On the data side, we introduce Objects365-Caption, enriching Objects365 with context-aware referring expressions for large-scale language supervision. We further provide a theoretical analysis showing that complementary gradient subspaces preserve alignment capacity and thereby scale representation diversity. Extensive experiments demonstrate that our single-checkpoint framework achieves highly competitive performance on standard REC benchmarks while exhibiting strong generalization across heterogeneous grounding datasets without benchmark-specific adaptation.

---


### 57. [Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry](https://arxiv.org/abs/2608.12753)

**<font color=#1a73e8>作者：</font>** Larissa Xu, King Bi, William Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study decentralized multi-player reinforcement learning in episodic tabular Markov decision processes (MDPs) under three forms of information asymmetry: (A) unobserved actions with common rewards, (B) observed actions with independent rewards, and (C) unobserved actions with independent rewards. Players cannot communicate during learning but may agree on a protocol a priori. For Problems A and B we propose \texttt{mQ-learning} and \texttt{mQ-learning-intervals}, achieving $\tilde{O}(\sqrt{H^4 S A_{\text{joint}}\, T})$ regret, where $H$ is the horizon, $S$ the state count, $T = KH$ the total steps, and $A_{\text{joint}} = \prod_{i=1}^M |\mathcal{A}_i|$ the joint action space across $M$ players. For Problem C we give \texttt{mEXC} and \texttt{mEXC-Bellman}, two-phase explore-then-commit algorithms with regret $\tilde{O}(H (S A_{\text{joint}})^{1/3} T^{2/3})$. Against the centralized joint-action benchmark, decentralized learning under information asymmetry matches the single-agent Q-learning rate of \cite{jin2018q} up to logarithmic factors. Because $A_{\text{joint}}$ grows exponentially in $M$, the bounds are most meaningful for small $M$ or small per-player action sets.

---


### 58. [ReconSpan: Reconstruction-Guided Adaptive Latent Tokenization](https://arxiv.org/abs/2608.12756)

**<font color=#1a73e8>作者：</font>** Lixing Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive latent tokenization maps a fine-grained input to a shorter sequence of continuous representations associated with input-dependent spans. We introduce ReconSpan, which divides text into chunks that a backward decoder can reconstruct from a single contextual prefix code and retains one such code as the latent token for each chunk. The reconstruction criterion is applied when chunks are formed, allowing one trained autoencoder to produce average chunk lengths from 6.5 to 12.2. At matched average length, reconstruction-guided boundaries preserve more text than random boundaries. Readers of the resulting latent sequence recover topic information reliably but struggle to extract exact details.

---


### 59. [NavSight in the Wild: Understanding Real-World Use of a Mobile Augmented Reality Application for People with Low Vision in Outdoor Navigation](https://arxiv.org/abs/2608.12759)

**<font color=#1a73e8>作者：</font>** Yuheng Wu, Kexin Zhang, Ben Kosa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ability to navigate outdoors safely and independently is crucial yet challenging for people with low vision (PLV). While various augmented reality (AR) systems for low vision have been designed and evaluated in ideal lab environments, no research has investigated their real-world feasibility and challenges. We present NavSight, a mobile AR application that assists PLV in outdoor navigation by recognizing important outdoor objects (e.g., curb, vehicle) and rendering real-time visual augmentations. Through a seven-day diary study with 12 PLV in real-world settings, we characterize the impact of NavSight on scene perception, users' configuration strategies on what objects to augment and how to augment them across scenarios, how users made sense of and responded to recognition errors, and the social acceptability of using NavSight in public. We further identify environmental factors affecting recognition, such as weather conditions, lighting and shadows, and nonstandard road markings and textures, as well as usability issues in daily use. We discuss these real-world challenges and derive design implications for future AI-powered assistive AR systems for outdoor use.

---


### 60. [PatchGen: Learning Soft Intra-Image Predictive Subsets for Visual Generalization](https://arxiv.org/abs/2608.12766)

**<font color=#1a73e8>作者：</font>** Zhaorui Tan, Weimiao Yu, Xi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual classifiers are expected to generalize under data shifts, target shifts, and their combinations, yet most existing methods focus on domain invariance while failing to address intra-image predictive sufficiency. We investigate the structural hypothesis that each image contains a sample-adaptive oracle intra-image predictive subset sufficient for label prediction, while the remaining patches form non-essential complementary context that may correlate with the label. The theoretical analysis shows that restricting prediction to this oracle subset preserves the Bayes risk achievable by the full-patch representation while admitting a complexity bound that tightens with the oracle-subset size. Based on this view, we propose PatchGen, a text-free module that learns a sample-dependent soft predictive-subset mask as a task-driven proxy for the unobserved oracle subset mask. Specifically, histopathology visualizations suggest that PatchGen assigns higher scores to tumor-consistent regions than to some frequently co-occurring inflammatory context. Extensive experiments on natural and histopathological image benchmarks spanning all three shift settings show that PatchGen improves average performance over matched-backbone baselines in most evaluated configurations, enhances generalization to unknown classes, and remains competitive with vision-language methods without text supervision.

---


### 61. [SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention](https://arxiv.org/abs/2608.12780)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Qirui Li, Hanlin Tang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) incur quadratic self-attention cost over spatiotemporal tokens. Existing training-free sparse attention methods often construct sparse masks from block-level or cluster-level proxy scores, which can obscure fine-grained differences among keys and miss high contribution keys under aggressive sparsity. Moreover, such proxy scores may yield overly concentrated softmax distributions, causing Top-$p$ to retain too few keys for some query clusters. Although a fixed Top-$k$ minimum alleviates this failure mode, a shared value cannot adapt to variations across heads and inputs. To address both limitations, we propose SCOPE, a training-free sparse attention framework that combines 3D-RoPE-aligned key subspace clustering with online per-head Top-$k$ estimation for efficient video-DiT inference. SCOPE partitions post-RoPE keys into temporal, height, and width subspaces, clusters them independently, and aggregates the corresponding centroid scores through lookup tables to obtain per key proxy scores for each query cluster. Building on existing hybrid Top-$p$/fixed Top-$k$ selection, SCOPE derives a head-specific Top-$k$ value online by averaging the initial retained key counts within each head, weighted by query cluster size, and selects additional keys only for query clusters whose initial retained key counts fall below this value. Sparse attention is then computed over the selected original keys and values. Across six model--task configurations, SCOPE consistently outperforms existing training-free baselines in both fidelity and latency, achieving up to a $1.99\times$ end-to-end speedup on 720p HunyuanVideo with $28.46$ dB PSNR relative to dense attention.

---


### 62. [ARAC: Benchmarking Auto-Research's Alignment and Completeness on End-to-End Researchs](https://arxiv.org/abs/2608.12788)

**<font color=#1a73e8>作者：</font>** Jiale Cui, Yueyao Yuan, Kaixi Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Auto-Research has surfaced a fundamental evaluation challenge: how can we measure the alignment, logical coherence, and evolutionary completeness of its research trajectory with human research behavior? We propose Auto-Research's Alignment and Completeness, ARAC-Bench: a Researcher-Mimicking Evaluation framework that shifts the objective from matching final answers to reproducing high-quality human research processes. The framework operates through two synergistic components: the Academic Cognition Skills system, which is the first to transforms implicit reviewer expertise into stage-calibrated, quantifiable rubrics; and a three-stage capability diagnostic protocol, which decomposes the research process under strict modular constraints into three traceable, mutually independent dimensions: Proposal, Experiment, and Synthesis. Systematic evaluation of 11 SOTA frameworks yields a best alignment score of only 67.9 of 100, revealing a significant gap in simulating rigorous human methodology. Validation against Ph.D. Candidates rankings shows a strong correlation of 0.8141, confirming that ARAC-Bench reliably reflects the dimensions researchers truly value. ARAC-Bench provides not only a fine-grained diagnostic tool but also a scalable reward signal for training the next generation of autonomous research systems.

---


### 63. [Considering Contribution Statements in Visualization and HCI Research](https://arxiv.org/abs/2608.12792)

**<font color=#1a73e8>作者：</font>** Mara Solen, Wesley Willett, Andrew M McNutt  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Contribution statements are an increasingly common way to make research labor visible, reduce academic malfeasance, and provide broader transparency. Despite this potential value, they remain uncommon in visualization and HCI. To explore this gap, we conducted an online study with (N=21) visualization and HCI researchers. We find a range of differing opinions about the utility of contribution statements, which are set against a background of tensions relating to contribution frameworks that inadequately fit contribution types in HCI and especially visualization, power dynamics between authors, bias in authorship perceptions, and the tedium of providing yet another form of documentation. From these factors, we offer a modest recommendation to authors: consider contribution statements. There are contexts when they may usefully explicate work, and others where they can cause author-team conflict or become a burdensome chore. Regardless of whether they are used by readers or not, we suggest that scaffolded mechanisms for reflecting on contribution roles are valuable both for public accountability and internal alignment. To institutions, we recommend that contribution statements be exempt from page or word limits, and that flexible templates and examples be provided to authors, but that they continue to not be required. By surfacing these perspectives, we seek to open a dialogue about what constitutes authorship, how our community might move toward more equitable and transparent attribution practices, and where the visualization and HCI communities might be uniquely equipped to help.

---


### 64. [CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility](https://arxiv.org/abs/2608.12805)

**<font color=#1a73e8>作者：</font>** Akanta Das, Al Amin Farhad, Mrinmoy Sarkar Anto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Access to clinical data is essential for developing reliable healthcare machine learning systems, but direct use of electronic health records is constrained by privacy regulation, institutional review, data-use agreements, and the risk of re-identification. Synthetic data promises a practical alternative: it can preserve useful statistical and clinical structure while reducing exposure of sensitive patient records. Prior studies often evaluate a single generator, one dataset, or a narrow downstream task, making it difficult to know when synthetic data can support model development and when it fails to preserve task-critical signal. We introduce CoMedBench, a reproducible benchmark that evaluates a family of generators under a common clinical-validity framework and one shared training and evaluation engine, spanning static tabular and temporal downstream tasks on established critical-care datasets. In total the benchmark spans 37 dataset-task pairs across two modalities consists of 20 static tabular and 17 temporal ICU time-series-drawn from seven public data sources: three intensive-care databases (MIMIC-III, MIMIC-IV, and eICU) together with the UCI Machine Learning Repository, the CDC BRFSS diabetes cohort (2015), NHANES (1999-2014), and the pycox survival datasets (GBSG and METABRIC). The benchmark evaluates both statistical fidelity and task utility by comparing models trained and tested across real and synthetic data. In these settings, synthetic training data preserves most of the downstream signal: on tabular tasks the reference generator CoMed-CTGAN retains a mean AUROC utility (the synthetic-to-real performance ratio) of 90.6%, rising to 97.3% for the strongest generator, CoMed-TVAE. Temporal ICU tasks are harder and more generator-sensitive: CoMed-CTGAN retains 81.6% (AUROC) and only 64.0% under the imbalance-sensitive AUPRC, whereas CoMed-TVAE still retains ~95% (AUROC).

---


### 65. [Erase but Preserve: Controllable Removal of Copyrighted Animation Characters via Optimized Semantic Anchors](https://arxiv.org/abs/2608.12806)

**<font color=#1a73e8>作者：</font>** Qiao Li, Xiaomeng Fu, Wangjia Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The exceptional generation capabilities of text-to-image diffusion models have raised copyright concerns, particularly the unauthorized reproduction of animation characters. Existing concept erasure methods fall short for animation character erasure: model modification methods struggle to identify suitable anchors for diverse, highly distinctive characters; prompt-based steering methods lack fine-grained control for precise intervention. These approaches often yield incomplete erasure and degraded image fidelity, hindering real-world deployment. In this paper, we propose a controllable method operating on the model's continuous textual representation to erase target characters during generation. We optimizes an anchor embedding via structural and detailed constraints to serve as a character surrogate, then replaces target-related embeddings with the anchor via a structure-aware adaptive strategy. Experiments show that our method achieves state-of-the-art erasure effectiveness and image fidelity preservation, while supporting controllable erasure degree, multi-target removal, and model transferability. Moreover, our optimized anchors are plug-and-play with current model modification baselines to improve their erasure performance.

---


### 66. [Structured Local Differential Modeling for AI-Generated Image Detection](https://arxiv.org/abs/2608.12811)

**<font color=#1a73e8>作者：</font>** Jiazhen Yang, Ruijin Jin, Junjun Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of AI-generated content has made the reliable detection of generated images an increasingly critical challenge. Existing detection methods are often dominated during training by semantically salient components with high signal-to-noise ratios (SNRs), thereby suppressing subtler forensic cues associated with the underlying generation mechanisms and embedded in low-level statistical structures. From an information-theoretic perspective, we present a key insight: effective detection in the low-level statistical space requires mitigating the dominance of semantic components while emphasizing and amplifying responses to low-SNR forgery traces. Building on this insight, we propose RippleNet, an AI-generated image detection framework based on local differential signals. RippleNet adaptively identifies forgery-sensitive regions and constructs multi-directional, multi-scale differential representations within local neighborhoods, explicitly characterizing anomalous patterns in neighborhood statistics. More importantly, we refine the attention mechanism to operate within the local differential representation space, enabling the model to establish explicit dependencies at a finer statistical granularity. This design facilitates the capture of pixel-level forgery traces that are difficult to model using conventional convolutions or image-wide patch-level attention. Extensive experiments on multiple public benchmarks and under cross-generator evaluation settings demonstrate that RippleNet achieves consistently competitive performance.

---


### 67. [FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines](https://arxiv.org/abs/2608.12814)

**<font color=#1a73e8>作者：</font>** Charin Polpanumas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> FastThaiG2P provides sub-millisecond Thai grapheme-to-phoneme conversion for text-to-speech pipelines (International Phonetic Alphabet and Kokoro-TTS conventions) using a PyThaiNLP-tokenized, extensible dictionary and normalization rules for common Central Thai speech. The approach achieves an average latency of 0.15 ms per utterance on a benchmark of 27,242 synthetically generated utterances, of which 30\% is spent on tokenization, 12\% on normalization, and 58\% on out-of-vocabulary fallbacks (0.5\% OOV rate). To demonstrate its effectiveness, we used FastThaiG2P to phonemize Som-TTS, an open dataset containing 20 hours of grapheme-and-audio pairs, then trained an 82M-parameter StyleTTS 2 model based on a Kokoro-TTS recipe. The resulting model vocalizes intelligible Thai speech suitable for prototyping and development at 0.25 real-time factor (4x real-time) with ONNX inference on CPU.

---


### 68. [RealmEye: Virtual Machine Introspection for Arm CCA Realm VMs](https://arxiv.org/abs/2608.12822)

**<font color=#1a73e8>作者：</font>** Ruofei Qu, Wei Feng, Hongzhan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential VMs (CVMs) have become the dominant substrate for sensitive cloud workloads, from financial services to privacy-preserving AI inference. The hardware isolation that protects these CVMs from a malicious cloud also blinds their owners to what runs inside them: kernel rootkits planted via network or supply-chain attacks can hide processes, tamper with kernel data, and exfiltrate model weights under the cover of the same isolation that defends the VM. Tenants therefore need to inspect a running CVM from outside, yet classical VM introspection (VMI) presupposes a trusted Hypervisor, which CVMs exclude from the TCB. The state-of-the-art CVM-VMI system, 00SEVen, restores introspection on AMD SEV-SNP via an in-VM agent at a privileged tier (VMPL0), a mechanism that does not exist on Arm CCA, leaving Realm VMs without any introspection solution.
We present RealmEye, the first VMI system for Arm CCA Realm VMs. RealmEye places the entire introspection logic inside the Realm Management Monitor (RMM) at R-EL2, achieving hardware-enforced separation between the monitor and the monitored VM: no agent runs inside the Realm, and the Realm remains unmodified. RealmEye reads Realm memory and registers, suspends the VM for consistent snapshots, and traps page-level accesses, without relying on any in-VM interface. A periodic, self-driven trigger mode keeps scan timing internal to the RMM, preventing the Hypervisor from colluding with in-Realm rootkits. Results are returned to the remote owner over a hardware-attested channel, and a CCA driver backend lets existing tools such as LibVMI and DRAKVUF interoperate with RealmEye unchanged. On the Arm FVP, RealmEye detects process hiding and syscall-table hooking by Diamorphine, and its in-RMM cost is linearly predictable from primitive invocation counts.

---


### 69. [LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2608.12825)

**<font color=#1a73e8>作者：</font>** Wenyu Li, Sidun Liu, Tongrui Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent query-based feed-forward 3DGS methods represent a scene using learnable queries, each aggregating multi-view evidence and decoding a group of Gaussians. Ideally, different queries should specialize in coherent local regions of the scene. However, we observe that Gaussians decoded from the same query often scatter across distant scene regions, resulting in weak query-level spatial coherence and poor alignment with the scene structure. We attribute this behavior to the purely latent representation of existing Gaussian queries. To address this limitation, we introduce LocusGS, which augments each Gaussian query with a 3D anchor state consisting of a center and a support radius. The anchor state is progressively refined across decoder layers and is used throughout query interaction, multi-view feature aggregation, and Gaussian generation. Specifically, an anchor-to-ray geometric bias guides each query toward spatially relevant image observations, while anchor-centered decoding organizes its Gaussians within a local region. Experiments on novel view synthesis benchmarks show that LocusGS improves rendering quality over query-based Gaussian token baselines under the same Gaussian budget. Further analysis shows that the learned anchors form coherent spatial layouts and lead to more structured Gaussian distributions, demonstrating that explicit anchor states improve the spatial organization. Our project page: this https URL.

---


### 70. [Validation of Smartphone-Based Photogrammetric 3D Body Scanning for Automated Anthropometric Measurements Compared with a Commercial Depth-Sensor-Based Body Scanner](https://arxiv.org/abs/2608.12827)

**<font color=#1a73e8>作者：</font>** Ruting Cheng, Boyuan Feng, Chuhui Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D body scanning has become an important tool in healthcare applications because of its rapid and non-invasive nature. While smartphone-based photogrammetric reconstruction provide a low-cost and accessible alternative to commercial 3D body scanners, their performance for whole-body scanning remains insufficiently validated. Thus, we designed this study to comprehensively validate the photogrammetric 3D scanning application by evaluating automatically extracted whole-body measurements and longitudinal body-shape monitoring. We evaluated a representative application, PolyCam, against the commercial depth-sensor-based Fit3D ProScanner using 144 pregnant participants scanned longitudinally throughout pregnancy. We designed an automatic circumference extraction pipeline to get measurements at four anatomical landmarks from paired 3D scans. A linear mixed-effects model was used to evaluate scanner effects and longitudinal body-shape changes. Measurement consistency was assessed using repeated PolyCam scans and tape measurements on a rigid mannequin. PolyCam demonstrated strong agreement with Fit3D, with average biases below 16 mm, intraclass correlation coefficients above 0.8, and Pearson correlation coefficients above 0.9 across all landmarks. Both systems captured comparable longitudinal body-shape changes. Mannequin experiments showed mean biases below 3.5 mm and no significant differences from tape measurements. These findings support smartphone photogrammetry as a potential accessible alternative to commercial body scanners and applicable for longitudinal 3D body-shape assessment.

---


### 71. [Semantic Steering for Controllable Generation: Tuning-Free Concept Erasure in Multimodal Diffusion Transformers](https://arxiv.org/abs/2608.12829)

**<font color=#1a73e8>作者：</font>** Qiao Li, Xiaomeng Fu, Yuanshu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Diffusion Transformers (MM-DiTs) have demonstrated remarkable text-to-image generation performance, surpassing traditional U-Net-based diffusion models. Nevertheless, their powerful generative capabilities also raise significant safety concerns, as they may generate sensitive or inappropriate content. While existing concept erasure methods aim to mitigate such risks, most require modifying model parameters, which are often architecture-specific and impractical for deployed larger models. Several tuning-free approaches face challenges when applied to advanced large-scale MM-DiTs due to their deeply embedded knowledge, broad semantic space, and context-dependent text encoders. To address these challenges, we propose to erase concepts by directly manipulating the model's internal representations. Our key insight, derived from an in-depth analysis of MM-DiT's block-wise generative roles, is that text-conditioned semantic representations are most salient in the middle blocks of MM-DiTs. Based on this, we extract representations of an unwanted concept and a desirable safe one from the middle block, construct a steering vector from their difference, and inject this single vector into consecutive early and middle blocks. By operating exclusively on the sparse text-branch tokens and leveraging the straight sampling trajectory of rectified flow, our method achieves effective concept erasure with negligible overhead and without any training. Extensive experiments across MM-DiT models demonstrate that our method achieves state-of-the-art performance in erasing diverse concepts, enables effective control over the final output, and remains robust to adversarial attacks.

---


### 72. [CABS+: Efficient and Scalable Model Merging via Conflict-Aware Sparsification and Adaptive Weight Allocation](https://arxiv.org/abs/2608.12842)

**<font color=#1a73e8>作者：</font>** Yuchen Liu, Zongzhen Yang, Binhang Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging has recently attracted significant attention as a promising paradigm for constructing unified multi-task models without requiring additional retraining. However, parameter conflicts and knowledge interference across tasks often degrade merged-model performance. Prior work introduced Conflict-Aware and Balanced Sparsification (CABS), which reduces parameter interference through structured pruning and sequential masking. However, CABS relies on grid search to determine scaling coefficients, resulting in exponential time complexity, while its optimization objective can be dominated by high-performance tasks, leading to suboptimal overall performance. To address these limitations, we extend CABS and propose CABS+. Specifically, Adaptive Weight Allocation (AWA) optimizes merging coefficients via a gradient-free search scheme to reduce time complexity, while an asymmetric fitness function promotes more comprehensive performance gains across tasks. Moreover, we conduct a systematic empirical study of key factors influencing model merging performance and propose Relative Synergy Score (RSS) to quantify model mergeability and guide model selection. We compare CABS+ with state-of-the-art model merging methods, including CABS, AdaMerging, and WUDIMerging, across 27 datasets and 5 models covering large language, small-scale language, and vision models. Extensive experiments verify the effectiveness and efficiency of CABS+. Compared with AdaMerging and WUDIMerging, CABS+ improves overall performance by 16.97% and 12.93%, respectively, exhibits stronger stability and robustness across varying task numbers and model architectures, uses less than 25% of the GPU memory required by AdaMerging, and achieves nearly a 4x speedup in merging time over WUDIMerging.

---


### 73. [Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories](https://arxiv.org/abs/2608.12847)

**<font color=#1a73e8>作者：</font>** Yifei Li, Heng Wang, Lingling Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval can identify a past trajectory that may matter, yet it does not specify how an acting agent should use that trajectory after users, entities, constraints, or environment state have changed. We identify this post-retrieval reuse step as a distinct bottleneck for long-horizon trajectory memory and formulate an evaluation framework that holds candidate retrieval, target state, model, decoding, and tool budget fixed while varying the support delivered to the agent. We instantiate the framework with query-conditioned reuse (QCR), a deliberately simple target-bound note that records a reusable procedure, bindings to recover, applicability conditions, and verification requirements. QCR serves to test the reuse hypothesis rather than to claim a universally preferred memory format. Across 2,391 target instances in WebArena, WorkArena, and AppWorld, QCR reaches 62.3% average Success, 10.7 points above Full Trajectory, while using 48.9% fewer online tokens. Summary reranking selects a reusable memory for 94.8% of targets, placing end-task Success within 1.8 points of an oracle reusable selector. Analyses by trajectory length and source--target binding shift show that direct trajectory injection loses much of its utility as traces grow longer or source-specific values change, whereas target-bound support preserves a larger share of the measured gain. The resulting framework separates retrieval quality from the problem of turning retrieved experience into safe, useful support for a new task.

---


### 74. [Beyond Source: An Empirical Study of Python Bytecode Security Risks](https://arxiv.org/abs/2608.12853)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Tian Xie, Wen Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Python package security is largely source-centric, yet Python runtimes can execute bytecode directly through .pyc files, compiled-only modules, and marshalled code objects, creating an inspection-execution gap. We present an empirical study of Python bytecode as a security artifact. We measure bytecode exposure in PyPI distributions, evaluate practical analyzability using version-aware tooling, assess CPython runtime robustness under adversarial bytecode, and test source-level reproduction of bytecode findings. Across 1,034,843 collected PyPI artifacts, we identify 7,388 bytecode-containing artifacts, including 228,578 .pyc files and 28,193 artifact-local source-less .pyc files. For modern CPython 3.8-3.14 bytecode, at least one selected decompiler emits source for 204,901 of 204,904 in-scope files, a result measuring emission rather than verified functional equivalence. Tools are non-robust: observed PyPI bytecode triggers managed-code exceptions and timeouts, while adversarial mutated bytecode also drives decompilers into native process failures; together these outcomes yield 17 distinct robustness signatures. Fuzzing produces 1,009 stack-deduplicated runtime findings dominated by pointer-dereference symptoms; 261 groups exhibit potential memory-corruption characteristics, and at least 91.7% of groups reach execution beyond the documented-unsafe ingestion boundary. None reproduce from ordinary Python source. Bytecode is thus a visible ecosystem artifact, a practical analysis target, and a security-relevant interpreter input whose behavior need not match source-level behavior.

---


### 75. [PolyPresentation: A Multimodal AI Platform for Slide-Aware Iterative Presentation Practice](https://arxiv.org/abs/2608.12857)

**<font color=#1a73e8>作者：</font>** Chen Chen, Jihao Li, Zhiyuan Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Presentations are essential for students, researchers, and professionals to communicate ideas persuasively, yet delivering them effectively requires repeated practice that coordinates content, delivery, visual materials, and audience interaction. Existing AI-assisted rehearsal tools provide scalable feedback, but they often treat presentations as single-run delivery performances, offering limited support for linking feedback to the slide deck or planning what to practice in the next iteration. To address this gap, we introduce PolyPresentation, a multimodal AI platform for slide-aware iterative presentation practice. PolyPresentation organizes slide-by-slide practice, full rehearsal, audience Q&A, and feedback into a unified practice loop, using slide-grounded evidence to help presenters diagnose performance issues and prepare for subsequent practice. We evaluate PolyPresentation through a rubric-based comparison with four baseline systems on 20 academic presentation rehearsals, and additionally assess its alignment with human ratings. Results suggest that PolyPresentation provides more actionable, context-aware, and practice-oriented support for improving presentations. The demonstration video is available at this https URL.

---


### 76. [AI and Consumer Rights in India Working Paper](https://arxiv.org/abs/2608.12863)

**<font color=#1a73e8>作者：</font>** Omir Kumar, Sriya Sridhar, Vibhav Mithal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems proliferate in consumer facing applications, questions about liability for AI related harms remain unresolved. This working paper examines whether India's Consumer Protection Act, 2019, adequately addresses harm caused by defective AI products and services, and whether it proportionately allocates liability across the AI value chain.
The Act's broad definitions of product liability, harm, and deficiency appear technology agnostic and potentially applicable to AI related incidents including personal injury, psychological harm, biased outputs, and loss of control. However, significant gaps remain. Proving causation between AI defects and consumer harm presents a technical challenge, as AI failures often stem from design choices rather than discrete defects. Additionally, the Act's framework assumes distinct roles for manufacturers, sellers, and service providers, yet the AI value chain involves overlapping responsibilities among data providers, model developers, deployers, and users that do not neatly map to these categories. Current liability frameworks lack proportionate mechanisms to effectively address complex, multistakeholder AI harms. While the Act may cover AI entities, enforcement requires clarification on sector specific overlaps.

---


### 77. [Discovering Persistent Behavioural Patterns for Interpretable Blockchain Forensics](https://arxiv.org/abs/2608.12864)

**<font color=#1a73e8>作者：</font>** Dorottya Zelenyanszki, Zhe Hou, Kamanashis Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public blockchain data enables large-scale DeFi-related analysis, but many existing approaches are application-specific, difficult to scale, or hard to interpret. This research proposes a scalable, application-agnostic framework for \emph{persistent behavioural pattern discovery} from large-scale blockchain activity. It constructs behaviour sentences enriched with contract, token and market context, then applies a two-step embedding process: sentence-level embeddings capture individual actions, while sequence-level embeddings capture user behaviour over time. An interpretable behavioural profiler characterizes discovered communities through behavioural motifs, routines, temporal dynamics, entity exposure, and suspiciousness evidence. Evaluation on Ethereum using over 30 million transactions shows that the framework uncovers both routine and malicious behavioural patterns, including decentralised exchange (DEX) trading, NFT activity, phishing, bot operations, oracle manipulation, and rug-pull schemes. Importantly, many patterns remain stable across independent observation windows, enabling the identification of long-term behaviours beyond a single analysis period. The proposed framework combines scalability, interpretability, and persistence analysis, supporting blockchain forensic investigation, behavioural attribution, and threat discovery.

---


### 78. [A Compositional Theory of Curvature in Probabilistic Circuits](https://arxiv.org/abs/2608.12869)

**<font color=#1a73e8>作者：</font>** Hrithik Suresh, Sahil Sidheekh, Shelar Parth Vijay 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic Circuits (PCs) are generative models that support exact inference and, unlike deep neural networks, admit an exact and tractable measure of loss-surface curvature: the trace of the Hessian of the log-likelihood. Recent work regularizes this trace globally to bias learning toward flatter, better generalizing optima. We show that treating sharpness as a global regularizer can be misspecified for PCs, whose curvature is inherently compositional. We prove that each sum node's contribution to the Hessian trace factorizes exactly into its circuit flow, which measures how heavily the node is used, and a local sharpness term determined by its output distribution. This decomposition provides insights into why global sharpness regularization is depth biased and can lead to underfitting. Building on it, we introduce an adaptive sharpness aware regularizer that penalizes nodes based on intrinsic local curvature and preserves closed form EM updates. We also show that empirically, this targeted regularization recovers the generalization that global regularization sacrifices while retaining the robustness and benefits of sharpness aware learning.

---


### 79. [Sustaining Plasticity via Learnable Wavelet Activations in Continual Learning](https://arxiv.org/abs/2608.12874)

**<font color=#1a73e8>作者：</font>** Zeyang Zhang, Tieliang Gong, Junyan Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plasticity loss has emerged as a critical challenge in continual learning that significantly hinders the acquisition of sequential tasks. While optimizing activation designs offers a potential solution, current fixed-form functions suffer from an inherent spectral bias towards low-frequency variations, whereas learnable variants permit unconstrained updates that induce catastrophic forgetting. To address these limitations, we propose a novel learnable wavelet activation that decomposes the activation function into low-frequency and high-frequency components to explicitly counter spectral bias. Furthermore, we employ dynamic wavelet injection to adaptively enhance plasticity for new tasks, alongside a regularization strategy to ensure the stability of previous learned knowledge. Theoretically, we provide rigorous mathematical guarantees for the proposed framework, proving the structural necessity of the hybrid wavelet architecture for efficient $L^2$ approximation and demonstrating that the decoupled learning rate mechanism successfully restores network plasticity for high-frequency information. Additionally, we provide a formal derivation of the loss-driven injection trigger mechanism to precisely guide the injection. Extensive empirical evaluations demonstrate that our approach maintains superior trainability and generalization throughout the learning process and achieves state-of-the-art performance across diverse continual learning benchmarks.

---


### 80. [ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification](https://arxiv.org/abs/2608.12877)

**<font color=#1a73e8>作者：</font>** Runze Zhao, Zixin Tang, Xiaoshuai Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However, these methods face two critical limitations: (1) agents may perform individual subtasks without sufficient awareness of the global verification objective, causing their reasoning to deviate from the intended direction; and (2) conflicts between parametric knowledge and the provided evidence may undermine evidence-grounded reasoning and lead to incorrect verdicts. To address these challenges, we propose ReflectFact, a novel self-reflective agent framework for multi-hop fact verification. ReflectFact introduces three key tasks. Explicit Reasoning Path Planning builds an evidence-grounded reasoning path by resolving implicit entities, decomposing the claim into sub-questions, and integrating the verified facts into a verdict. Evidence-Drift Verification makes the agent re-answer by quoting the supporting evidence when a grounded answer merely echoes its parametric prior, thereby calibrating evidence deviation to ensure grounded comprehension. Reasoning Reflection Verification re-examines each reasoning step and regenerates it once an inconsistency is detected, correcting reasoning flaws such as location bias and replacement bias through a global task perspective. Subsequently, the agent aggregates validated reasoning chains to yield reliable verdicts. Extensive experiments on HOVER and EX-FEVER demonstrate that ReflectFact effectively remedies the comprehension and reasoning defects of existing methods, achieving state-of-the-art performance and respectively outperforming the strongest baseline by 3.32\% and 2.78\% on the two datasets.

---


### 81. [Robust data-driven discovery of fractional differential equations via weak formulations and Pareto-based subset selection](https://arxiv.org/abs/2608.12879)

**<font color=#1a73e8>作者：</font>** Pongpisit Thanasutives, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fractional partial differential equations describe nonlocal dynamics, but discovering them from noisy data is difficult because fractional differentiation amplifies high-frequency measurement noise and the derivative orders are unknown. We propose Weak-Pareto, which combines an adjoint-consistent weak formulation of fractional terms with Pareto-based subset selection over discrete term types and continuous fractional orders. For linear right-hand-side terms, the adjoint transfers fractional operators from measured fields to smooth test functions, replacing noise-sensitive pointwise differentiation with smoothing integration; for nonlinear terms, the noise-suppression effect is partial yet useful. Coefficients are fitted by ridge regression within a branch-aware differential-evolution search over the orders. The support size is then selected at the validation-error-complexity elbow. We show that the variance of fixed linear right-hand-side weak features vanishes under grid refinement, whereas noise amplification in pointwise fractional features increases with derivative order. Across fractional advection-diffusion, reaction-diffusion, and Burgers benchmarks, Weak-Pareto recovers parsimonious structures from clean and noisy measurements. In controlled advection-diffusion and Burgers comparisons, it retains the correct support at every tested multiplicative-noise level, whereas the unregularised strong-form counterpart largely fails once noise is introduced; this advantage persists under additive Gaussian noise. Ablations show that the weak library drives noise robustness and that continuous-order Pareto search avoids the support-selection failure of a dense fixed dictionary. On the advection-diffusion benchmark, Weak-Pareto yields more consistent operator recovery and substantially lower measured runtime than a contemporary neural baseline.

---


### 82. [Adversarial Robustness in Smishing Detection: A Comparative Analysis of Adversarial Fragility in Classical vs. Transformer-Based Detection Systems](https://arxiv.org/abs/2608.12889)

**<font color=#1a73e8>作者：</font>** Denzel Chiuseni, Athanase Bahizire, Silva Hama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smishing detection systems are commonly trained and evaluated on clean, monolingual text. In low-resource settings, however, attackers frequently circumvent these systems through character obfuscation, cross-lingual code-switching, and structural perturbation. This study evaluates adversarial robustness for five model architectures: three classical lexical models (Random Forest, XGBoost, CNN+BiLSTM) and two multilingual transformers (mBERT, XLM-RoBERTa), using a dataset of 27,037 messages. Classical models are subjected to black-box generic attacks, while transformers are evaluated with attention-guided targeting. Each model is tested across three attack types and intensity levels, with performance measured by the Robustness Degradation Ratio (RDR). The results reveal a distinct architectural boundary: classical models experience near-catastrophic failure under character obfuscation and structural perturbation (RDR up to 0.988), whereas transformers demonstrate significantly greater resilience (RDR up to 0.351), with structural perturbation representing their most pronounced vulnerability. Effect-size analysis (Cliff's d) indicates a substantial difference between the two model categories. Within the transformer group, XLM-RoBERTa, despite achieving a higher clean-text baseline, exhibits greater degradation than mBERT. These findings demonstrate that clean-text performance is not a reliable predictor of adversarial robustness. Statistical validation using Mann-Whitney U and Friedman tests confirms that these patterns are attributable to model architecture rather than sampling. The results underscore the necessity for architecture-specific defences and frame smishing detection as an adversarial cybersecurity challenge rather than a static classification task.

---


### 83. [Predictive Memory Localization: Forecasting Selective Intervention Paths from Internal Signals](https://arxiv.org/abs/2608.12892)

**<font color=#1a73e8>作者：</font>** Jinhao Jing, Tian Zeyu, Lucas Qingyang Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering turns localized representations into control directions, but localization alone does not reveal whether a direction has a selective operating regime. We introduce Predictive Memory Localization (PML), which treats the measured-grid intervention path as the predictive object of memory localization. PML separates random-calibrated target movement from semantic-neighbor and capability damage, and compares static localization and supervised geometry with a strength-disjoint low-dose causal response. Our frozen study covers 3,000 records from nine datasets and fourteen domains, yielding 30,000 distinct record-direction-layer paths and 210,000 distinct path-strength evaluations. At layer 7, the geometry-derived RFM/AGOP direction reaches 13.1% target-any and 12.3% clean-any, exceeding random by 3.6 and 3.4 percentage points under a record-paired bootstrap. Across record-, dataset-, and domain-grouped splits, responses at $|\alpha|=0.1$ are the strongest signal for outcomes at disjoint strengths $|\alpha|\in\{0.25,0.5\}$. On held-out records, a predictor-driven selector chooses a coefficient or abstains, improves utility and reduces semantic-neighbor damage relative to a train-tuned fixed-strength policy, and avoids most evaluations in a dense scan. Across three residual-norm-matched base models, learned directions retain selective-path gains and low-dose responses yield 0.801-0.828 record-held-out macro AUROC. PML therefore turns memory localization into a falsifiable forecast of margin-level selective outcomes and a risk-aware intervention decision.

---


### 84. [Adaptive $k$ Nearest Neighbors Classifier via Granular Ball Computing](https://arxiv.org/abs/2608.12903)

**<font color=#1a73e8>作者：</font>** Xiaoyu Lian, Shuyin Xia, Hongxuan He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The $k$-Nearest Neighbor~(KNN) algorithm is widely used across various tasks. The selection of the $k$ value is a key issue because it significantly impacts performance. In this paper, an adaptive and efficient KNN approach via granular-ball computing is proposed. The method consists of two stages. \textcolor{black}{In the training stage, the dataset is first coarsely partitioned to reduce the complexity of data distributions within a granular ball, and then the Fisher criterion is introduced to control ball splitting and stopping, yielding a multi-granularity granular ball representation. In the prediction stage, the nearest granular ball is first located through a weighted distance mechanism, and an adaptive neighborhood is then constructed around the test sample. The effective $k$ value is dynamically determined by the actual number of samples contained in this neighborhood. The neighborhood induced by the nearest granular ball provides more stable local group information, thereby improving robustness against noise and local perturbations.} Experimental results demonstrate that the proposed method outperforms existing KNN variants across multiple datasets in terms of both accuracy and efficiency. The code has been open-sourced for reproducibility: this https URL.

---


### 85. [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](https://arxiv.org/abs/2608.12904)

**<font color=#1a73e8>作者：</font>** Yunhao Bai, Zhongwei Qiu, Guangyu Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-dependent prediction problems. To operationalize this view, we introduce HounsBench, a computed tomography (CT) centric patient-state benchmark that unifies these three task families with patient-disjoint splits and per-family metrics, and HounsWorld, a 3B multimodal world model that treats volumetric scans and language as observations of the shared state through Joint Understanding-Generation Learning. A shared transformer forms an implicit patient-state estimate and supports three outputs: query-conditioned answers that read out the state, reports and captions that reconstruct it in language, and condition-specific CT volumes for low-dose denoising, virtual contrast enhancement, and anatomy-constrained text-and-mask-to-volume generation. Zero-initialized CT adapters preserve pretrained multimodal mappings, while condition-explicit Hounsfield-unit window sampling exposes clinically meaningful density observations. HounsWorld shows strong performance across all three task families while consistently improving CT understanding through clinically structured completion. Our project is available at this https URL

---


### 86. [EGRL: Edge generation-guided relation-aware learning for RNA-protein interaction prediction](https://arxiv.org/abs/2608.12906)

**<font color=#1a73e8>作者：</font>** Danyu Li, Ling Zhou, Rubing Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RNA-Protein Interactions (RPIs) are critical for regulating cellular functions. While traditional wet-lab experiments for RPI detection are costly and time-consuming, Deep Learning (DL) methods provide an efficient computational alternative for RPI Prediction (RPIP). In particular, Graph Neural Networks (GNNs) are promising, as they naturally model RPI networks. However, existing GNN-based methods often rely on homogeneous graphs or predefined meta-paths, which limit their ability to handle data sparsity and to generalize to cold-start scenarios involving unknown molecules. To address these limitations, we propose Edge Generation-guided Relation-aware Learning (EGRL), a novel framework with several key components: implicit meta-path learning to capture relational semantics without handcrafted paths; a multi-relation-aware attention mechanism for adaptive fusion of interaction patterns; a graph generator that predicts potential ("soft") edges to support cold-start nodes; and a multi-feature fusion predictor for final interaction scoring. EGRL is jointly trained with a primary task loss and an auxiliary generator loss. Comprehensive evaluations on four benchmark datasets demonstrate that EGRL achieves competitive overall performance. More importantly, it exhibits superior generalization in cold-start settings, achieving an Area Under the Receiver Operating Characteristic curve (AUROC) of 0.867 and an Area Under the Precision-Recall curve (AUPR) of 0.861 on unknown molecules, corresponding to improvements of 8.6% in AUROC and 5.0% in AUPR over prior state-of-the-art methods. The code will be released soon.

---


### 87. [Revisiting Overestimation Bias Problem of Q-learning: Settling Large Discrete Action Space via Action Intersection](https://arxiv.org/abs/2608.12912)

**<font color=#1a73e8>作者：</font>** Pu Li, Tao Tan, Hong Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper considers the overestimation bias problem of Q-learning in the setting of a large action space, for the purpose of relieving the bottleneck of existing methods. We find that the large action space increases the randomness in Q-value estimation. The randomness makes two paradigms that drive the major literature on the overestimation problem have their own bottlenecks: the coupling paradigm, i.e., the optimal action and its Q-value are estimated with the same Q-function, always has a positive bias. This is because randomness leads to some actions having abnormally high estimated values than their true values, and the coupling methods prefer these actions. The decoupling paradigm, i.e., the optimal action and its Q-value are estimated with two independent Q-functions, always has a negative bias. This is because randomness increases the estimation gap between the two independent Q-tables for the same action. This paper shows that action intersection can be a simple yet powerful strategy to relieve these bottlenecks. The action intersection strategy enables semi-decoupling via two designs: (1) it allows two Q-functions to share a certain fraction of trajectory data; (2) if a data sample is shared, each Q-function is updated using the coupling paradigm; otherwise, using the decoupling paradigm. Two properties make the action intersection strategy powerful: (1) attaining a large bias range, i.e., varying the data sharing fraction, the estimation bias varies from underestimating to overestimating; (2) fine granularity: the action intersection size can be made arbitrarily finer to enable finer control. We consider two experiment settings, i.e., tabular and deep RL, deep RL experiments show that our method outperforms several SOTA baselines drastically; tabular experiments reveal why our method can achieve superior performance.

---


### 88. [Decoupled Contrastive Decoding via Expert-Aligned Drafting](https://arxiv.org/abs/2608.12913)

**<font color=#1a73e8>作者：</font>** Zhixuan Liu, Zhichen Dong, Yuanfu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contrastive Decoding (CD) improves generation quality, but its amateur-model pass makes decoding expensive. Accelerating CD with speculative decoding raises a proposal-alignment question: should the contrastive signal shape the drafter, or should it remain only in verification? We study this question in the lightweight feature-level drafter regime. Two controlled diagnostics, matched Cross-alpha training and an Approximate Dual-Drafter decomposition, give the same diagnosis: contrastive-aware drafting does not consistently improve over expert-aligned drafting because the contrastive correction is usually weaker than drafter error, and reconstruction can amplify that error. We introduce Decoupled Contrastive Decoding (DCD), which drafts with an expert-aligned lightweight proposer and applies the amateur only in unchanged CD verification. Standard speculative verification preserves the vanilla-CD output distribution. Across the main 8B settings, EAGLE3-based DCD achieves average greedy speedups of 1.65 to 1.95x over vanilla CD and reduces MMLU proposal-path latency by about 5 to 12x relative to amateur-coupled proposal paths.

---


### 89. [Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling](https://arxiv.org/abs/2608.12917)

**<font color=#1a73e8>作者：</font>** Takieddine Soualhi, Jacques Saraydaryan, Laetitia Matignon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing effective robot navigation methods in crowded environments is essential for real-world applications. Although recent deep reinforcement learning (DRL) methods have improved navigation performance in crowded environments, they often focus primarily on task-centric objectives and underrepresent social compliance objectives. In this paper, we introduce a novel proxemics-based reward formulation for DRL social navigation that provides a dense, interpretable social learning signal while maintaining navigation efficiency. Our approach models each human's personal space as a radial Gaussian-mixture field derived from Hall's proxemics theory and computes a robot-centric local cost over the robot's field of view. We integrate the proposed reward into established DRL navigation methods and evaluate it in simulation across multiple crowd scenarios, reward baselines, and crowd densities using both navigation metrics and social metrics. Results show that the proposed reward consistently improves social metrics in simulation while maintaining competitive navigation performance relative to the compared reward models.

---


### 90. [Momentum as Residual-Driven Multiplier Correction for Deep Learning Optimization](https://arxiv.org/abs/2608.12925)

**<font color=#1a73e8>作者：</font>** Zhixin Ren, Yau Lyu, Congrong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Momentum-based optimizers are widely used in modern deep learning, yet the relations among momentum recursion, update geometry, and acceleration remain only partially understood. We develop an $\textbf{A}$DMM-$\textbf{I}$nspired $\textbf{M}$omentum (AIM) framework based on residual-penalty variable splitting, which interprets momentum as a multiplier-like correction driven by the splitting residual. AIM recovers the exponential moving average of gradients from an ADMM-style multiplier update and separates two mechanisms that are usually intertwined in practical optimizers: the residual penalty determines the update geometry, whereas the approximation of the objective-related subproblem determines the acceleration form. Building on AIM, we propose $\textbf{R}$elativistic $\textbf{A}$daptive gradient $\textbf{D}$escent with $\textbf{A}$ccelerated $\textbf{R}$esidual (RADAR), which combines relativistic adaptive geometry, decoupled residual correction, and second-order momentum filtering to improve the update direction and momentum estimation. We establish stochastic convergence through a variance-perturbed Lyapunov drift analysis. Experiments on supervised vision learning, language modeling, and reinforcement learning show that RADAR achieves consistent improvements over strong adaptive optimizer baselines.

---


### 91. [H-VAEP and H-xT: Valuing Offensive On-the-Ball Actions in Handball by Estimating Probabilities](https://arxiv.org/abs/2608.12926)

**<font color=#1a73e8>作者：</font>** Julius Broermann, Oliver Müller, Michael Döring 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional player evaluation in professional handball relies on basic box-score metrics or heuristic indices, which fail to credit the multi-player build-up chain. While football (soccer) analytics has adopted Expected Threat (xT) and Valuing Actions by Estimating Probabilities (VAEP), these event-based action valuation frameworks have not yet been adapted to handball. In this paper, we present the first comprehensive adaptation and evaluation of xT and VAEP for handball, utilizing five seasons of tracking-derived event data from the Handball Bundesliga. We develop Handball-xT (H-xT) using a handball-native court zoning layout, demonstrating via simulations that it is systematically more robust than standard rectangular grids. We optimize Handball-VAEP (H-VAEP) by tailoring its feature space and selecting the context length to limit team-identity leakage. Our evaluation shows that H-VAEP yields exceptionally stable, discriminative, and intuitive player ratings that highlight build-up play. Finally, we release our complete code repository to help professional clubs deploy these models.

---


### 92. [Multi-perspective Imbalance-Conscious 6G Beamforming Optimization and Performance](https://arxiv.org/abs/2608.12929)

**<font color=#1a73e8>作者：</font>** Chukwunonso Henry Nwokoye, Blessing Oluchi Iloka, Chikwue V. Umeugoji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The study presents a systematic machine learning (ML) study of 6G-IoT beamforming optimization (6GBO) using supervised and unsupervised approaches. We compared the predictive power of network, environmental, device, and vision feature groups for 6GBO. Additionally, it addressed other unsupervised perspectives that can enhance 6GBO, including clustering network scenarios using methods such as K-means, DBSCAN, and hierarchical clustering. Several imbalance-aware experiments revealed that network features possess better prediction power than device, environmental, and vision feature groups, as evidenced by their recall, F1-score and ROC-AUC values. For unsupervised ML exploration (assessed using Elbow, Silhouette score, and Davies-Bouldin Index methods), the results indicate that the deployment environment and type of device primarily influence clustering, rather than mobility-based attributes. Furthermore, the explainability analysis showed that bandwidth, IoT sensors, and mobility possess higher global feature importance across the feature groups. In the future, we would apply deep and reinforcement learning techniques to predict throughput/latency or to optimize rewards determined by performance indicators like SNR enhancement

---


### 93. [Decomposition of Evidence, Contradiction, and Fragility in Perturbation Responses](https://arxiv.org/abs/2608.12935)

**<font color=#1a73e8>作者：</font>** Lei You  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Perturbation methods explain model decisions by measuring prediction changes under altered inputs, but response magnitude tells us only how much a model reacts, not what that reaction means. The same magnitude can support the final factual-counterfactual difference, oppose it, or arise strongly along the perturbation path yet vanish at the endpoint. We therefore track how the contrast develops as paired inputs are progressively revealed, using the final contrast to interpret the trajectory. We introduce DECAF (Decomposition of Evidence, Contradiction, And Fragility), which routes aligned, opposed, and endpoint-null responses into evidence E, contradiction C, and fragility F. The decomposition preserves ordinary magnitude exactly, Abs = E + C + F, and is unique under endpoint-relative axioms. Across controlled vision and tabular settings, the three components track independently measured behavior. In a 72-model ImageNet-9 audit, we compare cases with nearly identical response magnitude but different independently measured behaviors. The largest DECAF component agrees with an observed behavior in 96.4% of cases, compared with 35.0% for magnitude alone. Changing only the reveal path increases total response by nearly 80%, yet evidence barely changes while fragility grows by more than 4x. On FunnyBirds and ImageNet-1k, short forward-only DECAF trajectories outperform the tested general-purpose attribution baselines. On a 1B-scale DINOv2 model, a short trajectory matches a strong gradient-based baseline with 4.75x lower wall time and 2.36x lower peak memory.

---


### 94. [Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency](https://arxiv.org/abs/2608.12939)

**<font color=#1a73e8>作者：</font>** Guo An, Zijing Wu, Honghua Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) learn world models that predict in a compact latent space rather than in pixels, reducing the pressure to model nuisance appearance. Yet this provides no guarantee against visual perturbations: they can still alter the encoded representation and affect subsequent action-conditioned predictions. Bisimulation captures this requirement precisely: two observations should be treated as the same state only when their action-conditioned consequences agree. Guided by this criterion, we introduce Action-Conditioned Predictive Consistency (ACPC), a diagnostic that measures how far a clean history and a visually perturbed view of it diverge after being rolled forward under the same action sequence. We prove that this divergence bounds the perturbation-induced change in multi-step prediction error and planner cost. Building on pairwise ACPC, we define two complementary measures: the Invariance Radius (IR) summarizes clean-perturbed rollout spread, while the Separation Rate (SR) checks whether different states remain distinguishable after rollout. Experiments on four visual control tasks show that pairwise ACPC predicts perturbation-induced prediction and cost changes. On LeWM, the IR-SR screen transfers across tasks, and the joint diagnostic remains informative under blur and resize. PLDM exhibits similar diagnostic trends under a different architecture.

---


### 95. [CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation](https://arxiv.org/abs/2608.12944)

**<font color=#1a73e8>作者：</font>** Hamza Shafiq, Hung Manh Pham, Bin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiography (ECG), photoplethysmography (PPG), and phonocardiography (PCG) provide complementary views of the same cardiac cycle, yet existing cardiac foundation models are trained for a single sensing modality, leaving the shared physiology across sensors unexploited. We introduce CardioState-JEPA, a cardiac foundation model to learn a single shared representation jointly across ECG, PPG, and PCG, built on a physiology-aware joint-embedding predictive architecture. The model maps heterogeneous waveforms into a common token space, processes them with a single shared Transformer encoder, and learns by predicting masked latent cardiac states, placing the pretraining target on shared physiology rather than sensor-specific waveform appearance. To handle the temporal offsets between electrical, mechanical, and hemodynamic events, cross-modal prediction uses a learned delay aligner that matches signals at the corresponding cardiac time. Because synchronized multi-sensor recordings are scarce, CardioState-JEPA first learns within-modality structure from abundant unimodal data and then uses paired data to align modalities in latent cardiac time. Evaluated as a frozen encoder across 25 downstream tasks spanning ECG, PPG, and PCG, our encoder improves average PPG classification by 8.2 AUROC points, PCG murmur detection by 18.8 AUROC points, and ECG classification by 15.5 AUROC points over the best self-supervised signal baseline and matches or exceeds cardiac models trained with privileged clinical text or supervised labels on several ECG benchmarks. These results establish that heterogeneous cardiac signals can mutually supervise a single foundation model of cardiac physiology.

---


### 96. [The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use](https://arxiv.org/abs/2608.12959)

**<font color=#1a73e8>作者：</font>** Joyjeet Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models are judged by how well they predict, so when planning fails at long horizons the natural reading is that the predictor degrades. On a reproduction of LeWorldModel on TwoRoom we show the binding constraint is the planner's objective instead.
The predictor is not the limit: its imagined state seventy-five environment steps ahead is still only 0.189 as wrong as assuming the world froze, while the planner never imagines beyond twenty-five. The objective is. Cross-entropy-method planning minimises squared latent distance, which tracks true distance at r = 0.426, saturates by about eighty arena units and decreases beyond a hundred and twenty, so moving away from the goal can lower the cost. The information is present throughout: a ridge probe recovers position from the frozen embedding at R^2 0.9922.
The pathology is the method's, not one reimplementation's. It is present in the authors' released weights, and across four checkpoints long-horizon success rank-orders exactly with metric quality and inversely with prediction accuracy.
Replacing only the objective, with nothing retrained and no GPU, lifts goals reached at offset 100 from 26.0% to 98.0%, equals the 98.0% at offset 25, and reaches 92.0% under a third of the budget: planning stops depending on the horizon. The best cost is not the most accurate. A head learned from frame separation alone predicts spatial distance worse than a position probe (r = 0.819 against 0.9897) yet plans better, charging 24% more to cross the environment's dividing wall where squared latent distance charges 4% less. It has learned reachability, not proximity.

---


### 97. [Moose: Latent concept learning with reasoning-shortcut awareness in $\mathcal{EL}^{++}$](https://arxiv.org/abs/2608.12961)

**<font color=#1a73e8>作者：</font>** Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The OWL 2 EL profile is used in some of the largest production ontologies, including the Gene Ontology and SNOMED CT. Existing neuro-symbolic (NeSy) learning methods accept propositional theories or Datalog, and reasoning-shortcut (RS) awareness has not been investigated in ontology settings. We present Moose, a method that compiles an $\mathcal{EL}^{++}$ TBox and finite ABox to a Sentential Decision Diagram (SDD). The SDD acts as a differentiable weighted-model-counting layer, and we add closure clauses outside the $\mathcal{EL}^{++}$ profile on declared exhaustive families to overcome the limited expressivity of $\mathcal{EL}^{++}$ under partial supervision. We show termination, soundness, completeness, and polynomial intermediate sizes, and validate the proofs in Lean. We then define the first formal partial-supervision latent-concept-learning task over an OWL EL ontology, i.e., learning per-individual classifiers for latent concepts from observed ABox literals, and evaluate Moose on MNIST-with-ontology and Pizzaïolo. Moose improves over propositional-NeSy, fuzzy-logic, and ontology embedding baselines, and presents the first reasoning-shortcut analysis in an OWL EL setting.

---


### 98. [Understanding Backdoor Vulnerabilities in Vertical Federated Learning: The Gap Between Research and Practice](https://arxiv.org/abs/2608.12962)

**<font color=#1a73e8>作者：</font>** Ziqi Zhao, Jialin Lu, Junjie Shan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vertical Federated Learning (VFL) enables organizations holding complementary features of shared entities to collaborate and train models. In this setting, the initiator can withhold information about the learning task, while other contributors participate without exposing their local datasets, creating an asymmetric information structure aligned with growing privacy demands. However, this asymmetry is a double-edged sword. Among various threats, backdoor attacks are particularly concerning because VFL not only enables malicious contributors to poison the model during training, but also allows them to activate the backdoor at inference time to manipulate predictions. Although prior work has reported near-perfect attack success rates and proposed effective defenses, we find that most findings fail to hold under realistic conditions, exposing a fundamental gap between research and practice. In this paper, we present a systematic, practice-oriented study of backdoor vulnerabilities in VFL, revealing this gap in both methodological design and evaluation practices. We show that existing approaches overlook key practical constraints and therefore rely on unrealistic prior knowledge. Furthermore, these limitations have remained hidden due to poorly designed evaluation practices in the literature. To bridge this gap, we redefine threat models under realistic constraints, propose practical backdoor workflows, and introduce BVBench, a backdoor-centric benchmark that enables fair, practical, and comprehensive evaluation, preloaded with state-of-the-art baselines. BVBench provides strong evidence of the fragility of the current understanding of VFL backdoor risks and establishes a foundation for steering research toward uncovering practical vulnerabilities and developing more meaningful defenses.

---


### 99. [Bias Mitigation in Face Recognition via Demographic-based Supervised Contrastive Learning](https://arxiv.org/abs/2608.12971)

**<font color=#1a73e8>作者：</font>** Yu Linghu, Salman Mohammad, Xinyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems have been shown to be biased toward certain demographic groups by exhibiting different error rates across gender, age, or ethnicity. Though the imbalance of the training data with respect to these demographics is one cause of this bias, training on artificially balanced groups does not completely mitigate the problem. For deployment, face recognition typically works at operating points allowing very low false match rates and, hence, on the tail of the non-match score distribution. While class balancing can improve the means of these distributions, the aim of our approach is to improve fairness by addressing the behavior in the tail. Particularly, we propose the Demographic-based Supervised Contrastive loss (DeSCon) for face recognition, which relies on a well-designed composition of training batches and demographic-aware pair selection. Our experimental evaluation on both demographically-labeled datasets and standard verification benchmarks shows that DeSCon can improve fairness beyond balancing training datasets while maintaining competitive verification performance. Source code is available upon request.

---


### 100. [Comment on "Modeling rapid language learning by distilling Bayesian priors into artificial neural networks"](https://arxiv.org/abs/2608.12974)

**<font color=#1a73e8>作者：</font>** Orr Well, Idan Tarshish, Nur Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> McCoy & Griffiths (2025, henceforth M&G) suggest that a Bayesian prior can be distilled into Artificial Neural Networks (ANNs) through Model-Agnostic Meta-Learning (MAML, Finn et al., 2017). They support this empirically by showing that meta-trained networks demonstrate formal language learning abilities comparable to Yang & Piantadosi (2023)'s Bayesian learner, significantly outperforming standard ANNs. We point out that under the standard interpretation of a prior, M&G's procedure does not actually instill one; it merely initializes network weights favorably, leaving the objective function unchanged. We then consider a more permissive interpretation, where the system as a whole can be seen as implementing a Bayesian learner even without an explicit prior in the objective. We show that this interpretation faces nontrivial challenges. Finally, we assess how well MAML approximates the empirical results of Bayesian learning, showing that unlike genuine Bayesian learners, M&G's model overfits and generalizes poorly to unseen data.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
