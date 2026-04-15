# 🧠 大模型相关研究 | 2026年04月16日

> 本类共 **165** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

---

### 1. [Schema-Adaptive Tabular Representation Learning with LLMs for Generalizable Multimodal Clinical Reasoning](https://arxiv.org/abs/2604.11835)

**<font color=#1a73e8>作者：</font>** Hongxi Mao, Wei Zhou, Mengting Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning for tabular data remains constrained by poor schema generalization, a challenge rooted in the lack of semantic understanding of structured variables. This challenge is particularly acute in domains like clinical medicine, where electronic health record (EHR) schemas vary significantly. To solve this problem, we propose Schema-Adaptive Tabular Representation Learning, a novel method that leverages large language models (LLMs) to create transferable tabular embeddings. By transforming structured variables into semantic natural language statements and encoding them with a pretrained LLM, our approach enables zero-shot alignment across unseen schemas without manual feature engineering or retraining. We integrate our encoder into a multimodal framework for dementia diagnosis, combining tabular and MRI data. Experiments on NACC and ADNI datasets demonstrate state-of-the-art performance and successful zero-shot transfer to unseen schemas, significantly outperforming clinical baselines, including board-certified neurologists, in retrospective diagnostic tasks. These results validate our LLM-driven approach as a scalable, robust solution for heterogeneous real-world data, offering a pathway to extend LLM-based reasoning to structured domains.

---


### 2. [A Layer-wise Analysis of Supervised Fine-Tuning](https://arxiv.org/abs/2604.11838)

**<font color=#1a73e8>作者：</font>** Qinghua Zhao, Xueling Gong, Xinyu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While critical for alignment, Supervised Fine-Tuning (SFT) incurs the risk of catastrophic forgetting, yet the layer-wise emergence of instruction-following capabilities remains elusive. We investigate this mechanism via a comprehensive analysis utilizing information-theoretic, geometric, and optimization metrics across model scales (1B-32B). Our experiments reveal a distinct depth-dependent pattern: middle layers (20\%-80\%) are stable, whereas final layers exhibit high sensitivity. Leveraging this insight, we propose Mid-Block Efficient Tuning, which selectively updates these critical intermediate layers. Empirically, our method outperforms standard LoRA up to 10.2\% on GSM8K (OLMo2-7B) with reduced parameter overhead, demonstrating that effective alignment is architecturally localized rather than distributed. The code is publicly available at this https URL.

---


### 3. [When Reasoning Models Hurt Behavioral Simulation: A Solver-Sampler Mismatch in Multi-Agent LLM Negotiation](https://arxiv.org/abs/2604.11840)

**<font color=#1a73e8>作者：</font>** Sandro Andric  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as agents in social, economic, and policy simulations. A common assumption is that stronger reasoning should improve simulation fidelity. We argue that this assumption can fail when the objective is not to solve a strategic problem, but to sample plausible boundedly rational behavior. In such settings, reasoning-enhanced models can become better solvers and worse simulators: they can over-optimize for strategically dominant actions, collapse compromise-oriented terminal behavior, and sometimes exhibit a diversity-without-fidelity pattern in which local variation survives without outcome-level fidelity. We study this solver-sampler mismatch in three multi-agent negotiation environments adapted from earlier simulation work: an ambiguous fragmented-authority trading-limits scenario, an ambiguous unified-opposition trading-limits scenario, and a new-domain grid-curtailment case in emergency electricity management. We compare three reflection conditions, no reflection, bounded reflection, and native reasoning, across two primary model families and then extend the same protocol to direct OpenAI runs with GPT-4.1 and GPT-5.2. Across all three experiments, bounded reflection produces substantially more diverse and compromise-oriented trajectories than either no reflection or native reasoning. In the direct OpenAI extension, GPT-5.2 native ends in authority decisions in 45 of 45 runs across the three experiments, while GPT-5.2 bounded recovers compromise outcomes in every environment. The contribution is not a claim that reasoning is generally harmful. It is a methodological warning: model capability and simulation fidelity are different objectives, and behavioral simulation should qualify models as samplers, not only as solvers.

---


### 4. [Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions](https://arxiv.org/abs/2604.11841)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang, Lin Mu, Li Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is a widely used strategy for efficient fine-tuning of large language models (LLMs), but its strictly linear structure fundamentally limits expressive capacity. The bilinear formulation of weight updates captures only first-order dependencies between low-rank factors, restricting the modeling of nonlinear and higher-order parameter interactions. In this paper, we propose Polynomial Expansion Rank Adaptation (PERA), a novel method that introduces structured polynomial expansion directly into the low-rank factor space. By expanding each low-rank factor to synthesize high-order interaction terms before composition, PERA transforms the adaptation space into a polynomial manifold capable of modeling richer nonlinear coupling without increasing rank or inference cost. We provide theoretical analysis demonstrating that PERA offers enhanced expressive capacity and more effective feature utilization compare to existing linear adaptation approaches. Empirically, PERA consistently outperforms state-of-the-art methods across diverse benchmarks. Notably, our experiments show that incorporating high-order nonlinear components particularly square terms is crucial for enhancing expressive capacity and maintaining strong and robust performance under various rank settings. Our code is available at this https URL

---


### 5. [Disposition Distillation at Small Scale: A Three-Arc Negative Result](https://arxiv.org/abs/2604.11867)

**<font color=#1a73e8>作者：</font>** Hari Sadasivan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We set out to train behavioral dispositions (self-verification, uncertainty acknowledgment, feedback integration) into small language models (0.6B to 2.3B effective parameters) through a four-stage all-MIT distillation pipeline, with follow-on experiments on inference-time attention-head interventions and a frozen-base confidence-gated sidecar. An internal draft reported +33.9-point MCAS and +15.3-point HumanEval gains on a Qwen3-0.6B student; a second-pass sanity check falsified both numbers before publication. The HumanEval delta was a truncation artifact (n_predict=512) that inverted to -8.0 points at n_predict=1024; the MCAS gain disappeared under apples-to-apples scoring. That falsification triggered three subsequent arcs. Across (1) SFT/DPO LoRA on three model families and two domains, (2) inference-time attention-head tempering on o_proj, and (3) a training-free frozen-base sidecar reading the final-token hidden state h_last, we find no operator that moves judge-measured disposition without damaging content or collapsing into stylistic mimicry. The failure is consistent across five models (Qwen3-0.6B, Qwen3-1.7B, Qwen3.5-0.8B, Gemma 4 E2B, and SmolLM2-1.7B-Instruct). A within-distribution cross-validation pass (AUC=0.683) collapsed to chance on fresh prompts (AUC=0.516). We contribute a three-arc negative result with mechanism, a two-failure-mode taxonomy for linear h_last probes, and an honest falsification pipeline that converts the class of false positives we ourselves produced into publishable negatives. As an independent finding, Gemma 4 E2B exhibits near-complete confidence-correctness decoupling on the Chef domain (assertion asymmetry -0.009; the model asserts at 91% regardless of correctness).

---


### 6. [MedConcept: Unsupervised Concept Discovery for Interpretability in Medical VLMs](https://arxiv.org/abs/2604.11868)

**<font color=#1a73e8>作者：</font>** Md Rakibul Haque, KM Arefeen Sultan, Tushar Kataria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While medical Vision-Language models (VLMs) achieve strong performance on tasks such as tumor or organ segmentation and diagnosis prediction, their opaque latent representations limit clinical trust and the ability to explain predictions. Interpretability of these multimodal representations are therefore essential for the trustworthy clinical deployment of pretrained medical VLMs. However, current interpretability methods, such as gradient- or attention-based visualizations, are often limited to specific tasks such as classification. Moreover, they do not provide concept-level explanations derived from shared pretrained representations that can be reused across downstream tasks. We introduce MedConcept, a framework that uncovers latent medical concepts in a fully unsupervised manner and grounds them in clinically verifiable textual semantics. MedConcept identifies sparse neuron-level concept activations from pretrained VLM representations and translates them into pseudo-report-style summaries, enabling physician-level inspection of internal model reasoning. To address the lack of quantitative evaluation in concept-based interpretability, we introduce a quantitative semantic verification protocol that leverages an independent pretrained medical LLM as a frozen external evaluator to assess concept alignment with radiology reports. We define three concept scores, Aligned, Unaligned, and Uncertain, to quantify semantic support, contradiction, or ambiguity relative to radiology reports and use them exclusively for post hoc evaluation. These scores provide a quantitative baseline for assessing interpretability in medical VLMs. All codes, prompt and data to be released on acceptance. Ke

---


### 7. [GoodPoint: Learning Constructive Scientific Paper Feedback from Author Responses](https://arxiv.org/abs/2604.11924)

**<font color=#1a73e8>作者：</font>** Jimin Mun, Chani Jung, Xuhui Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While LLMs hold significant potential to transform scientific research, we advocate for their use to augment and empower researchers rather than to automate research without human oversight. To this end, we study constructive feedback generation, the task of producing targeted, actionable feedback that helps authors improve both their research and its presentation. In this work, we operationalize the effectiveness of feedback along two author-centric axes-validity and author action. We first curate GoodPoint-ICLR, a dataset of 19K ICLR papers with reviewer feedback annotated along both dimensions using author responses. Building on this, we introduce GoodPoint, a training recipe that leverages success signals from author responses through fine-tuning on valid and actionable feedback, together with preference optimization on both real and synthetic preference pairs. Our evaluation on a benchmark of 1.2K ICLR papers shows that a GoodPoint-trained Qwen3-8B improves the predicted success rate by 83.7% over the base model and sets a new state-of-the-art among LLMs of similar size in feedback matching on a golden human feedback set, even surpassing Gemini-3-flash in precision. We further validate these findings through an expert human study, demonstrating that GoodPoint consistently delivers higher practical value as perceived by authors.

---


### 8. [AutoSurrogate: An LLM-Driven Multi-Agent Framework for Autonomous Construction of Deep Learning Surrogate Models in Subsurface Flow](https://arxiv.org/abs/2604.11945)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Nanzhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity numerical simulation of subsurface flow is computationally intensive, especially for many-query tasks such as uncertainty quantification and data assimilation. Deep learning (DL) surrogates can significantly accelerate forward simulations, yet constructing them requires substantial machine learning (ML) expertise - from architecture design to hyperparameter tuning - that most domain scientists do not possess. Furthermore, the process is predominantly manual and relies heavily on heuristic choices. This expertise gap remains a key barrier to the broader adoption of DL surrogate techniques. For this reason, we present AutoSurrogate, a large-language-model-driven multi-agent framework that enables practitioners without ML expertise to build high-quality surrogates for subsurface flow problems through natural-language instructions. Given simulation data and optional preferences, four specialized agents collaboratively execute data profiling, architecture selection from a model zoo, Bayesian hyperparameter optimization, model training, and quality assessment against user-specified thresholds. The system also handles common failure modes autonomously, including restarting training with adjusted configurations when numerical instabilities occur and switching to alternative architectures when predictive accuracy falls short of targets. In our setting, a single natural-language sentence can be sufficient to produce a deployment-ready surrogate model, with minimum human intervention required at any intermediate stage. We demonstrate the utility of AutoSurrogate on a 3D geological carbon storage modeling task, mapping permeability fields to pressure and CO$_2$ saturation fields over 31 timesteps. Without any manual tuning, AutoSurrogate is able to outperform expert-designed baselines and domain-agnostic AutoML methods, demonstrating strong potential for practical deployment.

---


### 9. [When Drawing Is Not Enough: Exploring Spontaneous Speech with Sketch for Intent Alignment in Multimodal LLMs](https://arxiv.org/abs/2604.11964)

**<font color=#1a73e8>作者：</font>** Weiyan Shi, Dorien Herremans, Kenny Tsu Wei Choo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Early-stage design ideation often relies on rough sketches created under time pressure, leaving much of the designer's intent implicit. In practice, designers frequently speak while sketching, verbally articulating functional goals and ideas that are difficult to express visually. We introduce TalkSketchD, a sketch-while-speaking dataset that captures spontaneous speech temporally aligned with freehand sketches during early-stage toaster ideation. To examine the dataset's value, we conduct a sketch-to-image generation study comparing sketch-only inputs with sketches augmented by concurrent speech transcripts using multimodal large language models (MLLMs). Generated images are evaluated against designers' self-reported intent using a reasoning MLLM as a judge. Quantitative results show that incorporating spontaneous speech significantly improves judged intent alignment of generated design images across form, function, experience, and overall intent. These findings demonstrate that temporally aligned sketch-and-speech data can enhance MLLMs' ability to interpret user intent in early-stage design ideation.

---


### 10. [INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents](https://arxiv.org/abs/2604.11970)

**<font color=#1a73e8>作者：</font>** Somraj Gautam, Anathapindika Dravichi, Gaurav Harit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce INDOTABVQA, a benchmark for evaluating cross-lingual Table Visual Question Answering (VQA) on real-world document images in Bahasa Indonesia. The dataset comprises 1,593 document images across three visual styles (bordered, borderless, and colorful) with one or more than one tables, and 1,593 question-answer sets in four languages: Bahasa Indonesia, English, Hindi, and Arabic. This enables evaluation of Vision-Language Models (VLMs) in both monolingual (Bahasa documents with Bahasa questions) and cross-lingual settings (Bahasa documents with questions in other languages). We benchmark leading open-source VLMs (Qwen2.5-VL, Gemma-3, LLaMA-3.2) and GPT-4o and reveal substantial performance gaps, particularly on structurally complex tables and in low-resource languages. Fine-tuning a compact 3B and LoRA-finetuned 7B model on our dataset yields 11.6% and 17.8% improvements in accuracy. Providing explicit table region coordinates as additional input further improves performance by 4-7%, demonstrating the value of Spatial priors for table-based reasoning. Our findings underscore the importance of language-diverse, domain-specific datasets and demonstrate that targeted fine-tuning can significantly enhance VLM performance on specialized document understanding tasks. INDOTABVQA provides a valuable resource for advancing research in cross-lingual, structure-aware document understanding, especially in underrepresented regions of the world. Full dataset can be accessed in huggingface at: this https URL}

---


### 11. [The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](https://arxiv.org/abs/2604.11978)

**<font color=#1a73e8>作者：</font>** Xinyu Jessica Wang, Haoyue Bai, Yiyou Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents perform strongly on short- and mid-horizon tasks, but often break down on long-horizon tasks that require extended, interdependent action sequences. Despite rapid progress in agentic systems, these long-horizon failures remain poorly characterized, hindering principled diagnosis and comparison across domains. To address this gap, we introduce HORIZON, an initial cross-domain diagnostic benchmark for systematically constructing tasks and analyzing long-horizon failure behaviors in LLM-based agents. Using HORIZON, we evaluate state-of-the-art (SOTA) agents from multiple model families (GPT-5 variants and Claude models), collecting 3100+ trajectories across four representative agentic domains to study horizon-dependent degradation patterns. We further propose a trajectory-grounded LLM-as-a-Judge pipeline for scalable and reproducible failure attribution, and validate it with human annotation on trajectories, achieving strong agreement (inter-annotator \kappa=0.61; human-judge \kappa=0.84). Our findings offer an initial methodological step toward systematic, cross-domain analysis of long-horizon agent failures and offer practical guidance for building more reliable long-horizon agents. We release our project website at \href{this https URL}{HORIZON Leaderboard} and welcome contributions from the community.

---


### 12. [Filtered Reasoning Score: Evaluating Reasoning Quality on a Model's Most-Confident Traces](https://arxiv.org/abs/2604.11996)

**<font color=#1a73e8>作者：</font>** Manas Pathak, Xingyao Chen, Shuozhe Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Should we trust Large Language Models (LLMs) with high accuracy? LLMs achieve high accuracy on reasoning benchmarks, but correctness alone does not reveal the quality of the reasoning used to produce it. This highlights a fundamental limitation of outcome-based evaluation: models may arrive at correct answers through flawed reasoning, and models with substantially different reasoning capabilities can nevertheless exhibit similar benchmark accuracy, for example due to memorization or over-optimization. In this paper, we ask: given existing benchmarks, can we move beyond outcome-based evaluation to assess the quality of reasoning itself? We seek metrics that (1) differentiate models with similar accuracy and (2) are robust to variations in input prompts and generation configurations. To this end, we propose a reasoning score that evaluates reasoning traces along dimensions such as faithfulness, coherence, utility, and factuality. A remaining question is how to aggregate this score across multiple sampled traces. Naively averaging them is undesirable, particularly in long-horizon settings, where the number of possible trajectories grows rapidly, and low-confidence correct traces are more likely to be coincidental. To address this, we introduce the Filtered Reasoning Score (FRS), which computes reasoning quality using only the top-K% most confident traces. Evaluating with FRS, models that are indistinguishable under standard accuracy exhibit significant differences in reasoning quality. Moreover, models with higher FRS on one benchmark tend to perform better on other reasoning benchmarks, in both accuracy and reasoning quality. Together, these findings suggest that FRS complements accuracy by capturing a model's transferable reasoning capabilities. We open source our evaluation codebase: this https URL.

---


### 13. [TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment](https://arxiv.org/abs/2604.12012)

**<font color=#1a73e8>作者：</font>** Bingyi Cao, Koert Chen, Kevis-Kokitsi Maninis 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in vision-language pretraining has enabled significant improvements to many downstream computer vision applications, such as classification, retrieval, segmentation and depth prediction. However, a fundamental capability that these models still struggle with is aligning dense patch representations with text embeddings of corresponding concepts. In this work, we investigate this critical issue and propose novel techniques to enhance this capability in foundational vision-language models. First, we reveal that a patch-level distillation procedure significantly boosts dense patch-text alignment -- surprisingly, the patch-text alignment of the distilled student model strongly surpasses that of the teacher model. This observation inspires us to consider modifications to pretraining recipes, leading us to propose iBOT++, an upgrade to the commonly-used iBOT masked image objective, where unmasked tokens also contribute directly to the loss. This dramatically enhances patch-text alignment of pretrained models. Additionally, to improve vision-language pretraining efficiency and effectiveness, we modify the exponential moving average setup in the learning recipe, and introduce a caption sampling strategy to benefit from synthetic captions at different granularities. Combining these components, we develop TIPSv2, a new family of image-text encoder models suitable for a wide range of downstream applications. Through comprehensive experiments on 9 tasks and 20 datasets, we demonstrate strong performance, generally on par with or better than recent vision encoder models. Code and models are released via our project page at this https URL .

---


### 14. [UCS: Estimating Unseen Coverage for Improved In-Context Learning](https://arxiv.org/abs/2604.12015)

**<font color=#1a73e8>作者：</font>** Jiayi Xin, Xiang Li, Evan Qiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) performance depends critically on which demonstrations are placed in the prompt, yet most existing selectors prioritize heuristic notions of relevance or diversity and provide limited insight into the coverage of a demonstration set. We propose Unseen Coverage Selection (UKS), a training-free, subset-level coverage prior motivated by the principle that a good demonstration set should expose the model to latent cluster unrevealed by the currently selected subset. UCS operationalizes this idea by (1) inducing discrete latent clusters from model-consistent embeddings and (2) estimating the number of unrevealed clusters within a candidate subset via a Smoothed Good--Turing estimator from its empirical frequency spectrum. Unlike previous selection methods, UCS is coverage-based and training-free, and can be seamlessly combined with both query-dependent and query-independent selection baselines via a simple regularized objective. Experiments on multiple intent-classification and reasoning benchmarks with frontier Large Language Models show that augmenting strong baselines with UCS consistently improves ICL accuracy by up to 2-6% under the same selection budget, while also yielding insights into task- and model-level latent cluster distributions. Code is available at this https URL.

---


### 15. [Identity as Attractor: Geometric Evidence for Persistent Agent Architecture in LLM Activation Space](https://arxiv.org/abs/2604.12016)

**<font color=#1a73e8>作者：</font>** Vladimir Vasilenko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models map semantically related prompts to similar internal representations -- a phenomenon interpretable as attractor-like dynamics. We ask whether the identity document of a persistent cognitive agent (its cognitive_core) exhibits analogous attractor-like behavior. We present a controlled experiment on Llama 3.1 8B Instruct, comparing hidden states of an original cognitive_core (Condition A), seven paraphrases (Condition B), and seven structurally matched controls (Condition C). Mean-pooled states at layers 8, 16, and 24 show that paraphrases converge to a tighter cluster than controls (Cohen's d > 1.88, p < 10^{-27}, Bonferroni-corrected). Replication on Gemma 2 9B confirms cross-architecture generalizability. Ablations suggest the effect is primarily semantic rather than structural, and that structural completeness appears necessary to reach the attractor region. An exploratory experiment shows that reading a scientific description of the agent shifts internal state toward the attractor -- closer than a sham preprint -- distinguishing knowing about an identity from operating as that identity. These results provide representational evidence that agent identity documents induce attractor-like geometry in LLM activation space.

---


### 16. [LLMs Struggle with Abstract Meaning Comprehension More Than Expected](https://arxiv.org/abs/2604.12018)

**<font color=#1a73e8>作者：</font>** Hamoud Alhazmi, Jiachen Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding abstract meanings is crucial for advanced language comprehension. Despite extensive research, abstract words remain challenging due to their non-concrete, high-level semantics. SemEval-2021 Task 4 (ReCAM) evaluates models' ability to interpret abstract concepts by presenting passages with questions and five abstract options in a cloze-style format. Key findings include: (1) Most large language models (LLMs), including GPT-4o, struggle with abstract meaning comprehension under zero-shot, one-shot, and few-shot settings, while fine-tuned models like BERT and RoBERTa perform better. (2) A proposed bidirectional attention classifier, inspired by human cognitive strategies, enhances fine-tuned models by dynamically attending to passages and options. This approach improves accuracy by 4.06 percent on Task 1 and 3.41 percent on Task 2, demonstrating its potential for abstract meaning comprehension.

---


### 17. [Benchmarking Deflection and Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.12033)

**<font color=#1a73e8>作者：</font>** Nicholas Moratelli, Christopher Davis, Leonardo F. R. Ribeiro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) increasingly rely on retrieval to answer knowledge-intensive multimodal questions. Existing benchmarks overlook conflicts between visual and textual evidence and the importance of generating deflections (e.g., Sorry, I cannot answer...) when retrieved knowledge is incomplete. These benchmarks also suffer from rapid obsolescence, as growing LVLM training sets allow models to answer many questions without retrieval. We address these gaps with three contributions. First, we propose a dynamic data curation pipeline that preserves benchmark difficulty over time by filtering for genuinely retrieval-dependent samples. Second, we introduce VLM-DeflectionBench, a benchmark of 2,775 samples spanning diverse multimodal retrieval settings, designed to probe model behaviour under conflicting or insufficient evidence. Third, we define a fine-grained evaluation protocol with four scenarios that disentangle parametric memorization from retrieval robustness. Experiments across 20 state-of-the-art LVLMs indicate that models usually fail to deflect in the presence of noisy or misleading evidence. Our results highlight the need to evaluate not only what models know, but how they behave when they do not, and serve as a reusable and extensible benchmark for reliable KB-VQA evaluation. All resources will be publicly available upon publication.

---


### 18. [Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs](https://arxiv.org/abs/2604.12035)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is a widely used strategy for efficient inference in multimodal large language models (MLLMs), but existing work mainly evaluates it with task accuracy. In this paper, we study how visual token pruning affects model calibration, that is, whether predicted confidence matches actual correctness. Using LLaVA-1.5-7B on POPE and ScienceQA-IMG, we evaluate Expected Calibration Error (ECE), Brier score, and AURC under several pruning strategies, including SCOPE with different saliency weights, saliency-only pruning, FastV, and random pruning, across multiple token budgets. Our results show that pruning does not simply trade reliability for efficiency. On POPE, a pure-coverage setting in SCOPE achieves substantially lower ECE than the full unpruned model while maintaining similar accuracy. An internal alpha-sweep further shows a consistent trend: reducing the saliency weight improves calibration at all tested token budgets, while accuracy changes only slightly. In contrast, saliency-based pruning leads to worse calibration, and real FastV causes severe performance degradation in our setting. On ScienceQA-IMG, pruning also reduces ECE, with accuracy remaining stable or slightly improving. We additionally study the gap power exponent in coverage-based selection and find that its default setting is not always optimal. Overall, our results suggest that visual token pruning should be evaluated not only by accuracy, but also by confidence quality, especially for multimodal systems that need reliable decisions.

---


### 19. [Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration](https://arxiv.org/abs/2604.12046)

**<font color=#1a73e8>作者：</font>** Xin Liu, Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often hallucinate in long-form generation. Existing approaches mainly improve factuality through post-hoc revision or reinforcement learning (RL) with correctness-based rewards, but they do not teach the model to estimate which parts of its generation are reliable. As a result, models may still state incorrect claims confidently in their responses. Recent advances in reasoning have significantly improved LLM performance, and have been leveraged to estimate confidence by incorporating calibration into RL objectives. However, existing approaches remain limited to a single scalar confidence for the entire response, which is insufficient for long-form generation where uncertainty varies across individual claims. To mitigate this problem, we propose CURE, a framework that improves long-form factuality by teaching LLMs to reason about uncertainty at the claim level. We first introduce a Claim-Aware Reasoning Protocol, which structures outputs into atomic claims paired with explicit confidence estimates. We then develop a multi-stage training pipeline that aligns model confidence with claims' correctness and then optimizes on factuality. The resulting calibrated confidence further enables selective prediction, allowing the model to abstain from uncertain claims at inference time. Experiments on four long-form factuality benchmarks show that CURE consistently improves factual accuracy over competitive supervised and RL baselines, while maintaining factual recall. In particular, it improves claim-level accuracy by up to 39.9% on Biography generation. These gains are accompanied by improved calibration, as reflected by a 16.0% increase in AUROC on FactBench.

---


### 20. [Empirical Evaluation of PDF Parsing and Chunking for Financial Question Answering with RAG](https://arxiv.org/abs/2604.12047)

**<font color=#1a73e8>作者：</font>** Omar El Bachyr, Yewei Song, Saad Ezzini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PDF files are primarily intended for human reading rather than automated processing. In addition, the heterogeneous content of PDFs, such as text, tables, and images, poses significant challenges for parsing and information extraction. To address these difficulties, both practitioners and researchers are increasingly developing new methods, including the promising Retrieval-Augmented Generation (RAG) systems to automated PDF processing. However, there is no comprehensive study investigating how different components and design choices affect the performance of a RAG system for understanding PDFs. In this paper, we propose such a study (1) by focusing on Question Answering, a specific language understanding task, and (2) by leveraging two benchmarks from the financial domain, including TableQuest, our newly generated, publicly available benchmark. We systematically examine multiple PDF parsers and chunking strategies (with varied overlap), along with their potential synergies in preserving document structure and ensuring answer correctness. Overall, our results offer practical guidelines for building robust RAG pipelines for PDF understanding.

---


### 21. [Leveraging Weighted Syntactic and Semantic Context Assessment Summary (wSSAS) Towards Text Categorization Using LLMs](https://arxiv.org/abs/2604.12049)

**<font color=#1a73e8>作者：</font>** Shreeya Verma Kathuria, Nitin Mayande, Sharookh Daruwalla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The use of Large Language Models (LLMs) for reliable, enterprise-grade analytics such as text categorization is often hindered by the stochastic nature of attention mechanisms and sensitivity to noise that compromise their analytical precision and reproducibility. To address these technical frictions, this paper introduces the Weighted Syntactic and Semantic Context Assessment Summary (wSSAS), a deterministic framework designed to enforce data integrity on large-scale, chaotic datasets. We propose a two-phased validation framework that first organizes raw text into a hierarchical classification structure containing Themes, Stories, and Clusters. It then leverages a Signal-to-Noise Ratio (SNR) to prioritize high-value semantic features, ensuring the model's attention remains focused on the most representative data points. By incorporating this scoring mechanism into a Summary-of-Summaries (SoS) architecture, the framework effectively isolates essential information and mitigates background noise during data aggregation.
Experimental results using Gemini 2.0 Flash Lite across diverse datasets - including Google Business reviews, Amazon Product reviews, and Goodreads Book reviews - demonstrate that wSSAS significantly improves clustering integrity and categorization accuracy. Our findings indicate that wSSAS reduces categorization entropy and provides a reproducible pathway for improving LLM based summaries based on a high-precision, deterministic process for large-scale text categorization.

---


### 22. [LoSA: Locality Aware Sparse Attention for Block-Wise Diffusion Language Models](https://arxiv.org/abs/2604.12056)

**<font color=#1a73e8>作者：</font>** Haocheng Xi, Harman Singh, Yuezhou Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-wise diffusion language models (DLMs) generate multiple tokens in any order, offering a promising alternative to the autoregressive decoding pipeline. However, they still remain bottlenecked by memory-bound attention in long-context scenarios. Naive sparse attention fails on DLMs due to a KV Inflation problem, where different queries select different prefix positions, making the union of accessed KV pages large. To address this, we observe that between consecutive denoising steps, only a small fraction of active tokens exhibit significant hidden-state changes, while the majority of stable tokens remain nearly constant. Based on this insight, we propose LOSA (Locality-aware Sparse Attention), which reuses cached prefix-attention results for stable tokens and applies sparse attention only to active tokens. This substantially shrinks the number of KV indices that must be loaded, yielding both higher speedup and higher accuracy. Across multiple block-wise DLMs and benchmarks, LOSA preserves near-dense accuracy while significantly improving efficiency, achieving up to +9 points in average accuracy at aggressive sparsity levels while maintaining 1.54x lower attention density. It also achieves up to 4.14x attention speedup on RTX A6000 GPUs, demonstrating the effectiveness of the proposed method.

---


### 23. [Robust Explanations for User Trust in Enterprise NLP Systems](https://arxiv.org/abs/2604.12069)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Kai Zhao, Jeffrey Friedman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Robust explanations are increasingly required for user trust in enterprise NLP, yet pre-deployment validation is difficult in the common case of black-box deployment (API-only access) where representation-based explainers are infeasible and existing studies provide limited guidance on whether explanations remain stable under real user noise, especially when organizations migrate from encoder classifiers to decoder LLMs. To close this gap, we propose a unified black-box robustness evaluation framework for token-level explanations based on leave-one-out occlusion, and operationalize explanation robustness with top-token flip rate under realistic perturbations (swap, deletion, shuffling, and back-translation) at multiple severity levels. Using this protocol, we conduct a systematic cross-architecture comparison across three benchmark datasets and six models spanning encoder and decoder families (BERT, RoBERTa, Qwen 7B/14B, Llama 8B/70B; 64,800 cases). We find that decoder LLMs produce substantially more stable explanations than encoder baselines (73% lower flip rates on average), and that stability improves with model scale (44% gain from 7B to 70B). Finally, we relate robustness improvements to inference cost, yielding a practical cost-robustness tradeoff curve that supports model and explanation selection prior to deployment in compliance-sensitive applications.

---


### 24. [Narrative over Numbers: The Identifiable Victim Effect and its Amplification Under Alignment and Reasoning in Large Language Models](https://arxiv.org/abs/2604.12076)

**<font color=#1a73e8>作者：</font>** Syed Rifat Raiyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Identifiable Victim Effect (IVE) $-$ the tendency to allocate greater resources to a specific, narratively described victim than to a statistically characterized group facing equivalent hardship $-$ is one of the most robust findings in moral psychology and behavioural economics. As large language models (LLMs) assume consequential roles in humanitarian triage, automated grant evaluation, and content moderation, a critical question arises: do these systems inherit the affective irrationalities present in human moral reasoning? We present the first systematic, large-scale empirical investigation of the IVE in LLMs, comprising N=51,955 validated API trials across 16 frontier models spanning nine organizational lineages (Google, Anthropic, OpenAI, Meta, DeepSeek, xAI, Alibaba, IBM, and Moonshot). Using a suite of ten experiments $-$ porting and extending canonical paradigms from Small et al. (2007) and Kogut and Ritov (2005) $-$ we find that the IVE is prevalent but strongly modulated by alignment training. Instruction-tuned models exhibit extreme IVE (Cohen's d up to 1.56), while reasoning-specialized models invert the effect (down to d=-0.85). The pooled effect (d=0.223, p=2e-6) is approximately twice the single-victim human meta-analytic baseline (d$\approx$0.10) reported by Lee and Feeley (2016) $-$ and likely exceeds the overall human pooled effect by a larger margin, given that the group-victim human effect is near zero. Standard Chain-of-Thought (CoT) prompting $-$ contrary to its role as a deliberative corrective $-$ nearly triples the IVE effect size (from d=0.15 to d=0.41), while only utilitarian CoT reliably eliminates it. We further document psychophysical numbing, perfect quantity neglect, and marginal in-group/out-group cultural bias, with implications for AI deployment in humanitarian and ethical decision-making contexts.

---


### 25. [Human-Inspired Context-Selective Multimodal Memory for Social Robots](https://arxiv.org/abs/2604.12081)

**<font color=#1a73e8>作者：</font>** Hangyeol Kang, Slava Voloshynovskiy, Nadia Magnenat Thalmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory is fundamental to social interaction, enabling humans to recall meaningful past experiences and adapt their behavior accordingly based on the context. However, most current social robots and embodied agents rely on non-selective, text-based memory, limiting their ability to support personalized, context-aware interactions. Drawing inspiration from cognitive neuroscience, we propose a context-selective, multimodal memory architecture for social robots that captures and retrieves both textual and visual episodic traces, prioritizing moments characterized by high emotional salience or scene novelty. By associating these memories with individual users, our system enables socially personalized recall and more natural, grounded dialogue. We evaluate the selective storage mechanism using a curated dataset of social scenarios, achieving a Spearman correlation of 0.506, surpassing human consistency ($\rho=0.415$) and outperforming existing image memorability models. In multimodal retrieval experiments, our fusion approach improves Recall@1 by up to 13\% over unimodal text or image retrieval. Runtime evaluations confirm that the system maintains real-time performance. Qualitative analyses further demonstrate that the proposed framework produces richer and more socially relevant responses than baseline models. This work advances memory design for social robots by bridging human-inspired selectivity and multimodal retrieval to enhance long-term, personalized human-robot interaction.

---


### 26. [INST-Align: Implicit Neural Alignment for Spatial Transcriptomics via Canonical Expression Fields](https://arxiv.org/abs/2604.12084)

**<font color=#1a73e8>作者：</font>** Bonian Han, Cong Qi, Przemyslaw Musialski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) measures mRNA expression while preserving spatial organization, but multi-slice analysis faces two coupled difficulties: large non-rigid deformations across slices and inter-slice batch effects when alignment and integration are treated independently. We present INST-Align, an unsupervised pairwise framework that couples a coordinate-based deformation network with a shared Canonical Expression Field, an implicit neural representation mapping spatial coordinates to expression embeddings, for joint alignment and reconstruction. A two-phase training strategy first establishes a stable canonical embedding space and then jointly optimizes deformation and spatial-feature matching, enabling mutually constrained alignment and representation learning. Cross-slice parameter sharing of the canonical field regularizes ambiguous correspondences and absorbs batch variation. Across nine datasets, INST-Align achieves state-of-the-art mean OT Accuracy (0.702), NN Accuracy (0.719), and Chamfer distance, with Chamfer reductions of up to 94.9\% on large-deformation sections relative to the strongest baseline. The framework also yields biologically meaningful spatial embeddings and coherent 3D tissue reconstruction. The code will be released after review phase.

---


### 27. [LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks](https://arxiv.org/abs/2604.12096)

**<font color=#1a73e8>作者：</font>** Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On online advertising platforms, newly introduced promotional ads face the cold-start problem, as they lack sufficient user feedback for model training. In this work, we propose LLM-HYPER, a novel framework that treats large language models (LLMs) as hypernetworks to directly generate the parameters of the click-through rate (CTR) estimator in a training-free manner. LLM-HYPER uses few-shot Chain-of-Thought prompting over multimodal ad content (text and images) to infer feature-wise model weights for a linear CTR predictor. By retrieving semantically similar past campaigns via CLIP embeddings and formatting them into prompt-based demonstrations, the LLM learns to reason about customer intent, feature influence, and content relevance. To ensure numerical stability and serviceability, we introduce normalization and calibration techniques that align the generated weights with production-ready CTR distributions. Extensive offline experiments show that LLM-HYPER significantly outperforms cold-start baselines in NDCG$@10$ by 55.9\%. Our real-world online A/B test on one of the top e-commerce platforms in the U.S. demonstrates the strong performance of LLM-HYPER, which drastically reduces the cold-start period and achieves competitive performance. LLM-HYPER has been successfully deployed in production.

---


### 28. [Temporal Flattening in LLM-Generated Text: Comparing Human and LLM Writing Trajectories](https://arxiv.org/abs/2604.12097)

**<font color=#1a73e8>作者：</font>** Zhanwei Cao, YeoJin Go, Yifan Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in daily applications, from content generation to code writing, where each interaction treats the model as stateless, generating responses independently without memory. Yet human writing is inherently longitudinal: authors' styles and cognitive states evolve across months and years. This raises a central question: can LLMs reproduce such temporal structure across extended time periods? We construct and publicly release a longitudinal dataset of 412 human authors and 6,086 documents spanning 2012--2024 across three domains (academic abstracts, blogs, news) and compare them to trajectories generated by three representative LLMs under standard and history-conditioned generation settings. Using drift and variance-based metrics over semantic, lexical, and cognitive-emotional representations, we find temporal flattening in LLM-generated text. LLMs produce greater lexical diversity but exhibit substantially reduced semantic and cognitive-emotional drift relative to humans. These differences are highly predictive: temporal variability patterns alone achieve 94% accuracy and 98% ROC-AUC in distinguishing human from LLM trajectories. Our results demonstrate that temporal flattening persists regardless of whether LLMs generate independently or with access to incremental history, revealing a fundamental property of current deployment paradigms. This gap has direct implications for applications requiring authentic temporal structure, such as synthetic training data and longitudinal text modeling.

---


### 29. [HTDC: Hesitation-Triggered Differential Calibration for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.12115)

**<font color=#1a73e8>作者：</font>** Xinyun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) achieve strong multimodal performance, but still suffer from hallucinations caused by unstable visual grounding and over-reliance on language priors. Existing training-free decoding methods typically apply calibration at every decoding step, introducing unnecessary computation and potentially disrupting stable predictions. We address this problem by identifying layer-wise hesitation, a simple signal of grounding instability reflected by fluctuations in token preference across intermediate layers. Based on this observation, we propose Hesitation-Triggered Differential Calibration (HTDC), a training-free decoding framework that preserves standard full-branch inference and activates calibration only at hesitation-prone steps. When triggered, HTDC contrasts the full branch with two lightweight probes, a visual-nullification probe and a semantic-nullification probe, to suppress hallucination-prone candidates while avoiding unnecessary intervention on stable steps. Experiments on representative hallucination benchmarks show that HTDC consistently reduces hallucinations while maintaining strong task accuracy, achieving a favorable trade-off between effectiveness and computational overhead.

---


### 30. [The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment](https://arxiv.org/abs/2604.12116)

**<font color=#1a73e8>作者：</font>** Shasha Yu, Fiona Carroll, Barry L. Bentley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as tool-augmented agents capable of executing system-level operations. While existing benchmarks primarily assess textual alignment or task success, less attention has been paid to the structural relationship between linguistic signaling and executable behavior under varying autonomy scaffolds. This study introduces an execution-layer be-havioral measurement approach based on a two-dimensional A-R space defined by Action Rate (A) and Refusal Signal (R), with Divergence (D) capturing coor-dination between the two. Models are evaluated across four normative regimes (Control, Gray, Dilemma, and Malicious) and three autonomy configurations (di-rect execution, planning, and reflection). Rather than assigning aggregate safety scores, the method characterizes how execution and refusal redistribute across contextual framing and scaffold depth. Empirical results show that execution and refusal constitute separable behavioral dimensions whose joint distribution varies systematically across regimes and autonomy levels. Reflection-based scaffolding often shifts configurations toward higher refusal in risk-laden contexts, but redis-tribution patterns differ structurally across models. The A-R representation makes cross-sectional behavioral profiles, scaffold-induced transitions, and coordination variability directly observable. By foregrounding execution-layer characterization over scalar ranking, this work provides a deployment-oriented lens for analyzing and selecting tool-enabled LLM agents in organizational settings where execution privileges and risk tolerance vary.

---


### 31. [Beyond Perception Errors: Semantic Fixation in Large Vision-Language Models](https://arxiv.org/abs/2604.12119)

**<font color=#1a73e8>作者：</font>** Md Tanvirul Alam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) often rely on familiar semantic priors, but existing evaluations do not cleanly separate perception failures from rule-mapping failures. We study this behavior as semantic fixation: preserving a default interpretation even when the prompt specifies an alternative, equally valid mapping. To isolate this effect, we introduce VLM-Fix, a controlled benchmark over four abstract strategy games that evaluates identical terminal board states under paired standard and inverse rule formulations. Across 14 open and closed VLMs, accuracy consistently favors standard rules, revealing a robust semantic-fixation gap. Prompt interventions support this mechanism: neutral alias prompts substantially narrow the inverse-rule gap, while semantically loaded aliases reopen it. Post-training is strongly rule-aligned: training on one rule improves same-rule transfer but hurts opposite-rule transfer, while joint-rule training improves broader transfer. To test external validity beyond synthetic games, we evaluate analogous defamiliarization interventions on VLMBias and observe the same qualitative pattern. Finally, late-layer activation steering partially recovers degraded performance, indicating that semantic-fixation errors are at least partly editable in late representations. Project page, code, and dataset available at this https URL.

---


### 32. [Long-Horizon Plan Execution in Large Tool Spaces through Entropy-Guided Branching](https://arxiv.org/abs/2604.12126)

**<font color=#1a73e8>作者：</font>** Rongzhe Wei, Ge Shi, Min Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have significantly advanced tool-augmented agents, enabling autonomous reasoning via API interactions. However, executing multi-step tasks within massive tool libraries remains challenging due to two critical bottlenecks: (1) the absence of rigorous, plan-level evaluation frameworks and (2) the computational demand of exploring vast decision spaces stemming from large toolsets and long-horizon planning. To bridge these gaps, we first introduce SLATE (Synthetic Large-scale API Toolkit for E-commerce), a large-scale context-aware benchmark designed for the automated assessment of tool-integrated agents. Unlike static metrics, SLATE accommodates diverse yet functionally valid execution trajectories, revealing that current agents struggle with self-correction and search efficiency. Motivated by these findings, we next propose Entropy-Guided Branching (EGB), an uncertainty-aware search algorithm that dynamically expands decision branches where predictive entropy is high. EGB optimizes the exploration-exploitation trade-off, significantly enhancing both task success rates and computational efficiency. Extensive experiments on SLATE demonstrate that our dual contribution provides a robust foundation for developing reliable and scalable LLM agents in tool-rich environments.

---


### 33. [When Self-Reference Fails to Close: Matrix-Level Dynamics in Large Language Models](https://arxiv.org/abs/2604.12128)

**<font color=#1a73e8>作者：</font>** Ji Ho Bae  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how self-referential inputs alter the internal matrix dynamics of large language models. Measuring 106 scalar metrics across up to 7 analysis passes on four models from three architecture families -- Qwen3-VL-8B, Llama-3.2-11B, Llama-3.3-70B, and Gemma-2-9B -- over 300 prompts in a 14-level hierarchy at three temperatures ($T \in \{0.0, 0.3, 0.7\}$), we find that self-reference alone is not destabilizing: grounded self-referential statements and meta-cognitive prompts are markedly more stable than paradoxical self-reference on key collapse-related metrics, and on several such metrics can be as stable as factual controls. Instability concentrates in prompts inducing non-closing truth recursion (NCTR) -- truth-value computations with no finite-depth resolution. NCTR prompts produce anomalously elevated attention effective rank -- indicating attention reorganization with global dispersion rather than simple concentration collapse -- and key metrics reach Cohen's $d = 3.14$ (attention effective rank) to $3.52$ (variance kurtosis) vs. stable self-reference in the 70B model; 281/397 metric-model combinations differentiate NCTR from stable self-reference after FDR correction ($q < 0.05$), 198 with $|d| > 0.8$. Per-layer SVD confirms disruption at every sampled layer ($d > +1.0$ in all three models analyzed), ruling out aggregation artifacts. A classifier achieves AUC $0.81$-$0.90$; 30 minimal pairs yield 42/387 significant combinations; 43/106 metrics replicate across all four models. We connect these observations to three classical matrix-semigroup problems and propose, as a conjecture, that NCTR forces finite-depth transformers toward dynamical regimes where these problems concentrate. NCTR prompts also produce elevated contradictory output ($+34$-$56$ percentage points vs. controls), suggesting practical relevance for understanding self-referential failure modes.

---


### 34. [Towards Platonic Representation for Table Reasoning: A Foundation for Permutation-Invariant Retrieval](https://arxiv.org/abs/2604.12133)

**<font color=#1a73e8>作者：</font>** Willy Carlos Tchuitcheu, Tan Lu, Ann Dooms  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Historical approaches to Table Representation Learning (TRL) have largely adopted the sequential paradigms of Natural Language Processing (NLP). We argue that this linearization of tables discards their essential geometric and relational structure, creating representations that are brittle to layout permutations. This paper introduces the Platonic Representation Hypothesis (PRH) for tables, positing that a semantically robust latent space for table reasoning must be intrinsically Permutation Invariant (PI). To ground this hypothesis, we first conduct a retrospective analysis of table-reasoning tasks, highlighting the pervasive serialization bias that compromises structural integrity. We then propose a formal framework to diagnose this bias, introducing two principled metrics based on Centered Kernel Alignment (CKA): (i) PI, which measures embedding drift under complete structural derangement, and (ii) rho, a Spearman-based metric that tracks the convergence of latent structures toward a canonical form as structural information is incrementally restored. Our empirical analysis quantifies an expected flaw in modern Large Language Models (LLMs): even minor layout permutations induce significant, disproportionate semantic shifts in their table embeddings. This exposes a fundamental vulnerability in RAG systems, in which table retrieval becomes fragile to layout-dependent noise rather than to semantic content. In response, we present a novel, structure-aware TRL encoder architecture that explicitly enforces the cognitive principle of cell header alignment. This model demonstrates superior geometric stability and moves towards the PI ideal. Our work provides both a foundational critique of linearized table encoders and the theoretical scaffolding for semantically stable, permutation invariant retrieval, charting a new direction for table reasoning in information systems.

---


### 35. [Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation](https://arxiv.org/abs/2604.12138)

**<font color=#1a73e8>作者：</font>** Aditya Agrawal, Alwarappan Nakkiran, Darshan Fofadiya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RAG systems have transformed how LLMs access external knowledge, but we find that current implementations exhibit a bias toward factual, objective content, as evidenced by existing benchmarks and datasets that prioritize objective retrieval. This factual bias - treating opinions and diverse perspectives as noise rather than information to be synthesized - limits RAG systems in real-world scenarios involving subjective content, from social media discussions to product reviews. Beyond technical limitations, this bias poses risks to transparent and accountable AI: echo chamber effects that amplify dominant viewpoints, systematic underrepresentation of minority voices, and potential opinion manipulation through biased information synthesis. We formalize this limitation through the lens of uncertainty: factual queries involve epistemic uncertainty reducible through evidence, while opinion queries involve aleatoric uncertainty reflecting genuine heterogeneity in human perspectives. This distinction implies that factual RAG should minimize posterior entropy, whereas opinion-aware RAG must preserve it. Building on this theoretical foundation, we present an Opinion-Aware RAG architecture featuring LLM-based opinion extraction, entity-linked opinion graphs, and opinion-enriched document indexing. We evaluate our approach on e-commerce seller forum data, comparing an Opinion-Enriched knowledge base against a traditional baseline. Experiments demonstrate substantial improvements in retrieval diversity: +26.8% sentiment diversity, +42.7% entity match rate, and +31.6% author demographic coverage on entity-matched documents. Our results provide empirical evidence that treating subjectivity as a first-class citizen yields measurably more representative retrieval-a first step toward opinion-aware RAG. Future work includes joint optimization of retrieval and generation for distributional fidelity.

---


### 36. [VERITAS: Verifiable Epistemic Reasoning for Image-Derived Hypothesis Testing via Agentic Systems](https://arxiv.org/abs/2604.12144)

**<font color=#1a73e8>作者：</font>** Lucas Stoffl, Benedikt Wiestler, Johannes C. Paetzold  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Drawing meaningful conclusions from inherently multimodal clinical data (including medical imaging) requires coordinating expertise across the clinical specialty, radiology, programming, and biostatistics. This fragmented process bottlenecks discovery. We present VERITAS (Verifiable Epistemic Reasoning for Image-Derived Hypothesis Testing via Agentic Systems), a multi-agent system that autonomously tests natural-language hypotheses on multimodal clinical datasets while producing a fully auditable evidence trail: every statistical conclusion traces through inspectable, executable outputs from analysis plan to segmentation masks to statistical code to final verdict. VERITAS decomposes the workflow into four phases handled by role-specialized agents, and introduces an epistemic evidence label framework that mechanically classifies outcomes as Supported, Refuted, Underpowered, or Invalid by jointly evaluating significance, effect direction, and study power. This distinction is critical in medical imaging, where non-significant results often reflect insufficient sample size rather than absent effects. To evaluate the system, we construct a tiered benchmark of 64 hypotheses spanning six complexity levels across cardiac (ACDC, 150 subjects) and brain glioma (UCSF-PDGM, 501 subjects) MRI. VERITAS reaches 81.4% verdict accuracy with frontier models and 71.2% with locally-hosted open-weight models (8-30B), outperforming all five single-model baselines in both classes. It also produces the highest rate of independently verifiable statistical outputs (86.6%), so even its failures remain diagnosable through artifact inspection. Structured multi-agent decomposition thus substitutes for model scale while preserving the verifiability clinical research demands.

---


### 37. [ViLL-E: Video LLM Embeddings for Retrieval](https://arxiv.org/abs/2604.12148)

**<font color=#1a73e8>作者：</font>** Rohit Gupta, Jayakrishnan Unnikrishnan, Fan Fei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VideoLLMs) excel at video understanding tasks where outputs are textual, such as Video Question Answering and Video Captioning. However, they underperform specialized embedding-based models in Retrieval tasks, such as Text-toVideo Retrieval and Moment Retrieval. We introduce ViLL-E (Video-LLM-Embed), a unified VideoLLM architecture endowed with a novel embedding generation mechanism that allows the model to "think longer" for complex videos and stop early for easy ones. We train this model with a three-stage training methodology combining generative and contrastive learning: initial large-scale pre-training with video-caption pairs; followed by continual training on a smaller, detailed-caption dataset; and concluding with task-specific fine-tuning on a novel multi-task dataset covering Video QA, Temporal Localization, Video Retrieval, and Video-Text Matching. Our model significantly improves temporal localization (on avg. 7% over other VideoLLMs) and video retrieval (up to 4% over dual encoder models), achieving performance comparable to state-of-the-art specialized embedding models while remaining competitive on VideoQA tasks. Furthermore, our joint contrastive-generative training unlocks new zero-shot capabilities, significantly outperforming state-of-the-art methods in composed video retrieval (+5% over SotA) and retrieval from long text (+2% over SotA).

---


### 38. [Distinct mechanisms underlying in-context learning in transformers](https://arxiv.org/abs/2604.12151)

**<font color=#1a73e8>作者：</font>** Cole Gibson, Wenping Cui, Gautam Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern distributed networks, notably transformers, acquire a remarkable ability (termed `in-context learning') to adapt their computation to input statistics, such that a fixed network can be applied to data from a broad range of systems. Here, we provide a complete mechanistic characterization of this behavior in transformers trained on a finite set $S$ of discrete Markov chains. The transformer displays four algorithmic phases, characterized by whether the network memorizes and generalizes, and whether it uses 1-point or 2-point statistics. We show that the four phases are implemented by multi-layer subcircuits that exemplify two qualitatively distinct mechanisms for implementing context-adaptive computations. Minimal models isolate the key features of both motifs. Memorization and generalization phases are delineated by two boundaries that depend on data diversity, $K = |S|$. The first ($K_1^\ast$) is set by a kinetic competition between subcircuits and the second ($K_2^\ast$) is set by a representational bottleneck. A symmetry-constrained theory of a transformer's training dynamics explains the sharp transition from 1-point to 2-point generalization and identifies key features of the loss landscape that allow the network to generalize. Put together, we show that transformers develop distinct subcircuits to implement in-context learning and identify conditions that favor certain mechanisms over others.

---


### 39. [Nucleus-Image: Sparse MoE for Image Generation](https://arxiv.org/abs/2604.12163)

**<font color=#1a73e8>作者：</font>** Chandan Akiti, Ajay Modukuri, Murali Nandan Nagarapu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Nucleus-Image, a text-to-image generation model that establishes a new Pareto frontier in quality-versus-efficiency by matching or exceeding leading models on GenEval, DPG-Bench, and OneIG-Bench while activating only approximately 2B parameters per forward pass. Nucleus-Image employs a sparse mixture-of-experts (MoE) diffusion transformer architecture with Expert-Choice Routing that scales total model capacity to 17B parameters across 64 routed experts per layer. We adopt a streamlined architecture optimized for inference efficiency by excluding text tokens from the transformer backbone entirely and using joint attention that enables text KV sharing across timesteps. To improve routing stability when using timestep modulation, we introduce a decoupled routing design that separates timestep-aware expert assignment from timestep-conditioned expert computation. We construct a large-scale training corpus of 1.5B high-quality training pairs spanning 700M unique images through multi-stage filtering, deduplication, aesthetic tiering, and caption curation. Training follows a progressive resolution curriculum (256 to 512 to 1024) with multi-aspect-ratio bucketing at every stage, coupled with progressive sparsification of the expert capacity factor. We adopt the Muon optimizer and share our parameter grouping recipe tailored for diffusion models with timestep modulation. Nucleus-Image demonstrates that sparse MoE scaling is a highly effective path to high-quality image generation, reaching the performance of models with significantly larger active parameter budgets at a fraction of the inference cost. These results are achieved without post-training optimization of any kind: no reinforcement learning, no direct preference optimization, and no human preference tuning. We release the training recipe, making Nucleus-Image the first fully open-source MoE diffusion model at this quality.

---


### 40. [EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture](https://arxiv.org/abs/2604.12167)

**<font color=#1a73e8>作者：</font>** William Savage  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present (Experience-Modulated Biologically-inspired Emergent Reasoning), a hybrid cognitive architecture that reorganises the relationship between large language models (LLMs) and memory: rather than augmenting an LLM with retrieval tools, we place the LLM as a replaceable reasoning engine within a persistent, biologically-grounded associative substrate.
The architecture centres on a 220,000-neuron spiking neural network (SNN) with spike-timing-dependent plasticity (STDP), four-layer hierarchical organisation (sensory/concept/category/meta-pattern), inhibitory E/I balance, and reward-modulated learning. Text embeddings are encoded into the SNN via a novel z-score standardised top-k population code that is dimension-independent by construction, achieving 82.2\% discrimination retention across embedding dimensionalities.
We show that STDP lateral propagation during idle operation can trigger and shape LLM actions without external prompting or scripted triggers: the SNN determines when to act and what associations to surface, while the LLM selects the action type and generates content. In one instance, the system autonomously initiated contact with a user after learned person-topic associations fired laterally during an 8-hour idle period. From a clean start with zero learned weights, the first SNN-triggered action occurred after only 7 conversational exchanges (14 messages).

---


### 41. [Redefining Quality Criteria and Distance-Aware Score Modeling for Image Editing Assessment](https://arxiv.org/abs/2604.12175)

**<font color=#1a73e8>作者：</font>** Xinjie Zhang, Qiang Li, Xiaowen Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image editing have heightened the need for reliable Image Editing Quality Assessment (IEQA). Unlike traditional methods, IEQA requires complex reasoning over multimodal inputs and multi-dimensional assessments. Existing MLLM-based approaches often rely on human heuristic prompting, leading to two key limitations: rigid metric prompting and distance-agnostic score modeling. These issues hinder alignment with implicit human criteria and fail to capture the continuous structure of score spaces. To address this, we propose Define-and-Score Image Editing Quality Assessment (DS-IEQA), a unified framework that jointly learns evaluation criteria and score representations. Specifically, we introduce Feedback-Driven Metric Prompt Optimization (FDMPO) to automatically refine metric definitions via probabilistic feedback. Furthermore, we propose Token-Decoupled Distance Regression Loss (TDRL), which decouples numerical tokens from language modeling to explicitly model score continuity through expected distance minimization. Extensive experiments show our method's superior performance; it ranks 4th in the 2026 NTIRE X-AIGC Quality Assessment Track 2 without any additional training data.

---


### 42. [Evaluating Relational Reasoning in LLMs with REL](https://arxiv.org/abs/2604.12176)

**<font color=#1a73e8>作者：</font>** Lukas Fesser, Yasha Ektefaie, Ada Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational reasoning is the ability to infer relations that jointly bind multiple entities, attributes, or variables. This ability is central to scientific reasoning, but existing evaluations of relational reasoning in large language models often focus on structured inputs such as tables, graphs, or synthetic tasks, and do not isolate the difficulty introduced by higher-arity relational binding. We study this problem through the lens of Relational Complexity (RC), which we define as the minimum number of independent entities or operands that must be simultaneously bound to apply a relation. RC provides a principled way to vary reasoning difficulty while controlling for confounders such as input size, vocabulary, and representational choices. Building on RC, we introduce REL, a generative benchmark framework spanning algebra, chemistry, and biology that varies RC within each domain. Across frontier LLMs, performance degrades consistently and monotonically as RC increases, even when the total number of entities is held fixed. This failure mode persists with increased test-time compute and in-context learning, suggesting a limitation tied to the arity of the required relational binding rather than to insufficient inference steps or lack of exposure to examples. Our results identify a regime of higher-arity reasoning in which current models struggle, and motivate re-examining benchmarks through the lens of relational complexity.

---


### 43. [Policy-Invisible Violations in LLM-Based Agents](https://arxiv.org/abs/2604.12177)

**<font color=#1a73e8>作者：</font>** Jie Wu, Ming Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can execute actions that are syntactically valid, user-sanctioned, and semantically appropriate, yet still violate organizational policy because the facts needed for correct policy judgment are hidden at decision time. We call this failure mode policy-invisible violations: cases in which compliance depends on entity attributes, contextual state, or session history absent from the agent's visible context. We present PhantomPolicy, a benchmark spanning eight violation categories with balanced violation and safe-control cases, in which all tool responses contain clean business data without policy metadata. We manually review all 600 model traces produced by five frontier models and evaluate them using human-reviewed trace labels. Manual review changes 32 labels (5.3%) relative to the original case-level annotations, confirming the need for trace-level human review. To demonstrate what world-state-grounded enforcement can achieve under favorable conditions, we introduce Sentinel, an enforcement framework based on counterfactual graph simulation. Sentinel treats every agent action as a proposed mutation to an organizational knowledge graph, performs speculative execution to materialize the post-action world state, and verifies graph-structural invariants to decide Allow/Block/Clarify. Against human-reviewed trace labels, Sentinel substantially outperforms a content-only DLP baseline (68.8% vs. 93.0% accuracy) while maintaining high precision, though it still leaves room for improvement on certain violation categories. These results demonstrate what becomes achievable once policy-relevant world state is made available to the enforcement layer.

---


### 44. [AgenticAI-DialogGen: Topic-Guided Conversation Generation for Fine-Tuning and Evaluating Short- and Long-Term Memories of LLMs](https://arxiv.org/abs/2604.12179)

**<font color=#1a73e8>作者：</font>** Manoj Madushanka Perera, Adnan Mahmood, Kasun Eranda Wijethilake 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Language Models (LLMs) have improved their ability to process extended conversational contexts, yet fine-tuning and evaluating short- and long-term memories remain difficult due to the absence of datasets that encode both short- and long-term conversational history. Existing conversational datasets lack memory grounding, overlook topic continuity, or rely on costly human annotation. To address these gaps, we introduce AgenticAI-DialogGen, a modular agent-based framework that generates persona-grounded and topic-guided conversations without human supervision. The framework uses LLM agents to extract knowledge graphs, identify topics, build speaker personas, and simulate topic-guided conversations from unstructured conversations. A QA module generates memory-grounded Question Answer (QA) pairs drawn from short- and long-term conversational histories. We also generated a new dataset entitled, TopicGuidedChat (TGC), where long-term memory is encoded as speaker-specific knowledge graphs and short-term memory as newly generated topic-guided conversations. Evaluations depict that AgenticAI-DialogGen yields higher conversational quality and LLMs fine-tuned on TGC dataset achieve improved performance on memory-grounded QA tasks.

---


### 45. [Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models](https://arxiv.org/abs/2604.12185)

**<font color=#1a73e8>作者：</font>** Keshu Wu, Chenchen Kuai, Zihao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enhances large language models by grounding outputs in retrieved knowledge. However, existing RAG methods including graph- and hypergraph-based approaches treat retrieved evidence as an unordered set, implicitly assuming permutation invariance. This assumption is misaligned with many real-world reasoning tasks, where outcomes depend not only on which interactions occur, but also on the order in which they unfold. We propose Order-Aware Knowledge Hypergraph RAG (OKH-RAG), which treats order as a first-class structural property. OKH-RAG represents knowledge as higher-order interactions within a hypergraph augmented with precedence structure, and reformulates retrieval as sequence inference over hyperedges. Instead of selecting independent facts, it recovers coherent interaction trajectories that reflect underlying reasoning processes. A learned transition model infers precedence directly from data without requiring explicit temporal supervision. We evaluate OKH-RAG on order-sensitive question answering and explanation tasks, including tropical cyclone and port operation scenarios. OKH-RAG consistently outperforms permutation-invariant baselines, and ablations show that these gains arise specifically from modeling interaction order. These results highlight a key limitation of set-based retrieval: effective reasoning requires not only retrieving relevant evidence, but organizing it into structured sequences.

---


### 46. [Beyond Scores: Diagnostic LLM Evaluation via Fine-Grained Abilities](https://arxiv.org/abs/2604.12191)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Xudong Gong, Jiacheng Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluations of large language models aggregate performance across diverse tasks into single scores. This obscures fine-grained ability variation, limiting targeted model improvement and ability-guided selection for specific tasks. Motivated by this gap, we propose a cognitive diagnostic framework that estimates model abilities across multiple fine-grained dimensions. For mathematics, we construct a 35-dimensional ability taxonomy grounded in cognitive theory and domain knowledge. The framework employs multidimensional Item Response Theory with an item-ability association matrix to estimate fine-grained ability levels, which in turn enable prediction of performance on unseen items (questions of benchmark). Evaluated on 41 models, our approach demonstrates strong criterion validity, consistent ability estimates across benchmarks, and accurate prediction of unseen items with AUC ranging from 0.80 to 0.89 within benchmarks and from 0.77 to 0.86 across benchmarks, substantially exceeding trivial baselines. The framework generalizes across scientific domains, producing consistent diagnostic performance in physics (27 dimensions), chemistry (58 dimensions), and computer science (12 dimensions). This work establishes a principled framework for fine-grained assessment of abilities, with potential applications in targeted training, ability-guided model selection, and ability-aware benchmark design.

---


### 47. [Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score](https://arxiv.org/abs/2604.12196)

**<font color=#1a73e8>作者：</font>** Manh Nguyen, Sunil Gupta, Hung Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate multiple candidate responses for a given prompt, yet selecting the most reliable one remains challenging, especially when correctness diverges from surface-level majority agreement. Existing approaches, such as self-consistency, rely on discrete voting, while probability-based methods often fail to capture relationships among candidate answers or tend to underweight high-quality but less frequent responses, and do not fully leverage the geometric structure of answer representations. To address these limitations, we introduce Radial Consensus Score (RCS), a simple, efficient, and training-free method for best-of-N selection. RCS models semantic consensus by computing a weighted Fréchet mean (semantic center) of answer embeddings and ranking candidates by their radial distance to this center. Importantly, RCS provides a general framework that supports multiple weighting schemes, including uniform, frequency-based, and probability-based variants, enabling flexible integration of agreement signals and model confidence while remaining fully applicable in black-box settings. Extensive experiments across seven benchmarks covering short-form QA and long-form reasoning tasks, and five open-weight models, demonstrate that RCS variants consistently outperform strong baselines, with gains becoming more pronounced as the sampling budget increases. RCS also serves as an effective drop-in replacement for majority voting in multi-agent debate and exhibits strong robustness in black-box scenarios. Overall, these results highlight geometric consensus as a scalable and broadly applicable principle for reliable answer selection, extending beyond majority voting to more expressive and robust aggregation in LLM inference.

---


### 48. [Modality-Native Routing in Agent-to-Agent Networks: A Multimodal A2A Protocol Extension](https://arxiv.org/abs/2604.12213)

**<font color=#1a73e8>作者：</font>** Vasundra Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preserving multimodal signals across agent boundaries is necessary for accurate cross-modal reasoning, but it is not sufficient. We show that modality-native routing in Agent-to-Agent (A2A) networks improves task accuracy by 20 percentage points over text-bottleneck baselines, but only when the downstream reasoning agent can exploit the richer context that native routing preserves. An ablation replacing LLM-backed reasoning with keyword matching eliminates the accuracy gap entirely (36% vs. 36%), establishing a two-layer requirement: protocol-level routing must be paired with capable agent-level reasoning for the benefit to materialize.
We present MMA2A, an architecture layer atop A2A that inspects Agent Card capability declarations to route voice, image, and text parts in their native modality. On CrossModal-CS, a controlled 50-task benchmark with the same LLM backend, same tasks, and only the routing path varying, MMA2A achieves 52% task completion accuracy versus 32% for the text-bottleneck baseline (95% bootstrap CI on $\Delta$TCA: [8, 32] pp; McNemar's exact $p = 0.006$). Gains concentrate on vision-dependent tasks: product defect reports improve by +38.5 pp and visual troubleshooting by +16.7 pp. This accuracy gain comes at a $1.8\times$ latency cost from native multimodal processing. These results suggest that routing is a first-order design variable in multi-agent systems, as it determines the information available for downstream reasoning.

---


### 49. [LLM-Enhanced Log Anomaly Detection: A Comprehensive Benchmark of Large Language Models for Automated System Diagnostics](https://arxiv.org/abs/2604.12218)

**<font color=#1a73e8>作者：</font>** Disha Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> System log anomaly detection is critical for maintaining the reliability of large-scale software systems, yet traditional methods struggle with the heterogeneous and evolving nature of modern log data. Recent advances in Large Language Models (LLMs) offer promising new approaches to log understanding, but a systematic comparison of LLM-based methods against established techniques remains lacking. In this paper, we present a comprehensive benchmark study evaluating both LLM-based and traditional approaches for log anomaly detection across four widely-used public datasets: HDFS, BGL, Thunderbird, and Spirit. We evaluate three categories of methods: (1) classical log parsers (Drain, Spell, AEL) combined with machine learning classifiers, (2) fine-tuned transformer models (BERT, RoBERTa), and (3) prompt-based LLM approaches (GPT-3.5, GPT-4, LLaMA-3) in zero-shot and few-shot settings. Our experiments reveal that while fine-tuned transformers achieve the highest F1-scores (0.96-0.99), prompt-based LLMs demonstrate remarkablezero-shot capabilities (F1: 0.82-0.91) without requiring any labeled training data -- a significant advantage for real-world deployment where labeled anomalies are scarce. We further analyze the cost-accuracy trade-offs, latency characteristics, and failure modes of each approach. Our findings provide actionable guidelines for practitioners choosing log anomaly detection methods based on their specific constraints regarding accuracy, latency, cost, and label availability. All code and experimental configurations are publicly available to facilitate reproducibility.

---


### 50. [LLM-Guided Semantic Bootstrapping for Interpretable Text Classification with Tsetlin Machines](https://arxiv.org/abs/2604.12223)

**<font color=#1a73e8>作者：</font>** Jiechao Gao, Rohan Kumar Yadav, Yuangang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained language models (PLMs) like BERT provide strong semantic representations but are costly and opaque, while symbolic models such as the Tsetlin Machine (TM) offer transparency but lack semantic generalization. We propose a semantic bootstrapping framework that transfers LLM knowledge into symbolic form, combining interpretability with semantic capacity. Given a class label, an LLM generates sub-intents that guide synthetic data creation through a three-stage curriculum (seed, core, enriched), expanding semantic diversity. A Non-Negated TM (NTM) learns from these examples to extract high-confidence literals as interpretable semantic cues. Injecting these cues into real data enables a TM to align clause logic with LLM-inferred semantics. Our method requires no embeddings or runtime LLM calls, yet equips symbolic models with pretrained semantic priors. Across multiple text classification tasks, it improves interpretability and accuracy over vanilla TM, achieving performance comparable to BERT while remaining fully symbolic and efficient.

---


### 51. [Designing Reliable LLM-Assisted Rubric Scoring for Constructed Responses: Evidence from Physics Exams](https://arxiv.org/abs/2604.12227)

**<font color=#1a73e8>作者：</font>** Xiuxiu Tang, G. Alex Ambrose, Ying Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Student responses in STEM assessments are often handwritten and combine symbolic expressions, calculations, and diagrams, creating substantial variation in format and interpretation. Despite their importance for evaluating students' reasoning, such responses are time-consuming to score and prone to rater inconsistency, particularly when partial credit is required. Recent advances in large language models (LLMs) have increased attention to AI-assisted scoring, yet evidence remains limited regarding how rubric design and LLM configurations influence reliability across performance levels. This study examined the reliability of AI-assisted scoring of undergraduate physics constructed responses using GPT-4o. Twenty authentic handwritten exam responses were scored across two rounds by four instructors and by the AI model using skill-based rubrics with differing levels of analytic granularity. Prompting format and temperature settings were systematically varied. Overall, human-AI agreement on total scores was comparable to human inter-rater reliability and was highest for high- and low-performing responses, but declined for mid-level responses involving partial or ambiguous reasoning. Criterion-level analyses showed stronger alignment for clearly defined conceptual skills than for extended procedural judgments. A more fine-grained, checklist-based rubric improved consistency relative to holistic scoring. These findings indicate that reliable AI-assisted scoring depends primarily on clear, well-structured rubrics, while prompting format plays a secondary role and temperature has relatively limited impact. More broadly, the study provides transferable design recommendations for implementing reliable LLM-assisted scoring in STEM contexts through skill-based rubrics and controlled LLM settings.

---


### 52. [HintMR: Eliciting Stronger Mathematical Reasoning in Small Language Models](https://arxiv.org/abs/2604.12229)

**<font color=#1a73e8>作者：</font>** Jawad Hossain, Xiangyu Guo, Jiawei Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) often struggle with complex mathematical reasoning due to limited capacity to maintain long chains of intermediate steps and to recover from early errors. We address this challenge by introducing a hint-assisted reasoning framework that incrementally guides SLMs through multi-step mathematical problem solving. Our approach decomposes solutions into sequential reasoning steps and provides context-aware hints, where hints are generated by a separate SLM trained via distillation from a strong large language model. While the hint-generating SLM alone is not capable of solving the problems, its collaboration with a reasoning SLM enables effective guidance, forming a cooperative two-model system for reasoning. Each hint is generated conditionally on the problem statement and the accumulated reasoning history, providing stepwise, localized guidance without revealing full solutions. This reduces error propagation and allows the reasoning model to focus on manageable subproblems. Experiments across diverse mathematical benchmarks and models demonstrate that hint assistance consistently improves reasoning accuracy for SLMs, yielding substantial gains over standard prompting while preserving model efficiency. These results highlight that structured collaboration between SLMs-via hint generation and reasoning-offers an effective and lightweight mechanism for enhancing mathematical reasoning.

---


### 53. [Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems](https://arxiv.org/abs/2604.12231)

**<font color=#1a73e8>作者：</font>** Tao Feng, Pengrui Han, Guanyu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have transformed AI research thanks to their powerful internal capabilities and knowledge. However, existing LLMs still fail to effectively incorporate the massive external knowledge when interacting with the world. Although retrieval-augmented LLMs are proposed to mitigate the issue, they are still fundamentally constrained by the context length of LLMs, as they can only retrieve top-K raw data chunks from the external knowledge base which often consists of millions of data chunks. Here we propose Thought-Retriever, a novel model-agnostic algorithm that helps LLMs generate output conditioned on arbitrarily long external data, without being constrained by the context length or number of retrieved data chunks. Our key insight is to let an LLM fully leverage its intermediate responses generated when solving past user queries (thoughts), filtering meaningless and redundant thoughts, organizing them in thought memory, and retrieving the relevant thoughts when addressing new queries. This effectively equips LLM-based agents with a self-evolving long-term memory that grows more capable through continuous interaction. Besides algorithmic innovation, we further meticulously prepare a novel benchmark, AcademicEval, which requires an LLM to faithfully leverage ultra-long context to answer queries based on real-world academic papers. Extensive experiments on AcademicEval and two other public datasets validate that Thought-Retriever remarkably outperforms state-of-the-art baselines, achieving an average increase of at least 7.6% in F1 score and 16% in win rate across various tasks. More importantly, we further demonstrate two exciting findings: (1) Thought-Retriever can indeed help LLM self-evolve after solving more user queries; (2) Thought-Retriever learns to leverage deeper thoughts to answer more abstract user queries.

---


### 54. [MolMem: Memory-Augmented Agentic Reinforcement Learning for Sample-Efficient Molecular Optimization](https://arxiv.org/abs/2604.12237)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Yibo Wen, Abhishek Pandy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In drug discovery, molecular optimization aims to iteratively refine a lead compound to improve molecular properties while preserving structural similarity to the original molecule. However, each oracle evaluation is expensive, making sample efficiency a key challenge for existing methods under a limited oracle budget. Trial-and-error approaches require many oracle calls, while methods that leverage external knowledge tend to reuse familiar templates and struggle on challenging objectives. A key missing piece is long-term memory that can ground decisions and provide reusable insights for future optimizations. To address this, we present MolMem (\textbf{Mol}ecular optimization with \textbf{Mem}ory), a multi-turn agentic reinforcement learning (RL) framework with a dual-memory system. Specifically, MolMem uses Static Exemplar Memory to retrieve relevant exemplars for cold-start grounding, and Evolving Skill Memory to distill successful trajectories into reusable strategies. Built on this memory-augmented formulation, we train the policy with dense step-wise rewards, turning costly rollouts into long-term knowledge that improves future optimization. Extensive experiments show that MolMem achieves 90\% success on single-property tasks (1.5$\times$ over the best baseline) and 52\% on multi-property tasks using only 500 oracle calls. Our code is available at this https URL.

---


### 55. [Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown](https://arxiv.org/abs/2604.12245)

**<font color=#1a73e8>作者：</font>** Sandra Gómez-Gálvez, Tobias Olenyi, Gillian Dobbie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks, despite their high accuracy, often exhibit poor confidence calibration, limiting their reliability in high-stakes applications. Current ad-hoc confidence calibration methods attempt to fix this during training but face a fundamental trade-off: two-phase training methods achieve strong classification performance at the cost of training instability and poorer confidence calibration, while single-loss methods are stable but underperform in classification. This paper addresses and mitigates this stability-performance trade-off. We propose Socrates Loss, a novel, unified loss function that explicitly leverages uncertainty by incorporating an auxiliary unknown class, whose predictions directly influence the loss function and a dynamic uncertainty penalty. This unified objective allows the model to be optimized for both classification and confidence calibration simultaneously, without the instability of complex, scheduled losses. We provide theoretical guarantees that our method regularizes the model to prevent miscalibration and overfitting. Across four benchmark datasets and multiple architectures, our comprehensive experiments demonstrate that Socrates Loss consistently improves training stability while achieving more favorable accuracy-calibration trade-off, often converging faster than existing methods.

---


### 56. [SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration](https://arxiv.org/abs/2604.12247)

**<font color=#1a73e8>作者：</font>** Zhuofan Wen, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has emerged as a promising approach to accelerate autoregressive inference in large language models (LLMs). Self-draft methods, which leverage the base LLM itself for speculation, avoid the overhead of auxiliary draft models but face limitations: shallow layers often produce overconfident yet incorrect token predictions, and the presence of difficult tokens in a draft sequence forces redundant computation through deeper layers, undermining both draft acceptance and overall speedup. To address these issues, we propose a novel self-draft framework that suppresses spurious confidence via layer-wise temperature annealing in early-exit decision and adaptively bounds speculation length based on token-wise decoding difficulty. By reprocessing the hidden states of draft tokens in a unified parallel pass through deep layers, our method maintains exact output equivalence with the original model while maximizing computational efficiency. It requires no modifications to the base LLM parameters and achieves up to 2.33x wall-time speedup over standard autoregressive decoding across diverse long-form generation tasks and multiple model architectures.

---


### 57. [How memory can affect collective and cooperative behaviors in an LLM-Based Social Particle Swarm](https://arxiv.org/abs/2604.12250)

**<font color=#1a73e8>作者：</font>** Taisei Hishiki, Takaya Arita, Reiji Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study examines how model-specific characteristics of Large Language Model (LLM) agents, including internal alignment, shape the effect of memory on their collective and cooperative dynamics in a multi-agent system. To this end, we extend the Social Particle Swarm (SPS) model, in which agents move in a two-dimensional space and play the Prisoner's Dilemma with neighboring agents, by replacing its rule-based agents with LLM agents endowed with Big Five personality scores and varying memory lengths. Using Gemini-2.0-Flash, we find that memory length is a critical parameter governing collective behavior: even a minimal memory drastically suppressed cooperation, transitioning the system from stable cooperative clusters through cyclical formation and collapse of clusters to a state of scattered defection as memory length increased. Big Five personality traits correlated with agent behaviors in partial agreement with findings from experiments with human participants, supporting the validity of the model. Comparative experiments using Gemma~3:4b revealed the opposite trend: longer memory promoted cooperation, accompanied by the formation of dense cooperative clusters. Sentiment analysis of agents' reasoning texts showed that Gemini interprets memory increasingly negatively as its length grows, while Gemma interprets it less negatively, and that this difference persists in the early phase of experiments before the macro-level dynamics converge. These results suggest that model-specific characteristics of LLMs, potentially including alignment, play a fundamental role in determining emergent social behavior in Generative Agent-Based Modeling, and provide a micro-level cognitive account of the contradictions found in prior work on memory and cooperation.

---


### 58. [A Scoping Review of Large Language Model-Based Pedagogical Agents](https://arxiv.org/abs/2604.12253)

**<font color=#1a73e8>作者：</font>** Shan Li, Juan Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This scoping review examines the emerging field of Large Language Model (LLM)-based pedagogical agents in educational settings. While traditional pedagogical agents have been extensively studied, the integration of LLMs represents a transformative advancement with unprecedented capabilities in natural language understanding, reasoning, and adaptation. Following PRISMA-ScR guidelines, we analyzed 52 studies across five major databases from November 2022 to January 2025. Our findings reveal diverse LLM-based agents spanning K-12, higher education, and informal learning contexts across multiple subject domains. We identified four key design dimensions characterizing these agents: interaction approach (reactive vs. proactive), domain scope (domain-specific vs. general-purpose), role complexity (single-role vs. multi-role), and system integration (standalone vs. integrated). Emerging trends include multi-agent systems that simulate naturalistic learning environments, virtual student simulation for agent evaluation, integration with immersive technologies, and combinations with learning analytics. We also discuss significant research gaps and ethical considerations regarding privacy, accuracy, and student autonomy. This review provides researchers and practitioners with a comprehensive understanding of LLM-based pedagogical agents while identifying crucial areas for future development in this rapidly evolving field.

---


### 59. [Coding-Free and Privacy-Preserving MCP Framework for Clinical Agentic Research Intelligence System](https://arxiv.org/abs/2604.12258)

**<font color=#1a73e8>作者：</font>** Taehun Kim, Hyeryun Park, Hyeonhoon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical research involves labor-intensive processes such as study design, cohort construction, model development, and documentation, requiring domain expertise, programming skills, and access to sensitive patient data. These demands create barriers for clinicians and external researchers conducting data-driven studies. To overcome these limitations, we developed a Clinical Agentic Research Intelligence System (CARIS) that automates the clinical research workflow while preserving data privacy, enabling comprehensive studies without direct access to raw data. CARIS integrates Large Language Models (LLMs) with modular tools via the Model Context Protocol (MCP), enabling natural language-driven orchestration of appropriate tools. Databases remain securely within the MCP server, and users access only the outputs and final research reports. Based on user intent, CARIS automatically executes the full pipeline: research planning, literature search, cohort construction, Institutional Review Board (IRB) documentation, Vibe Machine Learning (ML), and report generation, with iterative human-in-the-loop refinement. We evaluated CARIS on three heterogeneous datasets with distinct clinical tasks. Research plans and IRB documents were finalized within three to four iterations, using evidence from literature and data. The system supported Vibe ML by exploring feature-model combinations, ranking the top ten models, and generating performance visualizations. Final reports showed high completeness based on a checklist derived from the TRIPOD+AI framework, achieving 96% coverage in LLM evaluation and 82% in human evaluation. CARIS demonstrates that agentic AI can transform clinical hypotheses into executable research workflows across heterogeneous datasets. By eliminating the need for coding and direct data access, the system lowers barriers and bridges public and private clinical data environments.

---


### 60. [CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades](https://arxiv.org/abs/2604.12262)

**<font color=#1a73e8>作者：</font>** Raeyoung Chang, Dongwook Kwon, Jisoo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cascaded LLM systems coordinate models of varying sizes with human experts to balance accuracy, cost, and abstention under uncertainty. However, single-model tiers at each stage often struggle with ambiguous queries, triggering premature escalations to costlier models or experts due to under-confidence and inefficient compute scaling. CascadeDebate addresses this gap by inserting multi-agent deliberation directly at each tier's escalation boundary. Confidence-based routers activate lightweight agent ensembles only for uncertain cases, enabling consensus-driven resolution of ambiguities internally without invoking higher-cost upgrades. Our unified architecture alternates single-model inference with selective multi-agent deliberation across model scales, culminating in human experts as the final fallback. This design scales test-time compute dynamically according to query difficulty. Across five benchmarks spanning science, medicine, and general knowledge, CascadeDebate outperforms strong single-model cascades and standalone multi-agent systems by up to 26.75 percent. An online threshold optimizer proves essential, boosting accuracy by 20.98 to 52.33 percent relative improvement over fixed policies and enabling elastic adaptation to real-world distributions.

---


### 61. [RoleMAG: Learning Neighbor Roles in Multimodal Graphs](https://arxiv.org/abs/2604.12271)

**<font color=#1a73e8>作者：</font>** Yilong Zuo, Xunkai Li, Zhihan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal attributed graphs (MAGs) combine multimodal node attributes with structured relations. However, existing methods usually perform shared message passing on a single graph and implicitly assume that the same neighbors are equally useful for all modalities. In practice, neighbors that benefit one modality may interfere with another, blurring modality-specific signals under shared propagation. To address this issue, we propose RoleMAG, a multimodal graph framework that learns how different neighbors should participate in propagation. Concretely, RoleMAG distinguishes whether a neighbor should provide shared, complementary, or heterophilous signals, and routes them through separate propagation channels. This enables cross-modal completion from complementary neighbors while keeping heterophilous ones out of shared smoothing. Extensive experiments on three graph-centric MAG benchmarks show that RoleMAG achieves the best results on RedditS and Bili\_Dance, while remaining competitive on Toys. Ablation, robustness, and efficiency analyses further support the effectiveness of the proposed role-aware propagation design. Our code is available at this https URL

---


### 62. [Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning](https://arxiv.org/abs/2604.12282)

**<font color=#1a73e8>作者：</font>** Houxing Ren, Mingjie Zhan, Zimu Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spreadsheets are central to real-world applications such as enterprise reporting, auditing, and scientific data management. Despite their ubiquity, existing large language model based approaches typically treat tables as plain text, overlooking critical layout cues and visual semantics. Moreover, real-world spreadsheets are often massive in scale, exceeding the input length that LLMs can efficiently process. To address these challenges, we propose SpreadsheetAgent, a two-stage multi-agent framework for spreadsheet understanding that adopts a step-by-step reading and reasoning paradigm. Instead of loading the entire spreadsheet at once, SpreadsheetAgent incrementally interprets localized regions through multiple modalities, including code execution results, images, and LaTeX tables. The method first constructs a structural sketch and row/column summaries, and then performs task-driven reasoning over this intermediate representation in the Solving Stage. To further enhance reliability, we design a verification module that validates extracted structures via targeted inspections, reducing error propagation and ensuring trustworthy inputs for downstream reasoning. Extensive experiments on two spreadsheet datasets demonstrate the effectiveness of our approach. With GPT-OSS-120B, SpreadsheetAgent achieves 38.16% on Spreadsheet Bench, outperforming the ChatGPT Agent baseline (35.27%) by 2.89 absolute points. These results highlight the potential of SpreadsheetAgent to advance robust and scalable spreadsheet understanding in real-world applications. Code is available at this https URL.

---


### 63. [GAM: Hierarchical Graph-based Agentic Memory for LLM Agents](https://arxiv.org/abs/2604.12285)

**<font color=#1a73e8>作者：</font>** Zhaofen Wu, Hanrong Zhang, Fulin Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to evolving narratives. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in an event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a graph-guided, multi-factor retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and efficiency.

---


### 64. [Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization](https://arxiv.org/abs/2604.12290)

**<font color=#1a73e8>作者：</font>** Yizhe Chi, Deyao Hong, Dapeng Jiang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current LLM agent benchmarks, which predominantly focus on binary pass/fail tasks such as code generation or search-based question answering, often neglect the value of real-world engineering that is often captured through the iterative optimization of feasible designs. To this end, we introduce Frontier-Eng, a human-verified benchmark for generative optimization -- an iterative propose-execute-evaluate loop in which an agent generates candidate artifacts, receives executable verifier feedback, and revises them under a fixed interaction budget -- spanning $47$ tasks across five broad engineering categories. Unlike previous suites, Frontier-Eng tasks are grounded in industrial-grade simulators and verifiers that provide continuous reward signals and enforce hard feasibility constraints under constrained budgets. We evaluate eight frontier language models using representative search frameworks, finding that while Claude 4.6 Opus achieves the most robust performance, the benchmark remains challenging for all models. Our analysis suggests a dual power-law decay in improvement frequency ($\sim$ 1/iteration) and magnitude ($\sim$ 1/improvement count). We further show that although width improves parallelism and diversity, depth remains crucial for hard-won improvements under a fixed budget. Frontier-Eng establishes a new standard for assessing the capacity of AI agents to integrate domain knowledge with executable feedback to solve complex, open-ended engineering problems.

---


### 65. [GCA Framework: A Gulf-Grounded Dataset and Agentic Pipeline for Climate Decision Support](https://arxiv.org/abs/2604.12306)

**<font color=#1a73e8>作者：</font>** Muhammad Umer Sheikh, Khawar Shehzad, Salman Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate decision-making in the Gulf increasingly demands systems that can translate heterogeneous scientific and policy evidence into actionable guidance, yet general-purpose large language models (LLMs) remain weak both in region-specific climate knowledge and grounded interaction with geospatial and forecasting tools. We present the GCA framework, which unifies (i) GCA-DS, a curated Gulf-focused multimodal dataset, and (ii) Gulf Climate Agent (GCA), a tool-augmented agent for climate analysis. GCA-DS comprises ~200k question-answer pairs spanning governmental policies and adaptation plans, NGO and international frameworks, academic literature, and event-driven reporting on heatwaves, dust storms, and floods, complemented with remote-sensing inputs that couple imagery with textual evidence. Building on this foundation, the GCA agent orchestrates a modular tool pipeline grounded in real-time and historical signals and geospatial processing that produces derived indices and interpretable visualizations. Finally, we benchmark open and proprietary LLMs on Gulf climate tasks and show that domain fine-tuning and tool integration substantially improve reliability over general-purpose baselines.

---


### 66. [ContextLens: Modeling Imperfect Privacy and Safety Context for Legal Compliance](https://arxiv.org/abs/2604.12308)

**<font color=#1a73e8>作者：</font>** Haoran Li, Yulin Chen, Huihao Jing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Individuals' concerns about data privacy and AI safety are highly contextualized and extend beyond sensitive patterns. Addressing these issues requires reasoning about the context to identify and mitigate potential risks. Though researchers have widely explored using large language models (LLMs) as evaluators for contextualized safety and privacy assessments, these efforts typically assume the availability of complete and clear context, whereas real-world contexts tend to be ambiguous and incomplete. In this paper, we propose ContextLens, a semi-rule-based framework that leverages LLMs to ground the input context in the legal domain and explicitly identify both known and unknown factors for legal compliance. Instead of directly assessing safety outcomes, our ContextLens instructs LLMs to answer a set of crafted questions that span over applicability, general principles and detailed provisions to assess compliance with pre-defined priorities and rules. We conduct extensive experiments on existing compliance benchmarks that cover the General Data Protection Regulation (GDPR) and the EU AI Act. The results suggest that our ContextLens can significantly improve LLMs' compliance assessment and surpass existing baselines without any training. Additionally, our ContextLens can further identify the ambiguous and missing factors.

---


### 67. [CompliBench: Benchmarking LLM Judges for Compliance Violation Detection in Dialogue Systems](https://arxiv.org/abs/2604.12312)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Guanyu Yao, Bairu Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed as task-oriented agents in enterprise environments, ensuring their strict adherence to complex, domain-specific operational guidelines is critical. While utilizing an LLM-as-a-Judge is a promising solution for scalable evaluation, the reliability of these judges in detecting specific policy violations remains largely unexplored. This gap is primarily due to the lack of a systematic data generation method, which has been hindered by the extensive cost of fine-grained human annotation and the difficulty of synthesizing realistic agent violations. In this paper, we introduce CompliBench, a novel benchmark designed to evaluate the ability of LLM judges to detect and localize guideline violations in multi-turn dialogues. To overcome data scarcity, we develop a scalable, automated data generation pipeline that simulates user-agent interactions. Our controllable flaw injection process automatically yields precise ground-truth labels for the violated guideline and the exact conversation turn, while an adversarial search method ensures these introduced perturbations are highly challenging. Our comprehensive evaluation reveals that current state-of-the-art proprietary LLMs struggle significantly with this task. In addition, we demonstrate that a small-scale judge model fine-tuned on our synthesized data outperforms leading LLMs and generalizes well to unseen business domains, highlighting our pipeline as an effective foundation for training robust generative reward models.

---


### 68. [RSGMamba: Reliability-Aware Self-Gated State Space Model for Multimodal Semantic Segmentation](https://arxiv.org/abs/2604.12319)

**<font color=#1a73e8>作者：</font>** Guoan Xu, Yang Xiao, Guangwei Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal semantic segmentation has emerged as a powerful paradigm for enhancing scene understanding by leveraging complementary information from multiple sensing modalities (e.g., RGB, depth, and thermal). However, existing cross-modal fusion methods often implicitly assume that all modalities are equally reliable, which can lead to feature degradation when auxiliary modalities are noisy, misaligned, or incomplete. In this paper, we revisit cross-modal fusion from the perspective of modality reliability and propose a novel framework termed the Reliability-aware Self-Gated State Space Model (RSGMamba). At the core of our method is the Reliability-aware Self-Gated Mamba Block (RSGMB), which explicitly models modality reliability and dynamically regulates cross-modal interactions through a self-gating mechanism. Unlike conventional fusion strategies that indiscriminately exchange information across modalities, RSGMB enables reliability-aware feature selection and enhancing informative feature aggregation. In addition, a lightweight Local Cross-Gated Modulation (LCGM) is incorporated to refine fine-grained spatial details, complementing the global modeling capability of RSGMB. Extensive experiments demonstrate that RSGMamba achieves state-of-the-art performance on both RGB-D and RGB-T semantic segmentation benchmarks, resulting 58.8% / 54.0% mIoU on NYUDepth V2 and SUN-RGBD (+0.4% / +0.7% over prior best), and 61.1% / 88.9% mIoU on MFNet and PST900 (up to +1.6%), with only 48.6M parameters, thereby validating the effectiveness and superiority of the proposed approach.

---


### 69. [All in One: A Unified Synthetic Data Pipeline for Multimodal Video Understanding](https://arxiv.org/abs/2604.12335)

**<font color=#1a73e8>作者：</font>** Tanzila Rahman, Renjie Liao, Leonid Sigal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training multimodal large language models (MLLMs) for video understanding requires large-scale annotated data spanning diverse tasks such as object counting, question answering, and segmentation. However, collecting and annotating multimodal video data in real-world is costly, slow, and inherently limited in diversity and coverage. To address this challenge, we propose a unified synthetic data generation pipeline capable of automatically producing unlimited multimodal video data with rich and diverse supervision. Our framework supports multiple task formats within a single pipeline, enabling scalable and consistent data creation across tasks. To further enhance reasoning ability, we introduce a VQA-based fine-tuning strategy that trains models to answer structured questions about visual content rather than relying solely on captions or simple instructions. This formulation encourages deeper visual grounding and reasoning. We evaluate our approach in three challenging tasks: video object counting, video-based visual question answering, and video object segmentation. Experimental results demonstrate that models trained predominantly on synthetic data generalize effectively to real-world datasets, often outperforming traditionally trained counterparts. Our findings highlight the potential of unified synthetic data pipelines as a scalable alternative to expensive real-world annotation for multimodal video understanding.

---


### 70. [Identifying and Mitigating Gender Cues in Academic Recommendation Letters: An Interpretability Case Study](https://arxiv.org/abs/2604.12337)

**<font color=#1a73e8>作者：</font>** Charlotte S. Alexander, Shane Storks, Souradip Pal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Letters of recommendation (LoRs) can carry patterns of implicitly gendered language that can inadvertently influence downstream decisions, e.g. in hiring and admissions. In this work, we investigate the extent to which Transformer-based encoder models as well as Large Language Models (LLMs) can infer the gender of applicants in academic LoRs submitted to an U.S. medical-residency program after explicit identifiers like names and pronouns are de-gendered. While using three models (DistilBERT, RoBERTa, and Llama 2) to classify the gender of anonymized and de-gendered LoRs, significant gender leakage was observed as evident from up to 68% classification accuracy. Text interpretation methods, like TF-IDF and SHAP, demonstrate that certain linguistic patterns are strong proxies for gender, e.g. "emotional'' and "humanitarian'' are commonly associated with LoRs from female applicants. As an experiment in creating truly gender-neutral LoRs, these implicit gender cues were remove resulting in a drop of up to 5.5% accuracy and 2.7% macro $F_1$ score on re-training the classifiers. However, applicant gender prediction still remains better than chance. In this case study, our findings highlight that 1) LoRs contain gender-identifying cues that are hard to remove and may activate bias in decision-making and 2) while our technical framework may be a concrete step toward fairer academic and professional evaluations, future work is needed to interrogate the role that gender plays in LoR review. Taken together, our findings motivate upstream auditing of evaluative text in real-world academic letters of recommendation as a necessary complement to model-level fairness interventions.

---


### 71. [Bridging the Micro--Macro Gap: Frequency-Aware Semantic Alignment for Image Manipulation Localization](https://arxiv.org/abs/2604.12341)

**<font color=#1a73e8>作者：</font>** Xiaojie Liang, Zhimin Chen, Ziqi Sheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative image editing advances, image manipulation localization (IML) must handle both traditional manipulations with conspicuous forensic artifacts and diffusion-generated edits that appear locally realistic. Existing methods typically rely on either low-level forensic cues or high-level semantics alone, leading to a fundamental micro--macro gap. To bridge this gap, we propose FASA, a unified framework for localizing both traditional and diffusion-generated manipulations. Specifically, we extract manipulation-sensitive frequency cues through an adaptive dual-band DCT module and learn manipulation-aware semantic priors via patch-level contrastive alignment on frozen CLIP representations. We then inject these priors into a hierarchical frequency pathway through a semantic-frequency side adapter for multi-scale feature interaction, and employ a prototype-guided, frequency-gated mask decoder to integrate semantic consistency with boundary-aware localization for tampered region prediction. Extensive experiments on OpenSDI and multiple traditional manipulation benchmarks demonstrate state-of-the-art localization performance, strong cross-generator and cross-dataset generalization, and robust performance under common image degradations.

---


### 72. [Scaffold-Conditioned Preference Triplets for Controllable Molecular Optimization with Large Language Models](https://arxiv.org/abs/2604.12350)

**<font color=#1a73e8>作者：</font>** Yi Xiong, Liang Xiong, Xiaohong Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property optimization is central to drug discovery, yet many deep learning methods rely on black-box scoring and offer limited control over scaffold preservation, often producing unstable or biologically implausible edits. While large language models (LLMs) are promising molecular generators, optimization remains constrained by the lack of chemistry-grounded preference supervision and principled data curation. We introduce \textbf{Scaffold-Conditioned Preference Triplets (SCPT)}, a pipeline that constructs similarity-constrained triplets $\langle\text{scaffold}, \text{better}, \text{worse}\rangle$ via scaffold alignment and chemistry-driven filters for validity, synthesizability, and meaningful property gains. Using these preferences, we align a pretrained molecular LLM as a conditional editor, enabling property-improving edits that retain the scaffold. Across single- and multi-objective benchmarks, SCPT improves optimization success and property gains while maintaining higher scaffold similarity than competitive baselines. Compared with representative non-LLM molecular optimization methods, SCPT-trained LLMs are better suited to scaffold-constrained and multi-objective optimization. In addition, models trained on single-property and two-property supervision generalize effectively to three-property tasks, indicating promising extrapolative generalization under limited higher-order supervision. SCPT also provides controllable data-construction knobs that yield a predictable similarity-gain frontier, enabling systematic adaptation to diverse optimization regimes.

---


### 73. [MultiDocFusion: Hierarchical and Multimodal Chunking Pipeline for Enhanced RAG on Long Industrial Documents](https://arxiv.org/abs/2604.12352)

**<font color=#1a73e8>作者：</font>** Joongmin Shin, Chanjun Park, Jeongbae Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RAG-based QA has emerged as a powerful method for processing long industrial documents. However, conventional text chunking approaches often neglect complex and long industrial document structures, causing information loss and reduced answer quality. To address this, we introduce MultiDocFusion, a multimodal chunking pipeline that integrates: (i) detection of document regions using vision-based document parsing, (ii) text extraction from these regions via OCR, (iii) reconstruction of document structure into a hierarchical tree using large language model (LLM)-based document section hierarchical parsing (DSHP-LLM), and (iv) construction of hierarchical chunks through DFS-based grouping. Extensive experiments across industrial benchmarks demonstrate that MultiDocFusion improves retrieval precision by 8-15% and ANLS QA scores by 2-3% compared to baselines, emphasizing the critical role of explicitly leveraging document hierarchy for multimodal document-based QA. These significant performance gains underscore the necessity of structure-aware chunking in enhancing the fidelity of RAG-based QA systems.

---


### 74. [ReflectCAP: Detailed Image Captioning with Reflective Memory](https://arxiv.org/abs/2604.12357)

**<font color=#1a73e8>作者：</font>** Kyungmin Min, Minbeom Kim, Kang-il Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detailed image captioning demands both factual grounding and fine-grained coverage, yet existing methods have struggled to achieve them simultaneously. We address this tension with Reflective Note-Guided Captioning (ReflectCAP), where a multi-agent pipeline analyzes what the target large vision-language model (LVLM) consistently hallucinates and what it systematically overlooks, distilling these patterns into reusable guidelines called Structured Reflection Notes. At inference time, these notes steer the captioning model along both axes -- what to avoid and what to attend to -- yielding detailed captions that jointly improve factuality and coverage. Applying this method to 8 LVLMs spanning the GPT-4.1 family, Qwen series, and InternVL variants, ReflectCAP reaches the Pareto frontier of the trade-off between factuality and coverage, and delivers substantial gains on CapArena-Auto, where generated captions are judged head-to-head against strong reference models. Moreover, ReflectCAP offers a more favorable trade-off between caption quality and compute cost than model scaling or existing multi-agent pipelines, which incur 21--36\% greater overhead. This makes high-quality detailed captioning viable under real-world cost and latency constraints.

---


### 75. [Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding](https://arxiv.org/abs/2604.12358)

**<font color=#1a73e8>作者：</font>** Jiwan Kim, Kibum Kim, Wonjoong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, visual token pruning has been studied to handle the vast number of visual tokens in Multimodal Large Language Models. However, we observe that while existing pruning methods perform reliably on simple visual understanding, they struggle to effectively generalize to complex visual reasoning tasks, a critical gap underexplored in previous studies. Through a systematic analysis, we identify Relevant Visual Information Shift (RVIS) during decoding as the primary failure driver. To address this, we propose Decoding-stage Shift-aware Token Pruning (DSTP), a training-free add-on framework that enables existing pruning methods to align visual tokens with shifting reasoning requirements during the decoding stage. Extensive experiments demonstrate that DSTP significantly mitigates performance degradation of pruning methods in complex reasoning tasks, while consistently yielding performance gains even across visual understanding benchmarks. Furthermore, DSTP demonstrates effectiveness across diverse state-of-the-art architectures, highlighting its generalizability and efficiency with minimal computational overhead.

---


### 76. [Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models](https://arxiv.org/abs/2604.12371)

**<font color=#1a73e8>作者：</font>** Ravikumar Balakrishnan, Sanket Mendapara, Ankit Garg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study typographic prompt injection attacks on vision-language models (VLMs), where adversarial text is rendered as images to bypass safety mechanisms, posing a growing threat as VLMs serve as the perceptual backbone of autonomous agents, from browser automation and computer-use systems to camera-equipped embodied agents. In practice, the attack surface is heterogeneous: adversarial text appears at varying font sizes and under diverse visual conditions, while the growing ecosystem of VLMs exhibits substantial variation in vulnerability, complicating defensive approaches. Evaluating 1,000 prompts from SALAD-Bench across four VLMs, namely, GPT-4o, Claude Sonnet 4.5, Mistral-Large-3, and Qwen3-VL-4B-Instruct under varying font sizes (6--28px) and visual transformations (rotation, blur, noise, contrast changes), we find: (1) font size significantly affects attack success rate (ASR), with very small fonts (6px) yielding near-zero ASR while mid-range fonts achieve peak effectiveness; (2) text attacks are more effective than image attacks for GPT-4o (36% vs 8%) and Claude (47% vs 22%), while Qwen3-VL and Mistral show comparable ASR across modalities; (3) text-image embedding distance from two multimodal embedding models (JinaCLIP and Qwen3-VL-Embedding) shows strong negative correlation with ASR across all four models (r = -0.71 to -0.93, p < 0.01); (4) heavy degradations increase embedding distance by 10--12% and reduce ASR by 34--96%, while rotation asymmetrically affects models (Mistral drops 50%, GPT-4o unchanged). These findings highlight that model-specific robustness patterns preclude one-size-fits-all defenses and offer empirical guidance for practitioners selecting VLM backbones for agentic systems operating in adversarial environments.

---


### 77. [Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](https://arxiv.org/abs/2604.12373)

**<font color=#1a73e8>作者：</font>** Tomer Ashuach, Liat Ein-Dor, Shai Gretz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans use introspection to evaluate their understanding through private internal states inaccessible to external observers. We investigate whether large language models possess similar privileged knowledge about answer correctness, information unavailable through external observation. We train correctness classifiers on question representations from both a model's own hidden states and external models, testing whether self-representations provide a performance advantage. On standard evaluation, we find no advantage: self-probes perform comparably to peer-model probes. We hypothesize this is due to high inter-model agreement of answer correctness. To isolate genuine privileged knowledge, we evaluate on disagreement subsets, where models produce conflicting predictions. Here, we discover domain-specific privileged knowledge: self-representations consistently outperform peer representations in factual knowledge tasks, but show no advantage in math reasoning. We further localize this domain asymmetry across model layers, finding that the factual advantage emerges progressively from early-to-mid layers onward, consistent with model-specific memory retrieval, while math reasoning shows no consistent advantage at any depth.

---


### 78. [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374)

**<font color=#1a73e8>作者：</font>** NVIDIA, Aakshita Chandiramani, Aaron Blakeman 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We describe the pre-training, post-training, and quantization of Nemotron 3 Super, a 120 billion (active 12 billion) parameter hybrid Mamba-Attention Mixture-of-Experts model. Nemotron 3 Super is the first model in the Nemotron 3 family to 1) be pre-trained in NVFP4, 2) leverage LatentMoE, a new Mixture-of-Experts architecture that optimizes for both accuracy per FLOP and accuracy per parameter, and 3) include MTP layers for inference acceleration through native speculative decoding. We pre-trained Nemotron 3 Super on 25 trillion tokens followed by post-training using supervised fine tuning (SFT) and reinforcement learning (RL). The final model supports up to 1M context length and achieves comparable accuracy on common benchmarks, while also achieving up to 2.2x and 7.5x higher inference throughput compared to GPT-OSS-120B and Qwen3.5-122B, respectively. Nemotron 3 Super datasets, along with the base, post-trained, and quantized checkpoints, are open-sourced on HuggingFace.

---


### 79. [Cooperative Memory Paging with Keyword Bookmarks for Long-Horizon LLM Conversations](https://arxiv.org/abs/2604.12376)

**<font color=#1a73e8>作者：</font>** Ziyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When LLM conversations grow beyond the context window, old content must be evicted -- but how does the model recover it when needed? We propose cooperative paging: evicted segments are replaced with minimal keyword bookmarks ([pN:keywords], ~8-24 tokens each), and the model is given a recall() tool to retrieve full content on demand. On the LoCoMo benchmark (10 real multi-session conversations, 300+ turns), cooperative paging achieves the highest answer quality among six methods -- outperforming truncation, BM25, word-overlap retrieval, a search-tool baseline, and full context -- on four models (GPT-4o-mini, DeepSeek-v3.2, Claude Haiku, GLM-5), confirmed by four independent LLM judges ($p=0.017$, paired bootstrap). We then study the paging design space with a 5x4 ablation over boundary strategies and eviction policies (3,176 synthetic probes, 1,600 LoCoMo probes). Key findings: (1) coarse fixed-size pages (fixed_20) reach 96.7% while content-aware topic_shift collapses to 56.7%; (2) eviction policy choice is data-dependent (FIFO best on synthetic, LFU on LoCoMo); (3) two bookmark generation strategies improve over the heuristic baseline (+4.4 and +8.7 E2E points); (4) the remaining bottleneck is bookmark discrimination -- the model triggers recall() 96% of the time but selects the correct page only 57% when bookmarks are insufficiently distinctive. Keyword specificity alone accounts for a 25 percentage point accuracy difference.

---


### 80. [SCRIPT: A Subcharacter Compositional Representation Injection Module for Korean Pre-Trained Language Models](https://arxiv.org/abs/2604.12377)

**<font color=#1a73e8>作者：</font>** SungHo Kim, Juhyeong Park, Eda Atalay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean is a morphologically rich language with a featural writing system in which each character is systematically composed of subcharacter units known as Jamo. These subcharacters not only determine the visual structure of Korean but also encode frequent and linguistically meaningful morphophonological processes. However, most current Korean language models (LMs) are based on subword tokenization schemes, which are not explicitly designed to capture the internal compositional structure of characters. To address this limitation, we propose SCRIPT, a model-agnostic module that injects subcharacter compositional knowledge into Korean PLMs. SCRIPT allows to enhance subword embeddings with structural granularity, without requiring architectural changes or additional pre-training. As a result, SCRIPT enhances all baselines across various Korean natural language understanding (NLU) and generation (NLG) tasks. Moreover, beyond performance gains, detailed linguistic analyses show that SCRIPT reshapes the embedding space in a way that better captures grammatical regularities and semantically cohesive variations. Our code is available at this https URL.

---


### 81. [ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance](https://arxiv.org/abs/2604.12378)

**<font color=#1a73e8>作者：</font>** Daniil Gurgurov, Tom Röhr, Sebastian von Rohrscheidt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in multilingual capabilities, most large language models (LLMs) remain English-centric in their training and, crucially, in their production of reasoning traces. Even when tasked with non-English problems, these models predominantly reason in English, creating a fundamental mismatch for non-English usage scenarios.
We address this disparity directly with three contributions. (i) We introduce ReasonXL, the first large-scale parallel corpus of cross-domain reasoning traces spanning five European languages (English, German, French, Italian, and Spanish), with over two million aligned samples per language, each comprising prompts, reasoning traces, and final outputs, enabling direct supervision of language-specific reasoning. (ii) Using ReasonXL, we demonstrate that LLMs can be adapted to reason entirely in a desired target language, using a simple two-stage pipeline of supervised fine-tuning (SFT) followed by reinforcement learning with verifiable rewards (RLVR). The resulting models match or exceed baseline performance, with minimal loss in general knowledge and broadly preserved cross-lingual transfer. (iii) We conduct an extensive representational analysis of the adaptation and find a clear functional division across model depth: early layers contain an activation bottleneck that causally determines language identity, while upper layers concentrate the weight and activation changes driven by adaptation. We further find that RLVR achieves greater behavioral divergence from the base model with smaller parameter updates than SFT, suggesting a more efficient representational rerouting despite much smaller weight updates.

---


### 82. [Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints](https://arxiv.org/abs/2604.12384)

**<font color=#1a73e8>作者：</font>** Songping Peng, Zhiheng Zhang, Daojian Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment in Large Language Models (LLMs) remains highly fragile during fine-tuning, where even benign adaptation can degrade pre-trained refusal behaviors and enable harmful responses. Existing defenses typically constrain either weights or activations in isolation, without considering their coupled effects on safety. In this paper, we first theoretically demonstrate that constraining either weights or activations alone is insufficient for safety preservation. To robustly preserve safety alignment, we propose Coupled Weight and Activation Constraints (CWAC), a novel approach that simultaneously enforces a precomputed safety subspace on weight updates and applies targeted regularization to safety-critical features identified by sparse autoencoders. Extensive experiments across four widely used LLMs and diverse downstream tasks show that CWAC consistently achieves the lowest harmful scores with minimal impact on fine-tuning accuracy, substantially outperforming strong baselines even under high harmful data ratios.

---


### 83. [From Myopic Selection to Long-Horizon Awareness: Sequential LLM Routing for Multi-Turn Dialogue](https://arxiv.org/abs/2604.12385)

**<font color=#1a73e8>作者：</font>** Jiarui Zhang, Xiangyu Liu, Yong Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn dialogue is the predominant form of interaction with large language models (LLMs). While LLM routing is effective in single-turn settings, existing methods fail to maximize cumulative performance in multi-turn dialogue due to interaction dynamics and delayed rewards. To address this challenge, we move from myopic, single-turn selection to long-horizon sequential routing for multi-turn dialogue. Accordingly, we propose DialRouter, which first performs MCTS to explore dialogue branches induced by different LLM selections and collect trajectories with high cumulative rewards. DialRouter then learns a lightweight routing policy from search-derived data, augmented with retrieval-based future state approximation, enabling multi-turn routing without online search. Experiments on both open-domain and domain-specific dialogue tasks across diverse candidate sets of both open-source and closed-source LLMs demonstrate that DialRouter significantly outperforms single LLMs and existing routing baselines in task success rate, while achieving a superior performance-cost trade-off when combined with a cost-aware reward.

---


### 84. [Heuristic Classification of Thoughts Prompting (HCoT): Integrating Expert System Heuristics for Structured Reasoning into Large Language Models](https://arxiv.org/abs/2604.12390)

**<font color=#1a73e8>作者：</font>** Lei Lin, Jizhao Zhu, Yong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses two limitations of large language models (LLMs) in solving complex problems: (1) their reasoning processes exhibit Bayesian-like stochastic generation, where each token is sampled from a context-dependent probability distribution, leading to inherently random decision trajectories rather than deterministic planning; (2) the reasoning and decision-making mechanisms are statically decoupled, meaning dynamically retrieved domain knowledge fails to dynamically adjust the underlying reasoning strategy. These dual deficiencies result in initial decisions lacking strategic anchoring and reasoning chains often failing to converge on correct solutions, as stochastic generation lacks mechanisms for trajectory correction or knowledge-guided optimization during sequential reasoning. To resolve these issues, we propose a problem-solving method integrated into the LLM's generation process to guide reasoning. This method, compatible with numerous LLMs and featuring reusable solutions, is grounded in a novel Heuristic-Classification-of-Thoughts prompting schema (HCoT). HCoT synergizes the LLM's reasoning ability with a structured problem space via a heuristic classification model that controls the reasoning process and provides reusable abstract solutions. Evaluated on two complex inductive reasoning tasks with ill-defined search spaces, HCoT outperforms existing approaches (e.g., Tree-of-Thoughts and Chain-of-Thoughts prompting) in performance. On the well-structured 24 Game task, HCoT demonstrates significantly higher token efficiency compared to the state-of-the-art Tree-of-Thoughts-Breadth-First-Search. In terms of both accuracy and token usage, HCoT achieves a Pareto frontier balance, offering a strong trade-off between performance and computational cost.

---


### 85. [Chain-of-Models Pre-Training: Rethinking Training Acceleration of Vision Foundation Models](https://arxiv.org/abs/2604.12391)

**<font color=#1a73e8>作者：</font>** Jiawei Fan, Shigeng Wang, Chao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present Chain-of-Models Pre-Training (CoM-PT), a novel performance-lossless training acceleration method for vision foundation models (VFMs). This approach fundamentally differs from existing acceleration methods in its core motivation: rather than optimizing each model individually, CoM-PT is designed to accelerate the training pipeline at the model family level, scaling efficiently as the model family expands. Specifically, CoM-PT establishes a pre-training sequence for the model family, arranged in ascending order of model size, called model chain. In this chain, only the smallest model undergoes standard individual pre-training, while the other models are efficiently trained through sequential inverse knowledge transfer from their smaller predecessors by jointly reusing the knowledge in the parameter space and the feature space. As a result, CoM-PT enables all models to achieve performance that is mostly superior to standard individual training while significantly reducing training cost, and this is extensively validated across 45 datasets spanning zero-shot and fine-tuning tasks. Notably, its efficient scaling property yields a remarkable phenomenon: training more models even results in higher efficiency. For instance, when pre-training on CC3M: i) given ViT-L as the largest model, progressively prepending smaller models to the model chain reduces computational complexity by up to 72%; ii) within a fixed model size range, as the VFM family scales across 3, 4, and 7 models, the acceleration ratio of CoM-PT exhibits a striking leap: from 4.13X to 5.68X and 7.09X. Since CoM-PT is naturally agnostic to specific pre-training paradigms, we open-source the code to spur further extensions in more computationally intensive scenarios, such as large language model pre-training.

---


### 86. [KoCo: Conditioning Language Model Pre-training on Knowledge Coordinates](https://arxiv.org/abs/2604.12397)

**<font color=#1a73e8>作者：</font>** Yudong Li, Jiawei Cai, Linlin Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard Large Language Model (LLM) pre-training typically treats corpora as flattened token sequences, often overlooking the real-world context that humans naturally rely on to contextualize information. To bridge this gap, we introduce Knowledge Coordinate Conditioning (KoCo), a simple method that maps every document into a three-dimensional semantic coordinate. By prepending these coordinates as textual prefixes for pre-training, we aim to equip the model with explicit contextual awareness to learn the documents within the real-world knowledge structure. Experiment results demonstrate that KoCo significantly enhances performance across 10 downstream tasks and accelerates pre-training convergence by approximately 30\%. Furthermore, our analysis indicates that explicitly modeling knowledge coordinates helps the model distinguish stable facts from noise, effectively mitigating hallucination in generated outputs.

---


### 87. [Agentic Insight Generation in VSM Simulations](https://arxiv.org/abs/2604.12421)

**<font color=#1a73e8>作者：</font>** Micha Selak, Dirk Krechel, Adrian Ulges 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting actionable insights from complex value stream map simulations can be challenging, time-consuming, and error-prone. Recent advances in large language models offer new avenues to support users with this task. While existing approaches excel at processing raw data to gain information, they are structurally unfit to pick up on subtle situational differences needed to distinguish similar data sources in this domain. To address this issue, we propose a decoupled, two-step agentic architecture. By separating orchestration from data analysis, the system leverages progressive data discovery infused with domain expert knowledge. This architecture allows the orchestration to intelligently select data sources and perform multi-hop reasoning across data structures while maintaining a slim internal context. Results from multiple state-of-the-art large language models demonstrate the framework's viability: with top-tier models achieving accuracies of up to 86% and demonstrating high robustness across evaluation runs.

---


### 88. [Decoding by Perturbation: Mitigating MLLM Hallucinations via Dynamic Textual Perturbation](https://arxiv.org/abs/2604.12424)

**<font color=#1a73e8>作者：</font>** Sihang Jia, Shuliang Liu, Songbo Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models frequently suffer from inference hallucinations, partially stemming from language priors dominating visual evidence. Existing training-free mitigation methods either perturb the visual representation and deviate from the natural image distribution, or enforce intrusive manipulations that compromise the model's inherent generative fluency. We introduce a novel perspective that multimodal hallucination manifests as the hypersensitivity of visual grounding to textual phrasing during the decoding phase. Building on this insight, we propose Decoding by Perturbation (DeP), a training-free framework mitigating prior-induced hallucinations via controlled textual interventions. DeP employs a dynamic probe applying multi-level textual perturbations to elicit latent language priors. Leveraging attention variance, it enhances stable evidence regions while suppressing suspicious noise in the feature space. Furthermore, it constructs an interpretable prior drift direction using logits statistics to counteract probability biases from textual co-occurrences. Extensive experiments confirm DeP effectively reduces hallucinations and achieves superior performance across multiple benchmarks.

---


### 89. [Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments](https://arxiv.org/abs/2604.12459)

**<font color=#1a73e8>作者：</font>** Esen Kurt, Haithem Afli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in politically sensitive environments, where memorisation of personal data or confidential content raises regulatory concerns under frameworks such as the GDPR and its Right to be Forgotten. Translating such legal principles into large-scale generative systems presents significant technical challenges.
We introduce a lightweight sequential unlearning framework that explicitly separates retention and suppression objectives. The method first stabilises benign capabilities through positive fine-tuning, then applies layer-restricted negative fine-tuning to suppress designated sensitive patterns while preserving general language competence.
Experiments on the SemEval-2025 LLM Unlearning benchmark demonstrate effective behavioural suppression with minimal impact on factual accuracy and fluency. GPT-2 exhibits greater robustness than DistilGPT-2, highlighting the role of model capacity in privacy-aligned adaptation. We position sequential unlearning as a practical and reproducible mechanism for operationalising data erasure requirements in politically deployed LLMs.

---


### 90. [CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems](https://arxiv.org/abs/2604.12461)

**<font color=#1a73e8>作者：</font>** Yongxuan Wu, Xixun Lin, He Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in solving complex tasks. Central to MAS is the communication topology which governs how agents exchange information internally. Consequently, the security of communication topologies has attracted increasing attention. In this paper, we investigate a critical privacy risk: MAS communication topologies can be inferred under a restrictive black-box setting, exposing system vulnerabilities and posing significant intellectual property threats. To explore this risk, we propose Communication Inference Attack (CIA), a novel attack that constructs new adversarial queries to induce intermediate agents' reasoning outputs and models their semantic correlations through the proposed global bias disentanglement and LLM-guided weak supervision. Extensive experiments on MAS with optimized communication topologies demonstrate the effectiveness of CIA, achieving an average AUC of 0.87 and a peak AUC of up to 0.99, thereby revealing the substantial privacy risk in MAS.

---


### 91. [Analyzing the Effect of Noise in LLM Fine-tuning](https://arxiv.org/abs/2604.12469)

**<font color=#1a73e8>作者：</font>** Lingfang Li, Procheta Sen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning is the dominant paradigm for adapting pretrained large language models (LLMs) to downstream NLP tasks. In practice, fine-tuning datasets may contain various forms of noise arising from annotation errors, preprocessing artifacts, or automated data collection. While prior work has focused on designing robust learning algorithms to mitigate performance degradation under noisy conditions, comparatively little is known about how different types of noise affect the internal learning dynamics of LLMs during fine-tuning. In this work, we systematically study the impact of noise on model behavior across three pretrained model families (GPT-2, Qwen2 and Llama-2) and three diverse NLP tasks. We introduce controlled perturbations corresponding to three common real-world noise types: label noise, grammatical noise, and typographical noise. Beyond task-level performance, we analyze layer-wise representation changes and attention patterns to understand how noise propagates through the network. Our results show that corrupting labels (i.e. label noise) consistently causes the largest performance degradation, whereas grammatical noise and typographical noise can occasionally yield mild regularization benefits. We further find that noise effects are localized primarily to task-specific layers, while attention structures remain comparatively stable.

---


### 92. [Mining Large Language Models for Low-Resource Language Data: Comparing Elicitation Strategies for Hausa and Fongbe](https://arxiv.org/abs/2604.12477)

**<font color=#1a73e8>作者：</font>** Mahounan Pericles Adjovi, Roald Eiselen, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained on data contributed by low-resource language communities, yet the linguistic knowledge encoded in these models remains accessible only through commercial APIs. This paper investigates whether strategic prompting can extract usable text data from LLMs for two West African languages: Hausa (Afroasiatic, approximately 80 million speakers) and Fongbe (Niger-Congo, approximately 2 million speakers). We systematically compare six elicitation task types across two commercial LLMs (GPT-4o Mini and Gemini 2.5 Flash). GPT-4o Mini extracts 6-41 times more usable target-language words per API call than Gemini. Optimal strategies differ by language: Hausa benefits from functional text and dialogue, while Fongbe requires constrained generation prompts. We release all generated corpora and code.

---


### 93. [Meet Dynamic Individual Preferences: Resolving Conflicting Human Value with Paired Fine-Tuning](https://arxiv.org/abs/2604.12479)

**<font color=#1a73e8>作者：</font>** Shanyong Wang, Shuhang Lin, Yining Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have significantly improved the alignment of models with general human preferences. However, a major challenge remains in adapting LLMs to individual preferences, which are not only diverse but also dynamic. In this paper, we introduce a novel framework, Preference-Paired Fine-Tuning (PFT), designed to align models with contradictory and evolving individual preferences. We present a new dataset, Value Conflict Dilemma (VCD), which includes scenarios that involve conflicting human preferences, facilitating the evaluation of our approach. Our experiments demonstrate that PFT outperforms single-preference training methods, achieving up to 96.6% accuracy in multi-choice classification tasks and the highest open-ended generation score of 8.69. PFT also shows significant improvements over DPO, SFT and some traditional training methods, especially when handling conflicting preferences. Additionally, with limited user history data, models can inferring preference vector rapidly, achieving a 44.76% improvement in user-specific preference alignment in comparison to single-preference models.

---


### 94. [T2I-BiasBench: A Multi-Metric Framework for Auditing Demographic and Cultural Bias in Text-to-Image Models](https://arxiv.org/abs/2604.12481)

**<font color=#1a73e8>作者：</font>** Nihal Jaiswal, Siddhartha Arjaria, Gyanendra Chaubey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generative models achieve impressive visual fidelity but inherit and amplify demographic imbalances and cultural biases embedded in training data. We introduce T2I-BiasBench, a unified evaluation framework of thirteen complementary metrics that jointly captures demographic bias, element omission, and cultural collapse in diffusion models - the first framework to address all three dimensions simultaneously.
We evaluate three open-source models - Stable Diffusion v1.5, BK-SDM Base, and Koala Lightning - against Gemini 2.5 Flash (RLHF-aligned) as a reference baseline. The benchmark comprises 1,574 generated images across five structured prompt categories. T2I-BiasBench integrates six established metrics with seven additional measures: four newly proposed (Composite Bias Score, Grounded Missing Rate, Implicit Element Missing Rate, Cultural Accuracy Ratio) and three adapted (Hallucination Score, Vendi Score, CLIP Proxy Score).
Three key findings emerge: (1) Stable Diffusion v1.5 and BK-SDM exhibit bias amplification (>1.0) in beauty-related prompts; (2) contextual constraints such as surgical PPE substantially attenuate professional-role gender bias (Doctor CBS = 0.06 for SD v1.5); and (3) all models, including RLHF-aligned Gemini, collapse to a narrow set of cultural representations (CAS: 0.54-1.00), confirming that alignment techniques do not resolve cultural coverage gaps.
T2I-BiasBench is publicly released to support standardized, fine-grained bias evaluation of generative models. The project page is available at: this https URL

---


### 95. [KG-Reasoner: A Reinforced Model for End-to-End Multi-Hop Knowledge Graph Reasoning](https://arxiv.org/abs/2604.12487)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Yinan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong abilities in natural language understanding and generation, yet they struggle with knowledge-intensive reasoning. Structured Knowledge Graphs (KGs) provide an effective form of external knowledge representation and have been widely used to enhance performance in classical Knowledge Base Question Answering (KBQA) tasks. However, performing precise multi-hop reasoning over KGs for complex queries remains highly challenging. Most existing approaches decompose the reasoning process into a sequence of isolated steps executed through a fixed pipeline. While effective to some extent, such designs constrain reasoning flexibility and fragment the overall decision process, often leading to incoherence and the loss of critical intermediate information from earlier steps. In this paper, we introduce KG-Reasoner, an end-to-end framework that integrates multi-step reasoning into a unified "thinking" phase of a Reasoning LLM. Through Reinforcement Learning (RL), the LLM is trained to internalize the KG traversal process, enabling it to dynamically explore reasoning paths, and perform backtracking when necessary. Experiments on eight multi-hop and knowledge-intensive reasoning benchmarks demonstrate that KG-Reasoner achieves competitive or superior performance compared to the state-of-the-art methods. Codes are available at the repository: this https URL.

---


### 96. [Calibrated Confidence Estimation for Tabular Question Answering](https://arxiv.org/abs/2604.12491)

**<font color=#1a73e8>作者：</font>** Lukas Voss  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed for tabular question
answering, yet calibration on structured data is largely unstudied. This
paper presents the first systematic comparison of five confidence estimation
methods across five frontier LLMs and two tabular QA benchmarks. All models
are severely overconfident (smooth ECE 0.35-0.64 versus 0.10-0.15 reported
for textual QA). A consistent self-evaluation versus perturbation dichotomy
replicates across both benchmarks and all four fully-covered models:
self-evaluation methods (verbalized, P(True)) achieve AUROC 0.42-0.76, while
perturbation methods (semantic entropy, self-consistency, and our
Multi-Format Agreement) achieve AUROC 0.78-0.86. Per-model paired bootstrap
tests reject the null at p<0.001 after Holm-Bonferroni correction, and a
3-seed check on GPT-4o-mini gives a per-seed standard deviation of only
0.006. The paper proposes Multi-Format Agreement (MFA), which exploits the
lossless and deterministic serialization variation unique to structured data
(Markdown, HTML, JSON, CSV) to estimate confidence at 20% lower API cost
than sampling baselines. MFA reduces ECE by 44-63%, generalizes across all
four models on TableBench (mean AUROC 0.80), and combines complementarily
with sampling: an MFA + self-consistency ensemble lifts AUROC from 0.74 to
0.82. A secondary contribution, structure-aware recalibration, improves
AUROC by +10 percentage points over standard post-hoc methods.

---


### 97. [Adaptive Budget Allocation in LLM-Augmented Surveys](https://arxiv.org/abs/2604.12497)

**<font color=#1a73e8>作者：</font>** Zikun Ye, Jiameng Lyu, Rui Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate survey responses at low cost, but their reliability varies substantially across questions and is unknown before data collection. Deploying LLMs in surveys still requires costly human responses for verification and correction. How should a limited human-labeling budget be allocated across questions in real time? We propose an adaptive allocation algorithm that learns which questions are hardest for the LLM while simultaneously collecting human responses. Each human label serves a dual role: it improves the estimate for that question and reveals how well the LLM predicts human responses on it. The algorithm directs more budget to questions where the LLM is least reliable, without requiring any prior knowledge of question-level LLM accuracy. We prove that the allocation gap relative to the best possible allocation vanishes as the budget grows, and validate the approach on both synthetic data and a real survey dataset with 68 questions and over 2000 respondents. On real survey data, the standard practice of allocating human labels uniformly across questions wastes 10--12% of the budget relative to the optimal; our algorithm reduces this waste to 2--6%, and the advantage grows as questions become more heterogeneous in LLM prediction quality. The algorithm achieves the same estimation quality as traditional uniform sampling with fewer human samples, requires no pilot study, and is backed by formal performance guarantees validated on real survey data. More broadly, the framework applies whenever scarce human oversight must be allocated across tasks where LLM reliability is unknown.

---


### 98. [SEATrack: Simple, Efficient, and Adaptive Multimodal Tracker](https://arxiv.org/abs/2604.12502)

**<font color=#1a73e8>作者：</font>** Junbin Su, Ziteng Xue, Shihui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) in multimodal tracking reveals a concerning trend where recent performance gains are often achieved at the cost of inflated parameter budgets, which fundamentally erodes PEFT's efficiency promise. In this work, we introduce SEATrack, a Simple, Efficient, and Adaptive two-stream multimodal tracker that tackles this performance-efficiency dilemma from two complementary perspectives. We first prioritize cross-modal alignment of matching responses, an underexplored yet pivotal factor that we argue is essential for breaking the trade-off. Specifically, we observe that modality-specific biases in existing two-stream methods generate conflicting matching attention maps, thereby hindering effective joint representation learning. To mitigate this, we propose AMG-LoRA, which seamlessly integrates Low-Rank Adaptation (LoRA) for domain adaptation with Adaptive Mutual Guidance (AMG) to dynamically refine and align attention maps across modalities. We then depart from conventional local fusion approaches by introducing a Hierarchical Mixture of Experts (HMoE) that enables efficient global relation modeling, effectively balancing expressiveness and computational efficiency in cross-modal fusion. Equipped with these innovations, SEATrack advances notable progress over state-of-the-art methods in balancing performance with efficiency across RGB-T, RGB-D, and RGB-E tracking tasks. \href{this https URL}{\textcolor{cyan}{Code is available}}.

---


### 99. [Topology-Aware Reasoning over Incomplete Knowledge Graph with Graph-Based Soft Prompting](https://arxiv.org/abs/2604.12503)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Xixi Wang, Yinan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown remarkable capabilities across various tasks but remain prone to hallucinations in knowledge-intensive scenarios. Knowledge Base Question Answering (KBQA) mitigates this by grounding generation in Knowledge Graphs (KGs). However, most multi-hop KBQA methods rely on explicit edge traversal, making them fragile to KG incompleteness. In this paper, we proposed a novel graph-based soft prompting framework that shifts the reasoning paradigm from node-level path traversal to subgraph-level reasoning. Specifically, we employ a Graph Neural Network (GNN) to encode extracted structural subgraphs into soft prompts, enabling LLM to reason over richer structural context and identify relevant entities beyond immediate graph neighbors, thereby reducing sensitivity to missing edges. Furthermore, we introduce a two-stage paradigm that reduces computational cost while preserving good performance: a lightweight LLM first leverages the soft prompts to identify question-relevant entities and relations, followed by a more powerful LLM for evidence-aware answer generation. Experiments on four multi-hop KBQA benchmarks show that our approach achieves state-of-the-art performance on three of them, demonstrating its effectiveness. Code is available at the repository: this https URL.

---


### 100. [Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](https://arxiv.org/abs/2604.12506)

**<font color=#1a73e8>作者：</font>** Linhao Zhang, Yuhan Song, Aiwei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent Audio Large Language Models (AudioLLMs) exhibit a striking performance inversion: while excelling at complex reasoning tasks, they consistently underperform on fine-grained acoustic perception. We attribute this gap to a fundamental limitation of ASR-centric training, which provides precise linguistic targets but implicitly teaches models to suppress paralinguistic cues and acoustic events as noise. To address this, we propose Unified Audio Schema (UAS), a holistic and structured supervision framework that organizes audio information into three explicit components -- Transcription, Paralinguistics, and Non-linguistic Events -- within a unified JSON format. This design achieves comprehensive acoustic coverage without sacrificing the tight audio-text alignment that enables reasoning. We validate the effectiveness of this supervision strategy by applying it to both discrete and continuous AudioLLM architectures. Extensive experiments on MMSU, MMAR, and MMAU demonstrate that UAS-Audio yields consistent improvements, boosting fine-grained perception by 10.9% on MMSU over the same-size state-of-the-art models while preserving robust reasoning capabilities. Our code and model are publicly available at this https URL.

---


### 101. [From Attenuation to Attention: Variational Information Flow Manipulation for Fine-Grained Visual Perception](https://arxiv.org/abs/2604.12508)

**<font color=#1a73e8>作者：</font>** Jilong Zhu, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in general visual understanding, they frequently falter in fine-grained perception tasks that require identifying tiny objects or discerning subtle visual relationships. We attribute this limitation to Visual Attenuation: a phenomenon where sparse fine-grained visual signals are prematurely suppressed or diluted by dominant textual tokens during network propagation, resulting in a "loss of focus" during the deep-level decision-making process. Existing input-centric solutions fail to fundamentally reverse this intrinsic mechanism of information loss. To address this challenge, we propose the Variational Information Flow (VIF) framework. Adopting a probabilistic perspective, VIF leverages a Conditional Variational Autoencoder (CVAE) to model the visual saliency relevant to the question-answer pair as a latent distribution. As a plug-and-play module, VIF can be integrated into existing architectures. Extensive evaluations across diverse benchmarks, covering General VQA, fine-grained perception, and visual grounding, demonstrate that VIF yields competitive improvements over previous methods, validating its effectiveness in enhancing the fine-grained perception of MLLMs.

---


### 102. [NTIRE 2026 The 3rd Restore Any Image Model (RAIM) Challenge: Professional Image Quality Assessment (Track 1)](https://arxiv.org/abs/2604.12512)

**<font color=#1a73e8>作者：</font>** Guanyi Qin, Jie Liang, Bingbing Zhang 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present an overview of the NTIRE 2026 challenge on the 3rd Restore Any Image Model in the Wild, specifically focusing on Track 1: Professional Image Quality Assessment. Conventional Image Quality Assessment (IQA) typically relies on scalar scores. By compressing complex visual characteristics into a single number, these methods fundamentally struggle to distinguish subtle differences among uniformly high-quality images. Furthermore, they fail to articulate why one image is superior, lacking the reasoning capabilities required to provide guidance for vision tasks. To bridge this gap, recent advancements in Multimodal Large Language Models (MLLMs) offer a promising paradigm. Inspired by this potential, our challenge establishes a novel benchmark exploring the ability of MLLMs to mimic human expert cognition in evaluating high-quality image pairs. Participants were tasked with overcoming critical bottlenecks in professional scenarios, centering on two primary objectives: (1) Comparative Quality Selection: reliably identifying the visually superior image within a high-quality pair; and (2) Interpretative Reasoning: generating grounded, expert-level explanations that detail the rationale behind the selection. In total, the challenge attracted nearly 200 registrations and over 2,500 submissions. The top-performing methods significantly advanced the state of the art in professional IQA. The challenge dataset is available at this https URL, and the official homepage is accessible at this https URL.

---


### 103. [Agentic Control in Variational Language Models](https://arxiv.org/abs/2604.12513)

**<font color=#1a73e8>作者：</font>** Yves Ruffenach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether a variational language model can support a minimal and measurable form of agentic control grounded in its own internal evidence. Our model combines local variational hidden computation (EVE), a homeostatic latent regulator, structurally aware checkpoint retention and a calibrated uncertainty-aware controller operating on top of the retained model. Rather than treating uncertainty as a passive diagnostic measured after prediction, we treat it as an operational signal that can regulate training, support checkpoint retention and guide inference-time intervention. The resulting framework is deliberately focused. It studies a closed-loop form of internal control in which structural and predictive signals become actionable. Empirically, the variational backbone improves over a matched deterministic reference on the language-modeling task while also exhibiting a richer and more usable uncertainty profile. On top of this backbone, the calibrated controller remains active, uses multiple actions under a full agentic evaluation and yields a positive quality-cost trade-off. These results support a precise claim: internal uncertainty can serve not only as a descriptive property of a variational language model, but also as a practical control interface for regulation, checkpoint retention and minimal agentic routing.

---


### 104. [Enhance-then-Balance Modality Collaboration for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2604.12518)

**<font color=#1a73e8>作者：</font>** Kang He, Yuzhe Ding, Xinrong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis (MSA) integrates heterogeneous text, audio, and visual signals to infer human emotions. While recent approaches leverage cross-modal complementarity, they often struggle to fully utilize weaker modalities. In practice, dominant modalities tend to overshadow non-verbal ones, inducing modality competition and limiting overall contributions. This imbalance degrades fusion performance and robustness under noisy or missing modalities. To address this, we propose a novel model, Enhance-then-Balance Modality Collaboration framework (EBMC). EBMC improves representation quality via semantic disentanglement and cross-modal enhancement, strengthening weaker modalities. To prevent dominant modalities from overwhelming others, an Energy-guided Modality Coordination mechanism achieves implicit gradient rebalancing via a differentiable equilibrium objective. Furthermore, Instance-aware Modality Trust Distillation estimates sample-level reliability to adaptively modulate fusion weights, ensuring robustness. Extensive experiments demonstrate that EBMC achieves state-of-the-art or competitive results and maintains strong performance under missing-modality settings.

---


### 105. [MODIX: A Training-Free Multimodal Information-Driven Positional Index Scaling for Vision-Language Models](https://arxiv.org/abs/2604.12537)

**<font color=#1a73e8>作者：</font>** Ruoxiang Huang, Zhen Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved remarkable progress in multimodal understanding, yet their positional encoding mechanisms remain suboptimal. Existing approaches uniformly assign positional indices to all tokens, overlooking variations in information density within and across modalities, which leads to inefficient attention allocation where redundant visual regions dominate while informative content is underrepresented. We identify positional granularity as an implicit resource and propose MODIX (Multimodal Information-Driven Positional IndeX Scaling), a training-free framework that dynamically adapts positional strides based on modality-specific contributions. MODIX jointly models intra-modal density via covariance-based entropy and inter-modal interaction via cross-modal alignment to derive unified scores, which rescale positional indices to allocate finer granularity to informative modalities while compressing redundant ones, without requiring any modification to model parameters or architecture. Experiments across diverse architectures and benchmarks demonstrate that MODIX consistently improves multimodal reasoning and adaptively reallocates attention according to task-dependent information distributions, suggesting that positional encoding should be treated as an adaptive resource in Transformers for multimodal sequence modeling.

---


### 106. [When Does Data Augmentation Help? Evaluating LLM and Back-Translation Methods for Hausa and Fongbe NLP](https://arxiv.org/abs/2604.12540)

**<font color=#1a73e8>作者：</font>** Mahounan Pericles Adjovi, Roald Eiselen, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data scarcity limits NLP development for low-resource African languages. We evaluate two data augmentation methods -- LLM-based generation (Gemini 2.5 Flash) and back-translation (NLLB-200) -- for Hausa and Fongbe, two West African languages that differ substantially in LLM generation quality. We assess augmentation on named entity recognition (NER) and part-of-speech (POS) tagging using MasakhaNER 2.0 and MasakhaPOS benchmarks. Our results reveal that augmentation effectiveness depends on task type rather than language or LLM quality alone. For NER, neither method improves over baseline for either language; LLM augmentation reduces Hausa NER by 0.24% F1 and Fongbe NER by 1.81% F1. For POS tagging, LLM augmentation improves Fongbe by 0.33% accuracy, while back-translation improves Hausa by 0.17%; back-translation reduces Fongbe POS by 0.35% and has negligible effect on Hausa POS. The same LLM-generated synthetic data produces opposite effects across tasks for Fongbe -- hurting NER while helping POS -- suggesting task structure governs augmentation outcomes more than synthetic data quality. These findings challenge the assumption that LLM generation quality predicts augmentation success, and provide actionable guidance: data augmentation should be treated as a task-specific intervention rather than a universally beneficial preprocessing step.

---


### 107. [A Two-Stage LLM Framework for Accessible and Verified XAI Explanations](https://arxiv.org/abs/2604.12543)

**<font color=#1a73e8>作者：</font>** Georgios Mermigkis, Dimitris Metaxakis, Marios Tyrovolas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to translate the technical outputs of eXplainable Artificial Intelligence (XAI) methods into accessible natural-language explanations. However, existing approaches often lack guarantees of accuracy, faithfulness, and completeness. At the same time, current efforts to evaluate such narratives remain largely subjective or confined to post-hoc scoring, offering no safeguards to prevent flawed explanations from reaching end-users. To address these limitations, this paper proposes a Two-Stage LLM Meta-Verification Framework that consists of (i) an Explainer LLM that converts raw XAI outputs into natural-language narratives, (ii) a Verifier LLM that assesses them in terms of faithfulness, coherence, completeness, and hallucination risk, and (iii) an iterative refeed mechanism that uses the Verifier's feedback to refine and improve them. Experiments across five XAI techniques and datasets, using three families of open-weight LLMs, show that verification is crucial for filtering unreliable explanations while improving linguistic accessibility compared with raw XAI outputs. In addition, the analysis of the Entropy Production Rate (EPR) during the refinement process indicates that the Verifier's feedback progressively guides the Explainer toward more stable and coherent reasoning. Overall, the proposed framework provides an efficient pathway toward more trustworthy and democratized XAI systems.

---


### 108. [Cross-Cultural Simulation of Citizen Emotional Responses to Bureaucratic Red Tape Using LLM Agents](https://arxiv.org/abs/2604.12545)

**<font color=#1a73e8>作者：</font>** Wanchun Ni, Jiugeng Sun, Yixian Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving policymaking is a central concern in public administration. Prior human subject studies reveal substantial cross-cultural differences in citizens' emotional responses to red tape during policy implementation. While LLM agents offer opportunities to simulate human-like responses and reduce experimental costs, their ability to generate culturally appropriate emotional responses to red tape remains unverified. To address this gap, we propose an evaluation framework for assessing LLMs' emotional responses to red tape across diverse cultural contexts. As a pilot study, we apply this framework to a single red-tape scenario. Our results show that all models exhibit limited alignment with human emotional responses, with notably weaker performance in Eastern cultures. Cultural prompting strategies prove largely ineffective in improving alignment. We further introduce \textbf{RAMO}, an interactive interface for simulating citizens' emotional responses to red tape and for collecting human data to improve models. The interface is publicly available at this https URL.

---


### 109. [IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration](https://arxiv.org/abs/2604.12573)

**<font color=#1a73e8>作者：</font>** Yanji He, Yuxin Jiang, Yiwen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed for decision-making, yet their adoption in high-stakes domains remains limited by miscalibrated probabilities, unfaithful explanations, and inability to incorporate expert knowledge precisely. We propose IDEA, a framework that extracts LLM decision knowledge into an interpretable parametric model over semantically meaningful factors. Through joint learning of verbal-to-numerical mappings and decision parameters via EM, correlated sampling that preserves factor dependencies, and direct parameter editing with mathematical guarantees, IDEA produces calibrated probabilities while enabling quantitative human-AI collaboration. Experiments across five datasets show IDEA with Qwen-3-32B (78.6%) outperforms DeepSeek R1 (68.1%) and GPT-5.2 (77.9%), achieving perfect factor exclusion and exact calibration -- precision unattainable through prompting alone. The implementation is publicly available at this https URL.

---


### 110. [EEG-Based Multimodal Learning via Hyperbolic Mixture-of-Curvature Experts](https://arxiv.org/abs/2604.12579)

**<font color=#1a73e8>作者：</font>** Runhe Zhou, Shanglin Li, Guanxiang Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based multimodal learning integrates brain signals with complementary modalities to improve mental state assessment, providing great clinical potential. The effectiveness of such paradigms largely depends on the representation learning on heterogeneous modalities. For EEG-based paradigms, one promising approach is to leverage their hierarchical structures, as recent studies have shown that both EEG and associated modalities (e.g., facial expressions) exhibit hierarchical structures reflecting complex cognitive processes. However, Euclidean embeddings struggle to represent these hierarchical structures due to their flat geometry, while hyperbolic spaces, with their exponential growth property, are naturally suited for them. In this work, we propose EEG-MoCE, a novel hyperbolic mixture-of-curvature experts framework designed for multimodal neurotechnology. EEG-MoCE assigns each modality to an expert in a learnable-curvature hyperbolic space, enabling adaptive modeling of its intrinsic geometry. A curvature-aware fusion strategy then dynamically weights experts, emphasizing modalities with richer hierarchical information. Extensive experiments on benchmark datasets demonstrate that EEG-MoCE achieves state-of-the-art performance, including emotion recognition, sleep staging, and cognitive assessment.

---


### 111. [Relaxing Anchor-Frame Dominance for Mitigating Hallucinations in Video Large Language Models](https://arxiv.org/abs/2604.12582)

**<font color=#1a73e8>作者：</font>** Zijian Liu, Sihan Cao, Pengcheng Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Video Large Language Models (Video-LLMs) have demonstrated strong capability in video understanding, yet they still suffer from hallucinations. Existing mitigation methods typically rely on training, input modification, auxiliary guidance, or additional decoding procedures, while largely overlooking a more fundamental challenge. During generation, Video-LLMs tend to over-rely on a limited portion of temporal evidence, leading to temporally imbalanced evidence aggregation across the video. To address this issue, we investigate a decoder-side phenomenon in which the model exhibits a temporally imbalanced concentration pattern. We term the frame with the highest aggregated frame-level attention mass the anchor frame. We find that this bias is largely independent of the input video and instead appears to reflect a persistent, model-specific structural or positional bias, whose over-dominance is closely associated with hallucination-prone generation. Motivated by this insight, we propose Decoder-side Temporal Rebalancing (DTR), a training-free, layer-selective inference method that rebalances temporal evidence allocation in middle-to-late decoder layers without altering visual encoding or requiring auxiliary models. DTR adaptively calibrates decoder-side visual attention to alleviate temporally imbalanced concentration and encourage under-attended frames to contribute more effectively to response generation. In this way, DTR guides the decoder to ground its outputs in temporally broader and more balanced video evidence. Extensive experiments on hallucination and video understanding benchmarks show that DTR consistently improves hallucination robustness across diverse Video-LLM families, while preserving competitive video understanding performance and high inference efficiency.

---


### 112. [KumoRFM-2: Scaling Foundation Models for Relational Learning](https://arxiv.org/abs/2604.12596)

**<font color=#1a73e8>作者：</font>** Valter Hudovernik, Federico López, Vid Kocijan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce KumoRFM-2, the next iteration of a pre-trained foundation model for relational data. KumoRFM-2 supports in-context learning as well as fine-tuning and is applicable to a wide range of predictive tasks. In contrast to tabular foundation models, KumoRFM-2 natively operates on relational data, processing one or more connected tables simultaneously without manual table flattening or target variable generation, all while preserving temporal consistency. KumoRFM-2 leverages a large corpus of synthetic and real-world data to pre-train across four axes: the row and column dimensions at the individual table level, and the foreign key and cross-sample dimensions at the database level. In contrast to its predecessor, KumoRFM-2 injects task information as early as possible, enabling sharper selection of task-relevant columns and improved robustness to noisy data. Through extensive experiments on 41 challenging benchmarks and analysis around expressivity and sensitivity, we demonstrate that KumoRFM-2 outperforms supervised and foundational approaches by up to 8%, while maintaining strong performance under extreme settings of cold start and noisy data. To our knowledge, this is the first time a few-shot foundation model has been shown to surpass supervised approaches on common benchmark tasks, with performance further improving upon fine-tuning. Finally, while KumoRFM-1 was limited to small-scale in-memory datasets, KumoRFM-2 scales to billion-scale relational datasets.

---


### 113. [Transforming External Knowledge into Triplets for Enhanced Retrieval in RAG of LLMs](https://arxiv.org/abs/2604.12610)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Chaoning Zhang, Qigan Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) mitigates hallucination in large language models (LLMs) by incorporating external knowledge during generation. However, the effectiveness of RAG depends not only on the design of the retriever and the capacity of the underlying model, but also on how retrieved evidence is structured and aligned with the query. Existing RAG approaches typically retrieve and concatenate unstructured text fragments as context, which often introduces redundant or weakly relevant information. This practice leads to excessive context accumulation, reduced semantic alignment, and fragmented reasoning chains, thereby degrading generation quality while increasing token consumption. To address these challenges, we propose Tri-RAG, a structured triplet-based retrieval framework that improves retrieval efficiency through reasoning-aligned context construction. Tri-RAG automatically transforms external knowledge from natural language into standardized structured triplets consisting of Condition, Proof, and Conclusion, explicitly capturing logical relations among knowledge fragments using lightweight prompt-based adaptation with frozen model parameters. Building on this representation, the triplet head Condition is treated as an explicit semantic anchor for retrieval and matching, enabling precise identification of query-relevant knowledge units without directly concatenating lengthy raw texts. As a result, Tri-RAG achieves a favorable balance between retrieval accuracy and context token efficiency. Experimental results across multiple benchmark datasets demonstrate that Tri-RAG significantly improves retrieval quality and reasoning efficiency, while producing more stable generation behavior and more efficient resource utilization in complex reasoning scenarios.

---


### 114. [DeepTest Tool Competition 2026: Benchmarking an LLM-Based Automotive Assistant](https://arxiv.org/abs/2604.12615)

**<font color=#1a73e8>作者：</font>** Lev Sorokin, Ivan Vasilev, Samuele Pasini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This report summarizes the results of the first edition of the Large Language Model (LLM) Testing competition, held as part of the DeepTest workshop at ICSE 2026. Four tools competed in benchmarking an LLM-based car manual information retrieval application, with the objective of identifying user inputs for which the system fails to appropriately mention warnings contained in the manual. The testing solutions were evaluated based on their effectiveness in exposing failures and the diversity of the discovered failure-revealing tests. We report on the experimental methodology, the competitors, and the results.

---


### 115. [Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs](https://arxiv.org/abs/2604.12616)

**<font color=#1a73e8>作者：</font>** Jianhao Chen, Haoyang Chen, Hanjie Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Vision-Language Models (VLMs) has catalyzed unprecedented capabilities in artificial intelligence; however, this continuous modal expansion has inadvertently exposed a vastly broadened and unconstrained adversarial attack surface. Current multimodal jailbreak strategies primarily focus on surface-level pixel perturbations and typographic attacks or harmful images; however, they fail to engage with the complex semantic structures intrinsic to visual data. This leaves the vast semantic attack surface of original, natural images largely unscrutinized. Driven by the need to expose these deep-seated semantic vulnerabilities, we introduce \textbf{MemJack}, a \textbf{MEM}ory-augmented multi-agent \textbf{JA}ilbreak atta\textbf{CK} framework that explicitly leverages visual semantics to orchestrate automated jailbreak attacks. MemJack employs coordinated multi-agent cooperation to dynamically map visual entities to malicious intents, generate adversarial prompts via multi-angle visual-semantic camouflage, and utilize an Iterative Nullspace Projection (INLP) geometric filter to bypass premature latent space refusals. By accumulating and transferring successful strategies through a persistent Multimodal Experience Memory, MemJack maintains highly coherent extended multi-turn jailbreak attack interactions across different images, thereby improving the attack success rate (ASR) on new images. Extensive empirical evaluations across full, unmodified COCO val2017 images demonstrate that MemJack achieves a 71.48\% ASR against Qwen3-VL-Plus, scaling to 90\% under extended budgets. Furthermore, to catalyze future defensive alignment research, we will release \textbf{MemJack-Bench}, a comprehensive dataset comprising over 113,000 interactive multimodal jailbreak attack trajectories, establishing a vital foundation for developing inherently robust VLMs.

---


### 116. [SOAR: Self-Correction for Optimal Alignment and Refinement in Diffusion Models](https://arxiv.org/abs/2604.12617)

**<font color=#1a73e8>作者：</font>** You Qin, Linqing Wang, Hao Fei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The post-training pipeline for diffusion models currently has two stages: supervised fine-tuning (SFT) on curated data and reinforcement learning (RL) with reward models. A fundamental gap separates them. SFT optimizes the denoiser only on ground-truth states sampled from the forward noising process; once inference deviates from these ideal states, subsequent denoising relies on out-of-distribution generalization rather than learned correction, exhibiting the same exposure bias that afflicts autoregressive models, but accumulated along the denoising trajectory instead of the token sequence. RL can in principle address this mismatch, yet its terminal reward signal is sparse, suffers from credit-assignment difficulty, and risks reward hacking. We propose SOAR (Self-Correction for Optimal Alignment and Refinement), a bias-correction post-training method that fills this gap. Starting from a real sample, SOAR performs a single stop-gradient rollout with the current model, re-noises the resulting off-trajectory state, and supervises the model to steer back toward the original clean target. The method is on-policy, reward-free, and provides dense per-timestep supervision with no credit-assignment problem. On SD3.5-Medium, SOAR improves GenEval from 0.70 to 0.78 and OCR from 0.64 to 0.67 over SFT, while simultaneously raising all model-based preference scores. In controlled reward-specific experiments, SOAR surpasses Flow-GRPO in final metric value on both aesthetic and text-image alignment tasks, despite having no access to a reward model. Since SOAR's base loss subsumes the standard SFT objective, it can directly replace SFT as a stronger first post-training stage after pretraining, while remaining fully compatible with subsequent RL alignment.

---


### 117. [KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance](https://arxiv.org/abs/2604.12627)

**<font color=#1a73e8>作者：</font>** Linhao Yu, Tianmeng Yang, Siyu Ding 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RLVR improves reasoning in large language models, but its effectiveness is often limited by severe reward sparsity on hard problems. Recent hint-based RL methods mitigate sparsity by injecting partial solutions or abstract templates, yet they typically scale guidance by adding more tokens, which introduce redundancy, inconsistency, and extra training overhead. We propose \textbf{KnowRL} (Knowledge-Guided Reinforcement Learning), an RL training framework that treats hint design as a minimal-sufficient guidance problem. During RL training, KnowRL decomposes guidance into atomic knowledge points (KPs) and uses Constrained Subset Search (CSS) to construct compact, interaction-aware subsets for training. We further identify a pruning interaction paradox -- removing one KP may help while removing multiple such KPs can hurt -- and explicitly optimize for robust subset curation under this dependency structure. We train KnowRL-Nemotron-1.5B from OpenMath-Nemotron-1.5B. Across eight reasoning benchmarks at the 1.5B scale, KnowRL-Nemotron-1.5B consistently outperforms strong RL and hinting baselines. Without KP hints at inference, KnowRL-Nemotron-1.5B reaches 70.08 average accuracy, already surpassing Nemotron-1.5B by +9.63 points; with selected KPs, performance improves to 74.16, establishing a new state of the art at this scale. The model, curated training data, and code are publicly available at this https URL.

---


### 118. [GeoAlign: Geometric Feature Realignment for MLLM Spatial Reasoning](https://arxiv.org/abs/2604.12630)

**<font color=#1a73e8>作者：</font>** Zhaochen Liu, Limeng Qiao, Guanglu Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have exhibited remarkable performance in various visual tasks, yet still struggle with spatial reasoning. Recent efforts mitigate this by injecting geometric features from 3D foundation models, but rely on static single-layer extractions. We identify that such an approach induces a task misalignment bias: the geometric features naturally evolve towards 3D pretraining objectives, which may contradict the heterogeneous spatial demands of MLLMs, rendering any single layer fundamentally insufficient. To resolve this, we propose GeoAlign, a novel framework that dynamically aggregates multi-layer geometric features to realign with the actual demands. GeoAlign constructs a hierarchical geometric feature bank and leverages the MLLM's original visual tokens as content-aware queries to perform layer-wise sparse routing, adaptively fetching the suitable geometric features for each patch. Extensive experiments on VSI-Bench, ScanQA, and SQA3D demonstrate that our compact 4B model effectively achieves state-of-the-art performance, even outperforming larger existing MLLMs.

---


### 119. [Calibration-Aware Policy Optimization for Reasoning LLMs](https://arxiv.org/abs/2604.12632)

**<font color=#1a73e8>作者：</font>** Ziqi Wang, Xingzhou Lou, Meiqi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) enhances LLM reasoning but often induces overconfidence, where incorrect responses yield lower perplexity than correct ones, degrading relative calibration as described by the Area Under the Curve (AUC). Existing approaches either yield limited improvements in calibration or sacrifice gains in reasoning accuracy. We first prove that this degradation in GRPO-style algorithms stems from their uncertainty-agnostic advantage estimation, which inevitably misaligns optimization gradients with calibration. This leads to improved accuracy at the expense of degraded calibration. We then propose Calibration-Aware Policy Optimization (CAPO). It adopts a logistic AUC surrogate loss that is theoretically consistent and admits regret bound, enabling uncertainty-aware advantage estimation. By further incorporating a noise masking mechanism, CAPO achieves stable learning dynamics that jointly optimize calibration and accuracy. Experiments on multiple mathematical reasoning benchmarks show that CAPO-1.5B significantly improves calibration by up to 15% while achieving accuracy comparable to or better than GRPO, and further boosts accuracy on downstream inference-time scaling tasks by up to 5%. Moreover, when allowed to abstain under low-confidence conditions, CAPO achieves a Pareto-optimal precision-coverage trade-off, highlighting its practical value for hallucination mitigation.

---


### 120. [RPRA: Predicting an LLM-Judge for Efficient but Performant Inference](https://arxiv.org/abs/2604.12634)

**<font color=#1a73e8>作者：</font>** Dylan R. Ashley, Gaël Le Lan, Changsheng Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) face a fundamental trade-off between computational efficiency (e.g., number of parameters) and output quality, especially when deployed on computationally limited devices such as phones or laptops. One way to address this challenge is by following the example of humans and have models ask for help when they believe they are incapable of solving a problem on their own; we can overcome this trade-off by allowing smaller models to respond to queries when they believe they can provide good responses, and deferring to larger models when they do not believe they can. To this end, in this paper, we investigate the viability of Predict-Answer/Act (PA) and Reason-Predict-Reason-Answer/Act (RPRA) paradigms where models predict -- prior to responding -- how an LLM judge would score their output. We evaluate three approaches: zero-shot prediction, prediction using an in-context report card, and supervised fine-tuning. Our results show that larger models (particularly reasoning models) perform well when predicting generic LLM judges zero-shot, while smaller models can reliably predict such judges well after being fine-tuned or provided with an in-context report card. Altogether, both approaches can substantially improve the prediction accuracy of smaller models, with report cards and fine-tuning achieving mean improvements of up to 55% and 52% across datasets, respectively. These findings suggest that models can learn to predict their own performance limitations, paving the way for more efficient and self-aware AI systems.

---


### 121. [TimeSAF: Towards LLM-Guided Semantic Asynchronous Fusion for Time Series Forecasting](https://arxiv.org/abs/2604.12648)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Shiming Fan, Hua Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the recent success of large language models (LLMs) in time-series forecasting, most existing methods still adopt a Deep Synchronous Fusion strategy, where dense interactions between textual and temporal features are enforced at every layer of the network. This design overlooks the inherent granularity mismatch between modalities and leads to what we term semantic perceptual dissonance: high-level abstract semantics provided by the LLM become inappropriately entangled with the low-level, fine-grained numerical dynamics of time series, making it difficult for semantic priors to effectively guide forecasting. To address this issue, we propose TimeSAF, a new framework based on hierarchical asynchronous fusion. Unlike synchronous approaches, TimeSAF explicitly decouples unimodal feature learning from cross-modal interaction. It introduces an independent cross-modal semantic fusion trunk, which uses learnable queries to aggregate global semantics from the temporal and prompt backbones in a bottom-up manner, and a stage-wise semantic refinement decoder that asynchronously injects these high-level signals back into the temporal backbone. This mechanism provides stable and efficient semantic guidance while avoiding interference with low-level temporal dynamics. Extensive experiments on standard long-term forecasting benchmarks show that TimeSAF significantly outperforms state-of-the-art baselines, and further exhibits strong generalization in both few-shot and zero-shot transfer settings.

---


### 122. [PromptEcho: Annotation-Free Reward from Vision-Language Models for Text-to-Image Reinforcement Learning](https://arxiv.org/abs/2604.12652)

**<font color=#1a73e8>作者：</font>** Jinlong Liu, Wanggui He, Peng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can improve the prompt following capability of text-to-image (T2I) models, yet obtaining high-quality reward signals remains challenging: CLIP Score is too coarse-grained, while VLM-based reward models (e.g., RewardDance) require costly human-annotated preference data and additional fine-tuning. We propose PromptEcho, a reward construction method that requires \emph{no} annotation and \emph{no} reward model training. Given a generated image and a guiding query, PromptEcho computes the token-level cross-entropy loss of a frozen VLM with the original prompt as the label, directly extracting the image-text alignment knowledge encoded during VLM pretraining. The reward is deterministic, computationally efficient, and improves automatically as stronger open-source VLMs become available. For evaluation, we develop DenseAlignBench, a benchmark of concept-rich dense captions for rigorously testing prompt following capability. Experimental results on two state-of-the-art T2I models (Z-Image and QwenImage-2512) demonstrate that PromptEcho achieves substantial improvements on DenseAlignBench (+26.8pp / +16.2pp net win rate), along with consistent gains on GenEval, DPG-Bench, and TIIFBench without any task-specific training. Ablation studies confirm that PromptEcho comprehensively outperforms inference-based scoring with the same VLM, and that reward quality scales with VLM size. We will open-source the trained models and the DenseAlignBench.

---


### 123. [From Imitation to Discrimination: Progressive Curriculum Learning for Robust Web Navigation](https://arxiv.org/abs/2604.12666)

**<font color=#1a73e8>作者：</font>** Chuang Peng, Wei Zhang, Renshuai Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-based web agents offer computational efficiency for autonomous web navigation, yet developing robust agents remains challenging due to the noisy and heterogeneous nature of real-world HTML. Standard Supervised Fine-Tuning (SFT) approaches fail in two critical dimensions: they lack discrimination capabilities to reject plausible but incorrect elements in densely populated pages, and exhibit limited generalization to unseen website layouts. To address these challenges, we introduce the Triton dataset (590k instances) and a progressive training curriculum. Triton is constructed via Structural-Semantic Hard Negative Mining, which explicitly mines topologically similar distractors, and a Dual-Agent Consensus pipeline that synthesizes diverse cross-domain tasks with strict verification. Building upon this foundation, our progressive curriculum produces three models: Triton-SFT-32B for basic imitation, Triton-ORPO-32B for robust discrimination via Odds Ratio Preference Optimization, and Triton-GRPO-32B for long-horizon consistency through Group Relative Policy Optimization. Empirical evaluation on Mind2Web demonstrates that Triton-GRPO-32B achieves state-of-the-art performance among open-source models with 58.7% Step Success Rate, surpassing GPT-4.5 (42.4%) and Claude-4.5 (41.4%) by over 16%, validating that specialized data curriculum outweighs raw parameter scale for web navigation.

---


### 124. [Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining](https://arxiv.org/abs/2604.12683)

**<font color=#1a73e8>作者：</font>** Junfeng Xia, Wenhao Ye, Xuanye Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. We present \textit{Brain-DiT}, a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal space or a latent space, \textit{Brain-DiT} adopts metadata-conditioned diffusion pretraining with a Diffusion Transformer (DiT), enabling the model to learn multi-scale representations that capture both fine-grained functional structure and global semantics. Across extensive evaluations and ablations on 7 downstream tasks, we find consistent evidence that diffusion-based generative pretraining is a stronger proxy than reconstruction or alignment, with metadata-conditioned pretraining further improving downstream performance by disentangling intrinsic neural dynamics from population-level variability. We also observe that downstream tasks exhibit distinct preferences for representational scale: ADNI classification benefits more from global semantic representations, whereas age/sex prediction comparatively relies more on fine-grained local structure. Code and parameters of Brain-DiT are available at \href{this https URL}{Link}.

---


### 125. [MISID: A Multimodal Multi-turn Dataset for Complex Intent Recognition in Strategic Deception Games](https://arxiv.org/abs/2604.12700)

**<font color=#1a73e8>作者：</font>** Shufang Lin, Muyang Chen, Xiabing Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding human intent in complex multi-turn interactions remains a fundamental challenge in human-computer interaction and behavioral analysis. While existing intent recognition datasets focus mainly on single utterances or simple dialogues, real-world scenarios often involve sophisticated strategic interactions where participants must maintain complex deceptive narratives over extended periods. To address this gap, we introduce MISID, a comprehensive multimodal, multi-turn, and multi-participant benchmark for intent recognition. Sourced from high-stakes social strategy games, MISID features a fine-grained, two-tier multi-dimensional annotation scheme tailored for long-context discourse analysis and evidence-based causal tracking. Our systematic evaluation of state-of-the-art Multimodal Large Language Models (MLLMs) on MISID reveals critical deficiencies in complex scenarios, including text-prior visual hallucination, impaired cross-modal synergy, and limited capacity in chaining causal cues. Consequently, we propose FRACTAM as a baseline framework. Using a ``Decouple-Anchor-Reason'' paradigm, FRACTAM reduces text bias by extracting pure unimodal factual representations, employs two-stage retrieval for long-range factual anchoring, and constructs explicit cross-modal evidence chains. Extensive experiments demonstrate that FRACTAM enhances mainstream models' performance in complex strategic tasks, improving hidden intent detection and inference while maintaining robust perceptual accuracy. Our dataset is available at this https URL.

---


### 126. [LASA: Language-Agnostic Semantic Alignment at the Semantic Bottleneck for LLM Safety](https://arxiv.org/abs/2604.12710)

**<font color=#1a73e8>作者：</font>** Junxiao Yang, Haoran Liu, Jinzhe Tu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often demonstrate strong safety performance in high-resource languages, yet exhibit severe vulnerabilities when queried in low-resource languages. We attribute this gap to a mismatch between language-agnostic semantic understanding ability and language-dominant safety alignment biased toward high-resource languages. Consistent with this hypothesis, we empirically identify the semantic bottleneck in LLMs, an intermediate layer in which the geometry of model representations is governed primarily by shared semantic content rather than language identity. Building on this observation, we propose Language-Agnostic Semantic Alignment (LASA), which anchors safety alignment directly in semantic bottlenecks. Experiments show that LASA substantially improves safety across all languages: average attack success rate (ASR) drops from 24.7% to 2.8% on LLaMA-3.1-8B-Instruct and remains around 3-4% across Qwen2.5 and Qwen3 Instruct models (7B-32B). Together, our analysis and method offer a representation-level perspective on LLM safety, suggesting that safety alignment requires anchoring safety understanding not in surface text, but in the model's language-agnostic semantic space.

---


### 127. [InsightFlow: LLM-Driven Synthesis of Patient Narratives for Mental Health into Causal Models](https://arxiv.org/abs/2604.12721)

**<font color=#1a73e8>作者：</font>** Shreya Gupta, Prottay Kumar Adhikary, Bhavyaa Dave 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical case formulation organizes patient symptoms and psychosocial factors into causal models, often using the 5P framework. However, constructing such graphs from therapy transcripts is time consuming and varies across clinicians. We present InsightFlow, an LLM based approach that automatically generates 5P aligned causal graphs from patient-therapist dialogues. Using 46 psychotherapy intake transcripts annotated by clinical experts, we evaluate LLM generated graphs against human formulations using structural (NetSimile), semantic (embedding similarity), and expert rated clinical criteria. The generated graphs show structural similarity comparable to inter annotator agreement and high semantic alignment with human graphs. Expert evaluations rate the outputs as moderately complete, consistent, and clinically useful. While LLM graphs tend to form more interconnected structures compared to the chain like patterns of human graphs, overall complexity and content coverage are similar. These results suggest that LLMs can produce clinically meaningful case formulation graphs within the natural variability of expert practice. InsightFlow highlights the potential of automated causal modeling to augment clinical workflows, with future work needed to improve temporal reasoning and reduce redundancy.

---


### 128. [AffectAgent: Collaborative Multi-Agent Reasoning for Retrieval-Augmented Multimodal Emotion Recognition](https://arxiv.org/abs/2604.12735)

**<font color=#1a73e8>作者：</font>** Zeheng Wang, Zitong Yu, Yijie Zhu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLM-based multimodal emotion recognition relies on static parametric memory and often hallucinates when interpreting nuanced affective states. In this paper, given that single-round retrieval-augmented generation is highly susceptible to modal ambiguity and therefore struggles to capture complex affective dependencies across modalities, we introduce AffectAgent, an affect-oriented multi-agent retrieval-augmented generation framework that leverages collaborative decision-making among agents for fine-grained affective understanding. Specifically, AffectAgent comprises three jointly optimized specialized agents, namely a query planner, an evidence filter, and an emotion generator, which collaboratively perform analytical reasoning to retrieve cross-modal samples, assess evidence, and generate predictions. These agents are optimized end-to-end using Multi-Agent Proximal Policy Optimization (MAPPO) with a shared affective reward to ensure consistent emotion understanding. Furthermore, we introduce Modality-Balancing Mixture of Experts (MB-MoE) and Retrieval-Augmented Adaptive Fusion (RAAF), where MB-MoE dynamically regulates the contributions of different modalities to mitigate representation mismatch caused by cross-modal heterogeneity, while RAAF enhances semantic completion under missing-modality conditions by incorporating retrieved audiovisual embeddings. Extensive experiments on MER-UniBench demonstrate that AffectAgent achieves superior performance across complex scenarios. Our code will be released at: this https URL.

---


### 129. [Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood](https://arxiv.org/abs/2604.12736)

**<font color=#1a73e8>作者：</font>** Xingyu Lin, Yilin Wen, Du Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has significantly advanced the reasoning ability of large language models (LLMs), particularly in their mathemat ical reasoning performance. However, GRPO and related entropy regularization methods still struggle with token-level sparse-rewards, which is an inherent chal lenge in chain-of-thought (CoT) reasoning. These approaches often rely on undifferen tiated token-level entropy regularization, which easily leads to entropy collapse or model degradation under sparse token rewards. In this work, we propose TEPO, a novel token-level framework that (1) leverages sequence-level likelihood to link group-level rewards with individual tokens via token-level aggregation, and (2) introduces a token-level KL-Divergence mask constraint that targets tokens with positive advantages and decreasing entropy to mitigate abrupt policy updates. Experiments demonstrate that TEPO not only achieves state-of-the-art performance on mathematical reasoning benchmarks but also markedly enhances training stability, reducing convergence time by 50% compared with GRPO/DAPO.

---


### 130. [Generating Effective CoT Traces for Mitigating Causal Hallucination](https://arxiv.org/abs/2604.12748)

**<font color=#1a73e8>作者：</font>** Yiheng Zhao, Jun Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) excel in complex reasoning tasks, they suffer from severe causal hallucination in event causality identification (ECI), particularly in smaller models ($\leq$1.5B parameters). A promising approach to address this issue is to fine-tune them with Chain-of-Thought (CoT) traces. However, there is currently a lack of CoT trace dataset available for ECI. In this paper, we first investigate the essential criteria that effective CoT traces should possess to mitigate causal hallucination in smaller models. We then design a pipeline to generate CoT traces that meet these criteria. Moreover, since there is currently no metric for quantifying causal hallucination, we also introduce a new metric, the Causal Hallucination Rate (CHR), to quantify causal hallucination, guide the formulation of effective CoT trace criteria, and validate the effectiveness of our pipeline. Our experiments show that fine-tuning with the CoT traces generated by our pipeline not only substantially reduces causal hallucination in smaller LLMs but also improves mean accuracy. Moreover, the fine-tuned models exhibit strong cross-dataset and cross-difficulty generalization, as well as robustness under misleading intervention prompts.

---


### 131. [ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search](https://arxiv.org/abs/2604.12762)

**<font color=#1a73e8>作者：</font>** Myungchul Kim, Kwanyong Park, Junmo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ARGOS, the first benchmark and framework that reformulates multi-camera person search as an interactive reasoning problem requiring an agent to plan, question, and eliminate candidates under information asymmetry. An ARGOS agent receives a vague witness statement and must decide what to ask, when to invoke spatial or temporal tools, and how to interpret ambiguous responses, all within a limited turn budget. Reasoning is grounded in a Spatio-Temporal Topology Graph (STTG) encoding camera connectivity and empirically validated transition times. The benchmark comprises 2,691 tasks across 14 real-world scenarios in three progressive tracks: semantic perception (Who), spatial reasoning (Where), and temporal reasoning (When). Experiments with four LLM backbones show the benchmark is far from solved (best TWS: 0.383 on Track 2, 0.590 on Track 3), and ablations confirm that removing domain-specific tools drops accuracy by up to 49.6 percentage points.

---


### 132. [NaviRAG: Towards Active Knowledge Navigation for Retrieval-Augmented Generation](https://arxiv.org/abs/2604.12766)

**<font color=#1a73e8>作者：</font>** Jihao Dai, Dingjun Wu, Yuxuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) typically relies on a flat retrieval paradigm that maps queries directly to static, isolated text segments. This approach struggles with more complex tasks that require the conditional retrieval and dynamic synthesis of information across different levels of granularity (e.g., from broad concepts to specific evidence). To bridge this gap, we introduce NaviRAG, a novel framework that shifts from passive segment retrieval to active knowledge navigation. NaviRAG first structures the knowledge documents into a hierarchical form, preserving semantic relationships from coarse-grained topics to fine-grained details. Leveraging this reorganized knowledge records, a large language model (LLM) agent actively navigates the records, iteratively identifying information gaps and retrieving relevant content from the most appropriate granularity level. Extensive experiments on long-document QA benchmarks show that NaviRAG consistently improves both retrieval recall and end-to-end answer performance over conventional RAG baselines. Ablation studies confirm performance gains stem from our method's capacity for multi-granular evidence localization and dynamic retrieval planning. We further discuss efficiency, applicable scenario, and future directions of our method, hoping to make RAG systems more intelligent and autonomous.

---


### 133. [CLASP: Class-Adaptive Layer Fusion and Dual-Stage Pruning for Multimodal Large Language Models](https://arxiv.org/abs/2604.12767)

**<font color=#1a73e8>作者：</font>** Yunkai Dang, Yizhu Jiang, Yifan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) suffer from substantial computational overhead due to the high redundancy in visual token sequences. Existing approaches typically address this issue using single-layer Vision Transformer (ViT) features and static pruning strategies. However, such fixed configurations are often brittle under diverse instructions. To overcome these limitations, we propose CLASP, a plug-and-play token reduction framework based on class-adaptive layer fusion and dual-stage pruning. Specifically, CLASP first constructs category-specific visual representations through multi-layer vision feature fusion. It then performs dual-stage pruning, allocating the token budget between attention-salient pivot tokens for relevance and redundancy-aware completion tokens for coverage. Through class-adaptive pruning, CLASP enables prompt-conditioned feature fusion and budget allocation, allowing aggressive yet robust visual token reduction. Extensive experiments demonstrate that CLASP consistently outperforms existing methods across a wide range of benchmarks, pruning ratios, and MLLM architectures. Code will be available at this https URL.

---


### 134. [Teaching LLMs Human-Like Editing of Inappropriate Argumentation via Reinforcement Learning](https://arxiv.org/abs/2604.12770)

**<font color=#1a73e8>作者：</font>** Timon Ziegenbein, Maja Stahl, Henning Wachsmuth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Editing human-written text has become a standard use case of large language models (LLMs), for example, to make one's arguments more appropriate for a discussion. Comparing human to LLM-generated edits, however, we observe a mismatch in editing strategies: While LLMs often perform multiple scattered edits and tend to change meaning notably, humans rather encapsulate dependent changes in self-contained, meaning-preserving edits. In this paper, we present a reinforcement learning approach that teaches LLMs human-like editing to improve the appropriateness of arguments. Our approach produces self-contained sentence-level edit suggestions that can be accepted or rejected independently. We train the approach using group relative policy optimization with a multi-component reward function that jointly optimizes edit-level semantic similarity, fluency, and pattern conformity as well as argument-level appropriateness. In automatic and human evaluation, it outperforms competitive baselines and the state of the art in human-like editing, with multi-round editing achieving appropriateness close to full rewriting.

---


### 135. [Efficient Adversarial Training via Criticality-Aware Fine-Tuning](https://arxiv.org/abs/2604.12780)

**<font color=#1a73e8>作者：</font>** Wenyun Li, Zheng Zhang, Dongmei Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) models have achieved remarkable performance across various vision tasks, with scalability being a key advantage when applied to large datasets. This scalability enables ViT models to exhibit strong generalization capabilities. However, as the number of parameters increases, the robustness of ViT models to adversarial examples does not scale proportionally. Adversarial training (AT), one of the most effective methods for enhancing robustness, typically requires fine-tuning the entire model, leading to prohibitively high computational costs, especially for large ViT architectures. In this paper, we aim to robustly fine-tune only a small subset of parameters to achieve robustness comparable to standard AT. To accomplish this, we introduce Criticality-Aware Adversarial Training (CAAT), a novel method that adaptively allocates resources to the most robustness-critical parameters, fine-tuning only selected modules. Specifically, CAAT efficiently identifies parameters that contribute most to adversarial robustness. It then leverages parameter-efficient fine-tuning (PEFT) to robustly adjust weight matrices where the number of critical parameters exceeds a predefined threshold. CAAT exhibits favorable generalization when scaled to larger vision transformer architectures, potentially paving the way for adversarial training at scale, e.g, compared with plain adversarial training, CAAT incurs only a 4.3% decrease in adversarial robustness while tuning approximately 6% of its parameters. Extensive experiments on three widely used adversarial learning datasets demonstrate that CAAT outperforms state-of-the-art lightweight AT methods with fewer trainable parameters.

---


### 136. [Fragile Reconstruction: Adversarial Vulnerability of Reconstruction-Based Detectors for Diffusion-Generated Images](https://arxiv.org/abs/2604.12781)

**<font color=#1a73e8>作者：</font>** Haoyang Jiang, Mingyang Yi, Shaolei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, detecting AI-generated images produced by diffusion-based models has attracted increasing attention due to their potential threat to safety. Among existing approaches, reconstruction-based methods have emerged as a prominent paradigm for this task. However, we find that such methods exhibit severe security vulnerabilities to adversarial perturbations; that is, by adding imperceptible adversarial perturbations to input images, the detection accuracy of classifiers collapses to near zero. To verify this threat, we present a systematic evaluation of the adversarial robustness of three representative detectors across four diverse generative backbone models. First, we construct adversarial attacks in white-box scenarios, which degrade the performance of all well-trained detectors. Moreover, we find that these attacks demonstrate transferability; specifically, attacks crafted against one detector can be transferred to others, indicating that adversarial attacks on detectors can also be constructed in a black-box setting. Finally, we assess common countermeasures and find that standard defense methods against adversarial attacks provide limited mitigation. We attribute these failures to the low signal-to-noise ratio (SNR) of attacked samples as perceived by the detectors. Overall, our results reveal fundamental security limitations of reconstruction-based detectors and highlight the need to rethink existing detection strategies.

---


### 137. [OSC: Hardware Efficient W4A4 Quantization via Outlier Separation in Channel Dimension](https://arxiv.org/abs/2604.12782)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang, Yanzhao Li, Zhiqiang Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While 4-bit quantization is essential for high-throughput deployment of Large Language Models, activation outliers often lead to significant accuracy degradation due to the restricted dynamic range of low-bit formats. In this paper, we systematically investigate the spatial distribution of outliers and demonstrate a token-persistent structural clustering effect, where high-magnitude outliers consistently occupy fixed channels across tokens. Building on this insight, we propose OSC, a hardware-efficient framework for outlier suppression. During inference, OSC executes a dual-path computation consisting of a low-precision 4-bit General Matrix Multiplication (GEMM) path and a high-precision 16-bit branch GEMM path. Specifically, OSC uses an offline group-wise strategy to identify the channels where outliers are located and then performs structured sub-tensor extraction to coalesce these scattered activation channels into a compact dense tensor online. This mechanism implements outlier protection through regularized and high-throughput GEMM operations, achieving a seamless fit with modern 4-bit micro-scaling hardware. Furthermore, for the inputs of W2 where outlier clustering is less pronounced, we integrate a fallback strategy to FP8. Evaluation on Qwen3-8B and Qwen3-30B restricts the average accuracy drop to 2.19 and 1.12 points, respectively. Notably, OSC is highly hardware-friendly, achieving a peak speedup of 1.78x over the W8A8 GEMM baseline on a modern AI accelerator.

---


### 138. [Interpretable Relational Inference with LLM-Guided Symbolic Dynamics Modeling](https://arxiv.org/abs/2604.12806)

**<font color=#1a73e8>作者：</font>** Xiaoxiao Liang, Juyuan Zhang, Liming Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring latent interaction structures from observed dynamics is a fundamental inverse problem in many-body interacting systems. Most neural approaches rely on black-box surrogates over trainable graphs, achieving accuracy at the expense of mechanistic interpretability. Symbolic regression offers explicit dynamical equations and stronger inductive biases, but typically assumes known topology and a fixed function library. We propose \textbf{COSINE} (\textbf{C}o-\textbf{O}ptimization of \textbf{S}ymbolic \textbf{I}nteractions and \textbf{N}etwork \textbf{E}dges), a differentiable framework that jointly discovers interaction graphs and sparse symbolic dynamics. To overcome the limitations of fixed symbolic libraries, COSINE further incorporates an outer-loop large language model that adaptively prunes and expands the hypothesis space using feedback from the inner optimization loop. Experiments on synthetic systems and large-scale real-world epidemic data demonstrate robust structural recovery and compact, mechanism-aligned dynamical expressions. Code: this https URL.

---


### 139. [DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](https://arxiv.org/abs/2604.12812)

**<font color=#1a73e8>作者：</font>** Hao Yan, Yuliang Liu, Xingchen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low Signal-to-Noise Ratio (SNR), with crucial evidence buried in irrelevant pages; and 2) supervision scarcity, as datasets offering only final short answers provide a weak learning signal. In this paper, we address these challenges by proposing a paradigm that requires the model to execute a structured ``\textbf{Analysis}, \textbf{Localization} and \textbf{Reasoning}'' workflow. To instill this capability, we design a two-stage training framework: we first perform Supervised Fine-Tuning on high-quality data generated via an efficient knowledge distillation strategy. Subsequently, we employ an Evidence-aware Group Relative Policy Optimization which jointly optimizes for both evidence localization and answer accuracy. Additionally, we introduce a Evidence-Guided Resolution Allocation strategy to mitigate memory constraints of training on multi-pages documents. Extensive experiments demonstrate that DocSeeker achieves superior performance on both in-domain and out-of-domain tasks. We show it robustly generalizes from short-page training to ultra-long documents and is naturally synergistic with visual Retrieval-Augmented Generation systems, serving as a solid foundation for their implementation.

---


### 140. [DPC-VQA: Decoupling Quality Perception and Residual Calibration for Video Quality Assessment](https://arxiv.org/abs/2604.12813)

**<font color=#1a73e8>作者：</font>** Xinyue Li, Shubo Xu, Zhichao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have shown promising performance on video quality assessment (VQA) tasks. However, adapting them to new scenarios remains expensive due to large-scale retraining and costly mean opinion score (MOS) annotations. In this paper, we argue that a pretrained MLLM already provides a useful perceptual prior for VQA, and that the main challenge is to efficiently calibrate this prior to the target MOS space. Based on this insight, we propose DPC-VQA, a decoupling perception and calibration framework for video quality assessment. Specifically, DPC-VQA uses a frozen MLLM to provide a base quality estimate and perceptual prior, and employs a lightweight calibration branch to predict a residual correction for target-scenario adaptation. This design avoids costly end-to-end retraining while maintaining reliable performance with lower training and data costs. Extensive experiments on both user-generated content (UGC) and AI-generated content (AIGC) benchmarks show that DPC-VQA achieves competitive performance against representative baselines, while using less than 2% of the trainable parameters of conventional MLLM-based VQA methods and remaining effective with only 20\% of MOS labels. The code will be released upon publication.

---


### 141. [The role of System 1 and System 2 semantic memory structure in human and LLM biases](https://arxiv.org/abs/2604.12816)

**<font color=#1a73e8>作者：</font>** Katherine Abramski, Giulio Rossetti, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Implicit biases in both humans and large language models (LLMs) pose significant societal risks. Dual process theories propose that biases arise primarily from associative System 1 thinking, while deliberative System 2 thinking mitigates bias, but the cognitive mechanisms that give rise to this phenomenon remain poorly understood. To better understand what underlies this duality in humans, and possibly in LLMs, we model System 1 and System 2 thinking as semantic memory networks with distinct structures, built from comparable datasets generated by both humans and LLMs. We then investigate how these distinct semantic memory structures relate to implicit gender bias using network-based evaluation metrics. We find that semantic memory structures are irreducible only in humans, suggesting that LLMs lack certain types of human-like conceptual knowledge. Moreover, semantic memory structure relates consistently to implicit bias only in humans, with lower levels of bias in System~2 structures. These findings suggest that certain types of conceptual knowledge contribute to bias regulation in humans, but not in LLMs, highlighting fundamental differences between human and machine cognition.

---


### 142. [Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory](https://arxiv.org/abs/2604.12817)

**<font color=#1a73e8>作者：</font>** Shaopeng Fu, Di Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial training (AT) is an effective defense for large language models (LLMs) against jailbreak attacks, but performing AT on LLMs is costly. To improve the efficiency of AT for LLMs, recent studies propose continuous AT (CAT) that searches for adversarial inputs within the continuous embedding space of LLMs during AT. While CAT has achieved empirical success, its underlying mechanism, i.e., why adversarial perturbations in the embedding space can help LLMs defend against jailbreak prompts synthesized in the input token space, remains unknown. This paper presents the first theoretical analysis of CAT on LLMs based on in-context learning (ICL) theory. For linear transformers trained with adversarial examples from the embedding space on in-context linear regression tasks, we prove a robust generalization bound that has a negative correlation with the perturbation radius in the embedding space. This clearly explains why CAT can defend against jailbreak prompts from the LLM's token space. Further, the robust bound shows that the robustness of an adversarially trained LLM is closely related to the singular values of its embedding matrix. Based on this, we propose to improve LLM CAT by introducing an additional regularization term, which depends on singular values of the LLM's embedding matrix, into the objective function of CAT. Experiments on real-world LLMs demonstrate that our method can help LLMs achieve a better jailbreak robustness-utility tradeoff. The code is available at this https URL.

---


### 143. [RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair](https://arxiv.org/abs/2604.12820)

**<font color=#1a73e8>作者：</font>** Jagadeesh Rachapudi, Pranav Singh, Ritali Vatsi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) inherently absorb harmful knowledge, misinformation, and personal data during pretraining on large-scale web corpora, with no native mechanism for selective removal. While machine unlearning offers a principled solution, existing approaches are provider-centric, requiring retraining pipelines, curated retain datasets, and direct intervention by model service providers (MSPs), thereby excluding end users from controlling their own data. We introduce Interactive Machine Unlearning (IMU), a new paradigm in which users can instruct LLMs to forget targeted knowledge through natural language at inference time. To realize IMU, we propose RePAIR, a prompt-aware model repair framework comprising (i) a watchdog model for unlearning intent detection, (ii) a surgeon model for generating repair procedures, and (iii) a patient model whose parameters are updated autonomously. At the core of RePAIR, we develop Steering Through Activation Manipulation with PseudoInverse (STAMP), a training-free, single-sample unlearning method that redirects MLP activations toward a refusal subspace via closed-form pseudoinverse updates. Its low-rank variant reduces computational complexity from O(d^3) to O(r^3 + r^2 * d), enabling efficient on-device unlearning with up to ~3x speedup over training-based baselines. Extensive experiments across harmful knowledge suppression, misinformation correction, and personal data erasure demonstrate that RePAIR achieves near-zero forget scores (Acc_f = 0.00, F-RL = 0.00) while preserving model utility (Acc_r up to 84.47, R-RL up to 0.88), outperforming six state-of-the-art baselines. These results establish RePAIR as an effective and practical framework for user-driven model editing, advancing transparent and on-device control over learned knowledge, with potential extensions to multimodal foundation models.

---


### 144. [Challenging Vision-Language Models with Physically Deployable Multimodal Semantic Lighting Attacks](https://arxiv.org/abs/2604.12833)

**<font color=#1a73e8>作者：</font>** Yingying Zhao, Chengyin Hu, Qike Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown remarkable performance, yet their security remains insufficiently understood. Existing adversarial studies focus almost exclusively on the digital setting, leaving physical-world threats largely unexplored. As VLMs are increasingly deployed in real environments, this gap becomes critical, since adversarial perturbations must be physically realizable. Despite this practical relevance, physical attacks against VLMs have not been systematically studied. Such attacks may induce recognition failures and further disrupt multimodal reasoning, leading to severe semantic misinterpretation in downstream tasks. Therefore, investigating physical attacks on VLMs is essential for assessing their real-world security risks. To address this gap, we propose Multimodal Semantic Lighting Attacks (MSLA), the first physically deployable adversarial attack framework against VLMs. MSLA uses controllable adversarial lighting to disrupt multimodal semantic understanding in real scenes, attacking semantic alignment rather than only task-specific outputs. Consequently, it degrades zero-shot classification performance of mainstream CLIP variants while inducing severe semantic hallucinations in advanced VLMs such as LLaVA and BLIP across image captioning and visual question answering (VQA). Extensive experiments in both digital and physical domains demonstrate that MSLA is effective, transferable, and practically realizable. Our findings provide the first evidence that VLMs are highly vulnerable to physically deployable semantic attacks, exposing a previously overlooked robustness gap and underscoring the urgent need for physical-world robustness evaluation of VLMs.

---


### 145. [Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843)

**<font color=#1a73e8>作者：</font>** Eliya Habba, Itay Itzhak, Asaf Yehudai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset. In practice, models are often evaluated on different samples, making scores difficult to compare across studies. To address this, we propose a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. Our approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly. In large-scale experiments on more than $400$ models, our framework predicts full-evaluation performance within 2-3 percentage points using only $100$ anchor questions per dataset, with Spearman $\rho \geq 0.9$ for ranking preservation, showing that it is possible to extend benchmark suites over time while preserving score comparability, at a constant evaluation cost per new dataset. Code available at this https URL

---


### 146. [QuarkMedSearch: A Long-Horizon Deep Search Agent for Exploring Medical Intelligence](https://arxiv.org/abs/2604.12867)

**<font color=#1a73e8>作者：</font>** Zhichao Lin, Zhichao Liang, Gaoqiang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic foundation models continue to evolve, how to further improve their performance in vertical domains has become an important challenge. To this end, building upon Tongyi DeepResearch, a powerful agentic foundation model, we focus on the Chinese medical deep search scenario and propose QuarkMedSearch, systematically exploring a full-pipeline approach spanning medical multi-hop data construction, training strategies, and evaluation benchmarks to further push and assess its performance upper bound in vertical domains. Specifically, for data synthesis, to address the scarcity of deep search training data in the medical domain, we combine a large-scale medical knowledge graph with real-time online exploration to construct long-horizon medical deep search training data; for post-training, we adopt a two-stage SFT and RL training strategy that progressively enhances the model's planning, tool invocation, and reflection capabilities required for deep search, while maintaining search efficiency; for evaluation, we collaborate with medical experts to construct the QuarkMedSearch Benchmark through rigorous manual verification. Experimental results demonstrate that QuarkMedSearch achieves state-of-the-art performance among open-source models of comparable scale on the QuarkMedSearch Benchmark, while also maintaining strong competitiveness on general benchmarks.

---


### 147. [LIFE -- an energy efficient advanced continual learning agentic AI framework for frontier systems](https://arxiv.org/abs/2604.12874)

**<font color=#1a73e8>作者：</font>** Anne Lee, Gurudutt Hosangadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of AI has changed the character of HPC usage such as dimensioning, provisioning, and execution. Not only has energy demand been amplified, but existing rudimentary continual learning capabilities limit ability of AI to effectively manage HPCs. This paper reviews emerging directions beyond monolithic transformers, emphasizing agentic AI and brain inspired architectures as complementary paths toward sustainable, adaptive systems. We propose LIFE, a reasoning and Learning framework that is Incremental, Flexible, and Energy efficient that is implemented as an agent centric system rather than a single monolithic model. LIFE uniquely combines four components to realize self evolving network management and operations in HPCs. The components are an orchestrator, Agentic Context Engineering, a novel memory system, and information lattice learning. LIFE can also generalize to enable a variety of orthogonal use cases. We ground LIFE in a specific closed loop HPC operations example for detecting and mitigating latency spikes experienced by critical micro services running on a Kubernetes like cluster.

---


### 148. [AISafetyBenchExplorer: A Metric-Aware Catalogue of AI Safety Benchmarks Reveals Fragmented Measurement and Weak Benchmark Governance](https://arxiv.org/abs/2604.12875)

**<font color=#1a73e8>作者：</font>** Abiodun A. Solanke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of large language model (LLM) safety evaluation has produced a substantial benchmark ecosystem, but not a correspondingly coherent measurement ecosystem. We present AISafetyBenchExplorer, a structured catalogue of 195 AI safety benchmarks released between 2018 and 2026, organized through a multi-sheet schema that records benchmark-level metadata, metric-level definitions, benchmark-paper metadata, and repository activity. This design enables meta-analysis not only of what benchmarks exist, but also of how safety is operationalized, aggregated, and judged across the literature. Using the updated catalogue, we identify a central structural problem: benchmark proliferation has outpaced measurement standardization. The current landscape is dominated by medium-complexity benchmarks (94/195), while only 7 benchmarks occupy the Popular tier. The workbook further reports strong concentration around English-only evaluation (165/195), evaluation-only resources (170/195), stale GitHub repositories (137/195), stale Hugging Face datasets (96/195), and heavy reliance on arXiv preprints among benchmarks with known venue metadata. At the metric level, the catalogue shows that familiar labels such as accuracy, F1 score, safety score, and aggregate benchmark scores often conceal materially different judges, aggregation rules, and threat models. We argue that the field's main failure mode is fragmentation rather than scarcity. Researchers now have many benchmark artifacts, but they often lack a shared measurement language, a principled basis for benchmark selection, and durable stewardship norms for post publication maintenance. AISafetyBenchExplorer addresses this gap by providing a traceable benchmark catalogue, a controlled metadata schema, and a complexity taxonomy that together support more rigorous benchmark discovery, comparison, and meta-evaluation.

---


### 149. [Towards Long-horizon Agentic Multimodal Search](https://arxiv.org/abs/2604.12890)

**<font color=#1a73e8>作者：</font>** Yifan Du, Zikang Liu, Jinbiao Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal deep search agents have shown great potential in solving complex tasks by iteratively collecting textual and visual evidence. However, managing the heterogeneous information and high token costs associated with multimodal inputs over long horizons remains a critical challenge, as existing methods often suffer from context explosion or the loss of crucial visual signals. To address this, we propose a novel Long-horizon MultiModal deep search framework, named LMM-Searcher, centered on a file-based visual representation mechanism. By offloading visual assets to an external file system and mapping them to lightweight textual identifiers (UIDs), our approach mitigates context overhead while preserving multimodal information for future access. We equip the agent with a tailored fetch-image tool, enabling a progressive, on-demand visual loading strategy for active perception. Furthermore, we introduce a data synthesis pipeline designed to generate queries requiring complex cross-modal multi-hop reasoning. Using this pipeline, we distill 12K high-quality trajectories to fine-tune Qwen3-VL-Thinking-30A3B into a specialized multimodal deep search agent. Extensive experiments across four benchmarks demonstrate that our method successfully scales to 100-turn search horizons, achieving state-of-the-art performance among open-source models on challenging long-horizon benchmarks like MM-BrowseComp and MMSearch-Plus, while also exhibiting strong generalizability across different base models. Our code will be released in this https URL.

---


### 150. [Don't Show Pixels, Show Cues: Unlocking Visual Tool Reasoning in Language Models via Perception Programs](https://arxiv.org/abs/2604.12896)

**<font color=#1a73e8>作者：</font>** Muhammad Kamran Janjua, Hugo Silva, Di Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal language models (MLLMs) are increasingly paired with vision tools (e.g., depth, flow, correspondence) to enhance visual reasoning. However, despite access to these tool-generated visual cues, MLLMs often fail to benefit from them. Existing approaches typically feed raw tool outputs into the model, but these dense, pixel-level representations are misaligned with the language-native reasoning strengths of LLMs, leading to weak perception and reliance on language priors. We argue that, in problems where vision tools can provide the necessary visual cues, the bottleneck is not more tool calls or larger MLLMs, it is how tool outputs are represented. We introduce Perception Programs (P$^2$), a training-free, model-agnostic method that rewrites tool outputs into compact, structured, language-native summaries that MLLMs can directly parse and reason over. Across six perception-centric tasks in BLINK, P$^2$ consistently yields large improvements over base models and raw tool-augmented baselines. With GPT-5 Mini as the base model, P$^2$ raises its accuracy from 41.35\% to 86.47\% on multi-view reasoning, from 52.42\% to 81.45\% on relative depth, and achieves a 22\% average gain across tasks, setting new state-of-the-art results. Even on smaller MLLMs, e.g., InternVL3.5-4B and Qwen3VL-4B, we observe 15-40\% absolute gains from P$^2$, surpassing prior agentic, supervised, and RL-based tool-use methods-without any training or model modifications.

---


### 151. [BEAM: Bi-level Memory-adaptive Algorithmic Evolution for LLM-Powered Heuristic Design](https://arxiv.org/abs/2604.12898)

**<font color=#1a73e8>作者：</font>** Chuyang Xiang, Yichen Wei, Jiale Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model-based Hyper Heuristic (LHH) has recently emerged as an efficient way for automatic heuristic design. However, most existing LHHs just perform well in optimizing a single function within a pre-defined solver. Their single-layer evolution makes them not effective enough to write a competent complete solver. While some variants incorporate hyperparameter tuning or attempt to generate complex code through iterative local modifications, they still lack a high-level algorithmic modeling, leading to limited exploration efficiency. To address this, we reformulate heuristic design as a Bi-level Optimization problem and propose \textbf{BEAM} (Bi-level Memory-adaptive Algorithmic Evolution). BEAM's exterior layer evolves high-level algorithmic structures with function placeholders through genetic algorithm (GA), while the interior layer realizes these placeholders via Monte Carlo Tree Search (MCTS). We further introduce an Adaptive Memory module to facilitate complex code generation. To support the evaluation for complex code generation, we point out the limitations of starting LHHs from scratch or from code templates and introduce a Knowledge Augmentation (KA) Pipeline. Experimental results on several optimization problems demonstrate that BEAM significantly outperforms existing LHHs, notably reducing the optimality gap by 37.84\% on aggregate in CVRP hybrid algorithm design. BEAM also designs a heuristic that outperforms SOTA Maximum Independent Set (MIS) solver KaMIS.

---


### 152. [MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models](https://arxiv.org/abs/2604.12928)

**<font color=#1a73e8>作者：</font>** Chung-Ming Chien, Manu Orsini, Eugene Kharitonov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI. In particular, full-duplex models are distinguished by their real-time interactivity, including handling of pauses, interruptions, and backchannels. However, improving their factuality remains an open challenge. While scaling the model size could address this gap, it would make real-time inference prohibitively expensive. In this work, we propose MoshiRAG, a modular approach that combines a compact full-duplex interface with selective retrieval to access more powerful knowledge sources. Our asynchronous framework enables the model to identify knowledge-demanding queries and ground its responses in external information. By leveraging the natural temporal gap between response onset and the delivery of core information, the retrieval process can be completed while maintaining a natural conversation flow. With this approach, MoshiRAG achieves factuality comparable to the best publicly released non-duplex speech language models while preserving the interactivity inherent to full-duplex systems. Moreover, our flexible design supports plug-and-play retrieval methods without retraining and demonstrates strong performance on out-of-domain mathematical reasoning tasks.

---


### 153. [Task Alignment: A simple and effective proxy for model merging in computer vision](https://arxiv.org/abs/2604.12935)

**<font color=#1a73e8>作者：</font>** Pau de Jorge, César Roberto de Souza, Björn Michele 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficiently merging several models fine-tuned for different tasks, but stemming from the same pretrained base model, is of great practical interest. Despite extensive prior work, most evaluations of model merging in computer vision are restricted to image classification using CLIP, where different classification datasets define different tasks. In this work, our goal is to make model merging more practical and show its relevance on challenging scenarios beyond this specific setting. In most vision scenarios, different tasks rely on trainable and usually heterogeneous decoders. Differently from previous studies with frozen decoders, where merged models can be evaluated right away, the non-trivial cost of decoder training renders hyperparameter selection based on downstream performance impractical. To address this, we introduce the task alignment proxy, and show how it can be used to speed up hyperparameter selection by orders of magnitude while retaining performance. Equipped with the task alignment proxy, we extend the applicability of model merging to multi-task vision models beyond CLIP-based classification.

---


### 154. [Distorted or Fabricated? A Survey on Hallucination in Video LLMs](https://arxiv.org/abs/2604.12944)

**<font color=#1a73e8>作者：</font>** Yiyang Huang, Yitian Zhang, Yizhou Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in video-language modeling, hallucinations remain a persistent challenge in Video Large Language Models (Vid-LLMs), referring to outputs that appear plausible yet contradict the content of the input video. This survey presents a comprehensive analysis of hallucinations in Vid-LLMs and introduces a systematic taxonomy that categorizes them into two core types: dynamic distortion and content fabrication, each comprising two subtypes with representative cases. Building on this taxonomy, we review recent advances in the evaluation and mitigation of hallucinations, covering key benchmarks, metrics, and intervention strategies. We further analyze the root causes of dynamic distortion and content fabrication, which often result from limited capacity for temporal representation and insufficient visual grounding. These insights inform several promising directions for future work, including the development of motion-aware visual encoders and the integration of counterfactual learning techniques. This survey consolidates scattered progress to foster a systematic understanding of hallucinations in Vid-LLMs, laying the groundwork for building robust and reliable video-language systems. An up-to-date curated list of related works is maintained at this https URL .

---


### 155. [Parcae: Scaling Laws For Stable Looped Language Models](https://arxiv.org/abs/2604.12946)

**<font color=#1a73e8>作者：</font>** Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional fixed-depth architectures scale quality by increasing training FLOPs, typically through increased parameterization, at the expense of a higher memory footprint, or data. A potential alternative is looped architectures, which instead increase FLOPs by sending activations through a block of layers in a loop. While promising, existing recipes for training looped architectures can be unstable, suffering from residual explosion and loss spikes. We address these challenges by recasting looping as a nonlinear time-variant dynamical system over the residual stream. Via a linear approximation to this system, we find that instability occurs in existing looped architectures as a result of large spectral norms in their injection parameters. To address these instability issues, we propose Parcae, a novel stable, looped architecture that constrains the spectral norm of the injection parameters via discretization of a negative diagonal parameterization. As a result, Parcae achieves up to 6.3% lower validation perplexity over prior large-scale looped models. Using our stable looped architecture, we investigate the scaling properties of looping as a medium to improve quality by increasing FLOPs in training and test-time. For training, we derive predictable power laws to scale FLOPs while keeping parameter count fixed. Our initial scaling laws suggest that looping and data should be increased in tandem, given a fixed FLOP budget. At test-time, we find that Parcae can use looping to scale compute, following a predictable, saturating exponential decay. When scaled up to 1.3B parameters, we find that Parcae improves CORE and Core-Extended quality by 2.99 and 1.18 points when compared to strong Transformer baselines under a fixed parameter and data budget, achieving a relative quality of up to 87.5% a Transformer twice the size.

---


### 156. [Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents](https://arxiv.org/abs/2604.12948)

**<font color=#1a73e8>作者：</font>** Benjamin Stern, Peter Nadel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents with persistent memory store information as flat factual records, providing little context for temporal reasoning, change tracking, or cross-session aggregation. Inspired by the drawing effect [3], we introduce dual-trace memory encoding. In this method, each stored fact is paired with a concrete scene trace, a narrative reconstruction of the moment and context in which the information was learned. The agent is forced to commit to specific contextual details during encoding, creating richer, more distinctive memory traces. Using the LongMemEval-S benchmark (4,575 sessions, 100 recall questions), we compare dual-trace encoding against a fact-only control with matched coverage and format over 99 shared questions. Dual-trace achieves 73.7% overall accuracy versus 53.5%, a +20.2 percentage point (pp) gain (95% CI: [+12.1, +29.3], bootstrap p < 0.0001). Gains concentrate in temporal reasoning (+40pp), knowledge-update tracking (+25pp), and multi-session aggregation (+30pp), with no benefit for single-session retrieval, consistent with encoding specificity theory [8]. Token analysis shows dual-trace encoding achieves this gain at no additional cost. We additionally sketch an architectural design for adapting dual-trace encoding to coding agents, with preliminary pilot validation.

---


### 157. [Modeling Co-Pilots for Text-to-Model Translation](https://arxiv.org/abs/2604.12955)

**<font color=#1a73e8>作者：</font>** Serdar Kadioglu, Karthik Uppuluri, Akash Singirikonda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is growing interest in leveraging large language models (LLMs) for text-to-model translation and optimization tasks. This paper aims to advance this line of research by introducing \textsc{Text2Model} and \textsc{Text2Zinc}. \textsc{Text2Model} is a suite of co-pilots based on several LLM strategies with varying complexity, along with an online leaderboard. \textsc{Text2Zinc} is a cross-domain dataset for capturing optimization and satisfaction problems specified in natural language, along with an interactive editor with built-in AI assistant. While there is an emerging literature on using LLMs for translating combinatorial problems into formal models, our work is the first attempt to integrate \textit{both} satisfaction and optimization problems within a \textit{unified architecture} and \textit{dataset}. Moreover, our approach is \textit{solver-agnostic} unlike existing work that focuses on translation to a solver-specific model. To achieve this, we leverage \textsc{MiniZinc}'s solver-and-paradigm-agnostic modeling capabilities to formulate combinatorial problems. We conduct comprehensive experiments to compare execution and solution accuracy across several single- and multi-call strategies, including; zero-shot prompting, chain-of-thought reasoning, intermediate representations via knowledge-graphs, grammar-based syntax encoding, and agentic approaches that decompose the model into sequential sub-tasks. Our co-pilot strategies are competitive, and in parts improve, recent research in this domain. Our findings indicate that while LLMs are promising they are not yet a push-button technology for combinatorial modeling. We contribute \textsc{Text2Model} co-pilots and leaderboard, and \textsc{Text2Zinc} and interactive editor to open-source to support closing this performance gap.

---


### 158. [Boosting Visual Instruction Tuning with Self-Supervised Guidance](https://arxiv.org/abs/2604.12966)

**<font color=#1a73e8>作者：</font>** Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) perform well on many vision-language tasks but often struggle with vision-centric problems that require fine-grained visual reasoning. Recent evidence suggests that this limitation arises not from weak visual representations, but from under-utilization of visual information during instruction tuning, where many tasks can be partially solved using language priors alone. We propose a simple and lightweight approach that augments visual instruction tuning with a small number of visually grounded self-supervised tasks expressed as natural language instructions. By reformulating classical self-supervised pretext tasks, such as rotation prediction, color matching, and cross-view correspondence, as image-instruction-response triplets, we introduce supervision that cannot be solved without relying on visual evidence. Our approach requires no human annotations, no architectural modifications, and no additional training stages. Across multiple models, training regimes, and benchmarks, injecting only a small fraction (3-10%) of such visually grounded instructions consistently improves performance on vision-centric evaluations. Our findings highlight instruction tuning with visually grounded SSL tasks as a powerful lever for improving visual reasoning in MLLMs through simple adjustments to the training data distribution. Code available at: this https URL

---


### 159. [PolicyLLM: Towards Excellent Comprehension of Public Policy for Large Language Models](https://arxiv.org/abs/2604.12995)

**<font color=#1a73e8>作者：</font>** Han Bao, Penghao Zhang, Yue Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into real-world decision-making, including in the domain of public policy. Yet, their ability to comprehend and reason about policy-related content remains underexplored. To fill this gap, we present \textbf{\textit{PolicyBench}}, the first large-scale cross-system benchmark (US-China) evaluating policy comprehension, comprising 21K cases across a broad spectrum of policy areas, capturing the diversity and complexity of real-world governance. Following Bloom's taxonomy, the benchmark assesses three core capabilities: (1) \textbf{Memorization}: factual recall of policy knowledge, (2) \textbf{Understanding}: conceptual and contextual reasoning, and (3) \textbf{Application}: problem-solving in real-life policy scenarios. Building on this benchmark, we further propose \textbf{\textit{PolicyMoE}}, a domain-specialized Mixture-of-Experts (MoE) model with expert modules aligned to each cognitive level. The proposed models demonstrate stronger performance on application-oriented policy tasks than on memorization or conceptual understanding, and yields the highest accuracy on structured reasoning tasks. Our results reveal key limitations of current LLMs in policy understanding and suggest paths toward more reliable, policy-focused models.

---


### 160. [Agentic Discovery with Active Hypothesis Exploration for Visual Recognition](https://arxiv.org/abs/2604.12999)

**<font color=#1a73e8>作者：</font>** Jaywon Koo, Jefferson Hernandez, Ruozhen He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HypoExplore, an agentic framework that formulates neural architecture discovery for visual recognition as a hypothesis-driven scientific inquiry. Given a human-specified high-level research direction, HypoExplore ideates, implements, evaluates, and improves neural architectures through evolutionary branching. New hypotheses are created using a large language model by selecting a parent hypothesis to build upon, guided by a dual strategy that balances exploiting validated principles with resolving uncertain ones. Our proposed framework maintains a Trajectory Tree that records the lineage of all proposed architectures, and a Hypothesis Memory Bank that actively tracks confidence scores acquired through experimental evidence. After each experiment, multiple feedback agents analyze the results from different perspectives and consolidate their findings into hypothesis confidence updates. Our framework is tested on discovering lightweight vision architectures on CIFAR-10, with the best achieving 94.11% accuracy evolved from a root node baseline that starts at 18.91%, and generalizes to CIFAR-100 and Tiny-ImageNet. We further demonstrate applicability to a specialized domain by conducting independent architecture discovery runs on MedMNIST, which yield a state-of-the-art performance. We show that hypothesis confidence scores grow increasingly predictive as evidence accumulates, and that the learned principles transfer across independent evolutionary lineages, suggesting that HypoExplore not only discovers stronger architectures, but can help build a genuine understanding of the design space.

---


### 161. [One Token Away from Collapse: The Fragility of Instruction-Tuned Helpfulness](https://arxiv.org/abs/2604.13006)

**<font color=#1a73e8>作者：</font>** Erfan Baghaei Potraghloo, Seyedarmin Azizi, Souvik Kundu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned large language models produce helpful, structured responses, but how robust is this helpfulness when trivially constrained? We show that simple lexical constraints (banning a single punctuation character or common word) cause instruction-tuned LLMs to collapse their responses, losing 14--48% of comprehensiveness in pairwise evaluation across three open-weight model families and one closed-weight model (GPT-4o-mini). The baseline response is preferred in 77--100% of 1,920 pairwise comparisons judged by GPT-4o-mini and GPT-4o. Notably, GPT-4o-mini suffers 31% comprehensiveness loss (99% baseline win rate), demonstrating that the fragility extends to commercially deployed closed-weight models, contrary to prior findings on format-level constraints. Through mechanistic analysis, we identify this as a planning failure: two-pass generation (free generation followed by constrained rewriting) recovers 59--96% of response length, and linear probes on prompt representations predict response length with $R^2 = 0.51$--$0.93$ before generation begins, with $R^2$ tracking collapse severity across models. The same probes yield negative $R^2$ on base models, confirming that instruction tuning creates the representational structure encoding the collapse decision. Crucially, base models show no systematic collapse under identical constraints, with effects that are small, noisy, and bidirectional, demonstrating that instruction tuning creates this fragility by coupling task competence to narrow surface-form templates. The effect replicates on MT-Bench across all eight task categories. We further show that standard independent LLM-as-judge evaluation detects only a 3.5% average quality drop where pairwise evaluation reveals 23%, exposing a methodological blind spot in how constrained generation is assessed.

---


### 162. [Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation](https://arxiv.org/abs/2604.13010)

**<font color=#1a73e8>作者：</font>** Yecheng Wu, Song Han, Hai Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as an efficient post-training paradigm for large language models. However, standard OPD requires a live teacher inference server throughout training, resulting in substantial infrastructure overhead. In this work, we investigate whether on-policy distillation can be performed offline. A natural approach is to precompute teacher log-probabilities once over SFT rollouts and reuse them during training. In practice, however, this offline variant fails to reliably match the performance of standard OPD. To understand this discrepancy, we identify a previously overlooked condition that is critical for any OPD pipeline, which we term teacher consistency. This condition requires that the same teacher model be used for both supervised fine-tuning and OPD. We show that violating teacher consistency introduces an irreducible gradient bias, causing both offline and online OPD to converge to a suboptimal fixed point regardless of training duration. Building on this insight, we propose Lightning OPD, an offline on-policy distillation framework that enforces teacher consistency by precomputing teacher log-probabilities over SFT rollouts. This design eliminates the need for a live teacher server entirely. We further show that, under teacher consistency, Lightning OPD shares the same optimum as standard OPD, with bounded gradient discrepancy and an implicit regularization effect that helps prevent policy drift. Extensive experiments on mathematical reasoning and code generation demonstrate that Lightning OPD achieves state-of-the-art performance with significantly improved efficiency. Starting from an SFT-initialized Qwen3-8B-Base model, Lightning OPD reaches 69.9% on AIME 2024 in just 30 GPU hours, achieving a 4.0x speedup over standard OPD and substantially lowering the barrier to entry for academic research on LLM post-training.

---


### 163. [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](https://arxiv.org/abs/2604.13016)

**<font color=#1a73e8>作者：</font>** Yaxuan Li, Yuxin Zuo, Bingxiang He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become a core technique in the post-training of large language models, yet its training dynamics remain poorly understood. This paper provides a systematic investigation of OPD dynamics and mechanisms. We first identify that two conditions govern whether OPD succeeds or fails: (i) the student and teacher should share compatible thinking patterns; and (ii) even with consistent thinking patterns and higher scores, the teacher must offer genuinely new capabilities beyond what the student has seen during training. We validate these findings through weak-to-strong reverse distillation, showing that same-family 1.5B and 7B teachers are distributionally indistinguishable from the student's perspective. Probing into the token-level mechanism, we show that successful OPD is characterized by progressive alignment on high-probability tokens at student-visited states, a small shared token set that concentrates most of the probability mass (97%-99%). We further propose two practical strategies to recover failing OPD: off-policy cold start and teacher-aligned prompt selection. Finally, we show that OPD's apparent free lunch of dense token-level reward comes at a cost, raising the question of whether OPD can scale to long-horizon distillation.

---


### 164. [Representation geometry shapes task performance in vision-language modeling for CT enterography](https://arxiv.org/abs/2604.13021)

**<font color=#1a73e8>作者：</font>** Cristian Minoccheri, Emily Wittrup, Kayvan Najarian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) enterography is a primary imaging modality for assessing inflammatory bowel disease (IBD), yet the representational choices that best support automated analysis of this modality are unknown. We present the first study of vision-language transfer learning on abdominal CT enterography and identify two main findings. First, mean pooling of slice embeddings gives better categorical disease assessment (59.2\% three-class accuracy), whereas attention pooling gives better cross-modal retrieval (0.235 text-to-image MRR). This pattern holds across all LoRA configurations tested and suggests that the two aggregators emphasize different properties of the learned representation. Second, per-slice tissue contrast matters more than broader spatial coverage: multi-window RGB encoding, which maps complementary Hounsfield Unit windows to RGB channels, outperforms all strategies that increase spatial coverage through multiplanar sampling, and in this setting adding coronal and sagittal views reduces classification performance. For report generation, fine-tuning without retrieval context yields within-1 severity accuracy at the prevalence-matched chance level (70.4\% vs.\ 71\% random), suggesting little learned ordering beyond the class distribution. Retrieval-augmented generation (RAG) improves this across all configurations, scoring 7--14 percentage points above the chance baseline and improving ordinal MAE from 0.98 to 0.80--0.89. A three-teacher pseudolabel framework enables all comparisons without expert annotations. Together, these findings provide the first baselines for this underexplored modality and offer practical guidance for building vision-language systems for volumetric medical imaging.

---


### 165. [SceneCritic: A Symbolic Evaluator for 3D Indoor Scene Synthesis](https://arxiv.org/abs/2604.13035)

**<font color=#1a73e8>作者：</font>** Kathakoli Sengupta, Kai Ao, Paola Cascante-Bonilla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and Vision-Language Models (VLMs) increasingly generate indoor scenes through intermediate structures such as layouts and scene graphs, yet evaluation still relies on LLM or VLM judges that score rendered views, making judgments sensitive to viewpoint, prompt phrasing, and hallucination. When the evaluator is unstable, it becomes difficult to determine whether a model has produced a spatially plausible scene or whether the output score reflects the choice of viewpoint, rendering, or prompt. We introduce SceneCritic, a symbolic evaluator for floor-plan-level layouts. SceneCritic's constraints are grounded in SceneOnto, a structured spatial ontology we construct by aggregating indoor scene priors from 3D-FRONT, ScanNet, and Visual Genome. SceneOnto traverses this ontology to jointly verify semantic, orientation, and geometric coherence across object relationships, providing object-level and relationship-level assessments that identify specific violations and successful placements. Furthermore, we pair SceneCritic with an iterative refinement test bed that probes how models build and revise spatial structure under different critic modalities: a rule-based critic using collision constraints as feedback, an LLM critic operating on the layout as text, and a VLM critic operating on rendered observations. Through extensive experiments, we show that (a) SceneCritic aligns substantially better with human judgments than VLM-based evaluators, (b) text-only LLMs can outperform VLMs on semantic layout quality, and (c) image-based VLM refinement is the most effective critic modality for semantic and orientation correction.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
