# 🧠 大模型相关研究 | 2026年05月06日

> 本类共 **203** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-203**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-203**

---

### 201. [Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces](https://arxiv.org/abs/2605.02829)

**<font color=#1a73e8>作者：</font>** Jingze Ge, Yun Liu, Xue Geng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence. This decoupled practice first compresses and then fine-tunes adapters, potentially misaligning the compressed subspace with downstream objectives and squandering a global parameter budget. To overcome this limitation, we introduce JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), a single framework that unifies compression and adaptation. From a small calibration set, JACTUS estimates input and pre-activation gradient covariances, forms their orthogonal union with the pretrained weight subspace, performs a projected low-rank approximation inside this union, allocates rank globally by marginal gain per parameter, and trains only a compact core matrix. This explicitly mitigates the potential misalignment between the compressed subspace and downstream objectives by coupling the directions preserved for compression with those required for adaptation, yielding a deployable low-rank model that avoids retaining full frozen weights while enabling fast and robust tuning. On vision, JACTUS attains an average 89.2% accuracy on ViT-Base across eight datasets at 80% retained parameters, surpassing strong 100% PEFT baselines (e.g., DoRA 87.9%). On language, JACTUS achieves an 80.9% average on Llama2-7B commonsense QA at the same 80% retained-parameter budget, outperforming 100% PEFT (e.g., DoRA 79.7%) and exceeding prior compress-then-finetune pipelines under the same ratained-parameter budget. We will release code.

---


### 202. [VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition](https://arxiv.org/abs/2605.02834)

**<font color=#1a73e8>作者：</font>** Tanush Yadav, Mohammadreza Salehi, Jae Sung Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.

---


### 203. [Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection](https://arxiv.org/abs/2605.02860)

**<font color=#1a73e8>作者：</font>** Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels.
To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate.
Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.

---


> [!TIP]
> 当前位于：**201-203**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-203**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
