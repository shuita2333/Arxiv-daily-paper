# 🧠 大模型相关研究 | 2026年06月23日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 151. [When Does a Video-Language Model Stop Watching? Reward Strength Controls the Formation and Reversal of Visual Shortcuts in Multimodal RLVR](https://arxiv.org/abs/2606.22043)

**<font color=#1a73e8>作者：</font>** Zekun Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is increasingly applied to large vision-language models (LVLMs), yet outcome-only optimization can drive a model to stop attending to the video and instead exploit linguistic priors -- a failure we call a visual shortcut. While the existence of such perception bypass is by now documented, how it forms, whether it can be undone, and when intervention still helps remain open. We treat the strength of a grounding penalty, lambda, as a control knob and characterize the formation-reversal dynamics of visual shortcuts along the training time axis. On a held-out, out-of-distribution diagnostic set, we find: (i) a sharp onset -- shortcut reliance emerges abruptly over a narrow window of optimization steps and is robust across random seeds; (ii) a monotone dose-response -- increasing lambda progressively suppresses the shortcut, and at an intermediate dose the trajectory first forms and then reverses the shortcut, exposing a hysteresis-like asymmetry between acquiring and removing it; and (iii) a critical intervention window -- applying the penalty before onset arrests shortcut formation, whereas the same penalty applied after consolidation is markedly less effective. Together these results recast visual-shortcut collapse not as a binary defect but as a controllable, time-dependent, and asymmetric process, with direct implications for when and how strongly to regularize multimodal RLVR.

---


### 152. [Morphology-Aware Multimodal Representation Learning for Insect Phylogenetic Reconstruction](https://arxiv.org/abs/2606.22077)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Kaijie Yu, Chun He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphological traits provide important evidence for phylogenetic reconstruction and evolutionary relationship analysis. Recent image-based approaches have introduced deep learning, particularly convolutional models, to derive morphological features from specimen images, but these methods generally rely on single-modality visual representations and do not explicitly incorporate morphological semantics. This study proposes a morphology-aware multimodal alignment framework for insect phylogenetic reconstruction. The framework combines specimen images with curated morphological descriptions by adapting a vision transformer through parameter-efficient fine-tuning and supervised contrastive learning, followed by image-text alignment in a shared latent space. The learned image embeddings are then used as continuous traits for Bayesian phylogenetic reconstruction. On the public Rove-Tree-11 dataset, comparative and ablation experiments across multiple visual backbones and feature adaptation strategies demonstrate that multimodal alignment improves topological agreement with the reference phylogeny. The results indicate that the proposed framework can derive morphology-aware visual traits for computational phylogenetic reconstruction.

---


### 153. [Can Reasoning Models Detect Changes to their Chains of Thought?](https://arxiv.org/abs/2606.22085)

**<font color=#1a73e8>作者：</font>** Sathvik Napa, Utkarsh Singh, Chengyuan Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are many reasons one may want to edit a model's chain of thought (CoT) -- e.g., to prefill it with reasoning from a stronger model or to remove steps that may yield unsafe outputs. The success of these interventions plausibly depends on a model's inability to notice them, as the model may alter its behavior if it suspects tampering. In this work, we study whether recent reasoning models are able to detect such interventions on their CoTs under a variety of conditions: both during reasoning and after it, and when prefilled both with their own CoTs and with those of other models. Broadly, we find that (i) models exhibit only very modest detection accuracy; (ii) models struggle to identify *how* their CoT was modified; and (iii) models are about as good at detecting changes to their own CoTs as to those of other models.

---


### 154. [From Recognition to Understanding: Unlocking Cognitive Time Series Reasoning with LLMs](https://arxiv.org/abs/2606.22126)

**<font color=#1a73e8>作者：</font>** Xin Qiu, Junlong Tong, Yao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time series analysis has recently been coupled with Large Language Models (LLMs) to leverage their reasoning and world knowledge capabilities, yet gains remain limited. We attribute this to a fundamental mismatch between existing task formulations and LLM strengths: most settings reduce time series understanding to curve-fitting systems, focusing on low-level prediction while ignoring the semantic, contextual, and reasoning-intensive nature of real-world temporal this http URL address these limitations, we introduce TSCognition, a multimodal benchmark for multi-dimensional time series reasoning. It collects real-world time series and textual information from 15 public sources and constructs approximately 41K QA samples around five cognitive reasoning tasks: Decoding, Grounding, Inferring, Extrapolating, and Acting. Building on this, we further propose TSAlign, a unified framework that encodes time series into compact patch-level representations and aligns them with semantic directions in the LLM embedding space via gated residual injection and multivariate this http URL show that TSAlign outperforms existing LLM, VLM, and time series QA baselines on TSCognition and the publicly available TimerBed benchmark while substantially reducing computational this http URL is available at: [this https URL](this https URL)

---


### 155. [BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language](https://arxiv.org/abs/2606.22138)

**<font color=#1a73e8>作者：</font>** Qizhi Pei, Zhimeng Zhou, Yi Duan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present BioMatrix, the first multimodal foundation model that natively integrates sequences, structures, and natural language for both molecules and proteins within a single decoder-only architecture. Existing biological foundation models pursue native multimodality and broad entity coverage separately: those that fuse multiple modalities under a shared objective remain confined to a single entity type, while those spanning multiple entity types either omit explicit structural modeling or rely on adapter-based designs in which the model cannot natively generate the very modalities it can read. BioMatrix closes this gap by mapping molecular sequences (supporting both SMILES and SELFIES notations), molecular structures, protein sequences, protein structures, and natural language into a shared discrete token space through a unified tokenization scheme, so that all modalities are consumed and produced uniformly under a single next-token prediction objective -- without external encoders, projection adapters, or modality-specific output heads. Built upon the Qwen3 language model (1.7B and 4B), BioMatrix is continually pretrained on 304.4 billion tokens spanning general and domain-specific text, sequence and structure views of molecules and proteins, and cross-modal corpora that interleave biomolecular entities with scientific text and link distinct entities through molecule-protein and protein-protein interaction data. After tuning on a comprehensive suite of downstream applications covering 80 tasks across 6 categories -- encompassing single-entity and multi-entity understanding and generation tasks across and within modalities -- BioMatrix achieves state-of-the-art or competitive performance on 77 out of 80 tasks, demonstrating that a single, natively multimodal generalist model can effectively match or surpass specialized approaches across a wide range of biological tasks.

---


### 156. [SAGE: An Expert-Annotated South Asian GI Endoscopy Dataset for Multimodal Learning and Hallucination Analysis](https://arxiv.org/abs/2606.22144)

**<font color=#1a73e8>作者：</font>** Niyoj Oli, Sachin Acharya, Sandesh Pokhrel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gastrointestinal cancers represent a growing health burden in the South Asian region, driven largely by rapid changes in socio-economic conditions & lifestyle habits. However, early diagnosis of such malignancies remains a significant challenge, largely due to a lack of modern equipment, lack of financial support, and a scarcity of GI experts. AI-assisted diagnosis & report generation, show great promise in alleviating this problem by providing low-skill manpower the technical expertise to perform diagnosis. However, almost all open-source, publicly available datasets are predominantly collected from the European region, with no representation from the South Asian region. The lack of open-source GI datasets from diverse geographic regions has made it difficult to assess whether population bias is present in existing models, and to develop geographically inclusive AI tools for automated GI diagnosis. To address this gap, we introduce SAGE: An Expert-Annotated South Asian GI Endoscopy dataset for image captioning, multi-label classification, and visual question answering (VQA) tasks. It consists of 1,300 images, their captions along with hallucination tag, 18 labels and 14,726 question-answer pairs making it well-suited for diverse range of tasks including classification, benchmarking, and fine-tuning large multimodal models (LMMs). We further conducted benchmarking of multi-class classifiers on the effect of population shift in GI imaging AI tasks, and contemporary LMMs on their performance. Our study reveals that task-specific models, such as multi-class classification models, suffer the most, with an average performance drop of 58% when evaluated on the South Asian dataset. For contemporary LMMs, benchmarking reveals a substantial drop in the average GREEN score for anatomical landmark detection (0.308) and abnormality detection (0.410).

---


### 157. [Improving Reasoning in Vision-Language Models via Perception Verified Self-Training](https://arxiv.org/abs/2606.22158)

**<font color=#1a73e8>作者：</font>** Sourabh Sharma, Sonam Gupta, Sadbhawna Thakur  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving human-like reasoning in Vision-Language Models (VLMs) remains a long-standing challenge. Recent approaches leverage Chain-of-Thought (CoT) rationales generated by human annotators or proprietary models to improve reasoning, which is costly and difficult to scale. Self-training offers a promising alternative by using models own outputs as supervision. However, existing methods often suffer from visual hallucinations -- where rationales describe non-existent visual content, and language shortcuts -- where predictions rely on textual priors rather than true visual grounding, as rationales are typically filtered only by answer correctness without verifying visual perception. To address this limitation, we propose a perception-verified self-training framework that enforces visually grounded reasoning. First, our method employs a CoT template (caption-reasoning-conclusion) that disentangles perception from reasoning, enabling independent verification of visual understanding. To compensate for the absence of ground-truth captions, we propose PerceptEval, an unsupervised method that evaluates caption quality based on its alignment with visual and textual elements present in the image. Using caption verification together with answer correctness, we partition the data into three subsets: easy (correct caption and conclusion), medium (correct caption but incorrect conclusion), and hard (incorrect caption). Building on this partitioning, we design a two-stage curriculum learning strategy. In Stage 1, the model is trained on easy examples and subsequently in Stage 2, medium samples are incorporated through a caption-guided reasoning enhancement procedure that regenerates reasoning conditioned on verified captions. Only regenerated samples with the correct conclusions are retained.

---


### 158. [Beyond Time Series: Spatial Reasoning for Epidemic Forecasting via Multimodal Learning](https://arxiv.org/abs/2606.22171)

**<font color=#1a73e8>作者：</font>** Diana Guadalupe Gomez, Chenwei Wu, Zhiyi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epidemic forecasting models typically rely on surveillance data reported over administrative regions, treating them as atomic units, thereby obscuring sub-regional spatial structure that shapes disease dynamics. We introduce a spatially structured multimodal epidemic forecasting setting that integrates region-level temporal surveillance data with spatially localized auxiliary signals that are misaligned in resolution and structure, reflecting realistic public health reporting constraints. Building on this formulation, we propose M-SPICE (Multimodal SPatIal Context for Epidemic Forecasting), a structure-aware spatiotemporal forecasting framework that performs joint reasoning over temporal disease dynamics and spatial context via attention-based multimodal fusion, allowing spatial signals to selectively condition temporal representations across forecast horizons. We evaluate our approach on real-world COVID-19, influenza, and influenza-like illness (ILI) forecasting tasks under realistic real-time evaluation protocols. Across all forecasting settings, our method consistently outperforms state-of-the-art multivariate time-series, multimodal, and epidemiological forecasting baselines while maintaining strong probabilistic forecasting performance. Finally, interpretability analyses reveal when, where, and how spatial signals are leveraged, highlighting settings in which purely temporal, region-aggregated models are most likely to fail.

---


### 159. [The Score Granularity Gap in Black-Box LLM Classification: A Comparative Study of Confidence Constructions](https://arxiv.org/abs/2606.22179)

**<font color=#1a73e8>作者：</font>** Ao Sun, Tian Sun, Jiaxing Geng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as black-box classifiers in pipelines that automate confident decisions and route uncertain ones to human review. Such selective prediction needs a confidence score that an operator can threshold at a chosen risk level. Prior work asks whether LLM confidence is well calibrated or well ranked; we ask a complementary, deployment-oriented question that has been largely overlooked: at what resolution can the score be thresholded? We call the answer the score granularity gap. Through a controlled comparison of seven ways to build a confidence score, from a single verbalized number, to token probabilities, to querying the model many times and combining the answers, across 25 model-dataset pairs (9 LLMs, 3 benchmarks), we find that single-shot verbalized confidence, once correctly converted to a class probability, ranks cases surprisingly well, yet takes only a handful of distinct values. It therefore offers an operator only a few coarse thresholds, no matter how well it ranks. We show which constructions widen this gap, at what inference cost, and with what effect on ranking, notably that multi-query aggregation helps weak models but can degrade already-strong ones. We translate these trade-offs into concrete deployment guidance.

---


### 160. [Residue-Level Attributions in Protein Language Models Do Not Recover Allergen Epitopes](https://arxiv.org/abs/2606.22181)

**<font color=#1a73e8>作者：</font>** Jianzhou Yao, Anxiong Song, Katja Baerenfaller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep allergenicity classifiers are increasingly used in safety screening of novel foods, and recent protein language models have substantially improved protein-level allergenicity prediction. However, whether their explanations capture biologically meaningful information remains unclear. We introduce an epitope-grounded residue-level benchmark for quantitatively evaluating attribution faithfulness in protein allergenicity models. Across frozen ESM-2, multi-task ESM-2, and DeepPlantAllergy, protein-level classification was robust, yet classification-head explanation signals did not significantly exceed random in their residue-level alignment with annotated epitopes across AUROC, AUPRC, and Precision@k. Integrated Gradients identified residues that were functionally important to the model, but not overlapping annotated epitopes. Saturation mutagenesis further suggested classifiers may rely on physicochemical and compositional sequence features rather than epitope-specific mechanisms. Residue-level importance signals should therefore not be interpreted as immunological explanations for safety screening or hypoallergen design without quantitative validation. Code available: this https URL

---


### 161. [Bayesian Adaptation Gym: A Benchmark for the Bayesian Low-Rank Adaptation of Multi-Modal Language Models](https://arxiv.org/abs/2606.22188)

**<font color=#1a73e8>作者：</font>** Colin Samplawski, Ramneet Kaur, Manoj Acharya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large multi-modal language models are increasingly deployed in high-stakes domains, making well-calibrated uncertainty essential. Traditional Bayesian methods approximate posteriors over all model weights, which becomes intractable for modern large models. For this reason, recent work instead considers Bayesian low-rank adaptation to enable tractable posterior approximation. Due to a lack of a standardized benchmark to evaluate these approaches, it remains unclear where these methods provide meaningful benefits. To fill this gap, we introduce Bayesian Adaptation Gym (BAG), a benchmark for the Bayesian adaptation of multi-modal language models. BAG provides reference implementations of classic Bayesian baselines and state-of-the-art adaptation methods, along with a multi-modal dataset and task suite designed to probe calibration, robustness under distribution shift, and decision-making under uncertainty via active learning. Using BAG, we conduct and report extensive experiments across model sizes, datasets, and tasks to highlight the successes and failures of current Bayesian adaptation approaches. To enable further research, BAG is fully open source: this https URL.

---


### 162. [L20-Edu-135M: An Auditable Single-GPU Study of Data-Efficient Small Language Modeling](https://arxiv.org/abs/2606.22189)

**<font color=#1a73e8>作者：</font>** Yin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models are cheap to serve and feasible on local hardware, but strong public 135M-class systems are commonly trained with hundreds of billions to trillions of tokens on large clusters. We study a sharply resource-constrained regime: a complete 134.5M-parameter language-model pipeline executed on one NVIDIA L20 GPU. The released checkpoint, L20-Edu-135M, receives approximately 13B pretraining tokens: 10B FineWeb-Edu tokens followed by a 3B-token educational, mathematics, code, and reasoning mixture. We document the architecture, data gates, cross-source MinHash/LSH near-deduplication, segment deduplication, benchmark-overlap removal, throughput optimization, supervised fine-tuning (SFT) with weight interpolation, and reinforcement learning from verifiable rewards (RLVR) on GSM8K. In a self-run zero-shot six-task harness, L20-Edu-135M obtains a mean score of 0.4150. It trails SmolLM-135M (0.4767) and SmolLM2-135M (0.4917), but its mean is 87.1% of SmolLM-135M's while its nominal token count is 2.17% as large. This ratio is descriptive, not evidence of statistical equivalence or a controlled scaling law. The model exceeds several older 100M-160M public baselines under the same harness. Direct GRPO-style RLVR decreases GSM8K exact-match accuracy from 1.82% to 1.59% (192-token completions) and 1.21% (320-token completions). These single-run results identify a concrete failure mode rather than establishing a general lower bound on RLVR. The contribution is an auditable resource-constrained case study, not a state-of-the-art claim.

---


### 163. [When Is Emergent Consensus Real? A Measured Coupling Gain and a Validity Diagnostic for LLM Agent Societies](https://arxiv.org/abs/2606.22203)

**<font color=#1a73e8>作者：</font>** Dongxu Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM "agent societies" are studied via demonstrations of emergent consensus or polarization -- with no measurable control parameter, no theory of when each regime appears, and no test of whether an outcome is a genuine social dynamic or a model artifact. We introduce the coupling gain gamma, measured per-agent by counterfactually perturbing a neighbour's stated opinion. (i) gamma is stable and model-distinguishing -- across five frontier models it spans 0.15-0.43 (n=20, 95% CIs <= 0.025), paraphrase-invariant; social-neighbour gamma roughly equals numeric-anchor gamma, so gamma is evidence-coupling, not uniquely social. (ii) Classical dynamics with measured (not assumed) coefficients organise the regime: Friedkin-Johnsen for consensus/pluralism, signed-Laplacian/structural-balance for polarization. (iii) Frontier LLMs do not spontaneously backfire (beta <= 0), so default societies do not self-polarize -- polarization is always induced; the beta>0 branch arises only in the FJ surrogate, never in the agents. (iv) A randomized-initial-condition diagnostic -- the (slope, bias) of final vs. initial opinion -- separates genuine averaging from model-prior artifacts (boundary-censoring ruled out by construction via interior-valued facts); applied to a published "emergent consensus" result (Chuang et al. 2023) it reveals a model-specific conflation: averaging on debatable claims, prior-artifact on settled facts. (v) Coupling is context-dependent: pairwise gamma does not predict multi-neighbour outcomes -- it can order them backwards -- whereas a modality-matched group coupling does (sixteen closed+open models, Pearson r=-0.70, permutation p=0.008). The regime laws take this matched coupling, not the single-neighbour gamma: emergent consensus must be read from coupling in the target interaction. We contribute a measurement protocol and a validity instrument, not new theory.

---


### 164. [Open AI in the Wild: Adoption and Adaptation of Open Models on r/LocalLLaMA](https://arxiv.org/abs/2606.22211)

**<font color=#1a73e8>作者：</font>** Woohyeuk Lee, James Howison, Min Kyung Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing work on AI openness has focused on defining what technical components or release practices qualify a system as "open". However, less is known about how openness is understood and put into practice by people who adopt and adapt these models under real-world constraints. In this paper, we present an empirical study of r/LocalLLaMA, a large online community centered on running and customizing open foundation models locally. Through thematic analysis of community discussions, we find that members conceptualize openness pragmatically - in relation to reliability, local control, privacy, and the ability to adapt models under constraints such as compute resources, licensing, and usability. We identify key motivations for adopting open models, including autonomy, experimentation, and resistance to platform instability, as well as deterrents such as steep learning curves and performance gaps compared to closed systems. We further describe how shared resources and projects, including datasets, evaluation frameworks, and inference tools, sustain interdependent development in the broader open AI ecosystem beyond individual model releases. We then discuss the implications of a utility-oriented view of openness, and how producer support for downstream usability and infrastructure could better enable sustained innovation in open model ecosystems.

---


### 165. [On the Expressive Power of Weight Quantization in Large Language Models](https://arxiv.org/abs/2606.22249)

**<font color=#1a73e8>作者：</font>** Shao-Qun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, weight quantization that encodes the learnable parameters of large language models in an $n$-bit format has garnered significant attention due to its potential for model compression and inference acceleration. Many practical techniques have been developed; however, the theoretical understanding of many aspects, especially the approximation and degradation of expressive power as the number of quantization bits decreases, remains unclear. In this paper, we provide a theoretical investigation into the expressive capability of large language models relative to the number of quantization bits. We argue that 1.58-bit is the limiting precision for weight quantization by establishing the universal approximation and expressive collapse properties of weight-quantized models with respect to the number of quantization bits. Additionally, we confirm that weight quantization leads to expressive degradation, in which the expressive capacity of weight-quantized models degrades polynomially as the number of quantization bits decreases. These theoretical findings provide a solid foundation for advancing weight quantization in the context of scaling laws and shed insights for future research in model compression and inference acceleration.

---


### 166. [Learning a Normal World Model for Few-Shot Boundary-Calibrated Abnormality Detection](https://arxiv.org/abs/2606.22261)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Weichao Liu, Weijie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abnormality detection in complex systems faces two practical barriers: abnormal labels are scarce, and binary labels do not quantify how far an event has departed from normal behavior. We study a normal-world modeling formulation for this setting. Instead of learning a large and incomplete space of abnormal classes, the model learns the normal world from abundant normal events and uses a few abnormal examples only to calibrate the boundary of normality. We instantiate this idea as a Hypergraph Entropic Normal-World Model. The model represents multivariate sensor windows as context-conditioned hypergraphs, where hyperedges capture high-order relations among groups of variables. It then defines abnormality by an entropy-aware normal-world energy that combines temporal prediction surprise, hypergraph consistency surprise, and latent normal-manifold departure. On the NASA C-MAPSS turbofan degradation benchmark, the proposed full energy achieves strong zero-shot and few-shot performance across all four subsets and reaches AUROC 0.9983 on FD004, the most complex setting with multiple operating conditions and fault modes. Beyond standard detection metrics, we introduce mechanistic validation tests to probe whether the energy encodes normal-world structure rather than a superficial input-output mapping. The learned energy accepts unseen healthy engines, increases along degradation trajectories, and sharply penalizes context-mismatched cross-variable coupling breaks. These results suggest that normal-world energy can serve as an anomaly score, a graded risk measure, and a testable representation of normal system behavior under severe abnormal-label scarcity.

---


### 167. [Evaluating Large Language Models for Hausa and Fongbe Machine Translation: Benchmarks, Failures, and Metric Reliability](https://arxiv.org/abs/2606.22269)

**<font color=#1a73e8>作者：</font>** Mahounan Pericles Adjovi, Roald Eiselen, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the translation quality of current large language models (LLMs) for English-to-Hausa and English-to-Fongbe - two typologically distinct West African languages from the Afroasiatic and Niger-Congo families respectively - and evaluate whether standard automatic metrics reliably reflect human judgment for these low-resource languages. We evaluate four models (GPT-4o Mini, Claude Sonnet 4, Gemini 2.5 Flash, and Qwen2.5-7B) at progressive scales (500 to 10,000 sentences) using automatic metrics (BLEU, chrF++, TER, COMET, BERTScore) validated against native-speaker judgment. Our results reveal three key findings. First, translation quality varies substantially by language: Hausa achieves acceptable quality (human scores 4.0-4.5/5) while Fongbe achieves poor quality (1.0-2.2/5), with a consistent 3x BLEU gap across all systems. Second, model rankings differ by language - Gemini leads for Fongbe while GPT-4o leads for Hausa by human evaluation - indicating that performance on one low-resource African language does not predict performance on another. Third, metric-human correlation varies dramatically: perfect rank correlation for Fongbe (rho=1.0) but weak correlation for Hausa (rho=0.5), where human evaluators preferred GPT-4o despite all automatic metrics ranking Claude first. We further show that neural metrics like BERTScore exhibit embedding collapse (within-language similarity >0.99) for both languages, limiting their ability to differentiate translation quality. Based on these findings, we recommend multi-metric evaluation for low-resource African languages, with particular caution when interpreting neural metrics. We establish that minimum sample sizes of n=2,500 sentences are required for stable system rankings, as smaller samples produced artifact findings that reversed at scale.

---


### 168. [Encoder-Decoder Manifold Alignment for Idempotent Generation](https://arxiv.org/abs/2606.22304)

**<font color=#1a73e8>作者：</font>** Dareen Alharthi, Abdul Waheed, Bhiksha Raj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, several learning paradigms have been introduced to enforce idempotency in generative models. The goal is to ensure that repeated application of a model leaves samples unchanged once they lie on the target data manifold. In practice, however, many of these approaches fail to achieve exact fixed points, leading to instability and drift under repeated application. In this work, we argue that a key reason for this failure is a geometric mismatch between the manifolds learned by the encoder and decoder. The encoder projects inputs onto one latent manifold, while the decoder implicitly learns to reconstruct data from a different manifold. This discrepancy prevents the model from learning truly idempotent mappings. To address this issue, we propose a new training framework that explicitly closes this gap by forcing the encoder and decoder to learn consistent representations of the same underlying data manifold. By aligning the geometry of these components, our method encourages stable projections. Empirically, we show that our approach achieves significantly lower idempotency error and consistently regenerates identical outputs under repeated application, compared to existing methods. We demonstrate the effectiveness of the proposed framework on both image generation and image editing tasks. Finally, we show that enforcing idempotency in this manner improves identity preservation and information stability, leading to more realistic and controllable generative editing models.

---


### 169. [Learning at the Right Pace: Adaptive Data Scheduling Improves LLM Reinforcement Learning](https://arxiv.org/abs/2606.22305)

**<font color=#1a73e8>作者：</font>** Zicheng Xu, Ruixuan Zhang, Yu-Neng Chuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve remarkable reasoning capabilities through reinforcement learning (RL) post-training. However, existing RL post-training commonly relies on uniform data sampling, which ignores the semantic structure of the training data and the changing capability of the training policy. To address these limitations, we propose Adaptive Data Scheduling (ADS), a dual-level data scheduling framework for pacing RL post-training that replaces uniform sampling with an adaptive distribution over semantic clusters and policy-boundary sample selection. At the cluster level, ADS organizes samples according to semantic patterns and maintains an adaptive inter-cluster distribution to solidify current training progress. At the sample level, ADS performs intra-cluster scheduling to continuously sample policy-boundary samples, which provides informative relative advantages. Experimental results across three LLMs and seven reasoning benchmarks demonstrate that ADS improves average accuracy by 5.2% over Group Relative Policy Optimization (GRPO). Notably, ADS consistently improves RL methods with different objective designs, highlighting its potential as a general data scheduling strategy for LLM RL post-training. The source code is available at: this https URL.

---


### 170. [Curriculum Reinforcement Learning Can Incentivize Reasoning Capacity in LLMs Beyond the Base Model](https://arxiv.org/abs/2606.22317)

**<font color=#1a73e8>作者：</font>** Pengxiang Cai, Tianchen Fang, Xiaohan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is widely viewed as a promising path toward continuously improving large language models. Recent works, however, suggest that mainstream RLVR often reallocates sampling probabilities among trajectories already present in the base model: it can improve sampling efficiency, reflected by higher pass@1 scores, but yields limited gains, and can even decrease pass@k scores when k is large, and therefore may fail to expand the base model's reasoning capacity boundary. In this paper, we present a boundary-aware Curriculum RL approach to move beyond the base model's reasoning capacity boundary. Our approach first uses pass@k sampling to locate the current reasoning capacity boundary, then applies targeted teacher guidance to examples near or beyond that boundary, and finally uses RL to consolidate the newly introduced reasoning patterns. Across Qwen, Llama, and DeepSeek base models, boundary-aware Curriculum RL improves both pass@1 scores and pass@256 scores, with pass@1 reflecting one-attempt performance and pass@256 serving as an empirical proxy for the reasoning capacity boundary. In our experiments, average pass@256 improves by 9.8 percentage points over the base models and by 10.3 percentage points over Vanilla RLVR. These results suggest that boundary-aware Curriculum RL can provide a scalable route for LLMs to continuously improve beyond the base model's empirical reasoning capacity boundary.

---


### 171. [Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice](https://arxiv.org/abs/2606.22327)

**<font color=#1a73e8>作者：</font>** Li Kong, Qi Qi, Yinyu Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The explosive demand for interactive Large Language Model serving has highlighted the management of the Key-Value cache's dynamic memory footprint as a critical area for performance optimization in inference engines. Modern inference systems overwhelmingly rely on time-centric scheduling heuristics, such as Shortest Job First. However, their theoretical optimality is rooted in traditional schedule modeling, failing to capture the highly dynamic, 2D spatio-temporal geometric growth specific to LLM inference mechanisms. To resolve this, we propose the geometry-aware online scheduling by introducing the Smallest Volume First (SVF) algorithm and its highly efficient variant, 1-bit SVF. Theoretically, we provide a rigorous mathematical foundation for our approach. Utilizing a novel proof methodology, we tighten the worst-case competitive ratio ($\text{CR} \le 48 \rightarrow \text{CR} \le 5$) for SVF with known output lengths. Building upon this core breakthrough, we complete a comprehensive theoretical taxonomy analyzing our algorithms across different traffic scenarios and information availability. Practically, we seamlessly integrate our approach as a plug-and-play layer in vLLM. Extensive evaluations on Llama-3.1 models demonstrate comprehensive performance gains: SVF delivers strong reductions in both average and tail latency, while 1-bit SVF, with merely a single bit information, achieves competitive throughput and latency. This work establishes a theoretically sound and empirically proven approach for resolving memory-constrained scheduling in modern LLM deployments. To facilitate future research, our code is available at this https URL.

---


### 172. [BabelJudge: Measuring LLM-as-a-Judge Reliability Across Languages and Agent Trajectories](https://arxiv.org/abs/2606.22329)

**<font color=#1a73e8>作者：</font>** Shreyas KC  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge has become the dominant approach to scalable evaluation in NLP pipelines, yet judges themselves carry systematic biases that raw accuracy hides: they favor responses placed in slot A (position bias), they prefer longer responses regardless of quality (verbosity bias), and their reliability degrades sharply in lower-resource languages. We introduce BabelJudge, an open-source benchmark and reliability audit framework that measures all four failure modes -- position bias, verbosity bias, order inconsistency, and cross-lingual degradation -- on any judge model, without requiring human preference labels. The key insight is gold-labelling by degradation: starting from a high-quality reference response and applying a controlled perturbation yields a pairwise item whose gold label is known by construction, eliminating annotation cost. We evaluate Qwen2.5-7B-Instruct-4bit across English, Hindi, Arabic, and Swahili and find that our composite bias-penalised reliability score drops from 0.714 in Hindi to 0.550 in Swahili, a gap that raw accuracy (0.835 vs. 0.660) understates. Swahili order consistency collapses to 0.480, meaning judge verdicts are near-random under slot-order swaps -- a failure mode invisible to accuracy alone. We further extend the framework to agentic evaluation via nine trajectory-level perturbations (argument corruption, tool swaps, hallucinated calls, missing steps) and three new metrics: tool accuracy, hallucination detection rate, and trajectory-length bias. BabelJudge is released as a Python package supporting 11 judge backends. Code: this https URL

---


### 173. [Hypothesis-Driven Skill Optimization for LLM Agents](https://arxiv.org/abs/2606.22330)

**<font color=#1a73e8>作者：</font>** Fangxin Shang, Yehui Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External skills can improve action-oriented LLM agents without changing model weights, but persistent skill updates are risky when they are distilled from sparse or noisy trajectories. A plausible reflection may encode a useful procedure, a spurious shortcut, or a rule that the target executor cannot reliably follow. We propose Hypothesis-Driven Skill Optimization (HDSO), a train-free framework in which both the skill curator and the agent executor are frozen inference endpoints. The curator observes executor traces, proposes a falsifiable hypothesis with an explicit validation plan, instantiates the hypothesis as a candidate skill package, validates the package through paired control/treatment executions, reviews behavior differences, and consolidates only supported candidates into an approved repository. The executor consumes approved skills through progressive disclosure, preserving the executor-only path when no skill is selected. On ALFWorld, HDSO improves executor-only baselines by +6.9 Avg. SR points for Qwen3-8B and +4.0 points for Qwen3.6-27B. Under 20% randomly flipped success/failure feedback during skill discovery and validation, HDSO preserves a +7.1-point gain for Qwen3-8B. Transfer and heterogeneous-pair diagnostics further show that validated repositories can be useful beyond the run that produced them, but cross-model curation succeeds only when curator diagnosis, executor capability, and validation evidence align. HDSO provides an auditable skill lifecycle for frozen action agents rather than an unconstrained memory accumulation procedure.

---


### 174. [Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior](https://arxiv.org/abs/2606.22349)

**<font color=#1a73e8>作者：</font>** Gevindu Ganganath, Pasindu Bolonghege, Qianru Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) provide a new opportunity to study how language shapes exploratory cognition because conversational strategies can be systematically manipulated at inference time. We introduce CURIOBOT, a framework that operationalizes Berlyne's collative variables, novelty, complexity, conflict, and uncertainty, as adaptive linguistic interventions for conversational tutoring. Across 270 tutoring conversations spanning multiple model families, domains, and topic complexity levels, curiosity-oriented interventions consistently increased exploratory learner behaviors, producing up to 2.4x more conversational turns under fixed time budgets. To measure these effects, we further introduce a learner-centered evaluation framework capturing exploratory questioning, conversational agency, productive struggle, and observable curiosity. Learner-side gains persisted even when tutor-side instructional quality remained unchanged, suggesting that curiosity functions as a partially independent interaction-level mechanism. More broadly, our results demonstrate that LLM-mediated dialogue can serve as a scalable experimental framework for studying how language shapes exploratory learning behavior.

---


### 175. [On the Sparsity-Storage-Accuracy Tradeoff in Parsimoniously Activated Dictionary Learning](https://arxiv.org/abs/2606.22352)

**<font color=#1a73e8>作者：</font>** Zihui Zhao, Yuanbo Tang, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dictionary learning has long been studied from both optimization and probabilistic perspectives. While formulations with element-wise sparsity regularization (e.g., L1-based sparse coding) admit well-established probabilistic interpretations, many structured variants that impose global constraints lack a clear and tractable generative view. In this paper, we revisit a class of practically effective yet theoretically under-explored dictionary learning methods that impose a simple global regularization on the number of activated dictionary atoms, which we term parsimoniously activated dictionary learning (PADL). We show that PADL admits an equivalent formulation as maximum a posteriori estimation under a structured generative model, with auxiliary latent variables that govern global activation patterns. This formulation allows us to derive generalization guarantees that are difficult to obtain under the original formulation. More importantly, it yields an analytical characterization of the tradeoff between sparsity, storage cost, and reconstruction accuracy, enabling data-driven estimation of optimal hyperparameters. Based on this connection, we develop an efficient and interpretable PADL algorithm that eliminates manual hyperparameter tuning, achieving improved reconstruction performance under comparable sparsity levels on visual benchmarks. We further demonstrate its practical utility in accelerating inference for vision-language models.

---


### 176. [First-Token Broadcasters: Mechanistic Origins of Language Identity and Distributed Robustness in Transformers](https://arxiv.org/abs/2606.22361)

**<font color=#1a73e8>作者：</font>** Arjun Pillai, Christian Hoang, Anjelo Jann Laroza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Why do multilingual language models sometimes generate in the wrong language, and why is this so hard to fix? We introduce Language Identity Head Ablation (LIHA), a causal intervention that zeros each attention head individually and measures the resulting language switch rate across a parallel dataset of 2,700 prompt-language pairs spanning seven languages. Applied to GPT-2, LIHA identifies a small set of first-token broadcaster heads - led by L6H1 (switch rate 0.32, 3.23 $\sigma$ above the population mean) - that attend persistently to the first prompt token, propagating its language signal throughout generation. Compensatory redistribution when heads are ablated is statistically significant (p < $10^{-5}$) and follows a directional, hierarchical pattern: compensation always recruits heads in layers above the ablated head, suggesting a feedforward cascade rather than global diffusion. To probe how training regime shapes these circuits, we apply LIHA to a controlled pair - Qwen2.5-1.5B-Base and Qwen2.5-1.5B-Instruct - identical in architecture and size, differing only in training. The base model is nearly flat (max SR=0.016, 200/336 heads at SR=0.0); the instruct model concentrates causal influence sharply at layer 0, led by L0H5 (SR=0.224, 8.93 $\sigma$ above mean), with all other layers near zero. This controlled comparison provides direct causal evidence that instruction tuning reorganizes language identity circuits toward early-layer localization. Extended experiments with Chinese and Russian confirm that first-token broadcasting is script-specific in GPT-2, with non-Latin languages handled at layer 0 - the same locus as the instruction-tuned model. Code and data will be released upon publication.

---


### 177. [Reference-Free Assessment of Physical Consistency in World Model-based Video Generation](https://arxiv.org/abs/2606.22363)

**<font color=#1a73e8>作者：</font>** Yun Oh, Sukmin Yun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD), our approach utilizes DROID-SLAM and SEA-RAFT to quantify physical inconsistencies, motivated by WorldScore. Videos filtered using our relative consistency assessment show an improvement in task success rates of over 8%, effectively narrowing the simulation-to-reality gap. Furthermore, our absolute assessment enables spatio-temporal localization, providing visualization of when and where physical artifacts occur.

---


### 178. [Towards Error-Free Long Video Generation](https://arxiv.org/abs/2606.22370)

**<font color=#1a73e8>作者：</font>** Shuning Chang, Weihua Chen, Jiasheng Tang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have made minute-level synthesis possible; however, generating long videos remains challenging due to error accumulation, attribute drift, and the limited availability of long video data. In this paper, we introduce an infinite-length video generation framework that focusing on addressing these issues and produces high-quality, dynamic, and identity-consistent single-shot long videos. We first finetune a diffusion model as a video extension model on large-scale short video data to autoregressively generate temporally coherent clips. Inspired by the success of large language models (LLMs), we adopt causal attention computation between clips to further finetune this model on long video data. In this way, the tokens in one clip (short video) are computed by bidirectional attention while tokens among clips are computed by unidirectional attention. This design leverages the strengths of modern diffusion models while preserving long-term context information, effectively mitigating error accumulation and attribute drift. To achieve memory efficiency during inference, we adopt a key-value (KV) caching mechanism to maintain a constant KV memory. Furthermore, we introduce truncation-rectified flow (T-RFlow) technique to further suppress error accumulation. Experimental results demonstrate the effectiveness of our method. Our framework establishes a new benchmark for realistic and coherent minute-level video synthesis.

---


### 179. [ARIA: A Causal-Aware Framework for Rescuing LLM Reasoning in Trustworthy Materials Discovery](https://arxiv.org/abs/2606.22375)

**<font color=#1a73e8>作者：</font>** Yi Cao, Liaoyaqi Wang, Jieneng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models have revolutionized the process of materials discovery, yet they often fail to satisfy underlying physical causality. Through an analysis of Large Language Models (LLMs) augmented with knowledge graphs derived from current literature, we uncover a phenomenon termed contextual tunneling, where models "over-anchor" on narrow, retrieved evidence while suppressing global physical reasoning. To address this problem, we introduce ARIA, a causal-aware framework that conditions knowledge use on mechanistic completeness. ARIA routes each query through a three-tier cascade: (i) direct causal reasoning when complete evidence chains of Process-Structure-Property (PSP) are available, (ii) physics-informed analogical transfer for sparse or novel material systems, and (iii) explicit parametric fallback when external evidence is incomplete. As a proof of concept, we construct a Knowledge Graph (KG) containing 2,839 extracted PSP relations from peer-reviewed articles in the materials literature and evaluate ARIA on forward prediction and inverse design tasks for two-dimensional (2D) materials. ARIA mitigates contextual tunneling, improves over unaugmented and naive KG-augmented baselines, and provides further gains when an online literature search is used for evidence enrichment. Crucially, ARIA produces auditable causal traces, enabling physically grounded and trustworthy AI-assisted materials discovery.

---


### 180. [Structured Hyperedge Adaptation for Parameter-Efficient Fine-Tuning of Vision Transformers](https://arxiv.org/abs/2606.22383)

**<font color=#1a73e8>作者：</font>** Edwin Kwadwo Tenagyei, Lei Wang, Ugochukwu Ejike Akpudo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has become a practical solution for adapting large pretrained vision transformers (ViTs) to downstream tasks while updating only a small subset of parameters. However, existing adapter-based methods perform adaptation independently for each token, implicitly assuming that token refinements should be learned in isolation. This token-wise formulation overlooks the structured relationships among tokens that naturally arise in visual scenes, potentially leading to redundant updates and spatially inconsistent feature refinement. In this work, we revisit the design of parameter-efficient adapters and propose to perform adaptation in hyperedge space rather than token space. We introduce HyperAdapter, a hypergraph-based adapter architecture that enables structured, group-aware adaptation through soft token routing. HyperAdapter constructs a soft hypergraph over ViT tokens using prototype-based assignments, aggregates token features into latent hyperedge representations, applies lightweight bottleneck adaptation at the hyperedge level, and diffuses the resulting updates back to tokens via the hypergraph incidence structure. This design injects an explicit structural inductive bias into PEFT while preserving the modularity and efficiency of standard adapters. Extensive experiments across diverse visual benchmarks demonstrate that structured hyperedge adaptation consistently outperforms strong PEFT baselines under comparable parameter budgets, with particularly pronounced gains on tasks requiring structured reasoning. Our results suggest that the choice of adaptation space is a critical yet underexplored dimension in parameter-efficient transfer for ViTs.

---


### 181. [MetaPS: Adaptive Programmatic Strategy Selection for Market Agents](https://arxiv.org/abs/2606.22385)

**<font color=#1a73e8>作者：</font>** Jiaxiang Chen, Aotian Luo, Zhouyi Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> No single market strategy always wins: momentum, mean reversion, risk control,and event-driven rules can each succeed or fail as market conditions this http URL than asking large language models to directly generate market actions,we study an executable decision paradigm where an agent selects from a library of programmatic strategies, each implemented as a code module mapping market observations to this http URL propose \textbf{MetaPS}, a simulation-guided framework for adaptive programmatic strategy selection. MetaPS rolls out candidate strategies in simulated or backtested markets, identifies states where particular strategies lead to better future outcomes, and converts these state--strategy pairs into supervised fine-tuning data. During inference, the simulator is no longer queried: MetaPS observes only the current market state and candidate strategy context, selects a suitable strategy program, and the selected program produces the final action. Experiments on multi-stock trading and a controlled goods-exchange sandbox show that MetaPS consistently improves across model scales from 0.8B to 9B parameters. It outperforms fixed-strategy baselines, direct decision-making agents, and prompted API-based LLM agents; in several settings, compact fine-tuned models even surpass stronger API models. These results demonstrate that market simulations can provide scalable and targeted supervision for learning adaptive, interpretable, and executable strategy selection.

---


### 182. [PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems](https://arxiv.org/abs/2606.22388)

**<font color=#1a73e8>作者：</font>** Jiayu Liu, Qihan Lin, Cheng Qian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly operate in large tool ecosystems, where real-world tasks require discovering relevant tools, inferring implicit sub-goals, and adapting to dynamic environments over long horizons. However, existing benchmarks rarely evaluate planning under retrieval-limited tool visibility. To address this gap, we introduce PlanBench-XL, an interactive benchmark of 327 retail tasks over 1,665 tools that tests whether agents can iteratively retrieve usable tools, invoke them to uncover intermediate evidence for subsequent calls toward the final goal. PlanBench-XL further features an optional blocking mechanism that simulates real-world unpredictability through missing, failing, or distracting tool functions, forcing agents to detect disrupted paths and adapt at runtime. Experiments on ten leading LLMs show that massive-tool planning remains challenging: while GPT-5.4 achieves 51.90% accuracy in block-free settings, it collapses to 11.36% under the most severe blocking condition. Further analysis shows that agents are especially vulnerable when failures lack explicit error signals or when recovery requires longer alternative tool-use paths. These results establish PlanBench-XL as a testbed for diagnosing agentic planning failures and highlight the need for robust adaptive planning in long-horizon tasks with large, imperfect tool environments.

---


### 183. [Gold Points Sniper: Self-guided Visual Reasoning in VLM for Fine-grained Action Understanding](https://arxiv.org/abs/2606.22409)

**<font color=#1a73e8>作者：</font>** Haodi Liu, Xinhang Yang, Kunda Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots operating in everyday environments must understand fine-grained human actions, intentions, and contextual cues from broad views where people occupy only small regions, a capability unmet by current systems. While open-vocabulary action recognition methods remain limited to assigning predefined labels, and vision-language models (VLMs) face an inherent trade-off between informational richness and factual fidelity in their outputs, neither approach achieves the deep semantic interpretation required for reliable human-robot interaction. We propose Gold Points Sniper (GPS), a novel framework that empowers lightweight VLMs with self-guided multimodal reasoning capabilities for fine-grained human action understanding. Our approach comprises three key modules: Gold Points Extractor trains VLMs to identify critical action-relevant details, Selective Socratic Questioner validates and refines these details through selective self-questioning, and Semantic Entailment Evaluator quantitatively assesses factual consistency using semantic entailment classification. Extensive experiments on our curated instruction-tuning dataset based on the CAP benchmark demonstrate that GPS-enhanced lightweight VLMs achieve substantial performance improvements, with some models reaching performance comparable to proprietary GPT-4o while maintaining superior factual accuracy. Our work establishes a reliable foundation for fine-grained action understanding in domestic robotics, enabling robots to safely interpret human behavior through information-dense yet factually grounded descriptions. Source code, training configurations, annotation prompts, and dataset details are released at this https URL.

---


### 184. [Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering](https://arxiv.org/abs/2606.22419)

**<font color=#1a73e8>作者：</font>** Madhulatha Mandarapu, Sandeep Kunkunuru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A recent Nature Medicine study reports that general-purpose frontier LLMs outperform specialized retrieval-augmented clinical tools on medical benchmarks, and that retrieval can hurt strong models. We ask the natural follow-up: does structured knowledge-graph (KG) grounding change this, and when does grounding help at all? We contribute two results. First, a reproduction: the study's headline HealthBench score (~88) is the Consensus variant, not full HealthBench, where frontier models and ideal completions both score ~46-47 under a physician-calibrated grader (agreement 82.5%); we reproduce GPT-5.2 Consensus =90.9 and flag a score-deflating grader bug. Second, a knowledge-boundary result. Using a graph+vector engine (samyama-graph) over the public biomedical KG PrimeKG, neither naive triple retrieval nor an agentic natural-language-to-Cypher loop (82% successful queries) improves MedQA across a weak-to-strong model ladder (all |Delta| <= 3.4). On a synthetic counterfactual KG, and on a hybrid benchmark mixing known and novel facts, the identical pipeline lifts out-of-training accuracy from chance to ~100% (+68 to +79) while adding nothing on known facts (a no-LLM arm answers both). Across three regimes (no-knowledge, graph-aided, hybrid), grounding helps only insofar as the decisive fact lies outside the model's training -- public-KG facts are redundant, private and novel data are where it pays -- matching the study's institutional-data caveat.

---


### 185. [Enhancing LLMs for Graph Tasks via Graph-aware LoRA Generation](https://arxiv.org/abs/2606.22429)

**<font color=#1a73e8>作者：</font>** Junshu Sun, Wanxing Chang, Qingming Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) tightly couple their input-output parameters to dataset-specific feature spaces and target sets, exhibiting limited transferability across different datasets. In contrast, language models (LMs) generalize flexibly via a unified input-output interface, motivating recent attempts to adapt LMs to graph tasks. However, existing methods struggle to encode whole-graph information, leading to potential information loss and suboptimal graph understanding. In this work, we propose a novel weight-level information injection paradigm for adapting LMs to graph tasks. This paradigm injects whole-graph information by generating task-specific weight updates that interact directly with hidden representations. Instantiating this paradigm following low-rank adaptation (LoRA), we introduce GaRA, a Graph-aware LoRA generation model. GaRA constructs low-rank weight updates conditioned on the original graph structures and constrains the norm of the generated updates, thus injecting whole-graph information and avoiding the optimization bias in the weight generation. Empirical studies demonstrate that GaRA consistently outperforms baselines on zero-shot graph learning tasks.

---


### 186. [Words as Difference Makers: How Large Language Models Determine Causal Structure in Text](https://arxiv.org/abs/2606.22430)

**<font color=#1a73e8>作者：</font>** Wolfgang Pietsch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Because large language models (LLMs) are impressively successful in predicting text, it appears that they must have access to a 'world model' representing causal and definitional structure. However, the dominant formalisms of modern causal inference -- Judea Pearl's interventionist approach and the Neyman-Rubin potential outcomes framework -- struggle to illuminate how LLMs learn causal structure. I resolve this puzzle by arguing that LLMs employ a specific inductive approach based on a difference-making logic -- sometimes called variational induction. I demonstrate how central aspects of this logic are realized during training, where LLMs require enormous amounts of text data from a wide range of contexts to identify difference- and indifference-makers within word sequences. Furthermore, I analyze specific architectural features of LLMs -- such as token embeddings and self-attention -- to determine their roles in variational induction. The difference-making logic of LLMs fundamentally parallels the experimental method, where causal relations are derived by systematically varying individual circumstances to determine their influence on a phenomenon.

---


### 187. [MMGist: A Comprehensive Multimodal Benchmark for 2027](https://arxiv.org/abs/2606.22437)

**<font color=#1a73e8>作者：</font>** Wenzhen Yuan, Jiacheng Ruan, Wutao Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We conduct a systematic study of 18 widely used vision-language benchmarks and identify three major issues: 1) many items do not rely on visual cues and therefore fail to effectively measure multimodal understanding; 2) many items are already close to performance saturation for current LVLMs, which limits their discriminative power; 3) a small number of anomalous items affect the reliability of evaluation results. To this end, we propose MMGist, a curated benchmark that covers seven capability dimensions and contains 7,262 items. MMGist is constructed through a three-stage pipeline, which sequentially combines text-ablation filtering, cross-model saturation filtering, and anomaly detection filtering. We conduct extensive experiments on 27 leading LVLMs and compare MMGist with the raw pool of 23,250 items. The results show that MMGist preserves model rankings with high fidelity, with Spearman $\rho = 0.98$, while reducing evaluation items by 69\% and improving cross-model discrimination by 78\%. Further results indicate that Visual Logic remains a systematic weakness of current LVLMs, while knowledge-intensive dimensions such as Expert Knowledge dimensions remain important factors for distinguishing closed-source models from open-source models. These findings suggest that high-quality evaluation should prioritize visual dependency, discriminative power, and reliability, rather than simply pursuing benchmark scale.

---


### 188. [Efficient Multimodal Clinical Question Answering for Pulmonary Embolism Risk Assessment](https://arxiv.org/abs/2606.22442)

**<font color=#1a73e8>作者：</font>** Xiangyuan Xue, Yang Yu, Yan Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pulmonary embolism (PE) is a high risk cardiopulmonary condition whose management requires both timely diagnosis and reliable assessment of future clinical risk. Because PE care routinely combines computed tomography pulmonary angiography (CTPA), radiology interpretation, and longitudinal electronic health record (EHR) evidence, it provides a clinically meaningful setting for evaluating compact multimodal language models. In this work, we build a benchmark using efficient multimodal large language models (MLLMs) on INSPECT, a multimodal PE dataset containing 23,248 CTPA studies from 19,402 patients. We formulate eight diagnostic and prognostic tasks as structured clinical question answering problems and evaluate on typical efficient MLLMs under CTPA-Only, EHR-Only, and CTPA+EHR settings with zero-shot and few-shot prompting. Results show that Gemma4 E4B and Gemma4 E2B perform more strongly when EHR evidence is available, especially under CTPA+EHR input. Task level analysis further shows that PE diagnosis achieves higher performance than prognostic tasks, particularly readmission prediction. These observations suggest that compact multimodal models have the great potential in early stage PE risk detection and explanation.

---


### 189. [Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence](https://arxiv.org/abs/2606.22449)

**<font color=#1a73e8>作者：</font>** Yi Yu, Tetsunari Inamura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current embodied world models are primarily optimized for predictive objectives, limiting their ability to generalize under distribution shifts and reason systematically about unseen situations and hypothetical interventions. We argue that embodied intelligence should move beyond predictive world modeling toward self-evolving cognitive systems that continually construct and refine internal causal representations through interaction with the environment. To this end, we propose a self-evolving cognitive framework via causal world modeling for embodied scientific intelligence, which integrates three complementary components: causal world modeling, intervention-driven causal reasoning, and continual cognitive refinement. The proposed framework continuously revises and expands its internal causal world model through causal discovery, intervention-driven feedback, and counterfactual reasoning, supporting continual cognitive refinement and enabling cognition itself to evolve over time. Furthermore, we reinterpret embodied interaction not merely as a means of trajectory optimization, but as an epistemic process for causal hypothesis generation, intervention-driven experimentation, and continual knowledge acquisition. This work provides a conceptual and theoretical foundation for a transition from predictive intelligence toward epistemic intelligence, in which intelligence emerges through the continual construction, revision, and refinement of causal world models via interaction with the environment. Accordingly, an intervention-driven causal-epistemic benchmarking paradigm is suggested for evaluating self-evolving embodied scientific intelligence.

---


### 190. [CASPER in the Machine: Insights into Character Variety in LLM-Generated Stories](https://arxiv.org/abs/2606.22454)

**<font color=#1a73e8>作者：</font>** Anneliese Brei, Abhisheik Sharma, Nicholas Sanaie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM-generated text is increasingly used, especially in fictional domains, we explore how much LLM-generated stories differ from human-written stories. In this work, we focus on characters. We borrow definitions from narratology to analyze eight intricate dimensions of character, such as stylization and wholeness. These dimensions consider more than just basic characteristics. They assess how characters are portrayed within their stories. After automatically inferring categories of characters within both LLM and human-written stories, we compare and contrast these two sets of stories. We consider the following overarching questions: (1) Do LLMs and human-written stories have similar characters? and (2) Do LLMs generate stories with a variety of characters? Our analysis includes research questions that focus on stories generated by popular LLMs and recently published human-written stories. We describe a number of interesting similarities, differences and key takeaways.

---


### 191. [PRIME: Evaluating Prompt Resolution Under Incompatible Instructions in LLMs](https://arxiv.org/abs/2606.22470)

**<font color=#1a73e8>作者：</font>** Tehreem Javed, Shumaim Fatimah, Masooma Bakhtiari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often encounter conflicting prompts, although current instruction following benchmarks assess those meta-instructions in isolation, limiting the insights about how models process conflicting instructions. We introduce a framework \textit{PRIME}(\textit{Prompt Resolution under Incompatible Meta-Instructions Evaluation}) to analyze behavior of LLMs when provided with conflicting instructions. \textit{PRIME} purposefully produces calibrated conflicts across response length, output format, and reasoning; classifying model responses with a deterministic behavioral taxonomy. We are evaluating five instruction tuned open weight LLMs in two distinct settings, balanced and naturally distributed. The conclusion we reach upon analysis is that conflict type is more significant in affecting behavior than model scale, and various failure modes across different categories of conflict. Our findings emphasize the value of developing conflict awareness and suggest ability of LLM to follow instructions cannot be assessed through isolated constraints alone.

---


### 192. [Interleaved Speech Language Models Latently Work In Text](https://arxiv.org/abs/2606.22473)

**<font color=#1a73e8>作者：</font>** Talia Sternberg, Gallil Maimon, Yossi Adi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models (SLMs) have been extensively studied, with the common paradigm incorporating text data and pre-trained text LMs. A leading approach is speech-text interleaving in which models are trained over sequences containing both speech and text tokens, aiming to boost even speech-only capabilities. Yet the way these two modalities interact in the model latent space remains unclear. In this work, we analyze interleaved speech-text LMs from different model families and sizes through the scope of the logit lens to provide such insight. We reveal that these models go through an implicit transcription phase in which the text token of the spoken word becomes decodable in intermediate layers, despite not being trained for speech recognition. The transcription of the word appears as one of the top candidate words for as much as 77\% of the data. Following this stage, the models proceed to predict the next word in the text space before transforming back to the speech domain. We finally analyze the role of interleaving data, and initializing from text LMs in eliciting this behavior, as well as seeing how this correlates with spoken knowledge abilities. Our analysis sheds light on the internal mechanisms underlying the relationship between speech and text modalities and could shape SLM optimization.

---


### 193. [ROMEVA: Geometry-Preserving Vocabulary Expansion for Roman Urdu Language Models](https://arxiv.org/abs/2606.22478)

**<font color=#1a73e8>作者：</font>** Mahnoor Khan, Afsheen Asif, Milhan Afzal Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual Language Models like mBERT are widely used for low-resource NLP, yet their adaptation to morphologically inconsistent languages such as Roman Urdu remains underexplored. Roman Urdu spelling variation causes severe sub-word fragmentation, averaging 1.50 sub-words per token. We propose \textit{ROMEVA} (Roman Urdu Embedding-preserving Vocabulary Adaptation), which combines sub-word-average initialization and a PCA-guided anchor loss to stabilize embeddings during vocabulary expansion. Using a 36,130-comment Roman Urdu corpus, we add 500 highly fragmented tokens to mBERT and compare naive fine-tuning, sub-word-aware fine-tuning, and \textit{ROMEVA}. While \textit{ROMEVA} most effectively preserves the pretrained embedding space, naive fine-tuning achieves the strongest downstream sentiment classification performance. These findings reveal a disconnect between embedding stability and downstream performance, suggesting that stronger adaptation may be preferable to strict embedding preservation in morphologically inconsistent languages.

---


### 194. [Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains](https://arxiv.org/abs/2606.22484)

**<font color=#1a73e8>作者：</font>** Richard Kang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The adoption of agentic AI coding systems -- where autonomous agents generate, review, test, and deploy code with minimal human intervention -- creates a governance challenge in regulated industries. Existing frameworks address AI-assisted development maturity or the productivity-reliability tension but offer no mechanism for calibrating human oversight intensity to regulatory impact. We present the Governed AI-Assisted Engineering (GAIE) framework, a three-tier graduated human oversight model for agentic code generation in regulated domains. GAIE introduces the Oversight Classification Model (OCM), a deterministic decision function that classifies code generation tasks by regulatory impact, customer proximity, reversibility, and data sensitivity to route them through one of three oversight tiers: human-in-the-loop (strategic functions), human-over-the-loop (customer-impacting), or automated-with-monitoring (internal). Each tier defines required evidence artifacts for compliance auditability. We map GAIE against the Bank of Thailand's 2025 AI risk-management policy and demonstrate cross-jurisdiction applicability to MAS (Singapore), NIST AI RMF, ISO/IEC 42001, and the EU AI Act. Evaluation through regulatory coverage analysis, comparative framework analysis, and analytical productivity modeling suggests that graduated oversight preserves 84--97% of agentic coding velocity (central estimate: 91%) while maintaining compliance evidence coverage for regulated functions. GAIE contributes a framework that explicitly bridges AI-assisted development maturity with regulatory governance through proportionate human oversight.

---


### 195. [VADAOrchestra: Neurosymbolic Orchestration of Adaptive Reasoning Workflows](https://arxiv.org/abs/2606.22485)

**<font color=#1a73e8>作者：</font>** Teodoro Baldazzi, Luigi Bellomarini, Andrea Coletta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision-making in real-world settings rarely follows a fixed script. Instead, it unfolds as a dynamic reasoning process in which the appropriate course of action evolves as new context and data become available. Traditional Business Process Management systems provide rigor, determinism, and auditability, yet they generally struggle to adapt their execution at runtime. Conversely, agentic systems based on Large Language Models (LLMs) bring flexibility to decision-making, but they are inherently opaque, often unreliable, and suffer from significant scalability constraints when operating over large datasets. To combine these complementary paradigms, we introduce VADAOrchestra, a neurosymbolic framework that models complex workflows as evolving reasoning processes. The framework adopts a hybrid approach: given a user query and a collection of data sources, an LLM-based orchestrator incrementally plans and adapts the workflow. This is encoded as a logic program in a fragment of Datalog+/- where predicates correspond to tool invocations and rules represent both predefined domain dependencies and logic constructs synthesized on demand to manipulate intermediate results. All logical inference tasks are then executed by a state-of-the-art Datalog+/- symbolic engine. This approach provides a verifiable reasoning trace, supporting the auditability and reproducibility of the entire process. Furthermore, by decoupling high-level orchestration from symbolic inference, it addresses scalability concerns, enabling complex reasoning over large datasets through targeted data querying. We evaluate VADAOrchestra on real-world financial use cases, demonstrating faithfulness, scalability, and explainability compared to standard agentic architectures.

---


### 196. [Grounded Scaling: Why Agentic AI Needs Deterministic Environments](https://arxiv.org/abs/2606.22495)

**<font color=#1a73e8>作者：</font>** Liang Ding, Xintong Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-chain agent execution fails exponentially in environments designed for human tolerance: with per-step determinism $\delta < 1$, $k$-step chain success degrades as $\delta^k$. The AGI-to-ASI scaling debate (Genewein et al., 2026) has so far framed progress as a race between compute growth and a list of frictions (data wall, abstraction barrier, embodied bottleneck, multi-agent trust); we argue that environment determinism is a complementary binding axis cutting across all four, for the broad class of agentic AI tasks whose outcomes are verifiable economically, physically, or through multi-party settlement. Three formal results pin down the regime: a Determinism-Efficiency Bound on chain-task success, a Verifier-Goodharting Floor on flywheel ceilings under imperfect rewards, and a convergence condition for environment-side skill evolution. We operationalise the framework as a Supply Certainty Index (SCI) over five measurable properties, a five-level Determinism Maturity Model (DMM) as adoption ladder, and a falsifiable open-question programme (OQ1-OQ5) with explicit null results that would force retraction. The position is platform-agnostic. We engage three competing positions: sim-to-real sufficiency, alignment sufficiency, and AI-as-normal-technology.

---


### 197. [Benchmarking Vision-Language Models for Microscopic Plant Image Understanding](https://arxiv.org/abs/2606.22497)

**<font color=#1a73e8>作者：</font>** Tianqi Wei, Xin Yu, Zhi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microscopic imaging provides essential visual evidence for studying plant biology and pathology at the cellular and subcellular levels. However, existing benchmarks on vision-language models primarily focus on macroscopic plant imagery, while the microscopic domain remains underexplored. To address this gap, we present PlantMicro, a comprehensive benchmark for evaluating vision-language models (VLMs) in microscopic plant imagery. PlantMicro integrates more than 5,000 images collected across diverse hosts, biological domains, and imaging modalities. Building on this diversity, we design a set of complementary tasks that capture different facets of microscopic image understanding. To support these tasks, we construct over 9,000 VQA pairs that systematically evaluate the capabilities of VLMs. Experiments on PlantMicro show that current VLMs struggle with fine-grained recognition and biologically grounded reasoning. For example, GPT-5 achieves 34.93% accuracy on the pathogen classification task, which is only modestly above the random-guessing baseline. The results highlight a significant gap in current VLMs' ability to comprehend plant microscopic images. PlantMicro provides a standardized foundation for advancing VLMs toward reliable and comprehensive microscopy-level plant understanding.

---


### 198. [Breaking the Likelihood Trap: Variance-Calibrated Modulation for Large Language Model Decoding](https://arxiv.org/abs/2606.22511)

**<font color=#1a73e8>作者：</font>** Yuanhao Ding, Meimingwei Li, Esteban Garces Arias 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In open-ended generation, LLMs frequently fall into the "likelihood trap", marked by repetitive degeneration and vocabulary dullness, creating a discrepancy between machine-generated and human-written text. While post-hoc tail truncation (e.g., Top-$p$, Min-$p$) avoids sampling from the unreliable tail, it can over-sample from the uncalibrated head and misalign generation with human lexical preferences; fixed scalar repetition penalties likewise ignore variation in logit scale across inference steps, potentially disrupting semantic coherence. To address both limitations, we propose Variance-Calibrated Modulation (VCM), a training-free pre-decoding intervention that reshapes the probability distribution before truncation through two dynamic mechanisms: (1) Contextual Searchlight via PMI, which suppresses global stopwords while elevating context-evoked tokens, and (2) Adaptive Self-Debiasing, which uses real-time logit standard deviation for scale-invariant penalization. Across open-ended generation, factual QA, and mathematical reasoning, VCM consistently mitigates the likelihood trap. With negligible computational overhead, VCM integrates with existing decoding strategies, improving diversity, coherence, and, particularly at higher decoding temperatures, reasoning accuracy.

---


### 199. [Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents](https://arxiv.org/abs/2606.22528)

**<font color=#1a73e8>作者：</font>** Shiyang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents increasingly rely on context compaction, summarization, or eviction to keep long-running sessions within a token budget. We show that this context-management layer is a safety-critical failure surface: in-context governance constraints that agents reliably obey while visible can be silently removed by compaction, causing the same agent to perform prohibited tool actions later in the session. We call this failure mode Governance Decay. We introduce ConstraintRot, a benchmark of long-horizon agent scenarios with deterministic tool-call grading, and measure compaction-induced violations across seven model families. Across 1,323 episodes, violation rises from 0% with the policy in full context to 30% after compaction, reaching 59% for some models; when the constraint survives the summary, violation remains 0%, but when it is dropped, violation reaches 38%. We further study a Compaction-Eviction Attack, in which adversarial in-context content biases the summarizer to omit a legitimate policy, and show that optimized injections defeat every evaluated model. Finally, we propose Constraint Pinning, a simple training-free mitigation that quarantines governance constraints from lossy compaction and restores violation to 0% in our benchmark. These results identify context management as a first-class governance surface for deployed LLM agents.

---


### 200. [NegAS: Negative Label Guided Attention and Scoring for Out-of-Distribution Object Detection with Vision-Language Models](https://arxiv.org/abs/2606.22537)

**<font color=#1a73e8>作者：</font>** Yingjie Zhang, Shuai Li, Peng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-Distribution (OOD) detection is essential for ensuring the robustness and reliability of object detection systems deployed in safety-critical applications. While prior research has mainly focused on uni-modal detectors or vision-language model (VLM) based classifiers, the potential of VLM-based object detectors in OOD scenarios remains underexplored. In this work, we take the first step toward building OOD object detection methods upon VLMs. We identify two challenges specific to VLM detectors: (i) their text-guided attention enhances foreground with ID labels but treats background uniformly, leaving potential OOD regions unexploited for separating in-distribution (ID) from OOD instances; and (ii) their sigmoid-based multi-label outputs are incompatible with softmax-based OOD scores, calling for scoring functions consistent with VLM probabilistic outputs. Hence, we introduce Negative Label Guided Attention and Scoring (NegAS). To address (i), we propose a negative label guided attention module (NegA), where LLM-generated, visually-similar but semantically-different negative labels are used to guide attention toward potential OOD background regions. To address (ii), we introduce a novel sigmoid-based OOD scoring function (NegS) that leverages both ID and negative labels, producing strong responses for ID instances and suppressed responses for OOD ones. Extensive experiments demonstrate that our approach improves OOD detection performance by a large margin while maintaining ID accuracy, e.g., reducing the FPR95 by 11.4% on the COCO dataset and 25.5% on the OpenImages dataset compared to the baseline model. While initially designed for dense VLM detectors like YOLO-World, we successfully adapt NegAS to Grounding DINO, a query-based VLM transformer and achieve significant improvements, demonstrating the generalizability of our framework.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
