# 🧠 大模型相关研究 | 2026年05月06日

> 本类共 **203** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 1. [Agentopic: A Generative AI Agent Workflow for Explainable Topic Modeling](https://arxiv.org/abs/2605.00833)

**<font color=#1a73e8>作者：</font>** Brice Valentin Kok-Shun, Johnny Chan, Gabrielle Peko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentopic is a novel agent-based workflow for explainable topic modeling that leverages the reasoning capabilities of Large Language Models (LLMs). Existing topic modeling approaches such as Latent Dirichlet Allocation (LDA) and BERTopic often lack transparency on how topics are assigned or grouped. Agentopic addresses this by using multiple agents that collaboratively perform topic identification, validation, hierarchical grouping, and natural language explanation. This design enables users to trace the reasoning behind topic assignments, enhancing interpretability without sacrificing accuracy. When seeded with topics from the British Broadcasting Corporation (BBC) dataset, Agentopic achieves an F1-score of 0.95, matching GPT-4.1, improving on LDA (0.93), and close to BERTopic (0.98). We used Agentopic to augment the BBC dataset with generated explanations to improve the dataset's richness and context. The unseeded Agentopic generated 2045 semantically coherent topics organized across six hierarchical levels, vastly enriching the original five-category structure. By embedding explainability throughout the workflow, Agentopic offers an interpretable alternative to black-box models, making it particularly valuable for crucial applications like finance and healthcare.

---


### 2. [Understanding Emergent Misalignment via Feature Superposition Geometry](https://arxiv.org/abs/2605.00842)

**<font color=#1a73e8>作者：</font>** Gouki Minegishi, Hiroki Furuta, Takeshi Kojima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment, where fine-tuning on narrow, non-harmful tasks induces harmful behaviors, poses a key challenge for AI safety in LLMs. Despite growing empirical evidence, its underlying mechanism remains unclear. To uncover the reason behind this phenomenon, we propose a geometric account based on the geometry of feature superposition. Because features are encoded in overlapping representations, fine-tuning that amplifies a target feature also unintentionally strengthens nearby harmful features in accordance with their similarity. We give a simple gradient-level derivation of this effect and empirically test it in multiple LLMs (Gemma-2 2B/9B/27B, LLaMA-3.1 8B, GPT-OSS 20B). Using sparse autoencoders (SAEs), we identify features tied to misalignment-inducing data and to harmful behaviors, and show that they are geometrically closer to each other than features derived from non-inducing data. This trend generalizes across domains (e.g., health, career, legal advice). Finally, we show that a geometry-aware approach, filtering training samples closest to toxic features, reduces misalignment by 34.5%, substantially outperforming random removal and achieving comparable or slightly lower misalignment than LLM-as-a-judge-based filtering. Our study links emergent misalignment to feature superposition, providing a basis for understanding and mitigating this phenomenon.

---


### 3. [ClinicBot: A Guideline-Grounded Clinical Chatbot with Prioritized Evidence RAG and Verifiable Citations](https://arxiv.org/abs/2605.00846)

**<font color=#1a73e8>作者：</font>** Navapat Nananukul, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis requires answers that are accurate, verifiable, and explicitly grounded in official guidelines. While large language models excel at natural language processing, their tendency to hallucinate undermines their utility in high-stakes medical contexts where precision is essential. Existing retrieval-augmented generation (RAG) systems treat all evidence equally, producing noisy context and generic answers misaligned with clinical practice. We present ClinicBot, an AI system that translates guideline recommendations into trustworthy clinical support through three key advances: (1) structured extraction of clinical guidelines into semantic units (recommendations, tables, definitions, narrative) with explicit provenance, (2) evidence prioritization that ranks content by clinical significance and guideline structure rather than textual similarity, and (3) a web-based interface that presents concise, actionable answers with verifiable evidence. We will demonstrate ClinicBot using diabetes questions from real patients and an additional diabetes risk assessment tool that is faithful to the American Diabetes Association (ADA) Standards of Care in Diabetes (2025). The demonstration will illustrate how semantic knowledge extraction and hierarchical evidence ranking can reliably operate in a multi-agent setting to process complex clinical guidelines at scale.

---


### 4. [H-Probes: Extracting Hierarchical Structures From Latent Representations of Language Models](https://arxiv.org/abs/2605.00847)

**<font color=#1a73e8>作者：</font>** Cutter Dawes, Aryan Sharma, Angelos Ioannis Lagos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representing and navigating hierarchy is a fundamental primitive of reasoning. Large language models have demonstrated proficiency in a wide variety of tasks requiring hierarchical reasoning, but there exists limited analysis on how the models geometrically represent the necessary latent constructions for such thinking. To this end, we develop \textit{H-probes}, a collection of linear probes that extract hierarchical structure, specifically depth and pairwise distance, from latent representations. In synthetic tree traversal tasks, the H-probes robustly find the subspaces containing hierarchical structure necessary to complete the tasks; furthermore, in comprehensive ablation experiments, we show that these hierarchy-containing subspaces are low-dimensional, causally important for high task performance, and generalize within- and out-of-domain. Furthermore, we find analogous, though weaker, hierarchical structure in real-world hierarchical contexts such as mathematical reasoning traces. These results demonstrate that models represent hierarchy not only at the level of syntax and concepts, but at deeper levels of abstraction -- including the reasoning process itself.

---


### 5. [GAZE: Grounded Agentic Zero-shot Evaluation with Viewer-Level Tools and Literature Retrieval on Rare Brain MRI](https://arxiv.org/abs/2605.00876)

**<font color=#1a73e8>作者：</font>** Duaa Alim, Mogtaba Alim, Liam Chalcroft  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) read an image and produce text in a single forward pass, whereas radiologists typically inspect an image several times and consult the literature before writing a report. We introduce GAZE (Grounded Agentic Zero-shot Evaluation), a framework that lets a medical VLM work in this iterative way by calling viewer-level tools (zoom, windowing, contrast, edge detection) and two retrieval tools backed by the U.S. National Library of Medicine (PubMed for medical literature, Open-i for radiological images), with structured outputs validated against a schema and full tool-call traces recorded for auditability. On NOVA, a benchmark of 906 brain MRI cases covering 281 rare neurological conditions, GAZE reaches 58.2 mean average precision (mAP) at intersection-over-union (IoU) 0.3 for lesion localisation and 34.9% Top-1 diagnostic accuracy under a joint protocol that scores captioning, diagnosis, and localisation from the image alone, without task-specific fine-tuning. Before any tool is used, structured prompting and schema-validated outputs already improve over the published Gemini 2.0 Flash baseline (20.2 to 29.4 mAP@0.3), so framework design is itself an experimental variable. Tool use helps rare pathologies disproportionately: the fraction of cases with IoU > 0.3 rises from 17% to 58% for diagnoses with three or fewer examples versus 25% to 68% for common conditions ($\geq$10 cases), with gains tracking engagement (Gemini 3 Flash: Cohen's d = 0.79, 11.8 tool calls per case; Gemini 2.0 Flash: tools used in 8.2% of cases, no significant benefit). Retrieval ablations additionally reveal a model-dependent trade-off in which gains in diagnosis can coincide with losses in localisation, reinforcing the case for joint evaluation of diagnosis, localisation, and captioning in medical VLMs.

---


### 6. [X2SAM: Any Segmentation in Images and Videos](https://arxiv.org/abs/2605.00891)

**<font color=#1a73e8>作者：</font>** Hao Wang, Limeng Qiao, Chi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong image-level visual understanding and reasoning, yet their pixel-level perception across both images and videos remains limited. Foundation segmentation models such as the SAM series produce high-quality masks, but they rely on low-level visual prompts and cannot natively interpret complex conversational instructions. Existing segmentation MLLMs narrow this gap, but are usually specialized for either images or videos and rarely support both textual and visual prompts in one interface. We introduce X2SAM, a unified segmentation MLLM that extends any-segmentation capabilities from images to videos. Given conversational instructions and visual prompts, X2SAM couples an LLM with a Mask Memory module that stores guided vision features for temporally consistent video mask generation. The same formulation supports generic, open-vocabulary, referring, reasoning, grounded conversation generation, interactive, and visual grounded segmentation across image and video inputs. We further introduce the Video Visual Grounded (V-VGD) segmentation benchmark, which evaluates whether a model can segment object tracks in videos from interactive visual prompts. With a unified joint training strategy over heterogeneous image and video datasets, X2SAM delivers strong video segmentation performance, remains competitive on image segmentation benchmarks, and preserves general image and video chat ability.

---


### 7. [Validation of Whole-Slide Foundation Models for Image Retrieval in TCGA Data](https://arxiv.org/abs/2605.00902)

**<font color=#1a73e8>作者：</font>** Tianhao Lei, Parsa Esmaeilkhani, Saghir Alfasly 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are reshaping computational histopathology, yet their value for whole-slide image retrieval relative to strong patch-based and supervised aggregation baselines remains unclear. We benchmarked ten pipelines on 9,387 diagnostic slides spanning 17 organs and 60 diagnoses from The Cancer Genome Atlas (TCGA) using patient-level leave-one-patient-out evaluation. Methods included four pre-trained slide foundation models, a supervised attention-based multiple instance learning (ABMIL) aggregator on patch embeddings, and patch-level retrieval across five sampling densities.
Performance varied more across organs and diagnoses than across architectures. Although the slide foundation model TITAN achieved the strongest overall results, its advantage was modest; ABMIL and patch-based methods reached comparable Top-1 and Top-3 accuracy, with no model consistently dominant. Morphologically distinctive entities approached ceiling performance, while rare, heterogeneous, and closely related subtypes remained challenging. Misclassifications aligned with organs exhibiting known inter-observer variability, suggesting an intrinsic ceiling for morphology-only retrieval.
Performance was driven primarily by patch-level feature representations, with limited benefit from slide-level aggregation, indicating aggregation may be unnecessary in many settings. These findings argue against a universally optimal architecture and instead support organ-resolved benchmarking, diagnosis-aware or ensemble strategies, stronger feature representations, and multimodal retrieval frameworks. Notably, even the best model achieved only $\approx 68\% \pm 21\%$ retrieval accuracy on TCGA, and some subtypes showed $0\%$ accuracy across all methods, highlighting fundamental limitations of morphology-based representations and the need for substantial progress before reliable clinical deployment.

---


### 8. [Generalized Category Discovery under Domain Shifts: From Vision to Vision-Language Models](https://arxiv.org/abs/2605.00906)

**<font color=#1a73e8>作者：</font>** Hongjun Wang, Po Hu, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) aims to categorize unlabelled instances from both known and unknown classes by transferring knowledge from labelled data of known classes. Existing methods assume all data comes from a single domain, yet real-world unlabelled data often exhibits domain shifts alongside semantic shifts. We study GCD under domain shifts and propose three frameworks that adapt foundation models, ranging from self-supervised vision models to vision-language models. (i) HiLo disentangles domain and semantic features through multi-level feature extraction and mutual information minimization, combined with PatchMix augmentation and curriculum sampling. (ii) HLPrompt extends HiLo with semantic-aware spatial prompt tuning to suppress background and domain noise. (iii) VLPrompt leverages vision-language models via factorized textual prompts and cross-modal consistency regularization. The three methods share core design principles while operating on different foundation backbones, making them suitable for different deployment scenarios. Extensive experiments on synthetic corruptions and real-world multi-domain shifts demonstrate consistent improvements over strong baselines. Project page: this https URL

---


### 9. [TRIP-Evaluate: An Open Multimodal Benchmark for Evaluating Large Models in Transportation](https://arxiv.org/abs/2605.00907)

**<font color=#1a73e8>作者：</font>** Han Gong, Zhen Zhou, Yunyang Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and multimodal large models (MLLMs) are increasingly used for transportation tasks such as regulation question answering, traffic management support, engineering review, and autonomous-driving scene reasoning. Yet transportation workflows are rule-intensive, computation-intensive, safety-critical, and inherently multimodal. Existing general benchmarks provide limited evidence of whether a model can apply regulations correctly, perform verifiable engineering calculations, or interpret traffic scenes reliably, while the small number of public transportation benchmarks remain narrow in scope and rarely support fine-grained diagnosis across text, images, and point-cloud data. To address this gap, we present TRIP-Evaluate, an open multimodal benchmark for large models in transportation. The benchmark organizes 837 items using a role-task-knowledge taxonomy that covers vehicle, traffic-management, traveler, and planning-and-design functions. Each item is annotated with capability, modality, and difficulty labels, enabling diagnosis from overall accuracy down to specific failure modes. The current release includes 596 text items, 198 image items, and 43 point-cloud items. TRIP-Evaluate also standardizes item construction, quality control, prompting, decoding, and scoring to improve cross-model comparability. Results on a diverse panel of models show that text-based performance is improving, but substantial weaknesses remain in multi-step engineering calculation, rule-constrained reasoning, multimodal scene understanding, and point-cloud understanding. Overall, TRIP-Evaluate provides a reproducible, diagnosable, and engineering-aligned evaluation baseline for model selection, regression testing, and safer deployment in transportation applications.

---


### 10. [Leveraging Imperfect Medical Data: A Manifold-Consistent Spatio-Temporal Network for Sensor-based Human Activity Recognition](https://arxiv.org/abs/2605.00913)

**<font color=#1a73e8>作者：</font>** Jiangtao Fan, Anish Jindal, Amir Atapour-Abarghouei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sensor-based Human Activity Recognition (HAR) has attracted increasing attention in medical and healthcare monitoring, particularly with the growth of Internet of Medical Things (IoMT). However, in real-world wearable sensing scenarios, IoMT signals are often corrupted by missing measurements, sensor failures, and environmental noise, which significantly degrade the performance of conventional deep learning models that assume clean and complete inputs. To address this challenge, we propose a Manifold-Consistent Spatio-Temporal Network (MCSTN) for robust HAR under imperfect sensing conditions. The proposed framework introduces a dual-level corruption modeling mechanism that simulates realistic sensor imperfections through both physical-level corruption and diffusion-driven continuous corruption. By enforcing representation consistency across multiple corrupted views, the model learns stable and corruption-invariant semantic representations. Furthermore, we design a dual-stream spatio-temporal architecture that explicitly decouples temporal dynamics modeling and spatial correlation learning. The temporal stream captures long-term activity dynamics, while the spatial stream models inter-sensor relationships, enabling more effective spatio-temporal representation learning. Extensive experiments on three widely used HAR benchmark datasets, PAMAP2, Opportunity, and WISDM, demonstrate that the proposed MCSTN achieves competitive performance compared with existing state-of-the-art methods, particularly under imperfect sensing conditions. These results validate the effectiveness and robustness of the proposed framework for real-world wearable IoMT sensing applications.

---


### 11. [The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate](https://arxiv.org/abs/2605.00914)

**<font color=#1a73e8>作者：</font>** Blaž Bertalanič, Carolina Fortuna  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate, where teams of LLMs iteratively exchange rationales and vote on answers, is widely deployed under the assumption that peer review filters hallucinations. Yet the failure dynamics of homogeneous debate remain poorly understood, therefore we report findings from a controlled empirical study of teams of $N{=}10$ homogeneous agents (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B) across $R{=}3$ debate rounds on two high-difficulty benchmarks (GSM-Hard and MMLU-Hard). We compare peer debate against isolated self-correction and a stochastic noise control that injects rationales from unrelated problems. We decompose debate failure into three model-dependent pathways: sycophantic conformity, where agents uncritically adopt majority answers (modal adoption up to 85.5%); contextual fragility, where peer rationales destabilize previously correct reasoning (vulnerability rate up to 70.0%); and consensus collapse, where plurality voting discards correct answers already present in the generation pool (oracle gap up to 32.3 percentage points). Ablations over communication density ($K \in \{2,4,9\}$) and sampling temperature ($T \in \{0.4, 0.7\}$) show that conformity reaches high levels at minimal peer exposure ($K{=}2$) and intensifies with greater initial diversity. Across all configurations, debate consumes 2.1-3.4$\times$ more tokens (up to 28,631 tokens per problem) than self-correction for equal or lower accuracy. Our results indicate that, within the 7-8B parameter class, homogeneous teams without structured roles do not benefit from unguided peer exchange, and that isolated self-correction consistently offers a more favorable cost-accuracy tradeoff.

---


### 12. [StyleShield: Exposing the Fragility of AIGC Detectors through Continuous Controllable Style Transfer](https://arxiv.org/abs/2605.00924)

**<font color=#1a73e8>作者：</font>** Guantian Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-generated content (AIGC) detectors are increasingly deployed in high-stakes settings such as academic integrity screening, yet their reliability rests on a fundamental paradox: as language models are trained on human-written corpora, the statistical boundary between AI and human writing will inevitably dissolve as models improve. Commercial incentives have further distorted this landscape -- detection services and "de-AIification" tools often operate within the same supply chain, replacing evaluation of content quality with judgment of content origin. We present StyleShield, the first flow matching framework for conditional text style transfer, operating directly in continuous token embedding space via a DiT backbone with zero-initialized cross-attention adapters conditioned on frozen Qwen-7B representations. At inference, we adapt the SDEdit paradigm from image synthesis to text embeddings, with a single parameter gamma providing smooth continuous control over the evasion-preservation trade-off. On a multi-domain Chinese benchmark, StyleShield achieves 94.6% evasion against the training detector and >=99% against three unseen detectors, maintaining 0.928 semantic similarity. We further introduce RateAudit, a document-level scheduling algorithm that demonstrates detection-rate verdicts can be set to arbitrary values, directly questioning the reliability of score-based evaluation.

---


### 13. [Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994)

**<font color=#1a73e8>作者：</font>** Mohammed Abu Baker, Luca Baroni, Dan Wilhelm  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Finetuning can significantly modify the behavior of large language models, including introducing harmful or unsafe behaviors. To study these risks, researchers develop model organisms: models finetuned to exhibit specific known behaviors for controlled experimentation. Identifying these behaviors remains challenging. We show that a simple perplexity-based method can surface finetuning objectives from model organisms by leveraging their tendency to overgeneralize their finetuned behaviors beyond the intended context. First, we generate diverse completions from the finetuned model using short random prefills drawn from general corpora. Second, we rank completions by decreasing perplexity gap between reference and finetuned models. The top-ranked completions often reveal the finetuning objectives, without requiring model internals or prior assumptions about the behavior. We evaluate this on a diverse set of model organisms (N=76, 0.5 to 70B parameters), including backdoored models, models finetuned to internalize false facts via synthetic document finetuning, adversarially trained models with hidden concerning behaviors, and models exhibiting emergent misalignment. For the vast majority of model organisms tested, the method surfaces completions revealing finetuning objectives within the top-ranked results, with models trained via synthetic document finetuning or to produce exact phrases being particularly susceptible. We further show that the technique can be effective even without access to the exact pre-finetuning checkpoint: trusted reference models from different families can serve as effective substitutes. As the method requires only next-token probabilities from the finetuned model, it is compatible with API-gated models that expose token logprobs.

---


### 14. [Can AI Debias the News? LLM Interventions Improve Cross-Partisan Receptivity but LLMs Overestimate Their Own Effectiveness](https://arxiv.org/abs/2605.01006)

**<font color=#1a73e8>作者：</font>** Faisal Feroz, Jonas R. Kunst  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Partisan news media erode cross-partisan trust, but large language models (LLMs) offer a potential means of debiasing such content at scale. Across two pre-registered experiments, we tested whether LLM-generated debiasing of liberal news headlines could improve conservative readers' trust-relevant judgments. Study 1 found that subtle lexical debiasing (replacing emotive words with more moderate synonyms) had no effect on any outcome. Study 2 found that a more substantive reframing intervention significantly increased conservatives' perceived trustworthiness, completeness, and willingness to engage with liberal news headlines, without producing a backfire effect among a sample of liberals. In Study 1, the intervention produced robust effects among LLM-simulated silicon participants, whereas it had no impact on human readers. In Study 2, the intervention's effects among silicon participants aligned directionally with human responses but were significantly larger in magnitude for some outcomes. Moderation analyses revealed that the model's implicit theory of who responds to debiasing diverged from the psychological profile that actually predicted human responsiveness. These findings demonstrate that LLM-based debiasing can improve cross-partisan receptivity when targeting ideological framing rather than surface-level language, but that current models lack both the quantitative accuracy and qualitative psychological fidelity to evaluate their own interventions without human oversight.

---


### 15. [CLEAR: Revealing How Noise and Ambiguity Degrade Reliability in LLMs for Medicine](https://arxiv.org/abs/2605.01011)

**<font color=#1a73e8>作者：</font>** Kevin H. Guo, Chao Yan, Avinash Baidya 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical large language model (LLM) evaluations rely on simplified, exam-style benchmarks that rarely reflect the ambiguity of real-world medical inquiries. We introduce the CLinical Evaluation of Ambiguity and Reliability (CLEAR) framework, which assesses how decision-space presentation, ambiguity, and uncertainty affect LLMs' reasoning on medical benchmarks. CLEAR systematically perturbs (1) the number of plausible answer options, (2) the presence of a ground truth or abstention option, and (3) the semantic framing of answer options. Applying CLEAR on three benchmarks evaluated across 17 LLMs reveals three notable limitations of existing evaluation methods. First, increasing the number of plausible answers degrades a model's ability to identify the correct answer and abstain against incorrect ones. Second, this lack of caution intensifies as the framing of abstention shifts from assertive rejection like "None of the Above" to uncertainty admission like "I don't know" (IDK). Notably, just including IDK in the answer space increases incorrect answer selections. Lastly, we formalize the performance gap between identifying the correct answer and abstaining from incorrect ones as the humility deficit, which worsens with model scale. Our findings reveal limitations in standard medical benchmarks and underscore that scaling alone does not resolve LLM reliability issues.

---


### 16. [Psychologically Potent, Computationally Invisible: LLMs Generate Social-Comparison Triggers They Fail to Detect](https://arxiv.org/abs/2605.01017)

**<font color=#1a73e8>作者：</font>** Hua Zhao, Jiapei Gu, Michelle Mingyue Gu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Xiaohongshu Social Comparison Reader Elicitation (XHS-SCoRE), a reader-grounded benchmark for detecting if a text-only Xiaohongshu (RedNote) post elicits UPWARD, DOWNWARD, or NEUTRAL/no clear social comparison from a first-person reader perspective. The task targets a socially meaningful relational signal that is behaviorally real yet not reducible to sentiment. Across prompted LLM classifiers and supervised Chinese encoder baselines, we find a consistent mismatch between generation fluency and reliable detection ability: the signal is textually learnable in-domain, but not robustly accessible to prompt-based classification. Prompted LLM classifiers exhibit stable, interpretable failure modes, especially neutralization of comparison-triggering posts and model-specific directional skew. A controlled pilot further shows that LLM-generated Xiaohongshu-style posts can shift perceived standing and comparison-related affect even when prompt-based detection of the same construct remains fragile. XHS-SCoRE contributes both a benchmark for reader-grounded comparison detection and a diagnostic framework for studying when socially meaningful relational cues remain only partially visible to prompt-based inference.

---


### 17. [WildTableBench: Benchmarking Multimodal Foundation Models on Table Understanding In the Wild](https://arxiv.org/abs/2605.01018)

**<font color=#1a73e8>作者：</font>** Junzhe Huang, Xiaoxiao Sun, Yan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using multimodal foundation models to analyze table images is a high-value yet challenging application in consumer and enterprise scenarios. Despite its importance, current evaluations rely largely on structured-text tables or clean rendered images, leaving the visual complexity of in-the-wild table images underexplored. Such images feature varied layouts and diverse domains that demand sophisticated structural perception and numerical reasoning. To bridge this gap, we introduce WildTableBench, the first question-answering benchmark for naturally occurring table images from real-world settings. WildTableBench comprises 402 high-information-density table images collected from online forums and websites across diverse domains, together with 928 manually annotated and verified questions spanning 17 subtypes across five categories. We evaluate 21 frontier proprietary and open-source multimodal foundation models on this benchmark. Only one model exceeds 50% accuracy, while all remaining models range from 4.1% to 49.9%. We further conduct diagnostic analyses to characterize model failures and reveal persistent weaknesses in structural perception and reasoning. These results and analyses provide useful insights into current model capabilities and establish WildTableBench as a valuable diagnostic benchmark for table image understanding.

---


### 18. [EmoMM: Benchmarking and Steering MLLM for Multimodal Emotion Recognition under Conflict and Missingness](https://arxiv.org/abs/2605.01024)

**<font color=#1a73e8>作者：</font>** Yueru Sun, Yimeng Zhang, Haoyu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Emotion Recognition (MER) is critical for interpreting real-world interactions. While Multimodal Large Language Models (MLLM) have shown promise in MER, their internal decision-making mechanisms under modality conflict and missingness remain largely underexplored. In this paper, to systematically investigate these behaviors, we introduce EmoMM, a comprehensive benchmark featuring modality-aligned, conflict, and missing subsets. Through extensive evaluation, we uncover a Video Contribution Collapse (VCC) phenomenon, where MLLM marginalize video evidence due to high token redundancy and modality preferences. To address this, we propose Conflict-aware Head-level Attention Steering (CHASE), a lightweight mechanism that detects modality conflicts and performs inference-time attention steering, effectively mitigating decision bias without retraining the backbone. Experimental results demonstrate that CHASE consistently improves performance across various settings, significantly enhancing the reliability of MLLM in complex affective scenarios.

---


### 19. [A Theoretical Game of Attacks via Compositional Skills](https://arxiv.org/abs/2605.01034)

**<font color=#1a73e8>作者：</font>** Xinbo Wu, Huan Zhang, Abhishek Umrawal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models grow increasingly capable, concerns about their safe deployment have intensified. While numerous alignment strategies aim to restrict harmful behavior, these defenses can still be circumvented through carefully designed adversarial prompts. In this work, we introduce a theoretical framework that formalizes a game between an attacker and a defender. Within this framework, we design a theoretical best-response attack strategy and show that it is closely related to many existing adversarial prompting methods. We further analyze the resulting game, characterize its equilibria, and reveal inherent advantages for the attacker. Drawing on our theoretical analysis, we also derive a provably optimal defense strategy. Empirically, we evaluate a practical instantiation of the theoretically optimal attack and observe stronger performance relative to existing adversarial prompting approaches in diverse settings encompassing different LLMs and benchmarks.

---


### 20. [Learning in the Fisher Subspace: A Guided Initialization for LoRA Fine-Tuning](https://arxiv.org/abs/2605.01046)

**<font color=#1a73e8>作者：</font>** Zhi-Quan Feng, Ying-Jia Lin, Hung-Yu Kao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA adapts large language models (LLMs) by restricting updates to low-rank subspaces of pre-trained weights. While this substantially reduces training cost, the effectiveness of adaptation critically depends on which subspace is chosen at initialization: a poor initialization that allocates capacity to task-irrelevant directions can severely hinder downstream performance. Existing initialization strategies primarily rely on the intrinsic properties of pre-trained weights, implicitly assuming that weight geometry alone reflects task relevance. However, such criteria overlook how the model interacts with the downstream data distribution. In this work, we formulate LoRA initialization as identifying the degree of impact of directions in parameter space under the target data distribution. We argue that data-aware sensitivity, rather than weight-only magnitude, should govern the choice of adaptation subspaces. Building on this perspective, we propose a Fisher-guided framework that leverages curvature information induced by downstream data to characterize how parameter perturbations influence model predictions. This perspective yields a principled, task-dependent criterion for selecting LoRA directions that better align adaptation with the target objective. Empirical results across diverse tasks and modalities demonstrate that data-aware initialization consistently and significantly improves downstream performance over existing approaches.

---


### 21. [Teaching LLMs Brazilian Healthcare: Injecting Knowledge from Official Clinical Guidelines](https://arxiv.org/abs/2605.01077)

**<font color=#1a73e8>作者：</font>** Hugo Abonizio, Filipe Rocha Lopes, Roberto Lotufo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Brazil's Unified Health System (SUS) relies on official clinical guidelines that define diagnostic criteria, treatments, dosages, and monitoring procedures for over 200 million citizens. Yet current LLMs perform poorly on this guideline-specific knowledge, and no benchmark evaluates clinical recall grounded in Brazilian Portuguese protocols. We address this gap by adapting Qwen2.5-14B-Instruct to the Brazilian clinical domain. From 178 official guidelines (~5.4M tokens), we generate ~70M tokens of synthetic data in three formats -- rephrases, wiki-style articles, and question-answer pairs -- using four generator LLMs. We then apply continual pre-training followed by Group Relative Policy Optimization (GRPO). We introduce HealthBench-BR, with 1,780 balanced true/false clinical assertions, and PCDT-QA, with 890 open-ended clinical questions scored by an LLM judge. Our best model achieves 83.9% on HealthBench-BR and 85.4% on PCDT-QA, outperforming GPT-5.2, Claude Sonnet 4.6, Gemini 3.1 Pro, and Google AI Overview's web-grounded RAG despite having only 14B parameters. Ablations show that generator diversity and reinforcement learning are critical to these gains. We release all datasets, benchmarks, and model weights to support reproducible clinical NLP research for Brazilian Portuguese. Code, data, and model weights are available at this https URL

---


### 22. [A Knowledge-Driven LLM-Based Decision-Support System for Explainable Defect Analysis and Mitigation Guidance in Laser Powder Bed Fusion](https://arxiv.org/abs/2605.01100)

**<font color=#1a73e8>作者：</font>** Basit Mahmud Shahriar, Md Habibor Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work presents a knowledge-driven decision-support system that integrates structured defect knowledge with LLM-based reasoning to provide explainable defect diagnosis and mitigation guidance in manufacturing, using LPBF as a representative, safety-critical case study. The proposed ontology-integrated LLM-based decision support system for LPBF defect analysis and mitigation guidance is built on a knowledge base containing 27 known LPBF defect types organized into hierarchical categories and causal relationships. The developed system supports fuzzy natural language queries for systematic knowledge retrieval, literature-supported explanation of defects, and guidance on defect causes and mitigation strategies derived from encoded process knowledge. Furthermore, a multimodal image-assessment module based on foundation models enables descriptor-guided interpretation of representative microscopic defect images through semantic alignment scoring. The proposed framework was evaluated through qualitative comparisons with general-purpose vision-language models, an ablation study, and an inter-rater reliability analysis. Evaluation on the literature-derived dataset showed that the fully integrated configuration outperformed the other three evaluated system configurations, achieving a macro-average F1 score of 0.808. Additionally, inter-rater reliability analysis using Cohen's kappa indicated substantial agreement between the model outputs and the literature-derived reference labels. These findings suggest that ontology-guided knowledge representation can improve the consistency, interpretability, and practical usefulness of LLM-assisted LPBF defect analysis.

---


### 23. [Virtual Speech Therapist: A Clinician-in-the-Loop AI Speech Therapy Agent for Personalized and Supervised Therapy](https://arxiv.org/abs/2605.01101)

**<font color=#1a73e8>作者：</font>** Shakeel Sheikh, Patrick Marmaroli, MD Sahidullah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops Virtual Speech Therapist (VST), an intelligent agent-based platform that streamlines stuttering assessment and delivers customized therapy planning through automated and adaptive AI-driven workflows. VST integrates state-of-the-art deep learning-based stuttering classification, and multi-agent large language model (LLM) reasoning to support evidence-based clinical decision-making. The VST begins with the acquisition and feature extraction of patient speech samples, followed by robust classification of stuttering types. Building on these outputs, VST initiates an agentic reasoning process in which specialized LLM agents autonomously generate, critique, and iteratively refine individualized therapy plans. A dedicated critic agent evaluates all generated therapy plans to ensure clinical safety, methodological soundness, and alignment with peer-reviewed evidence and established professional guidelines. The resulting output is a comprehensive, patient-specific therapy draft intended for clinician review. Incorporating clinician feedback, the system then produces a finalized therapy plan suitable for patient delivery, thereby maintaining a clinician-in-the-loop paradigm. Experimental evaluation by expert speech therapists confirms that VST consistently generates high-quality, evidence-based therapy recommendations. These findings demonstrate the system's potential to augment clinical workflows, reduce clinician burden, and improve therapeutic outcomes for individuals with speech impairments. An interactive user interface for the proposed system is available online at: this https URL , facilitating real-time stuttering assessment and personalized therapy planning.

---


### 24. [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/abs/2605.01106)

**<font color=#1a73e8>作者：</font>** Hector Borobia, Elies Seguí-Mas, Guillermina Tormo-Carbó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive inference by drafting candidate tokens with a fast model and verifying them in parallel with the target. Self-speculative methods avoid the need for an external drafter but have been studied exclusively in homogeneous Transformer architectures. We introduce component-aware self-speculative decoding, the first method to exploit the internal architectural heterogeneity of hybrid language models, isolating the SSM/linear-attention subgraph as a zero-cost internal draft. We evaluate this on two architecturally distinct hybrid families: Falcon-H1 (parallel: Mamba-2 + attention per layer) and Qwen3.5 (sequential: interleaved linear and attention layers), with a pure Transformer control (Qwen2.5). Parallel hybrids achieve acceptance rates of alpha = 0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only alpha = 0.038 -- an 18x gap attributable to how each architecture integrates its components. The property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B. We further show that perplexity degradation from a companion ablation study predicts speculative viability without running speculative decoding: a 3.15x ratio (Falcon) maps to alpha = 0.37 at k=4, while 81.96x (Qwen) maps to alpha = 0.019. For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy. The composition pattern of hybrid models -- not merely the presence of alternative components -- determines whether component-level self-speculation is viable.

---


### 25. [New Bounds for Zarankiewicz Numbers via Reinforced LLM Evolutionary Search](https://arxiv.org/abs/2605.01120)

**<font color=#1a73e8>作者：</font>** Jay Bhan, Nicole Nobili, Srinivasan Raghuraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Zarankiewicz number $\textbf{Z}(m, n, s, t)$ is the maximum number of edges in a bipartite graph $G_{m, n}$ such that there is no complete $K_{s, t}$ bipartite subgraph. We determine for the first time the exact values of three Zarankiewicz numbers: $\textbf{Z}(11, 21, 3, 3)=116$, $\textbf{Z}(11, 22, 3, 3)=121$, and $\textbf{Z}(12, 22, 3, 3)=132$. We further establish lower bounds for 41 more Zarankiewicz numbers, including several that are within one edge of the best known upper bound, and we match the established value in four more closed cases. Our results are obtained using OpenEvolve, an open-source evolutionary algorithm based on Large Language Models (LLMs) that iteratively improves algorithms for generating mathematical constructions by optimizing a reward signal which we tailored for this specific problem. These findings provide new extremal graph constructions and demonstrate the potential of LLM-guided evolutionary search to contribute to mathematical research. In addition to presenting the resulting constructions, we report the generation algorithms produced, describe the relevant implementation details, and provide our computational costs. Our costs are remarkably low, at less than \$30 for each Zarankiewicz parameter combination, showing that LLM-guided evolutionary search can be an inexpensive, reproducible, and accessible tool for discovering new combinatorial constructions.

---


### 26. [PERSA: Reinforcement Learning for Professor-Style Personalized Feedback with LLMs](https://arxiv.org/abs/2605.01123)

**<font color=#1a73e8>作者：</font>** Ravi Ranjan, Utkarsh Grover, Xiaomin Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can provide automated feedback in educational settings, but aligning an LLMs style with a specific instructors tone while maintaining diagnostic correctness remains challenging. We ask how can we update an LLM for automated feedback generation to align with a target instructors style without sacrificing core knowledge? We study how Reinforcement Learning from Human Feedback (RLHF) can adapt a transformer-based LLM to generate programming feedback that matches a professors grading voice. We introduce PERSA, an RLHF pipeline that combines supervised fine-tuning on professor demonstrations, reward modeling from pairwise preferences, and Proximal Policy Optimization (PPO), while deliberately constraining learning to style-bearing components. Motivated by analyses of transformer internals, PERSA applies parameter efficient fine-tuning. It updates only the top transformer blocks and their feed-forward projections, minimizing global parameter drift while increasing stylistic controllability. We evaluate our proposed approach on three code-feedback benchmarks (APPS, PyFiXV, and CodeReviewQA) using complementary metrics for style alignment and fidelity. Across both Llama-3 and Gemma-2 backbones, PERSA delivers the strongest professor-style transfer while retaining correctness, for example on APPS, it boosts Style Alignment Score (SAC) to 96.2% (from 34.8% for Base) with Correctness Accuracy (CA) up to 100% on Llama-3, and Gemma-2. Overall, PERSA offers a practical route to personalized educational feedback by aligning both what it says (content correctness) and, crucially, how it says it (instructor-like tone and structure).

---


### 27. [Forager: a lightweight testbed for continual learning with partial observability in RL](https://arxiv.org/abs/2605.01131)

**<font color=#1a73e8>作者：</font>** Steven Tang, Xinze Xiong, Anna Hakhverdyan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In continual reinforcement learning (CRL), good performance requires never-ending learning, acting, and exploration in a big, partially observable world. Most CRL experiments have focused on loss of plasticity -- the inability to keep learning -- in one-off experiments where some unobservable non-stationarity is added to classic fully observable MDPs. Further, these experiments rarely consider the role of partial observability and the importance of CRL agents that use memory or recurrence. One potential reason for this focus on mitigating loss of plasticity without considering partial observability is that many partially-observable CRL environments are prohibitively expensive. In this paper, we introduce Forager, a light-weight partially-observable CRL environment with a constant memory footprint. We provide a set of experiments and sample tasks demonstrating that Forager is challenging for current CRL agents and yet also allows for in-depth study of those agents. We demonstrate that agents exhibit loss of plasticity, proposed mitigations can help, but that most useful is to leverage state construction. We conclude with a variant of Forager that generates an unending stream of new tasks to learn that clearly highlights the limitations of current CRL agents.

---


### 28. [A Low-Latency Fraud Detection Layer for Detecting Adversarial Interaction Patterns in LLM-Powered Agents](https://arxiv.org/abs/2605.01143)

**<font color=#1a73e8>作者：</font>** Sheldon Yu, Yingcheng Sun, Hanqing Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-powered agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent behavior through direct prompt injection, indirect content attacks, and multi-turn escalation strategies. Existing defense strategies focus on prompt-level filtering and rule-based guardrails, which are often insufficient when risk emerges gradually across interaction sequences. In this work, we propose a complementary defense mechanism: a low-latency fraud detection layer for detecting adversarial interaction patterns in LLM-powered agents. Instead of determining whether a single prompt is malicious, our approach models risk over interaction trajectories using structured runtime features derived from prompt characteristics, session dynamics, tool usage, execution context, and fraud-inspired signals. The detection layer can be implemented using lightweight models leading to low-latency real-time deployments. To evaluate the framework, we construct a synthetic corpus of 12,000 multi-turn agent interactions generated from parameterized templates that simulate realistic agentic workflows. Using 42 structured features and an XGBoost classifier, our detector achieves over 9 times faster than LLM-based detectors. Through the experiment and ablation studies, our work suggests that interaction-level behavioral detection should become a core component of deployment-time defense for LLM-powered agents.

---


### 29. [Semantic Context-aware mOdality fUsion Transformer (SCOUT): A Context-Aware Multimodal Transformer for Concept-Grounded Pathology Report Generation](https://arxiv.org/abs/2605.01144)

**<font color=#1a73e8>作者：</font>** Suryakant Singh, Saarthak Kapse, Joel Saltz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide images (WSIs) present a fundamental challenge for computational pathology due to their extreme resolution, multi-scale heterogeneity, and the requirement for clinically reliable interpretation. Although recent pathology foundation models have enabled fluent report generation, they often lack clinical grounding, failing to accurately represent key diagnostic concepts and relationships observed by pathologists. This limitation arises from the difficulty of integrating heterogeneous visual evidence spanning fine-grained cellular patterns, slide-level tissue architecture, and high-level diagnostic concepts, while maintaining interpretability and clinical coherence. Here we present SCOUT: Semantic Context-aware mOdality fUsion Transformer, a context-aware concept-grounded multimodal framework for pathology report generation that enables progressive conditioning of image representations by global slide information and explicit diagnostic concepts. The method integrates local histological patterns, whole-slide context, and expert-curated semantic descriptors within a unified learning paradigm, allowing visual features to be dynamically refined throughout the encoding process. By combining depth-aware contextual modulation with adaptive multimodal fusion during text generation, the framework produces clinically coherent reports while preserving complementarity across representational scales. Using CONCH1.5 features, we evaluate SCOUT against WSI-Caption, HistGen, and BiGen on TCGA-BRCA, MICCAI REG, and HistAI. SCOUT achieves the best BLEU-1 to BLEU-4 and METEOR scores on all datasets, plus the best ROUGE-L on TCGA-BRCA and MICCAI REG. On TCGA-BRCA, it reaches 0.436/0.303/0.202/0.156 BLEU-1/2/3/4 and 0.204 METEOR; on REG 2025, it achieves 0.865/0.834/0.805/0.780 and 0.568. These results support progressive contextual conditioning for grounded pathology report generation.

---


### 30. [Position: Safety and Fairness in Agentic AI Depend on Interaction Topology, Not on Model Scale or Alignment](https://arxiv.org/abs/2605.01147)

**<font color=#1a73e8>作者：</font>** Tanav Singh Bajaj, Nikhil Singh, Karan Anand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed as interacting agents in high-stakes decisions, the AI safety community assumes that safety properties of individual models will compose into safe multi-agent behavior. This position paper argues that this assumption is fundamentally mistaken. In agentic AI, safety is determined by interaction topology, not model weights. When agents deliberate sequentially or aggregate via parallel voting with a judge, the structure of information flow and decision coupling dominates outcomes. Evidence across model families and scales reveals three persistent topology-driven pathologies: ordering instability, where system behavior depends primarily on agent sequence; information cascades, where early judgments propagate regardless of correctness; and functional collapse, where systems satisfy fairness metrics while abandoning meaningful risk discrimination. Contrary to intuition, scaling to more capable models strengthens these effects by increasing consensus formation and reducing the challenge of initial decisions. These failure modes are invisible to model-centric evaluation and alignment procedures. We argue that agentic AI must be treated as a dynamical system rather than a collection of aligned components. Interaction topology must become a primary target of safety evaluation and regulation, with systems required to demonstrate robustness across architectural variations before deployment.

---


### 31. [Arithmetic in the Wild: Llama uses Base-10 Addition to Reason About Cyclic Concepts](https://arxiv.org/abs/2605.01148)

**<font color=#1a73e8>作者：</font>** Sheridan Feucht, Tal Haklay, Usha Bhalla 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does structure in representations imply structure in computation? We study how Llama-3.1-8B reasons over cyclic concepts (e.g., "what month is six months after August?"). Even though Llama-3.1-8B's representations for these concepts are circularly structured, we find that instead of directly computing modular addition in the period of the cyclic concept (e.g., 12 for months), the model re-uses a generic addition mechanism across tasks that operates independently of concept-specific geometry. First, it computes the sum of its two inputs using base-10 addition (six + August=14). Then, it maps this sum back to cyclic concept space (14->February). We show that Llama-3.1-8B uses task-agnostic Fourier features to compute these sums--in fact, these features have periods that respect standard base-10 addition, e.g., 2, 5, and 10, rather than the cyclic concept period (e.g., 12 for months). Furthermore, we identify a sparse set of 28 MLP neurons re-used across all tasks (approximately 0.2% of the MLP at layer 18) that can be partitioned into disjoint clusters, each computing the sum for a Fourier feature with a different period. Our work highlights how an interplay between causal abstraction and feature geometry can deepen our mechanistic understanding of LMs.

---


### 32. [LLMs Should Not Yet Be Credited with Decision Explanation](https://arxiv.org/abs/2605.01164)

**<font color=#1a73e8>作者：</font>** Wenshuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that LLMs should not yet be credited with decision explanation. This matters because recent work increasingly treats accurate behavioral prediction, plausible rationales, and outcome-conditioned reasoning traces as evidence that LLMs explain why people decide as they do, risking a premature redefinition of what counts as explanatory progress in human decision modeling. We first distinguish three claims with different evidential burdens: decision prediction, rationale generation, and decision explanation. We then argue that the evidence most commonly offered for LLM-based decision accounts directly supports the first two claims, and sometimes explanatory hypothesis generation, but does not distinguish decision explanation from prediction-supportive rationalization. Next, we propose a bridge standard for decision-explanation credit: stronger claims should specify explanatory targets, discriminate against weaker rationalizer alternatives, use target-appropriate process- or intervention-sensitive validation, and bound their scope. We then situate this standard against competing views and related literatures, clarifying why it preserves the value of LLMs as predictors, narrators, and hypothesis generators while resisting premature explanatory credit. We conclude with a principle of credit calibration: LLMs should be credited for the strongest claim their evidence warrants, and no stronger; if adopted, this principle can help turn LLMs from persuasive narrators of decisions into more reliable instruments for discovering, testing, and communicating explanations of human behavior.

---


### 33. [Minimizing Collateral Damage in Activation Steering](https://arxiv.org/abs/2605.01167)

**<font color=#1a73e8>作者：</font>** Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause ``collateral damage", defined as unintended changes in the alignment of activations along other non-target feature directions. This damage occurs because standard methods implicitly assume the isotropy of non-target features. In this work, we provide a mathematical formalization of collateral damage and introduce a principled framework that models steering as a constrained optimization problem. Our method finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations. This weighting encodes the nonuniform cost of the perturbation in different feature directions, in contrast to isotropic approaches that penalize changes uniformly in all feature directions. By accounting for the empirical second-moment of activations, our approach achieves more precise control while reducing the degradation of model performance on unrelated tasks.

---


### 34. [SRA: Span Representation Alignment for Large Language Model Distillation](https://arxiv.org/abs/2605.01205)

**<font color=#1a73e8>作者：</font>** Quoc Phong Dao, Hoang Son Nguyen, Pham Khanh Chi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-Tokenizer Knowledge Distillation (CTKD) enables knowledge transfer between a large language model and a smaller student, even when they employ different tokenizers. While existing approaches mainly focus on token-level alignment strategies, which are often brittle and sensitive to discrepancies between tokenizers, we argue that the method of aggregating tokens into more robust representations before distillation is of equal importance. In this paper, we introduce \textbf{SRA} (\textbf{S}pan \textbf{R}epresentation \textbf{A}lignment for Large Language Model Distillation), a novel framework that reframes CTKD through the physical lens of Multi-Particle Dynamical Systems. SRA shifts the fundamental unit of alignment from tokens to robust, tokenizer-agnostic spans. We model each span as a cluster of particles and represent its state by its Center of Mass (CoM) - an attention-weighted average that captures rich semantic information. We leverage the concept of span centers of mass with attention-derived weighting to prioritize the most salient spans. In addition, we employ a geometric regularizer to preserve the structural integrity of the representation space and introduce aligned span logit distillation to enhance knowledge transfer across models. In challenging cross-architecture distillation experiments, SRA consistently and significantly outperforms state-of-the-art CTKD baselines, validating our physically-grounded approach.

---


### 35. [Agentic AI Systems Should Be Designed as Marginal Token Allocators](https://arxiv.org/abs/2605.01214)

**<font color=#1a73e8>作者：</font>** Siqi Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that agentic AI systems should be designed and evaluated as \emph{marginal token allocation economies} rather than as text generators priced by the unit. We follow a single request -- a developer asking a coding agent to fix a failing test -- through four economic layers that today are designed in isolation: a router that decides which model answers, an agent that decides whether to plan, act, verify, or defer, a serving stack that decides how to produce each token, and a training pipeline that decides whether the trace is worth learning from. We show that all four layers are solving the \emph{same} first-order condition -- marginal benefit equals marginal cost plus latency cost plus risk cost -- with different index sets and different prices. The framing is deliberately minimal: we do not propose a complete theory of AI economics. But adopting marginal token allocation as the shared accounting object explains why systems that locally minimize tokens globally misallocate them, predicts a small set of recurring failure modes (over-routing, over-delegation, under-verification, serving congestion, stale rollouts, cache misuse), and points to a concrete research agenda in token-aware evaluation, autonomy pricing, congestion-priced serving, and risk-adjusted RL budgeting.

---


### 36. [Lost in the Tower of Babel: The Adverse Effects of Incidental Multilingualism in LLMs](https://arxiv.org/abs/2605.01224)

**<font color=#1a73e8>作者：</font>** Anjishnu Mukherjee, Chutong Meng, Antonios Anastasopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper argues that contemporary multilingual NLP has converged on a fragile and misleading paradigm of incidental multilingualism. Today's LLMs appear multilingual largely because they are trained on massive, uneven web corpora, not because multilingual or multicultural competence has been treated as a core design objective. We contend that this paradigm systematically produces unequal, brittle, and opaque behavior across languages, with severe consequences in real-world and agentic deployments where models must reason, plan, and act across multiple linguistic contexts. We report a focused empirical study of two practical questions: which languages models self-report as supported and which languages they actually respond in across multilingual prompts. We additionally demonstrate how even a simple language-change attack can surface these failures and expose hidden assumptions about language in LLM-based systems. To address this, we call for a shift toward multilingualism by design: a research agenda that treats equitable multilingual performance, cultural grounding, and cross-lingual behavioral understanding as first-class goals in all aspects of the model pipeline.

---


### 37. [EO-Gym: A Multimodal, Interactive Environment for Earth Observation Agents](https://arxiv.org/abs/2605.01250)

**<font color=#1a73e8>作者：</font>** Sai Ma, Zhuang Li, Sichao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) analysis is inherently interactive: resolving uncertainty often requires expanding the region of interest, retrieving historical observations, and switching across sensors such as optical and Synthetic Aperture Radar. However, most EO benchmarks collapse this process into fixed-input, single-turn tasks. To address this gap, we present EO-Gym, a controlled executable framework for multimodal, tool-using EO agents that formulates EO analysis as a Gymnasium-style local geospatial workspace backed by more than 660k multimodal files indexed by location, time, and sensor type, with 35 EO-specialized tools spanning six task families. Built on this environment, we construct EO-Gym-Data, a benchmark of 9,078 trajectories and 34,604 reasoning steps, and grounded in eight public EO datasets together with Landsat and Sentinel-2 imagery. Evaluating $10$ open and closed VLMs shows that strong general-purpose models still struggle with interactive EO reasoning, especially on temporal and cross-modal workflows. As a reference baseline, EO-Gym-4B, obtained by fine-tuning Qwen3-VL-4B-Instruct on EO-Gym-Data, improves overall Pass@3 from $0.49$ to $0.74$ under the main evaluation setting. O-Gym provides a reproducible environment for interactive EO agents, operationalizing EO as an evidence-gathering problem that requires planning across geospatial, temporal, and sensing modality.

---


### 38. [Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm](https://arxiv.org/abs/2605.01255)

**<font color=#1a73e8>作者：</font>** Wen-Da Wei, Han-Bin Fang, Yang-Di Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) is highly memory-intensive, as training must store not only weights and optimizer states but also intermediate activations for backpropagation. While existing memory-efficient methods largely focus on gradients and optimizer states, activation compression is less well established due to the lack of LLM-tailored theory and guarantees. In this work, we develop a theoretical framework showing that activation compression is safe for linear operators when activation compression is unbiased, but problematic for nonlinear ones. We further derive gradient variance bound and establish convergence guarantees for applying activation compression to all linear operators under the standard $L$-smoothness assumption, showing that it does not change the convergence rate. Guided by the theory, we propose an activation-gradient co-compression method that reuses low-rank activation factors to compress linear-layer gradients without extra computation or additional gradient error. We conduct extensive experiments on Qwen and LLaMA models using a pretraining benchmark and multiple fine-tuning benchmarks to validate our theory and demonstrate competitive performance of our method in both accuracy and compression efficiency. We provide our code in the supplementary material for reproducibility.

---


### 39. [GIFT: Guided Fine-Tuning and Transfer for Enhancing Instruction-Tuned Language Models](https://arxiv.org/abs/2605.01256)

**<font color=#1a73e8>作者：</font>** Zhiwen Ruan, Yichao Du, Jianjie Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A promising paradigm for adapting instruction-tuned language models is to learn task-specific updates on a pretrained base model and subsequently merge them into the instruction-tuned model. However, existing approaches typically treat the instruction-tuned model as a passive target that is only involved at the final merging stage, without guiding the training process. We propose GIFT (Guided Fine-Tuning and Transfer), a simple and efficient framework that incorporates guidance from the instruction model into task adaptation. GIFT fine-tunes a low-rank adapter on the pretrained base model using confidence signals derived from the instruction-tuned model. The learned adapter is then merged into the instruction-tuned model, yielding task-specialized models that preserve general instruction-following behavior. We evaluate GIFT on mathematical and knowledge-intensive benchmarks across multiple model families and scales. Results show that GIFT consistently outperforms direct fine-tuning and representative transfer-based baselines, while maintaining robust generalization and favorable test-time scaling behavior.

---


### 40. [Exploring Prompt Alignment with Clinical Factors in Zero-Shot Segmentation VLMs for NSCLC Tumor Segmentation](https://arxiv.org/abs/2605.01266)

**<font color=#1a73e8>作者：</font>** Suraj Pai, Thibault Heintz, Cosmin Ciausu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot vision-language models (VLMs) offer a promptable alternative to task-specific training for gross tumor volume (GTV) delineation in non-small-cell lung cancer (NSCLC), but the prompt dimensions that govern their spatial behavior remain poorly understood. We study this question by probing alignment directions in VoxTell on a held-out internal NSCLC tumor dataset through sub-prompt decomposition into diagnosis, demographic, staging, anatomical, generic, and irrelevant controls; attribute-wise perturbation robustness; specificity ladders; and cross-case prompt swaps, while benchmarking against fine-tuned and zero-shot baselines using the Dice Similarity Coefficient (DSC) with Wilcoxon signed-rank tests and Benjamini-Hochberg correction. Alignment analyses revealed that anatomical location is the dominant driver of VoxTell's spatial attention: 63.4 percent of location perturbations caused catastrophic drops, prompt specificity improved from generic to full descriptions except for diagnosis-only prompts, irrelevant prompts correctly yielded zero segmentation, and cross-case prompt swaps confirmed patient-specific conditioning (matched DSC 0.906 vs. mismatched 0.406). Histology and stage substitutions had minimal effect, indicating that the model prioritizes "where to look" over "what to look for." In this context, VoxTell, operating fully zero-shot, achieved a mean DSC of 0.613, statistically indistinguishable from nnUNet (0.690, adjusted p = 0.156) and Ahmed et al. (0.675, adjusted p = 0.679), while significantly outperforming all other zero-shot models. Together, these findings argue that segmentation VLMs should be evaluated not only by Dice, but also by the prompt dimensions to which they align.

---


### 41. [Valley3: Scaling Omni Foundation Models for E-commerce](https://arxiv.org/abs/2605.01278)

**<font color=#1a73e8>作者：</font>** Zeyu Chen, Guanghao Zhou, Qixiang Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we present Valley3, an omni multimodal large language model (MLLM) developed for diverse global e-commerce tasks, with unified understanding and reasoning capabilities across text, images, video, and audio. A key feature of Valley3 is its native multilingual audio capability for e-commerce, developed by extending vision-language models to better support crucial audio-visual tasks, particularly in short-video scenarios. To achieve this, we carefully design a four-stage omni e-commerce continued pre-training pipeline, through which Valley3 progressively acquires audio understanding, cross-modal instruction-following, e-commerce domain knowledge, and long-context reasoning capabilities, ultimately evolving into an omni model for diverse e-commerce scenarios. Then, we further improve Valley3 through post-training to encourage long-chain reasoning with controllable reasoning modes, enabling one non-thinking mode and three distinct levels of thinking, thereby balancing inference efficiency in simple scenarios with deep reasoning for complex applications. Moreover, we equip Valley3 with agentic search capabilities to proactively invoke search tools and acquire task-relevant information for e-commerce deep research tasks. To comprehensively assess the capabilities of Valley3, we construct an omni e-commerce benchmark spanning 6 tasks. Experimental results show that Valley3 consistently outperforms strong baselines on our in-house and open-source e-commerce benchmarks, while remaining competitive on general-domain benchmarks.

---


### 42. [Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation](https://arxiv.org/abs/2605.01284)

**<font color=#1a73e8>作者：</font>** Peiyang Liu, Ziqiang Cui, Xi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative Retrieval-Augmented Generation (iRAG) has emerged as a powerful paradigm for answering complex multi-hop questions by progressively retrieving and reasoning over external documents. However, current systems predominantly operate on parsed text, which creates two critical bottlenecks: (1) \textit{Coarse-grained attribution}, where users are burdened with manually locating evidence within lengthy documents based on vague text-level citations; and (2) \textit{Visual semantic loss}, where the conversion of visually rich documents (e.g., slides, PDFs with charts) into text discards spatial logic and layout cues essential for reasoning. To bridge this gap, we present \textbf{Chain of Evidence (CoE)}, a retriever-agnostic visual attribution framework that leverages Vision-Language Models to reason directly over screenshots of retrieved document candidates. CoE eliminates format-specific parsing and outputs precise bounding boxes, visualizing the complete reasoning chain within the retrieved candidate set. We evaluate CoE on two distinct benchmarks: \textbf{Wiki-CoE}, a large-scale dataset of structured web pages derived from 2WikiMultiHopQA, and \textbf{SlideVQA}, a challenging dataset of presentation slides featuring complex diagrams and free-form layouts. Experiments demonstrate that fine-tuned Qwen3-VL-8B-Instruct achieves robust performance, significantly outperforming text-based baselines in scenarios requiring visual layout understanding, while establishing a retriever-agnostic solution for pixel-level interpretable iRAG. Our code is available at this https URL.

---


### 43. [Addressing Data Scarcity in Bangla Fake News Detection: An LLM-Based Dataset Augmentation Approach](https://arxiv.org/abs/2605.01292)

**<font color=#1a73e8>作者：</font>** Ahmed Alfey Sani, Kazi Akib Zaoad, Shefayat E Shams Adib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing spread of misinformation in digital media highlights the need for reliable fake news detection systems, yet progress in under-resourced languages such as Bangla is limited by small and imbalanced datasets. This study investigates whether Large Language Model (LLM) based augmentation can effectively address this limitation and improve Bangla fake news classification. Existing datasets remain valuable but highly imbalanced, limiting model performance, and LLM based augmentation for Bangla has been scarcely explored. To fill this gap, we propose a systematic augmentation framework that generates synthetic Bangla news articles using the instruction tuned Gemma 3 27B IT model, supported by semantic filtering and controlled subsampling to preserve label consistency and diversity. We compare zero shot and few shot prompting, evaluate multiple augmentation rates, and examine random versus similarity-based selection strategies. Our experiments show that augmenting only the minority class with a high augmentation rate and random subsampling yields the strongest gains, raising the Fake News F1 score from 0.85 to 0.88. To support reproducibility and further research in this low-resource domain, we publicly release 4,545 synthetically generated Bangla fake news samples along with our full implementation. These findings demonstrate that well-designed LLM-driven augmentation can significantly improve fake news detection in low resource settings and provide a practical foundation for advancing multilingual misinformation research.

---


### 44. [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2605.01293)

**<font color=#1a73e8>作者：</font>** Jie-Jing Shao, Haiyan Yin, Yueming Lyu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation model-driven agents often struggle with long-horizon planning due to the transient nature of purely prompting-based reasoning. While existing skill induction methods mitigate this by distilling experience into state-blind parameterized scripts, they fail to capture the conditional logic required for robust execution in dynamic environments. In this paper, we propose Neuro-Symbolic Skill Induction (NSI), a framework that lifts interaction traces into modular, \textit{logic-grounded} programs. By synthesizing explicit control flows and dynamic variable binding, NSI empowers agents to discover \textit{when} and \textit{why} to act. This paradigm enables the efficient generalization, allowing agents to induce skills from few-shot examples and flexibly adapt to unseen goals. Experiments on a series of agentic tasks demonstrate that NSI consistently outperforms state-of-the-art baselines, empowering agents to self-evolve into architects of logic-grounded skills.

---


### 45. [GA-VisAgent: A Multi-Agent application for code generation and visualization in interactive learning](https://arxiv.org/abs/2605.01299)

**<font color=#1a73e8>作者：</font>** Wang Jian, Zhou Jianbo, Xiong Yuhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometric Algebra (GA) presents challenges to learners due to its highly abstract mathematical structure and complex operational rules, as translating algebraic manipulations into concrete geometric interpretations is a non-intuitive process when developing related code. Currently, some existing GA software packages rely on manually written scripts for code generation and visualization, but their high learning curve hinders widespread adoption. Meanwhile, methods based on Large Language Models (LLMs) often produce logical errors when generating specific GA scripts, such as GAALOPScript, resulting in generally low accuracy. To address these issues, this study proposes GA-VisAgent -- a multi-agent interactive learning application for GA code generation and visualization -- building upon a Geometric algebra large language model (GAGPT). Integrating task planning mechanisms with ReAct reasoning strategies, GA-VisAgent can decompose complex operations into five standardized subtasks, including core operations like geometric products, rotations, and reflections. It supports natural language and mathematical formulas as input to automatically generate executable code, accompanied by interactive visualizations to aid user comprehension. Experimental results show that GA-VisAgent achieved a 90% code generation success rate across 40 typical Conformal GA tasks, representing a 70% improvement over GPT-4o. This application introduces an extensible new paradigm for teaching GA and developing visualization tools for related mathematical concepts. The online service for this project will be available at this http URL.

---


### 46. [Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2605.01302)

**<font color=#1a73e8>作者：</font>** Peiyang Liu, Qiang Yan, Ziqiang Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard Retrieval-Augmented Generation (RAG) systems predominantly rely on semantic relevance as a proxy for utility. However, this assumption collapses in realistic decision-making scenarios where user queries are laden with cognitive biases, such as false premises or confirmation bias. In such cases, maximizing relevance paradoxically promotes the retrieval of sycophantic evidence that reinforces hallucinations, a critical failure we term the ``Relevance-Robustness Gap''. To bridge this gap, we propose CoRM-RAG (Counterfactual Risk Minimization for RAG), a framework that aligns retrieval with decision safety rather than mere similarity. Grounded in causal intervention, we introduce a Cognitive Perturbation Protocol to simulate user biases during training, which is then distilled into a lightweight Evidence Critic. This scoring module learns to identify documents that possess sufficient evidential strength to steer the model toward correctness despite adversarial query perturbations. Extensive experiments on decision-making benchmarks demonstrate that CoRM-RAG significantly outperforms strong dense retrievers and LLM-based rerankers in adversarial settings, while enabling effective risk-aware abstention through reliable robustness scoring. Our code is available at this https URL.

---


### 47. [GraphSculptor: Sculpting Pre-training Coreset for Graph Self-supervised Learning](https://arxiv.org/abs/2605.01310)

**<font color=#1a73e8>作者：</font>** Chuang Liu, Zelin Yao, Xueqi Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph self-supervised learning typically relies on large-scale unlabeled datasets, heavily inflating computational costs. However, empirical evidence suggests that these datasets contain substantial redundancy-our analysis reveals that uniformly subsampling 50% of graphs retains over 96% of downstream performance. To exploit this redundancy, we introduce GraphSculptor for pre-training coreset construction. Unlike methods dependent on additional training-time signals or limited solely to topological statistics, GraphSculptor provides a label-free solution that constructs coresets via two complementary perspectives: intrinsic structure and contextual semantics. Concretely, structural diversity is quantified using intrinsic graph statistics, yielding a structural feature vector for each graph, while semantic diversity is captured by utilizing a pre-trained language model to encode descriptions generated via graph-to-text. GraphSculptor integrates these signals into a unified metric space and performs cluster-aware selection to preserve joint structural-semantic diversity. We further derive a theoretical bound on the loss gap between coreset and full-data pre-training, offering theoretical motivation for our selection formulation. Extensive experiments demonstrate that GraphSculptor effectively sculpts the dataset: a 10% coreset achieves 99.6% of full-data performance while reducing pre-training time by nearly 90%, offering a scalable solution for data-efficient graph pre-training.

---


### 48. [The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice](https://arxiv.org/abs/2605.01311)

**<font color=#1a73e8>作者：</font>** Jikai Jin, Vasilis Syrgkanis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline evaluation of language models from usage logs is biased when model choice is confounded: the same user-side factors that influence which model is used can also influence how its output is judged, so raw comparisons of logged scores mix self-selected populations rather than estimating a common quantity of interest. A small randomized experiment can break this bias by overriding model choice, but in practice such experiments are scarce and costly. We study a three-source design that combines a large confounded observational log (OBS) for scale, a small randomized experiment (EXP) for unconfounded scoring, and an offline simulator (SIM) that replays candidate models on cached contexts. Our main result is an identification theorem showing that the randomized experiment and the simulator are together enough to recover causal model values; the observational log enters only afterward, to reduce estimation error rather than to make the causal comparison valid. Six estimator families are evaluated in a controlled semi-synthetic validation and in two real-task cached benchmarks for summarization and coding. No family dominates every regime; relative performance depends on the amount of unbiased EXP supervision and on how closely the target reward aligns with OBS-derived structure.

---


### 49. [Beyond Perceptual Shortcuts: Causal-Inspired Debiasing Optimization for Generalizable Video Reasoning in Lightweight MLLMs](https://arxiv.org/abs/2605.01324)

**<font color=#1a73e8>作者：</font>** Jingze Wu, Quan Zhang, Hongfei Suo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although reinforcement learning (RL) has significantly advanced reasoning capabilities in large multimodal language models (MLLMs), its efficacy remains limited for lightweight models essential for edge this http URL address this issue, we leverage causal analysis and experiment to reveal the underlying phenomenon of perceptual bias, demonstrating that RL-based fine-tuning compels lightweight models to preferentially adopt perceptual shortcuts induced by data biases, rather than developing genuine reasoning this http URL by this insight, we propose VideoThinker, a causal-inspired framework that cultivates robust reasoning in lightweight models through a two-stage debiasing process. First, the Bias Aware Training stage forges a dedicated "bias model" to embody these shortcut behaviors. Then, the Causal Debiasing Policy Optimization (CDPO) algorithm fine-tunes the primary model, employing an innovative repulsive objective to actively push it away from the bias model's flawed logic while simultaneously pulling it toward correct, generalizable this http URL model, VideoThinker-R1, establishes a new state-of-the-art in video reasoning efficiency. For same-scale comparison, requiring no Supervised Fine-Tuning (SFT) and using only 1 of the training data for RL, it surpasses VideoRFT-3B with a 3.2% average gain on widely-used benchmarks and a 7% lead on VideoMME. For cross-scale comparison, it outperforms the larger Video-UTR-7B model on multiple benchmarks, including a 2.1% gain on MVBench and a 3.8% gain on TempCompass. Code is available at this https URL.

---


### 50. [Rethinking Model Selection in VLM Through the Lens of Gromov-Wasserstein Distance](https://arxiv.org/abs/2605.01325)

**<font color=#1a73e8>作者：</font>** Muyang Li, Yucheng Liu, Jianbo Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have enhanced traditional LLMs with visual capabilities through the integration of vision encoders. While recent works have explored various combinations of vision encoders and LLMs, there still lacks a principled understanding of what makes a vision encoder suitable for VLM alignment. In this paper, we systematically investigate this question via comprehensive experiments on a curated collection of 19 pre-trained vision encoders from diverse sources. We first demonstrate that common practices, such as choosing encoders with the largest size or highest zero-shot accuracy, consistently fail to identify optimal models. In fact, these metrics show only weak to moderate correlation with VLM performance. This intriguing finding begs a fundamental question: What factors of vision-encoders matter in VLM? Through comprehensive analysis, we identify that the structural similarity across modalities plays a crucial but previously overlooked role in vision-encoder selection, which we measure using the Gromov-Wasserstein distance as a proxy. From a theoretical perspective, we show that the learnability of cross-modality mapping can be provably associated with the Gromov-Wasserstein distance. Empirical verification on 60+ full VLM training runs shows that our proposed inference-only metric performs significantly better than alternative model selection strategies and exhibits a much stronger correlation with final VLM performance, thereby enabling efficient and effective prediction of VLM performance before full training.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
