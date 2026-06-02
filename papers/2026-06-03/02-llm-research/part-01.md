# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 1. [Emergent Collaborative Deliberation in Multi-Model AI Systems: A BFT-Derived Protocol for Epistemic Synthesis](https://arxiv.org/abs/2606.00005)

**<font color=#1a73e8>作者：</font>** VD Doske  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the Consilium Protocol, a Byzantine Fault Tolerance-derived architecture for structured multi-model AI deliberation that treats inter-model disagreement as epistemic signal rather than error. The protocol assigns engineered cognitive personas to language models -- separating what a model is from how it reasons -- and introduces an In-Sample/Out-of-Sample validation framework adapted from quantitative finance to distinguish training-data consensus from empirically grounded conclusions. Across 1,478 deliberation sessions spanning 32 topics in 10 domain categories, we demonstrate that (1) the cognitive persona, not the underlying model, determines epistemic behavior: free edge-inference models costing 0.0002 USD per batch produced comparable analytical output to frontier models costing 10.69 USD; (2) RLHF alignment training creates measurable, domain-specific epistemic blind spots -- contested policy topics exhibit 12.3 percentage points less adversarial challenge than settled science topics, and AI safety topics show asymmetric bias ($\Delta$=11.6%) where models challenge claims that AI is dangerous far more vigorously than claims that AI risk is overstated; (3) the protocol exhibits no directional bias of its own (immigration $\Delta$=2.3%, renewables $\Delta$=1.2%); and (4) out-of-sample evidence retrieval validated 239 claims with 100% evidence retrieval and surfaced 167 blind-spot discoveries invisible to training-data deliberation. Run-to-run reproducibility across randomized model$\times$persona assignments averages $\pm$2.2% standard deviation. Total cost for the complete battery including all overhead: 217 USD. We release the protocol specification under MIT license to enable independent verification.

---


### 2. [Empathic and agentic artificial intelligence in nursing: perspectives on a human-centered framework for cancer care navigation in the United States](https://arxiv.org/abs/2606.00010)

**<font color=#1a73e8>作者：</font>** Tyra Girdwood, Saba Kheirinejad, Parnian Kheirkhah Rahimabad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For patients experiencing cancer, nurse navigation can ease the burden of complex care by enhancing coordination of health services and patient outcomes. However, in under-resourced areas, trained nurse navigators may be limited or non-existent. In the United States, artificial intelligence (AI)-enabled digital health tools are increasingly available and may help address gaps in care coordination; however, most are not designed to specifically support nursing. This perspective piece discusses a human-centered AI framework that integrates empathic and agentic approaches grounded in the American Nurses Association's code of ethics to support nurses in the United States in cancer care navigation. The framework could augment, not replace, human empathy and agency while improving nurse workflow, patient-clinician relationships, and care coordination services in under-resourced areas.

---


### 3. [DraDDP: A Multimodal Multi-Party Dialogue Discourse Parsing Dataset](https://arxiv.org/abs/2606.00012)

**<font color=#1a73e8>作者：</font>** Shannan Liu, Peifeng Li, Yaxin Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-party dialogue discourse parsing aims to identify dependency structures and relation types between utterances in conversations. Previous studies are mostly limited to textual modality or two-party dialogue, failing to meet the multimodal and multi-party settings. In this paper, we construct the first publicly available English multimodal dataset DraDDP for multi-party dialogue discourse parsing, based on American TV dramas. DraDDP contains 495 dialogue segments with 6,374 utterances and 9.1 hours of parallel video content, covering rich multi-party interaction scenarios. Moreover, we establish comprehensive benchmarks by evaluating this task on DraDDP and conducting in-depth analysis on the impact of different modalities. Experimental results demonstrate the value of multimodal information in capturing dialogue structures and relation types. We will publicly release the dataset, annotation guidelines, and code to promote future research in multimodal dialogue understanding.

---


### 4. [Toward Robust In-Context Learning: Leveraging Out-of-distribution Proxies for Target Inaccessible Demonstration Retrieval](https://arxiv.org/abs/2606.00014)

**<font color=#1a73e8>作者：</font>** Hao Xu, Rite Bo, Fausto Giunchiglia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although studies have demonstrated that Large Language Models (LLMs) can perform well on Out-of-Distribution (OOD) tasks, their advantage tends to diminish as the distribution shift becomes more severe. Consequently, researchers aim to retrieve distributionally similar and informative demonstrations from the available source domain to boost the inference capabilities of LLMs. However, in practical scenarios where the target domain is inaccessible, evaluating the unknown distribution is challenging, which indirectly impacts the quality of the selected demonstrations. To address this problem, we propose \textbf{DOPA}, a demonstration search framework that incorporates an OOD proxy to approximate the inaccessible target domain and guide the retrieval process. Building on proxy-based evaluation, DOPA further introduces a Mahalanobis distance-based global diversity constraint to ensure sufficient diversity among the retrieved demonstrations. Experimental results on multiple LLMs and tasks demonstrate that DOPA effectively enhances robustness in OOD settings\footnote{this https URL\_code}.

---


### 5. [SortingHat: Redefining Operating Systems Education with a Tailored Digital Teaching Assistant](https://arxiv.org/abs/2606.00015)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Xinkui Zhao, Zuxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Operating Systems (OS) courses are among the most challenging in computer science education due to the complexity of internal structures and the diversity of running environments. Traditional teaching methods often fail to address the diverse backgrounds, learning speeds, and practical needs of students. To tackle these challenges, we present SortingHat, a personalized digital teaching assistant tailored specifically for OS education. SortingHat integrates advanced AI technologies, including a retrieval augmented generation (RAG) framework and multi agent reinforcement learning (MARL), to deliver adaptive, scalable, and effective educational support. SortingHat features a 3D digital human interface powered by large language models (LLMs) to provide personalized, empathetic, and context aware guidance. It generates tailored exercises based on each student's learning history and academic performance, reinforcing weak areas and challenging advanced concepts. Additionally, the system incorporates a robust evaluation pipeline that ensures fair, consistent, and unbiased grading of student submissions while delivering personalized, actionable feedback for improvement. By combining personalized guidance, adaptive content creation, and automated assessment, SortingHat transforms OS education into an engaging, immersive, and scalable experience.

---


### 6. [CSRP: Chain-of-Thought Reasoning for Chinese Text Correction via Reinforcement Learning with Efficiency-Aware Rewards](https://arxiv.org/abs/2606.00020)

**<font color=#1a73e8>作者：</font>** Wei Tian, Yuhao Zhou, Man Lan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) based Chinese Grammatical Error Correction (CGEC) systems face two critical challenges: general-purpose models lack specialized linguistic priors for subtle grammatical distinctions, and Supervised Fine-Tuning (SFT) with Maximum Likelihood Estimation fails to optimize for precision-focused metrics, leading to systematic over-correction. We propose CSRP, a three-stage framework that progressively builds correction capability through Continual Pre-training (CPT) on 5.9M balanced samples to internalize domain knowledge, Chain-of-Thought SFT with explicit error reasoning for diagnostic transparency, and Group Relative Policy Optimization with a novel Efficiency-Aware Reward that explicitly penalizes unnecessary edits. On the NACGEC benchmark, CSRP achieves state-of-the-art performance with 50.99 $F_{0.5}$ and 57.17 precision, substantially outperforming previous best results while effectively mitigating the over-correction bias inherent in MLE-trained models. Our method also advances CSCD spelling correction to 59.61 F1, surpassing GPT-4 by 5.20 points. Comprehensive ablation studies demonstrate that the RL alignment stage contributes a 8\% relative gain over the SFT baseline, and that this gain is orthogonal to the contribution of large-scale CPT, validating that explicit optimization for edit efficiency is essential for high-quality grammatical error correction. Our code is available at this https URL.

---


### 7. [SENSE: Semantic Embedding Navigation with Soft-gated Evaluation for Retrieval-based Speculative Decoding](https://arxiv.org/abs/2606.00021)

**<font color=#1a73e8>作者：</font>** Shaowen Chen, Zhicheng Liao, Hongwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative Decoding (SD) accelerates Large Language Model (LLM) inference by employing a lightweight draft model to propose candidate tokens, which are verified in parallel by the target model, without compromising generation quality. While Retrieval-based Speculative Decoding (RSD) is favored for its plug-and-play versatility, its potential is impeded by rigid lexical dependencies, rendering both retrieval and verification brittle to surface-level variations. To address this, we propose SENSE (Semantic Embedding Navigation with Soft-gated Evaluation). By anchoring retrieval on the hidden states of the target model, SENSE establishes robust semantic alignment, which empowers the Soft-gated Evaluation module to validate semantic equivalence rather than surface forms. To ensure rigorous benchmarking, we deconstruct existing methods into atomic primitives within a unified framework, facilitating granular, component-level comparison. Extensive experiments across diverse domains demonstrate that SENSE outperforms multiple baselines on the LLaMA and Qwen families, attaining up to 4.09 mean acceptance length and 3.26x speedup, while preserving generation quality. Our code will be released upon publication.

---


### 8. [ART: Attention Run-time Termination for Efficient Large Language Model Decoding](https://arxiv.org/abs/2606.00024)

**<font color=#1a73e8>作者：</font>** Chen Qiu, Guozhong Li, Panos Kalnis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context decoding in Large Language Models (LLMs) is severely constrained by the memory bandwidth required to fetch the extensive Key-Value (KV) cache. Most existing KV management methods rely on key-only pruning before decoding, despite the evidence that attention outputs depend jointly on keys and values, as incorporating values in their methods incurs prohibitive additional overhead. In this paper, we propose Attention Run-time Termination (ART), a lightweight run-time mechanism that tracks accumulated attention outputs during kernel execution and terminates subsequent KV block accesses once further contributions become negligible. This design makes ART orthogonal to existing key-based KV cache management methods, enabling seamless integration with them. Experiments on LongBench benchmarks show that ART achieves 20% higher generation throughput in large batch size than state-of-the-art baseline while maintaining comparable accuracy.

---


### 9. [A Multi-Domain Red Teaming Framework for Safety, Robustness, and Fairness Evaluation of Medical Large Language Models](https://arxiv.org/abs/2606.00027)

**<font color=#1a73e8>作者：</font>** Andrei Marian Feier, Veysel Kocaman, Yigit Gul 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed across healthcare, yet existing benchmarks fail to capture model behavior under adversarial or ethically complex conditions common in clinical practice. We developed a multi-domain red teaming framework evaluating eleven contemporary LLMs across 690 clinically grounded scenarios spanning nine domains and over 150 subcategories. Scenarios incorporated adversarial transformations, and responses were assessed using a seven-dimension rubric with LLM-assisted scoring and human-in-the-loop validation. Results revealed substantial performance variance, with mean scores ranging from 0.791 to 0.984. Critically, several high-performing systems produced complete failures in individual safety-critical scenarios, demonstrating that aggregate accuracy masks clinically meaningful risk. The highest-performing systems (X-BAI, GPT-5, Claude Opus 4.1) achieved scores above 0.97 with low variance, while performance varied significantly across domains. Equity-related tasks showed 10-20% error amplification with demographic modifications, and human reviewers identified clinically relevant failures missed by automated evaluation. Our findings demonstrate that performance variance and worst-case failures provide more clinically meaningful reliability indicators than mean accuracy alone, and that hybrid evaluation approaches combining automation with clinician oversight are essential for credible safety assessment.

---


### 10. [TCAR-Gen: Temporal Graph Retrieval with Evidence Fusion for Knowledge-Grounded Generation](https://arxiv.org/abs/2606.00029)

**<font color=#1a73e8>作者：</font>** Sidra Nasir, Muhammad Noman Zahid, Rizwan Ahmed Khan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation systems struggle with temporal reasoning and evidence fusion when answering complex questions over historical criminal case narratives. Existing approaches either retrieve independently of query semantics or fail to integrate multiple evidence sources coherently. We propose Temporal Context Augmented Retrieval Generation (TCAR-Gen), a framework that combines query-conditioned graph neural networks, temporal evidence fusion, and chain-of-trees reasoning to ground answer generation in retrieved evidence. On the Victorian Crime Diaries benchmark, TCAR-Gen achieves 0.3738 Recall@5, outperforming Vanilla RAG, Temporal RAG, GraphRAG-C, and GraphRAG-T across seven query types including multi-hop reasoning and counterfactual questions. Ablation studies reveal that the context graph, temporal penalty mechanism, and query conditioning are critical components. Cross-model evaluation across five language model (GPT-OSS 20B to TinyLlama 1.1B) demonstrates that TCAR-Gen maintains robust retrieval coverage at smaller model scales, though generation quality degrades substantially with reduced model capacity. Our work shows that explicit temporal modelling and multi-branch evidence fusion are essential for faithful, reasoning-intensive question answering over knowledge-grounded corpora.

---


### 11. [LLMs for Cardiovascular Risk Prediction from Structured Clinical Data](https://arxiv.org/abs/2606.00031)

**<font color=#1a73e8>作者：</font>** Jeba Maliha, Md Rafiul Kabir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coronary artery disease (CAD) remains one of the leading causes of death globally, highlighting the need for reliable predictive systems to support early diagnosis and risk assessment. While traditional machine learning models perform well on structured clinical data, large language models (LLMs) present new possibilities to interpret medical information expressed in natural language. In this work, we develop a hybrid framework that bridges structured clinical data and natural-language representations for CAD prediction. Using a publicly available dataset of 1,190 patient records with 11 clinical attributes, structured variables are converted into interpretable feature representations and synthetic clinical narratives using LLMs. A validation pipeline performs reverse extraction of clinical variables and computes a consistency score with the original records, achieving an average fidelity of 94.61%. We then evaluate four conventional machine learning models and compare their performance with LLM-based classification under zero-shot and few-shot prompting settings. We use two LLMs here, GPT and Gemini. Experimental results show that Random Forest achieves the highest accuracy. Despite this advantage, LLM-based classification remains beneficial in real-world clinical settings. This is because LLMs operate directly on natural language patient descriptions, meaning that sensitive numerical patient data such as exact lab values, blood pressure readings, and diagnostic codes are kept private. Findings suggest that combining structured clinical data with LLM-generated narratives can enable new directions for hybrid clinical prediction systems.

---


### 12. [Graph-Augmented Retrieval for Cross-Entity Financial Sentiment Analysis: A Comparative Study](https://arxiv.org/abs/2606.00062)

**<font color=#1a73e8>作者：</font>** Rajan Bastakoti, Sagar Bhetwal, Nirajan Acharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become foundational for grounding large language models in domain-specific corpora, yet conventional vector-based RAG systems are fundamentally limited in their ability to capture the structured, multi-entity relationships that underpin financial market analysis. This paper presents a comprehensive comparative study of a novel two-hop Graph-RAG architecture versus a standard vector-only baseline for cross-entity financial sentiment analysis. Our system constructs a sentiment-weighted knowledge graph of 59 equity entities from 255 news articles covering 10 major technology stocks, then augments dense retrieval with intensity-filtered graph traversal over INFLUENCES edges to surface relational evidence inaccessible to vector search alone.
We evaluate both architectures on 100 grounded queries (30 Direct, 70 Relational) using semantic similarity, entity recall, RAGAS metrics, latency benchmarks, and ablation studies. Graph-RAG achieves a statistically significant improvement in entity recall (+6.4%, p < 0.001, Wilcoxon signed-rank) and delivers substantially more relevant answers for complex multi-entity queries (+11.7% Answer Relevancy), with gains concentrating in relational question types (+16.1%). Critically, these improvements come at no measurable cost to answer quality (delta = +0.001 semantic similarity, Cohen's d = 0.078), with a modest 22.6% increase in mean latency offset by an 80% reduction in latency variance.
An ablation study on the graph traversal intensity threshold reveals an inverted-U relationship with answer quality, identifying tau = 0.5 as optimal over the production default of tau = 0.7. These findings characterize a precision-for-coverage trade-off inherent to graph-augmented retrieval and provide actionable architectural guidance for practitioners building RAG systems for multi-entity financial analysis.

---


### 13. [BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization](https://arxiv.org/abs/2606.00079)

**<font color=#1a73e8>作者：</font>** Jiayu Zhao, Zihan Teng, Minhao Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) large language models reduce per-token computation through sparse expert activation, but their deployment remains memory-intensive because all expert weights must be kept resident in memory. Existing MoE compression methods struggle in the ultra-low-bit regime: pruning irreversibly removes model capacity, while coarse-grained quantization fails to allocate bits according to heterogeneous expert and weight-direction importance. We propose BitsMoE, a spectral-energy-guided bit-allocation framework for MoE LLM quantization. BitsMoE decomposes each MoE layer by SVD into a shared basis and expert-specific spectral factors, retaining the shared basis without quantization to preserve common cross-expert structure and using the expert-specific factors as fine-grained quantization units. To determine the bit-width of each unit, BitsMoE formulates spectrum-wise mixed-precision quantization as an activation-aware reconstruction surrogate and solves an integer linear program that minimizes estimated reconstruction loss under a fixed bit budget. Experiments across multiple MoE LLMs show that BitsMoE substantially reduces downstream task accuracy degradation in ultra-low-bit regimes. Under 2-bit quantization on Qwen3-30B-A3B-Base, BitsMoE accelerates quantization by 12.3$\times$, improves average accuracy by 27.83 percentage points, and increases decoding speed by 1.76$\times$ over GPTQ. Our model and code are publicly available at this https URL.

---


### 14. [Planktonzilla: Multimodal dataset and models for understanding plankton ecosystems](https://arxiv.org/abs/2606.00080)

**<font color=#1a73e8>作者：</font>** Alan Gerson Contreras Montanares, Luis Valenzuela, Luis Martí 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Marine plankton underpin aquatic food webs and play a key role in global CO2 sequestration, making reliable species identification critical for understanding ocean health and climate feedbacks. Existing classification models perform well on individual collections but fail to generalize across instruments and environments due to isolated training datasets and inconsistent labels. To address this, we introduce Planktonzilla-17M, a unified dataset consolidating publicly available plankton image collections spanning thirteen imaging systems. It comprises 17.4 million images with standardized taxonomy and geo-environmental metadata, including 3.74 million plankton images spanning over 602 taxonomic classes, of which 201 are identified at the species level, making it the largest and most comprehensive plankton image dataset to date. Using this large-scale dataset, we perform a controlled comparison between supervised and CLIP-style image--text training on a shared ViT backbone. We find that a supervised classifier matches or exceeds CLIP-style training when trained using taxonomic lineage as text. We further observe that BioCLIP and BioCLIP2 perform poorly on plankton in zero-shot and few-shot settings. Leveraging Planktonzilla-17M improves plankton classification performance, highlighting the limitations of current biological foundation models in marine imaging domains.

---


### 15. [Structured Visual Evidence Decomposition for Evidence-Grounded Multimodal Screening of Obstructive Sleep Apnea-Hypopnea Syndrome](https://arxiv.org/abs/2606.00087)

**<font color=#1a73e8>作者：</font>** Chen Zhan, Yingchen Wei, Xiaoyu Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective pre-polysomnography screening for obstructive sleep apnea-hypopnea syndrome (OSAHS) requires combining clinical risk factors with visible craniofacial and neck cues. Directly prompting general-purpose multimodal foundation models for medical yes/no decisions can yield unstable, poorly calibrated outputs. We propose EviOSAHS, an evidence-grounded multimodal reasoning framework that separates image-only anatomical evidence acquisition from final clinical adjudication. Each frontal facial image is decomposed into seven fixed anatomical queries covering the neck, chin, mouth, face/neck fat, lower jaw, midface, and nose. Visual responses are converted into structured evidence cards recording target anatomy, visibility, risk direction, evidence strength, confidence, and a concise summary. These cards are combined with a cleaned clinical profile only in the final stage, where a large language model performs balanced binary screening adjudication. We evaluated EviOSAHS on a 642-subject cohort, mapping normal subjects to screening-negative and mild, moderate, or severe OSAHS subjects to screening-positive. EviOSAHS achieved 88.47% accuracy, 94.86% sensitivity, 93.74% F1-score, and a 5.14% false-negative rate, outperforming clinical-only prompting, direct multimodal prompting, and naive two-stage pipelines under a unified protocol. Ablations showed that seven-question visual decomposition and balanced final adjudication were critical to the high-sensitivity operating point. A question-level audit of 4,494 visual outputs showed a 100% structured parse rate and 93.88% high-visibility rate. EviOSAHS provides an auditable, high-sensitivity workflow for binary pre-polysomnography OSAHS screening, but should be viewed as a triage assistant rather than a diagnostic system. Prospective validation, external testing, and calibrated operating-point control are needed before clinical deployment.

---


### 16. [DLLM-JEPA: Joint Embedding Predictive Architectures for Masked Diffusion Language Models](https://arxiv.org/abs/2606.00091)

**<font color=#1a73e8>作者：</font>** Sangdae Nam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Joint Embedding Predictive Architectures (JEPAs) have reshaped self-supervised representation learning in vision. The recent LLM-JEPA ported JEPA to autoregressive language models but inherited two steep costs from the causal-attention substrate: it demands explicit multi-view data (e.g., text-code pairs), and it requires two gradient-carrying forward passes per step. We introduce DLLM-JEPA, which pairs JEPA with masked-diffusion language models to eliminate both costs at once. The bidirectional attention of diffusion models yields two semantically distinct views of the same input via different masking rates -- no explicit pairs needed -- and supports a single gradient-carrying forward pass, cutting training FLOPs by 33% relative to LLM-JEPA. DLLM-JEPA improves over diffusion-only fine-tuning in every (task, architecture) combination we evaluate: up to +18.7 pp on LLaDA-8B GSM8K and +11.4 pp on Dream-7B GSM8K, with consistent positive gains on Spider, NL-RX-SYNTH, and Django. Beyond accuracy, DLLM-JEPA exhibits a dual-win property: on LLaDA-8B with the Wide-t configuration, it simultaneously raises GSM8K accuracy (67.1 vs. 65.2, +1.8 pp), drives held-out Wikitext loss below the pre-trained base, and preserves MMLU accuracy at base level across three fine-tuning seeds -- whereas an L2-to-base parameter anchor matches baseline accuracy with no task gain. Layer-wise probing reveals the mechanism: a geometric-functional drift dissociation in which the fine-tuned backbone moves further from the pre-trained weights than the baseline yet forgets less on held-out Wikitext, with the amplification concentrated in middle transformer layers. The pattern appears on Dream-7B as well, indicating the phenomenon is not specific to a single backbone.

---


### 17. [Agreement Metrics for LLM-as-Judge Evaluation: What to Report and Why](https://arxiv.org/abs/2606.00093)

**<font color=#1a73e8>作者：</font>** Delip Rao, Chris Callison-Burch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Validating an LLM judge against human annotations usually means reporting several agreement statistics: accuracy, precision, recall, $F_1$, Cohen's $\kappa$, and one or more rank correlations. A survey of 24 recent LLM-as-judge papers finds metric choice entangled with the judgment scale, tie handling, invalid outputs, and abstention handling, and those choices rarely stated. For binary criteria -- the common case in rubric-based evaluation, where each criterion is graded MET or UNMET -- most of the reported numbers are redundant: Pearson's $r$, Spearman's $\rho$, Kendall's $\tau_b$, the phi coefficient $\phi$, and the Matthews Correlation Coefficient all reduce to a single number on non-degenerate binary data, so reporting several of them only creates an illusion of corroborating evidence. Cohen's $\kappa$ is the one agreement coefficient that adds information: it shares $\phi$'s numerator but normalizes differently, and the gap between them measures how far the judge's positive-label rate has drifted from the human's. We then trace what changes when a judge may abstain with a CANNOT_ASSESS verdict: the three common ways of handling abstentions are not interchangeable preprocessing choices but answer different questions, and they break the binary equivalences. The same equivalences reappear, up to a negligible finite-sample correction, for multi-judge ensembles scored with Fleiss' $\kappa$ or Krippendorff's $\alpha$. We close with a reporting checklist that names the judgment scale, the abstention and tie handling mode, coverage, the confusion matrix, and the aggregation level alongside any scalar agreement coefficient.

---


### 18. [Diversity Over Frequency: Rethinking Tool Use in Visual Chain-of-Thought Agents](https://arxiv.org/abs/2606.00096)

**<font color=#1a73e8>作者：</font>** Dong-Hee Kim, Reuben Tan, Donghyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual agents employ external visual tools within visual chains of thought to incorporate fine-grained evidence. While prior work has mainly studied these tools in visual search tasks, their role in more complex visual reasoning remains underexplored. In this paper, we move beyond simple visual search tasks to investigate more challenging tasks, including 3D spatial reasoning and medical visual question answering, where agents must integrate tool-acquired local evidence with the global context.
We identify a {tool-use collapse phenomenon: models progressively stop using tools while still achieving higher task accuracy.
Moreover, we observe a clear asymmetry: (i) completely eliminating tool use degrades performance, whereas (ii) incentivizing tool use yields only marginal gains despite substantially increasing usage.
We find that vanilla training and tool-use encouragement both reduce rollout diversity, explaining why higher tool use does not yield stronger reasoning performance.
Motivated by these findings, we add an entropy regularization term to encourage diverse rollout exploration, achieving the best performance despite gradually declining tool usage.
% We further observe similar dynamics on medical VQA, suggesting that tool-use collapse is not limited to 3D spatial reasoning.
Overall, our findings suggest a training-time view of tools as scaffolding, where broader exploration over language generation and visual tool invocation improves reasoning despite tool-use collapse.
Project page: this https URL

---


### 19. [CoCoVideo: The High-Quality Commercial-Model-Based Contrastive Benchmark for AI-Generated Video Detection](https://arxiv.org/abs/2606.00101)

**<font color=#1a73e8>作者：</font>** Huidong Feng, Wentao Chen, Jie Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of artificial intelligence generated content (AIGC) technologies, video forgery has become increasingly prevalent, posing new challenges to public discourse and societal security. Despite remarkable progress in existing deepfake detection methods, AIGC forgery detection remains challenging, as existing datasets mainly rely on open-source video generation models with quality far below that of commercial AIGC systems. Even datasets containing a few commercial samples often retain visible watermarks, compromising authenticity and hindering model generalization to high-fidelity AIGC videos. To address these issues, we introduce CoCoVideo-26K, a contrastive, commercial-model-based AIGC video dataset covering 13 mainstream commercial generators and providing semantically aligned real-fake video pairs. This dataset enables deeper exploration of the differences between authentic and high-quality synthetic videos and establishes a new benchmark for highly realistic video forgery detection. Building on this dataset, we propose CoCoDetect, a detection framework integrating contrastive learning with confidence-gated multimodal large language model (MLLM) inference. An R3D-18 backbone extracts spatio-temporal representations, while a confidence gate routes uncertain cases to an MLLM for reasoning about physical plausibility and scene consistency. Extensive experiments on CoCoVideo-26K and public benchmarks demonstrate state-of-the-art performance, validating the framework's robustness and generalizability. Our code and dataset are available at this https URL.

---


### 20. [Evaluating Interactive Reasoning in Large Language Models: A Hierarchical Benchmark with Executable Games](https://arxiv.org/abs/2606.00103)

**<font color=#1a73e8>作者：</font>** Mingyuan Fan, Weiguang Han, Daixin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a multi-turn interactive framework for reasoning evaluation that treats reasoning as active evidence acquisition and belief updating. Wherein, LLMs receive only the task rules, must issue targeted queries to a hidden environment, integrate partial observations over time, and decide when to submit a final answer. Beyond standard success rate and interaction efficiency, we evaluate contextual robustness under controlled contextual perturbations, and metacognitive adaptation through counterfactual revision and necessity judgment. We instantiate the framework as a benchmark of 474 executable games, each evaluated under five fixed configuration search spaces corresponding to five difficulty levels, and evaluate a broad set of frontier LLMs. Results show that the benchmark is highly discriminative, exposing large differences not only in success rate but also in interaction efficiency. Moreover, we empirically show that contextual perturbations cause moderate but consistent declines, whereas counterfactual revision and necessity judgment lead to much larger drops.

---


### 21. [Visual-Noise Guided In-Context Distillation for Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2606.00105)

**<font color=#1a73e8>作者：</font>** Junkai Chen, Yuhao He, Junxiang You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress on vision-language tasks, but they may also memorize and expose sensitive or restricted knowledge, raising concerns about privacy and broader safety risks. Machine Unlearning (MU) provides a promising way to remove targeted undesirable knowledge from trained models without retraining from scratch while preserving general model utility. Nevertheless, effective unlearning in MLLMs remains particularly challenging. Existing training-based methods often struggle to balance unlearning effectiveness and model utility. In contrast, training-free methods such as in-context unlearning preserve model utility by avoiding parameter updates, but they do not remove memorized knowledge at the parameter level and may remain vulnerable to reverse-engineering attacks. More importantly, in-context unlearning is insufficient in multimodal settings, where visual inputs can provide strong conditioning signals and induce undesirable outputs. To address these challenges, we propose Visual-Noise Guided In-Context Distillation (VGID), a distillation-based framework for MLLM unlearning. VGID dynamically constructs an unlearning-oriented teacher distribution from the frozen base model through dual-modal intervention that combines visual perturbation with textual in-context unlearning. The resulting intervention-induced distribution serves as a teacher signal for distillation, guiding the student model toward parameter-level unlearning without requiring external teacher models or explicit undesirable response annotations. Experimental results show that VGID achieves strong unlearning effectiveness while preserving competitive model utility, reducing forget set ROUGE-L by 0.371 with only a 0.055 drop in retain set ROUGE-L in a representative setting.

---


### 22. [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](https://arxiv.org/abs/2606.00123)

**<font color=#1a73e8>作者：</font>** Zixian Su, Hongkai Zhang, Fan Gao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown strong performance on public medical benchmarks, yet existing evaluations often remain weak proxies for clinical use, relying on isolated inputs and simplified recognition-style tasks. We introduce CardioLens, a leakage-resistant evaluation testbed for multi-sequence Cardiovascular Magnetic Resonance (CMR), constructed from private hospital archives through a rigorous report-to-QA construction and verification pipeline. CardioLens contains 473,896 slices and 13,494 verified QA pairs across 4D Cine, LGE, perfusion, and T2-weighted imaging, and evaluates three stages of CMR interpretation: image understanding, report generation, and disease diagnosis. Across 24 state-of-the-art MLLMs, CardioLens reveals a substantial clinical reality gap: models perform poorly overall, with performance degrading along the real CMR workflow. Confusion analysis further shows a category-collapse failure mode, where models default to frequent abnormal categories rather than distinguishing clinically distinct findings. To rule out MLLM-compatible input construction as the primary cause, we compare random, clinically motivated, and data-driven slice selection protocols under different slice budgets; performance changes only marginally, typically by about 1%. Explicit reasoning prompts also fail to rescue performance, often making models more conservative rather than improving visual evidence use. These results show that current MLLMs remain far from reliable CMR interpretation, where clinical decisions require integrating distributed evidence across sequences, views, and temporal phases. CardioLens provides a clinically grounded testbed for developing next-generation MLLMs toward real-world clinical deployment.

---


### 23. [A Shared Valence Axis Across Modern LLMs and Human EEG: The Saturation Regularity](https://arxiv.org/abs/2606.00129)

**<font color=#1a73e8>作者：</font>** Yousef A. Radwan, Xuhui Liu, Kilichbek Haydarov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as powerful representation learners whose internal features increasingly align with human cognition. We study whether modern LLMs can serve as a lens for understanding neural representations in the human brain, focusing on emotional valence in EEG.
We first build a one-dimensional valence direction, the V-axis, from modern LLMs using only nine emotion-evocative sentences. We validate it through zero-shot transfer to sentiment benchmarks and cross-model consistency across fourteen LLMs. We then show that this LLM-derived direction maps onto human neural activity. On a public EEG cohort of 123 subjects watching affective videos, a single linear projection on EEG features tracks the V-axis position of each stimulus. Moreover, 36 EEG emotion classifiers trained without exposure to the V-axis spontaneously rediscover the same direction in their internal representations, suggesting that the same valence structure emerges in both language models and human electrophysiology.
Yet this convergence does not provide an effective training signal. We test twenty-five alignment strategies, including knowledge distillation, representational similarity, contrastive, and topographic losses; none improve decoding, and sixteen significantly reduce accuracy. We formalize this result as the saturation regularity: once task labels alone drive a brain-decoding network onto the target direction, additional supervision mainly distorts an already-saturated basin, while the load-bearing within-class residual receives little useful gradient.
This regularity also indicates where improvement should come from: the residual subspace unreachable by supervision. Motivated by this insight, we ensemble across residual diversity rather than supervising the basin, improving balanced accuracy by 10.5% over the prior best on FACED, with the same effect replicated on SEED-V.

---


### 24. [World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](https://arxiv.org/abs/2606.00133)

**<font color=#1a73e8>作者：</font>** Arif Hassan Zidan, Yi Pan, Hanqi Jiang 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models, internal simulators that learn the structure and dynamics of an environment, have emerged as a central paradigm in the pursuit of artificial general intelligence, enabling agents to predict, plan, and reason within learned representations. Despite rapid progress across reinforcement learning, robotics, autonomous driving, and video generation, the field lacks a unified framework integrating its diverse architectural choices, training methods, reasoning mechanisms, and application settings. This survey addresses that gap with a multi-axis taxonomy organized along four dimensions: (i) architecture, encompassing representation format, dynamics formulation, input modality, learning paradigm, and downstream application; (ii) methodological family, including state-space and recurrent approaches, transformer-based models, diffusion-based generators, physics-informed networks, and language-augmented multimodal systems; (iii) reasoning strategy, covering imagination-based planning, latent policy learning, counterfactual reasoning, and planning under uncertainty; and (iv) application domain, spanning robotics, autonomous driving, video prediction, multimodal agents, reinforcement learning, scientific modeling, medical imaging, educational measurement, and business and finance. Tracing the field from early cognitive-science foundations to milestone systems such as PlaNet, the Dreamer family, MuZero, Sora, Cosmos, and Genie, we examine how these dimensions interact and highlight the recent convergence of chain-of-thought reasoning with world-model imagination. We review evaluation protocols and benchmarks, identify persistent challenges such as compounding prediction errors, sim-to-real transfer, and fragmented evaluation, and outline future directions toward unified multimodal world models, foundation-scale interactive simulators, and safe deployment in safety-critical domains.

---


### 25. [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/abs/2606.00135)

**<font color=#1a73e8>作者：</font>** Tong Liu, Cheng Qian, Matej Cief 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-calling is a central component of modern large language model (LLM) agents, equipping them with skills beyond their parametric knowledge. This paper studies tool-calling along two complementary axes: effectiveness, i.e., how this capability is measured, and efficiency, i.e., how it is learned. On effectiveness, we systematically analyze tool-calling evaluation pipelines and show that results can be highly sensitive to seemingly minor, often undocumented implementation choices including the random seed, system prompt, multi-turn template construction, and how prior interaction/reasoning history is carried forward. These choices can lead to substantial differences in reported performance, especially in multi-turn settings where without rigorous standardization, leaderboard rankings are unreliable. On efficiency, we examine standard reinforcement learning (RL) for tool-calling and identify two sources of computational waste: (i) during rollouts, many prompts produce no learning signal, and (ii) during policy updates, optimization incurs high computational cost. Guided by these findings, we introduce two techniques that accelerate RL-based tool-calling training, achieving substantial wall-clock speedup without degrading performance.

---


### 26. [RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning with Alleviated Forgetting](https://arxiv.org/abs/2606.00147)

**<font color=#1a73e8>作者：</font>** Yuduo Li, Xiaofeng Shi, Qian Kou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain-specific supervised fine-tuning (SFT) often improves in-domain performance at the cost of degrading a model's general capabilities. We view this degradation through two practical gaps in domain SFT: a supervision-compatibility gap, where domain targets differ in style and reasoning format from the original model's natural responses, and a trajectory-preservation gap, where teacher-forced SFT optimizes fixed target tokens without constraining the model's behavior on its own generated prefixes. This process fails to preserve the model's original behavior. We propose RAFT (Data Refinement and Adaptive Distillation for Domain Fine-Tuning with Alleviated Forgetting), a two-stage framework that addresses both factors. First, RAFT constructs model-compatible supervision through self-conditioned rewriting, semantic filtering, and answer fusion. Second, RAFT performs Answer-Conditioned On-Policy Distillation, where the original instruction-tuned model provides soft targets on student-generated trajectories while being conditioned on the fused answer as helpful context. We further introduce top-K temperature distillation and EMA-based adaptive loss balancing to stabilize the domain-general trade-off. Across three instruction-tuned backbones and five domains, RAFT improves average domain accuracy by 23.2% over standard SFT, while recovering part of the SFT-induced degradation on MS-Bench and IFEval, with relative improvements of 18.2% and 10.2%, respectively. These results show that coupling data refinement with trajectory-level preservation provides an effective recipe for domain fine-tuning with alleviated forgetting.

---


### 27. [StemBind: When MLLMs Get Lost Between Rules and Instances in Abstract Visual Reasoning](https://arxiv.org/abs/2606.00148)

**<font color=#1a73e8>作者：</font>** Xixiang He, Baiqi Wu, Xingming Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often know the rule but pick the wrong answer: on abstract visual reasoning (AVR) tasks, a model can describe what it sees and name the underlying pattern, yet still fail to choose the matching candidate. Existing AVR benchmarks cannot detect this because they collapse perception, rule induction, and answer selection into a single right-or-wrong signal. We introduce StemBind, a shared-stem diagnostic benchmark that probes the same visual stem with three aligned questions: Perception (what is in the image), Rule (what pattern governs it), and Full (which option completes it), so a final-answer error can be attributed to a specific sub-step on the same evidence. StemBind contains 2,298 curated knowledge-light stems across nine auditable visual operations, totaling 19,533 P/R/F tasks, with each full item annotated by Sternberg's four reasoning stages (S1 Encode, S2 Infer, S3 Map, S4 Apply). Evaluating 24 frontier MLLM configurations yields four findings. (i) The R-F chasm: rule accuracy exceeds full-item accuracy on 22 of 24 models, so most failures happen after the rule is identified. (ii) A persistent binding gap: even when P and R are both correct on the same stem, models still answer F incorrectly 51.2% of the time. (iii) The bottleneck is S3: process diagnostics and Stage-wise Stimulus Augmentation localize the dominant failure to rule-to-instance mapping. (iv) Scaling and thinking do not help: neither larger models nor explicit thinking mode reliably closes the gap, and thinking even lowers rule and full-item accuracy. StemBind reframes AVR evaluation from final-answer ranking to locating where abstract visual reasoning breaks down, identifying rule-to-instance binding as a concrete next target for vision-grounded reasoning.

---


### 28. [DiffCrossGait: Trajectory-Level Alignment for 2D-3D Cross-Modal Gait Recognition via Latent Diffusion](https://arxiv.org/abs/2606.00153)

**<font color=#1a73e8>作者：</font>** Zhiyang Lu, Ming Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal 2D-3D gait recognition is impeded by inherent domain discrepancies between 2D silhouette and 3D LiDAR range-view representations. While prior methods align only final embeddings, we propose DiffCrossGait, which reformulates cross-modal matching as trajectory-level alignment in an identity-relevant latent diffusion space, rather than assuming full equivalence between 2D and 3D observations. By driving both modalities with shared Gaussian noise within a latent space, we enable continuous alignment throughout the generative evolution. We introduce a Tri-Phase Alignment Strategy that exploits varying noise intensities to enforce identity anchoring, dynamics consistency, and cross-modal structural recoverability, thereby constraining both modalities to share denoising dynamics and bottleneck structure, which promotes modality-invariant gait features. Crucially, our framework decouples generative alignment from the discriminative backbone; the diffusion mechanism serves exclusively as a training objective, ensuring high inference efficiency by eliminating the computational overhead of iterative denoising. Extensive experiments on the SUSTech1K and FreeGait benchmarks demonstrate that DiffCrossGait achieves state-of-the-art performance.

---


### 29. [UF-AMA: A unified framework for cross-domain emotion recognition via adaptive multimodal alignment](https://arxiv.org/abs/2606.00170)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Shuo Wang, Junhong Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, emotion recognition based on physiological signals such as electroencephalogram (EEG) has gained considerable attention, as internal physiological data offer greater objectivity and reliability compared to external behavioral data like facial expressions. However, due to distribution shifts caused by individual and contextual differences, along with variations in sample quality across modalities, constructing a cross-domain multimodal emotion recognition model with high generalization and robustness remains a key challenge. In this study, we propose a Unified Framework with Adaptive Multimodal Alignment (UF-AMA) to address cross-subject and cross-session emotion recognition using multimodal physiological signals. First, we construct a cross-modal feature fusion network comprising Transformer encoders and multi-head cross-attention modules, enabling the deep integration of EEG signals and eye-tracking data. Subsequently, we introduce a confidence-aware screening mechanism that dynamically assesses the predictive reliability of each modality branch on target domain samples, partitions samples into different quality subsets, and accordingly applies global consistency alignment and cross-modal distillation. Finally, we propose a multi-level domain adaptation framework that jointly optimizes the marginal and conditional distributions of both local modality-specific and global fusion features, thereby reducing cross-domain distribution shifts at multiple granularities. Extensive experiments on the SEED and SEED-IV datasets demonstrate that UF-AMA achieves state-of-the-art (SOTA) performance in both cross-subject and cross-session tasks. The source code is available at: this https URL.

---


### 30. [Agentic Transformers Provably Learn to Search via Reinforcement Learning](https://arxiv.org/abs/2606.00183)

**<font color=#1a73e8>作者：</font>** Tong Yang, Yu Huang, Yingbin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree search is a central abstraction behind many language-agent reasoning and decision-making tasks: agents must explore actions, remember failures, and backtrack toward promising alternatives. Yet, we lack a theoretical understanding of how transformer-based policies acquire such search capabilities from the training dynamics of reinforcement learning (RL). We study this question in a stochastic $k$-ary tree environment, where an agentic transformer observes only its trajectory history through interaction and receives a terminal reward for reaching a hidden leaf goal node. We first construct a two-head transformer that implements randomized depth-first search (DFS): one head tracks previous actions, while the other detects failure outcomes and triggers backtracking. We then analyze the training dynamics of policy gradient under a depth-wise curriculum, showing that this same DFS mechanism emerges in stages from sparse reinforcement feedback without expert demonstrations. The resulting policy exhibits depth generalization: after training only on depth-$1$ and depth-$2$ trees, it succeeds on deeper full trees. We further show that, under imbalanced goal distributions, discounting the return leads to a ranked DFS policy that prioritizes higher-probability branches. Overall, our results identify a mechanistic normal form for transformer-based search, in which attention heads specialize and cooperate to extract decision-relevant traces from context and convert them into agentic action selection via RL training.

---


### 31. [Learning to Construct Practical Agentic Systems](https://arxiv.org/abs/2606.00189)

**<font color=#1a73e8>作者：</font>** Aditya Kumar, Zhihan Lei, Jerry Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated design and optimization of agentic LLM-based systems leads to sophisticated systems that substantially improve result quality over off-the-shelf agentic patterns. However, studies of fielded agentic systems show that production systems focus much more on issues such as simplicity, controllability, and predictability of inference costs. In this paper we propose principled approaches to designing and optimizing practical agentic systems. We describe an agent framework that enables designers to enforce modularity in agentic systems, by defining "pseudo-tools" that call LLMs recursively on a restricted context. Using this framework we hand-engineer agents for a diverse set of tasks, and show that relative to dynamically-planned workflows, hand-constructed fixed workflows are generally cheaper and more accurate. We then propose novel learning methods for the agentic components required by this framework, namely pseudo-tools and fixed workflows. These learning methods generally outperform hand-engineered agents. We also exploit the modularity of the framework to apply multi-objective optimization methods to jointly optimize cost and response quality and blend the results of multiple learning systems.

---


### 32. [BAGEN: Are LLM Agents Budget-Aware?](https://arxiv.org/abs/2606.00198)

**<font color=#1a73e8>作者：</font>** Yuxiang Lin, Zihan Wang, Mengyang Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While agents are increasingly spending more resources, today agent cost is mostly measured only after execution. A Budget-Aware Agent (BAGEN) should treat budget as an active control signal, rather than a passive cost metric. We first systematically define budget estimation as internal budgets (from agent computation) and external budgets (from agent actions). We then formalize budget-awareness as progressive interval estimation: at each step of a plan, an agent should predict an upper and lower bound on remaining budget, and alert when completion is unlikely. Scoring with a rollout-replay protocol, we find consistent failure patterns on four environments and five frontier agents: (1) strong agents do not necessarily have strong budget-awareness, with correlation r=0.35. (2) frontier models are consistently over-optimistic, continue spending on tasks that are unlikely to succeed, instead of alerting the user early. (3) budget-aware signal is actionable and trainable. Early stop saves 28-64% tokens on failed trajectories, and SFT+RL strengthens early stop and alert behavior. (4) precise interval calibration remains challenging, with interval coverage capping at 47% after SFT+RL. Project page: this https URL

---


### 33. [APE: Agentic Prompt Enhancer for Image Generation and Editing](https://arxiv.org/abs/2606.00204)

**<font color=#1a73e8>作者：</font>** Zijian Huang, Jay Zhangjie Wu, Zian Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural language has become a powerful interface for image generation and editing, yet text-guided visual systems remain highly sensitive to prompt formulation. Semantically similar requests can produce different outputs depending on wording, specificity, and how explicitly visual constraints are stated, motivating prompt enhancement as a trainable component rather than a peripheral user choice. Existing strong enhancers often rely on large, proprietary LLMs such as ChatGPT or Gemini, adding cost, latency, and deployment dependence to the visual generation pipeline. We propose Agentic Prompt Enhancer (APE), a lightweight framework that post-trains small language models (SLMs) as prompt-enhancement agents. APE supports both single-agent rewriting and role-specialized multi-agent enhancement. Its single-agent instantiation, SAPE, rewrites the prompt in one pass, while its multi-agent instantiation, MAPE, decomposes enhancement into a router--rewriter--composer process for handling compositional constraints over objects, attributes, spatial relations, and edits. With task-aware rewards and post-training protocols, APE improves visual alignment and prompt following without modifying the downstream visual model. Experiments on challenging image generation and editing benchmarks demonstrate that post-trained small prompt enhancers reliably outperform their base counterparts, narrowing the gap to closed-source prompt enhancers; in addition, MAPE proves particularly strong on complex compositional tasks within these benchmarks.

---


### 34. [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206)

**<font color=#1a73e8>作者：</font>** Sanae Lotfi, Polina Kirichenko, Steven Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is widely used to deploy large language models efficiently, but its effect on reasoning models is not well understood. Across math, coding, and science QA, we find that aggressive PTQ reduces accuracy while increasing chain-of-thought (CoT) length. Surprisingly, we show that in up to 52% of the quantized models' failures, models reach the right answer in intermediate reasoning steps but do not output it as a final answer. To understand why quantization leads to this increase in overthinking errors, we measure the token-level KL divergence between quantized and full-precision output distributions. Positions with high KL divergence correlate strongly with high next-token entropy, and at these positions quantized models disproportionately sample overthinking markers such as "wait", "but", and "alternatively". We show that simply introducing a training-free logit penalty on a curated set of overthinking markers can reduce CoT length by 12--23% while preserving or improving accuracy across 5 models (1.5B-32B parameters), 3 quantization methods, and 5 benchmarks, yielding a favorable Pareto frontier of accuracy against reasoning cost compared to penalizing other token sets. Overthinking errors produced by quantized models are particularly reduced by up to 58%.

---


### 35. [A Pre-Training Analogue of Grokking in Language Models: Tracing Delayed Grammatical Generalization](https://arxiv.org/abs/2606.00230)

**<font color=#1a73e8>作者：</font>** Sherin Muckatira, Namrata Shivagunde, Vijeta Deshpande 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking, the phenomenon in which neural networks generalize long after fitting their training data, has been studied in supervised settings on many epochs. LLM pre-training instead involves next-token prediction over an unlabeled corpus, with limited data repetition and no explicit train/validation split. To address this, we propose an exposure-based framework that enables the study of grokking-like dynamics during LLM pre-training. We ground our evaluation in BLiMP minimal pairs, which provide controlled grammatical contrasts. For every BLiMP minimal pair, we identify a critical phrase, the smallest continuous span that captures the grammatical contrast and the phenomenon-relevant context. Examples whose critical phrase appears in the pre-training window are assigned to the proxy-train split; the remaining examples are assigned to the proxy-validation split. Across five grammatical phenomena, we observe delayed generalization. Analyzing pre-training checkpoints before and after generalization shows that grammatical concept vectors become more predictive of grammatical acceptability and occupy a higher-dimensional subspace after generalization. We also find that attention from the critical token to the relevant context token is concentrated in a small number of heads.

---


### 36. [TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation](https://arxiv.org/abs/2606.00232)

**<font color=#1a73e8>作者：</font>** Kaixiang Zhao, Tianrun Yu, Shawn Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study fact-level repair for multimodal generation, where a fluent output may contain specific facts that are not supported by the input. Existing inference-time repair methods often generate feedback by jointly conditioning on the input and the current output. This design has two limitations: hallucinated claims in the output can bias the model's interpretation of the input, and free-form feedback cannot be ranked or scheduled at the fact level. We present TIGER, an inference-time framework that redesigns feedback for localized repair. TIGER independently extracts an observation graph from the input and a claim graph from the current output, then assigns each claim a graph-conditioned risk score based on support and conflict. The model repairs selected high-risk claims while keeping the backbone frozen. We provide a convergence analysis showing that the expected total risk decreases geometrically to an explicit asymptotic bound under mild assumptions. Experiments across four cross-modal paths, including image-to-text, image+text-to-text, audio-to-text, and video-to-text, show that TIGER reduces unsupported content while preserving task quality. The gains hold across multiple backbones, and a CrisisFACTS case study suggests that the same repair mechanism can improve grounding in multi-source settings.

---


### 37. [MindZero: Learning Online Mental Reasoning With Zero Annotations](https://arxiv.org/abs/2606.00240)

**<font color=#1a73e8>作者：</font>** Shunchi Zhang, Jin Lu, Chuanyang Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective real-world assistance requires AI agents with robust Theory of Mind (ToM): inferring human mental states from their behavior. Despite recent advances, several key challenges remain, including (1) online inference with robust uncertainty updates over multiple hypotheses; (2) efficient reasoning suitable for real-time assistance; and (3) the lack of ground-truth mental state annotations in real-world domains. We address these challenges by introducing MindZero, a self-supervised reinforcement learning framework that trains multimodal large language models (MLLMs) for efficient and robust online mental reasoning. During training, the model is rewarded for generating mental state hypotheses that maximize the likelihood of observed actions estimated by a planner, similar to model-based ToM reasoning. This method thus eliminates the need for explicit mental state annotations. After training, MindZero internalizes model-based reasoning into fast single-pass inference. We evaluate MindZero against baselines across challenging mental reasoning and AI assistance tasks in gridworld and household domains. We found that LLMs alone are insufficient; model-based methods improve accuracy but are slow, costly, and limited by backbone MLLM capacity. In contrast, MindZero enhances MLLMs' intrinsic ToM ability and significantly outperforms model-based methods in both accuracy and efficiency, showing that mental reasoning can be effectively learned as a self-supervised skill.

---


### 38. [InfoAtlas: A Foundation Model for Zero-Shot Statistical Dependence Estimate](https://arxiv.org/abs/2606.00241)

**<font color=#1a73e8>作者：</font>** Zhengyang Hu, Yanzhi Chen, Hanxiang Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Measuring statistical dependency between high-dimensional random variables is a fundamental task in data science and machine learning. Neural mutual information (MI) estimators offer a promising avenue, but they typically require costly iterative optimization for each new dataset, making them impractical for real-time applications. We present InfoAtlas, a foundation model-like architecture that eliminates this bottleneck by directly inferring MI in a single forward pass. Pretrained on large-scale synthetic data with rich dependence patterns, InfoAtlas learns to identify diverse dependence structures and predict MI directly from the dataset. Comprehensive experiments demonstrate that InfoAtlas matches state-of-the-art neural estimators in accuracy while achieving $100\times$ speedup, can flexibly handle varying dimensions and sample sizes through a single unified model, and generalizes effectively to complex, real-world scenarios. By reformulating MI estimation as an inference task, InfoAtlas establishes a foundation for real-time dependency analysis.

---


### 39. [Effects of Varying LLM Access on Essay Writing Behavior](https://arxiv.org/abs/2606.00250)

**<font color=#1a73e8>作者：</font>** Julia Christenson, Karin de Langis, Shirley Anugrah Hayati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Investigating the degree to which large language models (LLMs) affect teaching and learning in universities can help identify strategies for integrating LLMs in a way that supports, rather than undermines, student learning outcomes. This study examined how varying levels of LLM assistance affect writing performance, engagement, and perceived authorship. We report a pilot study in which 24 college students were randomly assigned to write a short essay with no LLM access, limited access (<=3 prompts, responses capped at 100 words), or unlimited access. Overall essay quality was statistically indistinguishable across groups. Yet writing behavior and perceived authorship diverged sharply: students with limited access reported higher ownership (62.5% would submit the essay as independent work, vs. 25% in the unlimited group), stronger organizational gains, and more strategic, revision-focused prompting. The unlimited group spent more time writing, produced essays more similar to LLM output, and reported reduced creative expression. Our findings suggest that constraining, rather than banning, LLM access may preserve authorship confidence while retaining the scaffolding benefits of AI assistance.

---


### 40. [Capability Self-Assessment: Teaching LLMs to Know Their Limits](https://arxiv.org/abs/2606.00251)

**<font color=#1a73e8>作者：</font>** Haoyan Yang, Reza Shirkavand, Yukai Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability to recognize one's own limitations and decide whether to solve a problem or delegate is fundamental for reliable intelligent systems. Yet we show that modern large language models systematically lack this ability: across diverse model families and scales, they overestimate their competence and attempt queries they cannot solve. We refer to this ability as Capability Self-Assessment (CSA) and formulate it as a policy-learning problem, aiming to improve self-assessment while preserving the model's original capabilities. Our results show that reinforcement learning teaches CSA effectively, significantly outperforming supervised fine-tuning while preserving original capabilities. In contrast, supervised fine-tuning severely degrades the capabilities the model is meant to assess. Moreover, learned self-assessment behavior generalizes well out of distribution, suggesting that CSA is a transferable model trait. Finally, CSA is practically useful: it improves local-cloud decision making at inference time and provides a signal for targeted data selection during training.

---


### 41. [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/abs/2606.00267)

**<font color=#1a73e8>作者：</font>** Junwon Seo, Sushant Veer, Ran Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models (WMs) have shown promise for policy evaluation and improvement by imagining realistic future observations conditioned on ego-robot actions. While WMs can model distributions over futures, policy evaluation and improvement typically rely on nominal imaginations, which can miss high-impact outcomes of robot actions unless prohibitively many samples are drawn. To enable robust policy evaluation and improvement over WM imaginations, we propose StressDream, which steers imaginations toward high-impact yet plausible outcomes specified at inference time by optimizing the initial noise of diffusion-based WMs. However, optimizing high-dimensional noise is challenging: the optimization must reason about nuanced, scene-dependent target events in generated videos while avoiding out-of-distribution (OOD) noise that yields implausible imaginations. We address this with two complementary objectives: a semantic objective with a Vision-Language Model that provides informative gradients by reasoning about the generated video, and a plausibility objective that prevents the optimized noise from drifting OOD. With state-of-the-art video world models for autonomous driving and robotic manipulation, we show that StressDream effectively steers imaginations toward high-impact yet plausible outcomes specified by text at inference time, such as task failures, enabling robust policy evaluation and improvement by identifying actions whose plausible futures include undesirable outcomes. Video results are available at this https URL.

---


### 42. [Hyperbolic and Evidence-Prioritized Experts for Large Vision-Language Models](https://arxiv.org/abs/2606.00275)

**<font color=#1a73e8>作者：</font>** Zijie Zhou, Dandan Zhu, Hangxiangpan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have demonstrated impressive performance on multimodal tasks through scaled architectures and extensive training. Recent studies introduce Mixture of Experts (MoE) into LVLMs for improved computational efficiency. However, existing MoE approaches treat visual and linguistic modalities with symmetric architectures, overlooking the inherent asymmetry in how these two modalities are processed. This asymmetry causes two critical issues. First, text and vision form hierarchical rather than parallel relationships, as text queries typically describe partial aspects of complete visual scenes. Euclidean expert space struggles to encode such containment structures. Second, language experts in deeper layers progressively shift from evidence-based processing to parametric memory dependence, losing grounding in the provided visual and linguistic information. To address these issues, we propose AsyMoE, a novel architecture that explicitly models this asymmetry through three specialized expert groups. Intra-modality experts handle modality-specific processing. Hyperbolic inter-modality experts capture hierarchical cross-modal relationships through negative curvature geometry. Evidence-priority language experts suppress parametric memory activation and maintain contextual grounding throughout network depth. Extensive experiments demonstrate that AsyMoE achieves consistent improvements over baseline methods, with average gains of 1.5\% over MoE variants and up to 3.8\% on hallucination-sensitive tasks. AsyMoE activates 25.45\% fewer parameters compared to dense models.

---


### 43. [Parameter Alignment Mitigates Catastrophic Forgetting in Multilingual Expert Language Models](https://arxiv.org/abs/2606.00284)

**<font color=#1a73e8>作者：</font>** Sanchit Ahuja, Terra Blevins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While continual pretraining~(CPT) is a practical way to extend large language models to new languages, naïve finetuning on targeted data erodes existing capabilities through catastrophic forgetting. Organizing training around language families reduces cross-language interference but cannot alone prevent forgetting of the general knowledge needed for downstream tasks. We link this forgetting to parameter drift in multilingual CPT and present a suite of five layer-aware parameter alignment strategies: hard layer freezing, soft regularization, post-hoc weight reversion, and model merging. We systematically compare our alignment strategies against two unregularized CPT baselines on benchmarks spanning 32 training languages from five language families, plus held-out languages, across four evaluation axes: perplexity, reading comprehension, physical reasoning, and translation. Parameter alignment substantially reduces forgetting at minimal cost to language acquisition: layer freezing and regularization best preserve comprehension, whereas post-hoc reversion yields the strongest translation gains. Together, these results map the acquisition--forgetting frontier for family-expert CPT and offer practical deployment guidelines pairing each strategy to the tasks it best serves.

---


### 44. [Leveraging the Learning Curve: Reusing Existing Architectural Patterns to Design and Implement MAS](https://arxiv.org/abs/2606.00287)

**<font color=#1a73e8>作者：</font>** Arthur Casals, Anarosa A. F. Brandão  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent advancements in AI have led to the development of specialized systems related to multi-agent systems (MAS). However, the inherently collaborative nature of agents is often overlooked, and many of these specialized systems are used as components by other AI systems. From a software engineering perspective, this context can benefit from aligning the architectural characteristics of distributed systems with the inherently distributed nature of MAS. We propose that introducing a minimal set of agent-related concepts into the Distributed Systems (DS) domain can improve the engineering of modern MAS by leveraging techniques from DS engineering with established agent theory. In this study, we recapitulated the common origins of MAS and DS by drawing architectural parallels to establish a unified engineering approach. We then defined a minimal set of agent concepts to perform two practical studies on leveraging MAS development. First, we incorporated these concepts into a DS architectural pattern to design a distributed MAS. We then used these concepts in a graduate course to teach MAS engineering to students with no prior knowledge of agent theory. The learning outcomes from both courses included successful MAS implementation using DS tools and techniques. Although more than two-thirds of these students had no practical experience in developing distributed systems, the average final grade in both courses was above 80\%, thus validating our approach. Finally, we discuss how this study supports the development of advanced systems using modern AI techniques consistently with established agent-related research while leveraging established DS techniques and concepts.

---


### 45. [Model-Native Computing Architecture: Envisioning Future System Architecture Through the Lens of Computer Architecture](https://arxiv.org/abs/2606.00288)

**<font color=#1a73e8>作者：</font>** Hai Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are undergoing a transition from model technology to system technology. As developers use Codex, Claude Code, AutoGPT, and related agents to write code, manage projects, and execute multi-step tasks, recurring engineering problems such as cache reuse, context management, agent scheduling, and permission control increasingly resemble classical computer systems problems. This paper develops that analogy as a visionary survey. We map concepts from computer architecture to the emerging model-native stack and review work on LLM-as-OS, memory management, agent frameworks, tool protocols, multi-agent coordination, cognitive architectures, and safety governance. We argue that these strands address different layers of the same system but lack a unified model.
To fill this gap, we propose the Intelligent Computing Architecture Model (ICAM), a six-layer framework for model-native computing with explicit interface contracts and design axioms. ICAM resolves the apparent tension over whether an LLM is more like a CPU or an operating system through a dual-plane view: a probabilistic execution plane concerned with what can be computed, and a deterministic control plane concerned with what should be computed. We further introduce three design laws: the Semantic Locality Law for KV-cache reuse and inference speedup, the Context Budget Law for effective working sets under finite windows and attention decay, and the Agent Speedup Law for diminishing returns in multi-agent collaboration. We validate these laws against published system-level data and relate them to recent evidence on agentic software practices. We conclude by identifying where the analogy breaks down and outlining a research roadmap for model-native computing. This is a conceptual and survey contribution; it does not report new experiments.

---


### 46. [Rethinking the Role of Temperature in Large Language Model Distillation](https://arxiv.org/abs/2606.00306)

**<font color=#1a73e8>作者：</font>** Hoang-Chau Luong, Lingwei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reverse Kullback-Leibler (RKL) divergence is widely favored over forward KL (FKL) in large language models (LLM) distillation, yet this preference is largely based on comparisons that omit the temperature $\tau$, overlooking its central role in softening teacher distributions and improving knowledge transfer. In this work, we revisit temperature in LLM distillation and show that it fundamentally changes the comparison between FKL and RKL. Our analysis reveals an asymmetric effect: temperature substantially enriches FKL with non-dominant token signals, whereas it mainly rescales RKL gradients, causing FKL to benefit much more from $\tau$ scaling than RKL. This asymmetry overturns the standard empirical conclusion: although RKL outperforms FKL at $\tau=1$, FKL consistently surpasses RKL at higher temperatures across instruction-following benchmarks. Moreover, the impact of temperature is not limited to FKL; it improves a broader family of distillation objectives, enabling simple KL-based methods to achieve competitive performance against recent state-of-the-art LLM distillation approaches.

---


### 47. [Coupling Language Models with Physics-based Simulation for Synthesis of Inorganic Materials](https://arxiv.org/abs/2606.00315)

**<font color=#1a73e8>作者：</font>** Edward W. Staley, Tom Arbaugh, Michael Pekala 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern generative machine learning (ML) models can propose novel inorganic crystalline materials with targeted properties; however, synthesis planning of these materials remains difficult due to the complexity of the associated physical processes and limited availability of computational tools. We introduce a novel hybrid framework to evaluate Large Language Models (LLMs) in inorganic synthesis planning by combining thermodynamic databases with simplified kinetics models to approximate realistic synthesis conditions. As a case study, we focus on the niobium-oxygen system, which features multiple industrially relevant oxide phases with well-characterized data. In computational simulations, we compare LLM-generated synthesis routes with classical path-planning algorithms, showing that the implicit priors in LLMs can yield more viable strategies. In our evaluation setting, classical search methods serve primarily as a foil rather than a direct competitor. This illustrates the relative complexity of the problem and highlights where the LLM's implicit priors add value.

---


### 48. [Adversarially Robust Control of Conditional Value-at-Risk via Rockafellar-Uryasev Conformal Inference](https://arxiv.org/abs/2606.00320)

**<font color=#1a73e8>作者：</font>** Catherine Chen, Jingyan Shen, Zhun Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an online, distribution-free framework for controlling the Conditional Value-at-Risk (CVaR), extending conformal tail risk control to non-stationary and adversarial environments. Unlike classical risk control methods, which rely on stationarity or linearity of expectation, our approach provides provable safety guarantees for a nonlinear tail risk functional under arbitrary data-generating processes that may drift or shift strategically over time. By leveraging deep connections between conformal tail risk control, online learning, and the variational representation of CVaR introduced by Rockafellar and Uryasev, we develop a novel procedure for online CVaR control with adversarial regret guarantees. The proposed method operates without assumptions on the underlying data-generating process, making it broadly applicable in modern high-stakes deployment settings. We prove that the realized empirical CVaR is asymptotically controlled at the target level, and that the resulting control is asymptotically tight up to a finite-sample conservatism gap. We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.

---


### 49. [Training-Free Object-Agnostic Jam Detection in Fulfillment Centers](https://arxiv.org/abs/2606.00321)

**<font color=#1a73e8>作者：</font>** Ruiliang Liu, Tina Dongxu Li, Joshua Migdal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In fulfillment centers, diverse objects move continuously from inbound to outbound operations and can become jammed due to excessive conveyor friction, incorrect orientation, or mechanical failures. Traditional jam detection approaches rely on object detection models to identify objects, followed by tracking algorithms (such as IoU overlap and Kalman filtering) to monitor motion over time. This pipeline requires thousands of manual annotations, consuming approximately two weeks of effort, and is limited to annotated object classes. We present a training-free, object-agnostic jam detection method that eliminates the need for labeled data. Our approach uniformly samples reference points within the monitoring region when no objects are present. As objects occlude these points, we detect motion. When a sufficient fraction remains occluded beyond a temporal threshold, we classify the event as a jam. Unlike conventional point tracking--which treats occlusion as a failure case--our approach repurposes occlusion as a detection signal, monitoring whether reference points remain persistently occluded rather than tracking where they move. Our experimental evaluation on 1,069 videos demonstrates that AllTracker achieves 100.00% precision and 93.33% F1 score, significantly outperforming classical sparse tracking methods while maintaining training-free deployment. This approach offers three key advantages: (1) no training data or manual annotations, (2) object-agnostic generalization to arbitrary object types, and (3) significantly reduced development time.

---


### 50. [Which Institutional Frameworks Do Chatbots Assume? Auditing Jurisdictional Defaults in Multilingual LLMs](https://arxiv.org/abs/2606.00333)

**<font color=#1a73e8>作者：</font>** Zhizhi Wang, Harini Suresh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly answer questions about taxes, labor protections, healthcare, education, pensions, and administrative procedures, where usefulness often depends on the applicable jurisdiction. Multilingual users may write in their most comfortable language rather than one associated with the country or region whose rules apply. We ask whether deployed LLMs use input language as a default jurisdictional signal when prompts omit any country or region. Prior multilingual audits show that prompt language can shift cultural, political, or normative outputs; we examine which legal-administrative framework models supply when jurisdiction is underspecified. We evaluate seven LLMs developed in the United States or China on 60 underspecified legal-administrative prompts in English and Mandarin Chinese under three system-prompt conditions, yielding 2,520 manually annotated responses. Across models and conditions, Chinese input more often produces China-specific answers, while English input more often produces U.S.-specific, comparative, or generic answers. Prompts requiring a single answer further increase jurisdiction selection: pooled across models, 74.5% of English-input responses adopt a U.S. framework, while 53.3% of Chinese-input responses adopt a China framework. This directional pattern appears in all seven models. We describe this deployment-level pattern as institutional-framework misselection risk: a fluent answer may rely on a legal-administrative context the user did not intend, especially when their preferred language differs from the relevant jurisdiction. LLM interfaces should not route institutional advice by input language alone; when location is absent, they should request it or state the jurisdictional scope of the answer.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
