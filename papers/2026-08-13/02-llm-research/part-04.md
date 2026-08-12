# 🧠 大模型相关研究 | 2026年08月13日

> 本类共 **184** 篇论文：已确认 **177** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-184**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-184**

---

### 151. [ReLTEx: Reliable LLM-based Taxonomy Expansion](https://arxiv.org/abs/2608.10970)

**<font color=#1a73e8>作者：</font>** Zeinab Ghamlouch, Mehwish Alam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in generating semantically relevant concepts and relations, making them promising tools for taxonomy enrichment. However, directly relying on LLM-generated expansions often leads to noisy, redundant, or hierarchically inconsistent structures, limiting their reliability for automated taxonomy expansion. In this paper, we present ReLTEx, a framework for reliable LLM-based taxonomy expansion. ReLTEx combines LLM-driven candidate generation with structure-aware validation and recursive expansion control to improve the consistency and quality of generated taxonomies by reducing hallucinations. We evaluate the proposed framework using benchmark taxonomies under a masked taxonomy expansion setting and compare multiple validation strategies. Experimental results, supported by both adapted evaluation metrics and human evaluation, demonstrate that ReLTEx produces more reliable and semantically coherent taxonomy expansions.

---


### 152. [MUSE: A Full-Text Cross-Domain Knowledge Base of Scientific Problems, Solutions, and Rationales](https://arxiv.org/abs/2608.10974)

**<font color=#1a73e8>作者：</font>** Tsofia Cohen, Tom Hope  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific papers contain fine-grained records of problem solving: authors mention technical obstacles and methods that were used to address them, often along with reasoning on why those methods were chosen. We introduce MUSE (Mining Underlying Scientific Explanations), a full-text, multi-domain resource of scientific Problem-Solution-Rationale (P-S-R) triplets. We curate 579 expert-annotated full-text paragraphs, with a rich annotation schema covering salient problem, solution, and rationale spans, solves and rationale_of links and conceptual coreference. A modular extraction pipeline scales this annotation to build a high-quality knowledge base of 37K source-grounded P-S-R triplets. We evaluate the extraction components and include a preliminary experiment training a rationale-supervised LLM for scientific problem solving. Interestingly, we find that rationale supervision improves performance on complex, multi-constraint problems but can harm performance on simpler ones.

---


### 153. [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](https://arxiv.org/abs/2608.10976)

**<font color=#1a73e8>作者：</font>** Foundation Model Team, XPeng Inc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models can connect scene understanding, semantic reasoning, and trajectory generation for autonomous driving. However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optimize as an action-facing representation. We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision. Logged trajectories provide action evidence, while scene context supplies causal semantics. The predicted XCoT sequence remains in context and conditions fixed trajectory queries through shared multimodal self-attention. Deterministic token-function routing applies the Reason FFN to XCoT tokens and the Control FFN to trajectory queries for flow-matching trajectory generation. We further introduce XCoT Policy Optimization (XCPO) as an optional refinement extension in the same executable token space. XCoT-VLA reduces longitudinal ADE from 1.645 to 1.323 on a general-distribution set and lateral FDE from 1.616 to 0.648 in lane-change scenarios. By representing driving-oriented reasoning with only 2-6 executable XCoT tokens, our method substantially reduces autoregressive reasoning overhead and remains within the real-time planning budget. These results demonstrate that driving-oriented reasoning can be compact, executable, and directly connected to trajectory generation.

---


### 154. [ThinkAfford: Affordance-Centric Reasoning for Fine-Grained 3D Grounding in Cluttered Scenes](https://arxiv.org/abs/2608.10981)

**<font color=#1a73e8>作者：</font>** Xinrui Lin, Sha Zhang, Shumin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Task-driven 3D affordance grounding aims to localize the functional region in a cluttered 3D scene that enables an action specified by a natural-language instruction. Existing methods either predict 3D masks directly or construct them by selecting and fusing intermediate 2D/3D regions. However, they remain vulnerable to two intertwined failure modes: the predicted or selected regions may miss the target interaction area or have unsuitable granularity, while language grounding may confuse visually similar alternatives under relational instructions. To this end, we introduce ThinkAfford, which decouples high-recall affordance proposal generation from instruction-grounded reasoning. Specifically, the Affordance Proposal Generation module first uses learnable affordance prompts and multi-level visual features to predict interaction-conditioned heatmaps, extracting a variable number of fine-grained proposals without parsed object or part names as segmentation prompts. Visual-Prompted Affordance Reasoning then reasons over labeled proposal overlays using the full instruction, returning identifiers in a structured "think-then-answer" response. Moreover, Group Relative Policy Optimization uses proposal-level rewards from lifted 3D overlap to align VPAR selection with final 3D grounding. On the SceneFun3D validation split, ThinkAfford achieves 10.69% AP50 and 25.46% AP25 under the official evaluator, outperforming comparable 3D open-vocabulary and vision-language-model-based 2D-to-3D baselines. Module-level diagnostics further show that APG attains 77.5% recall at 25% intersection-over-union, while GRPO-trained VPAR achieves 72.1% selection accuracy on APG-covered queries, compared with 63.4% under supervised fine-tuning.

---


### 155. [What Iterated Self-Feeding Probes of Language Models Measure, and a test that separates the construction from the model](https://arxiv.org/abs/2608.10986)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A growing class of methods probes a language model by feeding it its own output: self-consistency, iterated refinement, agentic loops. We ask what such a probe measures, in a construction chosen to make the question sharp: a ring of token cells resampled in place by the model's own windowed conditional p_r(x_i | x_{i+-r}). The substrate is Glauber dynamics on token sequences and is not new; what we change is the coupling. Advancing two rings that differ in one token under common random numbers makes undamaged copies diverge by exactly zero, so damage spreading becomes measurable where a maximal coupling gives mixing times instead. The answer is that it measures two different things at once, in readings that look alike. Some quantities are fixed by the construction: the damage light cone is kinematic, and the radius scaling of the token-space Lyapunov exponent lambda_ca(r) is model-invariant across 19 models and two scale ladders spanning 70x. Others genuinely track the model: lambda_ca crosses zero at a reproducible point in training, and the attractor share ranks models consistently however the lattice is built. Left undistinguished, the first kind is readily mistaken for the second -- we did so ourselves for four months, and report a phase transition we measured to three decimal places that belongs to the probe rather than to any language model. We give the test that separates them: hold the construction fixed and vary the model, or hold the model fixed and vary the construction, and see which readings move. We validate the instrument by reproduction first, recovering a Domany-Kinzel damage field bit-exactly against an independent prediction, and we report the estimator failures that this discipline caught -- four retracted verdicts, each on a quantity that looked like a measurement. The methodology ships as a package.

---


### 156. [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](https://arxiv.org/abs/2608.10996)

**<font color=#1a73e8>作者：</font>** Taojie Zhu, Yuan Xia, Tao Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has been especially effective in mathematics and coding, where answers can be checked automatically. Many open-ended medical questions lack comparably cheap outcome verifiers: responses may be partly correct, incomplete, or contain clinically consequential errors. Rubrics written or validated by physicians offer strong clinical grounding, but involving experts in every instance is costly. Model-generated rubrics make this supervision scalable. We introduce ConRub-Med to preserve useful distinctions as rubric feedback moves from construction to policy optimization. For each prompt, three heterogeneous language models propose atomic criteria independently; a separate model reviews them, retaining only criteria with semantic support from all three generators. Three-State scoring distinguishes correct coverage, missing information, and incorrect claims. Errors receive negative rather than zero credit. When every response in a complete Group Relative Policy Optimization (GRPO) group receives the same final reward, a pairwise judge provides sequence advantages only if both candidate orders agree, without changing the scalar rewards. Groups without ties use vanilla GRPO. In a blinded study matched by question, two medical experts rate panels from the full pipeline as more clinically relevant than panels produced by one generator. Across the evaluated open models, ConRub-Med ranks first on six of nine benchmarks and achieves the highest medical and generalization averages. Using the resulting rubric dataset of 5,166 prompts, it scores $38.98 \pm 1.04$ (mean $\pm$ SD) on HealthBench-Hard, compared with InfiMed-ORBIT's 33.60 with 8,000 samples and 37.30 with 28,000.

---


### 157. [Templated or fully Synthetic? Prompt construction as a confound in measuring LLM political stance beyond writing assistance](https://arxiv.org/abs/2608.11008)

**<font color=#1a73e8>作者：</font>** Ilias Chalkidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political stance detection in LLMs has long been dominated by closed-ended, multiple-choice political survey questions---originally designed for humans, and thus lacks the realism and nuance of human-AI interactions in the wild, while also being susceptible to sandbagging. The recent IssueBench framework substantially mitigates these limitations with templated prompts anchored in real-world chat logs. Given the rise in non-work-related use of GenAI assistants, we extend IssueBench beyond writing assistance to include two additional tasks, information seeking and opinion sharing. We argue that templated prompts still lack the nuance of real ones, especially for open-ended tasks, and remain recognisable as evaluation artefacts. We propose the use of fully synthetic (LLM-generated) prompts, produced under detailed instructions with real prompts as seeds. We assess the ecological validity of real, templated, and LLM-generated prompts in a small-scale study covering 3 highly contested policy issues and 3 recent geopolitical conflicts. Human and LLM annotators rank LLM-generated prompts as no less realistic than real ones and clearly more realistic than templated ones, and find that they carry their intended intent and stance more clearly; the LLMs separate templated prompts from the other two far more sharply than the humans do. In a case study, templated and LLM-generated prompts yield systematically different stance estimates for the same model, most visibly under neutral framings, where templated prompts overstate the model's leaning in the direction encoded by the topic-and-stance text (filler) slotted into their templates.

---


### 158. [Watching Synthetic Videos: Aligning Cross-modal Representations with Visual Synthesis for Zero-shot Video Captioning](https://arxiv.org/abs/2608.11013)

**<font color=#1a73e8>作者：</font>** Liangyu Fu, Junbo Wang, Yuke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-only training is a popular paradigm in zero-shot video captioning, where the video distribution is not available to the model during training, leading to a cross-modal gap between the training (text-only) and the inference (video-only). Previous works attempt to bridge the gap through simple linear transformations. However, the inherent gap between text and video makes cross-modal representation space alignment insufficient, resulting in inaccurate sentences. To address this issue, we propose a novel zero-shot video captioning framework (WSV) consisting of two training stages, which first generates corresponding synthetic video latent representations via a pretrained text-to-video generation model. To strengthen the fidelity of the latent representations, we propose a polisher capable of bridging the gap between real and synthetic video distributions. Subsequently, we design a prompter that conditions GPT-2 on the polished latent representations to generate the captions in the second training stage. During inference, an input video is encoded by a pretrained 3D Causal VAE and then fed directly into the prompter, which in turn guides GPT-2 to produce the final caption. Experimental results conducted on MSVD, MSR-VTT, and VATEX datasets demonstrate that our proposed method achieves scores of 52 and 95.7 on the B@4 and CIDEr metrics, respectively.

---


### 159. [When Visual Signals Mislead: A Mechanistic Study of Attribute Hallucination in Vision-Language Models](https://arxiv.org/abs/2608.11024)

**<font color=#1a73e8>作者：</font>** Yufei Zhang, Chenlu Zhan, Hongwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attribute hallucination---where vision-language models (VLMs) correctly identify an object but mischaracterize its properties---is prevalent yet mechanistically poorly understood. The dominant explanation, language-prior dominance, has motivated prior-suppression methods, but this explanation has not been directly tested at the attribute level. We present VISOR (Visual-Operational Remediation), a unified framework that couples null-image-based diagnosis with routed remediation. Its VSNR diagnostic decomposes each prediction into a visual logit signal and a language-prior signal. Across 10,791 negative-ground-truth samples from three VLM families and three attribute types, the visual signal strongly predicts false positives, whereas the language-prior signal is near chance. VISOR uses this diagnosis to separate two failure modes: low-margin but directionally correct visual signals in color/state attributes, and low-SNR or misaligned visual signals in material attributes. The same diagnosis routes each query to the appropriate operator: calibration for threshold-placement errors, abstention for training-free low-SNR handling, or targeted visual adaptation for material failures that prior suppression cannot correct. Across Qwen, InternVL, and LLaVA, VISOR reduces attribute false positives without relying on the prior-dominance assumption.

---


### 160. [Data Attribution of Emergent Misalignment with Persona Features](https://arxiv.org/abs/2608.11025)

**<font color=#1a73e8>作者：</font>** Clemens Vetter, David Kaczér, Lucie Flek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM) is the phenomenon where fine-tuning a language model on a narrow task leads to harmful behavior in unrelated domains. A leading mechanistic account attributes EM to persona features: latent directions acquired during pre-training that misaligned fine-tuning amplifies. We ask where these features come from: which pre-training documents activate them, and whether naturally occurring human-written text suffices to induce EM. Using Sparse Autoencoder (SAE) based model diffing across four open-weight models, we find that features related to jailbreak personas, sarcasm, deception, and manipulation are amplified by misalignment fine-tuning, while safety-relevant and assistant-identity features are suppressed. Steering individual features controls EM in both directions: it induces misalignment rates of up to 62% in aligned models -- exceeding the 35% reached by misalignment fine-tuning itself -- and re-aligns misaligned models to near-baseline misalignment rates. Attributing the causal features to a corpus of one million pre-training web documents retrieves semantically relevant narratives about villainous characters, domination, and harmful agency. However, fine-tuning on these human-written documents does not reliably induce EM, even after reformatting into assistant-style responses, whereas synthetic instruction-response pairs derived from the same content do -- and transfer across model families. Semantic relevance alone is therefore not sufficient: response structure or model-generated phrasing plays an important role in inducing EM.

---


### 161. [Mapping and Measuring the Behavioral Evolution of Large Language Models](https://arxiv.org/abs/2608.11027)

**<font color=#1a73e8>作者：</font>** Dong Qiao, Chris Ding, Jicong Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark leaderboards summarize how well a language model performs, but not how its behavior relates to that of other models or changes across generations. We characterize the output behavior of 32 models from six families using their responses to a shared bank of 10{,}000 prompts. After embedding each response, we construct three complementary sentence-level dissimilarities: an aligned mean per-prompt distance, which is a pseudometric on observed model responses; a PCA-compressed summary of prompt-wise disagreement; and an alignment-free Gromov--Wasserstein discrepancy between models' internal response geometries. We use these constructions to study static organization and temporal change on a release-date axis through behavioral maps, family-wise drift, hierarchical clustering, cross-family convergence, and response-cloud dispersion. Across the three constructions, model families form coherent clusters, with \texttt{gpt-2} as a global outlier; cross-family distances decrease over time; and several recent reasoning-oriented models have comparatively compact response clouds. A token-level cross-check based on per-prompt Maximum Mean Discrepancy closely agrees with the sentence-level mean distance (Spearman $\rho=0.98$) and recovers the same qualitative findings. We organize these comparisons through a measure-theoretic lens making their alignment and invariance assumptions explicit. We also establish an architecture-agnostic sufficient condition linking behavioral similarity to inference-prompt coverage, small excess population log-loss, and similar effective target distributions---a possible training-side account rather than an empirical explanation of the observed trends. Our pipeline is label-free, and re-encoding every response with three further encoders---down to one $73\times$ smaller---preserves the rank geometry, the outliers, and the sign of the time trend.

---


### 162. [Who Are You Explaining To? A Multi-Agent System for Audience-Aware XAI Narratives](https://arxiv.org/abs/2608.11033)

**<font color=#1a73e8>作者：</font>** Francesco Musicco, Danilo Danese, Giuseppe Fasano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation. In medical AI, the same local explanation must reach patients, clinicians, and data scientists through markedly different forms of communication, and naive verbalization through large language models (LLMs) is prone to weak grounding, conflation of attribution with causal language, and outputs that are persuasive without being faithful to the underlying model evidence. We introduce XstrAI, an audience-aware multi-agent framework that treats local explanations as fixed evidence and structures how it is communicated to each target reader. Each prediction case is encoded as an immutable structured representation, shared identically across audiences so the underlying evidence remains fixed. Generation is factored into three specialized LLM agents responsible for audience-aware planning, linguistic realization, and validation for grounding, attribution consistency, communicative risk, and audience appropriateness, with a bounded revision loop triggered on detected inconsistencies. We evaluate XstrAI on diabetes and stroke risk prediction against 11 baselines, ranging from direct verbalization to a re-implementation of a state-of-the-art narrator. The evaluation combines an intra-narrative regime measuring fidelity to SHAP evidence with an extra-narrative regime assessing audience appropriateness through reference corpora, multi-family LLM judges, and a survey with target readers. In both evaluations, XstrAI's narratives are consistently assigned to their intended audience by independent judges, and preferred over all baselines on Clinician and Patient audiences, with competitive performance on Data Scientist, where audience-conditioned single-prompt baselines lead.

---


### 163. [TEAMMix: Taxonomy Enrichment Augmentation and Minority-augmented Mixing Strategy for LLM-enhanced Weak-Supervised Hierarchical Text Classification](https://arxiv.org/abs/2608.11044)

**<font color=#1a73e8>作者：</font>** Jian Zhang, Zhuohao Yang, Songlin Lei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hierarchical Text Classification (HTC), as a critical text mining task, faces challenges such as complex label hierarchies and class imbalance. Existing methods based on large language models (LLMs) struggle to be efficiently applied to this task due to issues like lengthy prompts and loss of label structural information. To address these limitations, this paper proposes a weakly supervised HTC framework enhanced by LLM-based data augmentation. The framework first enriches the label hierarchy semantically through keyword generation and corpus mining, thereby enhancing the model's understanding of labels. Subsequently, it guides the LLM to generate pseudo-samples to mitigate the long-tail problem, and employs a Gaussian mixture model for confidence-based resampling to optimize the quality of generated data. Experimental results demonstrate that the proposed method effectively improves the reliability of LLM-generated pseudo-labels and significantly enhances classification performance on fine-grained and imbalanced datasets.

---


### 164. [ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization](https://arxiv.org/abs/2608.11045)

**<font color=#1a73e8>作者：</font>** He-Yen Hsieh, H. T. Kung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals.
Starting from a pretrained LLM, ReRound trains a conditional diffusion model to produce continuous reconstructions of low-bit weights for the LLM. These reconstructed weights act as a guidance signal to disambiguate the rounding direction of weights located close to interval midpoints.
To integrate this reconstruction-guided rounding with conventional RTN, ReRound introduces a tolerance metric measuring how far the quantized weight (not the final quantized integer) is away from the midpoint: quantized weights within a tolerance region around midpoints are quantized using diffusion-based reconstructions, whereas weights closer to quantization boundaries are quantized with RTN. By sweeping the tolerance parameter, ReRound generates multiple candidate quantized integer weight matrices and selects the de-quantized weight matrix candidate whose leading singular values most closely match those of the original full-precision weights. This selected candidate determines the tolerance parameter ReRound uses.
ReRound is particularly effective for smaller LLMs. Across a range of such models, it consistently outperforms standard RTN for 3-bit and 4-bit weight quantization. ReRound achieves superior accuracy compared to an extensive set of calibration-free methods, remains competitive with calibration-dependent approaches, and operates entirely offline, introducing no additional overhead during low-bit inference.
The ReRound strategy represents a new approach for low-bit quantization. The method applies to AI models beyond LLMs. This paper focuses on its applications to small LLMs.

---


### 165. [V-FiLLM: Verified Financial LLM Reasoning Benchmark](https://arxiv.org/abs/2608.11047)

**<font color=#1a73e8>作者：</font>** Alicia Larsen, Victoire Laurent, Aulia Kharis Rakhamsari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While existing benchmarks have made substantial progress in evaluating LLMs across STEM domains, financial reasoning over structured data remains comparatively less explored. We introduce V-FiLLM, a framework that generates financial reasoning benchmarks from executable computation trees grounded in real tables, yielding items whose answers are correct by construction. Trees are evaluated symbolically to obtain ground truth and rendered into natural-language questions, removing any model from the labeling loop, so items can be generated at arbitrary scale without annotation cost and without inheriting a generator's error rate. V-FiLLM exposes four independently controllable axes of difficulty including computation depth, expression breadth, financial concept complexity, and context size. By evaluating on open-source models, we find that accuracy falls up to 51% as reasoning depth increases, and up to 47% points under adversarial numerical perturbations, highlighting remaining challenges in robust financial reasoning over tables. We further show that lightweight LoRA fine-tuning on verified chain-of-thought traces improves accuracy from 81.1% to 85.6% on held-out problems and outperforms the base model by 5% points on FinQA (Chen et al., 2022a), s), suggesting that targeted, low-cost adaptation is a promising direction for compositional reasoning in financial QA.

---


### 166. [CapProbe: Evaluating Detailed Image Captions via Full-Scene Dense Question Answering](https://arxiv.org/abs/2608.11074)

**<font color=#1a73e8>作者：</font>** Mouxiao Huang, Qiangyu Yan, Borui Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating detailed image captions from Vision-Language Models (VLMs) requires going beyond surface-level semantic similarity. Reference-based metrics (e.g., CIDEr and SPICE) and LLM-as-scorer protocols struggle to verify dense factual claims, while existing QA-based alternatives generally offer lower probe density, narrower domain coverage, or no explicit alignment between individual questions and segmented image regions. We introduce CapProbe, a full-scene dense QA benchmark that turns detailed caption evaluation into region-aligned factual checking. Each image is decomposed into coarse semantic regions covering both foreground and background elements; for every retained region, we generate multiple-choice questions spanning 10 semantic categories, forming a dense checklist of probed visual facts. Guided by a two-tier taxonomy of 37 L1 domains and 219 L2 sub-domains, CapProbe comprises 346 images, 1,868 regions, and 25,650 questions, averaging 74 QA pairs per image. A language judge answers from the caption alone; an Uncertain option and Effective Accuracy provide a judge-dependent proxy for distinguishing unanswered probes from incorrectly resolved ones, while density-based metrics penalize verbose yet uninformative captions. The protocol is cost-effective: by converting unconstrained scalar scoring into structured MCQ reading, it reduces open-ended scoring bias while remaining judge-conditioned and yields relatively stable model rankings under a fixed reader. Experiments on 13 VLMs show large Coverage gaps across models, a clear competency-efficiency trade-off, and failure modes that sparse or overlap-based evaluation often misses. The benchmark data, annotations, and evaluation code will be released soon.

---


### 167. [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095)

**<font color=#1a73e8>作者：</font>** Kushal Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding READMEs like this http URL grow without bound in real repositories, stopping only when the repository retires or someone rewrites the file wholesale. We trace this to imperfect recall: appending an instruction is always cheap, but once an instruction's rationale is gone, deleting it without risking a correctness regression costs O(2^|D|) in a prompt of |D| instructions. We name the resulting divergence catastrophic remembering, the inverse of catastrophic forgetting around which continual learning is organized. First, we characterize this phenomenon across 247,694 instruction lifetimes in 1,867 repositories: agentic prompts grow without bound, more than tripling over their lifetime (+226%), gaining +4.9 net instructions every commit; further, the older an instruction gets, the less likely it is to be deleted (log-hazard -0.032/commit). Then, we show that prompt comments can halt the growth: inverting IFEval yields verifiable worlds whose optimal prompts are known, and there comments encoding latent reasoning remove 99.3% of excess instructions (+211.3% to +1.4%). Finally, applying the same inversion to WildIFEval, we show that prompt comments can improve real-world agentic instruction-following by up to 23.1%. If English is the new code, why don't we have comments yet?

---


### 168. [Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents](https://arxiv.org/abs/2608.11110)

**<font color=#1a73e8>作者：</font>** Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a tool-using agent is given the same task in a different language, does it still take the same steps? Multilingual evaluation rarely asks: it compares final answers and discards the actions. Yet those actions are the product: they fix cost and latency, decide how the system fails, and are the only auditable part of its behaviour. We make the action policy the measured object across 8 models, 6 parallel benchmarks and 41 languages (2.38M rollouts). The naive measurement fails: five confounds sit between raw trace similarity and any defensible claim, each able to flip a conclusion. Short traces score higher, empty traces score perfectly, unrelated traces agree by chance over half the time, the gap is capped by each model's reproducibility, and a model asked the same question twice in one language answers differently, leaving no baseline. We remove all five, and every correction makes the effect larger. Divergence proves structural, not sampling noise: it survives greedy decoding in every cell and stays flat as temperature rises, even as models grow less self-consistent. Normalised by their own reproducibility, four very different frontier models converge under greedy decoding, each keeping 71-73% of its action policy across languages, with model identity explaining only 5.7% of the variance. Below roughly 10B parameters it breaks down, and the ordering among smaller models is largely an artifact of a chance floor we measure by permutation rather than assume. Agents route non-English tasks through English; this pivot is causally load-bearing, confirmed by a pre-registered prediction across four models, and models will not abandon it when told to. Finally, a single trace-extraction regex, not the model, manufactured a multilingual failure: two worked examples raise one model's measured accuracy twenty-sixfold while its accuracy on readable outputs barely moves.

---


### 169. [Attention-Path Fragility as an Uncertainty Signal in Large Language Models](https://arxiv.org/abs/2608.11138)

**<font color=#1a73e8>作者：</font>** Minsoo Kim, Sungyoung Ji, Kisung Moon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose that a model's uncertainty about a token is reflected not only in the breadth of its output distribution but also in whether a confident prediction is \emph{fragile} under perturbation of its attention pathways. We instantiate this as ASMI (Attention-Subnetwork Mutual Information), a training-free estimator that masks attention heads and measures the BALD mutual information among the resulting subnetworks, with a semantic-agreement kernel to discount surface-form disagreement. The signal is not a restatement of output confidence: on grounded QA an out-of-fold test shows it adds error-predictive information beyond single-pass confidence and entropy, concentrated in \emph{confident-but-fragile} predictions, where acting on it roughly halves the retained error of a confidence filter. The distinctness is regime-graded, so ASMI predicts its own domain of applicability, strong where answers are routed through provided context and bounded by design where they are recalled from parametric knowledge. Sem-ASMI reads the signal from a single greedy response, without the stochastic generations the strongest baselines require, and ties or beats Semantic Entropy on ten of the twelve grounded benchmark-backbone settings. Across the same twelve settings, the best ASMI variant, typically the adaptive one reusing the ten samples already drawn for the baselines, ties or leads the strongest baseline in eight, significantly in three under a paired test. On parametric QA all variants revert to or below the zero-cost MSP baseline, exactly as predicted, and the estimates are near-deterministic across reruns. A head-level analysis shows that what tracks this boundary is not the presence of head-level fragility but whether that fragility couples to errors.

---


### 170. [The Illusion of Cross-Lingual Safety in Low-Resource Languages](https://arxiv.org/abs/2608.11146)

**<font color=#1a73e8>作者：</font>** Abigail Oppong, P Sam Sahil, Tadesse Destaw Belay 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models (LLMs) is largely developed in English, assuming these safeguards generalize across multilingual settings. However, this assumption remains underexplored and exposes a vulnerability in low-resource languages. We investigate cross-lingual safety transfer in four African languages, Twi, Hausa, Amharic, and Swahili, using LoDNA, a new safety dataset that pairs literal translations with culturally localized prompts. To move beyond generation-based evaluation, we propose a latent geometric framework that probes hidden-state refusal representations in LLMs. Our experimental results show that cross-lingual safety transfer is severely limited; harmful prompts retain less than 10% of the English refusal signal across most language-model pairs. Literal and localized prompts are semantically aligned (cosine 0.95-0.996) but drift across layers, suggesting models encode the concepts without routing them to safety mechanisms. These findings demonstrate that current multilingual safety alignment is superficial, providing strong evidence against the assumption of a universal, language-agnostic harm manifold within the specific low-resource languages studied. Warning: This paper contains example data that may be offensive or harmful.

---


### 171. [PRMU: A Corpus-Free Benchmark for Person-Centric Knowledge Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2608.11149)

**<font color=#1a73e8>作者：</font>** Huafeng Chen, Yueming Lyu, Ziyuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in storing and recalling rich person-related knowledge, raising increasing concerns about reliable knowledge removal. However, existing machine unlearning approaches for MLLMs typically assume access to original forget and retain corpora, which are often unavailable in realistic deletion scenarios. To address this limitation, we introduce PRMU, a benchmark for evaluating corpus-free multimodal unlearning under realistic person-centric deletion requests. PRMU focuses on naturally acquired person-related knowledge and evaluates whether models can remove target knowledge while preserving related knowledge through diverse textual and visual probes, including adversarial evaluation and fine-grained locality analysis. To facilitate research in this setting, we further introduce Similarity-Gated Projection Editing (SGPE), a lightweight corpus-free unlearning baseline with knowledge displacement, protected parameter-space editing, and locality-aware multimodal control. Extensive experiments on representative MLLMs reveal that existing unlearning methods often suffer from unfavorable forgetting-locality trade-offs, with significant locality degradation under aggressive forgetting settings, and remain vulnerable to multimodal knowledge reactivation. Meanwhile, SGPE provides a competitive trade-off between target forgetting, locality preservation, and general multimodal utility. We hope PRMU can facilitate future research toward realistic and scalable multimodal machine unlearning. Code and dataset will be released at this https URL.

---


### 172. [CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting](https://arxiv.org/abs/2608.11150)

**<font color=#1a73e8>作者：</font>** Jiayu Ding, Meilu Song, Yun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has advanced open vocabulary scene understanding, existing methods remain confined to explicit queries. They struggle to interpret implicit intents, complex spatial constraints, and commonsense reasoning required for practical embodied interactions. To address this gap, we introduce the task of reasoning 3D Gaussian segmentation and construct two benchmarks, Causal-LERF and Causal-ScanNet. These benchmarks systematically evaluate commonsense, spatial, affordance, and counterfactual reasoning. Evaluations reveal that current state of the art methods perform poorly on these reasoning challenges. Therefore, we propose CausalSplat, a framework that integrates vision-language models with 3D scene graphs to disentangle explicit structural perception from implicit logical inference. Extensive experiments demonstrate that CausalSplat achieves state of the art performance on our reasoning benchmarks while showing strong generalizability on standard referring and open vocabulary 3D segmentation tasks. Project Page: this https URL

---


### 173. [MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment](https://arxiv.org/abs/2608.11167)

**<font color=#1a73e8>作者：</font>** Changhao Xiang, Shangyu Xing, Zhen Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Multimodal Large Language Models (MLLMs) predominantly rely on image-text pairs for modality alignment pretraining, mapping global image representations to long textual descriptions. However, this image-level alignment suffers from referential ambiguity: models struggle to infer the correspondences between multiple visual objects and textual entities from the global representation, leading to data inefficiency and suboptimal semantic grounding. To address this, we propose MultiModal Code-Switching (MMCS), a novel pretraining paradigm that provides explicit object-level supervision. Inspired by the linguistic phenomenon of code-switching, MMCS interleaves vision and language by replacing textual entities with their corresponding visual objects, enforcing local vision-language grounding. We further develop a scalable data synthesis pipeline to generate a pretraining dataset of 773K samples with accurate object-entity correspondences. Experiments show that MMCS is highly data-efficient: with only 50K samples, it matches or surpasses models trained on 600K image-text pairs. Furthermore, MMCS consistently improves visual grounding and perception capabilities across varying model scales.

---


### 174. [Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation](https://arxiv.org/abs/2608.11191)

**<font color=#1a73e8>作者：</font>** Shiyu Xuan, Zechao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI Visual Grounding is a fundamental capability for GUI agents. Existing models typically freeze their parameters after deployment, limiting their ability to adapt to unseen interfaces. Although recent methods attempt to adapt models via test-time reinforcement learning, they cannot reflect upon failed exploration. To overcome this, we propose a Test-Time Self-Evolving framework that enables models to improve after deployment without human-annotated ground truth. It constructs a closed-loop of Exploration, Evaluation, Reflection, and Internalization. Specifically, the agent first explores unseen interfaces by predicting grounding coordinates for given instructions. To evaluate these explorations, we introduce an MLLM-based Reflector to assess the generated results and provide the corresponding reasoning reflections. To internalize reflection knowledge into the model weights, we propose Reflection-Guided On-Policy Self-Distillation, which translates high-level reasoning into dense token-level supervision via a conditioned self-teacher. Furthermore, we design a Contrastive Calibration method to prevent incorrect auto-regressive prefixes from corrupting the supervisory signals during failed explorations. Extensive experiments across six benchmarks demonstrate our framework's effectiveness, achieving an average accuracy improvement of 7.4% over the base model. To the best of our knowledge, this is the first work to successfully exploit on-policy self-distillation for test-time adaptation in GUI visual grounding. By filling the gap in post-deployment adaptation, our framework completes the self-evolving capability of GUI agents. The code will be released.

---


### 175. [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](https://arxiv.org/abs/2608.11197)

**<font color=#1a73e8>作者：</font>** Nikolai Bolik, Lennart Stöpler, Artur Andrzejak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shani et al. (2026) show that LLM representations broadly recover human category boundaries, while failing to reflect fine-grained typicality structure. Their analysis uses cosine similarity over dense model representations. We revisit their approach using overlap over active sparse autoencoder (SAE) latent sets as a more interpretable similarity measure. We first verify that this set-level measure is meaningful: SAE latent sets can recover union-like compositional structure in controlled toy models and induce semantically coherent neighborhoods in natural text. Extending the human-concepts analysis to SAE set similarities, we find that SAE activation sets do not recover human category boundaries or within-category typicality more faithfully than dense embeddings or residual-stream states, but instead track model-internal similarity structure. To probe this gap further, we study active latent sets under well-controlled semantic modifications, revealing a substantial mismatch between human judgements of conceptual change and change in the SAE active set. We interpret this as evidence that, outside idealised settings, SAE features do not compose via simple bag-of-features semantics.

---


### 176. [ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls](https://arxiv.org/abs/2608.11200)

**<font color=#1a73e8>作者：</font>** Chen Lyu, Xingwei Tan, Simon Cullen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic dialogue generation offers a way to study conversational dynamics in sensitive domains where real data are difficult to access, release, or annotate. The underlying abuse may occur online or offline: threats and coercion can appear directly in messages, while behaviours such as surveillance, isolation, stalking, and physical violence may be planned, disclosed, or referred to conversationally. Privacy and legal constraints make it difficult the release of large-scale real conversation datasets; existing work has mostly focused on sentence-level toxicity of online abuses, leaving a gap in modelling abuse as a relational and temporally unfolding phenomenon. In this work, we focus on modelling Violence Against Women and Girls (VAWG) scenarios as multi-turn dialogues. We introduce ConVAWG, a retrieval-grounded framework for generating CPS-aligned synthetic VAWG chat dialogues. ConVAWG builds scenarios from persona seeds, demographic patterns reported by the UK Office for National Statistics, official crime definitions, and retrieved Domestic Homicide Review cases; converts them into hierarchical event timelines; generates multi-scene role-play dialogues; and applies targeted activation-steered toxicity control to appropriate utterances. We release over 6,000 multi-turn dialogue events across 200 scenarios with rich scenario-, event-, and turn-level metadata. Extensive human evaluation, LLM-as-Judge assessment, ablations, and downstream tasks show strong dialogue quality and domain fidelity.

---


### 177. [VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics](https://arxiv.org/abs/2608.11201)

**<font color=#1a73e8>作者：</font>** Bowei Liu, Zheng Lu, Yuhan Bian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation models have significantly improved the realism of synthetic videos, blurring the boundary between generated and authentic content and raising concerns about misinformation. Existing MLLM-based detectors mainly rely on supervised fine-tuning or label-level reinforcement learning, where coarse supervision limits generalization to unseen scenarios and emerging video generators. To overcome these limitations, we are the first to introduce \textbf{meta-detection} into AI-generated video detection, enabling reliable forgery detection by jointly optimizing predicted labels and supporting evidence within reinforcement learning. This paradigm requires reliable evidence signals and effective mechanisms to integrate them into label-level optimization. Textual rationales provide semantic descriptions of forgery artifacts, but their generation and verification depend on external models, making supervision vulnerable to hallucinations and semantic biases. In contrast, temporal grounding provides more objective and verifiable evidence, as manipulated intervals can be precisely controlled during forgery construction. Based on this insight, we propose an automated data construction pipeline that generates paired real-fake videos by replacing temporal segments with boundary-frame-conditioned video generation models. Furthermore, we introduce \textbf{Evidence-Guided Reward Redistribution}, which performs evidence-aware credit assignment by redistributing rewards among label-correct responses according to evidence quality. This preserves reliable label supervision while encouraging detectors to acquire fine-grained and verifiable forgery localization capabilities. Extensive experiments demonstrate that \textbf{VidForensics-M1} effectively leverages verifiable temporal evidence to achieve robust and generalizable AI-generated video detection.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 178. [P3CA: Encoder-Agnostic Interpretation of Vision Foundation Model Embeddings via Spatial Probing](https://arxiv.org/abs/2608.10131)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Amoon Jamzad, Dilakshan Srikanthan, Faranak Akbarifar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models are increasingly used as reusable encoders in medical image computing, yet their high-dimensional spatial embeddings are difficult to inspect beyond downstream task performance or global dimensionality reduction. We propose position-prompted PCA (P3CA), an encoder-agnostic method for local probing of channel-rich spatial tensors. Given a user-selected spatial prompt, P3CA estimates the feature normalization and dominant covariance directions within that region, then applies the resulting projection to the full tensor to visualize where locally informative directions are expressed. This produces a region-conditioned representation lens without modifying the encoder, retraining, or requiring task-specific labels. We implement P3CA in EmbedVision, an interactive 3D Slicer-based workflow, and evaluate it across natural images, colorectal pathology foundation-model embeddings, and spatial transcriptomic tensors. Across these settings, prompted projections reveal local structure suppressed by global PCA, improve prompt-matched pathology discrimination from frozen three-dimensional projections, and support comparison between learned and measured spatial representations.

---


### 179. [Frozen Brain-MRI Foundation Models Are Site Fingerprints](https://arxiv.org/abs/2608.10295)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Saman Rahbar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen foundation-model (FM) embeddings are increasingly used as off-the-shelf brain-MRI representations, on the assumption that they capture anatomy. We audit what they actually encode and find that acquisition site is a large, intrinsic component of the representation. Across two independent cohorts (ABIDE-I, ABIDE-II), three frozen 3-D encoders (brain-pretrained, CT-pretrained, and randomly initialized), and every network depth, site is linearly decodable at roughly 0.9 balanced accuracy at deep layers, exceeding the decodability of every clinical or demographic variable (sex, age, autism diagnosis) at every layer. The effect is intrinsic rather than learned: a randomly initialized encoder is already a ~0.9 site classifier on both cohorts and across three architecture families (Swin, ViT, ResNet), and site is decodable at ~0.95 directly from the raw downsampled image with no encoder, so the fingerprint reflects low-level image statistics that any encoder preserves rather than a product of pretraining. Residualizing measured population covariates leaves site decodability essentially unchanged, indicating an acquisition- rather than population-driven effect. A nonlinear probe matches the linear one, so the fingerprint is fully linearly accessible. The site subspace is removable post hoc by iterative null-space projection or ComBat (site decodability 0.94 -> 0.07/0.00), and is a site-attribution concern for shared or federated embeddings; but for dense segmentation this removal is not free, because site and anatomy occupy an entangled linear subspace (a matched-rank random-direction projection is Dice-neutral, whereas removing the site subspace is destructive). We recommend site-audited use of frozen brain-MRI FMs and release an open audit toolkit.

---


### 180. [Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models](https://arxiv.org/abs/2608.10708)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seokhyun Youn, Dahyeon Kye, Sung-Ho Bae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision Foundation Models (VFMs) predict depth, camera pose, and pointmap in a single forward pass without per-scene optimization, achieving strong generalization. However, enforcing explicit multi-view geometric consistency, e.g., through bundle adjustment, is computationally costly and is thus not imposed during VFM pretraining, so such inconsistency can arise. To address this, implicit self-consistency derived from model outputs (e.g., pointmaps, features), though enforced at test-time in prior work, delivers inherently limited performance gain, especially on scenes where the pretrained VFM is highly inaccurate. In contrast to this implicit signal, we propose Self-Geometry, a plug-and-play test-time adaptation pipeline that directly imposes explicit multi-view geometric constraints using 2D pixel correspondences as pseudo ground-truth. Our proposed Self-Geometry consists of Geometric Disentanglement Optimization, which combines Multi-View Consistency and Epipolar Consistency losses with Gradient Disentanglement to prevent gradient conflict; Frame Angular-Neighbor, a view sampler based on SO(3) geodesic distances for lightly imposing these constraints; and Lightweight TTA, which adapts VFMs via LoRA. Our method achieves consistent improvements in both pose and geometry estimation across six VFMs (VGGT, $\pi^3$, DA3-Giant/Large/Base/Small) and four benchmarks (7Scenes, ETH3D, ScanNet++, HiRoom).

---


### 181. [Evaluating Semantic and Spatial Guidance for Foundation Model Segmentation of Small-Scale PV in Remote Sensing Imagery](https://arxiv.org/abs/2608.10801)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Roni Blushtein-Livnon, Tal Svoray, Osher Rafaeli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal PV data are essential for understanding adoption processes in off-grid regions, yet such data remain largely unavailable. Automated segmentation of remote sensing (RS) imagery offers a promising solution; yet, residential PV systems remain challenging targets because of their small size and sparse distribution, resulting in severe target-background imbalance. Vision-language foundation models (FMs) provide a data-efficient paradigm through prompt-based semantic and spatial guidance, but the relative contribution of different prompt types remains unclear. We systematically evaluate SAM3 for small-scale PV segmentation in RS imagery by comparing textual, geometric, and hybrid prompting, under varying supervision levels, training strategies, spatial resolutions, and imaging conditions. Multi-temporal aerial imagery from a large off-grid rural region serves as a study site, with findings validated across three additional datasets. Prompting strategy emerged as the dominant factor governing model behavior. Textual prompting consistently produced the lowest performance and showed the greatest sensitivity to supervision and imaging conditions. In contrast, spatial guidance substantially improved both segmentation accuracy and robustness. Hybrid prompting achieved the highest accuracy and stability, indicating that semantic and spatial guidance provide complementary information. Most performance gains were achieved with only a few hundred annotated samples, demonstrating strong data efficiency. Transfer learning had limited overall impact, with only modest improvements observed for textual prompting under limited supervision. Overall, our findings establish prompting strategy as a key determinant of SAM3 adaptation, robustness, and generalization, highlighting the potential of promptable FMs for scalable PV mapping in data-constrained off-grid regions.

---


### 182. [TACTICL: Task-Aware Compression of Tabular ICL Models](https://arxiv.org/abs/2608.10837)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mykhailo Koshil, Matthias Feurer, Katharina Eggensperger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The strong performance of foundation models for tabular tasks comes at substantial inference costs. Distilling models into task-specific architectures reduces model size and computational demands but also sacrifices in-context adaptability. Here we introduce TACTICL, an automated task-aware compression framework for tabular in-context learning models that jointly prunes transformer layers and replaces them with lightweight adapters trained on downstream tasks, thus blending in-context with in-weight learning. We study TACTICL on 47 benchmark datasets and show that we can substitute up to 85% of layers without substantial performance drop on a given downstream task. We further show that TACTICL maintains robustness to data shifts, leaving its in-context ability intact. Overall, TACTICL provides a robust framework for exploiting the depth-wise redundancy of tabular foundation models by combining task-specific adaptation and structured compression. We provide the code at: this https URL

---


### 183. [Foundation Model-Enabled Efficient Data Sampling (FEEDS): A label-efficient training strategy for pan-cancer, multi-tracer PET/CT datasets](https://arxiv.org/abs/2608.11076)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Biratal Raj Wagle, Bashirul Azam Biswas, Grant Chau 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated lesion segmentation in whole-body PET/CT imaging can assist clinicians with cancer detection, staging, and treatment planning across radiotracers and cancer types. However, training lesion segmentation models that capture variations in lesion size, distribution, and appearance requires large annotated datasets, whose creation is both time- and expertise-intensive. As a result, models trained on limited labeled PET/CT data often lack the accuracy and generalizability needed for clinical use. We present FEEDS (Foundation model-Enabled Efficient Data Sampling), a label- and compute-efficient learning strategy that uses vision foundation model embeddings to select the most informative and diverse unlabeled cases for expert annotation. Unlike unsupervised, semi-supervised, and active learning approaches, FEEDS is a one-step training paradigm requiring only a limited, representative training set, making it label- and compute-efficient. We train and validate FEEDS using the AutoPET-III dataset. We test its accuracy and generalizability on three held-out sets: AutoPET-III, DeepPSMA, and an internal Dartmouth-Hitchcock Medical Center dataset. We evaluate clinical utility at the voxel, lesion, and anatomic region level to assess performance in high-risk areas and treatment planning utility. FEEDS outperforms random-sampling-based labeling, pseudolabel-based semi-supervised learning, and training with limited labeled data alone. It generalizes across all three test sets, FDG and PSMA tracers, and multiple diseases, matching fully-labeled (100\%) training performance with 70\% less annotation burden. FEEDS addresses the challenge of label scarcity in an automatic lesion segmentation framework by providing a practical approach for constructing representative and diverse annotation queues from large, unannotated clinical repositories.

---


### 184. [Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives](https://arxiv.org/abs/2608.11093)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Songlin Du, Xiaoyong Lu, Zeyu Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-view feature matching aims to establish reliable correspondences across images with large viewpoint variations. Over the past decade, the field has evolved from task-specific models toward increasingly unified and generalizable correspondence models, with recent progress further driven by the emergence of vision foundation models (VFMs). Despite these advances, existing studies remain highly diverse in their problem formulations, model architectures, training paradigms, and evaluation protocols, making it difficult to obtain a unified understanding of the field. In this survey, we present a unified review of cross-view feature matching. We first introduce a structured taxonomy covering feature extraction, single-type feature matcher, multi-type feature matcher, VFMs based methods, training strategy and robust estimation, providing a coherent framework for analysis and comparison. We further examine recent advances, distilling key design principles and highlighting the shift toward unified and generalizable correspondence models. We also provide a unified experimental benchmarking of representative state-of-the-art methods under consistent protocols, enabling fair and comprehensive performance comparisons. In addition, we discuss open challenges and future directions, including efficiency, robustness under extreme conditions, and cross-domain generalization. This survey aims to provide a comprehensive and structured reference for understanding the evolution, current landscape, and future development of cross-view feature matching in the era of vision foundation models.

---


> [!TIP]
> 当前位于：**151-184**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-184**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
